#!/usr/bin/env python3
"""castor_wormhole_survey_leg2.py
Continues from ramens_rest (last_light).
Undocks, cloaks, transits to beid, cocibolca, and driftwood.
Surveys all three systems for wormholes.
"""
import sys, time
from sm import call, sc, status_line, wait_idle, safe, in_battle

def check_and_cloak():
    s = wait_idle()
    pl = s.get("player", {})
    if not pl.get("is_cloaked", False):
        print("Activating cloak...")
        call("spacemolt", "cloak")

def check_fuel_and_refuel():
    s = wait_idle()
    sh = s.get("ship", {})
    fuel = sh.get("fuel", 0)
    print(f"[FUEL CHECK] Current fuel: {fuel}/{sh.get('max_fuel', 110)}")
    if fuel < 25:
        print("[FUEL ALERT] Fuel < 25! Attempting in-space refuel from fuel_cell...")
        r = call("spacemolt", "refuel")
        print("In-space refuel result:", r)
        s = wait_idle()
        print("New fuel:", s.get("ship", {}).get("fuel"))

def fly_hops(route):
    for hop in route:
        s = wait_idle()
        sh = s.get("ship", {})
        fuel = sh.get("fuel", 0)
        loc = s.get("location", {})
        print(f"Current: {loc.get('system_id')} | Fuel: {fuel}/{sh.get('max_fuel')} | Jumping to {hop}")
        
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("ALERT: Battle or damage! Calling safe()")
            safe()
            sys.exit(1)
            
        check_fuel_and_refuel()
        call("spacemolt", "jump", {"target_system": hop})
        check_and_cloak()

def survey_curr_system():
    s = wait_idle()
    loc = s.get("location", {})
    sys_id = loc.get("system_id")
    print(f"\n--- Surveying system {sys_id} ---")
    r = call("spacemolt", "survey_system")
    print("Survey result:", r.get("result"))
    return r

def main():
    print("=== STARTING CASTOR CLUSTER WORMHOLE SURVEY (LEG 2) ===")
    s = wait_idle()
    loc = s.get("location", {})
    cur_sys = loc.get("system_id")
    docked = loc.get("docked_at")
    print(f"Starting at {cur_sys}, docked={docked}")
    
    if docked:
        print("Undocking from", docked)
        call("spacemolt", "undock")
    
    check_and_cloak()
    
    print("\n--- Transit from last_light to beid ---")
    fly_hops(['unknown_edge', 'the_telescope', 'first_step', 'markeb', 'beid'])
    
    # Survey Beid
    survey_curr_system()
    
    # Jump to Cocibolca and survey
    print("\n--- Jumping to cocibolca ---")
    fly_hops(['cocibolca'])
    survey_curr_system()
    
    # Jump to Driftwood and survey
    print("\n--- Jumping to driftwood ---")
    fly_hops(['driftwood'])
    survey_curr_system()
    
    print("\n--- Returning to first_step (memorial station) to safe dock and refuel ---")
    fly_hops(['cocibolca', 'beid', 'markeb', 'first_step'])
    call("spacemolt", "travel", {"target_poi": "first_step_memorial_station"})
    call("spacemolt", "dock", {"base_id": "first_step_memorial_station"})
    call("spacemolt", "refuel")
    print("SAFELY DOCKED AT first_step_memorial_station. Fuel refueled.")

if __name__ == "__main__":
    main()
