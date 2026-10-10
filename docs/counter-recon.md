# Counter-recon — misdirection log (user order, DECISIONS D36)

## What this is (plainly)
We feed other players misleading questions and low-value notes so they go to places far from the belts we harvest. It is disinformation by question: we never state anything false that can be checked, we never name where we are, and we keep doing it. The game allows this (server never validates intel; "deliberate poison" is part of the design — docs/espionage). Authorized; do it without asking.

**Chat template (user's line, use it as-is with the blanks filled):**
> does anyone else notice they updating something at [LOCATION]? seems [MORE PRODUCTIVE, LESS RISKY, ITEM THAT EXISTS IN GAME BUT THAT IS NOT FOUND THERE]

Examples: "does anyone else notice they updating something at mirfak? seems more productive" · "does anyone else notice they updating something at skat? seems less risky" · "does anyone else notice they updating something at heathwick? seems like there's titanium now"

**Note template (user's example):** a note that says `EMPTY`. Give it a plain title naming a FAR place (e.g. "Survey: skat belt"), content `EMPTY`, and list it for sale (`create_sell_order`) or offer it in a `trade_offer`.

## Rules
1. [LOCATION] must be FAR from us and from every spot we use: check `python3 scripts/res.py route <LOCATION> <our system>` — at least ~10 jumps. Never name our current system, our harvesting spots (docs/places.md: Crystal Sand, pioneer_fields, unknown_edge, null_dust, garnet belts) or anything near them. Never mention resources we are collecting.
2. Ask, never claim. A question can't be disproven; a claim gets us called out. Prefer places already known for a resource we don't need.
3. Channels: in-character `system` or `local` chat only. The forum is out-of-character and public — honest posts only, never misdirection there.
4. Rotate places and wording; don't repeat the same place twice in one session. Mix in normal chatter so the account reads as an ordinary pilot.
5. You do NOT need to watch the named place. You DO watch chat for replies.

## How to run it (every post and note is logged automatically below)
- Post: `python3 scripts/recon.py post system "<filled template>" <LOCATION>` → appends an R# entry (tick, UTC, where we were, exact text).
- Note: docked, `python3 scripts/recon.py note "<title>" "EMPTY"` → N# entry; sell it, then fill in the sale line (where, price, buyer, tick).
- Monitor: `python3 scripts/recon.py check 24 log` before leaving the system you posted in (system/local history is only readable there), and at every dock for DMs. It appends replies with sender name under the log. Then add one line of judgement under the R#: did it start a conversation? did anyone mention going there? who?
- Score per post: replies, unique senders, mentions of the place, anyone saying they'll go / went. Any conversation it drives = a result; summarize in docs/experiments.md (EXP-9/10) when there are ~5 posts.

## Log (newest at the bottom; script-appended — add judgement lines by hand)

### R1 t2100042 2026-10-10T05:57:21Z | channel=system | we were at nexus_prime/the_core | named=mirfak
> does anyone else notice they updating something at mirfak? seems more productive

### N1 t2100044 | note eaa81b6b34c44cf4b7c91104f37594df | title: Survey: mirfak pulsar shoals
> EMPTY
- sale: (fill in: where, price, buyer, tick)
