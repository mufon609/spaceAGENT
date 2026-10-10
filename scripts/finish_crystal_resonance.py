#!/usr/bin/env python3
import time, sys
from scripts.sm import call, sc, status_line, wait_idle

outbound_route = ["node_alpha", "synchrony", "the_experiment", "achernar", "garnet"]

print("=== STARTING FINAL CRYSTAL HARVEST LEG ===")
print("Initial status:", status_line())

call("spacemolt", "undock", {})
wait_idle()

print("Engaging integrated cloak...")
call("spacemolt", "cloak", {})

for i, dest in enumerate(outbound_route, 1):
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

print("\nArrived in Garnet! Traveling to garnet_dim_lattice...")
call("spacemolt", "travel", {"target_poi": "garnet_dim_lattice"})
wait_idle()

# Need 6 more crystals mined to reach 20/20
crystal_count = 4
cycle = 1
while crystal_count < 10 and cycle <= 60:
    call("spacemolt", "mine", {})
    wait_idle()
    
    cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
    for itm in cargo:
        if itm.get("item_id") == "energy_crystal":
            crystal_count = itm.get("quantity", 0)
    
    # Jettison filler ores
    for itm in cargo:
        iid = itm.get("item_id")
        if iid in ["iron_ore", "copper_ore", "carbon_ore"]:
            call("spacemolt_storage", "jettison", {"item_id": iid, "quantity": itm.get("quantity")})
    cycle += 1

print(f"\nFinal harvest target reached: {crystal_count} in cargo!")
call("spacemolt", "uncloak", {})

home_route = ["achernar", "the_experiment", "synchrony", "node_alpha", "nexus_prime"]
for dest in home_route:
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

call("spacemolt", "travel", {"target_poi": "the_core"})
wait_idle()
call("spacemolt", "dock", {})
wait_idle()

print("Status at Central Nexus:", status_line())

# Complete Crystal Resonance Harvest
print("Completing Crystal Resonance Harvest mission...")
r1 = call("spacemolt", "complete_mission", {"mission_id": "fecdab24f6e581cca4727dfa975a554e"})
print("Completion response:", r1)

# Deposit remaining crystals to storage (preserving fuel cells)
cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
for itm in cargo:
    iid = itm.get("item_id")
    if iid != "fuel_cell":
        call("spacemolt_storage", "deposit", {"item_id": iid, "quantity": itm.get("quantity"), "target": "self"})

# Refuel to 110/110
call("spacemolt", "refuel", {})

print("CRYSTAL RESONANCE HARVEST MISSION COMPLETED!")
print("Final status:", status_line())

