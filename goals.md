# Goals

## Now (priority order) — t2096475: DOCKED deep_range_outpost (OR)
1. Piloting is level 9 (58/3,525 XP): level 10 needs ~3,470 more XP = ~12 h of mining (~4 XP/min) or ~19 h of jumping (3/min). Resonance Miner (Requires Piloting 10; min crew 3; 40 copper_wiring, 30 titanium_alloy, 60 silicate_composite, ...). Our stock covers part of it: copper_wiring 40 @ deep_range, Ti ore 66 (=22 alloy; need 90 ore), Si 93 + Ni 74 (silicate_composite = 4 Si + 2 Ni each -> 60 needs 240 Si + 120 Ni). TELL USER; keep stacking Si/Ti/Ni.
2. Most useful mining for XP+stock: Crystal Sand (Si) via PB-9; pioneer_fields Ti yields only ~5-10 Ti per 40-cycle trip now (4 miners compete; Ti 82 left, p4).
3. Craft 2nd ML II from banked Ti (forge_titanium_alloy @ frontier_station: 3 Ti + 1 steel -> 1 alloy), or buy 7,308 @ ramens_rest (D23 rule: craft when Ti is in stock).
4. Exotic crystals mission (8k): 6 exotic_matter (10 @ node_gamma, far), 2 focused crystal, 2 silicate composite; Ni now 74.
5. Capital boards: dock-at-N-stations missions (best earners, full pay) - next circuit after Piloting plan.

## USER DIRECTIVE (S3, t~2096100) — REPO/PROMPT REORG, do at close-out (NOT before the user says wrap up)
User: create/push any files; the prompt rule 'never create/delete files' is to be CHANGED; keep repo clean; keep next agent well informed; minimise next session's token cost; we will match repo to the agent prompt afterwards. Git is mine to update.
CLOSE-OUT PLAN:
1. Split resources.md into machine-readable data/belts.tsv + data/systems.tsv + scripts/res.py (`res.py ore silicon`, `res.py sys <id>`, `res.py route A B`, `res.py stale`) so the next agent never reads 30KB; resources.md becomes a <3KB index (ROUTES, STATIONS, game-vs-repo note).
2. DECISIONS.md: keep last ~6 entries only; move older ones to archive/DECISIONS_old.md (never read at boot).
3. progression.md = volatile state only (<2KB: location, credits, skills, stock per station, missions); static ship/mechanics go to knowledge.md.
4. scripts/boot.py: ONE command printing tick + status + active missions + preflight + list_ships (replaces 4-5 boot calls).
5. Push cost: push_files needs full file content, so keep every frequently changed file small; one commit per checkpoint.
6. Write STARTUP.md = proposed new agent prompt (allow data/ scripts/ archive/ edits, boot sequence, token rules, user orders: stack rare ores, buy-if-cheaper, filler jettison OK).
7. New belt rows from S3 scouting after t2095950 (izar, hollowcrest, titawin, merope, tarazed, ain) are in /tmp/explore.jsonl only: run `python3 scripts/explore.py md` at close-out (lost if /tmp is wiped).

## User orders (S3) — override older 'craft, don't buy'
- STACK UP rare/blocker resources (silicon, titanium_ore, etc.) whenever found; bank in storage, return for more.
- BUY vs CRAFT: for any upgrade/module (NOT ships) compare exchange price vs raw-resource cost; if buying is cheaper, BUY it and SAVE the resources. Log comparison in DECISIONS (D23).
- JETTISON of worthless iron/copper filler while mining rare ore is APPROVED. Never jettison anything else. scripts/stackmine.py (PB-9).

## Income rules
- Solarian, Nebula, Outer Rim, Crimson missions pay in full (8k-20k). Voidborn underpaid (D1). Best: dock-at-N-stations circuits at capital boards (PB-7; S2 ~95k, S3 ~61k in 1 hr).
- No ore/refined DELIVERY missions without user OK (D7). Mine-only contracts are fine (ore stays ours).

## Strategy phases (user GAME-PLAN.md)
- P1 Wealth+XP <- HERE (164.6k). P2 Resonance Miner (user building). P3 fit: beam first (2-3 lasers) + survey_scanner + cloak; keep >=90% reactor load. P4 frontier Silicon runs.

## Open Questions for User
- Q4: Ore/refined DELIVERY missions (Sol board: 2,000 Lead Ore -> 20,000cr; the_long_haul 10 Ti alloy -> 10,000)? Allowed as "mission payout" or forbidden as "selling ore"? Default: forbidden. STILL OPEN.
- Q5: Stealth 1 unlock: buy a few cloaking_dust (3-4cr each) if it trains Stealth? Default: try other path first. STILL OPEN.
- Q7 (new): Piloting 10 needs ~3,470 more XP (~12 h mining). Is that the plan, or should I contribute my stockpile (silicate composite/Ti alloy/copper wiring) to the Resonance Miner commission you are building, or pursue another route to the hull?
