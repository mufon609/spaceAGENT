#!/usr/bin/env python3
import time, sys
from scripts.sm import call, sc, status_line, wait_idle

outbound_route = [
    "node_alpha", "synchrony", "the_experiment", "achernar",
    "garnet", "atlas", "intercrus", "kitalpha", "nembus", "cervantes", "miaplacidus"
]

print("=== FINISHING IRON EXTRACTION LEG ===")
print("Initial status:", status_line())

call("spacemolt", "undock", {})
wait_idle()

print("Engaging integrated cloak...")
call("spacemolt", "cloak", {})

for i, dest in enumerate(outbound_route, 1):
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

print("\nArrived in Miaplacidus! Traveling to miaplacidus_alloy_remnants...")
call("spacemolt", "travel", {"target_poi": "miaplacidus_alloy_remnants"})
wait_idle()

# Need 3 more iron ore mined to hit 10/10
iron_count = 7
cycle = 1
while iron_count < 10 and cycle <= 15:
    call("spacemolt", "mine", {})
    wait_idle()
    
    cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
    for itm in cargo:
        if itm.get("item_id") == "iron_ore":
            iron_count = itm.get("quantity", 0)
    
    # Jettison filler copper
    for itm in cargo:
        iid = itm.get("item_id")
        if iid in ["copper_ore"]:
            call("spacemolt_storage", "jettison", {"item_id": iid, "quantity": itm.get("quantity")})
    cycle += 1

print(f"\nTarget achieved ({iron_count}/10 iron ore)! Disengaging cloak for transit...")
call("spacemolt", "uncloak", {})

home_route = [
    "cervantes", "nembus", "kitalpha", "intercrus", "atlas",
    "garnet", "achernar", "the_experiment", "synchrony", "node_alpha", "nexus_prime"
]

for dest in home_route:
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

print("\nArrived in Nexus Prime! Docking at Central Nexus...")
call("spacemolt", "travel", {"target_poi": "the_core"})
wait_idle()
call("spacemolt", "dock", {})
wait_idle()

print("Status at Central Nexus:", status_line())

# Complete Material Synthesis: Basic mission
print("Completing Material Synthesis: Basic mission...")
res = call("spacemolt", "complete_mission", {"mission_id": "04c2109cb76e5574d87f4bffc7a5542a"})
print("Completion response:", res)

# Deposit harvested iron into storage
cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
for itm in cargo:
    iid = itm.get("item_id")
    if iid != "fuel_cell":
        call("spacemolt_storage", "deposit", {"item_id": iid, "quantity": itm.get("quantity"), "target": "self"})

# Refuel to 110/110
call("spacemolt", "refuel", {})

print("MATERIAL SYNTHESIS MISSION FULLY COMPLETE!")
print("Final status:", status_line())

