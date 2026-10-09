# Decisions

Log of real choices. Format: tick | decision needed | thinking | decision | why. Newest at bottom. Keep each entry <=6 lines.
Time = game tick (`curl -s https://game.spacemolt.com/health` -> tick; ~10s/tick, ~360 ticks/hr).

## D1 t2090950 — Voidborn missions pay 0-84%
- Need: keep doing empire missions?
- Thinking: treasury empty (iron 0/1500, deep_core 323/5000). Item rewards still paid in full.
- Decision: only take missions with item rewards or non-empire payers (Market Services). No detours for credit-only Voidborn missions.
- Why: time is better spent stockpiling/exploring than on unpaid work.

## D2 t2091300 — Laser upgrade path
- Need: more beam power (yield super-linear in beam).
- Thinking: ML II 7,007cr on market; ML III not sold anywhere. User rule (later): craft, don't buy items.
- Decision: do NOT buy ML II. Craft it: 3 titanium_alloy (onboard_alloy_synthesis 3 Ti ore + 2 Fe) + 3 circuit_board (carbon_arc 12 C + 2 Si) + 1 focused_crystal (focus_energy_crystal 4 energy_crystal + 1 Pd). All workshop recipes, no facility.
- Why: have C/Fe/Pd. Missing raw: titanium_ore 9, silicon_ore 2, energy_crystal 4 -> exploration target.

## D3 t2091440 — Safety layer before risk
- Need: survive PC shutdowns and lawless trips.
- Decision: preflight checklist each trip + `safe` emergency dock + exception/SIGTERM guard + setsid launch. Tested 3 paths live.
- Why: user requirement; unattended loops otherwise strand the ship in space.

## D4 t2091480 — Train Crafting/Refining (both 0)
- Thinking: workshop crafting is free. smelt_lead_ingot 4 Pb -> 2 ingots, 0.5 tick/run; ~+3 XP/run to BOTH crafting and refining. Lead is our least useful ore (652).
- Decision: burn lead into ingots at central_nexus during docked time (workshop only runs while docked). Outputs stay in storage (stockpile rule).
- Why: crafting skill gates/speeds every module build in D2. Cheapest XP available.

## D5 t2091490 — Lawless/frontier exploration risk
- Need: find titanium, silicon, energy_crystal, silver, nickel, cobalt.
- Thinking: Starter ship cannot be insured but is replaced free; death loses ~70% of fitted modules to a recoverable wreck + cargo; credits/skills/storage safe. Pirates patrol police<=20; being scanned = attack warning; at speed 1 flee is weak. In hyperspace (jump) you are not at a POI.
- Decision: go now with current fit (lasers needed to mine finds). Keep EM disruptor fitted (holds 90% reactor load = Engineering XP). Script leaves any POI with pirates; safe() on damage; fuel guard to return home.
- Why: user approved risk; expected loss small (~10k modules worst case, partly recoverable) vs. unlocking all crafting.

## D6 t2091490 — First exploration target: Solarian space via Pherkad
- Options: (a) frontier ring 2-3 jumps (gsc_0050, okab, megrez...) (b) Solarian border 7 jumps (furud) then Sirius 9.
- Decision: (b) node_gamma>synchrony>pherkad>gsc_0041>antares>homam>furud>nova_terra>sirius, scouting every belt.
- Why: Solarian = mining empire (Fe/Ti likely), stations to refuel/dock at the far end, Sirius sells Mining Survey Probe, Solarian treasury may pay missions. Only ~3 unclaimed systems to cross.
- RESULT t2091660: no contact in 3 lawless systems; lawless belts untouched (homam Fe 17k/Cu 69k; antares Fe/Cu 12k; ice/gas 10k-50k). No Ti/Si found.

## D7 t2091700 — Solarian missions vs ore-delivery missions
- Thinking: Sol board has dock-only exploration missions (infrastructure audit 20,000cr) and ore/refined delivery missions (faction: 2,000 Lead Ore -> 20,000cr; old_charts: 5 circuit_board -> 3,500cr). Delivering ore/refined for credits = selling ore in effect; hard rule forbids it.
- Decision: accept infrastructure audit + old_charts (dock objective free; circuit delivery parked). No ore-delivery missions; raised as Open Question.
- Why: audit costs only jumps that also scout new systems; ore rule respected.
- RESULT t2091929: audit paid 20,000cr IN FULL (Solarian treasury pays; Voidborn does not).

## D8 t2091700 — Titanium source
- Thinking: Sol main_belt lists titanium r25 + nickel r70 but drained (1-2 left). Lawless belts near empires are untouched.
- Decision: look for Ti/Ni in lawless systems bordering Solarian space (tau_ceti, lacaille_9352, acrux, nihal, markab, proxima_centauri, bluerift, gsc_0033).
- Why: same pattern that produced untouched Fe/Cu at homam/antares.

## D9 t2091929 — Five Capitals circuit (15,000cr, Solarian-paid, expires ~t2152400)
- Thinking: docks at Sol(done), Central Nexus, War Citadel(krynn 19j), Grand Exchange(haven 14j), Frontier(mobile_capital, first_step 13j), then back to Sol. ~60+ jumps at 60s each. Haven = Nebula space = silicon + trade_crystal (focused_crystal source) + biggest market.
- Decision: accept; first leg Sol -> Haven scouting every belt and docking at stations (refuel <70%).
- Why: pays reliably, scouts Nebula space for the two biggest crafting blockers, exploration XP per new system. Risk: unknown lawless gaps; starter hull, nothing in cargo.
- RESULT t2092400: Haven reached, 7 lawless systems no contact. Haven board added grand_tour (12k) + federation prospectus (20k, PAID IN FULL t2092456).

## D10 t2092300 — Silver at Nusakan skipped
- Thinking: silver r32 uncommon (18 units, p1) vs iron/copper r41 common at 5/cycle; only 7 cargo free, no station within 2 jumps.
- Decision: skip; return later with empty hold or bigger ship.
- Why: expected 1-2 silver before hold fills; not worth a detour.

## D11 t2092456 — Craft 8 focused crystals at Grand Exchange now
- Thinking: 33 trade_crystal mined at azmidi. focused_crystal is needed for ML II (1), cloak (1), survey_scanner_i (2), shield_booster_ii (2). 192 docked ticks; crafting XP; my docked time is used for memory commits anyway.
- Decision: queue facet_trade_crystal x8 (workshop, free). Outputs stay in storage at grand_exchange_station.
- Why: removes the focused_crystal blocker entirely without buying anything.

## D12 t2092456 — Capitals tour order
- Options computed by BFS: haven>first_step>frontier>nexus_prime>krynn>sol>haven = 84 jumps (best).
- Decision: do it after crafting finishes; stop at nexus_prime to craft lead ingots + check for the new ship; mine cobalt at krynn if live.
- Why: completes five_capitals (15k, return Sol) + grand_tour (12k, return Haven) in one loop.
