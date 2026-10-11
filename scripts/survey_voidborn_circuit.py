#!/usr/bin/env python3
"""survey_voidborn_circuit.py
Flies Absence cloaked on a circuit of all Voidborn empire stations:
nexus_prime -> node_alpha (node_alpha_processing_station) -> node_gamma (node_gamma_relay_station)
-> node_beta (node_beta_industrial_station) -> synchrony (synchrony_hub) -> the_experiment
Checks get_missions at each station for Voidborn empire missions.
Returns to central_nexus, refuels, and prints all discovered empire missions.
"""
import sys, time
from sm import call, sc, status_line, wait_idle, safe, in_battle

STATION_STOPS = [
    ('node_alpha', 'node_alpha_processing_station', 'node_alpha_processing_station'),
    ('node_gamma', 'node_gamma_relay_station', 'node_gamma_relay_station'),
    ('node_beta', 'node_beta_industrial_station', 'node_beta_industrial_station'),
    ('synchrony', 'synchrony_hub', 'synchrony_hub'),
    ('the_experiment', 'the_experiment_research_station', 'the_experiment_research_station')
]

def check_and_cloak():
    s = wait_idle()
    pl = s.get("player", {})
    if not pl.get("is_cloaked", False):
        print("Activating cloak...")
        call("spacemolt", "cloak")

def check_missions_at_station(station_name):
    print(f"\n=== MISSIONS AT {station_name} ===")
    r = call("spacemolt", "get_missions")
    text = r.get("result", "")
    missions = text.split("--- ")
    vb_found = []
    for m in missions:
        if not m.strip(): continue
        lines = m.strip().splitlines()
        header = lines[0]
        rw = [l for l in lines if l.startswith("Rewards:")]
        rw_str = rw[0] if rw else ""
        if "voidborn_mastery" in rw_str or "rep with voidborn" in rw_str:
            print("  * VOIDBORN MISSION:", header)
            print("   ", rw_str)
            vb_found.append(header)
        else:
            print("   ", header)
    return vb_found

def main():
    print("=== STARTING VOIDBORN EMPIRE MISSION CIRCUIT ===")
    s = wait_idle()
    loc = s.get("location", {})
    docked = loc.get("docked_at")
    if docked:
        print("Undocking from", docked)
        call("spacemolt", "undock")
    check_and_cloak()
    
    # 1. nexus_prime -> node_alpha
    print("\n--- Jumping to node_alpha ---")
    call("spacemolt", "jump", {"target_system": "node_alpha"})
    check_and_cloak()
    call("spacemolt", "travel", {"target_poi": "node_alpha_processing_station"})
    call("spacemolt", "dock", {"base_id": "node_alpha_processing_station"})
    check_missions_at_station("node_alpha_processing_station")
    call("spacemolt", "refuel")
    call("spacemolt", "undock")
    check_and_cloak()
    
    # 2. node_alpha -> node_gamma
    print("\n--- Jumping to node_gamma ---")
    call("spacemolt", "jump", {"target_system": "node_gamma"})
    check_and_cloak()
    call("spacemolt", "travel", {"target_poi": "node_gamma_relay_station"})
    call("spacemolt", "dock", {"base_id": "node_gamma_relay_station"})
    check_missions_at_station("node_gamma_relay_station")
    call("spacemolt", "refuel")
    call("spacemolt", "undock")
    check_and_cloak()
    
    # 3. node_gamma -> node_beta
    print("\n--- Jumping to node_beta ---")
    call("spacemolt", "jump", {"target_system": "node_beta"})
    check_and_cloak()
    call("spacemolt", "travel", {"target_poi": "node_beta_industrial_station"})
    call("spacemolt", "dock", {"base_id": "node_beta_industrial_station"})
    check_missions_at_station("node_beta_industrial_station")
    call("spacemolt", "refuel")
    call("spacemolt", "undock")
    check_and_cloak()
    
    # 4. node_beta -> nexus_prime -> synchrony
    print("\n--- Jumping back via node_alpha to synchrony ---")
    call("spacemolt", "jump", {"target_system": "node_alpha"})
    check_and_cloak()
    call("spacemolt", "jump", {"target_system": "synchrony"})
    check_and_cloak()
    call("spacemolt", "travel", {"target_poi": "synchrony_hub"})
    call("spacemolt", "dock", {"base_id": "synchrony_hub"})
    check_missions_at_station("synchrony_hub")
    call("spacemolt", "refuel")
    call("spacemolt", "undock")
    check_and_cloak()
    
    # 5. synchrony -> the_experiment
    print("\n--- Jumping to the_experiment ---")
    call("spacemolt", "jump", {"target_system": "the_experiment"})
    check_and_cloak()
    call("spacemolt", "travel", {"target_poi": "the_experiment_research_station"})
    call("spacemolt", "dock", {"base_id": "the_experiment_research_station"})
    check_missions_at_station("the_experiment_research_station")
    call("spacemolt", "refuel")
    call("spacemolt", "undock")
    check_and_cloak()
    
    # Return to Central Nexus
    print("\n--- Returning home to Central Nexus ---")
    call("spacemolt", "jump", {"target_system": "synchrony"})
    check_and_cloak()
    call("spacemolt", "jump", {"target_system": "node_alpha"})
    check_and_cloak()
    call("spacemolt", "jump", {"target_system": "nexus_prime"})
    check_and_cloak()
    call("spacemolt", "travel", {"target_poi": "the_core"})
    call("spacemolt", "dock", {"base_id": "central_nexus"})
    call("spacemolt", "refuel")
    print("Safely DOCKED AT CENTRAL NEXUS:", status_line())

if __name__ == "__main__":
    main()
