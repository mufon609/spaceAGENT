#!/usr/bin/env python3
"""harvest_argon_mission.py
Navigates from nexus_prime to achernar_gas_pocket in achernar,
mines 10 units of argon_gas for mission b5434cc27e8df34e7be9cb4e87d356fc,
returns to central_nexus, docks, completes mission, dumps cargo, and refuels.
"""
import sys, time
from sm import call, step, wait_idle, in_battle, safe, dump, sc

OUTBOUND = ['node_alpha', 'synchrony', 'the_experiment', 'achernar']
INBOUND = ['the_experiment', 'synchrony', 'node_alpha', 'nexus_prime']
MISSION_ID = 'b5434cc27e8df34e7be9cb4e87d356fc'

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
    print("=== Starting Argon Gas Harvest Mission ===")
    s = wait_idle()
    sh = s.get("ship", {})
    loc = s.get("location", {})
    print(f"Initial location: {loc.get('system_id')} @ {loc.get('poi_id')} | Fuel: {sh.get('fuel')}/{sh.get('max_fuel')}")

    # 1. Outbound transit to achernar
    print("Beginning outbound jumps...")
    if not jump_route(OUTBOUND):
        print("Outbound route failed!")
        return 1

    s = wait_idle()
    loc = s.get("location", {})
    if loc.get("system_id") != "achernar":
        print(f"Unexpected location: {loc.get('system_id')}, expected achernar")
        safe()
        return 1

    # 2. Travel to achernar_gas_pocket
    print("Traveling to achernar_gas_pocket...")
    if not step("travel", "achernar_gas_pocket"):
        print("Failed to travel to gas pocket!")
        safe()
        return 1
    wait_idle()

    # 3. Check safety & cloak
    nearby = sc(call("spacemolt", "get_nearby"))
    if nearby.get("pirate_count", 0) > 0 or in_battle():
        print("ALERT: Hostiles detected at gas pocket! Fleeing!")
        safe()
        return 1

    # Engage cloak
    print("Engaging cloak for extraction...")
    c_res = call("spacemolt", "cloak", {"enable": True})
    print("Cloak status:", c_res.get("result", "engaged"))

    # 4. Harvest Argon Gas
    target_count = 10
    collected = 0
    print(f"Harvesting argon gas until target of {target_count} units...")
    for cycle in range(1, 30):
        s = wait_idle()
        if in_battle():
            print("ALERT: Battle detected during mining! Aborting!")
            safe()
            return 1

        cargo_info = sc(call("spacemolt", "get_cargo"))
        cargo_items = cargo_info.get("cargo", [])
        argon = sum(item.get("quantity", 0) for item in cargo_items if item.get("item_id") == "argon_gas")
        print(f"Cycle {cycle}: Argon in cargo = {argon}/{target_count}")
        if argon >= target_count:
            collected = argon
            print(f"Harvest target reached: {collected} units!")
            break

        m_res = call("spacemolt", "mine")
        print("Mine outcome:", m_res.get("result", m_res.get("error", {}).get("message", "ok")))
        time.sleep(10.5)

    # Disengage cloak to save fuel during jump sequence
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
    print("Structured complete:", comp.get("structuredContent", {}))

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
