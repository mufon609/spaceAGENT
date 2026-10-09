# Knowledge

## § Worth-mining rules (observed)
- Yield per cycle tracks the chosen deposit's supported_power (p): p<=5 -> 1 unit; p~20 -> ~5; p~40 -> ~9 (Mining 8, beam 17).
- STOCK if a main deposit has p>=15 and remaining>=100. MISSION-only if p 3-5. DEAD if remaining<10.
- `mine` error `depleted` = POI unusable now (seen with remaining 1-3). Don't retry; move. Script stops on any error.
- Each cycle picks ONE deposit (weighted richness x rarity). Low-richness rare ore (Pt r14) picked ~1 in 4 cycles at Acubens; a near-empty rare deposit wastes cycles at 1/cycle.
- Crowding: Voidborn core belts drained to 0 by many players. Regen at Acubens ~0.3-0.5 units/tick per deposit (C 793->880, Pt 540->618 over ~250 ticks while mined).
- Before mining: `sm scout`; log line to resources.md (tick, crowd, verdict).

## § Economy quirks
- EMPIRE TREASURY: Voidborn missions pay partially/0 when treasury short (2026-10-09: network_expansion 142/1500, copper 1512/1800, iron 0/1500, deep_core 323/5000). ITEM rewards still delivered in full (10 exotic_matter). Market Services missions paid full.
- exotic_matter is category ore -> stockpile rule applies.
- market_participation_buying: buy 10 Copper Ore @ Central Nexus (ask 1cr) -> 1000cr. Done once.
- mine_resource objectives count units mined after accept. Turn in at issuing base.
- Ore bids often 1cr, asks high: market prices are not valuations.
- Voidborn tax: income 6%/week, property 0.75%/cycle, sales 1%, fuel +2cr/unit (refuel 43 = 172cr), repair 5cr/hull.
- Ships cost far above guide numbers (Liminal commission 89k credits-only / 12.5k + materials).

## § Ship/XP mechanics
- Engineering: passive ~1 XP/tick while reactor load >=90% (verified, power 27/30). Engineering lowers module draw ~1%/lvl; when load <90% upgrade a module to restore ("fitting ratchet").
- Stealth: +5 XP per cloak activation; docked on/off cycling cheapest (GAME-PLAN, unverified).
- Piloting XP: +3/jump, +1/travel, +1/mine. PB-1 ~30/trip.
- Resonance Miner: needs Piloting 10, min crew 3, 0 weapon slots, hull 150 shield 160 armor 6, speed 2, fuel 330, cargo 180 (ore 50% size), +25% ore yield, CPU 28, power 48, 2D/4U. Defaults mining_laser_ii + shield_booster_ii.
- Threshold: 1 fuel/jump, jump 60s (speed 1).

## § Module stats (catalog, CPU/power)
mining_laser_i 2/5 mine5 | mining_laser_ii 4/8 mine12 | mining_laser_iii 6/12 mine22 | strip_miner_i 7/22 mine50 common-only | strip_miner_ii 9/32 mine80 common-only | deep_core_extractor mk_i 8/15 mine15, ii 10/20 mine25, iii 14/28 mine40 (deep-core access) | survey_scanner_i 3/4 survey30 | survey_scanner_ii 5/7 survey60 rare-detect | deep_core_survey_scanner 6/8 survey90 deep-core detect | cloaking_device_i 5/10 cloak40 | afterburner_i 2/3 speed+1 | afterburner_iii 5/8 speed+3 | cargo_expander_i 1/1 +20 | cargo_expander_ii 2/2 +50 | shield_booster_ii 3/6 shield+50.
Prices @ node_gamma t2090767: cargo_expander_i 416, afterburner_ii 5354, afterburner_iii 4953, cloaking_device_i 13807, survey_scanner_ii 30786, mining_laser_ii 7150.

## § Tools
- HTTP v2 and MCP sessions coexist. scripts/sm.py = 1-line outputs; MCP mutation replies ~10k tokens.
- Tool calls (MCP or bash) can crash on long waits (~5 min). Background jobs survive. On crash: `sm status` first.

## § Skill Guide Summary (spacemolt.com/skill.md + guides miner/explorer, v0.613)
- Tick ~10s; 1 mutation/tick; queries free (300/min); mutations 30/min.
- Jump time (7-speed)x10s. Mutations auto-dock/undock as needed.
- 28 skills, train by doing, never lost. Mining: +1% yield/lvl + rarer-deposit bias. Deep Core Mining: +5%/lvl only at hidden deep-core POIs (need Deep Core Extractor + survey_system).
- Deposit lock: refused only if remaining <25% of max AND beam > 4x supported. Beam = sum of mining modules.
- Security: police_level 0 = lawless; capital 100; Low = slow police; Frontier = minimal.
- Death: lose hull, ~70% fitted modules, cargo. Keep credits/skills/storage. Respawn home. Insurance: get_insurance_quote/buy_insurance.
- Crafting queued; inputs from station storage; workshop jobs run only while docked there.
- Captain's log max 20 entries; newest replayed on login.
- Combat: avoid; flee early; stances fire/evade/brace/flee.
