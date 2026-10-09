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
- Decision: smelt banked Fe/Cu at every dock; big lead (638)/platinum (725)/tungsten (927) campaign at central_nexus later; carry filler instead of jettisoning where a dock is near.
- RESULT t2097100: 77 runs at deep_range_outpost (4 min): Refining 0->3, Crafting 1->3, +43 steel +34 wiring.

## D27 t2097200 — Ti stacking with ONE laser (beam 12)
- Thinking: beam 24 gave 0 Ti in 24 cycles at pioneer_fields; beam 12 ~1 Ti per 2.6-4.5 cycles. Ti is the Resonance bottleneck (90 ore for 30 alloys).
- Decision: ML II #2 stored at deep_range_outpost, run stackmine titanium_ore. Engineering passive XP off meanwhile (power 22/30).
- RESULT t2097140: +13 Ti in ~35 cycles; run stopped by action_in_progress (a gift attempt collided; user cancelled the gift). Ti banked 79.

## D28 t2097150 — Repo reorg started (user directive)
- Decision: data/systems.tsv + data/belts.tsv + scripts/res.py + boot.py; explore.py upserts data; knowledge.md absorbs LEARNED.md; DECISIONS split recent/archive; STARTUP.md = proposed prompt. Reason: next session should spend tokens on playing, not re-reading 30KB.
