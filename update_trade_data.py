"""Weekly Trade Analyzer data refresh.

Rewrites ROSTERS_2026, PLAYER_STATS_2026 and PLAYER_STATS_2026_THROUGH_WEEK in
data.py from two scraped text files, and adds any brand-new rostered players to
TRADE_VALUES_2026 (their preseason value). build.py then turns preseason values +
season production into live trade values (see live_trade_values()).

Usage:
    python3 update_trade_data.py ROSTERS_TXT STATS_TXT THROUGH_WEEK [--dry-run]

ROSTERS_TXT (one block per team, from each team's Yahoo roster page):
    ##Team Name
    Player|POS;Player|POS|STATUS;...

STATS_TXT (one line per player, from Yahoo's Players page, Season stats):
    POS~Player~R~games_played~season_fantasy_points      (R = rostered, blank = FA)

Exits non-zero (and changes nothing) if anything looks wrong.
"""
import re
import sys

import data as D

POSITIONS = {"QB", "RB", "WR", "TE", "DEF", "K"}


def fail(msg):
    print("ERROR:", msg)
    sys.exit(1)


def parse_rosters(path):
    rosters, cur = {}, None
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("##"):
            cur = line[2:].strip()
            rosters[cur] = []
            continue
        if cur is None:
            fail("roster file has players before the first ##Team line")
        for item in line.split(";"):
            parts = (item.split("|") + ["", ""])[:3]
            name, pos, status = (p.strip() for p in parts)
            if not name or pos not in POSITIONS:
                fail(f"bad roster entry for {cur}: {item!r}")
            rosters[cur].append((name, pos, status))
    return rosters


def parse_stats(path):
    stats = {}
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line:
            continue
        parts = line.split("~")
        if len(parts) != 5 or parts[0] not in POSITIONS:
            fail(f"bad stats line: {line!r}")
        pos, name, _rostered, gp, pts = parts
        stats[name] = (pos, int(float(gp or 0)), float(pts or 0))
    return stats


def main():
    if len(sys.argv) < 4:
        fail(__doc__)
    rosters = parse_rosters(sys.argv[1])
    stats = parse_stats(sys.argv[2])
    week = int(sys.argv[3])
    dry = "--dry-run" in sys.argv

    # --- sanity checks -------------------------------------------------
    if len(rosters) != 12:
        fail(f"expected 12 teams, got {len(rosters)}: {list(rosters)}")
    unknown = [t for t in rosters if t not in D.MANAGERS]
    if unknown:
        fail(f"team name(s) not in data.MANAGERS (renamed on Yahoo?): {unknown} -- "
             "stop and ask Turab before renaming anything")
    for t, ps in rosters.items():
        if not 12 <= len(ps) <= 20:
            fail(f"{t} has {len(ps)} players -- roster scrape looks incomplete")
    names = [n for ps in rosters.values() for n, _, _ in ps]
    dupes = {n for n in names if names.count(n) > 1}
    if dupes:
        fail(f"players on more than one roster: {sorted(dupes)}")
    for pos, minimum in {"QB": 30, "RB": 40, "WR": 60, "TE": 20, "DEF": 20}.items():
        n = sum(1 for p, _, _ in stats.values() if p == pos)
        if n < minimum:
            fail(f"only {n} {pos} rows in stats file (need {minimum}+ to set replacement level)")
    if week < D.PLAYER_STATS_2026_THROUGH_WEEK:
        fail(f"stats week {week} is older than what's already stored ({D.PLAYER_STATS_2026_THROUGH_WEEK})")

    # keep the existing dropdown order; new team names were rejected above
    order = [t for t in D.ROSTERS_2026 if t in rosters] + [t for t in rosters if t not in D.ROSTERS_2026]

    # --- new players get a preseason value ----------------------------
    rank = {n: r for r, n in D.YAHOO_RANKINGS_2026}
    pre = dict(D.TRADE_VALUES_2026)
    pos_of = {n: p for ps in rosters.values() for n, p, _ in ps}
    added = []
    for t in order:
        for name, pos, _ in rosters[t]:
            if name in pre:
                continue
            value = 0.5  # unranked in-season pickup: replacement-level preseason prior
            if name in rank:
                cands = [(abs(rank[m] - rank[name]), m) for m in pre
                         if m in rank and (pos_of.get(m) or D.PLAYER_POSITIONS.get(m)) == pos]
                if cands:
                    value = pre[min(cands)[1]][0]
            pre[name] = (value, False, False)
            added.append((name, pos, t, value))

    # --- render data.py blocks ----------------------------------------
    src = open("data.py", encoding="utf-8").read()

    def replace_block(src, start, end, new_body):
        i = src.index(start)
        j = src.index(end, i) + len(end)
        return src[:i] + new_body + src[j:]

    r = ["ROSTERS_2026 = {"]
    for t in order:
        r.append(f"    {t!r}: [")
        r += [f"        ({n!r}, {p!r}, {s!r})," for n, p, s in rosters[t]]
        r.append("    ],")
    r.append("}\n")
    src = replace_block(src, "ROSTERS_2026 = {", "\n}\n", "\n".join(r))

    s = [f"PLAYER_STATS_2026_THROUGH_WEEK = {week}", "PLAYER_STATS_2026 = {"]
    s += [f"    {n!r}: ({p!r}, {g}, {pts})," for n, (p, g, pts) in stats.items()]
    s.append("}\n")
    src = replace_block(src, "PLAYER_STATS_2026_THROUGH_WEEK = ", "\n}\n", "\n".join(s))

    if added:
        extra = "".join(f"    {n!r}: ({v}, False, False),\n" for n, _, _, v in added)
        i = src.index("TRADE_VALUES_2026 = {")
        j = src.index("\n}\n", i) + 1
        src = src[:j] + extra + src[j:]

    src = re.sub(r"(Pulled )\d{4}-\d{2}-\d{2}(, through Week )\d+",
                 lambda m: m.group(1) + __import__("datetime").date.today().isoformat() + m.group(2) + str(week),
                 src, count=1)

    print(f"teams: {len(order)}  rostered players: {len(names)}  stat rows: {len(stats)}  through week {week}")
    print(f"new players added to TRADE_VALUES_2026: {len(added)}")
    for n, p, t, v in added:
        print(f"  + {n} ({p}, {t}) preseason {v}")
    if dry:
        print("dry run -- data.py not written")
        return
    open("data.py", "w", encoding="utf-8").write(src)
    print("data.py updated")


if __name__ == "__main__":
    main()
