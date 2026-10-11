#!/usr/bin/env python3
"""goldcrest_to_home.py
Flies Absence cloaked from goldcrest through the 7-jump return vector:
goldcrest -> lhs_1140 -> antares -> gsc_0041 -> pherkad -> synchrony -> node_alpha -> nexus_prime.
Docks at central_nexus, turns in mission wh_intro_voidborn_37a7a6e8, and refuels.
"""
import sys, time
from sm import call, sc, status_line, wait_idle, safe, in_battle

ROUTE = ['lhs_1140', 'antares', 'gsc_0041', 'pherkad', 'synchrony', 'node_alpha', 'nexus_prime']

def check_and_cloak():
    s = wait_idle()
    pl = s.get("player", {})
    if not pl.get("is_cloaked", False):
        print("Activating cloak...")
        call("spacemolt", "cloak")

def main():
    print("=== STARTING CLOAKED RETURN SORTIE TO CENTRAL NEXUS ===")
    check_and_cloak()
    
    for hop in ROUTE:
        s = wait_idle()
        sh = s.get("ship", {})
        fuel = sh.get("fuel", 0)
        loc = s.get("location", {})
        print(f"At {loc.get('system_id')} | Fuel: {fuel}/{sh.get('max_fuel')} | Jumping to {hop}")
        
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("ALERT: Battle or damage! Calling safe()")
            safe()
            sys.exit(1)
            
        call("spacemolt", "jump", {"target_system": hop})
        check_and_cloak()

    print("\n--- Arrived in nexus_prime! Docking at central_nexus ---")
    call("spacemolt", "travel", {"target_poi": "the_core"})
    call("spacemolt", "dock", {"base_id": "central_nexus"})
    call("spacemolt", "refuel")
    
    print("\n--- Turning in Anomalous Readings mission ---")
    r_turnin = call("spacemolt", "complete_mission", {"mission_id": "wh_intro_voidborn_37a7a6e8"})
    print("Complete mission result:", r_turnin.get("result"))
    
    s = wait_idle()
    print("ALL DONE. Final status:", status_line())

if __name__ == "__main__":
    main()
