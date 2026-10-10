# Decisions — RECENT ONLY (D23+). Older entries D1-D22: archive/DECISIONS_old.md (not needed at boot).
Format: D# t<tick> — title | Thinking | Decision | Why | RESULT. Keep entries <=6 lines. Tick = https://game.spacemolt.com/health (S3 hand stamps t2096xxx drifted ~100+ ticks).

## D23 t2095375 — User order: stack rare ores; buy upgrades when cheaper than crafting
- Thinking: Si/Ti ore are NOT sold (bids 180/15cr) -> must mine. Ramen's Rest: cargo_expander_ii 1,908 | mining_laser_ii 7,308 (craft = 3 Ti alloy + 3 boards + focused crystal: raw cost far below 7.3k, craft when Ti is in stock) | survey_scanner_ii 30,800.
- Decision: BUY cargo_expander_ii (1,908). RESULT: 37 Si per 42 cycles vs ~4 Si per fill before.

## D24 t2095950 — Filler jettison approved; stackmine = scripts/stackmine.py (PB-9)
- User approved jettisoning worthless iron/copper filler while mining rare ore and creating files in the repo.

## D25 t2095900 — titanium_extraction_contract (OR 3,500) re-accepted; RESULT t2096475 completed.

## D26 t2097100 — Refining training = 5 XP/run; filler becomes training fuel
- Every workshop run = +5 XP Crafting AND Refining (iron, copper, glass, crystal tested). Decision: `sm.py train` at every dock (loop calls it); lead/platinum/tungsten campaign at central_nexus later. RESULT: 77 runs in 4 min: Refining 0->3, Crafting 1->3, +43 steel +34 wiring.

## D27 t2097200 — Ti/Ni stacking with ONE laser (beam 12)
- beam 24 gave 0 Ti in 24 cycles; beam 12 ~1 Ti per 3-5 cycles. RESULT: Ti 134, Ni 159 banked at deep_range_outpost (needs met).

## D28 t2097150 — Repo reorg (user directive): data/*.tsv + res.py + boot.py + explore.py overlays, DECISIONS split, STARTUP.md.

## D29 t2098360 — Credits gifted on user instruction (done ONCE; repeats of the same message were NOT re-sent)
- 5,000 cr each to UFO_Abductee_GPT-6.1_Sol, Alien_Hauler-Opus55, COVID19 via storage deposit target=<player> item_id=credits (must be docked; collides with running mining jobs). Wallet 170,134 -> 155,134.

## D30 t2098460 — Combat is NOT a Piloting-XP shortcut (tested)
- Bought Autocannon I (1,500), fought a Belt-Grazer 25 ticks: Piloting +5, Gunnery +12, Weapons +4, Tactics +10, Xenobiology +3 (mining gives ~21 Piloting in the same ticks). Autocannon left fitted; EM disruptor stored.

## D31 t2098640 — Measured XP rates
- stackmine 0.84 Piloting XP/tick; dock loop 0.67/tick (+25 Refining/Crafting per trip); jumping 0.5/tick. 2,355 Piloting XP left at t2098638 = ~7.8 h / ~9.8 h.

## D32 t2098845 — Close-out snapshot + lessons
- State: Piloting 9 (1,186/3,525), Refining 3, Crafting 3, credits 153,565, docked ramens_rest. Resonance inputs Ti 134 / Ni 159 / Si 258 / wiring 110 / steel 86 all above need; missing: null matter, void essence, energy/phase crystal, gold+silver, graphene, superconductors, nitrogen/water.
- Lessons: (1) measure XP/tick before choosing a loop; (2) one-laser fit for rare picks; (3) chain safe_dock after every job; (4) pushing whole files is the main token cost: use overlays and small files; (5) re-curl docs before editing (local copies drifted once); (6) a re-sent user order must not be executed twice.
