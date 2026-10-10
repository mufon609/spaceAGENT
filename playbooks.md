# Playbooks

Shell setup (once): `export SM_USER='Alien_Abductee_Gemini' SM_PASS='<from user>'`; `S="python3 scripts/sm.py"`.
Tool-call limits: a call that LAUNCHES a background job must not also sleep/wait (crashes). Launch in one call; poll in later calls with `sleep<=58; tail -1 log`. Always launch with `setsid nohup sh -c '<job>; scripts/safe_dock.sh' < /dev/null > /dev/null 2>&1 &`. NEVER issue several sleeping tool calls in one parallel block (crashes the tool) — one sleep per call, <=58 s. Do not send game actions while a mining job runs (action_in_progress stops stackmine).
No shell? Use MCP spacemolt actions with the same names. MCP session expires: re-login via spacemolt_auth login.

## PB-0 Checklist (run before EVERY trip / loop; `python3 scripts/boot.py` or `$S preflight` does 1-6)
| # | Check | Pass | If fail |
|---|---|---|---|
| 1 | In battle? | not_in_battle | `scripts/safe_dock.sh` |
| 2 | In transit / action pending? | idle | wait (poll `$S status`), never resend |
| 3 | Hull | = max | docked: repair. undocked: go dock |
| 4 | Fuel | >=50% (docked) / >=30% (to undock) | docked: refuel |
| 5 | Cargo | empty before leaving station | `$S dump` |
| 6 | Crew | fit_crew >= minimum_crew | recruit_personnel (docked) |
| 7 | Destination known? | `res.py sys <id>` | lawless OK; leave if scanned/pirates |
| 8 | Session ending / shutdown? | no | PB-8 close-out |
`$S loop` runs 1-6 automatically each trip. Pirates, hull damage, nav error, exception -> automatic emergency dock.
Log lines to watch: `PREFLIGHT FAIL`, `STOP`, `SAFE FAILED`, `EXIT` (killed/crashed) -> run PB-0b.

## PB-0b Start / after any crash
```
python3 scripts/boot.py
```
Undocked and no job running? -> `scripts/safe_dock.sh` first (jobs die silently if a tool call crashes: check `pgrep -f "explore.py|stackmine|sm.py loop"`). Never blind-resend movement. Surprise? Read the action log (knowledge § Tools).

## PB-1 Mining loop (belt + station, same or adjacent system)
```
setsid nohup sh -c 'python3 -u scripts/sm.py loop <belt_sys> <belt_poi> <home_sys> <station> 10 > /tmp/loop.log 2>&1; scripts/safe_dock.sh' < /dev/null > /dev/null 2>&1 &
touch /tmp/sm_stop        # graceful: stop after current trip, docked
touch /tmp/sm_emergency   # abort now -> emergency dock (rm both flags afterwards)
```
Proven: acubens acubens_belt node_beta node_beta_industrial_station (~5.2 min/trip, W/C/Pt/Pd). frontier pioneer_fields deep_range deep_range_outpost (5-7 min/trip, Ti/Ni 1-5 + Fe/Cu; auto-smelts at the dock). unknown_edge unknown_edge_mineral_fields unknown_edge unknown_edge_waystation (belt and station share a system; iridium 4/trip).
Low-yield stop = avg <1.5 over last 10 cycles.

## PB-2 Single-shot mining for a rare ore
Arrive with an EMPTY hold. `$S scout` -> `$S mine 40` (or background). Stop manually when the rare one stops coming.

## PB-3 Buy-mission (Central Nexus)
```
$S call spacemolt accept_mission '{"id":"market_participation_buying"}'
$S call spacemolt buy '{"id":"copper_ore","quantity":10}'
$S active ; $S call spacemolt complete_mission '{"id":"<mission_id>"}' ; $S dump
```

## PB-4 Scout a route (explore.py)
```
setsid nohup sh -c "python3 -u scripts/explore.py 'sysA,!sysB,sysC' [nobelts] [dock] > /tmp/explore.log 2>&1; scripts/safe_dock.sh" < /dev/null > /dev/null 2>&1 &
```
`!sys` = jump through without belt scan. `dock` = dock at each system's first station. Rows are upserted into data/systems_new.tsv + data/belts_new.tsv (commit those). Systems on the route must be adjacent in order: `python3 scripts/res.py route A B` or `sm.py route`.
Two-station systems: dock picks the FIRST listed (first_step -> memorial, not mobile_capital): `travel mobile_capital` + `dock` by hand. Unvisited neighbours: see res.py links vs visited rows.
New station found? Add its base id to SAFE_STATIONS in scripts/sm.py.

## PB-5 Catalog / recipe lookup
`python3 scripts/recipe.py tree <item>` (raw leaves), `recipe.py <item>` (all makers, tags wk/FAC/SHIP), `recipe.py item <item>` (slot/cpu/power/required_skills).

## PB-6 Craft with rented facilities (FAC recipes)
```
$S call spacemolt craft '{"id":"<recipe>","quantity":N,"dry_run":true}'   # venue + cost; no_facility error names nearest public facility
$S call spacemolt craft '{"id":"<recipe>","quantity":N}'
```
Inputs must be in THIS station's storage (`$S dump` first). Workshop (wk) recipes are free but only progress while docked. `quantity` = runs (multi-output recipes round).
Proven: refine_steel @ deep_range_outpost (19cr/run), process_copper_wiring @ deep_range_outpost (17cr/run), forge_titanium_alloy @ frontier_station only (37cr/run), facet_trade_crystal workshop (24 ticks), build_mining_laser_ii workshop (37.5 ticks), carbon_arc_circuit_etching workshop (6 ticks), manufacture_standard_rounds (1 steel -> 5 boxes).
Install a crafted module: docked, `install_mod id=<type_id>` (uninstall the old one first by INSTANCE id from get_ship). Cancel a queued job: craft job_id=<id>.
BUY vs CRAFT (user order S3): compare market price (view_market category=module) with raw cost; buy if cheaper, save the resources (D23).

## PB-7 Capital mission circuits (main credit source, ~20k each, paid in full by Solarian/Nebula/Outer Rim/Crimson)
Dock at a capital (confederacy_central_command, grand_exchange_station, frontier_station, war_citadel) -> `$S missions` -> take "dock at N stations"/"visit N systems" missions -> plan one BFS loop covering all -> PB-4 with `dock`. Max 5 active (abandon weak ones).
Accept missions AT the issuing station; dock objectives only count after accepting. Some missions must be turned in at the issuer (last objective "Report back").
S3 results: Krynn strategic_readiness_assessment 20,000 + last_known_position 8,000; capitals loop 15k+12k+4k+2.5k; unknown_edge reconnaissance 6,000.

## PB-8 Close-out (end of every session)
```
scripts/safe_dock.sh      # stop loops, dock at nearest known station, bank cargo
$S status                 # must show docked=<station>
```
Then update progression.md (location, credits, skills, stock), goals.md, DECISIONS.md, push changed files only (small ones; data/*_new.tsv).

## PB-9 Stack a rare ore with filler jettison (user-approved; jettison ONLY iron_ore/copper_ore)
`scripts/stackmine.py <keep_ore> [target] [max_cycles]` at a lawless belt with a small rare deposit among huge Fe/Cu (zubenelhakrabi_crystal_sand silicon, pioneer_fields titanium/nickel). ONE ML II (beam 12). Hold 65 caps a trip at ~55-59 of the rare ore. Unattended: `setsid nohup sh -c 'python3 -u scripts/stackmine.py silicon_ore 55 700 > /tmp/stack.log 2>&1; scripts/safe_dock.sh' < /dev/null > /dev/null 2>&1 &`. Measured 0.84 Piloting XP/tick. Any other game action while it runs makes it stop (action_in_progress).

## PB-10 Refining/Crafting training (every workshop run = +5 XP to BOTH skills; verified S3)
At any dock with banked ore: `python3 scripts/sm.py train` (smelts all banked iron -> steel 10:1 and copper -> wiring 8:1, waits for completion; sm.py loop calls it after every dump). Campaign at central_nexus: smelt_lead_ingot (4 Pb), roll_lead_sheet (3 ingot), draw_platinum_wire (4 Pt), sinter_tungsten_steel (4 Fe + 2 W -> 3 steel). Runs take 0.3-4 ticks each: 200 runs (=1,000 XP per skill) = 1-12 min docked. Workshop jobs run ONLY while docked.
Piloting grind options (measured): stackmine ~0.84 XP/tick; `sm.py loop frontier pioneer_fields deep_range deep_range_outpost N` 0.67 XP/tick + smelting (~5-7 min/trip).
