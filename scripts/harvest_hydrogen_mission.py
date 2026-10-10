#!/usr/bin/env python3
"""harvest_hydrogen_mission.py
Travels to stellar_siphon in nexus_prime, activates cloak, harvests 5 hydrogen_gas,
returns to the_core / central_nexus, docks, and completes mission ec50161e5d2bd0d1a71855a4b719cf02.
"""
import sys, time
from sm import call, step, wait_idle, in_battle, safe

def main():
    print("Preflight check...")
    s = wait_idle()
    sh = s.get("ship", {})
    loc = s.get("location", {})
    print(f"Location: {loc.get('system_id')} @ {loc.get('poi_id')} | Docked: {loc.get('docked')}")
    print(f"Fuel: {sh.get('fuel')}/{sh.get('max_fuel')} | Cargo: {sh.get('cargo')}/{sh.get('cargo_capacity')}")

    # 1. Travel to stellar_siphon if not already there
    if loc.get("poi_id") != "stellar_siphon":
        print("Traveling to stellar_siphon...")
        ok = step("travel", "stellar_siphon")
        if not ok:
            print("Failed to travel to stellar_siphon!")
            return 1
        s = wait_idle()
        print("Arrived at stellar_siphon.")

    # 2. Check cloak status / activate cloak if uncloaked
    # Passive stealth check
    print("Checking cloak / stealth...")
    res = call("spacemolt", "cloak")
    print("Cloak result:", res.get("result", res.get("error", {}).get("message", "unknown")))

    # 3. Mine hydrogen until at least 5 units in cargo
    target_count = 5
    while True:
        s = wait_idle()
        if in_battle():
            print("ALERT: Battle detected at gas cloud! Fleeing!")
            safe()
            return 1

        cargo_info = call("spacemolt", "get_cargo")
        cargo_items = cargo_info.get("cargo", [])
        h2 = 0
        for item in cargo_items:
            if item.get("id") == "hydrogen_gas" or item.get("item_id") == "hydrogen_gas":
                h2 = item.get("quantity", 0)
        
        print(f"Current hydrogen gas in cargo: {h2}/{target_count}")
        if h2 >= target_count:
            print("Target hydrogen collected!")
            break

        print("Harvesting gas cycle...")
        m_res = call("spacemolt", "mine")
        print("Mine outcome:", m_res.get("result", m_res.get("error", {}).get("message", "unknown")))
        time.sleep(10.5)

    # 4. Travel back to the_core
    print("Returning to The Core...")
    ok = step("travel", "the_core")
    if not ok:
        print("Failed to travel to the_core!")
        return 1
    wait_idle()

    # 5. Dock at central_nexus
    print("Docking at central_nexus...")
    d_res = call("spacemolt", "dock", {"base_id": "central_nexus"})
    print("Dock outcome:", d_res.get("result", d_res.get("error", {}).get("message", "unknown")))
    wait_idle()

    # 6. Complete mission
    print("Completing hydrogen_collection_run mission...")
    c_res = call("spacemolt", "complete_mission", {"mission_id": "ec50161e5d2bd0d1a71855a4b719cf02"})
    print("Mission completion outcome:", c_res.get("result", c_res.get("error", {}).get("message", "unknown")))

    # 7. Check skills
    sk = call("spacemolt", "get_skills")
    print("Skills update:")
    for s_entry in sk.get("skills", []):
        if s_entry.get("id") in ["voidborn_mastery", "stealth", "mining"]:
            print(f" - {s_entry.get('id')}: Lvl {s_entry.get('level')} ({s_entry.get('current_xp')}/{s_entry.get('next_level_xp')} XP)")

    return 0

if __name__ == "__main__":
    sys.exit(main())
