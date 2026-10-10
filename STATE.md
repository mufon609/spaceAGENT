# STATE (volatile; replace stale lines in place at every checkpoint)
game_version: 0.613.4   (notes last checked against this; boot.py compares)
last_update: t2103550 (Nitrogen Ice Harvest completed; Stock consolidated at Central Nexus; Voidborn Mastery L2 25/340)

## Ship (active)
- Absence id b18ca7242812c8ebcdf8c123c42b5122, T1 Voidborn stealth shuttle. Hull 45/45, Shield 80/80 (+5/tick), Fuel 110/110, Cargo 2/75 (2 fuel_cell carried for emergency mobile refueling), Slots 0W/2D/3U, speed 3, power 19/32, CPU 11/18.
- Fit: cargo_expander_ii (U1, +50 cargo) | ship_scanner_i (U2, scan:30, targeting/jam resist +10) | ice_harvester_i (U3, mine power 8, ice harvesting) | shield_recharger_i (D1, +2 regen) | thermal_hull_hardener (D2, +25% thermal). All 5 module slots fitted.
- Inherent capabilities: integrated_cloak 30, scan_resistance 20 (cloak strength 50 when active).
- Stored ship: Threshold starter id 1560ab3025cd17ccbce5701e2af70969 (with mining laser ii & autocannon i) safely preserved at Central Nexus shipyard for starter account. Never sell old equipment.
- Preserved modules in storage: gas_harvester_i, mining_laser_i, cargo_expander_i, shield_booster_i.
- LOCATION: DOCKED at Central Nexus (nexus_prime, Maximum Security). Safe dock.

## Skills (t2103550)
voidborn_mastery 2 (25/340 XP)
navigation 7 (214/2,265 XP)
mining 9 (2,536/3,525 XP) | piloting 9 (1,998/3,525 XP) | engineering 12 (3,230/5,940 XP)
deep_core_mining 8 (2,169/2,860) | crafting 4 (35/900) | exploration 4 (310/900) | refining 3 (475/585) | trading 3 (480/585) | leadership 1 (56/165) | stealth 0 (40/60 XP) | scanning 0 (25/60 XP) | tactics 0 (33/60 XP) | gunnery 0 (27/60 XP) | weapons 0 (9/60 XP) | xenobiology 0 (3/60 XP)

## Credits + tax
148,667 wallet. Tax: owed 12,093, prepaid 13,952 (next in ~36.6h). User rule: always prepaid.

## Stockpile (never sell) — full table: data/stock.tsv (`sm.py stock`, auto at boot; never hand-edit)
Summary: central_nexus: 14 iridium_ore, 3 dark_matter_residue, 1983 C, 927 W, 723 Pt, 638 Pb, 291 Pd, 50 argon_gas, 42 hydrogen_gas, 21 nitrogen_ice, 20 water_ice, 15 neon_gas, 2 plasma_gas, 1 deuterium_ice, 8 Fe, 3 Cu, 3 Si | deep_range_outpost: Ni 135, Ti 134, wiring 65, steel 67, spare ML II | ramens_rest: Si 183, trade_crystal 17, wiring 16, steel 10, modules | frontier_station: 15 nickel_ore, 8 titanium_ore, 99 iron_ore, 69 copper_ore.
Consolidation hub = **central_nexus** (Voidborn shipyard + biggest pile).

## Missions
- Active: wh_intro_voidborn_37a7a6e8 (Castor wormhole investigation; 500cr, trains exploration, scanning, wormhole_navigation).
- Completed this session:
  - nitrogen_ice_harvest (+36cr paid, +40 mining, +25 voidborn_mastery, +2 voidborn rep). Voidborn Mastery reached Level 2 (25/340 XP).
  - water_ice_extraction (+134cr paid, +25 mining, +25 voidborn_mastery, +2 voidborn rep). Unlocked chain: nitrogen_ice_harvest. VOIDBORN MASTERY LEVEL 2 ACHIEVED!
  - cryogenic_extraction_setup (+8cr paid, +15 mining, +15 voidborn_mastery, +1 voidborn rep). Purchased Ice Harvester I for 2,798cr. Unlocked chain: water_ice_extraction.
  - rare_gas_acquisition (+3,500cr, +40 mining, +25 voidborn_mastery, +2 voidborn rep). Voidborn Mastery reached 125/165.
  - hydrogen_collection_run (+80cr paid, +25 mining, +25 voidborn_mastery, +2 voidborn rep). Unlocked chain: rare_gas_acquisition.
  - the_signal_protocol (+1,416cr, +30 exploration, +20 scanning, +15 tactics, +25 voidborn_mastery, +2 voidborn rep).
  - hardware_optimization_defense (+1,932cr, +20 engineering, +15 voidborn_mastery, +1 voidborn rep).
  - hardware_optimization_cargo (+1,056cr, +15 engineering, +15 voidborn_mastery, +1 voidborn rep).
  - atmospheric_extraction_setup (+63cr, +15 mining, +15 voidborn_mastery, +1 voidborn rep).
  - the_collective_provides (+42cr paid, +30 mining, +10 trading, +25 voidborn_mastery, +2 voidborn rep).
  - the_void_gate_passage (+5,500cr, +30 nav XP).
  - neural_matrix_delivery (+3,211cr, +25 nav, +40 trade, +2 voidborn rep).
  - sensor_data_exchange (+7,000cr, +25 nav, +55 trade, +3 solarian rep).
  - federation_payment (+8,000cr, +30 nav, +60 trade, +3 nebula rep).
  - closing_the_circuit (+76cr paid, +20 lead, +35 nav, +75 trade, +3 voidborn rep). First ever designated "Trusted Courier".

## Counter-Recon & DM probes (docs/counter-recon.md)
- DM1: Wexler 41U-RH (Nexus Prime)
- DM2: Bach (Castor)
- DM3: Wexler Q75-M5 (Void Gate Outpost)
- DM4: GravelGarcia (Ramen's Rest)
- DM5: ThurstonHowell (Sirius Observatory)
- DM6: Wario (Market Prime)
- DM7: Rockefeller (Horizon)
- DM8: BedrockObama (Horizon)
- DM9: LurkerDen (Horizon)
- DM10: FatTony (Central Nexus)
Rule: never respond back to replies; only send once per player.
- Notes: N1 (mirfak), N2 (sandrift) created for 1,400cr trade offers.

## Now (priority order)
1. **Voidborn Mastery Level 10 Grind**: Target next Voidborn empire missions (`rare_gas_acquisition` with our 38 banked Argon Gas, followed by `amplification_materials`) to drive Voidborn Mastery to Level 2 and onward to Level 10.
2. **Fuel Independence**: Self-synthesize fuel cells from harvested atmospheric gases.
3. **Passive Stealth Training**: Run integrated cloak during deep space transit with ample fuel.
4. **Git Checkpoints**: Sync at each milestone, continuous relentless play.

