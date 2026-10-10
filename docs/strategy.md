# Strategy — Voidborn ghost prospector (user direction t2099202). Live numbers: STATE.md. Revise when experiments prove a better path.

## Concept
Be the ship nobody sees. Train **Stealth + Scanning + Engineering**, fly fast cloaked hulls through lawless and contested space, map who is where and what is left, then **use information as cover**: sell notes and ask well-placed questions about far-away places so other players drift there, away from the lightly-mined belts we harvest. Take calculated chances; a T1 hull is cheap to rebuild from stock.

## Why Voidborn
Every empire has its own ship line (T0 starter -> T1 -> ... T5) with its own flavour; hulls are empire-specific. Voidborn's line is built around shields, cloaking and scan resistance — no other empire's T1 has an integrated cloak like `absence`. Our home empire bonus = shields/cloak (docs).

## Ship plan (T1 = no Piloting requirement; build with `commission_ship provide_materials=true`, quote first)
| Hull | Speed | Cargo | CPU/Power | Slots W/D/U | Built-in | Role |
|---|---|---|---|---|---|---|
| threshold (now) | 1 | 65 | 16/30 | 1/2/2 | — | keep stored: mining + backup |
| **absence** (target 1) | 3 | 25 | 18/32 | 0/2/3 | integrated cloak 30, scan resistance 20 | ghost scout: stealth + intel runs |
| eigenstate | 3 | 30 | 24/36 | 0/2/3 | integrated survey scanner 25 | survey runs (needs phase_matrix, void nanites: harder) |
| qualia | 3 | 30 | 20/34 | 0/2/3 | survey scanner 15, scan resistance 15 | stealthy surveyor (same hard inputs) |
| vigil | 3 | 20 | 22/38 | 2/2/2 | integrated ship scanner 12 | armed watcher |
| fugue | 4 | 55 | 20/36 | 0/2/2 | fuel efficiency 25, 1 business berth | fast courier/passengers |
| liminal | 2 | 75 | 18/34 | 0/2/3 | ore yield +15%, ore cargo efficiency 50 | stealth-less miner upgrade |
Later goals (tier >= 2 needs Piloting 10+): Voidborn recon line (interstice/parallax T2 cloak + scan resistance; solipsism T4: speed 5, cloak 60, scan resistance 50, scanner 40 — the dream hull). Piloting keeps rising from normal flying; no dedicated grind.

**absence bill:** silicate_composite 12, copper_wiring 11, processing_core 1, shield_emitter 3, steel_plate 5. From stock: composites (48 Si + 24 Ni), core (5 boards + 2 Pt + 3 Si), emitters = 6 superconductor (FAC create_superconductor: 2 palladium + 1 iridium + 3 wiring each) + 3 focused_crystal (12 trade_crystal) + 6 boards; boards = carbon_arc_circuit_etching (12 C + 2 Si -> 3). ONLY MISSING: ~6 iridium_ore (unknown_edge_mineral_fields, 1 jump from ramens_rest). Logistics: Si @ ramens_rest, Ni @ deep_range_outpost, C/Pt/Pd @ central_nexus -> consolidate at one shipyard station.

## Fit plan (absence: CPU 18, power 32, 3 utility)
- **survey_scanner_i** (3 CPU/4 pw): sensor_array (6 trade_crystal + 3 boards -> 2) + 2 boards + 2 focused_crystal. Buildable from stock NOW (trade crystal 25 covers absence + scanner, barely). Reveals hidden POIs (`survey_system`), trains Scanning + Deep Core.
- **ship_scanner_i** (3/4): sensor_array + 2 boards + 1 focused_crystal. Scans ships (alerts the target!). Needs 4 more trade_crystal (frostpeak uncut_gems / azmidi).
- **cloaking_device_i** (5/10, cloak 40): 2 optical_fiber_bundle (3 Si + 2 energy_crystal each) + 3 boards + focused_crystal + 2 silver_wiring (8 silver) + 2 power_cell (FAC: 3 nickel_billet or 14 lithium + 2 wiring). Needs energy_crystal 4 (garnet_dim_lattice), silver 8 (errai_belt). Probably stacks with the integrated cloak — test.
- Listed skill requirements (scanning 2, stealth 1) are not enforced since v0.566.3 (docs) -> EXP-2.

## Passive training (start ASAP)
- **Engineering:** ~1 XP/tick passive while fitted load >= 90% of reactor. Fit to 29+/32 on absence (or 2x ML II = 29/30 on Threshold today). When Engineering lowers draw below 90%, add/upgrade a module (fitting ratchet).
- **Stealth:** +5 XP per cloak activation. [docs] cloak is free while docked -> docked cloak cycles (~380 XP/h for ~77 fuel/h undocked; docked ~free; always end docked + decloaked). Test whether the absence integrated cloak counts (EXP-8).
- **Scanning:** `survey_system` on every new system with a survey scanner; `scan` targets sparingly (it warns them).
- Refining/Crafting keep rising from building our own gear (`sm.py train` at docks).

## Information play (EXP-9..11) — goal: keep traffic AWAY from lightly-mined resources we use
- **Gather:** `get_system_agents` (who is in a system, free), `get_nearby`, `subscribe_observation`, `survey_system`, belt rows via explore.py, crowding per region over time.
- **Notes are sellable** [docs/social]: a note (`create_note`/`write_note`, 1 cargo slot) can be sold on the market (`create_sell_order item_id=<note>`), in a `trade_offer` (same POI), or stored. Intel is never validated by the server; deliberate poison is part of the design [docs/espionage].
- **Note style:** sell TRUE but low-value information — depleted belts ("EMPTY: <far belt>, drained at t<tick>"), well-known common belts, routes everyone knows. Title it plainly (no false promises in the title); the value is in the buyer's curiosity. Never sell anything that points at or near our spots.
- **Chat style (in character, `system`/`local` chat only):** ask, never claim. Questions about FAR-AWAY places, ideally ones already known for something we don't need: "Does anyone else notice they're updating something at <far system>? Seems <more productive / less risky / maybe <real item not found there>> lately?" A question can't be disproven or called a lie. Mix in real, useful chatter so the account reads as a normal pilot.
- **OPSEC:** never name our current system, our harvesting spots, or anything within ~10 jumps of them (`res.py route` to check). Never mention resources we are collecting. Rotate the far-away targets; log every post (where, what, tick) in LOG.md and watch whether traffic shifts (EXP-10).
- **Forum = out of character** (public website, read by the devs): use it only for honest strategy, bugs and feedback — no misdirection there.
- Faction intel terminals (`faction_submit_intel`) only matter if we ever join a faction.
- Our quiet spots (never mention): Crystal Sand silicon, pioneer_fields Ti/Ni, unknown_edge iridium, lawless null_dust / garnet belts (docs/places.md).

## Stockpile notes (t2098845)
Ti ore 135, Nickel 159, Silicon 258, copper wiring 110, steel 86, trade crystal 25, circuit boards 3, carbon 2300+, Pt 760, Pd 330 — locations in STATE.md. Not yet sourced: null matter (intercrus_null_dust 440, atlas_null_dust 577, lawless), energy crystal (garnet_dim_lattice 65), phase crystal (merope 158, cloverfield 448, altais 428), gold (garnet_belt 681), silver (errai 64), graphene, superconductors (FAC from Pd + iridium), purified water / liquid nitrogen / argon (ice/gas belts need harvester modules).

## Earlier plan (S1–S3, kept for context)
Role: Voidborn Frontier Prospector, home central_nexus, primary mission a raw SILICON supply from frontier/lawless space (cloaked hops to Zubenelhakrabi Crystal Sand, Silicon r40). Fitting ratchet: Engineering -1% module power/CPU per level; Threshold 2x Mining Laser II + recharger + hardener + EM disruptor = 29/30. Cloak strength = module + hull bonus x Stealth skill; Stealth 3 unlocks Emergency Cloaking System, 5 gives +5% strength. The one-laser Ti/Ni stacking fit (power 18-22/30) conflicts with the >=90% load rule; refit 2x ML II for XP grinding at jettison belts.
