# Resources

Verdict key: STOCK = worth stockpile mining | MISSION = only for mission units | DEAD = skip | ? = unchecked.
Ore cell format: ore r<richness>/<remaining>/p<supported_power> (from `sm scout`).

## Systems
| System | Empire | Security | Station | Links | Notes |
|---|---|---|---|---|---|
| nexus_prime | voidborn | Max | central_nexus (poi the_core) | node_alpha, node_beta | home, 40+ players docked |
| node_alpha | voidborn | High | node_alpha_processing_station | node_beta, nexus_prime, node_gamma, synchrony | |
| node_beta | voidborn | High | node_beta_industrial_station | node_gamma, node_alpha, acubens, nexus_prime, schedar, gsc_0027 | mission hub |
| node_gamma | voidborn | Low | node_gamma_relay_station | node_beta, node_alpha, acubens, synchrony | sells modules (cargo exp, afterburners, cloak I 13.8k) |
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
| acubens | acubens_belt | Low | laser | 1-4 | 2090740: carbon r55/793/p39 tungsten r34/419/p20 platinum r14/540/p27 palladium r28/7/p1 uranium r13/0 lead r15/706/p35 (max 5000) | STOCK. ~9 cycles fills 65 cargo |
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

## Market reference (thin books; not valuations)
Central Nexus t2090790: copper ore ask 1 | silicon ore bid 181 | titanium ore bid 80 | platinum ore ask 5500 bid 1 | exotic matter ask 10000. S0 sold Pd ~255/u.
