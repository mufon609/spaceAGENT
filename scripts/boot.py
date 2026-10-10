#!/usr/bin/env python3
"""boot.py - ONE command for session start: tick + game version check + status + skills + modules + missions + ships + preflight.
Needs SM_USER/SM_PASS env. Prints ~12 lines. Then read STATE.md and go."""
import json, os, re, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm import call, sc, status_line, preflight, missions

try:
    h = json.loads(urllib.request.urlopen("https://game.spacemolt.com/health", timeout=10).read().decode())
except Exception:
    h = {}
print("TICK", h.get("tick", "?"))
# The game patches often: STATE.md records the version our notes were last checked against.
try:
    noted = re.search(r"game_version:\s*(\S+)", open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "STATE.md")).read()).group(1)
except Exception:
    noted = "?"
v = h.get("version", "?")
print("VERSION %s (notes checked vs %s)%s" % (v, noted, "" if v == noted else
      " -> CHANGED: read changelog (sm.py call spacemolt get_version), fix affected notes, then update game_version in STATE.md"))
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
print("-- tax")
from sm import tax, stock
tax()
print("-- stock (data/stock.tsv)")
stock()
print("-- preflight")
preflight()
print("NEXT: undocked + no job running? -> scripts/safe_dock.sh. Read STATE.md. res.py for where/route.")
