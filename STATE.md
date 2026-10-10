# STATE (volatile; replace stale lines in place at every checkpoint)
game_version: 0.613.4   (notes last checked against this; boot.py compares)
last_update: t2100055 (S5 Absence construction session: haul, refine, craft, tax)

## Ship (active)
- Threshold id 1560ab3025cd17ccbce5701e2af70969, T0 starter (uninsurable, free replacement). Hull 75/75, Shield 80/80, Fuel 95/95, Cargo 115 (cargo_expander_ii fitted), Slots 1W/2D/2U, speed 1, power 20/30, CPU 12/16.
- Fit: mining_laser_ii e4eeee49de1176906fabb9be2130fb28 (U) | cargo_expander_ii (U) | autocannon_i 06c4502af99ff91b47e7c5abb010c2b9 (W) | shield_recharger_i 1f0da81d23fcc8b6f532f84796d7d916 (D) | thermal_hull_hardener ca1f562c57b452dcc8b03b181e8be2f0 (D).
- LOCATION t2100055: DOCKED central_nexus (nexus_prime, Voidborn capital). Hold empty. Fuel 95/95. Respawn/home base central_nexus. Nomadic: no owned/leased anything.

## Skills (t2100055)
piloting 9 | mining 9 | engineering 12 | deep_core_mining 8 | navigation 6 | exploration 4 | refining 3+ | crafting 3+ | trading 3 | leadership 1 | gunnery/weapons/tactics/xenobiology/scanning small | stealth 0 | voidborn_mastery 0

## Credits + tax
146,167 wallet t2100055. Tax: owed 11,369, prepaid 12,505 (topped up, next in 46.6h).

## Stockpile (never sell) — full table: data/stock.tsv (`sm.py stock`, auto at boot; never hand-edit)
Summary t2100055: central_nexus: 12 silicate_composite, 11 copper_wiring, 5 steel_plate, 1 processing_core, 14 iridium_ore, 3 dark_matter_residue, 1983 C, 927 W, 723 Pt, 638 Pb, 291 Pd, 35 Cu, 28 Fe, 3 Si, 1 circuit_board | deep_range_outpost: Ni 135, Ti 134, wiring 65, steel 67, spare ML II | ramens_rest: Si 183, trade_crystal 17, wiring 16, steel 10, modules.
Consolidation hub = **central_nexus** (Voidborn shipyard + biggest pile).

## Missions
Active: wh_intro_voidborn_37a7a6e8 (Castor wormhole investigation; 500cr, trains voidborn_mastery).

## Now (priority order) — strategy: docs/strategy.md (Voidborn ghost prospector)
1. **absence commission at central_nexus**: 3 shield_emitter crafting at Station Workshop. Once complete, call `commission_ship '{"ship_class":"absence","bare_hull":true,"source_missing_materials":false}'` (quote confirmed 9,255cr provide-materials).
2. **Switch to Absence**: board Absence once built, store Threshold. Test integrated cloak 30 and scan resistance 20 (EXP-8, EXP-12). Fit survey scanner / cloak modules.
3. **Voidborn empire mission**: fly wh_intro_voidborn_37a7a6e8 to Castor to start voidborn_mastery progression.
4. **Counter-recon**: R1 posted in nexus_prime system chat ("does anyone else notice they updating something at mirfak? seems more productive"), N1 EMPTY note created. Monitor responses (`recon.py check`).


## Open Questions for User
- Q4: ore/refined DELIVERY missions (Sol: 2,000 lead ore -> 20,000cr; the_long_haul 10 Ti alloy -> 10,000) — allowed as mission payout or forbidden as selling ore? Default forbidden. OPEN.
- Q5 (cloaking_dust for Stealth 1) and Q7 (Piloting grind) are superseded by the stealth/intel strategy (DECISIONS D34).
