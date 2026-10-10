#!/usr/bin/env python3
from scripts.sm import call, sc, status_line, wait_idle

outbound_route = [
    "node_alpha", "synchrony", "the_experiment", "achernar",
    "garnet", "atlas", "intercrus", "kitalpha", "kepler_442",
    "theemin", "hollowcrest", "merak", "alsciaukat", "errai"
]

print("=== FINISHING AMPLIFICATION MATERIALS SORTIE ===")
print("Initial status:", status_line())

call("spacemolt", "undock", {})
wait_idle()

print("Engaging integrated cloak...")
call("spacemolt", "cloak", {})

for i, dest in enumerate(outbound_route, 1):
    print(f"[{i}/{len(outbound_route)}] Jumping to {dest}...")
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

print("\nArrived in Errai! Traveling to errai_belt...")
call("spacemolt", "travel", {"target_poi": "errai_belt"})
wait_idle()

# Mine until silver count in cargo is 15
silver_count = 13
cycle = 1
while silver_count < 15 and cycle <= 15:
    print(f"\nMining cycle {cycle}...")
    call("spacemolt", "mine", {})
    wait_idle()
    
    cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
    for itm in cargo:
        if itm.get("item_id") == "silver_ore":
            silver_count = itm.get("quantity", 0)
    print(f"Cycle {cycle}: Silver Ore in cargo = {silver_count}/15")
    
    # Jettison filler Fe/Cu
    for itm in cargo:
        iid = itm.get("item_id")
        if iid in ["iron_ore", "copper_ore"]:
            print(f"Jettisoning filler {iid} x{itm.get('quantity')}...")
            call("spacemolt_storage", "jettison", {"item_id": iid, "quantity": itm.get("quantity")})
    cycle += 1

print("\nDisengaging cloak for transit...")
call("spacemolt", "uncloak", {})

# Return via express corridor errai -> fang -> last_light
print("Express return: errai -> fang -> last_light...")
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

# Jump home to nexus_prime
call("spacemolt", "undock", {})
wait_idle()

home_route = [
    "tidewater", "sabik", "alathfar", "hollowcrest", "theemin",
    "kepler_442", "kitalpha", "intercrus", "atlas", "garnet",
    "achernar", "the_experiment", "synchrony", "node_alpha", "nexus_prime"
]

for i, dest in enumerate(home_route, 1):
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()

print("\nArrived in Nexus Prime! Docking at Central Nexus...")
call("spacemolt", "travel", {"target_poi": "the_core"})
wait_idle()
call("spacemolt", "dock", {})
wait_idle()

print("Status at Central Nexus:", status_line())

# Complete mission!
print("Completing Amplification Materials mission...")
res = call("spacemolt", "complete_mission", {"mission_id": "d4312c8a0843775b78df57de8705a5e4"})
print("Completion response:", res)

# Deposit harvested silver ore to storage
cargo = sc(call("spacemolt", "get_cargo")).get("items", [])
for itm in cargo:
    iid = itm.get("item_id")
    if iid != "fuel_cell":
        call("spacemolt_storage", "deposit", {"item_id": iid, "quantity": itm.get("quantity"), "target": "self"})

# Refuel to 110
call("spacemolt", "refuel", {})

print("AMPLIFICATION MATERIALS MISSION FULLY COMPLETE!")
print("Final status:", status_line())
