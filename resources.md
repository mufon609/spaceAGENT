# Resources

Verdict key: STOCK = worth stockpile mining | MISSION = only for mission units | DEAD = skip | ? = unchecked.
Ore cell format: ore r<richness>/<remaining>/p<supported_power> (from `sm scout`).

## Systems
| System | Empire | Security | Station | Links | Notes |
|---|---|---|---|---|---|
| nexus_prime | voidborn | Max | central_nexus (poi the_core) | node_alpha, node_beta | home, 40+ players docked. NOT adjacent to acubens |
| node_alpha | voidborn | High | node_alpha_processing_station | node_beta, nexus_prime, node_gamma, synchrony | |
| node_beta | voidborn | High | node_beta_industrial_station | node_gamma, node_alpha, acubens, nexus_prime, schedar, gsc_0027 | mission hub; PB-1 home |
| node_gamma | voidborn | Low | node_gamma_relay_station | node_beta, node_alpha, acubens, synchrony | |
| acubens | voidborn | Low | none | node_gamma, node_beta, gsc_0027, hamal | best belt |
| synchrony | voidborn | Low | synchrony_hub | the_experiment, node_alpha, pherkad, node_gamma | no belts |
| pherkad | voidborn | Frontier (minimal police) | none | ironhollow, gsc_0041, shaula, synchrony, wolf_1061 | Cu/Fe belt, nebula |
| the_experiment, gsc_0027, hamal | voidborn | ? | ? | see get_map | visited S1, unrecorded |
| schedar | none | ? | ? | gsc_0027, gsc_0050, node_beta | visited S1 |

Frontier unvisited (unclaimed, security unknown — ask user): achernar, gj_3470, gsc_0041, gsc_0050, ironhollow, megrez, okab, ruchbah, shaula, thornhaven, wolf_1061.
Long routes: sirius 8 jumps (synchrony-pherkad-gsc_0041-antares-homam-furud-nova_terra); horizon 17; the_crucible 17.

## Deposits / belt health
| System | POI ID | Sec | Equip | Crowd | Last seen (tick: ore r/rem/p) | Verdict |
|---|---|---|---|---|---|---|
| acubens | acubens_belt | Low | laser | 0-4 | 2091290: carbon r55/812/p40 tungsten r34/347/p17 platinum r14/629/p31 palladium r28/1/p1 uranium r13/39/p1 lead r15/868/p43 (max 5000). Trend: W falling ~-20/trip-hr, Pt/Pb/U rising | STOCK. ~9 cycles fills 65 cargo |
| acubens | acubens_shadow_pocket | Low | ? | 6 | S1: camped dry | DEAD |
| pherkad | pherkad_null_rift | Frontier | laser | 5-7 (SANE faction Thresholds) | 2090940: iron r31/78/p3 copper r24/90/p4 null_matter r19/0 | MISSION. 1 unit/cycle; regen ~= drain |
| nexus_prime | material_harvesters | Max | laser | 0 | 2090790: iron r70/0 silicon r90/0 copper r80/0 energy_crystal r8/0 | DEAD (recheck: rich if regen) |
| nexus_prime | null_matter_anomaly | Max | laser | 2 | 2090790: null_matter r30/0 | DEAD |
| nexus_prime | stellar_siphon / cryogenic_reserve | Max | gas / ice harvester | ? | ? | ? |
| node_beta | eltanin_prime_belt | High | laser | 1-3 | 2090950: carbon r49/0 vanadium r48/0 tungsten r32/0 platinum r14/0 void_essence r5/0 | DEAD (mine -> depleted at rem 1-3) |
| node_beta | node_beta_frozen_drift | High | ice harvester | ? | ? | ? |
| node_gamma | bellatrix_major_belt | Low | laser | 0 | 2090760: carbon r67/0 palladium r16/0 iridium r11/0 thorium r19/0 | DEAD |
| node_gamma | node_gamma_ice_belt | Low | ice harvester | 2 | ? | ? |
| node_alpha | alpha_extraction_zone | High | laser | 3 | 2090780: carbon r48/0 vanadium r35/0 tungsten r29/0 void_essence r4/0 | DEAD |

## Module market (asks, t2091300; Mining Laser III/IV not sold anywhere seen)
| Module | node_beta | node_gamma | central_nexus |
|---|---|---|---|
| mining_laser_i | 1791 | 1846 | 1600 |
| mining_laser_ii | 7007 | 7150 | none |
| cargo_expander_i / ii / iii | - / 1672 / 4755 | 416 / - / - | 346 / 1414 / - |
| afterburner_ii / iii | 5422 / 5106 | 5354 / 4953 | 5219 / 4927 |
| cloaking_device_i / ii | 19860 / 55426 | 13807 / 55426 | 19574 / 43963 |
| survey_scanner_ii | - | 30786 | none (bid 100) |
| expanded_fuel_tank | 1705 | - | - |
Mining Survey Probe ~180cr at Sirius (forum).

## Ore market reference (thin books; not valuations)
Central Nexus t2090790: copper ore ask 1 | silicon ore bid 181 | titanium ore bid 80 | platinum ore ask 5500 bid 1 | exotic matter ask 10000.
Grand Exchange (Haven) unfilled bids (forum 09-23): adamantite 1600, darksteel 700, polonium 500, tritium_ice 400, thorium 240. Wren Farwander pays 25,000cr per live seam LOCATION (>300 units) of adamantite/darksteel/tritium/polonium — selling intel is not selling ore.
