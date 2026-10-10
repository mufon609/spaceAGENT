#!/usr/bin/env python3
import time, sys
from scripts.sm import call, sc, status_line, wait_idle

# Accept material_synthesis_basic
acc = call("spacemolt", "accept_mission", {"template_id": "material_synthesis_basic"})
print("Accept mission:", acc)

# Outbound route to miaplacidus: 11 jumps
outbound_route = [
    "node_alpha", "synchrony", "the_experiment", "achernar",
    "garnet", "atlas", "intercrus", "kitalpha", "nembus", "cervantes", "miaplacidus"
]

print("=== STARTING MATERIAL SYNTHESIS: BASIC (IRON/STEEL) SORTIE ===")
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

# Mine until 10 iron ore mined
iron_mined = 0
cycle = 1
while iron_mined < 10 and cycle <= 20:
    call("spacemolt", "mine", {})
    wait_idle()
    
    cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
    for itm in cargo:
        if itm.get("item_id") == "iron_ore":
            iron_mined = itm.get("quantity", 0)
    print(f"Cycle {cycle}: Iron Ore in hold = {iron_mined}/10")
    
    # Jettison filler copper
    for itm in cargo:
        iid = itm.get("item_id")
        if iid in ["copper_ore"]:
            call("spacemolt_storage", "jettison", {"item_id": iid, "quantity": itm.get("quantity")})
    cycle += 1

print(f"\nIron harvest target reached ({iron_mined}/10)! Disengaging cloak for transit...")
call("spacemolt", "uncloak", {})

# Return home
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

# Complete mission!
print("Completing Material Synthesis: Basic mission...")
res = call("spacemolt", "complete_mission", {"mission_id": acc.get("structuredContent", {}).get("mission", {}).get("mission_id", "")})
print("Completion response:", res)

# Deposit harvested iron into storage
cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
for itm in cargo:
    iid = itm.get("item_id")
    if iid != "fuel_cell":
        call("spacemolt_storage", "deposit", {"item_id": iid, "quantity": itm.get("quantity"), "target": "self"})

# Refuel to 110/110
call("spacemolt", "refuel", {})

print("MATERIAL SYNTHESIS SORTIE COMPLETE!")
print("Final status:", status_line())

