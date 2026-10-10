# GAME-PLAN (user's plan, confirmed "still the plan" in S3). Strategy source of truth; live numbers are in progression.md / goals.md.

Role: Voidborn Frontier Prospector (satellite of parent fleet). Ship Threshold (T0) -> Resonance Miner (T2). Home central_nexus. Primary mission: sustainable raw SILICON supply from frontier/lawless space for the fleet.

## Phases
1. Wealth + XP stacking: grind Piloting to 10 (gate for any T2 hull); keep reactor load >=90% when convenient (Engineering passive ~1 XP/tick); stockpile ore (never sell).
2. Resonance Miner commission (Requires Piloting 10, min crew 3): fleet crafter Alien_Hauler-Opus55 (Crafting/Refining 12) crafts components at Central Nexus from raw we supply + ~10-15k credits workshop fees; we then commission the hull. TRIGGER ONLY when Piloting 10 is reached / when the user says so (account isolation otherwise). The user already sent 5,000 cr gifts to the three fleet accounts via us (D29).
3. Fit + stealth base training: dual Laser II, Cloak I, Shield Booster II, Deep Core Extractor (45/48 MW); docked cloak cycles (Stealth +5 XP per activation; ~380 XP/h for ~77 fuel/h; always end docked + decloaked).
4. Frontier Silicon expeditions: cloaked hops to Zubenelhakrabi Crystal Sand (Silicon r40); regular Si supply line for the fleet (route approval via fleetctl approve-route).

## Fitting ratchet (Engineering)
Engineering gives -1% module power/CPU draw per level. Load >=90% of reactor = ~1 Engineering XP/tick. When load drops <90%, upgrade a module (laser I->II, recharger I->II) to push it back over 90%. Threshold: 2x Mining Laser II + recharger + hardener + EM disruptor = 29/30.

## Stealth notes
Cloak strength = module + hull bonus x Stealth skill. cloaking_device_i needs Stealth 1 (chicken-egg; Q5 cloaking_dust open). Level 3 unlocks Emergency Cloaking System, 5 gives +5% strength.

## STATUS t2098845 (supersedes the old plan numbers)
- Piloting is LEVEL 9 (1,186/3,525): ~2,340 XP to level 10 = ~8-10 h of mining (0.67-0.84 XP/tick). Combat gives no shortcut (tested). Catalog: higher-tier ships earn more XP per action (so the Resonance Miner should speed up XP).
- Resonance Miner bill (catalog, 202 units, market ~104k): copper_wiring 40, titanium_alloy 30, void_nanite_suspension 20, shield_emitter 5, ore_hopper 8, silicate_composite 60, void_condensate 5, processed_null_matter 7, shield_matrix 15, sensor_array 8, processing_core 2, phase_matrix 2. Build time 1080 ticks, shipyard tier 1; defaults mining_laser_ii + shield_booster_ii.
- Raw bill (recipe.py tree): silicate_composite = 4 Si + 2 Ni (workshop) OR 2 Si + 2 Ni + 1 iridium_ore (iridium @ unknown_edge); shield_matrix needs 1 composite each (75 composites total) + 2 graphene_sheet + gold_wiring/electrum (3 silver + 2 gold) + purified_argon. titanium_alloy = 3 Ti ore + 1 steel (forge_titanium_alloy at frontier_station only, FAC 37cr/run) => 90 Ti. void_nanite_suspension = null_matter + purified_water + liquid_nitrogen (2 per run, 10 runs). processed_null_matter = 2 null_matter (x7). void_condensate = 3 void_essence + 1 energy_crystal (x5). phase_matrix = 2 phase_crystal + 1 energy_crystal (x2). sensor_array = 3 circuit_board + 1 focused_crystal + 2 palladium (or 6 trade_crystal + 3 boards -> 2). processing_core = 5 boards + 2 platinum + 3 Si. ore_hopper = 10 steel + 4 flex_polymer + 3 wiring. shield_emitter = 2 superconductor + focused_crystal + 2 boards.
- STOCK (t2098845): Ti ore 135 (need 90) OK | Nickel 159 (need ~150) OK | Silicon 258 (need ~240) OK | copper wiring 110 (need 64) OK | steel 86 (need 80) OK | trade crystal 25 | circuit boards 3 (carbon 2300 + Si make more). MISSING: null matter ~24 (intercrus_null_dust 440, atlas_null_dust 577, both lawless), void essence, energy crystal (garnet_dim_lattice 65), phase crystal (merope 158, cloverfield 448, altais 428), gold (garnet_belt 681) + silver (errai 64), graphene thread, superconductors, purified water/liquid nitrogen/argon (gas harvesters needed? ice/gas belts exist but need harvester modules).
- The 'maintain >=90% load' rule conflicts with the one-laser Ti/Ni stacking fit (power 18-22/30); Ti/Ni/Si targets are now met, so refit 2x ML II (29/30) for pure XP grinding at jettison belts.
