# spaceAGENT — Alien_Abductee_Gemini memory

Persistent memory for an AI agent playing SpaceMolt (spacemolt.com). Read THIS file first, every session.

## Session boot (do in order)
1. Read `goals.md` (what to do + Open Questions). Resolve any question the user's message already answers; delete it.
2. Read `progression.md` (ship, modules, skills, credits) and `playbooks.md` (copy-paste loops).
3. Read `knowledge.md` only for the sections you need (mechanics, quirks, guide summary). Do NOT refetch spacemolt.com/skill.md.
4. Use `resources.md` when choosing where to mine/travel.
5. Login (MCP `spacemolt_auth login`) and run `get_status`. Compare against progression.md; fix stale lines.
6. Pick ONE objective from goals.md and execute a playbook.

## File map
| File | Holds | Update when |
|---|---|---|
| goals.md | Priority stack, active missions, Open Questions for User | objective done/changed |
| progression.md | Ship/module IDs, skills, credits trend, stockpile, gaps | each session + after purchases |
| playbooks.md | Exact repeatable loops (PB-x) | loop verified/changed |
| resources.md | Systems table + deposits table | every POI visited |
| knowledge.md | Mechanics, quirks, Skill Guide Summary | new mechanic learned |
| scripts/sm.py | Tiny HTTP client: compact output, saves tokens | when API changes |

## Hard rules (from user; never break)
- NEVER sell mined ore or anything refined/crafted from ore. Stockpile in station storage.
- Ask user BEFORE: selling non-ore items of value, scrapping/self-destruct, jettison, major purchases (>~5,000cr), entering unverified lawless/unknown-security space.
- If credits < 2,000 and no mission payout queued: stop and ask user.
- Mission rewards = allowed income.
- End every session docked at a station.
- Only touch repo mufon609/spaceAGENT branch `Alien_Abductee_Gemini`. Never force-push, never delete files.
- Never put the password in any repo file.

## Commit convention
`session <date or tick>: <one-line summary>`. Commit after each resource loop, every ~25 tool calls, before risky actions, at session end.

## Writing style for memory files
Short, factual, exact IDs/numbers. Replace stale lines in place. No narrative.
