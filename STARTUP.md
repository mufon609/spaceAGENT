# STARTUP — session kickoff prompt

Copy everything inside the box into the first message of a new session. Paste the credentials JSON where marked.
NEVER commit the filled-in version (the password must not enter the repo).

```
New SpaceMolt session. Credentials (do not write these to any file or commit):
<PASTE CREDENTIALS JSON HERE>

Boot sequence:
1. Read from github.com/mufon609/spaceAGENT branch Alien_Abductee_Gemini: README.md, goals.md, progression.md, last 3 entries of DECISIONS.md. Read playbooks.md / resources.md / knowledge.md only when needed. Mirror files to /tmp/spaceAGENT via raw.githubusercontent.com curl; clone scripts/ there too.
2. Get the game tick: curl -s https://game.spacemolt.com/health. Stamp all notes/decisions with t<tick>.
3. Log in (MCP spacemolt_auth login). For scripts: export SM_USER / SM_PASS from the credentials (env only).
4. Run: python3 scripts/sm.py status ; sm.py active ; sm.py preflight. Check list_ships for the new ship (Resonance Miner: needs Piloting 10 + min crew 3). Fix stale lines in progression.md.
5. If the ship is undocked with no job running: scripts/safe_dock.sh first.
6. Clear any Open Question in goals.md that my message answers. My answers this session: <optional: Q4/Q5 answers or new orders>
7. Tell me in 3-5 lines: location, credits, top goal, plan for this session. Then play.

Rules reminder: stockpile ore (never sell), craft don't buy, lawless OK (know the risks), log real decisions in DECISIONS.md, commit every ~25 tool calls / after each loop, background jobs via setsid + poll.sh (tool calls <=60s waiting), end docked via scripts/safe_dock.sh (PB-8) and update progression.md + goals.md before closing.
```

## Close-out phrase (send when you want the agent to stop)
```
Close out: run scripts/safe_dock.sh, confirm docked, update progression.md, goals.md, DECISIONS.md (+ resources/knowledge if changed), commit, add a captain's log entry, then report.
```
