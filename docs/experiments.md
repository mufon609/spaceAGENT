# Experiments — how this pilot learns the game
Rules: the game changes constantly, so test cheaply before betting big. One line per hypothesis: cost, risk, payoff. Run cheap ones in gaps (docked, between jobs). Record RESULT with tick, move proven mechanics into docs/game.md, add new hypotheses whenever something surprises you. The market restriction is deliberate: find the crafting/mission/salvage path. Aim for at least one experiment per session.
Status: OPEN | RUNNING | DONE (result) | DEAD (why).

## Seeded (user-approved t2099202)
- **EXP-1 Commission a T1 hull from own materials** — `sm.py call spacemolt commission_quote '{"ship_class":"absence"}'`. DONE t2101500: Absence commissioned at Central Nexus yard for 9,255cr labor using self-crafted silicate composites, superconductors, focused crystals, circuit boards, processing core, and shield emitters. Active ship id `b18ca7242812c8ebcdf8c123c42b5122`.
  - EXP-1b: measure Piloting XP/tick in the T1 vs Threshold (catalog: higher tiers earn more per action). OPEN
- **EXP-2 Module skill requirements unenforced?** (docs v0.566.3) — install a module whose listed skill we lack (cloaking_device_i stealth 1, or em_disruptor_i weapons 3 which we own @ ramens_rest). Cost: ~0. Payoff: cloak/stealth training now. DONE t2099600: NOT enforced — em_disruptor_i (weapons 3) installed at Weapons 0.
- **EXP-3 Mining drone** — `recipe.py tree mining_drone` / `light_drone_bay`; a DroneLang MINE/DEPOSIT loop deposits straight to station storage (passive ore + Drone Control XP, +5 per action). Cost: crafting. Payoff: income while the ship does other things. OPEN
- **EXP-4 Freight + passengers on mission circuits** (PB-3) — `spacemolt_shipping list`, `list_station_passengers` at each capital dock. Cost: cargo space/time. Payoff: 400+200/hop per package on routes we fly anyway; carrier tier grows. OPEN
- **EXP-5 Arena** (Krynn Blood Arena) — does it give Piloting XP, or only combat skills (500/skill/day cap)? Cost: travel. Payoff: risk-free combat skills. OPEN
- **EXP-6 survey_system** — needs a survey scanner. DONE t2106000: Survey Scanner I crafted from stored components and fitted to Absence. Running `survey_system` reveals hidden POIs and spatial anomaly signatures. Deep Core Mining 8, Scanning 1.
- **EXP-7 Achievements with rewards** — `get_achievements` + catalog achievements[].rewards (credits/skill_xp/titles). Cost: queries. Payoff: free goals. DONE t2099600: 8/68 earned; targets listed in docs/game.md § Verified S4.

## Stealth / intel (user direction t2099202, D34)
- **EXP-8 Stealth XP sources** — which actions give Stealth XP: cloaking_device activation (+5 known), the absence integrated cloak, docked cloak cycles (docs: cloak free while docked)? Measure XP/h and fuel/h for each; pick the passive loop. OPEN
- **EXP-9 EMPTY notes** — docs/counter-recon.md. Does a note titled for a far place with content `EMPTY` sell on the market / via trade_offer? Price, buyer, complaints. OPEN
- **EXP-10 Misdirection questions** — docs/counter-recon.md (user's template). Per post: replies, unique senders, mentions of the place, anyone saying they'll go. Summarize here every ~5 posts. OPEN
- **EXP-11 Traffic map** — record crowding per region (`get_system_agents` counts, faction tags) into data (column or data/traffic.tsv) to know which resources are lightly mined and which far places make good decoys. Feeds EXP-10. OPEN
- **EXP-12 Scan-resistance in practice** — in lawless space with absence: how often are we scanned/engaged vs the Threshold? Being scanned = warning sign. OPEN
- **EXP-13 Voidborn Mastery training source** — hypothesis: can it be trained by flying cloaked or passive void transit? DONE t2106927: Proven NEGATIVE. Passive flight/cloaking grants 0 XP. Voidborn Mastery is earned EXCLUSIVELY through Voidborn Empire storyline missions (+15 to +35 XP each). Reached Level 2 (185/340 XP).
- **EXP-14 Wormhole discovery & navigation** — investigate Castor cluster anomaly signatures via `wh_intro_voidborn_37a7a6e8`. DONE/PARTIAL t2103500: Wormhole entrances are dynamic anomaly POIs discovered via survey_system; transit accuracy scales with wormhole_navigation (+1 accuracy/level).

## Backlog (agent adds here)
- Wrecks: `get_wrecks` at lawless belts / battle sites; loot modules for own use; `sell_wreck` at NPC salvage yards is allowed. Needs tow rig.
- Rescue missions: fuel calls on the emergency channel (needs a refueling pump), claim via accept_mission; XP + payout + tips.
- Unknown sources: void_essence, graphene_thread, superconductor alternatives (cobalt_concentrate, noble_matte), nitrogen/water ice → harvester modules (craft vs buy price check).
- Nickel elsewhere on the 505-system map (only pioneer_fields known).

## Results log (newest first; move proven facts to docs/game.md)
- t2106950: EXP-13 done (Voidborn Mastery trained exclusively via empire missions; L2 185/340), EXP-14 documented (wormhole mechanics & survey requirements).
- t2106000: EXP-6 done (Survey Scanner I crafted & fitted to Absence).
- t2101500: EXP-1 done (Absence commissioned & fitted).
- t2099600: EXP-2 done (skill reqs unenforced), EXP-7 done (achievements).

