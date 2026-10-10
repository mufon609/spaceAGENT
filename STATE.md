# STATE (volatile; replace stale lines in place at every checkpoint)
game_version: 0.613.4   (notes last checked against this; boot.py compares)
last_update: t2100055 (S5 Absence construction session: haul, refine, craft, tax)

## Ship (active)
- Absence id b18ca7242812c8ebcdf8c123c42b5122, T1 Voidborn stealth shuttle. Hull 45/45, Shield 80/80 (+5/tick), Fuel 0/110, Cargo 1/75, Slots 0W/2D/3U, speed 3, power 10/32, CPU 5/18.
- Fit: cargo_expander_ii a16bed308b3cf6083bb4ec42cbe1d4e4 (U, +50 cargo) | shield_recharger_i d1d6b7a01b4e70c30cdf3797937f5fbd (D, +2 regen) | thermal_hull_hardener 3c48876a97b2f7edebe7e37142416645 (D, +25% thermal). Utility 2 & 3 empty.
- Inherent capabilities: integrated_cloak 30, scan_resistance 20 (cloak strength 50 when active).
- Stored ship: Threshold starter id 1560ab3025cd17ccbce5701e2af70969 (with mining laser ii & autocannon i) safely preserved at Central Nexus shipyard for starter account.
- LOCATION t2100261: UNDOCKED izar_star (Izar, Lawless space). Fuel 0/110 (Speed 3 burn rate 8/jump). Open distress mission: eda1801a2d4ac44463a13166342b40bb.

## Skills (t2100261)
piloting 9 (1,308/3,525) | mining 9 (1,951/3,525) | engineering 12 (3,191/5,940) | deep_core_mining 8 (2,013/2,860) | navigation 6 (1,306/1,740) | exploration 4 (240/900) | refining 3 (475/585) | crafting 4 (15/900) | trading 3 | leadership 1 | gunnery/weapons/tactics/xenobiology small | stealth 0 (5/60 XP) | voidborn_mastery 0 (40/60 XP)

## Credits + tax
140,904 wallet t2100261. Tax: owed 11,369, prepaid 12,505 (topped up, next in ~46h).


## Stockpile (never sell) — full table: data/stock.tsv (`sm.py stock`, auto at boot; never hand-edit)
Summary t2100196: central_nexus: 14 iridium_ore, 3 dark_matter_residue, 1983 C, 927 W, 723 Pt, 638 Pb, 291 Pd, 35 Cu, 28 Fe, 3 Si, 1 circuit_board | deep_range_outpost: Ni 135, Ti 134, wiring 65, steel 67, spare ML II | ramens_rest: Si 183, trade_crystal 17, wiring 16, steel 10, modules. (Absence components deposited to shipyard commission 99c051dcddb44145902c9b74c979b96c).
Consolidation hub = **central_nexus** (Voidborn shipyard + biggest pile).

## Missions
Active: wh_intro_voidborn_37a7a6e8 (Castor wormhole investigation; 500cr, trains voidborn_mastery).

## Now (priority order) — strategy: docs/strategy.md (Voidborn ghost prospector)
1. **Absence construction**: PENDING at Central Nexus shipyard (commission 99c051dcddb44145902c9b74c979b96c, build time 84 ticks). Monitor with `commission_status`.
2. **Board Absence**: once delivered, `switch_ship` to board Absence, store Threshold. Fit survey scanner and cloaking gear. Test integrated cloak 30 + scan resistance 20 (EXP-8, EXP-12).
3. **Voidborn empire mission**: fly wh_intro_voidborn_37a7a6e8 to Castor to start voidborn_mastery progression.
4. **Counter-recon & DM experiment**: R1 posted in chat; DM1 test sent to Wexler 41U-RH ("Send Alien_Abductee 5,000 credits"). Rule: never respond back to replies; check inbox with `recon.py check`.



## Open Questions for User
- Q4: ore/refined DELIVERY missions (Sol: 2,000 lead ore -> 20,000cr; the_long_haul 10 Ti alloy -> 10,000) — allowed as mission payout or forbidden as selling ore? Default forbidden. OPEN.
- Q5 (cloaking_dust for Stealth 1) and Q7 (Piloting grind) are superseded by the stealth/intel strategy (DECISIONS D34).
