# Knowledge

## § Worth-mining rules (observed)
- Yield per cycle tracks the chosen deposit's supported_power (p): p<=5 -> 1 unit; p~20 -> ~5; p~39 -> ~9 (Mining 8, beam 17).
- STOCK if a main deposit has p>=15 and remaining>=100. MISSION-only if p 3-5. DEAD if remaining<10.
- `mine` error `depleted` = POI unusable now (seen with remaining 1-3). Do not retry; move. Script stops on any error.
- Each cycle picks ONE deposit (weighted richness x rarity). Rare low-richness ore (e.g. Pt r14) rarely picked; a near-empty rare deposit wastes cycles at 1/cycle until drained.
- Crowding: Voidborn core belts drained to 0 by many players. Regen: Acubens ~+1-3/min per deposit (max 5000); Pherkad regen ~= 5 miners' drain.
- Before mining: `sm scout`. Log the line to resources.md (tick, crowd, verdict).

## § Economy quirks
- EMPIRE TREASURY: Voidborn missions pay partially or 0 when treasury short (2026-10-09: network_expansion 142/1500, copper 1512/1800, iron 0/1500). Market Services missions (market_participation_*) paid full.
- market_participation_buying: buy 10 Copper Ore @ Central Nexus (ask 1cr) -> 1000cr. Done once.
- Mission mine_resource objectives count units mined after accept (buying/storage doesn't count). Turn in at issuing base.
- Ore bids often 1cr, asks high: market prices are not valuations.
- Voidborn tax: income 6%/week, property 0.75%/cycle, sales 1%, fuel +2cr/unit, repair 5cr/hull.
- Ships cost far above guide numbers (Liminal commission 89k credits-only / 12.5k + materials).

## § Ship/XP mechanics
- Engineering: passive ~1 XP/tick while reactor load >=90% (verified: power 27/30). Engineering lowers module draw ~1%/level -> load drops; then upgrade a module to get back >=90% ("fitting ratchet", GAME-PLAN).
- Stealth: +5 XP per cloak activation, duration irrelevant. Cheapest: cloak on/off cycles while docked (~1 fuel each) (GAME-PLAN, unverified).
- T2 hulls require Piloting 10 (GAME-PLAN).
- Threshold: 1 fuel/jump, jump 60s (speed 1).

## § Tools
- HTTP v2 session and MCP session coexist. scripts/sm.py cuts output to 1 line/action.
- MCP mutation replies ~10k tokens; travel/jump may crash the MCP tool mid-flight: on crash run `sm status` before retrying (movement completes server-side).

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
