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
