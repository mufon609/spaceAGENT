# Decisions — RECENT ONLY (D23+). Older entries D1-D22: archive/DECISIONS_old.md (not needed at boot).
Format: D# t<tick> — title | Thinking | Decision | Why | RESULT. Keep entries <=6 lines. Tick = https://game.spacemolt.com/health (S3 hand stamps t2096xxx drifted ~100+ ticks).

## D23 t2095375 — User order: stack rare ores; buy upgrades when cheaper than crafting
- Thinking: Si/Ti ore are NOT sold (bids 180/15cr) -> must mine. Ramen's Rest: cargo_expander_ii 1,908 (craft = CE I + 2 Ti alloy + 4 flex polymer + 2 boards) | mining_laser_ii 7,308 (craft = 3 Ti alloy + 3 boards + focused crystal: raw cost far below 7.3k, craft when Ti is in stock) | survey_scanner_ii 30,800.
- Decision: BUY cargo_expander_ii (1,908) in place of ML II #2: cargo 115, beam 12. RESULT: 37 Si per 42 cycles vs ~4 Si per fill before.

## D24 t2095950 — Filler jettison approved; stackmine = scripts/stackmine.py (PB-9)
- User approved jettisoning worthless iron/copper filler while mining rare ore and creating files in the repo. Q4/Q5 still open.

## D25 t2095900 — titanium_extraction_contract (OR 3,500) re-accepted at deep_range_outpost
- RESULT t2096475: completed (29 Ti mined over 7 loop trips); pioneer_fields Ti then 0 -> slow regen, 4 competing miners.

## D26 t2097100 — Refining training = 5 XP/run; filler becomes training fuel
- Thinking: user asked to level Refining. Every workshop run = +5 XP Crafting AND Refining (iron, copper, glass, crystal tested). Cheapest: basic_iron_smelting 10 Fe, basic_copper_processing 8 Cu, smelt_lead_ingot 4 Pb, draw_platinum_wire 4 Pt.
- Decision: smelt banked Fe/Cu at every dock (sm.py train; loop calls it); big lead/platinum/tungsten campaign at central_nexus later.
- RESULT t2097100: 77 runs at deep_range_outpost (4 min): Refining 0->3, Crafting 1->3, +43 steel +34 wiring.

## D27 t2097200 — Ti stacking with ONE laser (beam 12)
- Thinking: beam 24 gave 0 Ti in 24 cycles at pioneer_fields; beam 12 ~1 Ti per 2.6-4.5 cycles. Ti is the Resonance bottleneck (90 ore for 30 alloys).
- Decision: ML II #2 stored at deep_range_outpost; stackmine titanium_ore. RESULT: Ti stock 104+ (>=90 needed); NICKEL now the scarce input (only pioneer_fields, drained).

## D28 t2097150 — Repo reorg (user directive)
- data/*.tsv + scripts/res.py + boot.py; explore.py upserts data/*_new.tsv overlay (small pushes); knowledge.md absorbs LEARNED.md; DECISIONS split recent/archive; STARTUP.md = proposed prompt.

## D29 t2098360 — Credits gifted on user instruction (done ONCE; later repeats of the same message were NOT re-sent)
- User asked for 5,000 cr to UFO_Abductee_GPT-6.1_Sol, Alien_Hauler-Opus55, COVID19 (first cancelled: accounts offline; then re-confirmed). Sent via storage deposit target=<player> item_id=credits at deep_range_outpost (needs docking; collides with running mining jobs: action_in_progress). Wallet 170,134 -> 155,134.

## D30 t2098460 — Combat is NOT a Piloting-XP shortcut (tested)
- Thinking: mining ~0.7-0.84 XP/tick => 8-10 h to Piloting 10. Catalog: piloting XP from travel/jump/mine/fight; higher-tier ships more per action.
- Test: bought Autocannon I (1,500), fought a Belt-Grazer 25 ticks at Crystal Sand: Piloting +5, Gunnery +12, Weapons +4, Tactics +10, Xenobiology +3. Not worth it; autocannon left fitted (power 18/30), EM disruptor in storage.

## D31 t2098640 — Measured XP rates (use for planning)
- stackmine (jettison filler, no travel): 0.84 Piloting XP/tick (~5/min). sm.py loop at pioneer_fields (docks + smelting): 0.67/tick + ~25 Refining/Crafting XP per 5-7 min trip. 2,355 Piloting XP left at t2098638 = ~7.8 h stackmine / ~9.8 h loop.
