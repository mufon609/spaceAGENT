#!/usr/bin/env python3
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm import call, sc, wait_idle, in_battle, safe, status_line, step

route = [
    "node_alpha", "synchrony", "the_experiment", "achernar",
    "garnet", "atlas", "intercrus", "kitalpha",
    "lacaille_8760", "theemin", "hollowcrest", "alathfar",
    "izar", "tidewater", "last_light", "unknown_edge",
    "the_telescope", "first_step", "void_gate", "haedus", "castor"
]

print("Engaging expedition flight to Castor on the Absence...")
for sys_id in route:
    s = wait_idle(120)
    if in_battle():
        print("IN BATTLE - EVADING")
        safe()
        sys.exit(1)
    sh = s.get("ship", {})
    if sh.get("hull", 0) < sh.get("max_hull", 0):
        print("HULL DAMAGED - EMERGENCY SAFE DOCK")
        safe()
        sys.exit(1)
    fuel = sh.get("fuel", 0)
    if fuel < 10:
        print(f"LOW FUEL ({fuel}) - STOPPING TO REFUEL")
        safe()
        sys.exit(1)
    print(f"Jumping to {sys_id} (fuel={fuel})...")
    ok = step("jump", sys_id)
    if not ok:
        print(f"Failed to jump to {sys_id}")
        sys.exit(1)
    print(status_line())

print("Arrived in Castor! Scanning system for wormhole and POIs...")
st = sc(call("spacemolt", "get_system"))
print("Castor POIs:", [p["id"] for p in st.get("pois", [])])
