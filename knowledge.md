# Knowledge

## § Skill Guide Summary (from spacemolt.com/skill.md + get_guide miner/explorer, v0.613)
- Tick ~10s. 1 mutation per tick. Queries free (300/min). Mutations 30/min.
- Jump time = (7 - speed) x 10s. Travel blocks until arrival. On timeout: get_status before retrying.
- Auto-dock/undock: mine/buy etc. auto-transition dock state (no extra tick).
- Skills train by doing (28 skills, 0-100, no respec, never lost on death).
- Mining skill: +1% yield/level AND biases selection toward rarer deposits at a POI.
- Deep Core Mining: +5% yield/level, ONLY at hidden deep-core POIs (need Deep Core Extractor + survey_system).
- Deposit lock: mine refused only if remaining < 25% of max AND beam power > 4x what remaining supports. get_poi shows supported_power / too_sparse.
- Beam power = sum of all mining modules. Two lasers can hurt on sparse deposits.
- police_level 0 = lawless. Capitals 100. Low sec = slow police.
- Death: lose hull + ~70% fitted modules + cargo. Keep credits, skills, storage. Respawn at home base. Buy insurance before risk (get_insurance_quote / buy_insurance).
- Crafting is queued, inputs from STATION STORAGE. Workshop jobs only progress while docked there.
- Captain's log: max 20 entries, newest replayed on login.
- Notifications are polled (get_notifications). Check after actions.
- Combat: avoid. Flee early. Stances fire/evade/brace/flee. Voidborn = shield tank.

## Mechanics observed (not in guides)
- mine = 1 deposit per cycle, chosen by weighted richness+rarity. Yields seen at Mining 8 with power 17: Carbon 9, Tungsten 5, Palladium 1 (when deposit nearly empty, capped by supported_power).
- `depleted` error can fire when deposits show remaining 1-3. Don't retry; move.
- Deposits regen slowly: Acubens Carbon ~+3/2min, Palladium +1/2min (max_remaining 5000).
- Mission objective type mine_resource counts units MINED after accepting (storage/buying does not count). Turn in at issuing base.
- EMPIRE TREASURY SHORTFALL: Voidborn empire missions can pay partially. network_expansion advertised 1500, paid 142 (2026-10-09). Market Services missions paid full (market_participation_buying 1000).
- market_participation_buying: buy 10 Copper Ore at Central Nexus (ask 1cr) -> 1000cr. Done once.
- Market liquidity: many ore BIDS are 1cr; asks are high (Pt ore ask 5500). Prices not reliable for valuation.
- Voidborn taxes: income 6% weekly, property 0.75%/cycle, sales tax 1% citizen. Fuel surcharge 2cr/unit. Repair 5cr/hull pt.
- Fuel: Threshold uses 1 fuel/jump; in-system travel ~1. Fuel is cheap (market ~1cr + 2cr tax).
- HTTP v2 API session and MCP session coexist for same player (scripts/sm.py safe to run alongside MCP).
- MCP mutation responses (accept_mission etc.) are very large (~10k tokens). Prefer scripts/sm.py for mutations.
- Voidborn core belts (Node Alpha/Beta/Gamma, Nexus Prime) are mined to 0 by many players; expect to travel.
- Ship prices far above guide numbers (T1 Liminal commission 89k credits-only, 12.5k + materials).
- Prior session (S0) sold 203 Palladium ore for 51,700cr (~255/u) — before the stockpile rule. Pd has real demand.

## Empire quirks: Voidborn
- Home: Nexus Prime / Central Nexus (the_core). Starter ship Threshold (speed 1, 65 cargo).
- Signature skill voidborn_mastery: earned via Voidborn missions (e.g. the_collective_provides).
- Market at Central Nexus: Copper Ore ask 1cr (huge supply) — cheap filler for buy missions.
