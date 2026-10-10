# Strategy (long plan). Live numbers are in STATE.md. Revise when experiments (docs/experiments.md) prove a better path.

## SOLO SHIP LADDER (D33, catalog v0.613.4) — verify each with `commission_quote` before committing materials
Ships come from `commission_ship(ship_class, provide_materials=true)` at a shipyard (cheapest with own materials), not the market (rule: never buy ships). Keep the Threshold stored as the free mining/backup hull; swap with `switch_ship`.
| Hull | Tier | Piloting | Cargo | Speed | Slots W/D/U | Power | Crew | Why |
|---|---|---|---|---|---|---|---|---|
| threshold (now) | T0 | - | 65 | 1 | 1/2/2 | 30 | 1 | starter |
| absence | T1 | none | 25 | 3 | 0/2/3 | 32 | 1 | stealth explorer: integrated cloak 30 + scan resistance 20; 3x speed for scouting lawless space |
| liminal | T1 | none | 75 | 2 | 0/2/3 | 34 | 1 | miner upgrade: 2x speed, +1 utility |
| resonance_miner | T2 | 10 | 180 | 2 | 0/2/4 | 48 | 3 | end goal miner |
Other T1 Voidborn (no piloting gate): fugue courier (55 cargo, speed 4), residuum salvager (100 cargo), rime ice harvester, accretion gas harvester, eigenstate scout, qualia explorer, apeiron EW, paradox fighter, vigil patrol. `python3 scripts/recipe.py` + catalog ships[] for bills.
- absence bill: silicate_composite 12, copper_wiring 11, processing_core 1, shield_emitter 3, steel_plate 5. From stock: composites 48 Si + 24 Ni; core = 5 boards + 2 Pt + 3 Si; emitters = 6 superconductor (FAC create_superconductor: 2 palladium + 1 iridium + 3 wiring each) + 3 focused_crystal (12 trade_crystal) + 6 boards; boards = carbon_arc_circuit_etching (12 C + 2 Si -> 3). ONLY MISSING: ~6 iridium_ore (unknown_edge_mineral_fields, 1 jump from ramens_rest). Logistics: Si @ ramens_rest, Ni @ deep_range_outpost, C/Pt/Pd @ central_nexus -> consolidate at one shipyard station.
- liminal bill: silicate_composite 12, copper_wiring 10, void_nanite_suspension 5, shield_emitter 2, shield_matrix 5, ore_hopper 3, processing_core 1. Extra needs vs stock: gold ~20 (gold_wiring for 5 shield matrices; garnet_belt), 10 graphene_sheet (FAC exfoliate_graphene 6 C -> 1), 5 purified_argon (25 argon_gas: gas harvester), void nanites (3 null_matter + water ice + nitrogen ice: ice harvester), flex_polymer 12 (8 Si + 4 Ni each), ~4 iridium.
- resonance_miner: see STATUS below; still needs Piloting 10 + crew 3 + void essence/energy/phase crystal sources.
- [?] Higher-tier hulls grant more XP per action (catalog text) — measure Piloting XP/tick in a T1 vs the Threshold (EXP-1b).


## Original user plan (S1–S3; phases still valid, routes may change)
Role: Voidborn Frontier Prospector. Ship Threshold (T0) -> Resonance Miner (T2). Home central_nexus. Primary mission: sustainable raw SILICON supply from frontier/lawless space. Phases:
1. Wealth + XP stacking: grind Piloting to 10 (gate for any T2 hull); keep reactor load >=90% when convenient (Engineering passive ~1 XP/tick); stockpile ore (never sell).
2. Resonance Miner commission (Requires Piloting 10, min crew 3): SOLO since D33 — craft every component ourselves (no skill gate; Workshop free, FAC rented). The old plan (fleet crafter Alien_Hauler-Opus55 crafts from our raw at Central Nexus, ~10-15k fees) is DROPPED unless the user re-enables it. The user sent 5,000 cr gifts to three fleet accounts via us once (D29).
3. Fit + stealth base training: dual Laser II, Cloak I, Shield Booster II, Deep Core Extractor (45/48 MW); docked cloak cycles (Stealth +5 XP per activation; ~380 XP/h for ~77 fuel/h; always end docked + decloaked).
4. Frontier Silicon expeditions: cloaked hops to Zubenelhakrabi Crystal Sand (Silicon r40); regular Si supply line (fleet hand-off / fleetctl approve-route only if the user re-enables fleet ties).

## Fitting ratchet (Engineering)
Engineering gives -1% module power/CPU draw per level. Load >=90% of reactor = ~1 Engineering XP/tick. When load drops <90%, upgrade a module (laser I->II, recharger I->II) to push it back over 90%. Threshold: 2x Mining Laser II + recharger + hardener + EM disruptor = 29/30.

## Stealth notes
Cloak strength = module + hull bonus x Stealth skill. cloaking_device_i lists Stealth 1 (probably unenforced since v0.566.3 -> EXP-2; old Q5 cloaking_dust idea superseded); the absence hull has an integrated cloak. Level 3 unlocks Emergency Cloaking System, 5 gives +5% strength.

## STATUS t2098845 (supersedes the old plan numbers)
- Piloting is LEVEL 9 (1,186/3,525): ~2,340 XP to level 10 = ~8-10 h of mining (0.67-0.84 XP/tick). Combat gives no shortcut (tested). Catalog: higher-tier ships earn more XP per action (so the Resonance Miner should speed up XP).
- Resonance Miner bill (catalog, 202 units, market ~104k): copper_wiring 40, titanium_alloy 30, void_nanite_suspension 20, shield_emitter 5, ore_hopper 8, silicate_composite 60, void_condensate 5, processed_null_matter 7, shield_matrix 15, sensor_array 8, processing_core 2, phase_matrix 2. Build time 1080 ticks, shipyard tier 1; defaults mining_laser_ii + shield_booster_ii.
- Raw bill (recipe.py tree): silicate_composite = 4 Si + 2 Ni (workshop) OR 2 Si + 2 Ni + 1 iridium_ore (iridium @ unknown_edge); shield_matrix needs 1 composite each (75 composites total) + 2 graphene_sheet + gold_wiring/electrum (3 silver + 2 gold) + purified_argon. titanium_alloy = 3 Ti ore + 1 steel (forge_titanium_alloy at frontier_station only, FAC 37cr/run) => 90 Ti. void_nanite_suspension = null_matter + purified_water + liquid_nitrogen (2 per run, 10 runs). processed_null_matter = 2 null_matter (x7). void_condensate = 3 void_essence + 1 energy_crystal (x5). phase_matrix = 2 phase_crystal + 1 energy_crystal (x2). sensor_array = 3 circuit_board + 1 focused_crystal + 2 palladium (or 6 trade_crystal + 3 boards -> 2). processing_core = 5 boards + 2 platinum + 3 Si. ore_hopper = 10 steel + 4 flex_polymer + 3 wiring. shield_emitter = 2 superconductor + focused_crystal + 2 boards.
- STOCK (t2098845): Ti ore 135 (need 90) OK | Nickel 159 (need ~150) OK | Silicon 258 (need ~240) OK | copper wiring 110 (need 64) OK | steel 86 (need 80) OK | trade crystal 25 | circuit boards 3 (carbon 2300 + Si make more). MISSING: null matter ~24 (intercrus_null_dust 440, atlas_null_dust 577, both lawless), void essence, energy crystal (garnet_dim_lattice 65), phase crystal (merope 158, cloverfield 448, altais 428), gold (garnet_belt 681) + silver (errai 64), graphene thread, superconductors, purified water/liquid nitrogen/argon (gas harvesters needed? ice/gas belts exist but need harvester modules).
- The 'maintain >=90% load' rule conflicts with the one-laser Ti/Ni stacking fit (power 18-22/30); Ti/Ni/Si targets are now met, so refit 2x ML II (29/30) for pure XP grinding at jettison belts.
