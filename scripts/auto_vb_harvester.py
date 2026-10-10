#!/usr/bin/env python3
import time, sys
from scripts.sm import call, sc, status_line, wait_idle

def check_mastery():
    sk = sc(call("spacemolt", "get_skills")).get("skills", {})
    vb = sk.get("voidborn_mastery", {})
    return vb.get("level", 0), vb.get("xp", 0), vb.get("next_level_xp", 0)

print("Starting auto_vb_harvester...")
lvl, xp, nxt = check_mastery()
print(f"Current Voidborn Mastery: Level {lvl} ({xp}/{nxt} XP)")

# Check if board has newly spawned Voidborn missions
ms = sc(call("spacemolt", "get_missions")).get("missions", [])
for m in ms:
    rw = m.get("rewards", {})
    if "voidborn_mastery" in str(rw):
        print("Found Voidborn mission:", m.get("template_id"), m.get("title"))

