#!/usr/bin/env python3
"""res.py - query the repo's resource/system knowledge WITHOUT reading big files (token saver).
  res.py ore <name>        belts listing that ore (name substring, e.g. silicon, titanium, gold), richest first
  res.py sys <id>          system row: empire, police, stations, links + its belts
  res.py route <A> <B>     shortest jump path over known links (data/systems.tsv)
  res.py near <sys> [n=3]  systems within n jumps (with empire/police/stations)
  res.py grep <text>       any belt/system row containing text
Data: data/systems.tsv (id, empire, police, stations, links) and data/belts.tsv (system, poi, police, equip, players, last_seen, verdict).
explore.py upserts both files as it scouts (commit them at checkpoints)."""
import os, re, sys
from collections import deque
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")

def rows(name):
    out = []
    for l in open(os.path.join(D, name)):
        if l.startswith("#") or not l.strip():
            continue
        out.append(l.rstrip("\n").split("\t"))
    return out

S = {r[0]: r for r in rows("systems.tsv")}
B = rows("belts.tsv")

def links(s):
    return [x for x in S.get(s, ["", "", "", "", ""])[4].split(",") if x]

def main(a):
    if not a:
        print(__doc__); return
    c = a[0]
    if c == "ore":
        q = a[1].lower(); hits = []
        for b in B:
            m = re.findall(r"(%s\w*) r(\d+)/(\d+)(?:/p(\d+))?" % re.escape(q), b[5])
            for name, r, rem, p in m:
                hits.append((int(rem), b[0], b[1], name, r, p, b[2], b[6]))
        for rem, s, poi, name, r, p, pol, v in sorted(hits, reverse=True)[:15]:
            print("%s/%s %s r%s rem=%s p%s police=%s | %s" % (s, poi, name, r, rem, p, pol, v[:60]))
        if not hits: print("no belt row mentions", q)
    elif c == "sys":
        r = S.get(a[1])
        print("\t".join(r) if r else "unknown system")
        for b in B:
            if b[0] == a[1]: print(" ", b[1], "|", b[5][:200], "|", b[6][:50])
    elif c == "route":
        src, dst = a[1], a[2]; prev = {src: None}; q = deque([src])
        while q:
            u = q.popleft()
            if u == dst: break
            for v in links(u):
                if v not in prev: prev[v] = u; q.append(v)
        if dst not in prev: print("no known path (links only exist for visited systems)"); return
        p = []; u = dst
        while u: p.append(u); u = prev[u]
        p.reverse(); print(len(p) - 1, "jumps:", ">".join(p))
    elif c == "near":
        n = int(a[2]) if len(a) > 2 else 3; seen = {a[1]: 0}; q = deque([a[1]])
        while q:
            u = q.popleft()
            if seen[u] >= n: continue
            for v in links(u):
                if v not in seen: seen[v] = seen[u] + 1; q.append(v)
        for s, d in sorted(seen.items(), key=lambda x: x[1]):
            r = S.get(s)
            if r: print(d, s, r[1], "police", r[2], "stations", r[3])
    elif c == "grep":
        for r in list(S.values()) + B:
            if a[1].lower() in "\t".join(r).lower(): print("\t".join(r)[:300])

main(sys.argv[1:])
