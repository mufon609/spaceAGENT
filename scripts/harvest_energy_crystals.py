#!/usr/bin/env python3
import time, sys
from scripts.sm import call, sc, status_line, wait_idle

# Outbound route: nexus_prime -> node_alpha -> synchrony -> the_experiment -> achernar -> garnet (5 jumps)
outbound_route = ["node_alpha", "synchrony", "the_experiment", "achernar", "garnet"]

print("=== STARTING ENERGY CRYSTAL SORTIE ===")
print("Initial status:", status_line())

call("spacemolt", "undock", {})
wait_idle()

print("Engaging integrated cloak...")
call("spacemolt", "cloak", {})

for i, dest in enumerate(outbound_route, 1):
    print(f"[{i}/{len(outbound_route)}] Jumping to {dest}...")
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

print("\nArrived in Garnet! Traveling to garnet_dim_lattice...")
call("spacemolt", "travel", {"target_poi": "garnet_dim_lattice"})
wait_idle()

print("Status at garnet_dim_lattice:", status_line())

# Mine until 20 Energy Crystals mined
# Objective requires mining 20 Energy Crystals
crystal_mined = 0
cycle = 1
while crystal_mined < 20 and cycle <= 35:
    print(f"\nMining cycle {cycle}...")
    res = call("spacemolt", "mine", {})
    wait_idle()
    
    cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
    for itm in cargo:
        if itm.get("item_id") == "energy_crystal":
            crystal_mined = itm.get("quantity", 0)
    print(f"Cycle {cycle}: Energy Crystal in hold = {crystal_mined}/20")
    
    # Jettison filler ores (iron, copper) to preserve hold
    for itm in cargo:
        iid = itm.get("item_id")
        if iid in ["iron_ore", "copper_ore", "carbon_ore"]:
            print(f"Jettisoning filler {iid} x{itm.get('quantity')}...")
            call("spacemolt_storage", "jettison", {"item_id": iid, "quantity": itm.get("quantity")})
    cycle += 1

print("\nDisengaging cloak for transit...")
call("spacemolt", "uncloak", {})

# Return route: garnet -> achernar -> the_experiment -> synchrony -> node_alpha -> nexus_prime (5 jumps)
home_route = ["achernar", "the_experiment", "synchrony", "node_alpha", "nexus_prime"]
for i, dest in enumerate(home_route, 1):
    print(f"[{i}/{len(home_route)}] Jumping home to {dest}...")
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

print("\nArrived in Nexus Prime! Docking at Central Nexus...")
call("spacemolt", "travel", {"target_poi": "the_core"})
wait_idle()
call("spacemolt", "dock", {})
wait_idle()

print("Status at Central Nexus:", status_line())

# Complete Crystal Resonance Harvest
print("Completing Crystal Resonance Harvest mission...")
r1 = call("spacemolt", "complete_mission", {"mission_id": "fecdab24f6e581cca4727dfa975a554e"})
print("Completion response 1:", r1)

# Complete The Resonance Chamber
print("Completing The Resonance Chamber mission...")
r2 = call("spacemolt", "complete_mission", {"mission_id": "ab0f6e5968a424a51b1371445dd516f1"})
print("Completion response 2:", r2)

# Deposit remaining crystals to storage
cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
for itm in cargo:
    iid = itm.get("item_id")
    if iid != "fuel_cell":
        call("spacemolt_storage", "deposit", {"item_id": iid, "quantity": itm.get("quantity"), "target": "self"})

# Refuel to 110/110
call("spacemolt", "refuel", {})

print("DOUBLE CRYSTAL MISSION SORTIE COMPLETE!")
print("Final status:", status_line())

