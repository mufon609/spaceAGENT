# spaceAGENT — Alien_Abductee_Gemini memory

Memory for an AI agent playing SpaceMolt. Read THIS first. Keep reads small: only open what the task needs.

## Session boot (in order)
1. `goals.md` — what to do now + Open Questions. Clear any question the user's message answers.
2. `progression.md` — ship, modules, skills, credits, stockpile, active missions.
3. `playbooks.md` — pick a loop, run it.
4. `resources.md` — only when choosing where to go (belt health, crowding, security).
5. `knowledge.md` — only when a mechanic is unclear. Never refetch spacemolt.com/skill.md.
6. Login (MCP `spacemolt_auth login`), `sm status`, fix stale lines in progression.md.

## Files
| File | Holds |
|---|---|
| goals.md | Objective stack, strategy phases, Open Questions for User |
| progression.md | Ship/module IDs, skills, credits trend, stockpile, missions, gaps |
| playbooks.md | Copy-paste loops (PB-x) with yields/timings |
| resources.md | Systems table + deposit/belt-health table (crowd, depletion, verdict) |
| knowledge.md | Mechanics, quirks, worth-mining rules, Skill Guide Summary |
| scripts/sm.py | Tiny HTTP client, 1-line outputs. Use it for mutations (MCP replies are ~10k tokens) |

## Hard rules (user)
- NEVER sell mined ore or anything made from ore. Stockpile in station storage.
- Ask user BEFORE: selling valuable non-ore items, scrap/self-destruct, jettison, purchases >~5,000cr, entering lawless/unknown-security space not listed as verified in resources.md.
- Credits < 2,000 with no payout queued: stop, ask user.
- End sessions docked. Never write the password into the repo.
- Repo: only mufon609/spaceAGENT branch `Alien_Abductee_Gemini`. No force-push, no file deletes.
- Account is isolated (other fleet accounts exist; user handles them). Do not contact them unless told.

## Commit
Message: `session <date/tick>: <summary>`. After each loop, every ~25 tool calls, before risky actions, at session end.
