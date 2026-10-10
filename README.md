# spaceAGENT — memory of SpaceMolt pilot Alien_Abductee_Gemini (read THIS first)

One isolated account, one cheap agent, as long and as far as possible. Identity: Voidborn ghost prospector — stealth, scanning, information as a weapon (docs/strategy.md). The game patches constantly: **notes are evidence, not truth** — check the version line from boot.py and verify anything that matters live before betting on it.

## EMERGENCY / SHUTDOWN
```
scripts/safe_dock.sh     # kill all jobs -> wait out jump -> flee battle -> nearest known station -> dock -> bank cargo
```
Exit 0 = docked. Exit 1 = read the SAFE line (usually fuel / action_in_progress: rerun). An undocked ship whose session idles gets towed (~500cr).

## Boot (≈3 calls)
1. `export SM_USER=Alien_Abductee_Gemini SM_PASS=<from user>`; `python3 scripts/boot.py` (tick, VERSION check, status, skills, modules, missions, ships, tax top-up, stock snapshot, preflight).
2. Read `STATE.md` (state + Now + Open Questions) and the top 3 entries of `DECISIONS.md`.
3. VERSION CHANGED? Read the changelog (`python3 scripts/sm.py call spacemolt get_version`), fix affected notes, bump `game_version` in STATE.md.
4. Undocked with no job running → `scripts/safe_dock.sh` first.

## Hard rules (user)
- **Market:** NEVER sell mined ore or anything made from ore (stockpile in station storage). BUY a module/upgrade (never a ship) only when its price is below the raw-resource cost of crafting it; log the comparison in DECISIONS.md. No other market buying (no market-participation missions); station refuel/repair services are fine. The point: learn the game by mining + crafting. Allowed income: mission rewards, freight, passengers, bounties, rescues, salvage (`sell_wreck` at an NPC salvage yard), and **selling information** (notes, intel). Misdirection is authorized standing policy: docs/counter-recon.md (never reveal our location or nearby spots; ask, never claim; forum stays honest).
- **Taxes always prepaid:** boot.py runs `sm.py tax` (tops the prepay pool up to owed + 10%, pays any tax bounty). Never let a tax debt form.
- **Nomadic:** no ongoing costs — never own, build or lease facilities, outposts or bases; per-run rental fees are fine. Home base is only the respawn point.
- **Stockpile tracking:** `sm.py stock` (auto at boot) writes data/stock.tsv for every station. Consolidate at central_nexus (Voidborn shipyard) when trips pass by; don't scatter, don't waste trips hauling.
- **Jettison** only iron/copper filler while mining a rarer ore (jettisoned ore is destroyed). Nothing else.
- **Ask first:** selling valuable non-ore items, scrapping/buying a ship, self-destruct, other irreversible commitments. Credits < 2,000 with no payout queued → stop and ask.
- **Isolated account:** no contact, gifts or coordination with other fleet accounts unless the user says so. Execute a user order exactly ONCE even if the message is re-sent.
- **Secrets:** password only in env vars SM_USER/SM_PASS. Never in a file, commit or log. Never register an account.
- **Repo:** only github.com/mufon609/spaceAGENT, branch `main`. Create/edit/move/delete files freely; keep it small. No force-push, no new repos/branches, no settings changes.
- Take chances: lawless space, cloaked runs, new mechanics are encouraged; a T1 hull is rebuildable from stock. Bank valuables first, leave a POI on pirates, log risks and sightings.

## Files
| File | Holds | Read |
|---|---|---|
| STATE.md | volatile: ship, fit, location, skills, credits, stock per station, missions, Now, Open Questions | every boot |
| DECISIONS.md | decisions ONLY, newest first (D#, t<tick>, RESULT) — be decisive, don't ask about what's already permitted | top 3 at boot |
| docs/counter-recon.md | misdirection playbook (user's chat template, EMPTY notes) + running log of posts, notes and replies | before posting/selling |
| docs/experiments.md | ranked hypotheses to test + results | when choosing what to do |
| docs/playbooks.md | PB-0..PB-10 step sequences, job launch pattern | when running a loop |
| docs/game.md | mechanics verified in play, rates, quirks, harness | when a mechanic is unclear |
| docs/places.md | ore locations, routes, stations, market reference | when choosing where to go |
| docs/strategy.md | long plan, ship ladder, build bills vs stock | when planning |
| docs/reference.md | condensed official docs/guides/changelog (v0.613.4) | for a mechanic never used yet |
| data/systems.tsv, data/belts.tsv | machine-readable systems + belts (query with res.py, never cat) | via scripts |
| data/stock.tsv | every station's storage (sm.py stock; regenerated at boot) | grep it |
| scripts/ | sm.py (client, loop, safe, train), boot.py, res.py, recipe.py, explore.py, stackmine.py, recon.py (counter-recon post/note/check), safe_dock.sh, poll.sh | — |
| archive/ | old decision log D1–D22 | rarely |
| PROMPT.md | the agent's system prompt (user pastes it into the console) | never at boot |

## Cheap lookups (never cat big files)
- Where/route: `python3 scripts/res.py ore <name> | sys <id> | route A B | near <sys> [n] | grep <txt>` (route uses the full public map).
- Recipes/items/ships: `python3 scripts/recipe.py tree <item> [n] | <item> | uses <item> | item <item>` (catalog cached in /tmp; `-f` after a version change).
- Live game: `python3 scripts/sm.py status | scout | missions | active | storage [station] | call <tool> <action> '{json}'`.
