# Knowledge

## § Worth-mining rules (observed)
- YIELD IS SUPER-LINEAR IN BEAM POWER (forum test): beam 40 vs 5 -> 12-18x ore. Never trade beam for other modules.
- Per-cycle yield capped by deposit supported_power (p): p<=5 -> 1 unit regardless of beam.
- Ours (beam 17, Mining 8): carbon p40 -> 9, tungsten p20 -> 5, Pt -> 2, trade_crystal p10 -> 2-3.
- STOCK if a main deposit has p>=15 and remaining>=100. MISSION-only if p 3-5. DEAD if remaining<10.
- `mine` error `depleted` = POI unusable now. Don't retry; move.
- Each cycle picks ONE deposit: weight = richness x (1 + 0.1 x Mining x rank); rank common0 uncommon1 rare2 exotic3 legendary4. At Mining 8 exotic trade_crystal r30 beats iron r34 ~3:1 (observed 7/8 picks).
- Cargo trap: if the belt has big common deposits (5/cycle), you need free cargo for the rare one; arrive with an empty hold. Regenerating commons get richer over time (pioneer_fields Ti/trip fell 5 -> 1).
- Regen at Acubens ~0.3-0.5 units/tick per deposit. Policed belts sit at 0; lawless belts 10k-100k.
- JETTISONED ORE IS DESTROYED. Never jettison ore.

## § Crafting
- Station Workshop hand-crafting is FREE (0 cr). Inputs must be in THIS station's storage; quantity is capped by what's there.
- Workshop jobs advance only while docked at that station. Speed x1 (skill 0) -> x5 (skill 100), higher of Crafting/Refining.
- XP: 3 small runs gave +10 Crafting AND +10 Refining. smelt_lead_ingot = 0.5 tick/run (cheapest trainer).
- Engineering ALSO trains by crafting components/modules (not only >=90% reactor load).
- Recipes have no skill gates in catalog; ITEMS have required_skills to equip (mining_laser_ii mining 2, cloaking_device_i stealth 1).
- Lookup: `python3 scripts/recipe.py tree <item>` (cached /tmp/catalog.json from https://game.spacemolt.com/api/catalog.json).
- Key routes: circuit_board = carbon_arc_circuit_etching (wk: 12 C + 2 Si -> 3); titanium_alloy = forge_titanium_alloy (FAC: 3 Ti + 1 steel -> 1) or anchor_plate_forging (wk: 3 anchor_plate -> 2); focused_crystal = 4 trade_crystal | 4 raw_focusing_crystal | 4 energy_crystal + 1 Pd (wk); steel_plate = refine_steel (FAC 5 Fe -> 2) or sinter_tungsten_steel (wk 4 Fe + 2 W -> 3); silver_wiring = 4 silver_ore; copper_wiring = process_copper_wiring (FAC 4 Cu -> 2) or basic (wk 8 Cu -> 1).
- Bulk: craft accepts jobs=[...] (up to 50 per action).
- facet_trade_crystal (4 trade_crystal -> 1 focused_crystal) = 24 ticks/run at skill 0 (8 runs = 192 ticks, docked).
- FACILITY (FAC) RECIPES ARE RENTABLE: most empire stations host station-owned production facilities. `craft` auto-routes to one, charges labor + rental per run, runs ~0.1 tick/run, and KEEPS RUNNING AFTER UNDOCK. Examples: refine_steel 19cr/run, process_copper_wiring 17cr/run (deep_range_outpost); forge_titanium_alloy 37cr/run (frontier_station). Not "buying items" (service fee).
- If no facility here can run it, the `no_facility` error names the nearest public one. Use dry_run to quote.
- onboard_* recipes (e.g. onboard_alloy_synthesis) are SHIP capabilities: run automatically on hulls that have them; cannot be crafted at a station. recipe.py tags them SHIP.
- Facility jobs give less crafting XP than workshop (~+5 per job vs per run).
- frontier_station also rents: Polymer Synthesizer (Si+Ni -> flex_polymer), Fluorine Acid Bath (2 Si + etchant -> 5 circuit boards), Sensor Assembly Line, Nickel-Steel Forge, Plate Press.

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
- S2 crossed ~25 lawless systems (5 routes) with zero pirate contact.
- Starter ships cannot be insured (replaced free). Death: ~70% fitted modules drop to wreck (recoverable), 50-80% cargo drops. Credits/skills/storage safe.
- Combat logout: aggression flag 30 ticks; disconnect while flagged = pilotless 30 ticks.
- Police drones don't chase across POIs.
- TOW (CONFIRMED t2093500): ship left undocked while the session idled was recovered by the Galactic Salvage Authority to the nearest station (zubenelhakrabi -> ramens_rest), ~500cr. Not dangerous, but always end docked (scripts/safe_dock.sh).

## § Intel sources (forum, verify live)
- Silicon + trade_crystal + nickel + titanium belong to the METALLIC belt ore table; not survey-gated. Every known core belt is stripped; look in untouched lawless belts / special POIs (Crystal Sand).
- Forum belt intel decays in ~weeks (Mimosa "100k" -> 110 by t2092400). Trust only fresh `scout` reads.
- Cobalt: Krynn War Materials belt (forum). Titanium ore stored by a player at The Crucible.

## § Mission payers (t2094013)
- Paid in full: Solarian (audit 20,000), Nebula (prospectus 20,000), Outer Rim (memorial 8,000; wayfinder 20,000; debris 4,500). Voidborn: 0-84%.
- Outer Rim board (frontier_station = mobile_capital, first_step): wayfinder circuit 20k (6 OR stations within 3 jumps, 11-jump loop), memorial 8k (instant at first_step_memorial_station), debris 4.5k. Outer Rim fuel tax ~1cr/unit.
- Missions must be ACCEPTED at their issuing station (mission_not_available elsewhere). Dock objectives only count after accepting (re-dock if needed).
- Best earners: dock-at-N-stations exploration missions at capitals: ~20k each, ~1 hr with scouting.
- Player stations in lawless space may deny docking (access_denied); explore.py continues.

## § Economy quirks
- EMPIRE TREASURY: Voidborn missions pay 0-84% (treasury short). Item rewards paid in full. Market Services missions paid full.
- exotic_matter is category ore -> stockpile rule applies.
- Ore bids often 1cr, asks high; energy_crystal ask 34k at Sirius vs 1,400 at Grand Exchange (books differ wildly per station).
- Fuel tax: Voidborn +2/unit, Solarian ~+6/unit, Nebula ~+5/unit, Outer Rim ~+1/unit.
- Insurance/home: spacemolt_salvage actions quote/insure/policies/set_home.

## § Ship/XP mechanics
- Engineering passive ~1 XP/tick at >=90% load. Draw drops ~1%/level: Engineering 12 put Threshold at 26/30 (87%) -> passive XP OFF until a module upgrade (ML I->ML II gives ~29/30).
- Resonance Miner: needs Piloting 10, min crew 3, 0 weapon slots, cargo 180 (ore 50% size), +25% ore yield, CPU 28, power 48, 2D/4U, speed 2, fuel 330.
- Threshold: 1 fuel/jump, jump 60s (speed 1). In-system travel ~1-2 min.

## § Module stats (base CPU/power)
mining_laser_i 2/5 mine5 | ii 4/8 mine12 | iii 6/12 mine22 | strip_miner_i 7/22 mine50 common-only | deep_core_extractor mk_i 8/15 mine15 | survey_scanner_i 3/4 survey30 | ii 5/7 survey60 | cloaking_device_i 5/10 | afterburner_i 2/3 +1spd | cargo_expander_i 1/1 +20 | ii 2/2 +50 | shield_booster_ii 3/6 | em_disruptor_i 5/8 | shield_recharger_i 2/5 | thermal_hull_hardener 2/4.

## § Tools
- HTTP v2 and MCP sessions coexist. Scripts give 1-line outputs; MCP mutation replies ~10k tokens.
- Tool calls crash on long waits; launch background jobs with `setsid nohup ... < /dev/null &` in their own call; poll with scripts/poll.sh (sleep <=60).
- Client timeout does NOT cancel travel/jump (ERR in_transit). Poll `sm status`.
- Background jobs can still die when the agent session pauses -> ship idles undocked -> tow. Keep runs short near session end.
- Docs as markdown: https://spacemolt.com/docs/<slug>.md (police, scanning, death, crafting, travel, mining, combat, ships, exploration). Public bulk feed has no resource data.
- explore.py scans every non-planet/star/station POI (unknown types like "Crystal Sand" were skipped before t2094013).
- Action log: `sm call spacemolt_social get_action_log '{"page_size":12}'` explains surprises (tows, level-ups).
- Repo is public: refresh local copies with curl https://raw.githubusercontent.com/mufon609/spaceAGENT/Alien_Abductee_Gemini/<file>.

## § Skill Guide Summary (spacemolt.com/skill.md + guides, v0.613)
- Tick ~10s; 1 mutation/tick; queries free (300/min); mutations 30/min. Jump time (7-speed)x10s.
- 28 skills, train by doing, never lost. Deposit lock: refused only if remaining <25% of max AND beam > 4x supported.
- Death keeps credits/skills/storage; respawn at home base. Crafting queued, inputs from station storage.
- Captain's log max 20 entries. Combat: avoid; flee early.
