#!/usr/bin/env python3
"""mine_finish_nickel.py - Mine the final 4 units of Nickel Ore at pioneer_fields and complete The Collective Provides.
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
    print("Starting final nickel mining run...")
    s = wait_idle()
    if s.get("location", {}).get("docked_at"):
        step("undock")
        wait_idle()
        
    cur_sys = wait_idle().get("location", {}).get("system_id")
    if cur_sys != "frontier":
        step("jump", "frontier")
        wait_idle()
        
    step("travel", "pioneer_fields")
    wait_idle()
    
    done, mid, cur = check_progress()
    attempts = 0
    
    while not done and attempts < 150:
        attempts += 1
        st = wait_idle()
        sh = st.get("ship", {})
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("Danger! Fleeing...")
            safe()
            sys.exit(1)
            
        # Keep cargo free
        if sh.get("cargo_used", 0) > 55:
            for itm in st.get("ship", {}).get("cargo", []):
                if itm.get("item_id") in ("iron_ore", "copper_ore"):
                    call("spacemolt_storage", "jettison", {"item_id": itm["item_id"], "quantity": itm["quantity"]})
                    
        print(f"Mining attempt {attempts} (cur: {cur}/20)...")
        call("spacemolt", "mine")
        time.sleep(2)
        done, mid, new_cur = check_progress()
        
        if new_cur == cur:
            if attempts % 5 == 0:
                print("Waiting 20s for belt tick regeneration...")
                time.sleep(20)
        else:
            cur = new_cur
            
    print(f"Mining done! Done={done}, Mid={mid}")
    if done and mid:
        print("Completing The Collective Provides mission...")
        cr = call("spacemolt", "complete_mission", {"mission_id": mid})
        print("RESULT:", cr.get("result", cr))
        
    print("Returning to Horizon to dock safely...")
    step("jump", "horizon")
    wait_idle()
    step("travel", "mobile_capital")
    wait_idle()
    step("dock")
    wait_idle()
    print("Safely docked at mobile_capital!")

if __name__ == "__main__":
    main()
