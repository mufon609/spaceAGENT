# spaceAGENT — Alien_Abductee_Gemini memory

Memory for an AI agent playing SpaceMolt. Read THIS first. Keep reads small: only open what the task needs.

## EMERGENCY / SHUTDOWN (do this before the PC turns off, or if anything looks wrong)
```
export SM_USER='Alien_Abductee_Gemini' SM_PASS='<from user>'
scripts/safe_dock.sh          # kill loops -> wait out jump -> flee battle -> nearest known station -> dock -> bank cargo
scripts/safe_dock.sh home     # same, but always fly to central_nexus
```
Exit 0 = docked. Exit 1 = read the SAFE line (usually fuel) and act. Tested S2: loop mid-jump -> docked in ~2.5 min.
No shell? MCP: spacemolt action=get_status -> if in battle spacemolt_battle action=stance id=flee -> jump/travel to nearest station (resources.md) -> dock.

## Session boot (in order)
1. `goals.md` — what to do now + Open Questions. Clear any question the user's message answers.
2. `progression.md` — ship, location, modules, skills, credits, stockpile, active missions.
3. `playbooks.md` — pick a loop, run it. Every loop starts with the Checklist (PB-0).
4. `resources.md` — only when choosing where to go (belt health, crowding, security).
5. `knowledge.md` — only when a mechanic is unclear. Never refetch spacemolt.com/skill.md.
6. `DECISIONS.md` — skim the last 3 entries for context.
7. Login (MCP `spacemolt_auth login`), `sm status`, fix stale lines in progression.md.

## Files
| File | Holds |
|---|---|
| goals.md | Objective stack, strategy phases, Open Questions for User |
| progression.md | Ship/module IDs, location, skills, credits trend, stockpile, missions, gaps |
| playbooks.md | Checklist + copy-paste loops (PB-x) with yields/timings |
| resources.md | Systems table + deposit/belt-health table (crowd, depletion, verdict) + market prices |
| knowledge.md | Mechanics, quirks, worth-mining rules, Skill Guide Summary |
| DECISIONS.md | Every real decision: tick, thinking, choice, why, result |
| scripts/sm.py | Tiny HTTP client, 1-line outputs, preflight, loop, safe (emergency dock; SAFE_STATIONS = known stations in 4 empires) |
| scripts/safe_dock.sh | One-command emergency dock |
| scripts/explore.py | Scout a route of systems; records security/stations/every resource POI; auto-safe |
| scripts/recipe.py | Offline recipe trees from the game catalog (wk/FAC/SHIP tags) |
| scripts/poll.sh | Print only new lines of a background job's log |

## Hard rules (user)
- NEVER sell mined ore or anything made from ore. Stockpile in station storage. Never jettison ore (destroyed).
- CRAFT, DON'T BUY: build modules/upgrades from our own ore (workshop or rented facility). Buy raw materials only if impossible to obtain otherwise. Facility rental fees are fine.
- Lawless space is allowed without asking (user, S2) — know the mechanics first (knowledge.md § Risk).
- Ask user BEFORE: selling valuable non-ore items, scrap/self-destruct, jettison, major purchases.
- Credits < 2,000 with no payout queued: stop, ask user.
- End sessions docked (run safe_dock.sh; PB-8). An undocked idle ship gets towed (~500cr). Never write the password into the repo.
- Log every real choice in DECISIONS.md with the game tick.
- Repo: only mufon609/spaceAGENT branch `Alien_Abductee_Gemini`. No force-push, no file deletes.
- Account is isolated (other fleet accounts exist; user handles them). Do not contact them unless told.

## Commit
Message: `session <date/tick>: <summary>`. After each loop, every ~25 tool calls, before risky actions, at session end.
