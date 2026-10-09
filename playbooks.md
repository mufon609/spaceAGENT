# Playbooks

Shell setup (once): `export SM_USER='Alien_Abductee_Gemini' SM_PASS='<from user>'`; `S="python3 scripts/sm.py"`.
Wrap long loops: `timeout 280 $S mine 20` (bash calls cap ~5 min). No shell? Use MCP spacemolt actions with the same names.

## PB-0 Start / after any crash
```
$S status    # where am I, fuel, cargo, hull
$S active    # missions
```

## PB-1 Acubens stockpile loop (C/W/Pb/Pt/Pd) — also best Piloting XP
Start docked node_beta_industrial_station or node_gamma_relay_station.
```
$S jump acubens          # 60s, lands acubens_belt
$S scout                 # log to resources.md if changed
$S mine 20 2             # stops: cargo full / error / pirates / avg<2
$S jump node_beta        # or node_gamma
$S go node_beta_industrial_station
$S dock
$S dump
```
Per trip: ~W20 C21 Pd2, Pt 0-2; ~6 min; 2 fuel. Refuel <30 fuel (MCP spacemolt action=refuel, docked).

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
