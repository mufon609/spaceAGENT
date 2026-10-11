# Strategy — Voidborn ghost prospector (user direction t2099202). Live numbers: STATE.md. Revise when experiments prove a better path.

## Concept
Be the ship nobody sees. Train **Stealth + Scanning + Engineering**, fly fast cloaked hulls through lawless and contested space, map who is where and what is left, then **use disinformation as cover**: misleading chat questions and EMPTY notes about far-away places pull other players away from the lightly-mined belts we harvest (docs/counter-recon.md). Take calculated chances; a T1 hull is cheap to rebuild from stock.

## Why Voidborn
Every empire has its own ship line (T0 starter -> T1 -> ... T5) with its own flavour; hulls are empire-specific. Voidborn's line is built around shields, cloaking and scan resistance — no other empire's T1 has an integrated cloak like `absence`. Our home empire bonus = shields/cloak (docs).

## Ship plan (T1 = no Piloting requirement; Voidborn designs ONLY at a Voidborn shipyard, e.g. central_nexus)
Quote: `sm.py call spacemolt_ship commission_quote '{"ship_class":"absence","bare_hull":false,"source_missing_materials":false}'` (shows credits-only vs provide-materials price). Build: same params on `commission_ship` with the materials in that station's storage.
| Hull | Speed | Cargo | CPU/Power | Slots W/D/U | Built-in | Role |
|---|---|---|---|---|---|---|
| threshold | 1 | 65 | 16/30 | 1/2/2 | — | stored at Central Nexus: combat bounties & backup |
| **absence (ACTIVE)** | 3 | 75 (w/ Expander II) | 18/32 | 0/2/3 | integrated cloak 30, scan resistance 20 | ghost scout, survey harvester, diplomatic courier |
| eigenstate | 3 | 30 | 24/36 | 0/2/3 | integrated survey scanner 25 | survey runs (needs phase_matrix, void nanites: harder) |
| qualia | 3 | 30 | 20/34 | 0/2/3 | survey scanner 15, scan resistance 15 | stealthy surveyor (same hard inputs) |
| vigil | 3 | 20 | 22/38 | 2/2/2 | integrated ship scanner 12 | armed watcher |
| fugue | 4 | 55 | 20/36 | 0/2/2 | fuel efficiency 25, 1 business berth | fast courier/passengers |
| liminal | 2 | 75 | 18/34 | 0/2/3 | ore yield +15%, ore cargo efficiency 50 | stealth-less miner upgrade |
Later goals (tier >= 2 needs Piloting 10+): Voidborn recon line (interstice/parallax T2 cloak + scan resistance; solipsism T4: speed 5, cloak 60, scan resistance 50, scanner 40 — the dream hull). Piloting keeps rising from normal flying; no dedicated grind.

## Active Absence Configuration & Strategy
- Absence commissioned at Central Nexus yard (id `b18ca7242812c8ebcdf8c123c42b5122`).
- Fit: cargo_expander_ii (+50 cargo to 75 total), survey_scanner_i (survey 30, hidden anomaly detection), mining_laser_i (precision extraction), shield_recharger_i (+2 regen), thermal_hull_hardener (+25% thermal defense). All 5 slots fitted.
- In-flight doctrine: automatic integrated cloaking immediately upon undock and after each hyperspace jump; 4 fuel cells held in cargo for autonomous mobile refueling; zero-market ore trading; separate armed Threshold stored at Central Nexus for combat missions.

## Voidborn Mastery Progression Strategy (Target Level 5+)
- Core insight: Voidborn Mastery CANNOT be trained by passive flight or cloaking. It is earned EXCLUSIVELY via Voidborn Empire storyline missions (+15 to +35 XP each).
- Storyline chain progression: complete active contracts (Conductive Lattice -> Resonance Substrate -> Final Calibration -> The Crimson Resonance) to progress through levels (L1=60, L2=165, L3=340, L4=585, L5=900).

- **survey_scanner_i** (3 CPU/4 pw): sensor_array (6 trade_crystal + 3 boards -> 2) + 2 boards + 2 focused_crystal. Buildable from stock NOW (trade crystal 25 covers absence + scanner, barely). Reveals hidden POIs (`survey_system`), trains Scanning + Deep Core.
- **ship_scanner_i** (3/4): sensor_array + 2 boards + 1 focused_crystal. Scans ships (alerts the target!). Needs 4 more trade_crystal (frostpeak uncut_gems / azmidi).
- **cloaking_device_i** (5/10, cloak 40): 2 optical_fiber_bundle (3 Si + 2 energy_crystal each) + 3 boards + focused_crystal + 2 silver_wiring (8 silver) + 2 power_cell (FAC: 3 nickel_billet or 14 lithium + 2 wiring). Needs energy_crystal 4 (garnet_dim_lattice), silver 8 (errai_belt). Probably stacks with the integrated cloak — test.
- Listed skill requirements (scanning 2, stealth 1) are not enforced since v0.566.3 (docs) -> EXP-2.

## Passive training (start ASAP)
- **Engineering:** ~1 XP/tick passive while fitted load >= 90% of reactor. Fit to 29+/32 on absence (or 2x ML II = 29/30 on Threshold today). When Engineering lowers draw below 90%, add/upgrade a module (fitting ratchet).
- **Stealth:** +5 XP per cloak activation. [docs] cloak is free while docked -> docked cloak cycles (~380 XP/h for ~77 fuel/h undocked; docked ~free; always end docked + decloaked). Test whether the absence integrated cloak counts (EXP-8).
- **Scanning:** `survey_system` on every new system with a survey scanner; `scan` targets sparingly (it warns them).
- Refining/Crafting keep rising from building our own gear (`sm.py train` at docks).

## Counter-recon (docs/counter-recon.md — playbook, user's exact template, running log)
Misleading chat questions + EMPTY notes about far places pull players away from our belts. Gather traffic data on every run (`get_system_agents`, `get_nearby`, `subscribe_observation`) to pick quiet belts and far decoys (EXP-11). Faction intel terminals only matter if we ever join a faction.

## Stockpile notes (t2098845)
Ti ore 135, Nickel 159, Silicon 258, copper wiring 110, steel 86, trade crystal 25, circuit boards 3, carbon 2300+, Pt 760, Pd 330 — locations in STATE.md. Not yet sourced: null matter (intercrus_null_dust 440, atlas_null_dust 577, lawless), energy crystal (garnet_dim_lattice 65), phase crystal (merope 158, cloverfield 448, altais 428), gold (garnet_belt 681), silver (errai 64), graphene, superconductors (FAC from Pd + iridium), purified water / liquid nitrogen / argon (ice/gas belts need harvester modules).

## Fuel Self-Sufficiency & Independence (user directive t2100128)
Stop relying on station refuel services and empire taxes; eliminate purchasing token costs.
- **In-flight consumables:** `fuel_cell` (size 1) restores +20 fuel anywhere via `spacemolt use_item '{"item_id":"fuel_cell"}'`. Keeping 5 in cargo provides +100 autonomous fuel (covers a full tank on Absence, fuel cap 110).
- **Zero-cost production chain:**
  - `gas_harvester_i` (utility, 4 CPU, 6 power, mining power 8) harvests `hydrogen_gas` from clouds (e.g. `achernar_gas_pocket`, 4 jumps from Nexus Prime).
  - Workshop: `compress_hydrogen_gas` (8 H2 gas -> 3 liquid H2, 1.1 ticks).
  - Workshop: `craft_fuel_cell` (2 liquid H2 + 1 steel plate -> 1 fuel cell, 1.35 ticks).
  - Salvage alternative: `scavenge_fuel_cells` (8 salvage metal + 3 salvage components -> 4 fuel cells).
- **Rule:** Never pay station refuel tariffs or burn round-trips for fuel when autonomous fuel cells can be crafted from stocked filler steel + harvested gas.

## Earlier plan (S1–S3, kept for context)
Role: Voidborn Frontier Prospector, home central_nexus, primary mission a raw SILICON supply from frontier/lawless space (cloaked hops to Zubenelhakrabi Crystal Sand, Silicon r40). Fitting ratchet: Engineering -1% module power/CPU per level; Threshold 2x Mining Laser II + recharger + hardener + EM disruptor = 29/30. Cloak strength = module + hull bonus x Stealth skill; Stealth 3 unlocks Emergency Cloaking System, 5 gives +5% strength. The one-laser Ti/Ni stacking fit (power 18-22/30) conflicts with the >=90% load rule; refit 2x ML II for XP grinding at jettison belts.

