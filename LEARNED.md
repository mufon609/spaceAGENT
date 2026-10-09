# LEARNED.md — facts only discoverable by playing (verified S3 unless marked). Append new ones; promote to knowledge.md/playbooks at close-out.

## XP / skills
- XP table (shared by all skills): level N->N+1 costs [60,165,340,585,900,1285,1740,2265,2860,3525,4260,5065,5940,...]. Piloting 9->10 = 3,525. Skill level 1 needs 60.
- Piloting XP: jump +3, in-system travel +1, mine cycle +1. Mining cycle = 1 per tick (~10 s, ~6/min incl. overhead) => mining ~6 XP/min beats jumping (3/min, 60 s/jump at speed 1).
- Crafting + Refining: EVERY workshop run gives +5 XP to BOTH skills, regardless of recipe time/size (verified: iron smelt, copper wiring, reinforced glass, trade-crystal facet). So train with the cheapest-input recipe: basic_iron_smelting (10 iron -> 1 steel, 0.3 tick/run, 10 runs = 3 ticks), basic_copper_processing (8 Cu -> 1 wiring), smelt_lead_ingot (4 Pb -> 2 ingots), draw_platinum_wire (4 Pt -> 1), roll_lead_sheet (3 ingot -> 2 sheets). 1,000 XP = 200 runs. Facility (rented) jobs give less XP: use the workshop.
- Engineering passive XP needs reactor load >=90% (Threshold: 2x Mining Laser II = 29/30 OK; with Cargo Expander II 24/30 = off).

## Mining
- Yield is super-linear in beam, but deposit supported-power p caps rare picks (Si p2-4 -> +1..3 per pick whatever the beam). A big beam does NOT raise rare-ore picks; it just fills the hold with filler faster. At pioneer_fields beam 24 gave 0 Ti in 24 cycles while beam 12 gave ~1 Ti per 4-5 cycles (hypothesis: pick weighting/p cap; unverified).
- Crystal Sand silicon: +1..3 per pick, ~1 pick in 3-4; the 89-170 unit deposit regenerates slowly and shrinks when mined (47->167 over ~600 ticks; 145->89 after 37 mined).
- unknown_edge_mineral_fields (station in the SAME system): carbon 16/pick, aluminum 14, vanadium ~8, iridium 4, dark matter 1 at beam 24; hold 65 fills in ~9 cycles.
- `mine` returns error code cargo_full when the hold is full (sm.py now treats it as normal). Jettisoned ore is gone (approved only for iron/copper filler).
- Other players compete: pioneer_fields titanium 76->0 in ~20 min with 4 miners present.

## Fitting / ship
- Cargo Expander II +50 (bought 1,908); install/uninstall at a dock only; installed modules are addressed by type id (install_mod id=mining_laser_ii) and by instance id for uninstall.
- Resonance Miner: `catalog type=ships id=resonance_miner` shows `Requires: Piloting level 10`, min crew 3, build list.

## Economy / market
- silicon_ore, titanium_ore, nickel are NOT sold anywhere seen (only buy bids 180/15/14); they must be mined. titanium_alloy is not sold either (bid 311).
- Buy-vs-craft: cargo_expander_ii 1,908, mining_laser_ii 7,308 at Ramen's Rest.
- Fuel is ~1 cr/unit in Outer Rim (taxes), 1 fuel per jump.

## Missions (full pay: Solarian, Nebula, Outer Rim, Crimson)
- S3 paid: strategic_readiness_assessment 20,000 (Crimson; 6 stations; REPORT BACK at war_citadel), last_known_position 8,000 (just dock Ironhearth; chain next = combat), five_capitals 15,000, grand_tour 12,000, cartography 4,000, local_survey 2,500, titanium_extraction 3,500, edge_of_known_space_reconnaissance 6,000 (accept at unknown_edge waystation; visit last_light + deep_range, dock deep_range_outpost, completes there).
- courier_to_haven gives no cargo (you must supply 5 silver): avoid. the_long_haul/other faction supply contracts need delivered goods (Q4).
- Missions only listed when docked; sm.py get_missions output is truncated: use `sm.py missions`.
- Max 5 active missions.

## Tools / harness
- Several `sleep` bash calls in ONE parallel block crash the tool; a crash does not kill setsid jobs. A user interrupt can kill an explore.py job -> check `pgrep -f explore.py` and the ship's state.
- MCP session expires (not_authenticated): re-login. sm.py session is separate and self-renews.
- push_files needs full file content: keep volatile files small.
- Tick: /health tick is the truth; hand-estimated stamps drift.
- explore.py `!` systems = jump through; without `dock` it ends in space; chain `; scripts/safe_dock.sh` for unattended runs.
