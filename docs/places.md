# Places (index). Systems + belts are in data/systems.tsv + data/belts.tsv (explore.py upserts them): query with `python3 scripts/res.py ore|sys|route|near|grep` instead of reading them.

Verdict words in belts.tsv: STOCK = worth stockpile mining | MISSION = mission units only | DEAD = skip | FUTURE = needs gear we lack (harvesters).
PATTERN: policed belts are drained to ~0; LAWLESS belts hold 10k-100k Fe/Cu plus small rare deposits (silicon, titanium, null matter, gold, trade crystal, silver...). Ore cell notation: ore r<richness>/<remaining>/p<supported_power>. ~125 systems and ~110 belts recorded; the north-east lawless region beyond rukbat (mirfak, menkib, skat, wolf_359, heathwick, meridian, navi) holds only Fe/Cu, lithium (meridian 25k), aluminum (skat 28k), zinc (heathwick 19k, brightfall 8k), gas: no Ni/Ti/Si.

## WHAT THE GAME REMEMBERS vs WHAT ONLY THIS REPO REMEMBERS
- Game remembers: visited flags, skills, storage per station, ship, credits. It does NOT give a new agent belt contents, yields, routes, prices or mission boards: this repo is the only source. Rows carry the tick they were seen; belts decay fast (Ti 76->0 in 20 min).

## Crafting-material locations (quick index; verify with res.py)
- SILICON: zubenelhakrabi_crystal_sand (+1..3/pick, ~1 pick in 3.5; ~55 per 135 cycles; slow regen). Stripped: haven commerce_fields, nexus_prime material_harvesters.
- TITANIUM + NICKEL: frontier pioneer_fields (p3 / p1; ONE laser; contested; Ti regen ~1/min; Ni ~0 left but we banked 159). Nickel exists nowhere else on the known map. krynn war_materials ~empty.
- IRIDIUM: unknown_edge_mineral_fields (356, p17; station in same system) + carbon/vanadium/aluminum 700 each; gliese_436 (1047, policed).
- NULL MATTER: null_dust_intercrus (440), null_dust_atlas (577) — lawless, on the zubenelhakrabi->nexus route. GOLD: garnet_belt (681, p34). ENERGY CRYSTAL: garnet_dim_lattice (65). PHASE CRYSTAL: cloverfield 448, altais 428, merope 158, alsciaukat/sheliak/errai nebulae.
- TRADE CRYSTAL: frostpeak uncut_gems (423, p21) > azmidi unclaimed_facets (206, p10) > keelbreak (63). SILVER: errai_belt (64, p3), nusakan (18). ALUMINUM 29k + MANGANESE 14k: sheliak; ALUMINUM 28k: skat. LITHIUM: wazn, meridian. ZINC: cloverfield, izar, heathwick, brightfall. QUANTUM FRAGMENTS: markeb, the_telescope, wezen, izar, distant_light, errai/alsciaukat/sheliak nebulae.
- Carbon/tungsten/platinum/palladium/lead: acubens_belt (node_beta loop PB-1), stock at central_nexus 2000+.
- Wildlife-only: raw_focusing_crystal, anchor_plate (magnet-barnacle), irradiated_marrow. Exotic matter: none known (10 @ node_gamma storage). Void essence, graphene, superconductor, liquid nitrogen: sources not yet found.

## ROUTES (verified; 1 fuel/jump, ~1 min/jump; 0 pirate contact; use res.py route A B for others)
- ramens_rest(last_light) > tidewater > sabik > alathfar > merak > zubenelhakrabi = 5 jumps (alt via fang,errai,alsciaukat,sheliak).
- last_light > unknown_edge > altais > frontier > deep_range = 4 jumps. last_light > unknown_edge > the_telescope > first_step = 3. deep_range > first_step = 2 (frontier_station forges titanium alloy). last_light > ain > rukbat > menkib > wolf_359 = 4 (north-east region).
- first_step > markeb > beid > driftwood > cloverfield > wazn > frostpeak > stonecrest > the_levy > ogma > traders_rest > haven = 11.
- haven > market_prime > gold_run > copernicus > keelbreak > zibal > revati > alfirk > dubhe > maplevale > miaplacidus > mimosa > tau_ceti > alpha_centauri > sol = 14.
- sol > sirius > epsilon_eridani > proxima_centauri > dheneb > thabit > canopus > spica > propus > ankaa > alphecca > scheat > nashira > rasalgethi > fumalsamakah > albireo > the_rampart > the_crucible > iron_reach > krynn = 19.
- krynn > nexus_prime = 20 (iron_reach,the_crucible,the_rampart,albireo,fumalsamakah,bd20_2457,wasat,westmark,mebsuta,adhara,pipirima,gudja,rastaban,lhs_1140,antares,gsc_0041,pherkad,synchrony,node_alpha).
- zubenelhakrabi > 70_ophiuchi > kepler_442 > kitalpha > intercrus > atlas > garnet > achernar > the_experiment > synchrony > node_alpha > nexus_prime = 11 (passes null matter, gold, energy crystal belts).

## STATIONS / DOCK NAMES (travel id)
central_nexus@the_core(nexus_prime; HOME) | war_citadel(krynn) | grand_exchange_station(haven; POI grand_exchange) | sol_central(sol; base confederacy_central_command) | mobile_capital(first_step; base frontier_station; the other first_step station is the memorial) | ramens_rest(last_light) | deep_range_outpost(deep_range) | unknown_edge_waystation | the_anvil_arsenal | ironhearth_station | blood_forge_smelting_works (POI red_maw is NOT the station) | iron_reach_mining_colony | the_crucible_garrison | the_rampart_checkpoint | synchrony_hub | node_alpha_processing_station | node_beta_industrial_station | node_gamma_relay_station | the_experiment_research_station | gold_run_extraction_hub | market_prime_exchange | the_levy_customs_station | alpha_centauri_colonial_station | sirius_observatory_station.

## Market reference (asks unless noted; thin books)
Ramen's Rest t2095372: cargo_expander_ii 1,908 | autocannon_i 1,500 | mining_laser_ii 7,308 | mining_laser_i 1,441 | survey_scanner_ii 30,800 | ice_harvester_i 5,769 | gas_harvester_ii 6,323 | afterburner_ii 4,392+ | fuel_optimizer 3,708+ | titanium_alloy BID 311 | silicon BID 180 | Ti ore BID 15 | silver BID 48 | nickel BID 14 | quantum_fragments ask 350 | adamantite ask 50,000 | energy_crystal ask 14,894.
Grand Exchange t2092400: trade_crystal 547 | energy_crystal 1400 | silver_ore 148 | circuit_board 905 | focused_crystal 2236 | mining_laser_i 1520 | ice_harvester_i 5000 | anchor_plate bid 204 | deep_core_extractor_mk_i bid 6000.
Sirius t2091650: energy_crystal 34123 | focused_crystal 3000 | mining_laser_ii 5388 | survey_scanner_ii 29395 | ice_harvester_i 7293 | gas_harvester_i 8304. Central Nexus t2090790: exotic matter 10000. Voidborn core t2091300: mining_laser_ii 7007 | cloaking_device_i 13.8k-19.8k.
Fuel tax/unit: Voidborn 2, Solarian ~6, Nebula ~5, Crimson ~4, Outer Rim ~1.
