#!/usr/bin/env python3
"""sm.py - minimal SpaceMolt HTTP v2 client. Stdlib only. Token-cheap output.

Credentials come from env vars (NEVER commit them):
  export SM_USER='Alien_Abductee_Gemini'  SM_PASS='<password>'
Session id is cached in /tmp/sm_session (30 min idle expiry; auto re-login).
An HTTP session coexists with an MCP session for the same player.

Usage:
  sm.py call <tool> <action> ['{json}']   raw call, prints result text
  sm.py status                            one-line status
  sm.py mine [max_cycles] [min_avg]       mine until cargo full / error / pirates / low yield
  sm.py scout                             1-line POI report: sec, crowd, ores (paste to resources.md)
  sm.py loop <belt_sys> <belt_poi> <home_sys> <station> [trips]
                                          full mine->bank loop; run in background:
                                          nohup python3 -u sm.py loop ... > /tmp/loop.log 2>&1 &
                                          graceful stop after current trip: touch /tmp/sm_stop
                                          abort now + emergency dock:       touch /tmp/sm_emergency
  sm.py preflight                         checklist: battle/transit/hull/fuel/cargo/crew; auto-fix if docked
  sm.py safe [home]                       EMERGENCY DOCK: kill loops, flee battle, nearest known station
                                          (or home), dock. Exit 0 only when docked. Use before PC shutdown.
  sm.py go <poi_id>                       travel within system
  sm.py jump <system_id>                  jump to adjacent system
  sm.py dock | undock
  sm.py dump                              deposit ALL cargo to station storage (must be docked)
  sm.py notes                             drain notifications
  sm.py poi | sys                         current POI resources | system POIs+links
  sm.py route <system_or_poi>             jump path + fuel
  sm.py missions | active                 board missions | my active missions (compact)
  sm.py storage [station_id]              storage here or remote
Tools: spacemolt, spacemolt_storage, spacemolt_market, spacemolt_social, spacemolt_battle,
       spacemolt_catalog(action=catalog)
"""
import json, os, sys, time, urllib.request, urllib.error

API = "https://game.spacemolt.com/api/v2"
SESS_FILE = "/tmp/sm_session"


def _post(path, body=None, sid=None, timeout=900):
    req = urllib.request.Request(API + path, data=json.dumps(body or {}).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    if sid:
        req.add_header("X-Session-Id", sid)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try:
            return json.loads(e.read().decode())
        except Exception:
            return {"error": {"code": "http_%d" % e.code, "message": str(e)}}


def login():
    u, p = os.environ.get("SM_USER"), os.environ.get("SM_PASS")
    if not (u and p):
        sys.exit("set SM_USER and SM_PASS env vars")
    sid = _post("/session")["session"]["id"]
    r = _post("/spacemolt_auth/login", {"username": u, "password": p}, sid)
    if "error" in r:
        sys.exit("login failed: %s" % r["error"])
    open(SESS_FILE, "w").write(sid)
    return sid


def sid():
    if os.path.exists(SESS_FILE):
        return open(SESS_FILE).read().strip()
    return login()


def call(tool, action, body=None):
    r = _post("/%s/%s" % (tool, action), body, sid())
    err = r.get("error") or {}
    if err.get("code") in ("session_invalid", "not_authenticated", "unauthorized"):
        login()
        r = _post("/%s/%s" % (tool, action), body, sid())
    return r


def sc(r):
    return r.get("structuredContent") or {}


def status_line():
    r = call("spacemolt", "get_status")
    if "error" in r:
        return "ERR %s" % r["error"]
    s = sc(r)
    p, sh, lo = s.get("player", {}), s.get("ship", {}), s.get("location", {})
    dock = lo.get("docked_at") or "-"
    return ("cr=%s sys=%s poi=%s docked=%s sec=%s fuel=%s/%s cargo=%s/%s hull=%s/%s" % (
        p.get("credits"), lo.get("system_id"), lo.get("poi_id"), dock,
        (lo.get("security_status") or "?").split(" (")[0], sh.get("fuel"), sh.get("max_fuel"),
        sh.get("cargo_used"), sh.get("cargo_capacity"), sh.get("hull"), sh.get("max_hull")))


def scout():
    """One line per POI: sec, crowd, each ore richness/remaining/supported_power. Paste into resources.md."""
    s = sc(call("spacemolt", "get_status"))
    lo = s.get("location", {})
    n = sc(call("spacemolt", "get_nearby"))
    players = n.get("count", len(n.get("nearby") or []))
    pirates = n.get("pirate_count", 0)
    creatures = n.get("creature_count", 0)
    ores = " ".join("%s:r%s/%s/p%s" % (x.get("item_id", "?").replace("_ore", ""), x.get("richness"),
                    x.get("remaining"), x.get("supported_power", 0)) for x in lo.get("resources", []))
    print("SCOUT %s/%s sec=%s players=%s pirates=%s creatures=%s | %s" % (
        lo.get("system_id"), lo.get("poi_id"), (lo.get("security_status") or "?").split(" (")[0],
        players, pirates, creatures, ores or "no resources"))


def mine(max_cycles=100, min_avg=0.0):
    """min_avg>0: stop when avg yield of last 5 cycles < min_avg. Returns stop reason."""
    tot, recent, why = {}, [], "max_cycles"
    for i in range(1, max_cycles + 1):
        r = call("spacemolt", "mine")
        if "error" in r:
            e = r["error"]
            print("STOP cycle=%d err=%s: %s" % (i, e.get("code"), e.get("message")))
            why = "error"
            break
        s = sc(r)
        d, sh = s.get("details", {}), s.get("ship", {})
        rid, q = d.get("resource_id"), d.get("quantity", 0)
        tot[rid] = tot.get(rid, 0) + q
        recent = (recent + [q])[-5:]
        used, cap = sh.get("cargo_used", 0), sh.get("cargo_capacity", 0)
        print("c%d +%s %s (left %s) cargo %s/%s" % (i, q, rid, d.get("remaining"), used, cap))
        if s.get("location", {}).get("nearby_pirate_count", 0):
            print("STOP pirates nearby")
            why = "danger"
            break
        if sh.get("hull", 1) < sh.get("max_hull", 0):
            print("STOP hull damaged %s/%s" % (sh.get("hull"), sh.get("max_hull")))
            why = "danger"
            break
        if cap and used >= cap - 1:
            print("STOP cargo full")
            why = "full"
            break
        if min_avg and len(recent) == 5 and sum(recent) / 5.0 < min_avg:
            print("STOP low yield avg=%.1f < %s" % (sum(recent) / 5.0, min_avg))
            why = "low_yield"
            break
        if os.path.exists(EMERGENCY):
            print("STOP emergency flag")
            why = "danger"
            break
    print("TOTAL " + " ".join("%s=%s" % kv for kv in tot.items()))
    return why


def dump():
    r = call("spacemolt", "get_cargo")
    items = [{"item_id": c["item_id"], "quantity": c["quantity"]}
             for c in sc(r).get("cargo", []) if c.get("quantity")]
    if not items:
        print("cargo empty")
        return True
    r = call("spacemolt_storage", "deposit", {"items": items})
    print("ERR %s" % r["error"] if "error" in r else "deposited " +
          " ".join("%s=%s" % (i["item_id"], i["quantity"]) for i in items))
    return "error" not in r


# ---------------------------------------------------------------- safety layer
# Known stations where we can dock (add new ones as found). First entry = home.
SAFE_STATIONS = ["central_nexus", "node_beta_industrial_station", "node_alpha_processing_station",
                 "node_gamma_relay_station", "synchrony_hub"]
EMERGENCY = "/tmp/sm_emergency"   # touch -> loops abort now and run safe()
STOPFILE = "/tmp/sm_stop"         # touch -> loops stop after current trip (docked)
MIN_FUEL_PCT = 0.5                # preflight: refuel when docked below this; refuse to undock below 0.3


def wait_idle(max_wait=240):
    """Wait until not in transit and no pending action. Returns status dict."""
    t0 = time.time()
    while True:
        s = sc(call("spacemolt", "get_status"))
        lo, q = s.get("location", {}), s.get("queue", {})
        if not lo.get("in_transit") and not q.get("has_pending"):
            return s
        if time.time() - t0 > max_wait:
            print("WARN still busy after %ss" % max_wait)
            return s
        time.sleep(5)


def step(action, target=None, tries=4):
    """One mutation with retry on busy/in-transit. Returns True on success."""
    for _ in range(tries):
        r = call("spacemolt", action, {"id": target} if target else {})
        code = (r.get("error") or {}).get("code", "")
        if not code:
            return True
        if code in ("action_pending", "in_transit", "rate_limited"):
            wait_idle(120)
            continue
        print("STOP %s %s: %s" % (action, target, short(r)))
        return False
    print("STOP %s %s: retries exhausted" % (action, target))
    return False


def in_battle():
    r = call("spacemolt_battle", "status")
    return "error" not in r


def preflight(require_docked=False):
    """Checklist before leaving: not in battle/transit, hull full, fuel ok, cargo empty.
    Docked: auto-repair, auto-refuel (<MIN_FUEL_PCT), auto-dump cargo. Returns True if clear to fly."""
    s = wait_idle()
    if in_battle():
        print("PREFLIGHT FAIL in battle")
        return False
    sh, lo = s.get("ship", {}), s.get("location", {})
    docked = bool(lo.get("docked_at"))
    if docked:
        if sh.get("hull", 0) < sh.get("max_hull", 0):
            print("preflight repair:", short(call("spacemolt", "repair"))[:100])
        if sh.get("fuel", 0) < MIN_FUEL_PCT * sh.get("max_fuel", 1):
            print("preflight refuel:", short(call("spacemolt", "refuel"))[:100])
        if sh.get("cargo_used", 0) > 0:
            dump()
        s = sc(call("spacemolt", "get_status"))
        sh = s.get("ship", {})
    elif require_docked:
        print("PREFLIGHT FAIL not docked")
        return False
    probs = []
    if sh.get("hull", 0) < sh.get("max_hull", 0):
        probs.append("hull %s/%s" % (sh.get("hull"), sh.get("max_hull")))
    if sh.get("fuel", 0) < 0.3 * sh.get("max_fuel", 1):
        probs.append("fuel %s/%s" % (sh.get("fuel"), sh.get("max_fuel")))
    if docked and sh.get("cargo_used", 0) > 0:
        probs.append("cargo not empty %s" % sh.get("cargo_used"))
    if (sh.get("personnel") or {}).get("fit_crew", 1) < sh.get("minimum_crew", 1):
        probs.append("crew below minimum")
    if probs:
        print("PREFLIGHT FAIL " + "; ".join(probs))
        return False
    print("PREFLIGHT OK hull=%s/%s fuel=%s/%s cargo=%s/%s" % (sh.get("hull"), sh.get("max_hull"),
          sh.get("fuel"), sh.get("max_fuel"), sh.get("cargo_used"), sh.get("cargo_capacity")))
    return True


def kill_other_loops():
    """Kill running sm.py loops except this process (and its parent wrapper)."""
    me = {os.getpid(), os.getppid()}
    for pid in os.popen("pgrep -f 'sm.py loop'").read().split():
        if int(pid) not in me:
            try:
                os.kill(int(pid), 15)
            except OSError:
                pass


def safe(home_only=False):
    """EMERGENCY DOCK: kill loops, wait out transit, flee battle, go to nearest known station, dock."""
    kill_other_loops()
    print("SAFE start", time.strftime("%H:%M:%S"))
    s = wait_idle()
    if in_battle():
        print("in battle -> stance flee")
        call("spacemolt_battle", "stance", {"id": "flee"})
        for _ in range(60):
            time.sleep(10)
            if not in_battle():
                break
        s = wait_idle()
    lo, sh = s.get("location", {}), s.get("ship", {})
    if lo.get("docked_at"):
        print("SAFE already docked at %s" % lo["docked_at"])
        _clear_flags()
        return True
    # 1) station in this system?
    sysd = sc(call("spacemolt", "get_system")).get("system", {})
    here = [p["id"] for p in sysd.get("pois", []) if p.get("type") == "station" or p.get("has_base")]
    if here and not home_only:
        target_poi, path = here[0], []
    else:
        # 2) fewest jumps among known stations (home wins ties)
        best = None
        for st in (SAFE_STATIONS[:1] if home_only else SAFE_STATIONS):
            rt = sc(call("spacemolt", "find_route", {"id": st}))
            if not rt.get("found"):
                continue
            if rt.get("estimated_fuel", 0) > sh.get("fuel", 0):
                print("skip %s: fuel %s > %s" % (st, rt.get("estimated_fuel"), sh.get("fuel")))
                continue
            if best is None or rt["total_jumps"] < best["total_jumps"]:
                best = rt
        if best is None:
            print("SAFE FAIL no reachable station (fuel?). Consider distress_signal fuel.")
            return False
        target_poi = best.get("target_poi")
        path = [x["system_id"] for x in best["route"][1:]]
    print("SAFE route: %s -> %s" % (" > ".join(path) or "same system", target_poi))
    for sysid in path:
        if not step("jump", sysid):
            return False
    cur = wait_idle().get("location", {}).get("poi_id")
    if cur != target_poi and not step("travel", target_poi):
        return False
    if not step("dock"):
        return False
    s = wait_idle()
    ok = bool(s.get("location", {}).get("docked_at"))
    if ok and s.get("ship", {}).get("cargo_used", 0):
        dump()
    print("SAFE %s | %s" % ("DOCKED" if ok else "FAILED", status_line()))
    if ok:
        _clear_flags()
    return ok


def _clear_flags():
    for f in (EMERGENCY, STOPFILE):
        if os.path.exists(f):
            os.remove(f)


def loop(belt_sys, belt_poi, home_sys, station, trips):
    """Repeat: preflight -> belt -> mine till full -> home station -> dock -> dump.
    Any danger/error -> safe() (emergency dock). touch STOPFILE = stop after trip; EMERGENCY = abort now."""
    for t in range(1, trips + 1):
        if os.path.exists(EMERGENCY):
            return safe()
        if not preflight():
            print("trip%d aborted by preflight" % t)
            return safe()
        lo = sc(call("spacemolt", "get_status")).get("location", {})
        if lo.get("system_id") != belt_sys and not step("jump", belt_sys):
            return safe()
        if sc(call("spacemolt", "get_status")).get("location", {}).get("poi_id") != belt_poi:
            if not step("travel", belt_poi):
                return safe()
        print("trip%d %s" % (t, time.strftime("%H:%M:%S")), end=" ")
        scout()
        why = mine(40, 2)
        if why in ("danger", "error"):
            return safe()
        for a, tgt in (("jump", home_sys), ("travel", station), ("dock", None)):
            if not step(a, tgt):
                return safe()
        dump()
        print(status_line())
        if os.path.exists(STOPFILE):
            _clear_flags()
            print("STOP requested via %s (docked)" % STOPFILE)
            return True
    print("LOOP DONE")
    return True


def missions(action):
    r = call("spacemolt", action)
    if "error" in r:
        print(short(r))
        return
    s = sc(r)
    ms = s.get("missions") or []
    if isinstance(ms, dict):
        ms = ms.get("active") or ms.get("available") or []
    for m in ms:
        objs = "; ".join("%s %s/%s" % (o.get("description", ""), o.get("current", ""), o.get("required", ""))
                         if "current" in o else o.get("description", "") for o in m.get("objectives", []))
        rw = m.get("rewards", {})
        print("%s | %s | %s d%s | %scr | %s" % (m.get("mission_id") or m.get("id") or "-", m.get("template_id"),
              m.get("type"), m.get("difficulty"), rw.get("credits"), objs[:200]))
    if not ms:
        print(short(r))


def short(r):
    if "error" in r:
        return "ERR %s: %s" % (r["error"].get("code"), r["error"].get("message"))
    return str(r.get("result", ""))[:1500]


def main(a):
    if not a:
        print(__doc__)
        return
    c = a[0]
    if c == "call":
        body = json.loads(a[3]) if len(a) > 3 else {}
        print(short(call(a[1], a[2], body)))
    elif c == "status":
        print(status_line())
    elif c == "mine":
        mine(int(a[1]) if len(a) > 1 else 100, float(a[2]) if len(a) > 2 else 0.0)
    elif c == "loop":
        loop(a[1], a[2], a[3], a[4], int(a[5]) if len(a) > 5 else 1)
    elif c == "scout":
        scout()
    elif c == "preflight":
        preflight()
    elif c == "safe":
        sys.exit(0 if safe(home_only=(len(a) > 1 and a[1] == "home")) else 1)
    elif c == "go":
        print(short(call("spacemolt", "travel", {"id": a[1]})))
    elif c == "jump":
        print(short(call("spacemolt", "jump", {"id": a[1]})))
    elif c in ("dock", "undock"):
        print(short(call("spacemolt", c)))
    elif c == "dump":
        dump()
    elif c == "notes":
        print(short(call("spacemolt", "get_notifications")))
    elif c == "poi":
        print(short(call("spacemolt", "get_poi")))
    elif c == "sys":
        print(short(call("spacemolt", "get_system")))
    elif c == "route":
        print(short(call("spacemolt", "find_route", {"id": a[1]})))
    elif c == "missions":
        missions("get_missions")
    elif c == "active":
        missions("get_active_missions")
    elif c == "storage":
        body = {"station_id": a[1]} if len(a) > 1 else {}
        print(short(call("spacemolt_storage", "view", body)))
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
