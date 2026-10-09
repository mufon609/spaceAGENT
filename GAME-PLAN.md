# GAME-PLAN (user's plan, restated S3 t~2096500: "still the plan"). Source of truth for strategy; status numbers are in progression.md.

Role: Voidborn Frontier Prospector (satellite of parent fleet). Ship Threshold (T0) -> Resonance Miner (T2). Home central_nexus. Primary mission: sustainable raw SILICON supply from frontier/lawless space for the fleet.

## Phases
1. Wealth + XP stacking: grind Piloting to 10 (gate for any T2 hull); keep reactor load >=90% (Engineering passive XP ~1/tick = ~360/h); stockpile ore (never sell).
2. Resonance Miner commission (needs Piloting 10, min crew 3): fleet crafter Alien_Hauler-Opus55 (Crafting/Refining 12) crafts the 12 components at Central Nexus from raw we gift + ~10-15k credits workshop fees; we then commission the hull. TRIGGER ONLY when Piloting 10 is reached (account isolation otherwise: no contact with other fleet accounts before then; user says when).
3. Fit + stealth base training: dual Laser II, Cloak I, Shield Booster II, Deep Core Extractor (45/48 MW); docked cloak cycles (Stealth +5 XP per activation; station cycling = 10x XP per fuel vs cloaked jumps; ~380 XP/h for ~77 fuel/h; always end docked + decloaked).
4. Frontier Silicon expeditions: cloaked hops to Zubenelhakrabi Crystal Sand (Silicon r40); open a regular Si supply line (route approval via fleetctl approve-route).

## Fitting ratchet (Engineering)
Engineering gives -1% module power/CPU draw per level. Load >=90% of reactor = ~1 Engineering XP/tick (flying or docked). When load drops <90%, upgrade a module (laser I->II, recharger I->II) to push it back over 90% = free progression + better gear. RULE: keep power draw >=27/30 on Threshold when not on a special-purpose fit.

## Stealth notes
Cloak strength = module + hull bonus x Stealth skill. cloaking_device_i needs Stealth 1 (chicken-egg; Q5 cloaking_dust open). Level 3 unlocks Emergency Cloaking System, 5 gives +5% strength.

## S3 CORRECTIONS / DISCOVERIES (supersede old numbers)
- Piloting is LEVEL 9 at t2096475 (58/3,525 XP). Level 10 needs ~3,470 more XP: ~12 h mining (4 XP/min) or ~19 h jumping (3/min). XP: jump +3, travel +1, mine cycle +1.
- Resonance Miner build list (catalog): copper_wiring 40, titanium_alloy 30, void_nanite_suspension 20, shield_emitter 5, ore_hopper 8, silicate_composite 60, void_condensate 5, processed_null_matter 7, shield_matrix 15, sensor_array 8, processing_core 2, phase_matrix 2 (202 units; market value ~104k). Build time 1080 ticks, shipyard tier 1. Defaults: mining_laser_ii + shield_booster_ii.
- Raw bill (recipe.py tree): silicate_composite = 4 Si + 2 Ni (workshop) OR bond_iridium_silicate_composite = 2 Si + 2 Ni + 1 iridium_ore (iridium r25 433 @ unknown_edge_mineral_fields, 1 jump from last_light); shield_matrix needs 1 silicate_composite + 2 graphene_sheet + gold_wiring/electrum + purified_argon (so 75 composites total incl. 15 matrices). titanium_alloy = 3 Ti ore + 1 steel (forge_titanium_alloy FAC) => 90 Ti ore. void_nanite_suspension = null_matter + purified_water + liquid_nitrogen (2 per run; 10 runs). processed_null_matter = 2 null_matter (14 for 7). void_condensate = 3 void_essence + 1 energy_crystal. phase_matrix = 2 phase_crystal + 1 energy_crystal. sensor_array = 3 circuit_board + 1 focused_crystal + 2 palladium. processing_core = 5 circuit_board + 2 platinum + 3 Si. ore_hopper = 10 steel + 4 flex_polymer + 3 copper_wiring. shield_emitter = 2 superconductor + focused_crystal + 2 circuit_board.
- Where: null_matter 440-577 at intercrus/atlas (lawless, on the zubenelhakrabi->nexus route); gold 681 garnet_belt; phase_crystal cloverfield/alsciaukat/sheliak/altais/merope; energy_crystal garnet_dim_lattice (65); Ti ore: pioneer_fields (slow). Our stock t2096475: Si 93 (+mining), Ti ore 66 + 0, Ni 74, copper_wiring 40, trade_crystal 29, carbon 2300+, Pd 330, Pt 755, W 1140.
- Plan item 'maintain >=90% load' conflicts with the CE II fit used for Si stacking (power 24/30=80%). Use ML II + ML II (97%) when not stacking; with filler jettison (PB-9) the 65 hold is enough for ~55 Si per trip.
