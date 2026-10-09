# Goals

## Now (priority order) — t2096104: DOCKED ramens_rest (last_light)
1. Piloting 8 (2716/2860) -> 9 -> 10 for the Resonance Miner (user building; min crew 3 via recruit_personnel). Best XP: mine cycle +1 (~4/min) > jump +3 (~3/min).
2. Titanium: 47 ore @ deep_range_outpost; contract titanium_extraction 10/20 (pioneer_fields drained, regen ~1/min). Option: craft 2nd ML II (9 Ti ore -> 3 alloy via forge_titanium_alloy @ frontier_station + 3 boards @ ramens_rest + focused crystal from 4 trade_crystal).
3. Si 93 stacked @ ramens_rest = enough. Scout unvisited systems near Crystal Sand (titawin, merope, hollowcrest, izar, rukbat) for Ti/silver/new belts (exploration XP).
4. Exotic crystals mission (8k): 6 exotic_matter (10 @ node_gamma, far), 2 focused crystal, 2 silicate composite (4 Si + 2 Ni each; Ni 49 @ deep_range).
5. Capital boards: dock-at-N-stations missions (best earners, full pay).

## USER DIRECTIVE (S3, t~2096100) — REPO/PROMPT REORG, do at close-out (NOT before the user says wrap up)
User: create/push any files; the prompt rule 'never create/delete files' is to be CHANGED; keep repo clean; keep next agent well informed; minimise next session's token cost; we will match repo to the agent prompt afterwards. Git is mine to update.
CLOSE-OUT PLAN:
1. Split resources.md into machine-readable data/belts.tsv + data/systems.tsv + scripts/res.py (`res.py ore silicon`, `res.py sys <id>`, `res.py route A B`, `res.py stale`) so the next agent never reads 30KB; resources.md becomes a <3KB index (ROUTES, STATIONS, game-vs-repo note).
2. DECISIONS.md: keep last ~6 entries only; move older ones to archive/DECISIONS_old.md (never read at boot).
3. progression.md = volatile state only (<2KB: location, credits, skills, stock per station, missions); static ship/mechanics go to knowledge.md.
4. scripts/boot.py: ONE command printing tick + status + active missions + preflight + list_ships (replaces 4-5 boot calls).
5. Push cost: push_files needs full file content, so keep every frequently changed file small; one commit per checkpoint.
6. Write STARTUP.md = proposed new agent prompt (allow data/ scripts/ archive/ edits, boot sequence, token rules, user orders: stack rare ores, buy-if-cheaper, filler jettison OK).

## User orders (S3) — override older 'craft, don't buy'
- STACK UP rare/blocker resources (silicon, titanium_ore, etc.) whenever found; bank in storage, return for more.
- BUY vs CRAFT: for any upgrade/module (NOT ships) compare exchange price vs raw-resource cost; if buying is cheaper, BUY it and SAVE the resources. Log comparison in DECISIONS (D23).
- JETTISON of worthless iron/copper filler while mining rare ore is APPROVED. Never jettison anything else. scripts/stackmine.py (PB-9).

## Income rules
- Solarian, Nebula, Outer Rim, Crimson missions pay in full (8k-20k). Voidborn underpaid (D1). Best: dock-at-N-stations circuits at capital boards (PB-7; S2 ~95k, S3 ~61k in 1 hr).
- No ore/refined DELIVERY missions without user OK (D7). Mine-only contracts are fine (ore stays ours).

## Strategy phases (user GAME-PLAN.md)
- P1 Wealth+XP <- HERE (161k). P2 Resonance Miner (user building). P3 fit: beam first (2-3 lasers) + survey_scanner + cloak; keep >=90% reactor load. P4 frontier Silicon runs.

## Open Questions for User
- Q4: Ore/refined DELIVERY missions (Sol board: 2,000 Lead Ore -> 20,000cr; the_long_haul 10 Ti alloy -> 10,000)? Allowed as "mission payout" or forbidden as "selling ore"? Default: forbidden. STILL OPEN.
- Q5: Stealth 1 unlock: buy a few cloaking_dust (3-4cr each) if it trains Stealth? Default: try other path first. STILL OPEN.
