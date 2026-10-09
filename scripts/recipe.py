#!/usr/bin/env python3
"""recipe.py - offline recipe/item lookup from the game catalog. Stdlib only.

Downloads https://game.spacemolt.com/api/catalog.json once to /tmp/catalog.json (refetch with -f).
Usage:
  recipe.py <item_id>              all recipes that make it (wk = hand-craftable at any Station Workshop)
  recipe.py tree <item_id> [n]     cheapest hand-craftable tree, n units -> raw leaf materials
  recipe.py uses <item_id>         recipes that consume it
  recipe.py item <item_id>         item stats (slot, cpu, power, required_skills, base_value)
  recipe.py -f ...                 force catalog refresh (after a game version change)
Leaves = items with no hand-craftable recipe (ores, salvage, creature parts...).
Tags: wk = Station Workshop (free, docked) | FAC = needs a production facility (own/faction/rented) | SHIP = onboard_*, runs automatically only on hulls with that built-in capability.
"""
import json, os, sys, urllib.request

CAT = "/tmp/catalog.json"


def load(force=False):
    if force or not os.path.exists(CAT):
        urllib.request.urlretrieve("https://game.spacemolt.com/api/catalog.json", CAT)
    c = json.load(open(CAT))
    rl = c["recipes"] if isinstance(c["recipes"], list) else list(c["recipes"].values())
    il = c["items"] if isinstance(c["items"], list) else list(c["items"].values())
    return rl, {i["id"]: i for i in il}


def hand(r):
    """Workshop-craftable. onboard_* recipes only run automatically on ships with that capability."""
    return bool(r.get("hand_craftable")) and not r["id"].startswith("onboard_")


def fmt(r):
    tag = "wk " if hand(r) else ("SHIP" if r["id"].startswith("onboard_") else "FAC")
    return "%s %-34s t%-6s %s -> %s" % (tag, r["id"], r.get("crafting_time"),
        " + ".join("%sx%s" % (i["quantity"], i["item_id"]) for i in r["inputs"]),
        " + ".join("%sx%s" % (o["quantity"], o["item_id"]) for o in r["outputs"]))


def makers(rl, item):
    return [r for r in rl if any(o["item_id"] == item for o in r["outputs"])]


def best(rl, item):
    """Pick a hand-craftable recipe with the fewest distinct inputs, then most output."""
    c = [r for r in makers(rl, item) if hand(r)]
    if not c:
        return None
    return min(c, key=lambda r: (len(r["inputs"]), -sum(o["quantity"] for o in r["outputs"] if o["item_id"] == item)))


def tree(rl, item, qty, depth=0, leaves=None, seen=()):
    leaves = {} if leaves is None else leaves
    r = best(rl, item) if item not in seen else None
    if r is None or depth > 8:
        leaves[item] = leaves.get(item, 0) + qty
        print("  " * depth + "%s x%s  [raw/leaf]" % (item, qty))
        return leaves
    out = sum(o["quantity"] for o in r["outputs"] if o["item_id"] == item)
    runs = -(-qty // out)
    print("  " * depth + "%s x%s  <- %s x%d runs" % (item, qty, r["id"], runs))
    for i in r["inputs"]:
        tree(rl, i["item_id"], i["quantity"] * runs, depth + 1, leaves, seen + (item,))
    return leaves


def main(a):
    force = "-f" in a
    a = [x for x in a if x != "-f"]
    if not a:
        print(__doc__)
        return
    rl, items = load(force)
    if a[0] == "tree":
        leaves = tree(rl, a[1], int(a[2]) if len(a) > 2 else 1)
        print("RAW TOTAL: " + ", ".join("%s %s" % (k, v) for k, v in sorted(leaves.items())))
    elif a[0] == "uses":
        for r in rl:
            if any(i["item_id"] == a[1] for i in r["inputs"]):
                print(fmt(r))
    elif a[0] == "item":
        i = items.get(a[1])
        print(json.dumps({k: v for k, v in (i or {}).items() if k != "description"}) if i else "unknown item")
    else:
        for r in makers(rl, a[0]):
            print(fmt(r))


if __name__ == "__main__":
    main(sys.argv[1:])
