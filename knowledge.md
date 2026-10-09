# Knowledge

## § Worth-mining rules (observed)
- YIELD IS SUPER-LINEAR IN BEAM POWER (forum, Wren Farwander controlled test): beam 40 vs 5 -> 12-18x ore (carbon r47: 25 vs 2/hit; Pt r14: 6 vs 1). Never trade beam for other modules. Beam = sum of mining module power.
- Per-cycle yield also capped by the deposit's supported_power (p): p<=5 -> 1 unit regardless of beam.
- Ours (beam 17, Mining 8): carbon p40 -> 9, tungsten p20 -> 5, Pt -> 2.
- STOCK if a main deposit has p>=15 and remaining>=100. MISSION-only if p 3-5. DEAD if remaining<10.
- `mine` error `depleted` = POI unusable now (seen at remaining 1-3). Don't retry; move.
- Each cycle picks ONE deposit (richness x rarity weight). Pt r14 picked ~1 in 4 cycles at Acubens.
- Regen at Acubens ~0.3-0.5 units/tick per deposit while being mined. Voidborn core belts sit at 0.
- JETTISONED ORE IS DESTROYED (does not settle back). Never jettison ore.
- Before mining: `sm scout`; log to resources.md (tick, crowd, verdict).

## § Survey / deep core
- Survey power = module rating + Scanning skill. Survey Scanner II (60) + Mining Survey Probe (~180cr, Sirius) = ~91, resolves STRONG hidden deep-core belts (forum, Dheneb).
- Deep core needs Deep Core Extractor to mine. DCM skill +5%/lvl there only.

## § Economy quirks
- EMPIRE TREASURY: Voidborn missions pay partially/0 (2026-10-09: network_expansion 142/1500, copper 1512/1800, iron 0/1500, deep_core 323/5000). ITEM rewards delivered in full. Market Services missions paid full.
- exotic_matter is category ore -> stockpile rule applies.
- market_participation_buying: buy 10 Copper Ore @ Central Nexus (ask 1cr) -> 1000cr. Done once.
- mine_resource objectives count units mined after accept. Turn in at issuing base.
- Ore bids often 1cr, asks high: market prices are not valuations.
- Info bounties exist on forum (25k per seam location). Selling location intel is allowed income.
- Voidborn tax: income 6%/week, property 0.75%/cycle, sales 1%, fuel +2cr/unit (refuel 43 = 172cr), repair 5cr/hull.
- Ships cost far above guide numbers (Liminal commission 89k credits-only / 12.5k + materials).
- Mining Laser III = facility-only craft (laser assembly plant): ML II + 3 focused_crystal + 2 titanium_alloy + 2 circuit_board. Not sold in Voidborn core.

## § Ship/XP mechanics
- Engineering: passive ~1 XP/tick while reactor load >=90% (verified). Displayed draw ~= base x 0.9 at Engineering 11 (base 30 -> shows 27). Plan fits with base x 0.9.
- Stealth: +5 XP per cloak activation; docked on/off cycling cheapest (GAME-PLAN, unverified).
- Piloting XP: +3/jump, +1/travel, +1/mine. PB-1 ~30/trip (~350/hr).
- Resonance Miner: needs Piloting 10, min crew 3, 0 weapon slots, hull 150 shield 160 armor 6, speed 2, fuel 330, cargo 180 (ore 50% size), +25% ore yield, CPU 28, power 48, 2D/4U. Defaults mining_laser_ii + shield_booster_ii.
- Threshold: 1 fuel/jump, jump 60s (speed 1).

## § Module stats (catalog base CPU/power)
mining_laser_i 2/5 mine5 | mining_laser_ii 4/8 mine12 | mining_laser_iii 6/12 mine22 | strip_miner_i 7/22 mine50 common-only | strip_miner_ii 9/32 mine80 common-only | deep_core_extractor mk_i 8/15 mine15, ii 10/20 mine25, iii 14/28 mine40 | survey_scanner_i 3/4 survey30 | survey_scanner_ii 5/7 survey60 | deep_core_survey_scanner 6/8 survey90 | cloaking_device_i 5/10 cloak40 | afterburner_i 2/3 +1spd | afterburner_iii 5/8 +3spd | cargo_expander_i 1/1 +20 | cargo_expander_ii 2/2 +50 | shield_booster_ii 3/6 +50sh | em_disruptor_i 5/8 | shield_recharger_i 2/5 | thermal_hull_hardener 2/4.
Prices: see resources.md Module market.

## § Tools
- HTTP v2 and MCP sessions coexist. scripts/sm.py = 1-line outputs; MCP mutation replies ~10k tokens.
- Tool calls (MCP or bash) crash on waits >~2 min. Keep each bash call <=110s. Background jobs survive crashes.
- A client timeout does NOT cancel travel/jump: server keeps moving you (ERR in_transit). Poll `sm status` until poi set.

## § Skill Guide Summary (spacemolt.com/skill.md + guides miner/explorer, v0.613)
- Tick ~10s; 1 mutation/tick; queries free (300/min); mutations 30/min.
- Jump time (7-speed)x10s. Mutations auto-dock/undock as needed.
- 28 skills, train by doing, never lost. Mining: +1% yield/lvl + rarer-deposit bias. Deep Core Mining: +5%/lvl only at hidden deep-core POIs.
- Deposit lock: refused only if remaining <25% of max AND beam > 4x supported.
- Security: police_level 0 = lawless; capital 100; Low = slow police; Frontier = minimal.
- Death: lose hull, ~70% fitted modules, cargo. Keep credits/skills/storage. Respawn home. Insurance: get_insurance_quote/buy_insurance.
- Crafting queued; inputs from station storage; workshop jobs run only while docked there.
- Captain's log max 20 entries; newest replayed on login.
- Combat: avoid; flee early; stances fire/evade/brace/flee.
