#!/usr/bin/env python3
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm import call, sc, wait_idle, in_battle, safe, status_line, step

route = [
    "frontier", "altais", "unknown_edge", "last_light",
    "tidewater", "sabik", "alathfar", "hollowcrest",
    "theemin", "kepler_442", "kitalpha", "intercrus",
    "atlas", "garnet", "achernar", "the_experiment",
    "synchrony", "node_alpha", "nexus_prime"
]

print("Starting route to nexus_prime...")
for sys_id in route:
    s = wait_idle(120)
    if in_battle():
        print("IN BATTLE - ABORTING ROUTE")
        safe()
        sys.exit(1)
    sh = s.get("ship", {})
    if sh.get("hull", 0) < sh.get("max_hull", 0):
        print("HULL DAMAGED - ABORTING ROUTE")
        safe()
        sys.exit(1)
    fuel = sh.get("fuel", 0)
    if fuel < 5:
        print(f"LOW FUEL ({fuel}) - ABORTING ROUTE")
        safe()
        sys.exit(1)
    print(f"Jumping to {sys_id} (fuel={fuel})...")
    ok = step("jump", sys_id)
    if not ok:
        print(f"Failed to jump to {sys_id}")
        sys.exit(1)
    print(status_line())

print("Arrived in nexus_prime! Finding central_nexus POI...")
st = sc(call("spacemolt", "get_system"))
pois = [p["id"] for p in st.get("pois", []) if "central" in p["id"] or "nexus" in p["id"] or p.get("type") == "station"]
target_poi = "central_nexus"
if "central_nexus" in pois:
    target_poi = "central_nexus"
elif pois:
    target_poi = pois[0]

print(f"Traveling to {target_poi}...")
step("travel", target_poi)
print(f"Docking at {target_poi}...")
step("dock")
print("ROUTE COMPLETE:", status_line())
