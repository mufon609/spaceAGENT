# Playbooks

Shell setup (once): `export SM_USER='Alien_Abductee_Gemini' SM_PASS='<from user>'`; `S="python3 scripts/sm.py"`.
Tool-call limits: a call that LAUNCHES a background job must not also sleep/wait (crashes). Launch in one call; poll in later calls with `scripts/poll.sh <log> 50`. Always launch with `setsid nohup ... < /dev/null &`. NEVER issue several sleeping tool calls in one parallel block (crashes the tool) — one sleep per call, <=58 s.
No shell? Use MCP spacemolt actions with the same names. MCP session expires: re-login via spacemolt_auth login.

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
Undocked and no loop running? -> `scripts/safe_dock.sh` first (explore.py jobs die silently if a tool call is interrupted: check `pgrep -f explore.py`). Never blind-resend movement. Surprise? Read the action log (knowledge § Tools).

## PB-1 Mining loop (any belt + nearby station)
```
setsid nohup python3 -u scripts/sm.py loop <belt_sys> <belt_poi> <home_sys> <station> 10 > /tmp/loop.log 2>&1 < /dev/null &
scripts/poll.sh /tmp/loop.log 50
touch /tmp/sm_stop        # graceful: stop after current trip, docked
touch /tmp/sm_emergency   # abort now -> emergency dock (rm both flags afterwards)
```
Proven: acubens acubens_belt node_beta node_beta_industrial_station (~5.2 min/trip, ~W19 C19 Pt3 Pd2). frontier pioneer_fields deep_range deep_range_outpost (~8 min/trip, Ti 1-12 + Fe/Cu/Ni; Ti now drained).
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
`!sys` = pass through without belt scan (already recorded). `dock` = dock at each system's first station (refuels <70%). `nobelts` = skip all scans.
Systems on the route must be adjacent in order: get the path with `find_route` (resources.md ROUTES has verified chains).
Two-station systems: dock picks the FIRST listed (first_step -> memorial, not mobile_capital): `travel mobile_capital` + `dock` by hand. Without `dock` flag explore ends in space at a POI: travel to the station + dock by hand.
New station found? Add its base id to SAFE_STATIONS in scripts/sm.py.

## PB-5 Catalog / recipe lookup
`python3 scripts/recipe.py tree <item>` (full hand-craftable tree -> raw leaves), `recipe.py <item>` (all makers, tags wk/FAC/SHIP), `recipe.py item <item>` (slot/cpu/power/required_skills).

## PB-6 Craft with rented facilities (FAC recipes)
```
$S call spacemolt craft '{"id":"<recipe>","quantity":N,"dry_run":true}'   # venue + cost; no_facility error names nearest public facility
$S call spacemolt craft '{"id":"<recipe>","quantity":N}'                  # runs ~0.1 tick/run, survives undock
```
Inputs must be in THIS station's storage (`$S dump` first). Workshop (wk) recipes are free but only progress while docked. `quantity` on a multi-output recipe = outputs wanted (carbon_arc_circuit_etching quantity 2 or 3 -> 1 run = 3 boards).
Proven: refine_steel @ deep_range_outpost (19cr/run), process_copper_wiring @ deep_range_outpost (17cr/run), forge_titanium_alloy @ frontier_station (37cr/run), facet_trade_crystal workshop (24 ticks/run, free), build_mining_laser_ii workshop (37.5 ticks), carbon_arc_circuit_etching workshop (6 ticks).
Install a crafted module: docked, `$S call spacemolt install_mod '{"id":"<module_type_id>"}'` (uninstall the old one first by instance id; keep it in storage). Cancel a queued job: craft job_id=<id> (refunds inputs).
BUY vs CRAFT (user order S3): compare market price (view_market category=module) with raw cost; buy if cheaper, save the resources (D23: cargo_expander_ii bought 1,908).

## PB-7 Capital mission circuits (main credit source, ~20k each, paid in full by Solarian/Nebula/Outer Rim/Crimson)
Dock at a capital (confederacy_central_command, grand_exchange_station, frontier_station, war_citadel) -> `$S missions` -> take "dock at N stations"/"visit N systems" missions -> plan one BFS loop covering all -> PB-4 with `dock`. Max 5 active missions (abandon weak ones).
Accept missions AT the issuing station; dock objectives only count after accepting (re-dock if needed). Some missions must be turned in at the issuer (check last objective "Report back").
S3 results: Krynn strategic_readiness_assessment 20,000 (6 Crimson stations) + last_known_position 8,000 (dock Ironhearth); capitals loop 15k+12k+4k+2.5k.

## PB-8 Close-out (end of every session)
```
scripts/safe_dock.sh      # stop loops, dock at nearest known station, bank cargo
$S status                 # must show docked=<station>
```
Then update progression.md (location, credits, skills, stockpile), goals.md (next steps), DECISIONS.md, commit.

## PB-9 Stack a rare ore with filler jettison (user-approved Q6, S3; jettison ONLY iron_ore/copper_ore)
Use at a lawless belt with a small rare deposit among huge Fe/Cu (e.g. zubenelhakrabi_crystal_sand silicon). Arrive with empty hold, beam LOW (ML II + cargo_expander_ii = cargo 115, beam 12).
Script logic (save as scripts/stackmine.py or paste; stdlib, imports sm.py `call, sc`):
```
loop up to max_cycles: r=call("spacemolt","mine"); s=sc(r); d=s["details"]; ship=s["ship"]
  total[keep]+=d["quantity"] if d["resource_id"]==keep
  stop if pirates (s["location"]["nearby_pirate_count"]) or hull<max_hull or /tmp/sm_emergency or total>=target
  if ship["cargo_used"]>=ship["cargo_capacity"]-6:
     for it in sc(call("spacemolt","get_status"))["cargo"]: (item_id, quantity)
        if item_id in ("iron_ore","copper_ore"): call("spacemolt","jettison",{"id":item_id,"quantity":quantity})
```
Chain a safe dock so an unattended run never leaves the ship parked: `setsid nohup sh -c 'python3 -u scripts/stackmine.py silicon_ore 40 160 > /tmp/stack2.log 2>&1; scripts/safe_dock.sh > /tmp/safe.log 2>&1' < /dev/null > /dev/null 2>&1 &`
Yield facts: beam12 gives +2-3 Si/pick (p-capped), ~1 pick in 3-4; cycle ~15 s. Silicon deposit shrinks as it is mined: recheck `scout` first.
