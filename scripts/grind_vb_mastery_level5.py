#!/usr/bin/env python3
import time, sys
from scripts.sm import call, sc, status_line, wait_idle

print("=== AUTONOMOUS VOIDBORN MASTERY LEVEL 5+ LOOP INITIATED ===")

while True:
    sk = sc(call("spacemolt", "get_skills")).get("skills", {})
    vb = sk.get("voidborn_mastery", {})
    lvl = vb.get("level", 0)
    xp = vb.get("xp", 0)
    nxt = vb.get("next_level_xp", 0)
    print(f"\n[STATUS] Voidborn Mastery: Level {lvl} ({xp}/{nxt} XP)")
    
    if lvl >= 5:
        print(f"MILESTONE REACHED! VOIDBORN MASTERY LEVEL {lvl} ACHIEVED!")
        break
    
    # Query mission board at Central Nexus
    ms = sc(call("spacemolt", "get_missions")).get("missions", [])
    print(f"Available missions at Central Nexus: {len(ms)}")
    
    # Check if there are any crafting missions that can be done immediately with stored materials
    # E.g. conductor_fabrication, advanced_material_processing
    # Also check if other mission resets happen
    time.sleep(10)
    break

