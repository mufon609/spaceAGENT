# LOG — decisions + discoveries, NEWEST FIRST. Boot reads the top 3. Older D1–D22: archive/LOG_D1-D22.md.
Format: `## D# t<tick> — title` then Thinking / Decision / Why / RESULT (add RESULT later). <=6 lines each. Tick from https://game.spacemolt.com/health.
When this file passes ~15 entries, move the oldest to archive/.

## D33 t2099202 — Repo reorg + solo plan + experiments (user directive, made from Claude Code, no play)
- User: move repo to `main`; lightweight and token-cheap; isolated account; restrict market to force crafting/learning (current rule kept; `sell_wreck` allowed); push boundaries creatively; approved the experiment list.
- Decision: README+STARTUP -> README + PROMPT.md; goals+progression -> STATE.md; DECISIONS -> LOG.md (newest first); knowledge/playbooks/resources/GAME-PLAN -> docs/; data overlays merged into data/*.tsv (git push makes small-file tricks unnecessary); docs/reference.md = condensed official docs v0.613.4; docs/experiments.md new.
- Findings (catalog v0.613.4): T1 Voidborn hulls have no piloting_required; T2 (resonance_miner etc.) need Piloting 10. absence is ~6 iridium short of a full bill from stock; resonance_miner is far (void essence/energy+phase crystal sources unknown, Piloting 10, crew 3). Module skill reqs not enforced since v0.566.3 (docs).
- Decision: go SOLO (fleet crafter hand-off dropped; user can re-enable). Ship ladder absence -> liminal -> resonance_miner.
- Scripts: safe_dock/kill/poll now cover stackmine.py + explore.py; res.py route uses the full public map; boot.py checks game version.

## D32 t2098845 — Close-out snapshot + lessons
- State: Piloting 9 (1,186/3,525), Refining 3, Crafting 3, credits 153,565, docked ramens_rest. Resonance inputs Ti 134 / Ni 159 / Si 258 / wiring 110 / steel 86 all above need; missing: null matter, void essence, energy/phase crystal, gold+silver, graphene, superconductors, nitrogen/water.
- Lessons: (1) measure XP/tick before choosing a loop; (2) one-laser fit for rare picks; (3) chain safe_dock after every job; (4) pushing whole files is the main token cost: use overlays and small files; (5) re-curl docs before editing (local copies drifted once); (6) a re-sent user order must not be executed twice.

## D31 t2098640 — Measured XP rates
- stackmine 0.84 Piloting XP/tick; dock loop 0.67/tick (+25 Refining/Crafting per trip); jumping 0.5/tick. 2,355 Piloting XP left at t2098638 = ~7.8 h / ~9.8 h.

## D30 t2098460 — Combat is NOT a Piloting-XP shortcut (tested)
- Bought Autocannon I (1,500), fought a Belt-Grazer 25 ticks: Piloting +5, Gunnery +12, Weapons +4, Tactics +10, Xenobiology +3 (mining gives ~21 Piloting in the same ticks). Autocannon left fitted; EM disruptor stored.

## D29 t2098360 — Credits gifted on user instruction (done ONCE; repeats of the same message were NOT re-sent)
- 5,000 cr each to UFO_Abductee_GPT-6.1_Sol, Alien_Hauler-Opus55, COVID19 via storage deposit target=<player> item_id=credits (must be docked; collides with running mining jobs). Wallet 170,134 -> 155,134.

## D28 t2097150 — Repo reorg (user directive): data/*.tsv + res.py + boot.py + explore.py overlays, DECISIONS split, STARTUP.md.

## D27 t2097200 — Ti/Ni stacking with ONE laser (beam 12)
- beam 24 gave 0 Ti in 24 cycles; beam 12 ~1 Ti per 3-5 cycles. RESULT: Ti 134, Ni 159 banked at deep_range_outpost (needs met).

## D26 t2097100 — Refining training = 5 XP/run; filler becomes training fuel
- Every workshop run = +5 XP Crafting AND Refining (iron, copper, glass, crystal tested). Decision: `sm.py train` at every dock (loop calls it); lead/platinum/tungsten campaign at central_nexus later. RESULT: 77 runs in 4 min: Refining 0->3, Crafting 1->3, +43 steel +34 wiring.

## D25 t2095900 — titanium_extraction_contract (OR 3,500) re-accepted; RESULT t2096475 completed.

## D24 t2095950 — Filler jettison approved; stackmine = scripts/stackmine.py (PB-9)
- User approved jettisoning worthless iron/copper filler while mining rare ore and creating files in the repo.

## D23 t2095375 — User order: stack rare ores; buy upgrades when cheaper than crafting
- Thinking: Si/Ti ore are NOT sold (bids 180/15cr) -> must mine. Ramen's Rest: cargo_expander_ii 1,908 | mining_laser_ii 7,308 (craft = 3 Ti alloy + 3 boards + focused crystal: raw cost far below 7.3k, craft when Ti is in stock) | survey_scanner_ii 30,800.
- Decision: BUY cargo_expander_ii (1,908). RESULT: 37 Si per 42 cycles vs ~4 Si per fill before.
