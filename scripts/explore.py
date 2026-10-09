#!/usr/bin/env python3
"""explore.py - scout a path of adjacent systems; record security, stations, every belt/ice/gas field.
Usage (background):  setsid nohup python3 -u explore.py sysA,sysB,sysC [nobelts] [dock] > /tmp/explore.log 2>&1 < /dev/null &
  dock = after scouting, dock at the first station of each system (inspection missions, refuel <70%).
Output: /tmp/explore.log (readable lines) + /tmp/explore.jsonl (one JSON per system; convert with
        `python3 explore.py md` -> markdown rows for resources.md).
Safety: leaves a POI with pirates; safe() on hull damage/battle; fuel guard turns home when fuel < return+8.
Needs SM_USER/SM_PASS. Imports sm.py from the same folder.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm import call, sc, wait_idle, in_battle, safe, step, status_line

def explore(route, belts=True, home="node_beta_industrial_station", dock=False):
    """Scout a path of adjacent systems. Per system: security, stations, POIs; per belt/ice/gas: ores + crowd.
    Pirates at a POI -> leave it at once. Hull damage / battle -> safe(). Fuel guard: turns back when
    fuel < route-home estimate + 8. Appends JSON lines to /tmp/explore.jsonl."""
    out = open("/tmp/explore.jsonl", "a")
    for sysid in route:
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
        if belts:
            for p in pois:
                if p.get("type") not in ("asteroid_belt", "ice_field", "gas_cloud", "nebula"):
                    continue
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
        if dock and rec["stations"]:
            ok = step("travel", rec["stations"][0]) and step("dock")
            print("  DOCK %s %s" % (rec["stations"][0], "ok" if ok else "FAILED"))
            if ok:
                sh = wait_idle().get("ship", {})
                if sh.get("fuel", 0) < 0.7 * sh.get("max_fuel", 1):
                    print("  refuel:", str(call("spacemolt", "refuel").get("result", ""))[:80])
    print("EXPLORE route done |", status_line())
    return True


def to_md():
    for l in open("/tmp/explore.jsonl"):
        r = json.loads(l)
        sec = "LAWLESS" if not r["police"] else "police %s" % r["police"]
        links = ",".join(c.get("system_id", c) if isinstance(c, dict) else c for c in (r["links"] or []))
        print("| %s | %s | %s | %s | %s |" % (r["system"], r["empire"] or "none", sec, ",".join(r["stations"]) or "none", links))
    eqm = {"asteroid_belt": "laser", "ice_field": "ice harvester", "gas_cloud": "gas harvester", "nebula": "laser"}
    for l in open("/tmp/explore.jsonl"):
        r = json.loads(l)
        for b in r["belts"]:
            ores = " ".join("%s r%s/%s/p%s" % (k.replace("_ore", ""), *v) for k, v in b["ores"].items())
            print("| %s | %s | %s | %s | %s | %s |" % (r["system"], b["poi"], "LAWLESS" if not r["police"] else "p%s" % r["police"],
                  eqm.get(b["type"], "?"), b["players"], ores))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "md":
        to_md()
    elif len(sys.argv) > 1:
        opts = sys.argv[2:]
        explore(sys.argv[1].split(","), belts="nobelts" not in opts, dock="dock" in opts)
    else:
        print(__doc__)
