#!/usr/bin/env python3
"""fly_to_market_prime.py - Automated flight from Sirius to Market Prime Exchange.
Safe jumps with fuel and battle checks, travels to POI, docks cleanly.
"""
import sys, time
from sm import call, sc, step, wait_idle, in_battle, safe

ROUTE = [
    'lacaille_9352', 'grumium', 'ridgecrest', 'cervantes',
    'miaplacidus', 'maplevale', 'dubhe', 'alfirk', 'revati',
    'zibal', 'keelbreak', 'copernicus', 'gold_run', 'market_prime'
]

def main():
    print("Starting flight to Market Prime...")
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
            
    print("Arrived in market_prime! Traveling to market_prime_exchange...")
    wait_idle()
    if step("travel", "market_prime_exchange"):
        print("At market_prime_exchange, docking...")
        wait_idle()
        if step("dock"):
            print("Successfully docked at Market Prime Exchange!")
            sys.exit(0)
    print("Failed travel or dock, attempting emergency safe...")
    safe()

if __name__ == "__main__":
    main()
