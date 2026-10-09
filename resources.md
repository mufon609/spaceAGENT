# Resources

Verdict: STOCK = worth stockpile mining | MISSION = mission units only | DEAD = skip | FUTURE = needs gear we lack.
Ore cell: ore r<richness>/<remaining>/p<supported_power>. Generate rows with `python3 scripts/explore.py md`.
PATTERN (t2091600): policed belts are drained to ~0; LAWLESS belts are near-untouched (10k-70k units).

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
| the_experiment, gsc_0027, hamal, schedar | voidborn/none | ? | ? | visited S1, belts unrecorded (check for Silicon) |
Verified safe-to-transit (no contact S2): gsc_0041, antares, homam. Route node_beta->sirius = 9 jumps, ~25 min with belt scouting.
Unvisited frontier near home: achernar, gj_3470, gsc_0050, ironhollow, megrez, okab, ruchbah, shaula, thornhaven, wolf_1061.

## Deposits / belt health
| System | POI ID | Police | Equip | Players | Last seen (tick: ore r/rem/p) | Verdict |
|---|---|---|---|---|---|---|
| acubens | acubens_belt | low | laser | 0-5 | 2091440: carbon r55/789/p39 tungsten r34/347/p17 platinum r14/664/p33 palladium r28/4/p1 uranium r13/72/p3 lead r15/923/p46 (max 5000) | STOCK (PB-1) |
| acubens | acubens_shadow_pocket | low | ? | 6 | S1: camped dry | DEAD |
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
| nexus_prime | material_harvesters | 100 | laser | 0 | 2090790: iron r70/0 silicon r90/0 copper r80/0 energy_crystal r8/0 | DEAD now; recheck (only Si + energy_crystal seen in Voidborn) |
| nexus_prime | null_matter_anomaly | 100 | laser | 2 | 2090790: null_matter r30/0 | DEAD |
| node_beta | eltanin_prime_belt | high | laser | 1-3 | 2090950: all 0 | DEAD |
| node_gamma | bellatrix_major_belt | 55 | laser | 0 | 2091600: all 0 | DEAD |
| node_gamma | node_gamma_ice_belt | 55 | ice harvester | 1 | 2091600: nitrogen_ice r44/10 | DEAD |
| node_alpha | alpha_extraction_zone | high | laser | 3 | 2090780: all 0 | DEAD |

## Still unfound (crafting blockers)
titanium_ore, silicon_ore (Voidborn/Nebula space per docs), energy_crystal (rare; Sirius ask 34,123!), trade_crystal (Nebula ore), silver_ore, nickel_ore, cobalt_ore.
Wildlife sources: raw_focusing_crystal (ranched "druse"), anchor_plate (magnet-barnacle shell -> titanium_alloy), irradiated_marrow (geiger-hound -> power_cell).

## Market reference (asks unless noted; thin books, not valuations)
Sirius t2091650: energy_crystal 34123 | focused_crystal 3000 | silver_wiring 171 | titanium_alloy bid 264 | silicon_ore bid 180 (no asks) | iron 13 | copper 1 | platinum_ore 167 | palladium 234 | tungsten 107 | deuterium_ice 120 | mining_survey_probe 180 | mining_laser_ii 5388 | ship_scanner_i 2661 | survey_scanner_ii 29395 | ice_harvester_i 7293 | gas_harvester_i 8304.
Central Nexus t2090790: copper ore 1 | silicon bid 181 | titanium ore bid 80 | exotic matter 10000.
Modules Voidborn core t2091300: mining_laser_ii 7007 (node_beta) | cargo_expander_ii 1414-1672 | afterburner_iii ~4950 | cloaking_device_i 13.8k-19.8k.
Fuel: Voidborn tax 2cr/unit; Solarian tax ~6cr/unit (28 fuel = 224cr at Sirius).
Forum bounty: 25,000cr per live seam location (>300 units) of adamantite/darksteel/tritium_ice/polonium (Wren Farwander).
