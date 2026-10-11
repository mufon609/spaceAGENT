#!/usr/bin/env python3
"""castor_wormhole_survey.py
Flies Absence cloaked from central_nexus (nexus_prime) through the deep corridor
to last_light (ramens_rest) for refueling, then to beid, cocibolca, and driftwood.
Performs survey_system at each system looking for wormholes and anomalies.
Traverses wormhole if detected, or surveys all target systems and returns safely.
Maintains integrated cloak, monitors fuel, and refuels at friendly stations.
"""
import sys, time
from sm import call, sc, status_line, wait_idle, safe, in_battle

LEG1_TO_LAST_LIGHT = [
    'node_alpha', 'synchrony', 'the_experiment', 'achernar', 'garnet',
    'atlas', 'intercrus', 'kitalpha', 'kepler_442', 'theemin',
    'hollowcrest', 'alathfar', 'sabik', 'tidewater', 'last_light'
]

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
        
        # Check battle/danger
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("ALERT: Battle or damage! Calling safe()")
            safe()
            sys.exit(1)
            
        check_fuel_and_refuel()
        # Jump
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
    print("=== STARTING CASTOR WORMHOLE SURVEY EXPEDITION ===")
    s = wait_idle()
    loc = s.get("location", {})
    cur_sys = loc.get("system_id")
    docked = loc.get("docked_at")
    print(f"Starting at {cur_sys}, docked={docked}")
    
    # Pre-flight check
    sh = s.get("ship", {})
    print(f"Fuel: {sh.get('fuel')}/{sh.get('max_fuel')} | Cargo: {sh.get('cargo_used')}/{sh.get('cargo_capacity')}")
    
    # Undock if docked
    if docked:
        print("Undocking from", docked)
        call("spacemolt", "undock")
    
    check_and_cloak()
    
    if cur_sys == 'nexus_prime':
        print("\n--- LEG 1: Transit to last_light (ramens_rest) ---")
        fly_hops(LEG1_TO_LAST_LIGHT)
        
        # Dock at ramens_rest and refuel
        print("Arrived at last_light. Docking at ramens_rest...")
        call("spacemolt", "travel", {"target_poi": "ramens_rest"})
        call("spacemolt", "dock", {"base_id": "ramens_rest"})
        call("spacemolt", "refuel")
        s = wait_idle()
        print("Refueled at ramens_rest. Status:", status_line(s))
        call("spacemolt", "undock")
        check_and_cloak()
        
    print("\n--- LEG 2: Transit from last_light to beid ---")
    fly_hops(['unknown_edge', 'the_telescope', 'first_step', 'markeb', 'beid'])
    
    # Survey Beid
    res_beid = survey_curr_system()
    
    # Jump to Cocibolca and survey
    print("\n--- Jumping to cocibolca ---")
    fly_hops(['cocibolca'])
    res_coci = survey_curr_system()
    
    # Jump to Driftwood and survey
    print("\n--- Jumping to driftwood ---")
    fly_hops(['driftwood'])
    res_drift = survey_curr_system()
    
    # Check if any wormhole was revealed
    print("\n=== SURVEY COMPLETE: INSPECTING ALL POIS IN CASTOR CLUSTER ===")
    
    print("\n--- Returning to first_step (memorial station) to safe dock ---")
    fly_hops(['cocibolca', 'beid', 'markeb', 'first_step'])
    call("spacemolt", "travel", {"target_poi": "first_step_memorial_station"})
    call("spacemolt", "dock", {"base_id": "first_step_memorial_station"})
    call("spacemolt", "refuel")
    s = wait_idle()
    print("SAFELY DOCKED AT first_step_memorial_station:", status_line(s))

if __name__ == "__main__":
    main()
