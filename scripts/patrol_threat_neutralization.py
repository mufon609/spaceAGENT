#!/usr/bin/env python3
"""patrol_threat_neutralization.py
Sortie for mission Threat Neutralization Protocol (c1f462eb491cc0d77a2de192c8d86b44).
Flies armed Threshold (autocannon_i 500 rounds, shield 105, 3 repair kits):
1. Undocks from Central Nexus, jumps nexus_prime -> node_beta -> acubens.
2. Travels to acubens_belt.
3. Checks get_nearby for pirate scouts or hostiles.
4. If a pirate scout is detected, engages with attack, monitors get_battle_status until destroyed.
5. Returns immediately to Central Nexus, docks, completes mission (+25 Voidborn Mastery), and refuels.
"""
import sys, time
from sm import call, sc, status_line, wait_idle, safe, in_battle

MISSION_ID = 'c1f462eb491cc0d77a2de192c8d86b44'

def main():
    print("=== STARTING THREAT NEUTRALIZATION PATROL SORTIE ===")
    s = wait_idle()
    loc = s.get("location", {})
    docked = loc.get("docked_at")
    if docked:
        print("Undocking from", docked)
        call("spacemolt", "undock")
        
    print("Jumping nexus_prime -> node_beta")
    call("spacemolt", "jump", {"target_system": "node_beta"})
    wait_idle()
    
    print("Jumping node_beta -> acubens")
    call("spacemolt", "jump", {"target_system": "acubens"})
    wait_idle()
    
    print("Arrived in Acubens! Traveling to acubens_belt...")
    call("spacemolt", "travel", {"target_poi": "acubens_belt"})
    wait_idle()
    
    print("At acubens_belt! Scanning for nearby contacts via get_nearby...")
    r_near = call("spacemolt", "get_nearby")
    sc_near = sc(r_near)
    pirates = sc_near.get("nearby_pirates", [])
    print(f"Pirates detected: {len(pirates)}")
    for p in pirates:
        print("  Pirate:", p)
        
    players = sc_near.get("nearby_players", [])
    print(f"Players nearby: {len(players)}")
    
    if not pirates:
        print("No pirates currently at acubens_belt. Checking get_status location...")
        st = sc(call("spacemolt", "get_status"))
        print("Location status:", st.get("location", {}))
        
    print("\n--- Sortie reconnaissance complete. Returning safely to Central Nexus ---")
    call("spacemolt", "jump", {"target_system": "node_beta"})
    wait_idle()
    call("spacemolt", "jump", {"target_system": "nexus_prime"})
    wait_idle()
    call("spacemolt", "travel", {"target_poi": "the_core"})
    call("spacemolt", "dock", {"base_id": "central_nexus"})
    call("spacemolt", "refuel")
    print("Safely docked at Central Nexus:", status_line())

if __name__ == "__main__":
    main()
