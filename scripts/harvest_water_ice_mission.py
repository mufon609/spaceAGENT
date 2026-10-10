#!/usr/bin/env python3
"""harvest_water_ice_mission.py
Navigates from nexus_prime to gsc_0041_frost_ring in gsc_0041,
mines 5 units of water_ice for mission 9a7dc7f9380da1d03378b88f192b0c4d,
returns to central_nexus, docks, completes mission, dumps cargo, and refuels.
"""
import sys, time
from sm import call, step, wait_idle, in_battle, safe, dump, sc

OUTBOUND = ['node_alpha', 'synchrony', 'pherkad', 'gsc_0041']
INBOUND = ['pherkad', 'synchrony', 'node_alpha', 'nexus_prime']
MISSION_ID = '9a7dc7f9380da1d03378b88f192b0c4d'

def jump_route(route):
    for hop in route:
        s = wait_idle()
        sh = s.get("ship", {})
        loc = s.get("location", {})
        cur_sys = loc.get("system_id")
        fuel = sh.get("fuel", 0)
        print(f"At {cur_sys} | Fuel: {fuel}/{sh.get('max_fuel')} | Hull: {sh.get('hull')}/{sh.get('max_hull')}")

        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("ALERT: battle or hull damage, executing safe dock!")
            safe()
            return False

        if fuel < 12:
            print(f"ALERT: low fuel ({fuel}), executing safe dock!")
            safe()
            return False

        if cur_sys == hop:
            continue

        print(f"Jumping to {hop}...")
        ok = step("jump", hop)
        if not ok:
            cur = wait_idle().get("location", {}).get("system_id")
            if cur != hop:
                print(f"Jump to {hop} failed, executing safe dock!")
                safe()
                return False
    return True

def main():
    print("=== Starting Water Ice Harvest Mission ===")
    s = wait_idle()
    sh = s.get("ship", {})
    loc = s.get("location", {})
    print(f"Initial location: {loc.get('system_id')} @ {loc.get('poi_id')} | Fuel: {sh.get('fuel')}/{sh.get('max_fuel')}")

    # 1. Outbound transit to gsc_0041
    print("Beginning outbound jumps...")
    if not jump_route(OUTBOUND):
        print("Outbound route failed!")
        return 1

    s = wait_idle()
    loc = s.get("location", {})
    if loc.get("system_id") != "gsc_0041":
        print(f"Unexpected location: {loc.get('system_id')}, expected gsc_0041")
        safe()
        return 1

    # 2. Travel to gsc_0041_frost_ring
    print("Traveling to gsc_0041_frost_ring...")
    if not step("travel", "gsc_0041_frost_ring"):
        print("Failed to travel to frost ring!")
        safe()
        return 1
    wait_idle()

    # 3. Check safety & engage cloak
    nearby = sc(call("spacemolt", "get_nearby"))
    if nearby.get("pirate_count", 0) > 0 or in_battle():
        print("ALERT: Hostiles detected at frost ring! Fleeing!")
        safe()
        return 1

    print("Engaging cloak for ice extraction...")
    call("spacemolt", "cloak", {"enable": True})

    # 4. Harvest Water Ice
    target_count = 5
    collected = 0
    print(f"Harvesting water ice until target of {target_count} units...")
    for cycle in range(1, 20):
        s = wait_idle()
        if in_battle():
            print("ALERT: Battle detected during mining! Aborting!")
            safe()
            return 1

        cargo_info = sc(call("spacemolt", "get_cargo"))
        cargo_items = cargo_info.get("cargo", [])
        water_ice = sum(item.get("quantity", 0) for item in cargo_items if item.get("item_id") == "water_ice")
        print(f"Cycle {cycle}: Water Ice in cargo = {water_ice}/{target_count}")
        if water_ice >= target_count:
            collected = water_ice
            print(f"Harvest target reached: {collected} units!")
            break

        m_res = call("spacemolt", "mine")
        print("Mine outcome:", m_res.get("result", m_res.get("error", {}).get("message", "ok")))
        time.sleep(10.5)

    # Disengage cloak for transit
    print("Disengaging cloak for transit...")
    call("spacemolt", "cloak", {"enable": False})

    # 5. Return transit to nexus_prime
    print("Beginning return jumps...")
    if not jump_route(INBOUND):
        print("Return route failed!")
        return 1

    # 6. Travel to the_core and dock at central_nexus
    print("Arrived at nexus_prime. Traveling to the_core...")
    wait_idle()
    if not step("travel", "the_core"):
        print("Failed to travel to the_core!")
        safe()
        return 1

    wait_idle()
    print("Docking at central_nexus...")
    d_res = call("spacemolt", "dock", {"base_id": "central_nexus"})
    print("Dock outcome:", d_res.get("result", d_res.get("error", {}).get("message", "ok")))
    wait_idle()

    # 7. Complete Mission
    print(f"Completing mission {MISSION_ID}...")
    comp = call("spacemolt", "complete_mission", {"mission_id": MISSION_ID})
    print("Mission complete result:", comp.get("result", comp.get("error", {}).get("message", "ok")))

    # 8. Dump cargo and refuel
    print("Dumping cargo to storage...")
    dump()
    print("Refueling ship...")
    rf = call("spacemolt", "refuel")
    print("Refuel result:", rf.get("result", "ok"))

    # 9. Status & skills update
    st = sc(call("spacemolt", "get_status"))
    sk = st.get("skills", {})
    vm = sk.get("voidborn_mastery", {})
    print(f"SUCCESS! Voidborn Mastery: Level {vm.get('level')} ({vm.get('xp')}/{vm.get('next_level_xp')} XP)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
