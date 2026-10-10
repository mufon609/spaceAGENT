#!/usr/bin/env python3
"""fly_signal_protocol.py - Execute The Signal Protocol:
1. Undock from Central Nexus
2. Jump to Node Beta, travel & dock at node_beta_industrial_station
3. Undock, jump to Node Gamma, travel & dock at node_gamma_relay_station
4. Undock, jump to Node Alpha, then Nexus Prime
5. Travel & dock at central_nexus
6. Complete mission for +25 Voidborn Mastery XP!
"""
import sys, time
from sm import call, sc, step, wait_idle, in_battle, safe

def main():
    print("Starting The Signal Protocol run...")
    s = wait_idle()
    if s.get("location", {}).get("docked_at"):
        print("Undocking from Central Nexus...")
        step("undock")
        wait_idle()
        
    # Step 1: Jump to node_beta
    print("Jumping to node_beta...")
    step("jump", "node_beta")
    wait_idle()
    print("Traveling to node_beta_industrial_station...")
    step("travel", "node_beta_industrial_station")
    wait_idle()
    print("Docking at Node Beta Industrial Station...")
    step("dock")
    wait_idle()
    print("Recalibration 1 complete at Node Beta!")
    time.sleep(2)
    
    # Step 2: Undock and jump to node_gamma
    print("Undocking from Node Beta...")
    step("undock")
    wait_idle()
    print("Jumping to node_gamma...")
    step("jump", "node_gamma")
    wait_idle()
    print("Traveling to node_gamma_relay_station...")
    step("travel", "node_gamma_relay_station")
    wait_idle()
    print("Docking at Node Gamma Relay Station...")
    step("dock")
    wait_idle()
    print("Recalibration 2 complete at Node Gamma!")
    time.sleep(2)
    
    # Step 3: Return to Nexus Prime
    print("Undocking from Node Gamma...")
    step("undock")
    wait_idle()
    print("Jumping to node_alpha...")
    step("jump", "node_alpha")
    wait_idle()
    print("Jumping to nexus_prime...")
    step("jump", "nexus_prime")
    wait_idle()
    print("Traveling to the_core...")
    step("travel", "the_core")
    wait_idle()
    print("Docking at Central Nexus...")
    step("dock")
    wait_idle()
    print("Returned to Central Nexus! Completing mission...")
    
    # Complete mission
    r = call("spacemolt", "complete_mission", {"mission_id": "58e1ca82275b6f2900da400f8f5c8bc2"})
    print("Mission result:", r.get("result", r))
    print("Signal Protocol successfully completed!")

if __name__ == "__main__":
    main()
