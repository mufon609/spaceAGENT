#!/usr/bin/env python3
import time, sys
from scripts.sm import call, sc, status_line, wait_idle

route = [
    "node_alpha", "synchrony", "the_experiment", "achernar",
    "garnet", "atlas", "intercrus", "kitalpha", "kepler_442",
    "theemin", "hollowcrest", "alathfar", "sabik", "tidewater",
    "last_light", "unknown_edge", "the_telescope", "first_step",
    "markeb", "beid", "castor"
]

print("=== STARTING CASTOR WORMHOLE EXPEDITION ===")
print("Initial status:", status_line())

# Activate cloak for safety
print("Activating integrated cloak...")
call("spacemolt", "cloak", {})

for i, dest in enumerate(route, 1):
    print(f"\n[{i}/{len(route)}] Jumping to {dest}...")
    r = call("spacemolt", "jump", {"target_system": dest})
    if "error" in r:
        print("Jump error:", r)
        # Check if already there or stuck
        time.sleep(2)
    wait_idle()
    st = status_line()
    print("Arrived:", st)
    
    # Check if we are at a station system where we can refuel safely if fuel is getting low (<40)
    # At last_light (ramens_rest) or unknown_edge (unknown_edge_waystation)
    if dest in ["last_light", "unknown_edge"]:
        print(f"Checking status at {dest}...")

print("\n=== ARRIVED IN CASTOR! ===")
sys_info = sc(call("spacemolt", "get_system", {"system_id": "castor"}))
pois = sys_info.get("pois", [])
print(f"Castor POIs ({len(pois)}):")
for p in pois:
    print(" ", p.get("id"), "|", p.get("name"), "|", p.get("type"), "|", p.get("class"))

