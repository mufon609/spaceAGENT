#!/bin/sh
# EMERGENCY DOCK. Run before shutting the PC down, or whenever something looks wrong.
# Stops every running loop, waits out any jump, flees battle, flies to the nearest known
# station (or home with: safe_dock.sh home), docks, banks cargo. Exit 0 = docked.
# Needs SM_USER / SM_PASS in the environment.
cd "$(dirname "$0")" || exit 1
touch /tmp/sm_emergency
pkill -f "sm.py loop" 2>/dev/null
python3 -u sm.py safe "$@"
