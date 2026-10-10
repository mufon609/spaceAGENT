#!/usr/bin/env python3
"""fly_to_synchrony.py - Automated flight from Market Prime to Synchrony Hub.
Safe jumps with fuel and battle checks, travels to POI, docks cleanly.
"""
import sys, time
from sm import call, sc, step, wait_idle, in_battle, safe

ROUTE = [
    'gold_run', 'copernicus', 'keelbreak', 'zibal', 'revati',
    'alfirk', 'dubhe', 'maplevale', 'miaplacidus', 'cervantes',
    'nembus', 'kitalpha', 'intercrus', 'atlas', 'garnet',
    'achernar', 'the_experiment', 'synchrony'
]

def main():
    print("Starting flight to Synchrony Hub...")
    s = wait_idle()
    if s.get("location", {}).get("docked_at"):
        print("Undocking...")
        if not step("undock"):
            print("Failed to undock!")
            sys.exit(1)
            
    for hop in ROUTE:
        s = wait_idle()
        sh = s.get("ship", {})
        loc = s.get("location", {})
        cur_sys = loc.get("system_id")
        fuel = sh.get("fuel", 0)
        print(f"At {cur_sys} | Fuel: {fuel}/{sh.get('max_fuel')} | Hull: {sh.get('hull')}/{sh.get('max_hull')}")
        
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("ALERT: battle or hull damage detected, safe docking!")
            safe()
            sys.exit(1)
            
        if fuel < 6:
            print("ALERT: fuel critical, safe docking!")
            safe()
            sys.exit(1)
            
        if cur_sys == hop:
            continue
            
        print(f"Jumping to {hop}...")
        ok = step("jump", hop)
        if not ok:
            print(f"Jump to {hop} failed, executing safe dock!")
            safe()
            sys.exit(1)
            
    print("Arrived in synchrony! Traveling to synchrony_hub...")
    wait_idle()
    if step("travel", "synchrony_hub"):
        print("At synchrony_hub, docking...")
        wait_idle()
        if step("dock"):
            print("Successfully docked at Synchrony Hub!")
            sys.exit(0)
    print("Failed travel or dock, attempting emergency safe...")
    safe()

if __name__ == "__main__":
    main()
