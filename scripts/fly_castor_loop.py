#!/usr/bin/env python3
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm import call, sc, wait_idle, in_battle, safe, status_line, step

def refuel_if_station():
    s = sc(call("spacemolt", "get_system"))
    for p in s.get("pois", []):
        if p.get("type") == "station":
            print(f"Refueling stop at station {p['id']}...")
            step("travel", p["id"])
            step("dock")
            call("spacemolt", "refuel")
            step("undock")
            break

# Leg 1: izar -> tidewater -> last_light
print("Starting flight to Castor. Jumping to tidewater...")
step("jump", "tidewater")
print(status_line())

print("Jumping to last_light...")
step("jump", "last_light")
print(status_line())
refuel_if_station() # refuel at ramens_rest

# Leg 2: last_light -> unknown_edge -> the_telescope -> first_step
print("Jumping to unknown_edge...")
step("jump", "unknown_edge")
print(status_line())
refuel_if_station() # refuel at unknown_edge_waystation

print("Jumping to the_telescope (uncharted)...")
step("jump", "the_telescope")
print(status_line())

print("Jumping to first_step (uncharted)...")
step("jump", "first_step")
print(status_line())
refuel_if_station() # refuel at first_step_memorial_station

# Leg 3: first_step -> void_gate -> haedus -> castor
print("Jumping to void_gate...")
step("jump", "void_gate")
print(status_line())
refuel_if_station() # refuel at void_gate_outpost

print("Jumping to haedus...")
step("jump", "haedus")
print(status_line())

print("Jumping to castor (MISSION DESTINATION)...")
step("jump", "castor")
print(status_line())

print("Arrived in Castor! Scanning system...")
sys_info = sc(call("spacemolt", "get_system"))
pois = sys_info.get("pois", [])
print("Castor POIs:", [(p.get("id"), p.get("type")) for p in pois])

for p in pois:
    if p.get("type") in ("wormhole", "anomaly", "relic") or "wormhole" in p.get("id", "").lower():
        print(f"Found target wormhole POI {p['id']}! Traveling...")
        step("travel", p["id"])
        break

print("MISSION PROGRESS:")
call("spacemolt", "get_active_missions")
