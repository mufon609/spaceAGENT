# Decisions

Log of real choices. Format: tick | decision needed | thinking | decision | why. Newest at bottom. Keep each entry <=6 lines.
Time = game tick (`curl -s https://game.spacemolt.com/health` -> tick; ~10s/tick, ~360 ticks/hr). NOTE: S3 stamps t2096xxx run ~150 ticks ahead of the real tick (estimated by hand); always read the health endpoint.

## D1 t2090950 — Voidborn missions pay 0-84%
- Thinking: treasury empty. Item rewards still paid in full.
- Decision: only take missions with item rewards or non-empire payers. No detours for credit-only Voidborn missions.
- Why: time is better spent stockpiling/exploring than on unpaid work.

## D2 t2091300 — Laser upgrade path
- Thinking: ML II 7,007cr on market; ML III not sold anywhere. User rule then: craft, don't buy (superseded by D23: buy if cheaper).
- Decision: craft ML II: 3 titanium_alloy + 3 circuit_board (carbon_arc 12 C + 2 Si) + 1 focused_crystal.
- RESULT t2095230: crafted + installed at ramens_rest (power 29/30).

## D3 t2091440 — Safety layer before risk
- Decision: preflight checklist each trip + `safe` emergency dock + exception/SIGTERM guard + setsid launch. Tested 3 paths live.
- Why: unattended loops otherwise strand the ship in space.

## D4 t2091480 — Train Crafting/Refining (both 0)
- Decision: burn lead into ingots at central_nexus during docked time (smelt_lead_ingot 0.5 tick/run, +3 XP both skills). Outputs stay in storage.

## D5 t2091490 — Lawless/frontier exploration risk
- Thinking: starter ship uninsurable but replaced free; death loses ~70% fitted modules to a recoverable wreck; credits/skills/storage safe. Pirates patrol police<=20.
- Decision: go with current fit; script leaves any POI with pirates; safe() on damage; fuel guard.
- RESULT S2+S3: ~100 lawless systems crossed, zero pirate contact.

## D6 t2091490 — First exploration target: Solarian space via Pherkad
- RESULT t2091660: lawless belts untouched (Fe/Cu 12k-100k, ice/gas 10k-50k). No Ti/Si found there.

## D7 t2091700 — Solarian missions vs ore-delivery missions
- Thinking: Sol board has dock-only exploration missions (audit 20,000cr) and ore/refined delivery missions (2,000 Lead Ore -> 20,000cr). Delivering ore for credits = selling ore in effect.
- Decision: dock-only missions yes; no ore-delivery missions; raised as Open Question Q4 (still open).
- RESULT t2091929: audit paid 20,000cr IN FULL (Solarian treasury pays; Voidborn does not).

## D8 t2091700 — Titanium source
- Decision: look for Ti/Ni in less-trafficked systems. RESULT t2093000: titanium at frontier pioneer_fields (r30, ~50 units, regenerating); drained to 0 by t2096000 (4 miners).

## D9 t2091929 — Five Capitals circuit (15,000cr)
- RESULT: paid in full t2095400 (Sol). Haven board added grand_tour (12k, paid) + federation prospectus (20k, paid t2092456).

## D10 t2092300 — Silver at Nusakan skipped (18 units, p1; hold nearly full of Fe/Cu).

## D11 t2092456 — Craft 8 focused crystals at Grand Exchange
- Decision: queue facet_trade_crystal x8 (workshop, free). RESULT t2095000: cancelled after 1 run (refund 28 trade_crystal, carried) to avoid 27 min idle dock; 29 trade_crystal now at ramens_rest.

## D12 t2092456 — Capitals tour order
- BFS: haven>first_step>frontier>nexus_prime>krynn>sol>haven = 84 jumps (best). Completed S3.

## D13 t2092480 — Leave Haven with focused_crystal job unfinished (workshop jobs pause on undock). Accepted deep_space_cartography (done S3, 4k).

## D14 t2092760 — Swap dead missions for Outer Rim work
- RESULT t2093000: memorial 8k + wayfinder 20k + debris 4.5k paid in full.

## D15 t2093000 — Mine titanium for OR titanium_extraction_contract (3,500; mine 20 Ti; ore stays ours).
## D16 t2093100 — Silicon plan: Zubenelhakrabi Crystal Sand (done S3).
## D17 t2093200 — Stop titanium grind at 13 Ti (Ti/trip fell 5->1). Contract abandoned S3, re-accepted t2095900 (see below).

## D18 t2093100 — Use rented station facilities for facility-only steps
- Decision: refine_steel (19cr/run) + process_copper_wiring (17cr/run) at deep_range_outpost; forge_titanium_alloy (37cr/run) at frontier_station.
- RESULT t2093125: 4 titanium_alloy made.

## D19 t2094013 — Close-out (user request)
- Event: explore.py died after jumping into zubenelhakrabi (session pause). Ship sat undocked; towed to Ramen's Rest, ~500cr.
- Decision: end docked; add all discovered stations to SAFE_STATIONS.

## D20 t2094100 — Silicon run + home via unexplored route
- Decision: Crystal Sand (Si r40 p2; iron/copper p5000; 9 harmless grazers): 18 cycles -> Si 11. Returned to central_nexus via 11 unexplored lawless jumps, scanning belts (gold 681 p34 at garnet_belt).
- RESULT t2094390: 0 contact, fuel 89->59. 6 circuit_board crafted at central_nexus.
- Cost: forgot titanium_alloy (4) was at ramens_rest -> ML II delayed; plan item locations before leaving a station.

## D21 t2094500 — Crimson capital circuit instead of straight home
- Decision: abandon titanium_extraction (13/20), accept strategic_readiness_assessment (20k, 6 Crimson stations, report back at war_citadel); last_known_position (8k) accepted after.
- RESULT t2095100: +20,000 and +8,000 paid in full (Crimson). Chain next damage_assessment is combat: skipped.

## D22 t2095100 — Complete capital loop krynn>sol>haven
- RESULT: five_capitals +15,000, grand_tour +12,000, cartography +4,000, local_survey +2,500. Credits 102k -> 163k in ~1 hr. Abandoned courier_to_haven (needed 5 silver, none provided).

## D23 t2095375 — User order: stack rare ores; buy upgrades when cheaper than crafting
- Event: user: stack up silicon/titanium_ore when found; if an upgrade (not ship) is cheaper to buy than craft from raw at exchange rates, buy it and save resources.
- Thinking: Si/Ti ore are NOT sold (only bids 180/15cr) -> must mine. Ramen's Rest t2095372: cargo_expander_ii 1,908 (craft = CE I + 2 Ti alloy + 4 flex polymer + 2 boards) | mining_laser_ii 7,308 (craft = 3 Ti alloy = 9 Ti ore + 3 boards + focused crystal: raw cost far below 7.3k, so craft ML II when Ti is in stock) | survey_scanner_ii 30,800 | titanium_alloy not sold.
- Decision: BUY cargo_expander_ii (1,908) in place of ML II #2 (stored): cargo 115, beam 12, power 24/30. Si yield is p2-capped so lower beam loses little.
- RESULT t2095450: Crystal Sand fill: 37 Si per 42 cycles (vs ~4 Si per fill before). Rule of thumb: buy when market price < roughly 2x raw value of scarce inputs and crafting needs a blocked input (Ti alloy).

## D24 t2095950 — Filler jettison approved; stackmine recorded as PB-9
- Event: user approved jettisoning worthless iron/copper filler while mining rare ore (conditional on keeping the knowledge base current) and approved recording the script logic in playbooks.md (PB-9). Q4 (delivery missions) and Q5 (cloaking dust) remain open.
- Decision: scripts/stackmine.py (local only) jettisons ONLY iron_ore/copper_ore when hold >= cap-6; chained with safe_dock.sh. Pushed resources.md (routes, stations, belt table, game-vs-repo memory).
- Why: hold 115 fills with filler after ~4 Si per trip otherwise.

## D25 t2095900 — Re-accept titanium_extraction_contract (OR, 3,500) at deep_range_outpost
- Result: 4 loop trips mined 19+12+9+6+1 Ti total (47 banked at deep_range_outpost); pioneer_fields Ti hit 0 (competition + slow regen ~1/min); contract ~10/20, still open.
