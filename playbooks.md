# Playbooks

Shell setup (once): `export SM_USER='Alien_Abductee_Gemini' SM_PASS='<from user>'`; `S="python3 scripts/sm.py"`.
Tool-call limits: a call that LAUNCHES a background job must not also sleep/wait (crashes). Launch in one call; poll in later calls with `scripts/poll.sh <log> 50`. Always launch with `setsid nohup ... < /dev/null &` (survives tool crashes).
No shell? Use MCP spacemolt actions with the same names.

## PB-0 Checklist (run before EVERY trip / loop; `$S preflight` does 1-6)
| # | Check | Pass | If fail |
|---|---|---|---|
| 1 | In battle? (spacemolt_battle status) | not_in_battle | `scripts/safe_dock.sh` |
| 2 | In transit / action pending? | idle | wait (poll `$S status`), never resend |
| 3 | Hull | = max | docked: repair. undocked: go dock |
| 4 | Fuel | >=50% (docked) / >=30% (to undock) | docked: refuel |
| 5 | Cargo | empty before leaving station | `$S dump` |
| 6 | Crew | fit_crew >= minimum_crew | recruit_personnel (docked) |
| 7 | Destination known? | resources.md row | lawless OK; read knowledge § Risk; leave if scanned/pirates |
| 8 | Session ending / shutdown? | no | PB-8 close-out |
`$S loop` runs 1-6 automatically each trip. Pirates, hull damage, nav error, exception -> automatic emergency dock.
Log lines to watch: `PREFLIGHT FAIL`, `STOP`, `SAFE FAILED`, `EXIT` (killed/crashed) -> run PB-0b.

## PB-0b Start / after any crash
```
$S status ; $S active ; $S preflight
```
Undocked and no loop running? -> `scripts/safe_dock.sh` first. Never blind-resend movement. Surprise? Read the action log (knowledge § Tools).

## PB-1 Mining loop (any belt + nearby station)
```
setsid nohup python3 -u scripts/sm.py loop <belt_sys> <belt_poi> <home_sys> <station> 10 > /tmp/loop.log 2>&1 < /dev/null &
scripts/poll.sh /tmp/loop.log 50
touch /tmp/sm_stop        # graceful: stop after current trip, docked
touch /tmp/sm_emergency   # abort now -> emergency dock
```
Proven: acubens acubens_belt node_beta node_beta_industrial_station (~5.2 min/trip, ~W19 C19 Pt3 Pd2). frontier pioneer_fields deep_range deep_range_outpost (~8 min/trip, Ti 1-5 + Fe/Cu/Ni).
The belt system must be adjacent to the station system. Low-yield stop = avg <1.5 over last 10 cycles.

## PB-2 Single-shot mining for a rare ore
Arrive with an EMPTY hold. `$S scout` -> `$S mine 40` (or background). Stop manually when the rare one stops coming (`pkill -f "sm.py mine"`).

## PB-3 Buy-mission (Central Nexus)
```
$S call spacemolt accept_mission '{"id":"market_participation_buying"}'
$S call spacemolt buy '{"id":"copper_ore","quantity":10}'
$S active ; $S call spacemolt complete_mission '{"id":"<mission_id>"}' ; $S dump
```

## PB-4 Scout a route (explore.py)
```
setsid nohup python3 -u scripts/explore.py 'sysA,!sysB,sysC' dock > /tmp/explore.log 2>&1 < /dev/null &
scripts/poll.sh /tmp/explore.log 50        # repeat; prints only new lines
python3 scripts/explore.py md              # markdown rows -> resources.md
```
`!sys` = pass through without belt scan (already recorded). `dock` = dock at each system's first station (refuels <70%).
Systems on the route must be adjacent in order: build it with BFS on get_map or `$S route <target>`.
Two-station systems: dock picks the FIRST listed (first_step -> memorial, not mobile_capital): dock the right one by hand.
New station found? Add its base id to SAFE_STATIONS in scripts/sm.py.

## PB-5 Catalog / recipe lookup
`python3 scripts/recipe.py tree <item>` (full hand-craftable tree -> raw leaves), `recipe.py <item>` (all makers, tags wk/FAC/SHIP), `recipe.py item <item>` (slot/cpu/power/required_skills).

## PB-6 Craft with rented facilities (FAC recipes)
```
$S call spacemolt craft '{"id":"<recipe>","quantity":N,"dry_run":true}'   # venue + cost; no_facility error names nearest public facility
$S call spacemolt craft '{"id":"<recipe>","quantity":N}'                  # runs ~0.1 tick/run, survives undock
```
Inputs must be in THIS station's storage (`$S dump` first). Workshop (wk) recipes are free but only progress while docked.
Proven: refine_steel @ deep_range_outpost (19cr/run), process_copper_wiring @ deep_range_outpost (17cr/run), forge_titanium_alloy @ frontier_station (37cr/run), facet_trade_crystal workshop (24 ticks/run, free).
Install a crafted module: docked, `$S call spacemolt install_mod '{"id":"<module_id>"}'` (uninstall the old one first if slots are full; keep it in storage).

## PB-7 Capital mission circuits (main credit source, ~20k each, paid in full by Solarian/Nebula/Outer Rim)
Dock at a capital (confederacy_central_command, grand_exchange_station, frontier_station) -> `$S missions` -> take "dock at N stations"/"visit N systems" missions -> plan one BFS loop covering all -> PB-4 with `dock`.
Accept missions AT the issuing station; dock objectives only count after accepting (re-dock if needed).

## PB-8 Close-out (end of every session)
```
scripts/safe_dock.sh      # stop loops, dock at nearest known station, bank cargo
$S status                 # must show docked=<station>
```
Then update progression.md (location, credits, skills, stockpile), goals.md (next steps), DECISIONS.md, commit.
