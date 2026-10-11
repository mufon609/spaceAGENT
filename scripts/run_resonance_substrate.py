#!/usr/bin/env python3
"""run_resonance_substrate.py - automated mission completion for Resonance Substrate.
Hauled 5 Energy Crystals from Central Nexus.
Flies Absence cloaked to garnet_dim_lattice (garnet).
Mines until total Energy Crystals >= 15 (jettisoning Fe/Cu filler).
Returns cloaked to node_beta_industrial_station (node_beta).
Turns in mission, refuels, and prints rewards.
"""
import sys, time
from sm import call, sc, status_line, wait_idle, safe, in_battle

OUT_ROUTE = ['node_alpha', 'synchrony', 'the_experiment', 'achernar', 'garnet']
RETURN_ROUTE = ['achernar', 'the_experiment', 'synchrony', 'node_alpha', 'node_beta']

def check_and_cloak():
    s = wait_idle()
    pl = s.get("player", {})
    if not pl.get("is_cloaked", False):
        print("Activating integrated cloak...")
        call("spacemolt", "cloak")

def check_fuel():
    s = wait_idle()
    sh = s.get("ship", {})
    fuel = sh.get("fuel", 0)
    print(f"[FUEL CHECK] {fuel}/{sh.get('max_fuel', 110)}")
    if fuel < 25:
        print("[FUEL ALERT] Fuel < 25! Using emergency fuel cell from cargo...")
        r = call("spacemolt", "use_item", {"item_id": "fuel_cell"})
        print("Use item result:", r)
        s = wait_idle()
        print("New fuel:", s.get("ship", {}).get("fuel"))

def fly_hops(route):
    for hop in route:
        s = wait_idle()
        sh = s.get("ship", {})
        loc = s.get("location", {})
        print(f"At {loc.get('system_id')} | Fuel: {sh.get('fuel')}/{sh.get('max_fuel')} | Jumping to {hop}...")
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("ALERT: Under attack or damaged! Calling safe()")
            safe()
            sys.exit(1)
        check_fuel()
        call("spacemolt", "jump", {"target_system": hop})
        check_and_cloak()

def get_crystal_count():
    r = call("spacemolt", "get_cargo")
    res = r.get("result", "")
    count = 0
    for line in res.splitlines():
        if "energy crystal" in line.lower():
            parts = line.split()
            for p in parts:
                if p.isdigit():
                    count = int(p)
                    break
    return count

def clean_filler():
    r = call("spacemolt", "get_cargo")
    res = r.get("result", "")
    for line in res.splitlines():
        ll = line.lower()
        if "iron ore" in ll or "copper ore" in ll:
            parts = line.split()
            qty = 0
            for p in parts:
                if p.isdigit():
                    qty = int(p)
                    break
            item_id = "iron_ore" if "iron ore" in ll else "copper_ore"
            if qty > 0:
                print(f"Jettisoning {qty} {item_id} filler...")
                call("spacemolt", "jettison", {"item_id": item_id, "quantity": qty})

def main():
    print("=== STARTING RESONANCE SUBSTRATE MISSION RUN ===")
    s = wait_idle()
    loc = s.get("location", {})
    docked = loc.get("docked_at")
    if docked:
        print(f"Undocking from {docked}...")
        call("spacemolt", "undock")
    check_and_cloak()

    cur_crystals = get_crystal_count()
    print(f"Initial Energy Crystals in cargo: {cur_crystals}/15")

    if cur_crystals < 15:
        print("\n--- INBOUND SORTIE TO GARNET ---")
        fly_hops(OUT_ROUTE)
        print("Arrived in garnet! Traveling to garnet_dim_lattice...")
        call("spacemolt", "travel", {"target_poi": "garnet_dim_lattice"})
        check_and_cloak()

        print("\n--- HARVESTING ENERGY CRYSTALS ---")
        cycles = 0
        max_cycles = 150
        while cycles < max_cycles:
            cur_crystals = get_crystal_count()
            print(f"[Cycle {cycles}] Energy Crystals: {cur_crystals}/15")
            if cur_crystals >= 15:
                print("TARGET ACHIEVED: 15/15 Energy Crystals in hold!")
                break
            
            check_fuel()
            
            # Mine cycle
            m_res = call("spacemolt", "mine")
            err = m_res.get("error", {})
            if err.get("code") == "cargo_full":
                print("Hold full, clearing iron/copper filler...")
                clean_filler()
            cycles += 1
            time.sleep(1)

        # Final cleanup of any filler
        clean_filler()

    cur_crystals = get_crystal_count()
    print(f"\nCargo before return transit: {cur_crystals}/15 Energy Crystals")

    print("\n--- RETURN SORTIE TO NODE BETA ---")
    fly_hops(RETURN_ROUTE)

    print("Arrived in node_beta! Traveling to node_beta_industrial_station...")
    call("spacemolt", "travel", {"target_poi": "node_beta_industrial_station"})
    print("Docking at node_beta_industrial_station...")
    call("spacemolt", "dock", {"base_id": "node_beta_industrial_station"})
    
    print("\n--- TURNING IN MISSION ---")
    r_turnin = call("spacemolt", "complete_mission", {"mission_id": "df70f8c82e6d923f313fae3cc9ba3d1d"})
    if "error" in r_turnin:
        print("Error with ID, trying template name...")
        r_turnin = call("spacemolt", "complete_mission", {"mission_id": "resonance_substrate"})
    print("Turn-in result:", r_turnin)

    print("\n--- REFUELING AT NODE BETA ---")
    call("spacemolt", "refuel")
    
    s = wait_idle()
    print("\nFINAL STATUS:", status_line(s))
    
    # Check skills
    sk = sc(call("spacemolt", "get_skills")).get("skills", {})
    vb = sk.get("voidborn_mastery", {})
    print(f"VOIDBORN MASTERY: Level {vb.get('level')} ({vb.get('xp')}/{vb.get('next_level_xp')} XP)")

if __name__ == "__main__":
    main()
