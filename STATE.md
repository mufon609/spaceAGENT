# STATE (volatile; replace stale lines in place at every checkpoint)
game_version: 0.613.4   (notes last checked against this; boot.py compares)
last_update: t2098845 (S3 close-out) — repo reorganised t2099202, no play since

## Ship (active)
- Threshold id 1560ab3025cd17ccbce5701e2af70969, T0 starter (uninsurable, free replacement). Hull 75, Shield 80, Fuel 95, Cargo 65, Slots 1W/2D/2U, speed 1, power 30, CPU 16.
- Fit: mining_laser_ii e4eeee49de1176906fabb9be2130fb28 (U, ONE laser = beam 12) | utility 2 EMPTY | autocannon_i 09e7c93730b3074b5512a76f9142aadd (W, 500 rounds) | shield_recharger_i 1f0da81d23fcc8b6f532f84796d7d916 (D) | thermal_hull_hardener ca1f562c57b452dcc8b03b181e8be2f0 (D). Power 18/30 (Engineering passive OFF; 2x ML II = 29/30 turns it on).
- Docs v0.612.7: Threshold starter got a pulse laser; `refit_ship` resets a hull to class spec for free (check before using: may change the fit).
- Stored modules: spare ML II @ deep_range_outpost; ML I, cargo_expander_ii, em_disruptor_i, 4 standard_rounds_box @ ramens_rest.
- LOCATION: DOCKED ramens_rest (last_light, Outer Rim). Hold empty. Fuel 84/95. Home base central_nexus.

## Skills (t2098845)
piloting 9 (1,186/3,525) | mining 9 (1,951/3,525) | engineering 12 (3,125/5,940) | deep_core_mining 8 (2,013/2,860) | navigation 6 (1,234/1,740) | exploration 4 (235/900) | refining 3 (270/585) | crafting 3 (290/585) | trading 3 | leadership 1 | gunnery/weapons/tactics/xenobiology/scanning small | bounty_hunting 0 | stealth 0

## Credits
153,565 (t2098845). History: 102,410 (S3 start t2094400) -> 153,565. S3 income +71,000 (readiness 20k, last_known 8k, five_capitals 15k, grand_tour 12k, cartography 4k, survey 2.5k, titanium contract 3.5k, reconnaissance 6k). Spend: gifts 15,000 (user order, D29), autocannon 1,500, cargo_expander_ii 1,908, fuel ~1,500.

## Stockpile (never sell) t2098845
- central_nexus: carbon 2019, tungsten 927, platinum 725, lead 638, palladium 303, copper 35, iron 28
- node_beta_industrial_station: carbon 339, tungsten 223, platinum 38, palladium 30, lead 16, steel 3, lead_ingot 4, platinum_wiring 1, null_matter 1, copper 18, iron 13
- node_gamma_relay_station: exotic_matter 10, carbon 21, tungsten 20, palladium 4, null_matter 1, copper 11, iron 13
- grand_exchange_station (haven): copper 15, iron 10
- deep_range_outpost: titanium_ore 134, nickel_ore 159, copper_wiring 94, steel_plate 72, iron 4, mining_laser_ii 1
- ramens_rest: silicon_ore 258, trade_crystal 25, focused_crystal 1, circuit_board 3, titanium_alloy 1, steel_plate 14, copper_wiring 16, reinforced_glass 1, standard_rounds_box 4, titanium_ore 1, iron 9, copper 3, mining_laser_i 1, cargo_expander_ii 1, em_disruptor_i 1
- Crafting inputs must sit in the storage of the station where you craft: plan consolidation before a build (see docs/strategy.md).

## Missions
Active: NONE. Leads: exotic_crystal_synthesis (8,000; needs 6 exotic_matter, 10 @ node_gamma), wh_intro wormhole missions (500cr), grazer hunts (1.0-1.3k).

## Now (priority order) — strategy: docs/strategy.md (Voidborn ghost prospector)
1. **Passive training today:** refit Threshold to >=90% load (2x ML II = 29/30: spare ML II @ deep_range_outpost) so Engineering ticks while we work. Run EXP-2 (install a module whose listed skill we lack).
2. **Build survey_scanner_i** from stock at ramens_rest (trade crystals + boards + carbon; PB-6) and start `survey_system` on every system visited (Scanning XP).
3. **Build absence** (EXP-1): mine ~6 iridium at unknown_edge, consolidate inputs at a shipyard station, craft components, commission. Then fit survey scanner + cloak and start stealth training (EXP-8).
4. **cloaking_device_i inputs:** energy_crystal 4 (garnet_dim_lattice), silver 8 (errai_belt), power cells. Gather on scouting runs.
5. **Information play** (EXP-9..11): log traffic per region on every run (get_system_agents); test selling a true-but-low-value note; ask decoy questions about far-away places in system chat (never near our spots).
6. Credits via capital-board circuits + freight/passengers on the same routes (PB-7, PB-3) when needed. Refining/Crafting via `sm.py train` at every dock.

## Open Questions for User
- Q4: ore/refined DELIVERY missions (Sol: 2,000 lead ore -> 20,000cr; the_long_haul 10 Ti alloy -> 10,000) — allowed as mission payout or forbidden as selling ore? Default forbidden. OPEN.
- Q5 (cloaking_dust for Stealth 1) and Q7 (Piloting grind) are superseded by the stealth/intel strategy (LOG D34).
