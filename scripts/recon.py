#!/usr/bin/env python3
"""recon.py - counter-recon: post misdirection, sell notes, and record every reply in docs/counter-recon.md.
  recon.py post <system|local> "<text>" [named_place]  send chat + append an R# entry (tick, utc, where we were, exact text)
  recon.py note "<title>" "<content>"                 create a note (docked, 1 cargo) + append an N# entry; sell it yourself
                                                     (create_sell_order / trade_offer) and add price/buyer to the entry
  recon.py check [hours=24] [log]                     print chat since our posts: system/local of the CURRENT system + all DMs;
                                                     'log' appends new replies to the file (skips ones already recorded)
System/local chat history is only readable while you are in that system: run `check` before leaving. DMs work anywhere.
Needs SM_USER/SM_PASS. Imports sm.py."""
import json, os, re, sys, time, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sm import call, sc, short

F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", "counter-recon.md")


def tick():
    try:
        return json.loads(urllib.request.urlopen("https://game.spacemolt.com/health", timeout=8).read().decode()).get("tick")
    except Exception:
        return "?"


def where():
    lo = sc(call("spacemolt", "get_status")).get("location", {})
    return lo.get("system_id", "?"), lo.get("poi_id", "?")


def nxt(prefix):
    n = [int(x) for x in re.findall(r"^### %s(\d+) " % prefix, open(F).read(), re.M)]
    return max(n or [0]) + 1


def append(text):
    with open(F, "a") as f:
        f.write(text)


def msgs(r):
    s = sc(r)
    m = s.get("messages") if isinstance(s, dict) else None
    return m if isinstance(m, list) else (s if isinstance(s, list) else [])


def field(m, *keys):
    for k in keys:
        if m.get(k):
            return str(m[k])
    return "?"


def post(channel, text, place="-"):
    t, utc = tick(), time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    sysid, poi = where()
    r = call("spacemolt_social", "chat", {"channel": channel, "content": text})
    if "error" in r:
        print(short(r)); return
    n = nxt("R")
    append("\n### R%d t%s %s | channel=%s | we were at %s/%s | named=%s\n> %s\n" % (n, t, utc, channel, sysid, poi, place, text))
    print("posted R%d in %s %s" % (n, channel, sysid))


def note(title, content):
    r = call("spacemolt_social", "create_note", {"title": title, "content": content})
    if "error" in r:
        print(short(r)); return
    s = sc(r); nid = s.get("note_id") or (s.get("note") or {}).get("id") or "?"
    n = nxt("N")
    append("\n### N%d t%s | note %s | title: %s\n> %s\n- sale: (fill in: where, price, buyer, tick)\n" % (n, tick(), nid, title, content[:300]))
    print("note N%d id=%s" % (n, nid))


def check(hours=24.0, log=False):
    since = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(time.time() - hours * 3600))
    body = open(F).read()
    posts = re.findall(r"^### (R\d+) t\S+ (\S+) \| channel=(\w+) \| we were at (\w+)/", body, re.M)
    posts = [p for p in posts if p[1] >= since]
    if not posts:
        print("no posts in the last %sh" % hours); return
    first = min(p[1] for p in posts)
    here, _ = where()
    new = []
    for ch in ("system", "local", "private"):
        if ch != "private" and not any(p[2] == ch and p[3] == here for p in posts):
            continue
        for m in msgs(call("spacemolt_social", "get_chat_history", {"channel": ch, "limit": 100, "after": first})):
            who, ts, txt = field(m, "sender_name", "sender", "username", "from", "player_name"), \
                field(m, "timestamp_utc", "timestamp", "created_at"), field(m, "content", "message", "text")
            if who == os.environ.get("SM_USER"):
                continue
            ref = ([p[0] for p in posts if p[1] <= ts and (ch == "private" or p[2] == ch)] or ["R?"])[-1]
            line = "- reply %s %s [%s] %s: %s" % (ref, ts, ch, who, txt.replace("\n", " ")[:300])
            print(line)
            if txt[:80] not in body:
                body += txt[:80]  # also dedupes within this run
                new.append(line)
    if log and new:
        append("\n" + "\n".join(new) + "\n")
        print("logged %d new replies" % len(new))


def main(a):
    if not a:
        print(__doc__)
    elif a[0] == "post" and len(a) >= 3:
        post(a[1], a[2], a[3] if len(a) > 3 else "-")
    elif a[0] == "note" and len(a) >= 3:
        note(a[1], a[2])
    elif a[0] == "check":
        check(float(a[1]) if len(a) > 1 and a[1] != "log" else 24.0, "log" in a)
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
