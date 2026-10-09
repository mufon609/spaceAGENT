#!/usr/bin/env python3
"""stackmine.py <keep_ore> [target_units=100] [max_cycles=200]
Mine at the current POI; when the hold is within 6 of full, jettison ONLY iron_ore/copper_ore (worthless filler;
user-approved S3, Q6). Stops at target units of keep_ore, pirates, hull damage, /tmp/sm_emergency, any mine error.
Unattended-safe launch (auto-docks afterwards):
  setsid nohup sh -c 'python3 -u scripts/stackmine.py silicon_ore 40 160 > /tmp/stack.log 2>&1; scripts/safe_dock.sh > /tmp/safe.log 2>&1' < /dev/null > /dev/null 2>&1 &
Proven: zubenelhakrabi_crystal_sand, beam 12, cargo 115: 40 Si per ~100 cycles (~25 min)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm import call, sc

FILLER = ("iron_ore", "copper_ore")
keep = sys.argv[1]
target = int(sys.argv[2]) if len(sys.argv) > 2 else 100
maxc = int(sys.argv[3]) if len(sys.argv) > 3 else 200
have = {}
for i in range(1, maxc + 1):
    r = call("spacemolt", "mine")
    if "error" in r:
        print("STOP err", r["error"].get("code"), r["error"].get("message")); break
    s = sc(r); d = s.get("details", {}); sh = s.get("ship", {})
    rid, q = d.get("resource_id"), d.get("quantity", 0)
    have[rid] = have.get(rid, 0) + q
    used, cap = sh.get("cargo_used", 0), sh.get("cargo_capacity", 0)
    print("c%d +%s %s cargo %s/%s total=%s" % (i, q, rid, used, cap, have.get(keep, 0)))
    if s.get("location", {}).get("nearby_pirate_count", 0) or sh.get("hull", 1) < sh.get("max_hull", 0) or os.path.exists("/tmp/sm_emergency"):
        print("STOP danger"); break
    if have.get(keep, 0) >= target:
        print("STOP target reached"); break
    if cap and used >= cap - 6:
        items = sc(call("spacemolt", "get_status")).get("cargo", []) or []
        done = False
        for it in items:
            if it.get("item_id") in FILLER and it.get("quantity", 0) > 0:
                jr = call("spacemolt", "jettison", {"id": it["item_id"], "quantity": it["quantity"]})
                print("JETTISON", it["item_id"], it["quantity"], "ERR" if "error" in jr else "ok"); done = True
        if not done:
            print("STOP hold full of non-filler"); break
print("TOTAL", have)
