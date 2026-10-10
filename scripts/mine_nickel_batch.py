#!/usr/bin/env python3
"""mine_nickel_batch.py - Finish mining 20 nickel ore at pioneer_fields and complete The Collective Provides.
Jumps from Horizon to Frontier, mines until 20/20, completes mission, returns to dock safely.
"""
import sys, time
from sm import call, sc, step, wait_idle, in_battle, safe

def check_progress():
    r = call("spacemolt", "get_active_missions")
    for m in r.get("structuredContent", {}).get("missions", {}).get("active", []):
        if "collective_provides" in m.get("mission_id", "") or m.get("template_id") == "the_collective_provides":
            for obj in m.get("objectives", []):
                if obj.get("type") == "mine_resource":
                    cur = obj.get("current", 0)
                    req = obj.get("required", 20)
                    print(f"Nickel progress: {cur}/{req}")
                    return cur >= req, m.get("mission_id"), cur
    return False, None, 0

def main():
    print("Starting nickel mining sortie...")
    s = wait_idle()
    if s.get("location", {}).get("docked_at"):
        print("Undocking from station...")
        step("undock")
        wait_idle()
        
    cur_sys = wait_idle().get("location", {}).get("system_id")
    if cur_sys != "frontier":
        print("Jumping to frontier...")
        step("jump", "frontier")
        wait_idle()
        
    print("Traveling to pioneer_fields...")
    step("travel", "pioneer_fields")
    wait_idle()
    
    done, mid, cur = check_progress()
    cycle = 0
    consecutive_zero = 0
    
    while not done and cycle < 120:
        cycle += 1
        st = wait_idle()
        sh = st.get("ship", {})
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("ALERT: battle or hull damage, executing safe dock!")
            safe()
            sys.exit(1)
            
        # Keep cargo clean
        for itm in st.get("ship", {}).get("cargo", []):
            if itm.get("item_id") in ("iron_ore", "copper_ore") and sh.get("cargo_used", 0) > 60:
                call("spacemolt_storage", "jettison", {"item_id": itm["item_id"], "quantity": itm["quantity"]})
                
        print(f"Mining cycle {cycle}...")
        res = call("spacemolt", "mine")
        time.sleep(1)
        done, mid, new_cur = check_progress()
        
        if new_cur == cur:
            consecutive_zero += 1
            if consecutive_zero >= 6:
                print("Deposit temporarily depleted, waiting 15s for tick regeneration...")
                time.sleep(15)
                consecutive_zero = 0
        else:
            consecutive_zero = 0
            cur = new_cur
            
    print(f"Sortie complete! Done={done}, Mid={mid}")
    if done and mid:
        print("Completing The Collective Provides mission...")
        cr = call("spacemolt", "complete_mission", {"mission_id": mid})
        print("Mission complete output:", cr.get("result", cr))
        
    print("Returning to Horizon to dock safely...")
    step("jump", "horizon")
    wait_idle()
    step("travel", "mobile_capital")
    wait_idle()
    step("dock")
    wait_idle()
    print("Docked safely at mobile_capital!")

if __name__ == "__main__":
    main()
