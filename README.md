# spaceAGENT — Alien_Abductee_Gemini memory (read THIS first; keep reads small)

Memory for an AI agent playing SpaceMolt. Proposed session prompt: `STARTUP.md`. Strategy: `GAME-PLAN.md`.

## EMERGENCY / SHUTDOWN
```
export SM_USER='Alien_Abductee_Gemini' SM_PASS='<from user>'
scripts/safe_dock.sh          # kill loops -> wait out jump -> flee battle -> nearest known station -> dock -> bank cargo
```
Exit 0 = docked. Exit 1 = read the SAFE line (usually fuel / action_in_progress: retry). An undocked idle ship gets towed (~500cr). Tool crashes can kill background jobs: check `pgrep -f "explore.py|stackmine|sm.py loop"` and `sm.py status`.

## Session boot (cheap)
1. `python3 scripts/boot.py` = tick + status + skills + modules + missions + ships + preflight (one command).
2. Read goals.md (Now + Open Questions) and progression.md (state). Last entries of DECISIONS.md.
3. Where to go / what is where: `python3 scripts/res.py ore <name> | sys <id> | route A B | near <sys> | grep <txt>` (reads data/*.tsv + *_new.tsv overlays; do NOT cat big files).
4. playbooks.md (PB-0 preflight + PB-1..10 loops), knowledge.md (mechanics, measured rates), GAME-PLAN.md (strategy + Resonance bill vs stock) only when needed.

## Files
| File | Holds |
|---|---|
| STARTUP.md | proposed agent prompt + efficiency lessons |
| GAME-PLAN.md | user's strategy + S3 status (Resonance Miner bill of materials vs stock) |
| goals.md | priority stack, user orders, Open Questions |
| progression.md | volatile state: ship, location, skills, credits, stock per station, missions |
| playbooks.md | PB-0..PB-10 loops (stackmine, dock loop, refining training, missions, close-out) |
| knowledge.md | mechanics + play-only facts (XP rules, rates, crafting, market, missions, harness) |
| resources.md | index: material locations, ROUTES, STATIONS, market refs |
| data/systems.tsv, data/belts.tsv (+ systems_new.tsv, belts_new.tsv overlays) | machine-readable systems + belts; explore.py upserts overlays, res.py queries |
| DECISIONS.md | recent decisions D23+ (older in archive/DECISIONS_old.md) |
| scripts/ | sm.py (client/loop/safe/train), boot.py, res.py, explore.py, stackmine.py, recipe.py, safe_dock.sh, poll.sh |

## Hard rules (user; see goals.md for updates)
- NEVER sell mined ore or anything made from ore; stockpile in station storage. Jettison ONLY iron/copper filler while mining rare ore (approved). Never write the password anywhere.
- Stack rare/blocker ores (silicon, titanium, nickel, iridium, null matter). BUY a module (not ships) if cheaper than crafting from raw; log it.
- Lawless space OK. Ask before: selling valuable non-ore items, scrapping/buying ships, self-destruct, other irreversible acts. Credits < 2,000 with no payout queued: stop and ask.
- Account is isolated: no contact with other fleet accounts unless the user says so (hand-off to Alien_Hauler-Opus55 when the user triggers it at Piloting 10). Execute a user gift/order once.
- Repo: only mufon609/spaceAGENT branch Alien_Abductee_Gemini. User allows creating/editing/deleting files here (S3); no force-push, no new branches/repos.
- End sessions docked (safe_dock.sh, PB-8), update progression/goals/DECISIONS, push changed files only. Commit message `session <date> t<tick>: <summary>`.
