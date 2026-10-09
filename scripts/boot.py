#!/usr/bin/env python3
"""boot.py - ONE command for session start (replaces status + active + preflight + list_ships + skills + tick).
Needs SM_USER/SM_PASS env. Prints ~12 lines. Then read goals.md + progression.md and go."""
import json, os, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm import call, sc, status_line, preflight, missions

try:
    t = json.loads(urllib.request.urlopen("https://game.spacemolt.com/health", timeout=10).read().decode()).get("tick")
except Exception as e:
    t = "?"
print("TICK", t)
print(status_line())
st = sc(call("spacemolt", "get_status"))
sk = st.get("skills") or {}
if isinstance(sk, dict):
    print("SKILLS", " ".join("%s=%s" % (k, v if not isinstance(v, dict) else v.get("level")) for k, v in sk.items()))
mods = st.get("modules") or []
print("MODS", ", ".join(m.get("type_id", str(m)) if isinstance(m, dict) else str(m) for m in mods))
print("SHIP power %s/%s cpu %s/%s" % (st.get("ship", {}).get("power_used"), st.get("ship", {}).get("power_capacity"), st.get("ship", {}).get("cpu_used"), st.get("ship", {}).get("cpu_capacity")))
print("-- missions")
missions("get_active_missions")
print("-- ships")
r = call("spacemolt_ship", "list_ships")
txt = r.get("result") or json.dumps(sc(r))[:600]
print(txt if isinstance(txt, str) else str(txt)[:600])
print("-- preflight")
preflight()
print("NEXT: undocked + no job running? -> scripts/safe_dock.sh. Read goals.md Now + progression.md. res.py for where/route.")
