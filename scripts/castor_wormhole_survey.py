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

print("=== STARTING CASTOR SURVEY RUN WITH SURVEY SCANNER I ===")
print("Initial status:", status_line())

call("spacemolt", "undock", {})
wait_idle()

print("Engaging integrated cloak...")
call("spacemolt", "cloak", {})

for i, dest in enumerate(route, 1):
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

print("\nArrived in Castor! Running survey_system...")
res = call("spacemolt", "survey_system", {})
print("Survey system response:", res)

# Check POIs in Castor after survey
sys_info = sc(call("spacemolt", "get_system", {"system_id": "castor"}))
pois = sys_info.get("pois", [])
print(f"Castor POIs now ({len(pois)}):")
for p in pois:
    print(" ", p.get("id"), "|", p.get("name"), "|", p.get("type"), "| class:", p.get("class"))

# Look for any wormhole or deep core POI
target_poi = None
for p in pois:
    if "wormhole" in str(p).lower() or p.get("type") in ["wormhole", "anomaly", "deep_core"]:
        target_poi = p.get("id")
        print("Found target anomaly POI:", p)
        break

if target_poi:
    print(f"Traveling to {target_poi}...")
    call("spacemolt", "travel", {"target_poi": target_poi})
    wait_idle()
    # Check if we can traverse wormhole
    print("Attempting wormhole traversal...")
    # Check what actions are available or if jump works through it
    r_trv = call("spacemolt", "travel", {"target_poi": target_poi})
    print("Action result:", r_trv)

print("\nChecking active mission progress:")
print(sc(call("spacemolt", "get_active_missions")).get("missions", []))

# Return via express corridor to Ramen's Rest to refuel
print("\nReturning: castor -> beid -> markeb -> first_step -> the_telescope -> unknown_edge -> last_light...")
return_route = ["beid", "markeb", "first_step", "the_telescope", "unknown_edge", "last_light"]
for dest in return_route:
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

call("spacemolt", "travel", {"target_poi": "ramens_rest"})
wait_idle()
call("spacemolt", "dock", {})
wait_idle()
call("spacemolt", "refuel", {})
print("Refueled at Ramen's Rest:", status_line())

# Jump home to nexus_prime
call("spacemolt", "undock", {})
wait_idle()

home_corridor = [
    "tidewater", "sabik", "alathfar", "hollowcrest", "theemin",
    "kepler_442", "kitalpha", "intercrus", "atlas", "garnet",
    "achernar", "the_experiment", "synchrony", "node_alpha", "nexus_prime"
]

for dest in home_corridor:
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

call("spacemolt", "travel", {"target_poi": "the_core"})
wait_idle()
call("spacemolt", "dock", {})
wait_idle()
call("spacemolt", "refuel", {})

print("Safely docked at Central Nexus! Status:", status_line())

