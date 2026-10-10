# Game knowledge — mechanics + play-only facts
Untagged lines = verified live in S1–S3 (game <= v0.613.4, t <= 2098845). `[docs]` = official docs only, never tested by us. `[?]` = hypothesis. When play contradicts a line, fix it in place and note it in LOG.md. Full official rules: docs/reference.md (grep it, don't read it whole).

## Verified S4 (t2099600, v0.613.4)
- Module skill requirements are NOT enforced: em_disruptor_i (lists weapons 3) installed with Weapons 0 (EXP-2). Fit cloaks/scanners without the listed skill.
- Empire-exclusive hulls: commission_quote/commission_ship for a Voidborn design (absence, eigenstate...) at a non-Voidborn yard -> `wrong_faction` ("commission it at a voidborn shipyard, or license and build it at your own faction station").
- Missions "Craft N items" count craft RUNS, not output units. `quantity` on a multi-output recipe is output units, rounded to runs (slugs: quantity 2 -> 1 run of 5).
- Uninstall/reinstall of a weapon empties its magazine. install_mod needs the module in CARGO (withdraw from storage first); uninstall_mod takes `module_id` from get_ship.
- Storage API: tool spacemolt_storage actions view|deposit|withdraw (item_id, quantity). `view` with no station returns `locations` = every station holding our items (sm.py stock uses it).
- Jettison [help text]: containers last 10 min and are lootable; when one despawns, ore matching that POI's deposit settles back into the deposit (dumping filler does not strip the belt). Mid-flight jettison destroys the cargo.
- Taxes: Voidborn income tax 6% (missions + market margin + salvage + ship/facility sales + rescue), property tax 0.75% of hull+fitted modules of every owned ship, weekly-ish assessment. `prepay_tax` escrows credits (surplus refunded); unpaid tax becomes a bounty (`pay_bounty empire source=self`). Sales tax: Voidborn/Nebula 1%, Solarian 3%, Crimson 4%. Tax record showed 51,700cr market sales from early sessions.
- Chat: get_chat_history fields sender, content, timestamp_utc, system_id. Last Light system chat: 2 messages in 3 weeks (quiet systems are useless for counter-recon).
- Achievements 8/68 (t2099600): open targets with progress — voyager_ii 127/250 systems, jump_master 1,204/25,000, artisan 166/10,000 crafts, deep_core_master 0/25, threshold_crosser 0/25, industrialist 0/10, well_insured 0/10, first_blood 0/1.

## Version watch (v0.613.4) — official changes that override older beliefs
- [docs v0.566.3] Module skill requirements are NOT enforced (only CPU/power limit fitting). The catalog still lists required_skills; our old "cloak needs Stealth 1" belief is probably dead -> EXP-2.
- [catalog] Ship gates: T1 hulls have no piloting_required; higher tiers need Piloting 10/20/30/50. Each empire has its own hull line. See docs/strategy.md ship plan.
- [docs] Removed: repair_module/module wear, salvage_wreck. Rescue missions: one claimable mission per mayday via accept_mission, 30-min expiry, counts toward the 5-mission cap (v0.608.0). Hit table per gun (v0.593). Arena (Krynn Blood Arena): combat XP only, 500/skill/day, no credits (v0.586).
- [docs] Rate limits 30 mutations + 300 queries per minute per session; login/session creation 30/min/IP (escalating IP timeouts).
- [docs] Starter ships earn no combat XP (v0.553.1) — CONFLICT with D30 (Threshold got Gunnery +12 from a grazer): trust the live result.

## XP / skills
- XP table (same for every skill): level N->N+1 costs [60,165,340,585,900,1285,1740,2265,2860,3525,4260,5065,5940,...]. Piloting 9->10 = 3,525 XP. Skills never lost.
- Piloting XP: jump +3, in-system travel +1, mine cycle +1 (measured: stackmine 0.84 XP/tick = ~5/min; dock loop 0.67/tick; jumping 3 per 6 ticks = 0.5/tick). A mine cycle is 1 per tick. Catalog: 'higher-tier ships grant more XP per action'.
- Crafting + Refining: EVERY workshop run gives +5 XP to BOTH (verified on iron smelt, copper wiring, glass, crystal facet) regardless of recipe time/size. Train with the cheapest-input recipes: basic_iron_smelting (10 Fe->1 steel, 0.3 tick), basic_copper_processing (8 Cu->1 wiring), smelt_lead_ingot (4 Pb->2), draw_platinum_wire (4 Pt->1), roll_lead_sheet (3 ingot->2), fuse_reinforced_glass (5 Si). 77 runs = ~385 XP each skill in ~4 min. `sm.py train` does it. Rented facility jobs give less XP; use the Station Workshop. Workshop speed scales with max(Crafting, Refining).
- Engineering passive XP (~1/tick) needs reactor load >=90% (Threshold: ML II + ML II = 29/30 OK; ML II + Cargo Expander = 24/30 off; one ML II = 22/30 off). Engineering draw drops ~1%/level.
- exploration XP: first visit to a system (small). deep_core_mining: mining with power 3+ gear. Mining skill gains fast (~+1 per cycle too).

## Combat as XP (tested t2098460): NOT a Piloting shortcut
- A 25-tick grazer fight gave Piloting +5 (mining gives ~21 in the same ticks), Gunnery +12, Weapons +4, Tactics +10, Xenobiology +3. Autocannon I (1,500 @ ramens_rest; no skill req; 10 dmg/tick, 500-round mag; ammo = manufacture_standard_rounds: 1 steel -> 5 boxes, 1 box fills the magazine) needs `spacemolt_battle reload weapon_instance_id=<id> ammo_item_id=standard_rounds_box` and `advance` x4 to reach the 'inner' zone; grazers (60 hull) hit back ~1.4/tick and may flee. EM disruptor needs weapons skill 3 + em_charge (unusable).

## Mining
- Each cycle picks ONE deposit: weight = richness x (1 + 0.1 x Mining x rank); rank common0 uncommon1 rare2 exotic3 legendary4. Yield is super-linear in beam, but supported power p caps rare picks (Si p2-4 -> +1..3 per pick whatever the beam). A big beam mostly fills the hold with filler faster; at pioneer_fields beam 24 gave 0 Ti in 24 cycles while beam 12 gave ~1 Ti per 2.6-4.5 cycles (hypothesis, repeatable). For rare ores use ONE ML II.
- Depleted deposits cap usable beam; regen ~0.3-0.5/tick policed, ~1/min for Ti at pioneer_fields; Crystal Sand Si shrinks when mined and regenerates slowly. Other players mine the same deposits (Ti 76->0 in ~20 min with 4 miners).
- `mine` returns error cargo_full when the hold is full (sm.py treats it as normal). Jettisoned ore is lost to us (container despawns after 10 min, matching ore returns to the deposit): user-approved ONLY for iron/copper filler while mining rare ore (scripts/stackmine.py). With jettison the hold (65) caps a trip at ~55-59 of the rare ore.
- Policed belts are drained; lawless belts have 10k-100k Fe/Cu. Rare ores sit in nebulae/special POIs (Crystal Sand, null_dust, garnet_belt...). Use `python3 scripts/res.py ore <name>`. NICKEL is scarce on the known map (only pioneer_fields).
- unknown_edge_mineral_fields (station in same system): beam 24 -> carbon 16, aluminum 14, vanadium ~8, iridium 4 per pick; hold 65 fills in ~9 cycles.

## Crafting
- Station Workshop hand-crafting is FREE; inputs must be in THIS station's storage; jobs advance only while docked there. `quantity` = runs (multi-output recipes round: carbon_arc_circuit_etching quantity 2-3 = 1 run = 3 boards). Bulk: jobs=[...] up to 50. dry_run=true quotes.
- FACILITY (FAC) recipes rent a station facility per run (e.g. forge_titanium_alloy 37cr/run at Frontier Station only; deep_range_outpost has no Alloy Foundry); jobs keep running after undock.
- Key routes: circuit_board = carbon_arc_circuit_etching (12 C + 2 Si -> 3); titanium_alloy = forge_titanium_alloy (FAC: 3 Ti ore + 1 steel -> 1) or anchor_plate_forging (3 anchor_plate -> 2; plates only from wildlife/market); focused_crystal = 4 trade_crystal (workshop 24 ticks) | 4 raw_focusing_crystal; steel = basic_iron_smelting (wk) | refine_steel (FAC); silicate_composite = 4 Si + 2 Ni (wk) or 2 Si + 2 Ni + 1 iridium_ore (bond_iridium_silicate_composite); copper_wiring = basic_copper_processing (wk 8 Cu) | process_copper_wiring (FAC 4 Cu -> 2). refractory_sinter has no recipe.
- Lookup: `python3 scripts/recipe.py tree <item>` / `recipe.py <item>` / `recipe.py item <item>` (catalog cached /tmp/catalog.json from https://game.spacemolt.com/api/catalog.json).
- onboard_* recipes are SHIP capabilities (not station-craftable). Catalog lists required_skills (mining_laser_ii mining 2; cloaking_device_i stealth 1) but docs say they are not enforced since v0.566.3 (EXP-2).
- [docs] Crafting has no skill gate; Crafting/Refining only speed the Workshop (up to 5x at 100). Facility jobs give no Crafting XP. Do not re-issue a slow craft (duplicates the job). Rented public facility fee = 25% of output value.

## Fitting / ship
- Threshold: 1W/2D/2U, CPU 16, power 30, speed 1, jump 60 s, 1 fuel/jump, cargo 65, fuel 95. install/uninstall only at a dock. install_mod takes the TYPE id; uninstall_mod needs the INSTANCE id (read get_ship; ids change after withdraw/reinstall).
- Module stats (CPU/power): mining_laser_i 2/5 mine5 | ii 4/8 mine12 | iii 6/12 mine22 | strip_miner_i 7/22 mine50 common-only | deep_core_extractor mk_i 8/15 | survey_scanner_i 3/4 | ii 5/7 | cloaking_device_i 5/10 | afterburner_i 2/3 | cargo_expander_i 1/1 +20 | ii 2/2 +50 | shield_booster_ii 3/6 | em_disruptor_i 5/8 | autocannon_i 3/4 | shield_recharger_i 2/5 | thermal_hull_hardener 2/4.
- Starter ship uninsurable (replaced free). Death drops ~70% fitted modules to a recoverable wreck (anyone can loot) and 50-80% of cargo; credits/skills/storage/other ships safe. Owned ships can be stored and swapped at stations (`switch_ship`).

## Stealth / cloak
- Cloak strength = module + hull bonus x Stealth skill (1%/lvl) vs scan power. cloaking_device_i (cloak 40, 10 pw) lists stealth 1; ii (70) stealth 3; emergency_cloaking_system stealth 3; phase cloak (95) stealth 5 — requirements probably unenforced (EXP-2). Stealth XP +5 per activation (dock-cycle training). [docs] Cloak burns 1 fuel/tick undocked (free docked / at skill 10). The absence hull has an integrated cloak 30 + scan resistance 20.

## Risk / lawless
- Pirates patrol police<=20 systems; scanned = warning. ~120 lawless systems crossed (S2+S3), zero contact. In jump transit you are not at a POI. Combat logout: flag 30 ticks.
- TOW: an undocked ship whose session idles is recovered by the Galactic Salvage Authority to the nearest station (~500cr). Always end docked; chain `scripts/safe_dock.sh` after unattended jobs. Jobs can die when a tool call crashes/is interrupted: check `pgrep -f "explore.py|stackmine|sm.py loop"` + `sm.py status`; stackmine also stops with action_in_progress if you send other game actions meanwhile (don't).

## Economy / market
- Silicon, titanium ore, nickel are NOT sold anywhere seen (only buy bids 180/15/14); mine them. titanium_alloy not sold (bid 311). Market (Ramen's Rest t2095372): cargo_expander_ii 1,908, mining_laser_ii 7,308, survey_scanner_ii 30,800, autocannon_i 1,500.
- BUY vs CRAFT (user order S3): buy modules/upgrades (never ships) when market price < raw-resource cost; log in DECISIONS.md (D23).
- Gifts: `spacemolt_storage deposit target=<player> item_id=credits quantity=N` (must be docked; unlock after 1000 lifetime credits earned).
- Fuel tax per unit: Voidborn 2, Solarian ~6, Nebula ~5, Crimson ~4, Outer Rim ~1. exotic_matter is category ore (stockpile rule). Ore bids often 1cr.
- Empire treasury: Voidborn missions pay 0-84%; Solarian/Nebula/Outer Rim/Crimson pay in full.

## Missions
- Accept AT the issuing station; dock objectives count only after accepting; max 5 active; board visible only when docked (`sm.py missions`; get_missions raw output is truncated by sm.py).
- Paid S3: strategic_readiness_assessment 20,000 (Crimson, report back at war_citadel), last_known_position 8,000 (chain next = combat), five_capitals 15,000, grand_tour 12,000, cartography 4,000, local_survey 2,500, titanium_extraction 3,500, edge_of_known_space_reconnaissance 6,000 (accept at unknown_edge waystation; completes at deep_range_outpost). S2: wayfinder 20,000, memorial 8,000, debris 4,500, audit 20,000, prospectus 20,000.
- courier_to_haven provides no cargo (you must own 5 silver): avoid. Faction/delivery supply contracts (63k-100k) need delivered goods: Q4.
- Lawless/player stations may deny docking (wealth_lane).

## Tools / harness (cost control)
- sm.py = 1-line outputs; raw MCP game actions return ~10k tokens each. MCP session expires (re-login); sm.py session self-renews; both coexist.
- NEVER send several sleeping bash calls in one parallel block (tool crash). A crash does not always kill setsid jobs. Launch jobs in their own call; poll with one `sleep<=58; tail -1 log` per call.
- Repo workflow: work in a git clone of main; commit + `git push` (costs no tokens for file content). push_files (GitHub MCP) only as fallback — it needs the FULL content of each file. `git pull --rebase` before editing if anything else may have pushed.
- Efficiency lessons (S1–S3): biggest token sinks were pasting whole files to push, raw MCP game calls, polling a job every minute with long output, re-reading big tables, re-deriving documented facts. Decide a job's length up front, chain safe_dock, poll with 1-line output. Highest value per token: scripts that write machine-readable rows as a side effect (explore.py), measuring rates (XP/tick) before choosing a loop, one-command boots.
- Tick: https://game.spacemolt.com/health (hand-estimated stamps drift ~100+ ticks).
- Docs: https://spacemolt.com/docs/<slug>.md, public docs MCP https://game.spacemolt.com/mcp/docs, in-game `get_guide`, changelog in-game `get_version`. Map (all 505 systems + links, no police levels): https://game.spacemolt.com/api/map. Catalog: /api/catalog.json (1 req/min). Action log: `sm.py call spacemolt_social get_action_log '{"page_size":12}'`.

## Skill Guide Summary (v0.613)
- Tick ~10 s; 1 mutation per tick (a 2nd concurrent action returns action_in_progress); queries free (300/min); mutations 30/min. Jump time (7-speed)x10 s. 28 skills train by doing. Deposit lock: refused only if remaining <25% of max AND beam > 4x supported. Death keeps credits/skills/storage; respawn at home. Captain's log max 20 entries (newest is replayed on login: use it as GitHub-outage backup). Combat: avoid; flee early.
