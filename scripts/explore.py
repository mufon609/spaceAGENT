#!/usr/bin/env python3
"""explore.py - scout a path of adjacent systems; record security, stations, every resource POI.
Usage (background):  setsid nohup sh -c "python3 -u scripts/explore.py 'sysA,!sysB,sysC' [nobelts] [dock] > /tmp/explore.log 2>&1; scripts/safe_dock.sh" < /dev/null > /dev/null 2>&1 &
  dock = after scouting, dock at the first station of each system (inspection missions, refuel <70%).
  !sys = jump through but skip belt scan for that system. Without `dock` the ship ends in space: chain safe_dock.sh.
Output: /tmp/explore.log + /tmp/explore.jsonl (raw) AND data/systems.tsv + data/belts.tsv are UPSERTED live (keeps manual verdicts);
        commit those two files at checkpoints. Query with scripts/res.py.
Safety: leaves a POI with pirates; safe() on hull damage/battle; fuel guard turns home when fuel < return+8 (home default node_beta).
Needs SM_USER/SM_PASS. Imports sm.py from the same folder. Dies silently if the agent tool call is interrupted: check pgrep -f explore.py.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm import call, sc, wait_idle, in_battle, safe, step, status_line

DATA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


def _tick():
    try:
        import urllib.request
        return json.loads(urllib.request.urlopen("https://game.spacemolt.com/health", timeout=8).read().decode()).get("tick")
    except Exception:
        return "?"


def _load(name):
    p = os.path.join(DATA, name); d = {}
    if os.path.exists(p):
        for l in open(p):
            if l.startswith("#") or not l.strip():
                continue
            c = l.rstrip("\n").split("\t"); d[tuple(c[:2]) if name == "belts.tsv" else c[0]] = c
    return d


def _save(name, hdr, d):
    os.makedirs(DATA, exist_ok=True)
    open(os.path.join(DATA, name), "w").write(hdr + "\n".join("\t".join(v) for _, v in sorted(d.items())) + "\n")


def upsert(rec, tick):
    """Merge one explored system into data/systems.tsv and data/belts.tsv (keeps manual verdicts)."""
    S = _load("systems.tsv"); B = _load("belts.tsv")
    lk = ",".join(c.get("system_id", c) if isinstance(c, dict) else c for c in (rec.get("links") or []))
    S[rec["system"]] = [rec["system"], rec.get("empire") or "none", str(rec.get("police") or 0), ";".join(rec.get("stations") or []) or "none", lk]
    for b in rec.get("belts", []):
        ores = " ".join("%s r%s/%s/p%s" % (k.replace("_ore", ""), *v) for k, v in b["ores"].items())
        old = B.get((rec["system"], b["poi"]))
        B[(rec["system"], b["poi"])] = [rec["system"], b["poi"], str(rec.get("police") or 0), b.get("type", ""), str(b.get("players")), "t%s: %s" % (tick, ores), old[6] if old and len(old) > 6 else ""]
    _save("systems.tsv", "# id\tempire\tpolice(0=lawless)\tstations(;)\tlinks(,)\n", S)
    _save("belts.tsv", "# system\tpoi\tpolice\tequip/type\tplayers\tlast_seen(ore r<richness>/<remaining>/p<supported_power>)\tverdict\n", B)


def explore(route, belts=True, home="node_beta_industrial_station", dock=False):
    """Scout a path of adjacent systems. Per system: security, stations, POIs; per resource POI: ores + crowd.
    Pirates at a POI -> leave it at once. Hull damage / battle -> safe(). Fuel guard: turns back when
    fuel < route-home estimate + 8. Appends JSON lines to /tmp/explore.jsonl and upserts data/*.tsv."""
    out = open("/tmp/explore.jsonl", "a")
    for sysid in route:
        scan = belts and not sysid.startswith("!")
        sysid = sysid.lstrip("!")
        s = wait_idle()
        sh = s.get("ship", {})
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("EXPLORE danger before jump -> safe")
            return safe()
        back = sc(call("spacemolt", "find_route", {"id": home})).get("estimated_fuel", 0)
        if sh.get("fuel", 0) < back + 8:
            print("EXPLORE fuel guard: fuel %s, home needs %s -> safe home" % (sh.get("fuel"), back))
            return safe(home_only=True)
        if s.get("location", {}).get("system_id") != sysid and not step("jump", sysid):
            return safe()
        sysd = sc(call("spacemolt", "get_system")).get("system", {})
        pois = sysd.get("pois", [])
        rec = {"tick": None, "system": sysid, "empire": sysd.get("empire"), "police": sysd.get("police_level"),
               "security": sysd.get("security_status"), "links": sysd.get("connections"),
               "stations": [p["id"] for p in pois if p.get("type") == "station" or p.get("has_base")],
               "pois": ["%s:%s" % (p["id"], p.get("type")) for p in pois], "belts": []}
        tag = "LAWLESS" if not sysd.get("police_level") else "police=%s" % sysd.get("police_level")
        print("SYS %s %s empire=%s stations=%s links=%s" % (sysid, tag, sysd.get("empire"), rec["stations"],
              [c.get("system_id", c) if isinstance(c, dict) else c for c in (sysd.get("connections") or [])]))
        if scan:
            for p in pois:
                if p.get("type") in ("sun", "planet", "station", "relic", "wormhole", "jump_gate") or p.get("has_base"):
                    continue  # scan every other POI type (belts, ice, gas, nebula, crystal sand, ...)
                if not step("travel", p["id"]):
                    return safe()
                st = wait_idle()
                lo, sh = st.get("location", {}), st.get("ship", {})
                n = sc(call("spacemolt", "get_nearby"))
                ores = {x.get("item_id"): [x.get("richness"), x.get("remaining"), x.get("supported_power", 0)]
                        for x in lo.get("resources", [])}
                b = {"poi": p["id"], "type": p.get("type"), "players": n.get("count"),
                     "pirates": n.get("pirate_count", 0), "creatures": n.get("creature_count", 0), "ores": ores}
                rec["belts"].append(b)
                print("  BELT %s %s players=%s pirates=%s | %s" % (p["id"], p.get("type"), b["players"],
                      b["pirates"], " ".join("%s:r%s/%s/p%s" % (k.replace("_ore", ""), *v) for k, v in ores.items())))
                if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
                    print("EXPLORE attacked -> safe")
                    out.write(json.dumps(rec) + "\n")
                    return safe()
                if b["pirates"]:
                    print("  pirates here -> skip rest of system")
                    break
        out.write(json.dumps(rec) + "\n")
        out.flush()
        upsert(rec, _tick())
        if dock and rec["stations"]:
            ok = step("travel", rec["stations"][0]) and step("dock")
            print("  DOCK %s %s" % (rec["stations"][0], "ok" if ok else "FAILED"))
            if ok:
                sh = wait_idle().get("ship", {})
                if sh.get("fuel", 0) < 0.7 * sh.get("max_fuel", 1):
                    print("  refuel:", str(call("spacemolt", "refuel").get("result", ""))[:80])
    print("EXPLORE route done |", status_line())
    return True


if __name__ == "__main__":
    if len(sys.argv) > 1:
        opts = sys.argv[2:]
        explore(sys.argv[1].split(","), belts="nobelts" not in opts, dock="dock" in opts)
    else:
        print(__doc__)
