# Resources

Verdict: STOCK = worth stockpile mining | MISSION = mission units only | DEAD = skip | FUTURE = needs gear we lack.
Ore cell: ore r<richness>/<remaining>/p<supported_power>. Generate rows with `python3 scripts/explore.py md`.
PATTERN (t2091600): policed belts are drained to ~0; LAWLESS belts are near-untouched (10k-100k units).

## Systems (police: 0 = lawless)
| System | Empire | Police | Station | Links |
|---|---|---|---|---|
| nexus_prime | voidborn | 100 | central_nexus (poi the_core) HOME | node_alpha, node_beta (NOT acubens) |
| node_alpha | voidborn | high | node_alpha_processing_station | node_beta, nexus_prime, node_gamma, synchrony |
| node_beta | voidborn | high | node_beta_industrial_station | node_gamma, node_alpha, acubens, nexus_prime, schedar, gsc_0027 |
| node_gamma | voidborn | 55 | node_gamma_relay_station | node_beta, node_alpha, acubens, synchrony |
| acubens | voidborn | low | none | node_gamma, node_beta, gsc_0027, hamal |
| synchrony | voidborn | 55 | synchrony_hub | the_experiment, node_alpha, pherkad, node_gamma |
| pherkad | voidborn | 30 | none | ironhollow, gsc_0041, shaula, synchrony, wolf_1061 |
| gsc_0041 | none | 0 LAWLESS | none | shaula, ironhollow, antares, pherkad |
| antares | none | 0 LAWLESS | none | gsc_0041, gsc_0033, lhs_1140, homam |
| homam | none | 0 LAWLESS | none | gsc_0033, bluerift, furud, antares |
| furud | solarian | 30 | none | nova_terra, acrux, homam, nihal |
| nova_terra | solarian | 55 | nova_terra_central | sirius, epsilon_eridani, furud, procyon, lacaille_9352 |
| sirius | solarian | 80 | sirius_observatory_station | lacaille_9352, nova_terra, epsilon_eridani, sol |
| sol | solarian | 100 | sol_central (base confederacy_central_command) | sirius, alpha_centauri |
| alpha_centauri | solarian | 80 | alpha_centauri_colonial_station | sol, tau_ceti |
| epsilon_eridani | solarian | 55 | none | procyon, nova_terra, nihal, markab, sirius, proxima_centauri |
| procyon | solarian | 30 | procyon_colonial_station | epsilon_eridani, proxima_centauri, markab, nihal, nova_terra |
| tau_ceti | solarian | 55 | none | electra, alpha_centauri, timberline, mimosa |
| mimosa | solarian | 30 | none | electra, miaplacidus, ross_154, tau_ceti |
| miaplacidus | none | 0 LAWLESS | none | maplevale, cervantes, mimosa |
| maplevale | none | 0 LAWLESS | none | miaplacidus, dubhe, ross_154 |
| dubhe | none | 0 LAWLESS | none | alfirk, maplevale |
| alfirk | none | 0 LAWLESS | none | revati, dubhe, peacock, gsc_0009 |
| revati | none | 0 LAWLESS | none | gsc_0009, alfirk, peacock, zibal, pinewatch |
| zibal | none | 0 LAWLESS | none | gsc_0009, keelbreak, revati, kurhah |
| keelbreak | none | 0 LAWLESS | none | gsc_0030, zibal, xihe, copernicus |
| copernicus | nebula | 30 | none | wealth_lane, bunda, gold_run, gsc_0030, keelbreak |
| gold_run | nebula | 55 | gold_run_extraction_hub | cargo_lanes, market_prime, bunda, copernicus, wealth_lane |
| market_prime | nebula | 80 | market_prime_exchange | cargo_lanes, gold_run, haven |
| haven | nebula | 100 | grand_exchange (base grand_exchange_station) | market_prime, traders_rest |
| traders_rest | nebula | 80 | traders_rest_resort_station | factory_belt, khambalia, haven, gliese_436, ogma |
| factory_belt | nebula | 55 | factory_belt_manufacturing_hub | traders_rest, khambalia, pollux, treasure_cache |
| treasure_cache | nebula | 30 | treasure_cache_trading_post | ross_128, pollux, ashford, factory_belt |
| pollux | nebula | 30 | none | sadalmelik, factory_belt, nusakan, khambalia, treasure_cache |
| nusakan | none | 0 LAWLESS | none | azmidi, sadalmelik, pollux, naos |
| azmidi | nebula | 30 | none | nusakan, alioth, khambalia, almach |
| khambalia | nebula | 55 | none | factory_belt, traders_rest, azmidi, pollux, gliese_436 |
| gliese_436 | nebula | 55 | none | ogma, caph, the_levy, khambalia, traders_rest |
| the_levy | nebula | 30 | the_levy_customs_station | ogma, wealth_lane, gliese_436, stonecrest |
| wealth_lane | none | 0 LAWLESS | player station 22c5a816... (access denied) | copernicus, the_levy, gold_run |
| cargo_lanes | nebula | 55 | cargo_lanes_freight_depot | gold_run, market_prime, bunda, alrakis, alula |
| the_experiment, gsc_0027, hamal, schedar | voidborn/none | ? | ? | visited S1, belts unrecorded (check for Silicon) |
Verified safe-to-transit (no contact S2): gsc_0041, antares, homam, miaplacidus, maplevale, dubhe, alfirk, revati, zibal, keelbreak, nusakan, wealth_lane. Sol->Haven = 14 jumps (~45 min with scouting). Solarian stations docked OK: sirius, alpha_centauri, nova_terra, procyon, sol. Route node_beta->sirius = 9 jumps, ~25 min with belt scouting.
Unvisited frontier near home: achernar, gj_3470, gsc_0050, ironhollow, megrez, okab, ruchbah, shaula, thornhaven, wolf_1061.

## Deposits / belt health
| System | POI ID | Police | Equip | Players | Last seen (tick: ore r/rem/p) | Verdict |
|---|---|---|---|---|---|---|
| acubens | acubens_belt | low | laser | 0-5 | 2091440: carbon r55/789/p39 tungsten r34/347/p17 platinum r14/664/p33 palladium r28/4/p1 uranium r13/72/p3 lead r15/923/p46 (max 5000) | STOCK (PB-1) |
| acubens | acubens_shadow_pocket | low | ? | 6 | S1: camped dry | DEAD |
| azmidi | unclaimed_facets_azmidi | 30 | laser | 2 | 2092300: iron r34/100000/p5000 copper r34/100000/p5000 trade_crystal r30/206/p10 | BEST TRADE CRYSTAL: picked 7/8 cycles, 2-3/cycle (Mining 8). Nearest dock: treasure_cache (2j) / the_levy (3j) |
| nusakan | nusakan_belt | 0 | laser | 1 | 2092300: iron r42/99988 copper r41/99982 silver r32/18/p1 | SILVER (18). Come with empty hold: Fe/Cu picks are 5/cycle |
| gliese_436 | gliese_436_belt | 55 | laser | 4 | 2092500: carbon r42/1839/p91 platinum r19/205/p10 iridium r18/1047/p52 gold r29/73/p3 osmium r12/230/p11 thorium 0 | STOCK mixed (iridium/osmium) |
| wealth_lane | trappist_prime_belt | 0 | laser | 0 | 2092500: iron r53/100000 copper r41/100000 | STOCK Fe/Cu |
| khambalia | khambalia_crystal_market | 55 | laser | 0 | 2092500: iron r36/225 copper r35/251 trade_crystal r30/3/p1 | thin |
| azmidi | azmidi_belt | 30 | laser | 1 | 2092300: carbon r64/46 platinum r12/12 palladium r29/1 thorium r11/17 aluminum r49/47 rhodium r12/0 | thin |
| treasure_cache / khambalia / pollux | belts | 30-55 | laser | 1-3 | 2092300: carbon/iridium/gold/nickel/vanadium/lead ~0 | DEAD |
| nebula gas/ice (factory_belt, treasure_cache, azmidi, khambalia, the_levy, cargo_lanes, gliese_436, wealth_lane) | various | 0-55 | harvesters | 0-1 | 2092300-500: H2 31-50k, argon/neon ~50k, xenon 10k, krypton 5k (azmidi), deuterium 4.3k (the_levy), ammonia 9k (azmidi) | FUTURE |
| keelbreak | uncut_gems_keelbreak | 0 | laser | 5 | 2092400: iron r45/97938/p4896 copper r24/99611/p4980 trade_crystal r18/63/p3 | STOCK Fe/Cu + some trade crystal |
| miaplacidus | miaplacidus_alloy_remnants | 0 | laser | 1 | 2092400: iron r39/100000/p5000 copper r29/100000/p5000 sol_alloy r5/898/p44 | STOCK Fe/Cu (lawless) |
| haven | commerce_fields | 100 | laser | 1 | 2092400: iron r75/10 copper r65/10 nickel r55/2 silicon r70/2 trade_crystal r20/14 (p1) | DEAD; proves metallic table has Si + trade_crystal |
| gold_run | gold_run_mineral_fields | 55 | laser | 4 | 2092400: carbon r48/332/p16 vanadium r46/1 palladium r30/1 gold r25/0 | thin carbon |
| mimosa | unstable_pocket_mimosa | 30 | laser | 2 | 2092400: iron r42/110/p5 copper r33/129/p6 (forum said 100k on 09-18: drained) | DEAD |
| miaplacidus / zibal / mimosa / gold_run / haven | ice fields | 0-100 | ice harvester | 1-2 | 2092400: water_ice 4k-41k, nitrogen_ice 23k-50k, helium 4.5-5k, CO2 ice 9k (haven) | FUTURE |
| maplevale / copernicus / haven / market_prime | gas clouds | 0-100 | gas harvester | 0-2 | 2092400: argon/neon ~50k, xenon 10k + nebula_gas 10k + chlorine 10k (maplevale) | FUTURE |
| homam | homam_belt | 0 | laser | 0 | 2091600: iron r55/17594/p879 copper r26/69219/p3460 | STOCK Fe/Cu (lawless) |
| antares | sol_alloy_scatter_antares | 0 | laser | 1 | 2091600: iron r32/12088/p604 copper r31/12710/p635 sol_alloy r5/1221/p61 | STOCK Fe/Cu (lawless) |
| furud | furud_legacy_drift | 30 | laser | 5 | 2091600: iron r45/75383/p3769 copper r31/99301/p4965 sol_alloy r9/199/p9 | STOCK Fe/Cu, 1 jump to nova_terra_central |
| furud | furud_belt | 30 | laser | 0 | 2091600: carbon r63/133/p6 tungsten r41/63/p3 | thin |
| pherkad | pherkad_null_rift | 30 | laser | 2-7 | 2091600: iron r31/77/p3 copper r24/151/p7 null_matter r19/0 | MISSION |
| pherkad | refracted_nebula_pherkad | 30 | laser | 3 | 2091600: iron r28/12/p1 copper r30/16/p1 energy_crystal r4/0 | DEAD |
| gsc_0041 | gsc_0041_frost_ring | 0 | ice harvester | 1 | 2091600: water_ice r52/9637/p481 nitrogen_ice r49/28097/p1404 deuterium_ice r12/3454/p172 | FUTURE |
| antares | antares_ice_fields | 0 | ice harvester | 1 | 2091600: water_ice r55/9674 nitrogen_ice r41/23763 deuterium_ice r20/2562 helium_ice r24/3767 | FUTURE |
| homam | homam_cryobelt | 0 | ice harvester | 0 | 2091600: water_ice r57/8705 nitrogen_ice r41/50000 helium_ice r13/5000 | FUTURE |
| antares | antares_gas_cloud | 0 | gas harvester | 0 | 2091600: hydrogen r42/694 argon r53/48097 plasma r19/4465 nebula_gas r21/9894 neon r44/48855 chlorine r22/728 | FUTURE |
| furud | furud_vapor_fields | 30 | gas harvester | 0 | 2091600: hydrogen r64/1004 argon r41/48910 neon r31/50000 chlorine r16/821 | FUTURE |
| furud | furud_ice_shelf | 30 | ice harvester | 1 | 2091600: water_ice r57/78 helium_ice r16/15 | DEAD |
| nova_terra | nova_terra_industrial_belt | 55 | laser | 0 | 2091600: carbon/tungsten/iridium/thorium/lead/aluminum/legacy all 0 | DEAD |
| nova_terra | gas_plume / ice_shelf | 55 | harvesters | 0-1 | 2091600: ~0 | DEAD |
| sirius | sirius_gas_pocket | 80 | gas harvester | 1 | 2091600: all 0 | DEAD |
| sol | main_belt | 100 | laser | 2-5 | 2091900: iron r80/10 copper r60/10 nickel r70/2 titanium r25/2 sol_alloy r15/2 antimatter_cell r5/1 (all p1) | DEAD but proves Ti+Ni exist in Solarian belts |
| epsilon_eridani | delta_major_belt | 55 | laser | 0 | 2091880: carbon r61/87/p4 vanadium r50/32/p1 platinum r16/34/p1 aluminum r57/91/p4 legacy r5/20/p1 | thin |
| epsilon_eridani | epsilon_eridani_ice_fields | 55 | ice harvester | 0 | 2091880: water_ice r67/25830/p1291 nitrogen_ice r53/50000/p2500 | FUTURE (policed!) |
| procyon | procyon_gas_cloud | 30 | gas harvester | 0 | 2091860: hydrogen r48/217 argon r42/194 chlorine r25/18 | thin |
| alpha_centauri / procyon / sol ice+gas | various | 30-100 | harvesters | 0-3 | 2091900: ~0 | DEAD |
| nexus_prime | material_harvesters | 100 | laser | 0 | 2090790: iron r70/0 silicon r90/0 copper r80/0 energy_crystal r8/0 | DEAD now; recheck (only Si + energy_crystal seen in Voidborn) |
| nexus_prime | null_matter_anomaly | 100 | laser | 2 | 2090790: null_matter r30/0 | DEAD |
| node_beta | eltanin_prime_belt | high | laser | 1-3 | 2090950: all 0 | DEAD |
| node_gamma | bellatrix_major_belt | 55 | laser | 0 | 2091600: all 0 | DEAD |
| node_gamma | node_gamma_ice_belt | 55 | ice harvester | 1 | 2091600: nitrogen_ice r44/10 | DEAD |
| node_alpha | alpha_extraction_zone | high | laser | 3 | 2090780: all 0 | DEAD |

## Still unfound (crafting blockers)
titanium_ore, silicon_ore (metallic-belt table; all known core belts stripped), energy_crystal (rare), nickel_ore, cobalt_ore (Krynn War Materials belt per forum).
Trade crystal: azmidi unclaimed_facets_azmidi (206, p10, verified) > keelbreak (63, p3). Silver: nusakan (18).
Wildlife sources: raw_focusing_crystal (ranched "druse"), anchor_plate (magnet-barnacle shell -> titanium_alloy), irradiated_marrow (geiger-hound -> power_cell).

## Market reference (asks unless noted; thin books, not valuations)
Grand Exchange (haven) t2092400: trade_crystal 547 (179k listed, bid 546 = liquid) | energy_crystal 1400 (802) | silver_ore 148 | circuit_board 905 | focused_crystal 2236 | mining_laser_i 1520 | ice_harvester_i 5000 | silicon/titanium/nickel: bids only (180/102/64) | anchor_plate bid 204 | deep_core_extractor_mk_i bid 6000.
Sirius t2091650: energy_crystal 34123 | focused_crystal 3000 | silver_wiring 171 | titanium_alloy bid 264 | silicon_ore bid 180 (no asks) | iron 13 | copper 1 | platinum_ore 167 | palladium 234 | tungsten 107 | deuterium_ice 120 | mining_survey_probe 180 | mining_laser_ii 5388 | ship_scanner_i 2661 | survey_scanner_ii 29395 | ice_harvester_i 7293 | gas_harvester_i 8304.
Central Nexus t2090790: copper ore 1 | silicon bid 181 | titanium ore bid 80 | exotic matter 10000.
Modules Voidborn core t2091300: mining_laser_ii 7007 (node_beta) | cargo_expander_ii 1414-1672 | afterburner_iii ~4950 | cloaking_device_i 13.8k-19.8k.
Fuel: Voidborn tax 2cr/unit; Solarian ~6cr/unit; Nebula ~5cr/unit.
Forum bounty: 25,000cr per live seam location (>300 units) of adamantite/darksteel/tritium_ice/polonium (Wren Farwander).
