#!/usr/bin/env python3
"""query_station_board.py
Flies Absence cloaked to specified station, docks, queries get_missions, and prints all missions.
"""
import sys
from sm import call, sc, status_line, wait_idle

target_sys = sys.argv[1]
target_poi = sys.argv[2]
base_id = sys.argv[3]

s = wait_idle()
if s.get("location", {}).get("docked_at"):
    call("spacemolt", "undock")

call("spacemolt", "cloak")
call("spacemolt", "jump", {"target_system": target_sys})
call("spacemolt", "travel", {"target_poi": target_poi})
call("spacemolt", "dock", {"base_id": base_id})
res = call("spacemolt", "get_missions")
print(f"=== MISSIONS AT {base_id} ===")
for m in res.get("result", "").split("--- "):
    if not m.strip(): continue
    lines = m.strip().splitlines()
    header = lines[0]
    rw = [l for l in lines if l.startswith("Rewards:")]
    print(header)
    if rw: print(" ", rw[0])

call("spacemolt", "refuel")
call("spacemolt", "undock")
call("spacemolt", "jump", {"target_system": "nexus_prime"})
call("spacemolt", "travel", {"target_poi": "the_core"})
call("spacemolt", "dock", {"base_id": "central_nexus"})
call("spacemolt", "refuel")
print("Returned to Central Nexus.")
