# Playbooks

Shell setup (once): `export SM_USER='Alien_Abductee_Gemini' SM_PASS='<from user>'`; `S="python3 scripts/sm.py"`.
Bash tool calls crash near 5 min: wrap with `timeout 280`, poll background jobs with `sleep <=145`.
No shell? Use MCP spacemolt actions with the same names.

## PB-0 Start / after any crash
```
$S status    # where am I, fuel, cargo, hull
$S active    # missions
```
On tool crash mid-travel: movement still completes server-side. Run `$S status`, never blind-resend.

## PB-1 Acubens stockpile loop (C/W/Pb/Pt/Pd) — best Piloting XP (~30/trip)
Start docked node_beta_industrial_station. Run in background, supervise by tailing log:
```
nohup python3 -u scripts/sm.py loop acubens acubens_belt node_beta node_beta_industrial_station 6 > /tmp/loop.log 2>&1 &
sleep 140; grep -E "^(trip|TOTAL|STOP|LOOP|refuel|cr=)" /tmp/loop.log | tail -4
touch /tmp/sm_stop        # graceful stop after current trip (ends docked)
```
Loop auto-stops on: hull damage, pirates at belt, nav/dock error. Refuels <40% fuel.
Measured S2 (6 trips, ~5.2 min each, ~3 fuel each): total W115 C116 Pt18 Pd12 Pb6. Per trip ~W19 C19 Pt3 Pd2.
If a trip prints STOP: run PB-0, read the STOP line, fix, restart.

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

## PB-5 Catalog lookup (cheap)
`$S call spacemolt_catalog catalog '{"type":"items","id":"<item>"}'` (also type ships/recipes, search=...)
