# Decisions

Log of real choices. Format: tick | decision needed | thinking | decision | why. Newest at bottom. Keep each entry <=6 lines.
Time = game tick (`curl -s https://game.spacemolt.com/health` -> tick; ~10s/tick, ~360 ticks/hr).

## D1 t2090950 — Voidborn missions pay 0-84%
- Need: keep doing empire missions?
- Thinking: treasury empty (iron 0/1500, deep_core 323/5000). Item rewards still paid in full.
- Decision: only take missions with item rewards or non-empire payers (Market Services). No detours for credit-only Voidborn missions.
- Why: time is better spent stockpiling/exploring than on unpaid work.

## D2 t2091300 — Laser upgrade path
- Need: more beam power (yield super-linear in beam).
- Thinking: ML II 7,007cr on market; ML III not sold anywhere. User rule (later): craft, don't buy items.
- Decision: do NOT buy ML II. Craft it: 3 titanium_alloy + 3 circuit_board (carbon_arc 12 C + 2 Si) + 1 focused_crystal. (Ti alloy route corrected in D18.)
- Why: have C/Fe/Pd. Missing raw: titanium_ore, silicon_ore, focused_crystal source -> exploration target.

## D3 t2091440 — Safety layer before risk
- Need: survive PC shutdowns and lawless trips.
- Decision: preflight checklist each trip + `safe` emergency dock + exception/SIGTERM guard + setsid launch. Tested 3 paths live.
- Why: user requirement; unattended loops otherwise strand the ship in space.

## D4 t2091480 — Train Crafting/Refining (both 0)
- Thinking: workshop crafting is free. smelt_lead_ingot 4 Pb -> 2 ingots, 0.5 tick/run; ~+3 XP/run to BOTH crafting and refining. Lead is our least useful ore (652).
- Decision: burn lead into ingots at central_nexus during docked time (workshop only runs while docked). Outputs stay in storage (stockpile rule).
- Why: crafting skill gates/speeds every module build in D2. Cheapest XP available.

## D5 t2091490 — Lawless/frontier exploration risk
- Need: find titanium, silicon, energy_crystal, silver, nickel, cobalt.
- Thinking: Starter ship cannot be insured but is replaced free; death loses ~70% of fitted modules to a recoverable wreck + cargo; credits/skills/storage safe. Pirates patrol police<=20; being scanned = attack warning; at speed 1 flee is weak. In hyperspace (jump) you are not at a POI.
- Decision: go now with current fit (lasers needed to mine finds). Keep EM disruptor fitted (holds reactor load = Engineering XP). Script leaves any POI with pirates; safe() on damage; fuel guard to return home.
- Why: user approved risk; expected loss small (~10k modules worst case, partly recoverable) vs. unlocking all crafting.
- RESULT S2: ~25 lawless systems crossed, zero pirate contact.

## D6 t2091490 — First exploration target: Solarian space via Pherkad
- Decision: node_gamma>synchrony>pherkad>gsc_0041>antares>homam>furud>nova_terra>sirius, scouting every belt.
- Why: Solarian = mining empire, stations at far end, Solarian treasury may pay missions. Only ~3 unclaimed systems to cross.
- RESULT t2091660: no contact in 3 lawless systems; lawless belts untouched (homam Fe 17k/Cu 69k; antares Fe/Cu 12k; ice/gas 10k-50k). No Ti/Si found.

## D7 t2091700 — Solarian missions vs ore-delivery missions
- Thinking: Sol board has dock-only exploration missions (audit 20,000cr) and ore/refined delivery missions (2,000 Lead Ore -> 20,000cr; 5 circuit_board -> 3,500cr). Delivering ore/refined for credits = selling ore in effect.
- Decision: dock-only missions yes; no ore-delivery missions; raised as Open Question.
- RESULT t2091929: audit paid 20,000cr IN FULL (Solarian treasury pays; Voidborn does not).

## D8 t2091700 — Titanium source
- Thinking: Sol main_belt lists titanium r25 + nickel r70 but drained. Lawless belts near empires are untouched.
- Decision: look for Ti/Ni in less-trafficked systems.
- RESULT t2093000: titanium at frontier pioneer_fields (Outer Rim capital system, r30, ~50 units regenerating).

## D9 t2091929 — Five Capitals circuit (15,000cr, Solarian-paid, expires ~t2152400)
- Decision: accept; first leg Sol -> Haven scouting every belt and docking at stations.
- Why: pays reliably, scouts Nebula space for crafting blockers, exploration XP per new system.
- RESULT t2092400: Haven reached, 7 lawless systems no contact. Haven board added grand_tour (12k) + federation prospectus (20k, PAID IN FULL t2092456).

## D10 t2092300 — Silver at Nusakan skipped
- Thinking: silver r32 uncommon (18 units, p1) vs iron/copper r41 common at 5/cycle; only 7 cargo free.
- Decision: skip; return later with empty hold or bigger ship.

## D11 t2092456 — Craft 8 focused crystals at Grand Exchange
- Thinking: 33 trade_crystal mined at azmidi. focused_crystal needed for ML II (1), cloak (1), survey_scanner_i (2), shield_booster_ii (2).
- Decision: queue facet_trade_crystal x8 (workshop, free) at grand_exchange_station.
- Why: removes the focused_crystal blocker without buying anything.

## D12 t2092456 — Capitals tour order
- BFS: haven>first_step>frontier>nexus_prime>krynn>sol>haven = 84 jumps (best). Stop at nexus_prime for lead-ingot crafting + new-ship check; cobalt at krynn.

## D13 t2092480 — Leave Haven with focused_crystal job unfinished
- Thinking: workshop jobs pause on undock and resume on return; Haven is the final stop.
- Decision: depart now; also accepted deep_space_cartography (Horizon + The Crucible on the loop).
- Why: saves ~28 min idle.

## D14 t2092760 — Swap dead missions for Outer Rim work
- Decision: abandon Voidborn titanium contract + old_charts; take the_memorial (8k), frontier_wayfinder_circuit (20k), debris_field_reports (4.5k).
- RESULT t2093000: all paid in full (32.5k). Credits 103,729.

## D15 t2093000 — Mine titanium for an Outer Rim mining contract
- Thinking: OR titanium_extraction_contract (3,500; mine 20 Ti, ore stays mine). pioneer_fields Ti r30 p1-3; deep_range_outpost 1 jump for banking.
- Decision: sm.py loop frontier pioneer_fields deep_range deep_range_outpost. Also local_sector_survey (route-compatible).
- Why: titanium is a hard crafting blocker.

## D16 t2093100 — Silicon plan: Zubenelhakrabi detour on the way home
- Thinking: GAME-PLAN names Zubenelhakrabi Crystal Sand (Silicon r40); 8 jumps from first_step, then 11 to nexus_prime.
- Decision: fly first_step>...>zubenelhakrabi, mine silicon, continue to nexus_prime; craft circuit boards at central_nexus (carbon there); ML II at haven (focused crystals there).
- Why: one route closes every ML II blocker without buying anything.

## D17 t2093200 — Stop titanium grind at 13 Ti
- Thinking: Fe/Cu regenerated to 6-7/pick, hold fills in ~12 cycles; Ti/trip fell 5 -> 4 -> 3 -> 1.
- Decision: stop; keep contract for the Resonance Miner (5.5x hold). 13 Ti covers ML II.
- Why: exploration trains Piloting faster and capitals pay 27k+.

## D18 t2093100 — Use rented station facilities for facility-only steps
- Thinking: titanium_alloy has no ore-based workshop recipe (onboard_ = ship-only). Station production facilities rent per run. Facility fees are a service; outputs come from our own ore.
- Decision: refine_steel x3 (6 steel, 57cr) + process_copper_wiring x20 (40 wiring, 340cr) at deep_range_outpost; forge_titanium_alloy x4 (148cr) at Frontier Station.
- RESULT t2093125: 4 titanium_alloy made. Remaining ML II input: 3 circuit_board (needs 2 silicon).

## D19 t2094013 — Close-out (user request)
- Event: explore.py died right after jumping into zubenelhakrabi (session pause). Ship sat undocked; session idled -> Galactic Salvage Authority towed it to Ramen's Rest (last_light), ~500cr. Confirms forum tow mechanic. Crystal Sand POI not scanned (explore.py skipped unknown POI types; fixed).
- Decision: end docked at ramens_rest; deposit titanium_alloy 4, steel 2, Ti 1 there; add all discovered stations to SAFE_STATIONS so safe() finds the nearest one anywhere.
- Next session: zubenelhakrabi Crystal Sand is 5 jumps (fang>errai>alsciaukat>sheliak>zubenelhakrabi): scan + mine silicon, then craft ML II (restores >=90% power for Engineering XP; Engineering 12 dropped load to 26/30).
