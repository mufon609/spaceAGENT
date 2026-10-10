#!/usr/bin/env python3
import time, sys
from scripts.sm import call, sc, status_line, wait_idle

# Outbound route: nexus_prime -> errai (14 jumps)
outbound_route = [
    "node_alpha", "synchrony", "the_experiment", "achernar",
    "garnet", "atlas", "intercrus", "kitalpha", "kepler_442",
    "theemin", "hollowcrest", "merak", "alsciaukat", "errai"
]

print("=== STARTING AMPLIFICATION MATERIALS (SILVER ORE) SORTIE ===")
print("Initial status:", status_line())

# Undock
call("spacemolt", "undock", {})
wait_idle()

# Activate cloak
print("Engaging integrated cloak...")
call("spacemolt", "cloak", {})

for i, dest in enumerate(outbound_route, 1):
    print(f"[{i}/{len(outbound_route)}] Jumping to {dest}...")
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

print("\nArrived in Errai! Traveling to errai_belt...")
call("spacemolt", "travel", {"target_poi": "errai_belt"})
wait_idle()

print("Status at errai_belt:", status_line())

# Mine until 15 Silver Ore is collected
silver_count = 0
cycle = 1
while silver_count < 15 and cycle <= 30:
    print(f"\nMining cycle {cycle}...")
    r = call("spacemolt", "mine", {})
    wait_idle()
    
    cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
    for itm in cargo:
        if itm.get("item_id") == "silver_ore":
            silver_count = itm.get("quantity", 0)
    print(f"Cycle {cycle}: Silver Ore in cargo = {silver_count}/15")
    
    # If hold gets full with filler iron/copper, jettison them (retaining silver and fuel cells)
    for itm in cargo:
        iid = itm.get("item_id")
        if iid in ["iron_ore", "copper_ore"]:
            print(f"Jettisoning filler {iid} x{itm.get('quantity')}...")
            call("spacemolt_storage", "jettison", {"item_id": iid, "quantity": itm.get("quantity")})
    
    cycle += 1

print(f"\nHarvest target reached ({silver_count}/15 silver ore)!")

# Disengage cloak to save fuel during transit
call("spacemolt", "uncloak", {})

# Quick return route: errai -> fang -> last_light (refuel at ramens_rest)
print("\nTaking express corridor to Ramen's Rest: errai -> fang -> last_light...")
call("spacemolt", "jump", {"target_system": "fang"})
wait_idle()
call("spacemolt", "jump", {"target_system": "last_light"})
wait_idle()

call("spacemolt", "travel", {"target_poi": "ramens_rest"})
wait_idle()
call("spacemolt", "dock", {})
wait_idle()
print("Refueling at Ramen's Rest...")
call("spacemolt", "refuel", {})
print("Refueled at Ramen's Rest:", status_line())

# Undock from Ramen's Rest and jump home
call("spacemolt", "undock", {})
wait_idle()

home_route = [
    "tidewater", "sabik", "alathfar", "hollowcrest", "theemin",
    "kepler_442", "kitalpha", "intercrus", "atlas", "garnet",
    "achernar", "the_experiment", "synchrony", "node_alpha", "nexus_prime"
]

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

# Complete Amplification Materials mission
print("Completing Amplification Materials mission...")
res = call("spacemolt", "complete_mission", {"mission_id": "d4312c8a0843775b78df57de8705a5e4"})
print("Completion response:", res)

# Deposit harvested silver ore into station storage (keep 2 fuel cells)
cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
for itm in cargo:
    iid = itm.get("item_id")
    if iid != "fuel_cell":
        print(f"Depositing {iid} x{itm.get('quantity')} to storage...")
        call("spacemolt_storage", "deposit", {"item_id": iid, "quantity": itm.get("quantity"), "target": "self"})

# Refuel to 110/110
call("spacemolt", "refuel", {})

print("MISSION SORTIE COMPLETE!")
print("Final status:", status_line())

