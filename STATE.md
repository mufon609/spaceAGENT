# STATE (volatile; replace stale lines in place at every checkpoint)
game_version: 0.613.4   (notes last checked against this; boot.py compares)
last_update: t2099600 (S4 probe session from Claude Code: missions, tax, EXP-2)

## Ship (active)
- Threshold id 1560ab3025cd17ccbce5701e2af70969, T0 starter (uninsurable, free replacement). Hull 75, Shield 80, Fuel 95, Cargo 65, Slots 1W/2D/2U, speed 1, power 30, CPU 16.
- Fit: mining_laser_ii e4eeee49de1176906fabb9be2130fb28 (U, ONE laser = beam 12) | utility 2 EMPTY | autocannon_i 06c4502af99ff91b47e7c5abb010c2b9 (W, 0 ammo: reinstall emptied it; 4 standard_rounds_box @ ramens_rest) | shield_recharger_i 1f0da81d23fcc8b6f532f84796d7d916 (D) | thermal_hull_hardener ca1f562c57b452dcc8b03b181e8be2f0 (D). Power 18/30 (Engineering passive OFF; 2x ML II = 29/30 turns it on).
- Docs v0.612.7: Threshold starter got a pulse laser; `refit_ship` resets a hull to class spec for free (check before using: may change the fit).
- Stored modules: spare ML II @ deep_range_outpost; ML I, cargo_expander_ii, em_disruptor_i, 4 standard_rounds_box @ ramens_rest.
- LOCATION t2099600: DOCKED ramens_rest (last_light, Outer Rim). Hold empty. Fuel 84/95. Respawn/home base central_nexus. Nomadic: no owned/leased anything.

## Skills (t2098845; crafting +25 +~25 at t2099600)
piloting 9 (1,186/3,525) | mining 9 (1,951/3,525) | engineering 12 (3,125/5,940) | deep_core_mining 8 (2,013/2,860) | navigation 6 (1,234/1,740) | exploration 4 (235/900) | refining 3 (270/585) | crafting 3 (290/585) | trading 3 | leadership 1 | gunnery/weapons/tactics/xenobiology/scanning small | bounty_hunting 0 | stealth 0 | voidborn_mastery 0 (empire signature skill: only from Voidborn empire missions)

## Credits + tax
147,198 wallet t2099600 (+3,500 workshop mission; 9,867 moved to tax prepay). Tax: owed ~11,363 (Voidborn income 6% + property 0.75%), prepaid 12,499, next assessment ~t2116800 (~48h). Boot tops it up automatically (`sm.py tax`).
153,565 (t2098845). History: 102,410 (S3 start t2094400) -> 153,565. S3 income +71,000 (readiness 20k, last_known 8k, five_capitals 15k, grand_tour 12k, cartography 4k, survey 2.5k, titanium contract 3.5k, reconnaissance 6k). Spend: gifts 15,000 (user order, D29), autocannon 1,500, cargo_expander_ii 1,908, fuel ~1,500.

## Stockpile (never sell) — full table: data/stock.tsv (`sm.py stock`, auto at boot; never hand-edit)
Summary t2099600: central_nexus C 2019, W 927, Pt 725, Pb 638, Pd 303 | deep_range_outpost Ni 159, Ti 134, wiring 94, steel 72, spare ML II | ramens_rest Si 243, trade_crystal 25, wiring 16, steel 10, boards 3, glass 4, slug cases 10, modules (ML I, cargo_expander_ii, em_disruptor_i) | **unknown_edge_waystation iridium 20**, Al 42, C 41, V 16, dark_matter_residue 3 | node_beta C 339, W 223 | node_gamma exotic_matter 10 | haven Cu/Fe scraps.
Consolidation hub = **central_nexus** (Voidborn shipyard + biggest pile). Move stock there when a trip passes by; mine/store elsewhere only when hauling would waste a trip. Crafting inputs must be in the storage of the station where you craft.

## Missions
Active: NONE. Done t2099600: workshop_production_run 3,500 (any 5 craft RUNS; repeatable at many boards?). Leads: exotic_crystal_synthesis (8,000; needs 6 exotic_matter, 10 @ node_gamma), wh_intro wormhole missions (500cr), grazer hunts (1.0-1.3k).

## Now (priority order) — strategy: docs/strategy.md (Voidborn ghost prospector)
1. **absence build at central_nexus** (Voidborn-only design: commission only at a Voidborn shipyard). Haul to central_nexus: Si ~65 + trade_crystal 25 + boards + wiring 16 (ramens_rest), iridium 6+ (unknown_edge, take all 20), Ni 24+ + wiring + steel (deep_range_outpost). C/Pt/Pd already there. Route ramens_rest > unknown_edge > ... (res.py route last_light nexus_prime). Then `commission_quote` there, craft components (superconductor is FAC: dry_run for venue), commission.
2. **Fit**: survey_scanner_i craft (same trip: needs carbon at central_nexus) + cloaking_device_i later. Skill reqs are NOT enforced (EXP-2 confirmed) -> fit them immediately, start Stealth/Scanning XP.
3. Engineering passive: refit to >=90% load whenever docked where the spare ML II is (deep_range_outpost).
4. Counter-recon at busy systems (docs/counter-recon.md); Last Light chat is near-dead (2 msgs in 3 weeks) — post where players are.
5. Cheap credits: workshop_production_run (3,500 for 5 craft runs) whenever a board offers it; capital circuits (PB-7). Voidborn missions at central_nexus also train voidborn_mastery.

## Open Questions for User
- Q4: ore/refined DELIVERY missions (Sol: 2,000 lead ore -> 20,000cr; the_long_haul 10 Ti alloy -> 10,000) — allowed as mission payout or forbidden as selling ore? Default forbidden. OPEN.
- Q5 (cloaking_dust for Stealth 1) and Q7 (Piloting grind) are superseded by the stealth/intel strategy (DECISIONS D34).
