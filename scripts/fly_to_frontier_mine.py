#!/usr/bin/env python3
"""fly_to_frontier_mine.py - Fly to Frontier/Pioneer Fields, mine 20 nickel ore, complete mission.
Safely checks fuel and battle, retries transient timeouts, travels to pioneer_fields, mines nickel, completes The Collective Provides.
"""
import sys, time
from sm import call, sc, step, wait_idle, in_battle, safe

ROUTE = [
    'the_experiment', 'achernar', 'garnet',
    'atlas', 'intercrus', 'kitalpha', 'kepler_442', 'theemin',
    'hollowcrest', 'alathfar', 'sabik', 'tidewater', 'last_light',
    'unknown_edge', 'altais', 'frontier'
]

def robust_step(action, target=None, retries=3):
    for attempt in range(retries):
        try:
            return step(action, target)
        except Exception as e:
            print(f"Transient error on {action} {target} (attempt {attempt+1}/{retries}): {e}")
            time.sleep(3)
    return False

def check_mission_progress():
    try:
        r = call("spacemolt", "get_active_missions")
        for m in r.get("structuredContent", {}).get("missions", {}).get("active", []):
            if m.get("template_id") == "the_collective_provides" or "collective_provides" in m.get("mission_id", ""):
                for obj in m.get("objectives", []):
                    if obj.get("type") == "mine_resource":
                        print(f"Mission progress: {obj.get('current')}/{obj.get('required')}")
                        return obj.get("current", 0) >= obj.get("required", 20), m.get("mission_id")
    except Exception as e:
        print(f"Error checking mission progress: {e}")
    return False, None

def main():
    print("Resuming flight to Frontier from current location...")
    s = wait_idle()
    if s.get("location", {}).get("docked_at"):
        print("Undocking...")
        if not robust_step("undock"):
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
        ok = robust_step("jump", hop)
        if not ok:
            # Check if we landed anyway
            cur = wait_idle().get("location", {}).get("system_id")
            if cur == hop:
                print(f"Jump succeeded despite return value, now at {hop}")
            else:
                print(f"Jump to {hop} failed, executing safe dock!")
                safe()
                sys.exit(1)
            
    print("Arrived in frontier! Traveling to pioneer_fields...")
    wait_idle()
    if not robust_step("travel", "pioneer_fields"):
        print("Failed to travel to pioneer_fields!")
        safe()
        sys.exit(1)
        
    print("At pioneer_fields! Starting mining operation for nickel ore...")
    done, mid = check_mission_progress()
    cycles = 0
    while not done and cycles < 80:
        cycles += 1
        s = wait_idle()
        sh = s.get("ship", {})
        if in_battle() or sh.get("hull", 0) < sh.get("max_hull", 0):
            print("Danger at belt! Fleeing to safe dock...")
            safe()
            sys.exit(1)
            
        if sh.get("cargo_used", 0) >= sh.get("cargo_capacity", 75) - 2:
            print("Hold near full! Jettisoning non-nickel ores to keep space...")
            for itm in s.get("ship", {}).get("cargo", []):
                if itm.get("item_id") in ("iron_ore", "copper_ore"):
                    call("spacemolt_storage", "jettison", {"item_id": itm["item_id"], "quantity": itm["quantity"]})
                    break
                    
        print(f"Mining cycle {cycles}...")
        try:
            call("spacemolt", "mine")
        except Exception as e:
            print(f"Transient mine error: {e}")
        time.sleep(1)
        done, mid = check_mission_progress()
        
    print(f"Mining completed! Done={done}, Mission ID={mid}")
    if done and mid:
        print("Completing The Collective Provides mission...")
        cr = call("spacemolt", "complete_mission", {"mission_id": mid})
        print("Mission complete result:", cr.get("result", cr))
        
    print("Traveling to nearest station to dock safely (Deep Range Outpost or Ramen's Rest)...")
    safe()

if __name__ == "__main__":
    main()
