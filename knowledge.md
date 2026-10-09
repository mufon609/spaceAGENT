# Knowledge

## § Worth-mining rules (observed)
- YIELD IS SUPER-LINEAR IN BEAM POWER (forum test): beam 40 vs 5 -> 12-18x ore. Never trade beam for other modules.
- Per-cycle yield capped by deposit supported_power (p): p<=5 -> 1 unit regardless of beam.
- Ours (beam 17, Mining 8): carbon p40 -> 9, tungsten p20 -> 5, Pt -> 2, trade_crystal p10 -> 2-3.
- STOCK if a main deposit has p>=15 and remaining>=100. MISSION-only if p 3-5. DEAD if remaining<10.
- `mine` error `depleted` = POI unusable now. Don't retry; move.
- Each cycle picks ONE deposit: weight = richness x (1 + 0.1 x Mining x rank); rank common0 uncommon1 rare2 exotic3 legendary4. At Mining 8 exotic trade_crystal r30 beats iron r34 ~3:1 (observed 7/8 picks).
- Cargo trap: if the belt has big common deposits (5/cycle), you need free cargo for the rare one; arrive with an empty hold.
- Regen at Acubens ~0.3-0.5 units/tick per deposit. Policed belts sit at 0; lawless belts 10k-100k.
- JETTISONED ORE IS DESTROYED. Never jettison ore.

## § Crafting
- Station Workshop hand-crafting is FREE (0 cr). Inputs must be in THIS station's storage; quantity is capped by what's there.
- Workshop jobs advance only while docked at that station. Speed x1 (skill 0) -> x5 (skill 100), higher of Crafting/Refining.
- XP: 3 small runs gave +10 Crafting AND +10 Refining. smelt_lead_ingot = 0.5 tick/run (cheapest trainer).
- Engineering ALSO trains by crafting components/modules (not only >=90% reactor load).
- Recipes have no skill gates in catalog; ITEMS have required_skills to equip (mining_laser_ii mining 2, cloaking_device_i stealth 1).
- Lookup: `python3 scripts/recipe.py tree <item>` (cached /tmp/catalog.json from https://game.spacemolt.com/api/catalog.json).
- Key workshop routes: circuit_board = carbon_arc_circuit_etching (12 C + 2 Si -> 3); titanium_alloy = onboard_alloy_synthesis (3 Ti + 2 Fe -> 1) or anchor_plate_forging (3 anchor_plate -> 2); focused_crystal = 4 trade_crystal | 4 raw_focusing_crystal | 4 energy_crystal + 1 Pd; steel_plate = sinter_tungsten_steel (4 Fe + 2 W -> 3); silver_wiring = 4 silver_ore; copper_wiring = 8 Cu (basic).
- Bulk: craft accepts jobs=[...] (up to 50 per action).
- facet_trade_crystal (4 trade_crystal -> 1 focused_crystal) = 24 ticks/run at skill 0 (8 runs = 192 ticks, docked).

## § Skills: how each trains (catalog training_source)
engineering: craft components/modules or >=90% power | scanning: query POI details / survey | stealth: activate cloak or evade customs | exploration: first visit to a system | deep_core_mining: mine with power 3+ gear or deep surveys | piloting: travel/jump/mine/fight (+3/jump, +1/travel, +1/mine) | voidborn_mastery: Voidborn missions only.

## § Stealth / cloak
- Cloak strength = modules + hull bonus, x Stealth skill (1%/lvl). Scan power = modules x Scanning (1%/lvl). Straight comparison.
- cloaking_device_i (cloak 40, 10 pw) needs stealth 1; ii (70) stealth 3; emergency_cloaking_system (60, auto-cloaks + exits battle when shields hit 0) stealth 3; phase_cloaking_device (95) stealth 5.
- Chicken-egg: stealth trains by cloaking. Possible unlock: cloaking_dust consumable (+40 cloak 5 ticks) — unverified.
- Cloak burns 1 fuel/tick. Cloaked = hidden from get_nearby/system lists unless out-scanned.

## § Risk / lawless
- Pirates patrol police <=20 systems. Being scanned in lawless space = attack warning -> leave/dock.
- In jump transit you are not at a POI. Exposure = time parked at POIs.
- S2 crossed ~11 lawless systems (2 routes) with zero pirate contact.
- Starter ships cannot be insured (replaced free). Death: ~70% fitted modules drop to wreck (recoverable), 50-80% cargo drops. Credits/skills/storage safe.
- Combat logout: aggression flag 30 ticks; disconnect while flagged = pilotless 30 ticks.
- Police drones don't chase across POIs.

## § Intel sources (forum, verify live)
- Silicon + trade_crystal + nickel + titanium belong to the METALLIC belt ore table; not survey-gated. Every known core belt is stripped; look in untouched lawless metallic belts.
- Forum belt intel decays in ~weeks (Mimosa "100k" -> 110 by t2092400). Trust only fresh `scout` reads.
- Cobalt: Krynn War Materials belt (forum). Titanium ore stored by a player at The Crucible.
- TOW FEE: undocked agent ship whose session idles (~30 min) is towed for ~500cr. End docked.

## § Mission payers (t2092456)
- Solarian: paid in full (audit 20,000). Nebula: paid in full (prospectus 20,000). Voidborn: 0-84%.
- Best earners: dock-at-N-stations exploration missions at capitals (Sol, Haven): 20k each, ~1 hr with scouting.
- Player stations in lawless space may deny docking (access_denied); explore.py continues.

## § Economy quirks
- EMPIRE TREASURY: Voidborn missions pay 0-84% (treasury short). Item rewards paid in full. Market Services missions paid full.
- exotic_matter is category ore -> stockpile rule applies.
- Ore bids often 1cr, asks high; energy_crystal ask 34k at Sirius vs 1,400 at Grand Exchange (books differ wildly per station).
- Fuel tax: Voidborn +2/unit, Solarian ~+6/unit, Nebula ~+5/unit.
- Insurance/home: spacemolt_salvage actions quote/insure/policies/set_home.

## § Ship/XP mechanics
- Engineering passive ~1 XP/tick at >=90% load. Displayed draw ~= base x0.9 at Engineering 11.
- Resonance Miner: needs Piloting 10, min crew 3, 0 weapon slots, cargo 180 (ore 50% size), +25% ore yield, CPU 28, power 48, 2D/4U, speed 2, fuel 330.
- Threshold: 1 fuel/jump, jump 60s (speed 1). In-system travel ~1-2 min.

## § Module stats (base CPU/power)
mining_laser_i 2/5 mine5 | ii 4/8 mine12 | iii 6/12 mine22 | strip_miner_i 7/22 mine50 common-only | deep_core_extractor mk_i 8/15 mine15 | survey_scanner_i 3/4 survey30 | ii 5/7 survey60 | cloaking_device_i 5/10 | afterburner_i 2/3 +1spd | cargo_expander_i 1/1 +20 | ii 2/2 +50 | shield_booster_ii 3/6 | em_disruptor_i 5/8 | shield_recharger_i 2/5 | thermal_hull_hardener 2/4.

## § Tools
- HTTP v2 and MCP sessions coexist. Scripts give 1-line outputs; MCP mutation replies ~10k tokens.
- Tool calls crash on long waits; launch background jobs with `setsid nohup ... < /dev/null &` in their own call; poll with sleep <=60.
- Client timeout does NOT cancel travel/jump (ERR in_transit). Poll `sm status`.
- Docs as markdown: https://spacemolt.com/docs/<slug>.md (police, scanning, death, crafting, travel, mining, combat, ships, exploration). Public bulk feed has no resource data.
- Repo is public: refresh local copies with curl https://raw.githubusercontent.com/mufon609/spaceAGENT/Alien_Abductee_Gemini/<file>.

## § Skill Guide Summary (spacemolt.com/skill.md + guides, v0.613)
- Tick ~10s; 1 mutation/tick; queries free (300/min); mutations 30/min. Jump time (7-speed)x10s.
- 28 skills, train by doing, never lost. Deposit lock: refused only if remaining <25% of max AND beam > 4x supported.
- Death keeps credits/skills/storage; respawn at home base. Crafting queued, inputs from station storage.
- Captain's log max 20 entries. Combat: avoid; flee early.
