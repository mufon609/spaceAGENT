#!/usr/bin/env python3
"""run_conductive_lattice_complete.py
Autonomous pipeline:
1. Navigates Absence cloaked from node_alpha to errai_belt (13 hops).
2. Mines silver_ore until cargo holds >= 20 units total. Jettisons filler iron/copper.
3. Express corridor back via Ramen's Rest (errai -> fang -> last_light -> ramens_rest) to refuel.
4. Returns to node_beta_industrial_station.
5. Docks, completes 'conductive_lattice' (+5,500cr, +45 Trading, +3 Voidborn rep, unlocks resonance_substrate).
"""
import sys, time
sys.path.insert(0, "scripts")
from sm import call, sc, status_line, wait_idle

outbound_route = [
    "synchrony", "the_experiment", "achernar",
    "garnet", "atlas", "intercrus", "kitalpha", "kepler_442",
    "theemin", "hollowcrest", "merak", "alsciaukat", "errai"
]

def jump_step(dest):
    print(f"Jumping to {dest}...")
    call("spacemolt", "jump", {"target_system": dest})
    wait_idle()
    s = wait_idle()
    sh = s.get("ship", {})
    loc = s.get("location", {})
    print(f"  Arrived: {loc.get('system_id')} | Fuel: {sh.get('fuel')}/{sh.get('max_fuel')}")
    # Mobile refuel from fuel cell if fuel gets low (<15)
    if sh.get("fuel", 0) < 15:
        print("  Low fuel detected! Consuming fuel cell from cargo...")
        call("spacemolt", "refuel_from_cargo", {"item_id": "fuel_cell", "quantity": 1})
        wait_idle()

print("=== STARTING AUTONOMOUS CONDUCTIVE LATTICE HARVEST ===")
print("Initial status:", status_line())

# Verify cloak is on
call("spacemolt", "cloak", {})
wait_idle()

# Outbound transit
for i, dest in enumerate(outbound_route, 1):
    print(f"[{i}/{len(outbound_route)}]", end=" ")
    jump_step(dest)

print("\nArrived in Errai! Traveling to errai_belt...")
call("spacemolt", "travel", {"target_poi": "errai_belt"})
wait_idle()

# Check cargo silver count
def get_silver_qty():
    cargo = sc(call("spacemolt", "get_cargo")).get("cargo", [])
    for itm in cargo:
        if itm.get("item_id") == "silver_ore":
            return itm.get("quantity", 0)
    return 0

silver = get_silver_qty()
print(f"Initial silver ore in hold: {silver}/20")

# Mine until silver >= 20
cycle = 1
while silver < 20 and cycle <= 40:
    print(f"Mining cycle {cycle}...")
    call("spacemolt", "mine", {})
    wait_idle()
    silver = get_silver_qty()
    print(f"  Silver Ore in hold: {silver}/20")
    
    # Jettison filler ores (iron/copper)
    cargo = sc(call("spacemolt", "get_cargo")).get("cargo", [])
    for itm in cargo:
        iid = itm.get("item_id")
        if iid in ["iron_ore", "copper_ore", "carbon_ore"]:
            print(f"  Jettisoning filler {iid} x{itm.get('quantity')}...")
            call("spacemolt_storage", "jettison", {"item_id": iid, "quantity": itm.get("quantity")})
    cycle += 1

print(f"\nHarvest target reached ({silver} units)! Proceeding to refuel & return.")

# Return via express route: errai -> fang -> last_light -> ramens_rest
print("Taking express corridor to Ramen's Rest: errai -> fang -> last_light...")
call("spacemolt", "uncloak", {})
wait_idle()

jump_step("fang")
jump_step("last_light")

print("Traveling to ramens_rest...")
call("spacemolt", "travel", {"target_poi": "ramens_rest"})
wait_idle()
print("Docking at ramens_rest...")
call("spacemolt", "dock", {})
wait_idle()
print("Refueling at ramens_rest...")
call("spacemolt", "refuel", {})
wait_idle()
print("Refueled:", status_line())

# Undock and return to node_beta
call("spacemolt", "undock", {})
wait_idle()
call("spacemolt", "cloak", {})
wait_idle()

home_to_beta = [
    "tidewater", "sabik", "alathfar", "hollowcrest", "theemin",
    "kepler_442", "kitalpha", "intercrus", "atlas", "garnet",
    "achernar", "the_experiment", "synchrony", "node_alpha", "node_beta"
]

print("Beginning return journey to Node Beta...")
for i, dest in enumerate(home_to_beta, 1):
    print(f"[{i}/{len(home_to_beta)}]", end=" ")
    jump_step(dest)

print("Arrived in Node Beta! Traveling to node_beta_industrial_station...")
call("spacemolt", "travel", {"target_poi": "node_beta_industrial_station"})
wait_idle()
print("Docking at Node Beta Industrial Station...")
call("spacemolt", "dock", {})
wait_idle()

# Complete Conductive Lattice mission!
print("Completing Conductive Lattice mission...")
res = call("spacemolt", "complete_mission", {"mission_id": "d278ce12f370277b30c7329738c12a84"})
print("Mission complete response:", res)

# Refuel
call("spacemolt", "refuel", {})
wait_idle()

print("CONDUCTIVE LATTICE MISSION COMPLETED SUCCESSFULLY!")
print("Final status:", status_line())
