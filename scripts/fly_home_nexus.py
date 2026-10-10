#!/usr/bin/env python3
"""fly_home_nexus.py - Fly from Horizon to Central Nexus.
Preflights each jump, checks battle & hull, docks safely at central_nexus.
"""
import sys, time
from sm import call, sc, step, wait_idle, in_battle, safe

ROUTE = [
    'altais', 'unknown_edge', 'last_light', 'tidewater', 'sabik',
    'alathfar', 'hollowcrest', 'theemin', 'kepler_442', 'kitalpha',
    'intercrus', 'atlas', 'garnet', 'achernar', 'the_experiment',
    'synchrony', 'node_alpha', 'nexus_prime'
]

def main():
    print("Starting flight home to Central Nexus...")
    for hop in ROUTE:
        s = wait_idle()
        sh = s.get("ship", {})
        loc = s.get("location", {})
        cur_sys = loc.get("system_id")
        fuel = sh.get("fuel", 0)
        print(f"At {cur_sys} | Fuel: {fuel}/{sh.get('max_fuel')} | Hull: {sh.get('hull')}/{sh.get('max_hull')}")
        
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("ALERT: battle or hull damage, executing safe dock!")
            safe()
            sys.exit(1)
            
        if fuel < 6:
            print("ALERT: low fuel, safe docking!")
            safe()
            sys.exit(1)
            
        if cur_sys == hop:
            continue
            
        print(f"Jumping to {hop}...")
        ok = step("jump", hop)
        if not ok:
            cur = wait_idle().get("location", {}).get("system_id")
            if cur != hop:
                print(f"Jump to {hop} failed, executing safe dock!")
                safe()
                sys.exit(1)
            
    print("Arrived in nexus_prime! Traveling to the_core...")
    wait_idle()
    if step("travel", "the_core"):
        print("At the_core, docking at central_nexus...")
        wait_idle()
        if step("dock"):
            print("Successfully docked at central_nexus!")
            sys.exit(0)
    print("Attempting safe dock...")
    safe("central_nexus")

if __name__ == "__main__":
    main()
