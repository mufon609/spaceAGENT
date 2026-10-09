# Playbooks

Shell setup (once): `export SM_USER='Alien_Abductee_Gemini' SM_PASS='<from user>'`; `S="python3 scripts/sm.py"`.
Bash tool calls crash near 2-5 min: keep each call <=110s; run loops with nohup and poll the log.
No shell? Use MCP spacemolt actions with the same names.

## PB-0 Checklist (run before EVERY trip / loop; `$S preflight` does all of it)
| # | Check | Pass | If fail |
|---|---|---|---|
| 1 | In battle? (spacemolt_battle status) | not_in_battle | `scripts/safe_dock.sh` |
| 2 | In transit / action pending? | idle | wait (poll `$S status`), never resend |
| 3 | Hull | = max | docked: repair. undocked: go dock |
| 4 | Fuel | >=50% (docked) / >=30% (to undock) | docked: refuel |
| 5 | Cargo | empty before leaving station | `$S dump` |
| 6 | Crew | fit_crew >= minimum_crew | recruit_personnel (docked) |
| 7 | Destination security known & allowed | in resources.md | ask user |
| 8 | Shutdown coming? | no | `scripts/safe_dock.sh` |
`$S loop` runs 1-5 automatically each trip; any failure, pirates, hull damage, or nav error -> automatic emergency dock.

## PB-0b Start / after any crash
```
$S status ; $S active ; $S preflight
```
On tool crash mid-travel: movement still completes server-side. Never blind-resend.

## PB-1 Acubens stockpile loop (C/W/Pb/Pt/Pd) — best Piloting XP (~30/trip)
Start anywhere in node_beta/acubens area (loop resumes from any state).
```
nohup python3 -u scripts/sm.py loop acubens acubens_belt node_beta node_beta_industrial_station 10 > /tmp/loop.log 2>&1 &
sleep 100; grep -E "^(PREFLIGHT|trip|TOTAL|STOP|SAFE|LOOP|cr=)" /tmp/loop.log | tail -4
touch /tmp/sm_stop        # graceful: stop after current trip, docked
touch /tmp/sm_emergency   # abort now -> emergency dock
```
Measured S2: ~5.2 min/trip, ~3 fuel/trip, per trip ~W19 C19 Pt3 Pd2 Pb1.
If log shows STOP/SAFE FAILED: run PB-0b, read the line, fix, restart.

## PB-2 Pherkad Cu/Fe (mission units only)
node_beta -> node_alpha -> synchrony -> pherkad (3 jumps), `$S go pherkad_null_rift`, `$S mine 40`. 1 unit/cycle. Return same path.

## PB-3 Buy-mission (Central Nexus)
```
$S call spacemolt accept_mission '{"id":"market_participation_buying"}'
$S call spacemolt buy '{"id":"copper_ore","quantity":10}'
$S active ; $S call spacemolt complete_mission '{"id":"<mission_id>"}' ; $S dump
```

## PB-4 Scout a system
```
$S route <sys> ; $S jump <sys> ; $S sys     # read Security first; unknown/lawless & unapproved -> jump back
$S go <belt> ; $S scout                     # paste line into resources.md
```
New station found? Add its base id to SAFE_STATIONS in scripts/sm.py and to resources.md.

## PB-5 Catalog lookup (cheap)
`$S call spacemolt_catalog catalog '{"type":"items","id":"<item>"}'` (also type ships/recipes, search=...)
