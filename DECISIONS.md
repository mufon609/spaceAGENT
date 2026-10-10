# DECISIONS — decisions only, NEWEST FIRST. Boot reads the top 3. Older D1–D22: archive/DECISIONS_D1-D22.md.
Purpose: force decisiveness. Everything README permits is already decided — do it, write the decision here, move on. Ask the user ONLY for the README "Ask first" list. No running log of events: mechanics -> docs/game.md, experiment results -> docs/experiments.md, misdirection posts/replies -> docs/counter-recon.md, state -> STATE.md.
Format: `## D# t<tick> — title` then Thinking / Decision / Why, plus a RESULT line later. <=6 lines each. When this file passes ~15 entries, move the oldest to archive/.

## D38 t2100055 — Built Absence components; assembled at Central Nexus (user order)
- Thinking: Absence requires 12 silicate_composite, 11 copper_wiring, 1 processing_core, 3 shield_emitter, 5 steel_plate at a Voidborn shipyard.
- Decision: Hauled silicon, trade crystals, boards from Ramen's Rest; retrieved 20 iridium + 3 dark matter at Unknown Edge; sintered 12 silicate composites and gathered wiring/plates at Deep Range; flew 19 jumps to Central Nexus. Rented refinery for 6 superconductors; crafted focused crystals, circuit boards, and processing core at Workshop.
- RESULT: 12 silicate composites, 11 copper wiring, 5 steel plates, 1 processing core stored at Central Nexus. 3 shield emitters crafting at Workshop.


## D37 t2099600 — Taxes always prepaid; nomadic; one stock hub (user order)
- Decision: boot runs `sm.py tax` (prepay to owed+10%) and `sm.py stock` (data/stock.tsv). Prepaid 9,867 now (pool 12,499 vs owed 11,363). Never own/lease facilities or bases (no ongoing costs). Hub = central_nexus (Voidborn shipyard, biggest pile); absence will be built there.
- RESULT: workshop_production_run +3,500 (5 craft runs at ramens_rest); EXP-2 confirmed skill reqs unenforced.

## D36 t2099202 — Counter-recon is standing policy (user order)
- Decision: post misdirection questions in system/local chat using the user's template ("does anyone else notice they updating something at [LOCATION]? seems [MORE PRODUCTIVE / LESS RISKY / ITEM NOT FOUND THERE]") and sell `EMPTY` notes about far places, to pull players away from the belts we harvest. No asking first; no need to watch the named place; DO record every reply and sender.
- How + full running log: docs/counter-recon.md (scripts/recon.py post | note | check log). Only new strategic choices about it come back here.

## D35 t2099202 — Information play rules (user; detailed in docs/counter-recon.md)
- Goal changed from steering players toward competitors to keeping traffic AWAY from lightly-mined resources we use. Notes are sellable on the market (docs/social); intel is unvalidated by design. Rules: never reveal our location/spots or anything near them; chat = in-character questions about far-away places, never disprovable claims; sell true-but-low-value notes; forum (OOC, public) = honest only.

## D34 t2099202 — New direction: Voidborn stealth + scanning + information warfare (user)
- User: drop the fleet-merge plan and the T2 miner goal entirely; push stealth, scanning and engineering (passive, start ASAP); take chances; sell/spread scouting info about competitor regions so players crowd there while we harvest quiet belts.
- Decision: targets = absence (T1 cloak hull, ~6 iridium short) + survey_scanner_i (buildable from stock) + cloaking_device_i (needs energy crystal, silver, power cells). Selling information (notes etc.) is allowed. docs/strategy.md rewritten; EXP-8..11 added.

## D33 t2099202 — Repo reorg + solo plan + experiments (user directive, made from Claude Code, no play)
- User: move repo to `main`; lightweight and token-cheap; isolated account; restrict market to force crafting/learning (current rule kept; `sell_wreck` allowed); push boundaries creatively; approved the experiment list.
- Decision: README+STARTUP -> README + PROMPT.md; goals+progression -> STATE.md; DECISIONS -> LOG.md (newest first); knowledge/playbooks/resources/GAME-PLAN -> docs/; data overlays merged into data/*.tsv (git push makes small-file tricks unnecessary); docs/reference.md = condensed official docs v0.613.4; docs/experiments.md new.
- Findings (catalog v0.613.4): T1 Voidborn hulls have no piloting_required. absence is ~6 iridium short of a full bill from stock. Module skill reqs not enforced since v0.566.3 (docs).
- Decision: go SOLO; T1 ship ladder (superseded by D34).
- Scripts: safe_dock/kill/poll now cover stackmine.py + explore.py; res.py route uses the full public map; boot.py checks game version.

## D32 t2098845 — Close-out snapshot + lessons
- State: Piloting 9 (1,186/3,525), Refining 3, Crafting 3, credits 153,565, docked ramens_rest. Stock Ti 134 / Ni 159 / Si 258 / wiring 110 / steel 86; not yet sourced: null matter, void essence, energy/phase crystal, gold+silver, graphene, superconductors, nitrogen/water.
- Lessons: (1) measure XP/tick before choosing a loop; (2) one-laser fit for rare picks; (3) chain safe_dock after every job; (4) pushing whole files is the main token cost: use overlays and small files; (5) re-curl docs before editing (local copies drifted once); (6) a re-sent user order must not be executed twice.

## D31 t2098640 — Measured XP rates
- stackmine 0.84 Piloting XP/tick; dock loop 0.67/tick (+25 Refining/Crafting per trip); jumping 0.5/tick. 2,355 Piloting XP left at t2098638 = ~7.8 h / ~9.8 h.

## D30 t2098460 — Combat is NOT a Piloting-XP shortcut (tested)
- Bought Autocannon I (1,500), fought a Belt-Grazer 25 ticks: Piloting +5, Gunnery +12, Weapons +4, Tactics +10, Xenobiology +3 (mining gives ~21 Piloting in the same ticks). Autocannon left fitted; EM disruptor stored.

## D29 t2098360 — Credits gifted on user instruction (done ONCE; repeats of the same message were NOT re-sent)
- 5,000 cr each to three player accounts named by the user via storage deposit target=<player> item_id=credits (must be docked; collides with running mining jobs). Wallet 170,134 -> 155,134.

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
