# -*- coding: utf-8 -*-
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import data as D

OUT = os.path.dirname(__file__)

NAV_ITEMS = [
    ("index.html", "Home"),
    ("standings.html", "Standings"),
    ("scores.html", "Weekly Scores"),
    ("power-rankings.html", "Power Rankings"),
    ("history.html", "History & Records"),
    ("managers.html", "Managers"),
    ("records.html", "All-Time Records"),
    ("rivalries.html", "Rivalries"),
    ("draft-central.html", "Draft Central"),
    ("draft.html", "Draft Recap"),
    ("keepers.html", "Keepers"),
    ("trades.html", "Trade Newsletter"),
    ("trade-analyzer.html", "Trade Analyzer"),
    ("trash-talk.html", "Trash Talk"),
    ("futures.html", "Futures & Ballot"),
    ("rules.html", "Rules"),
    ("recap.html", "Newsletter"),
]

def nav_html(active):
    links = []
    for href, label in NAV_ITEMS:
        cls = "nav-link active" if href == active else "nav-link"
        links.append(f'<a class="{cls}" href="{href}">{label}</a>')
    return f'''
<header class="site-header">
  <div class="header-inner">
    <a class="brand" href="index.html">
      <span class="brand-mark">LB</span>
      <span class="brand-text">LOW BALLERZ<small>Fantasy Football League &middot; Est. 2008</small></span>
    </a>
    <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">&#9776;</button>
    <nav class="site-nav" id="siteNav">
      {''.join(links)}
    </nav>
  </div>
</header>
'''

def footer_html():
    return '''
<footer class="site-footer">
  <div class="footer-inner">
    <div>
      <span class="brand-mark small">LB</span>
      <strong>Low Ballerz</strong> &middot; Yahoo Fantasy Football League #40967
    </div>
    <div class="footer-links">
      <span>18 seasons strong since 2008</span>
      <span>&middot;</span>
      <span>Built for the league, by the league</span>
    </div>
  </div>
</footer>
'''

SITE_URL = "https://lowballerz.scypherapps.com"

def page(title, active, body, description=""):
    page_title = f"{title} | Low Ballerz"
    desc = description or "Official site of the Low Ballerz fantasy football league — standings, scores, history, draft grades and more."
    canonical = f"{SITE_URL}/{active}" if active != "index.html" else f"{SITE_URL}/"
    og_image = f"{SITE_URL}/assets/og-image.png"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Low Ballerz">
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{page_title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{og_image}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body>
{nav_html(active)}
<main>
{body}
</main>
{footer_html()}
<script src="script.js"></script>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "5cf27d3ed846468badc8a27605ce585f"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
'''

def money(n):
    return f"${n}"

def fmt_score(v):
    return f"{v:.2f}" if v is not None else "—"

def team_pill(team):
    mgr = D.MANAGERS.get(team, "")
    return f'<span class="team-pill">{team}<small>{mgr}</small></span>'

def ordinal(n):
    if 10 <= n % 100 <= 20:
        suf = "th"
    else:
        suf = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suf}"

def parse_record(rec):
    parts = rec.split("-")
    w, l = int(parts[0]), int(parts[1])
    t = int(parts[2]) if len(parts) > 2 else 0
    return w, l, t

def initials(name):
    words = [w for w in name.replace("(", " ").replace(")", " ").split() if w[:1].isalpha()]
    return "".join(w[0].upper() for w in words[:2]) or "?"

def mgr_slug(name):
    """Stable URL-safe id for a manager name, e.g. 'wajahat z' -> 'wajahat-z'."""
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

STANDINGS_BY_TEAM_2025 = {row[1]: row for row in D.STANDINGS_2025}

def compute_manager_career(mgr):
    team = D.CURRENT_TEAM_BY_MANAGER.get(mgr)
    champ_years = sorted([y for y, (t, m, c) in D.CHAMPIONS_BY_MANAGER.items() if m == mgr], reverse=True)
    podiums = [(y, p) for y, p, t, m in D.PODIUM_FINISHES if m == mgr]
    p1 = sum(1 for y, p in podiums if p == 1)
    p2 = sum(1 for y, p in podiums if p == 2)
    p3 = sum(1 for y, p in podiums if p == 3)
    row = STANDINGS_BY_TEAM_2025.get(team)
    career = D.CAREER_RECORDS.get(mgr, {"W": 0, "L": 0, "T": 0, "seasons": 0, "first_year": None, "last_year": None})
    games = career["W"] + career["L"] + career["T"]
    win_pct = career["W"] / games if games else 0.0
    return {
        "mgr": mgr, "team": team, "champ_years": champ_years, "titles": len(champ_years),
        "p1": p1, "p2": p2, "p3": p3, "podiums_total": p1 + p2 + p3,
        "row2025": row,
        "career_w": career["W"], "career_l": career["L"], "career_t": career["T"],
        "career_seasons": career["seasons"], "career_first_year": career["first_year"],
        "career_win_pct": win_pct,
    }

def manager_bio(c):
    parts = []
    if c["career_seasons"]:
        career_rec = f'{c["career_w"]}-{c["career_l"]}' + (f'-{c["career_t"]}' if c["career_t"] else "")
        parts.append(f'Career record: {career_rec} ({c["career_win_pct"]*100:.1f}%) across {c["career_seasons"]} seasons since {c["career_first_year"]}.')
    if c["titles"]:
        yrs = ", ".join(str(y) for y in c["champ_years"])
        parts.append(f'{c["titles"]}x champion ({yrs}).')
    else:
        parts.append("No championships yet.")
    if c["podiums_total"]:
        parts.append(f'{c["podiums_total"]} career podium finish{"es" if c["podiums_total"] != 1 else ""} since 2011 ({c["p1"]}x 1st, {c["p2"]}x 2nd, {c["p3"]}x 3rd).')
    if c["row2025"]:
        rank, _team, rec, pf, pa, wv, mv = c["row2025"]
        parts.append(f'Finished {ordinal(rank)} in 2025 at {rec}.')
    return " ".join(parts)

def compute_h2h_2025():
    mgrs = list(D.CURRENT_TEAM_BY_MANAGER.keys())
    h2h = {m: {n: [0, 0] for n in mgrs if n != m} for m in mgrs}
    for w, games in D.WEEKLY_SCORES_2025.items():
        for a, sa, b, sb in games:
            ma, mb = D.MANAGERS.get(a), D.MANAGERS.get(b)
            if ma not in h2h or mb not in h2h:
                continue
            if sa > sb:
                h2h[ma][mb][0] += 1
                h2h[mb][ma][1] += 1
            else:
                h2h[mb][ma][0] += 1
                h2h[ma][mb][1] += 1
    return h2h, mgrs

def compute_h2h_alltime():
    mgrs = list(D.CURRENT_TEAM_BY_MANAGER.keys())
    h2h = {m: {n: [0, 0, 0] for n in mgrs if n != m} for m in mgrs}
    for (a, b), v in D.ALL_TIME_H2H.items():
        if a not in h2h or b not in h2h:
            continue
        h2h[a][b][0] += v["w1"]; h2h[a][b][1] += v["w2"]; h2h[a][b][2] += v["ties"]
        h2h[b][a][0] += v["w2"]; h2h[b][a][1] += v["w1"]; h2h[b][a][2] += v["ties"]
    return h2h, mgrs

def compute_futures():
    mgrs = list(D.CURRENT_TEAM_BY_MANAGER.keys())
    careers = {m: compute_manager_career(m) for m in mgrs}
    scores = {}
    for m, c in careers.items():
        rank = c["row2025"][0] if c["row2025"] else 12
        scores[m] = c["titles"] * 3 + c["podiums_total"] * 1 + (13 - rank) * 0.4 + 1
    total = sum(scores.values())
    odds_list = []
    for m, s in scores.items():
        prob = s / total
        if prob >= 0.5:
            odds = f'-{round(100 * prob / (1 - prob))}'
        else:
            odds = f'+{round(100 * (1 - prob) / prob)}'
        odds_list.append((m, careers[m]["team"], prob, odds, careers[m]))
    odds_list.sort(key=lambda x: -x[2])
    return odds_list

# ---------------------------------------------------------------
# INDEX
# ---------------------------------------------------------------
def build_index():
    champ = D.STANDINGS_2025[0]
    banners = build_banner_cards()
    body = f'''
<section class="hero">
  <div class="hero-inner">
    <p class="eyebrow">Yahoo Fantasy Football &middot; League #40967 &middot; 18th season</p>
    <h1>LOW BALLERZ</h1>
  </div>
  <div class="hero-banners">
    <p class="hero-banners-label">Banners of Champions &mdash; every title since 2011</p>
    <div class="banner-scroll-wrap in-hero">
      <div class="banner-rack banner-rack-scroll">{banners["banner_cards"]}</div>
    </div>
  </div>
  <div class="hero-inner">
    <p class="hero-sub">The one and only home for standings, scores, history, draft grades, trash talk and everything else the league needs. Twelve managers. Eighteen seasons. Zero mercy.</p>
    <div class="hero-actions">
      <a class="btn btn-gold" href="standings.html">See Standings</a>
      <a class="btn btn-outline" href="power-rankings.html">2026 Power Rankings</a>
    </div>
  </div>
</section>

<section class="stat-strip">
  <div class="stat-card">
    <span class="stat-label">Defending Champion</span>
    <span class="stat-value">Mamba Mentality</span>
    <span class="stat-sub">kumail &middot; 2025 Title</span>
  </div>
  <div class="stat-card">
    <span class="stat-label">2026 Draft</span>
    <span class="stat-value">Completed</span>
    <span class="stat-sub">Aug 22, 2026 &middot; 2 Keepers/Team</span>
  </div>
  <div class="stat-card">
    <span class="stat-label">League Size</span>
    <span class="stat-value">12 Teams</span>
    <span class="stat-sub">Head-to-Head &middot; Full PPR</span>
  </div>
  <div class="stat-card">
    <span class="stat-label">Founded</span>
    <span class="stat-value">2008</span>
    <span class="stat-sub">18 seasons of history</span>
  </div>
</section>

<section class="section">
  <h2 class="section-title">2026 Season Status</h2>
  <div class="notice-card">
    <p><strong>The draft is done.</strong> All 12 rosters are set after the live draft on <strong>Saturday, August 22</strong> &mdash; see the full results on <a href="draft.html">Draft Recap &amp; Grades</a>. Standings and weekly scores below still reflect the completed <strong>2025 season</strong> &mdash; this page will start tracking live 2026 results once Week 1 kicks off.</p>
  </div>
</section>

<section class="section">
  <h2 class="section-title">2025 Final Standings — Top 3</h2>
  <div class="podium">
'''
    medals = ["gold", "silver", "bronze"]
    for i, row in enumerate(D.STANDINGS_2025[:3]):
        rank, team, rec, pf, pa, wv, mv = row
        body += f'''
    <div class="podium-card {medals[i]}">
      <span class="podium-rank">#{rank}</span>
      <span class="podium-team">{team}</span>
      <span class="podium-mgr">{D.MANAGERS.get(team,"")}</span>
      <span class="podium-record">{rec} &middot; {fmt_score(pf)} PF</span>
    </div>
'''
    body += '''
  </div>
</section>
'''
    body += f'''
<section class="section">
  <h2 class="section-title">Explore the League</h2>
  <div class="link-grid">
    <a class="link-card" href="standings.html"><h3>Standings</h3><p>Full 2025 final standings with records, points for/against and waiver activity.</p></a>
    <a class="link-card" href="scores.html"><h3>Weekly Scores</h3><p>Every matchup from every week of the 2025 season, regular season through the championship.</p></a>
    <a class="link-card" href="power-rankings.html"><h3>Power Rankings</h3><p>Way-too-early 2026 power rankings based on last year's results and offseason moves.</p></a>
    <a class="link-card" href="history.html"><h3>History &amp; Records</h3><p>All-time champions dating back to 2008, plus single-season records.</p></a>
    <a class="link-card" href="managers.html"><h3>Managers</h3><p>Every current manager's trophy case and career highlights.</p></a>
    <a class="link-card" href="records.html"><h3>All-Time Records</h3><p>Sortable career ledger &mdash; titles, podiums and 2025 results.</p></a>
    <a class="link-card" href="rivalries.html"><h3>Rivalries</h3><p>2025 head-to-head records between every manager in the league.</p></a>
    <a class="link-card" href="draft-central.html"><h3>Draft Central</h3><p>The completed 2026 draft board, final order and live results.</p></a>
    <a class="link-card" href="draft.html"><h3>Draft Recap</h3><p>Full 2026 draft board and grades, plus the 2025 draft archive.</p></a>
    <a class="link-card" href="keepers.html"><h3>Keepers</h3><p>2026 keepers by team, longest active streaks, and the new rules starting 2027.</p></a>
    <a class="link-card" href="trades.html"><h3>Trade Newsletter</h3><p>Every trade from 2021-2025, graded with the benefit of hindsight.</p></a>
    <a class="link-card" href="trade-analyzer.html"><h3>Trade Analyzer</h3><p>Pick two teams and get an instant value verdict on any trade.</p></a>
    <a class="link-card" href="trash-talk.html"><h3>Trash Talk Board</h3><p>The receipts. Cold, hard, stat-backed disrespect.</p></a>
    <a class="link-card" href="futures.html"><h3>Futures &amp; Ballot</h3><p>2026 championship odds and a live predictions ballot.</p></a>
    <a class="link-card" href="rules.html"><h3>League Rules</h3><p>Scoring settings, roster requirements, waivers, trades and playoff format.</p></a>
    <a class="link-card" href="recap.html"><h3>Newsletter</h3><p>The 2025 season recap, superlatives, awards, and a weekly 2026 template.</p></a>
  </div>
</section>
'''
    return page("Home", "index.html", body, "Official site of the Low Ballerz fantasy football league — standings, scores, history, draft grades and more.")

# ---------------------------------------------------------------
# STANDINGS
# ---------------------------------------------------------------
def build_standings():
    rows = ""
    for rank, team, rec, pf, pa, wv, mv in D.STANDINGS_2025:
        cls = ""
        if rank == 1: cls = "row-champ"
        elif rank <= 6: cls = "row-playoff"
        rows += f'''
    <tr class="{cls}">
      <td class="rank-cell">{rank}{' &#127942;' if rank==1 else ''}</td>
      <td>{team_pill(team)}</td>
      <td>{rec}</td>
      <td>{fmt_score(pf)}</td>
      <td>{fmt_score(pa)}</td>
      <td>{money(wv)}</td>
      <td>{mv}</td>
    </tr>'''
    body = f'''
<section class="page-hero">
  <p class="eyebrow">2025 Season &middot; Final</p>
  <h1>Standings</h1>
  <p class="hero-sub">Final placement for the 2025 season, including the playoff bracket. The 2026 regular-season table will populate here once games kick off.</p>
</section>
<section class="section">
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>Rank</th><th>Team</th><th>Record</th><th>PF</th><th>PA</th><th>Waiver $</th><th>Moves</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
  <div class="legend">
    <span><i class="dot dot-champ"></i> Champion</span>
    <span><i class="dot dot-playoff"></i> Made the playoffs (top 6)</span>
  </div>
</section>
'''
    return page("Standings", "standings.html", body, "2025 final standings for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# SCORES
# ---------------------------------------------------------------
def build_scores():
    tabs = ""
    panels = ""
    week_labels = {w: f"Week {w}" for w in range(1,15)}
    all_weeks = list(range(1,15))
    for i, w in enumerate(all_weeks):
        active = "active" if i == 0 else ""
        tabs += f'<button class="week-tab {active}" data-week="w{w}">{week_labels[w]}</button>'
        matches = ""
        for a, sa, b, sb in D.WEEKLY_SCORES_2025[w]:
            a_win = sa > sb
            matches += f'''
        <div class="matchup-card">
          <div class="matchup-team {'winner' if a_win else ''}">
            <span class="mt-name">{a}</span>
            <span class="mt-score">{fmt_score(sa)}</span>
          </div>
          <div class="matchup-vs">vs</div>
          <div class="matchup-team {'winner' if not a_win else ''}">
            <span class="mt-name">{b}</span>
            <span class="mt-score">{fmt_score(sb)}</span>
          </div>
        </div>'''
        panels += f'<div class="week-panel {active}" id="w{w}"><div class="matchup-grid">{matches}</div></div>'

    # playoffs
    playoff_html = ""
    for round_name, games in D.PLAYOFF_BRACKET_2025.items():
        playoff_html += f'<h3 class="playoff-round-title">{round_name}</h3><div class="matchup-grid">'
        for a, sa, b, sb in games:
            if sa is None:
                playoff_html += f'''
        <div class="matchup-card bye-card">
          <div class="matchup-team winner"><span class="mt-name">{a}</span><span class="mt-score">BYE</span></div>
        </div>'''
                continue
            a_win = sa > sb
            playoff_html += f'''
        <div class="matchup-card">
          <div class="matchup-team {'winner' if a_win else ''}">
            <span class="mt-name">{a}</span><span class="mt-score">{fmt_score(sa)}</span>
          </div>
          <div class="matchup-vs">vs</div>
          <div class="matchup-team {'winner' if not a_win else ''}">
            <span class="mt-name">{b}</span><span class="mt-score">{fmt_score(sb)}</span>
          </div>
        </div>'''
        playoff_html += "</div>"

    body = f'''
<section class="page-hero">
  <p class="eyebrow">2025 Season</p>
  <h1>Weekly Scores</h1>
  <p class="hero-sub">Every regular-season matchup (Weeks 1&ndash;14), plus the full playoff bracket. Click a week to jump to it.</p>
</section>
<section class="section">
  <h2 class="section-title">Regular Season</h2>
  <div class="week-tabs">{tabs}</div>
  <div class="week-panels">{panels}</div>
</section>
<section class="section">
  <h2 class="section-title">Playoffs (Weeks 15&ndash;17)</h2>
  {playoff_html}
</section>
'''
    return page("Weekly Scores", "scores.html", body, "Every weekly matchup score from the 2025 Low Ballerz fantasy football season.")

# ---------------------------------------------------------------
# POWER RANKINGS
# ---------------------------------------------------------------
POWER_RANKINGS_2026 = [
    ("Mamba Mentality", "kumail", 1, "Defending champion, and they did it the hard way — a 4-seed that knocked off the undefeated #1 overall team in the semis, then won the title by 0.48 points. Nothing here suggests a fluke: top-3 in PF two years running."),
    ("Scypher", "Sadiq", 2, "Went a perfect 14-0 in the regular season with the league's best scoring offense (2660.16 PF) — then blew the semifinal and settled for 3rd. The commissioner's team has the horses; the postseason nerves are the only question."),
    ("Christian My Calf Hurt", "Sarosh", 3, "Runner-up by the width of a single stat correction. Consistent all year, playoff-tested, and one of only two teams to make the championship game."),
    ("Hells Angels", "omar", 4, "9-5 with the best point differential outside the top 3, plus the league's fattest waiver war chest heading into the offseason ($55 left). Quietly one of the most complete rosters in the league."),
    ("Sahara and Sahil", "Meisam", 5, "9-5 and top-6 in scoring, but flamed out early in the playoffs. The pieces are good; the seeding tiebreakers weren't kind."),
    ("Hakka PUKA!!", "Parvez", 6, "A grinder — 7-7 in the regular season but scrapped its way to a 5th-place playoff finish and stayed within a possession of a title shot most weeks."),
    ("Hurts My Brain", "Hussain", 7, "5-9 masked a genuinely dangerous offense that dropped a 216-point week. If the injury luck turns, this team jumps fast."),
    ("Immaculate Concepcion", "Hassnain", 8, "7-7 with the widest week-to-week swings in the league (a 74.98 floor and a 211.06 ceiling). Boom or bust, literally."),
    ("Chase the Baker Ladd!", "Turab", 9, "6-8, 10th place, but opened the season with a signature win over the eventual champ. Consistency is the 2026 mandate."),
    ("Philly Illy", "Ilyas", 10, "5-9 but never bottom of the barrel — a middling scoring profile that needs difference-makers, not just depth."),
    ("Ali Khalid LLC", "wiseonekms", 11, "5-9 despite the fewest roster moves in the league (11) and $70 of FAAB left unused. A quieter approach than most, and the results weren't there — a retool, not a rebuild."),
    ("This hill I die on", "wajahat z", 12, "3-11, the league's lowest scoring offense (2026.46 PF) and its highest points-allowed. Nowhere to go but up."),
]

def build_power_rankings():
    cards = ""
    for team, mgr, rank, blurb in POWER_RANKINGS_2026:
        cards += f'''
    <div class="rank-card">
      <span class="rank-num">{rank}</span>
      <div class="rank-body">
        <h3>{team} <small>{mgr}</small></h3>
        <p>{blurb}</p>
      </div>
    </div>'''
    body = f'''
<section class="page-hero">
  <p class="eyebrow">Way-Too-Early &middot; 2026 Preseason</p>
  <h1>Power Rankings</h1>
  <p class="hero-sub">Since the 2026 season hasn't kicked off yet, these preseason rankings are built from 2025 final standings, scoring trends and offseason activity. Once Week 1 is in the books, it's all about results.</p>
</section>
<section class="section">
  <div class="rank-list">{cards}</div>
</section>
'''
    return page("Power Rankings", "power-rankings.html", body, "2026 preseason power rankings for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# HISTORY
# ---------------------------------------------------------------
TROPHY_SVG = '''<svg class="trophy-icon" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M7 4h10v3.5a5 5 0 0 1-5 5 5 5 0 0 1-5-5V4Z" fill="currentColor"/>
<path d="M7 5H4a1 1 0 0 0-1 1v1a4 4 0 0 0 4 4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
<path d="M17 5h3a1 1 0 0 1 1 1v1a4 4 0 0 1-4 4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
<path d="M12 12.5v3" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
<path d="M8.5 19.5c0-1.4 1.6-2.2 3.5-2.2s3.5.8 3.5 2.2" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"/>
<path d="M9 20h6" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>
</svg>'''

def build_banner_cards():
    """Shared championship-banner builder, used on both History & Records and the homepage."""
    reigning_year = max(D.CHAMPIONS_BY_MANAGER)
    reigning_team, reigning_mgr_key, reigning_current = D.CHAMPIONS_BY_MANAGER[reigning_year]
    reigning_display_team = reigning_current or reigning_team

    titles = {}
    for year, (team, mgr, current_team) in D.CHAMPIONS_BY_MANAGER.items():
        key = mgr if mgr else "unknown"
        titles.setdefault(key, {"years": [], "team_names": set(), "current": current_team})
        titles[key]["years"].append(year)
        titles[key]["team_names"].add(team)

    # sort: most titles first, then most recent title first, then name
    banner_order = sorted(
        titles.items(),
        key=lambda kv: (-len(kv[1]["years"]), -max(kv[1]["years"]), kv[0])
    )

    banner_cards = ""
    for mgr_key, info in banner_order:
        years_sorted = sorted(info["years"], reverse=True)
        is_unknown = mgr_key == "unknown"
        is_departed = (not is_unknown) and info["current"] is None
        display_name = "Unattributed" if is_unknown else mgr_key
        sub_label = None
        if is_unknown:
            sub_label = "Manager name hidden by Yahoo for these old seasons"
        elif is_departed:
            sub_label = "Former league member — no longer in the league"
        else:
            sub_label = info["current"]
        sub_html = f'<span class="banner-mgr">{sub_label}</span>' if sub_label else ""
        trophies = TROPHY_SVG * len(years_sorted)
        years_label = ", ".join(str(y) for y in years_sorted)
        is_reigning = years_sorted[0] == reigning_year and mgr_key == reigning_mgr_key
        extra_cls = " banner-reigning" if is_reigning else (" banner-departed" if (is_departed or is_unknown) else "")
        banner_cards += f'''
    <div class="banner-card{extra_cls}">
      <div class="banner-trophies">{trophies}</div>
      <span class="banner-team">{display_name}</span>
      {sub_html}
      <span class="banner-years">{years_label}</span>
      <span class="banner-count">{len(years_sorted)}x Champion</span>
    </div>'''

    return {
        "reigning_year": reigning_year,
        "reigning_mgr_key": reigning_mgr_key,
        "reigning_display_team": reigning_display_team,
        "banner_cards": banner_cards,
    }

def build_history():
    rows = ""
    for year, first, second, third, _finish in D.ALL_TIME:
        champ_marker = ' &#127942;' if True else ''
        rows += f'''
    <tr>
      <td>{year}</td>
      <td class="champ-cell">{first}</td>
      <td>{second}</td>
      <td>{third}</td>
    </tr>'''

    # ---- All-Time Finishes: every current manager's placement, every year ----
    h2h_all, mgrs_all = compute_h2h_alltime()
    careers = {m: compute_manager_career(m) for m in mgrs_all}
    finish_order = sorted(mgrs_all, key=lambda m: -careers[m]["career_win_pct"])

    finish_header = "<th>Season</th>" + "".join(f'<th>{m}</th>' for m in finish_order)
    finish_rows = ""
    for year in sorted(D.ALL_TIME_FINISHES.keys(), reverse=True):
        year_data = D.ALL_TIME_FINISHES[year]
        cells = f'<td>{year}</td>'
        for m in finish_order:
            rank = year_data.get(m)
            if rank is None:
                cells += '<td class="table-footnote">&mdash;</td>'
            elif rank == 1:
                cells += f'<td class="champ-cell">{rank}st &#127942;</td>'
            else:
                suffix = {2: "nd", 3: "rd"}.get(rank, "th")
                cells += f'<td>{rank}{suffix}</td>'
        finish_rows += f'<tr>{cells}</tr>'

    # ---- Trophy Case: reigning champion + banners grouped by the actual account/manager ----
    banners = build_banner_cards()
    reigning_year = banners["reigning_year"]
    reigning_mgr_key = banners["reigning_mgr_key"]
    reigning_display_team = banners["reigning_display_team"]
    banner_cards = banners["banner_cards"]

    # ---- Career Standings: 1st/2nd/3rd tallies by manager ----
    tally = {}
    for year, place, team, mgr in D.PODIUM_FINISHES:
        key = mgr if mgr else "__unattributed__"
        row = tally.setdefault(key, {"1": 0, "2": 0, "3": 0})
        row[str(place)] += 1

    def sort_key(item):
        key, row = item
        return (-row["1"], -row["2"], -row["3"], key)

    current_tally = {k: v for k, v in tally.items() if k not in ("__unattributed__", "m")}
    other_tally = {k: v for k, v in tally.items() if k in ("__unattributed__", "m")}
    ordered = sorted(current_tally.items(), key=sort_key)
    ordered_other = sorted(other_tally.items(), key=sort_key)

    leaderboard_rows = ""
    rank_n = 0
    for key, row in ordered:
        rank_n += 1
        total = row["1"] + row["2"] + row["3"]
        leaderboard_rows += f'''
    <tr>
      <td class="rank-cell">{rank_n}</td>
      <td class="champ-cell">{key}</td>
      <td>{D.CURRENT_TEAM_BY_MANAGER.get(key, "")}</td>
      <td>{row["1"]}</td>
      <td>{row["2"]}</td>
      <td>{row["3"]}</td>
      <td><strong>{total}</strong></td>
    </tr>'''
    for key, row in ordered_other:
        total = row["1"] + row["2"] + row["3"]
        if key == "__unattributed__":
            name_cell = "Unattributed (2008&ndash;2010)"
            team_cell = '<span class="banner-mgr">Manager names hidden by Yahoo</span>'
        else:
            name_cell = "m"
            team_cell = '<span class="banner-mgr">Former league member, left after 2021</span>'
        leaderboard_rows += f'''
    <tr class="row-departed">
      <td class="rank-cell">&ndash;</td>
      <td class="champ-cell">{name_cell}</td>
      <td>{team_cell}</td>
      <td>{row["1"]}</td>
      <td>{row["2"]}</td>
      <td>{row["3"]}</td>
      <td><strong>{total}</strong></td>
    </tr>'''

    leaderboard_table = f'''
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>#</th><th>Manager</th><th>Current Team</th><th>1st</th><th>2nd</th><th>3rd</th><th>Total Podiums</th></tr></thead>
      <tbody>{leaderboard_rows}</tbody>
    </table>
  </div>
  <p class="table-footnote">Ranked among today's 12 managers only, by championships then 2nd-place then 3rd-place finishes. kumail leads the league in titles (3), but Meisam and Turab have been on the podium the most overall (8 times each) &mdash; Turab's five 3rd-place finishes are the most of anyone who's won just one title. The two unranked rows at the bottom are podium finishes that can't be credited to a current member: a departed 13th manager known only as "m" (3 titles, gone since 2021), and three seasons (2008&ndash;2010) whose manager identities Yahoo has hidden.</p>'''

    trophy_case = f'''
<section class="section">
  <h2 class="section-title">Trophy Case</h2>
  <div class="reigning-champ-banner">
    <div class="reigning-trophy">{TROPHY_SVG}</div>
    <div class="reigning-body">
      <span class="reigning-label">{reigning_year} Reigning Champion</span>
      <span class="reigning-team">{reigning_mgr_key}</span>
      <span class="reigning-mgr">{reigning_display_team}</span>
    </div>
  </div>
  <div class="banner-rack">{banner_cards}</div>
  <p class="table-footnote">Banners are grouped by the actual Yahoo account that won the title, not the team name &mdash; teams rebrand often (Sadiq alone has won as "Scypher" twice), so this is the real head-to-head trophy count. Verified against Yahoo's manager records for every season from 2011 to 2025. 2008&ndash;2010 manager identities are hidden by Yahoo's privacy settings on those old seasons and couldn't be recovered. "m" was a 13th league member who won three titles before leaving the league after the 2021 season &mdash; not one of today's 12 managers.</p>
</section>

<section class="section">
  <h2 class="section-title">Career Standings by Manager</h2>
  <p class="section-note">Every 1st, 2nd, and 3rd place finish since 2008, credited to the actual person behind the team &mdash; not whatever the team happened to be named that year.</p>
  {leaderboard_table}
</section>
'''

    # records computed from full 2025 weekly data
    all_games = []
    for w, games in D.WEEKLY_SCORES_2025.items():
        for a, sa, b, sb in games:
            all_games.append((w, a, sa, b, sb))
    high = max(all_games, key=lambda g: max(g[2], g[4]))
    low = min(all_games, key=lambda g: min(g[2], g[4]))
    closest = min(all_games, key=lambda g: abs(g[2]-g[4]))
    blowout = max(all_games, key=lambda g: abs(g[2]-g[4]))

    high_team, high_score = (high[1], high[2]) if high[2] > high[4] else (high[3], high[4])
    low_team, low_score = (low[1], low[2]) if low[2] < low[4] else (low[3], low[4])

    body = f'''
<section class="page-hero">
  <p class="eyebrow">2008 &ndash; 2025</p>
  <h1>League History &amp; Records</h1>
  <p class="hero-sub">Eighteen seasons of champions, and the single-season records from the most recently completed year.</p>
</section>
{trophy_case}
<section class="section">
  <h2 class="section-title">All-Time Champions</h2>
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>Season</th><th>1st Place</th><th>2nd Place</th><th>3rd Place</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
  <p class="table-footnote">Note: many teams have rebranded over the years (e.g. "Champ Scypher" &rarr; "Scypher" for 2026), so the same manager may appear under different team names across seasons.</p>
</section>

<section class="section">
  <h2 class="section-title">Every Manager's Finish, Every Year</h2>
  <p class="section-note">Same 15 seasons (2011&ndash;2025), but broken out by manager instead of just the podium &mdash; final placement after the full playoff and consolation bracket, not just regular-season record. Columns are ordered by career win percentage, same as the Rivalries page. A dash means that manager wasn't in the league that season (see the Records page for each manager's tenure).</p>
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr>{finish_header}</tr></thead>
      <tbody>{finish_rows}</tbody>
    </table>
  </div>
  <p class="table-footnote">2008&ndash;2010 aren't included here &mdash; Yahoo hides manager identities on those archived seasons, so no attribution is possible. Pulled directly from each season's final Yahoo standings.</p>
</section>

<section class="section">
  <h2 class="section-title">2025 Season Records</h2>
  <div class="record-grid">
    <div class="record-card">
      <span class="record-label">Highest Single-Week Score</span>
      <span class="record-value">{fmt_score(high_score)}</span>
      <span class="record-sub">{high_team} &middot; Week {high[0]}</span>
    </div>
    <div class="record-card">
      <span class="record-label">Lowest Single-Week Score</span>
      <span class="record-value">{fmt_score(low_score)}</span>
      <span class="record-sub">{low_team} &middot; Week {low[0]}</span>
    </div>
    <div class="record-card">
      <span class="record-label">Closest Margin</span>
      <span class="record-value">{fmt_score(abs(closest[2]-closest[4]))}</span>
      <span class="record-sub">{closest[1]} vs {closest[3]} &middot; Week {closest[0]}</span>
    </div>
    <div class="record-card">
      <span class="record-label">Biggest Blowout</span>
      <span class="record-value">{fmt_score(abs(blowout[2]-blowout[4]))}</span>
      <span class="record-sub">{blowout[1]} vs {blowout[3]} &middot; Week {blowout[0]}</span>
    </div>
    <div class="record-card">
      <span class="record-label">Best Regular Season</span>
      <span class="record-value">14-0</span>
      <span class="record-sub">Champ Scypher &middot; 2025</span>
    </div>
    <div class="record-card">
      <span class="record-label">Highest Season PF</span>
      <span class="record-value">2660.16</span>
      <span class="record-sub">Champ Scypher &middot; 2025</span>
    </div>
  </div>
</section>
'''
    return page("History & Records", "history.html", body, "All-time champions and single-season records for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# DRAFT
# ---------------------------------------------------------------
DRAFT_GRADES_2025 = [
    ("Champ Scypher", "A+", "1.02 Jahmyr Gibbs, 2.11 Josh Allen, 3.02 Jaxon Smith-Njigba. Turned this class into a 14-0 regular season and the league's best offense (2660 PF) — as good a draft-to-results translation as it gets."),
    ("Mamba Mentality", "A", "1.01 Ashton Jeanty plus 2.12 Marvin Harrison Jr. gave this roster a true bell-cow plus a difference-making WR2. Rode it to the title."),
    ("Christian My Calf Hurt", "A-", "1.11 Christian McCaffrey as the anchor, with Amon-Ra St. Brown falling to 2.02. Volatile due to McCaffrey's injury history, but the depth carried them to the championship game."),
    ("Hells Angels", "B+", "1.07 Nico Collins and a string of solid Round 2-4 value (Josh Jacobs, Davante Adams, James Cook) built a deep, well-rounded 9-5 roster."),
    ("Sahara and Sahil", "B+", "1.09 Malik Nabers and 2.04 A.J. Brown gave this team an elite WR duo; the roster scored top-6 in the league."),
    ("Hakka PUKA!!", "B", "1.05 CeeDee Lamb and 2.08 Jayden Daniels — a solid 1-2 punch that delivered a 7-7 record and a playoff berth."),
    ("Hurts My Brain", "B-", "1.04 Derrick Henry was a slam-dunk pick, but thin depth behind him (Bo Nix at 3.04) left this team unable to survive injuries. Talent outpaced the record."),
    ("Chig-Chig Boom", "C+", "1.10 Jonathan Taylor was a strong start, but the middle rounds (Omarion Hampton, Courtland Sutton) never hit their upside consistently."),
    ("You're Ma Nanga Guy", "C+", "1.12 Drake London and a QB-heavy build (Mahomes at 5.12, Jefferson at 14.01) — talented on paper, but a 6-8 finish says the roster construction needs a rethink for 2026."),
    ("Tera Boutte Mein Danda", "C", "1.06 Lamar Jackson was elite value, but the supporting cast (Terry McLaurin, Trey McBride) didn't provide enough separation from the pack."),
    ("Ali Khalid LLC", "C-", "1.08 Bijan Robinson had bust potential written all over it in a good way, but this roster saw the least activity in the league all year (11 moves, $70 of FAAB unused) — a sign the original plan didn't get much of a chance to adjust."),
    ("This hill I die on", "D+", "1.03 Saquon Barkley was arguably the draft's best value pick, but the rest of the roster produced the league's lowest scoring output. A season to forget despite the headline pick."),
]

# Value-based grades for the 2026 draft, written immediately after the live draft on
# Aug 22, 2026 — judged on ADP value, roster construction and positional balance,
# since there are no season results yet to grade against.
DRAFT_GRADES_2026 = [
    ("Immaculate Concepcion", "A+", "1.11 Jonathan Taylor (kept at a Round 1 cost) plus 2.02 Saquon Barkley gives this roster the best RB1/RB1 combo in the league. Add 3.11 Jaylen Waddle, 4.02 Terry McLaurin and 5.11 Sam LaPorta and this is a stacked, top-heavy monster with almost no weak spot."),
    ("Mamba Mentality", "A", "1.01 Ashton Jeanty and 3.01 Malik Nabers alone are league-winning assets, and 4.12 Patrick Mahomes gives a rock-solid floor at QB. The RB2 spot (Jeremiyah Love) and late flier (Travis Hunter) are boom-or-bust, but the top of this roster is as good as anyone's."),
    ("Scypher", "A", "1.08 Jahmyr Gibbs and 12.08 De'Von Achane — both kept — is the best RB duo in the league relative to what it actually cost. 2.05 Nico Collins anchors the receiving corps. Quarterback is a total question mark (Dart, Shough, Tagovailoa), but the RB efficiency alone carries this class."),
    ("Hakka PUKA!!", "A", "1.03 Ja'Marr Chase is the safest true WR1 in the game, 2.10 Jayden Daniels (kept) is exceptional QB value, and 15.03 Puka Nacua (kept) is one of the single best keeper bargains in the league. Deep at every position with almost no holes."),
    ("Hells Angels", "A-", "1.04 Jaxon Smith-Njigba plus a kept RB1/RB2 in Josh Jacobs and James Cook III gives this team a high floor everywhere. 3.04 Trey McBride and 5.04 Bo Nix round out a quietly complete, well-balanced build."),
    ("Sahara and Sahil", "A-", "1.05 Josh Allen is the safest QB anchor available, 2.08 Kenneth Walker III and 3.05 Breece Hall give a strong RB1/RB2, and 13.05 Garrett Wilson (kept) is a ridiculous value at that cost. WR depth beyond Wilson is unproven, but the top of the roster is excellent."),
    ("Chase the Baker Ladd!", "A-", "1.12 Chase Brown and 2.01 Omarion Hampton is a legitimate workhorse RB1/RB2 pairing, and 14.01 Justin Jefferson (kept via a 2023 trade) is the single best value asset in the entire league. No clear QB1 on the roster is the one real concern."),
    ("Christian My Calf Hurt", "B+", "1.10 Christian McCaffrey (kept) and 2.03 Jalen Hurts is a strong 1-2, with 3.10 Tee Higgins and 8.10 Rome Odunze (kept) stacking the receiving corps. Injury risk at the top (CMC) and thin proven RB depth behind him are the risks."),
    ("Philly Illy", "B+", "1.09 CeeDee Lamb, 2.04 A.J. Brown and 5.09 Emeka Egbuka (kept) is arguably the best three-deep WR room in the league, and 3.09 Justin Herbert anchors at QB. Running back was almost entirely ignored until Round 4, which is the clear weakness here."),
    ("This hill I die on", "B+", "1.02 Lamar Jackson gives elite dual-threat QB upside, 2.11 Amon-Ra St. Brown (kept) is fantastic WR1 value, and 3.02 Derrick Henry still offers bell-cow volume. WR2/WR3 depth (Burden, Reed, Robinson) is unproven boom-or-bust."),
    ("Ali Khalid LLC", "B", "1.07 Bijan Robinson (kept) is elite value at that cost, and 2.06 Drake London gives a true WR1. But the RB room craters after Bijan (Jadarian Price, Tank Dell, Brian Robinson are all speculative), and the QB room (Goff, developmental rookie Fernando Mendoza) is thin."),
    ("Hurts My Brain", "B-", "1.06 Joe Burrow is a bold, top-heavy QB anchor with real injury-history risk, and 12.06 Brock Bowers (kept) is elite TE value. Running back was a total afterthought until Round 7 — Tuten, Dowdle, Mason and the kept Cam Skattebo are unproven, and that's the roster's clear weak spot."),
]

def build_draft():
    def render_board(draft_dict, css_class="draft-board"):
        rounds_html = ""
        for rnd in sorted(draft_dict.keys()):
            picks = draft_dict[rnd]
            cells = ""
            for i, (player, team) in enumerate(picks):
                overall = (rnd-1)*12 + i + 1
                cells += f'''
      <div class="pick-cell">
        <span class="pick-num">{overall}</span>
        <span class="pick-player">{player}</span>
        <span class="pick-team">{team}</span>
      </div>'''
            rounds_html += f'''
    <div class="draft-round">
      <h3>Round {rnd}</h3>
      <div class="pick-grid">{cells}</div>
    </div>'''
        return f'<div class="{css_class}">{rounds_html}</div>'

    def render_grades(grades):
        grade_rows = ""
        for team, grade, blurb in grades:
            grade_rows += f'''
    <div class="grade-card">
      <div class="grade-badge grade-{grade[0].lower()}">{grade}</div>
      <div class="grade-body">
        <h3>{team_pill(team)}</h3>
        <p>{blurb}</p>
      </div>
    </div>'''
        return f'<div class="grade-list">{grade_rows}</div>'

    body = f'''
<section class="page-hero">
  <p class="eyebrow">2026 Draft &middot; Completed Saturday, August 22, 2026</p>
  <h1>Draft Recap &amp; Grades</h1>
  <p class="hero-sub">The 2026 draft is in the books &mdash; full 16-round board and value-based grades below (judged on ADP value and roster construction, since there are no season results yet). Looking for this year's keepers? Head to the <a href="keepers.html">Keepers page</a>.</p>
</section>

<section class="section">
  <h2 class="section-title">2026 Draft Grades</h2>
  <p class="section-note">Graded on value and roster construction right after the draft &mdash; not on results, since the season hasn't started yet.</p>
  {render_grades(DRAFT_GRADES_2026)}
</section>

<section class="section">
  <h2 class="section-title">Full 2026 Draft Board</h2>
  {render_board(D.DRAFT_2026)}
</section>

<section class="section">
  <h2 class="section-title">2025 Draft Archive</h2>
  <p class="section-note">For reference: how last year's draft actually played out, graded with the benefit of hindsight.</p>
  {render_grades(DRAFT_GRADES_2025)}
  {render_board(D.DRAFT_2025)}
</section>
'''
    return page("Draft Recap & Grades", "draft.html", body, "Full 2026 draft board and grades, plus the 2025 draft archive, for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# KEEPERS
# ---------------------------------------------------------------
def build_keepers():
    keeper_cards = ""
    for slot, team, mgr in D.DRAFT_ORDER_2026:
        keepers = D.KEEPERS_2026.get(team, [])
        history = D.KEEPER_HISTORY.get(team, {})
        keeper_lines = ""
        for player, rnd in keepers:
            years, note = history.get(player, (1, ""))
            streak_label = "New Keeper" if years <= 1 else f"{years}x Straight Year"
            streak_cls = "streak-new" if years <= 1 else ("streak-hot" if years >= 4 else "streak-warm")
            keeper_lines += f'''
        <div class="keeper-line">
          <div class="keeper-line-top">
            <span class="keeper-player">{player}</span>
            <span class="keeper-cost">Rd {rnd}</span>
          </div>
          <div class="keeper-meta">
            <span class="streak-badge {streak_cls}">{streak_label}</span>
            <span class="keeper-note">{note}</span>
          </div>
        </div>'''
        keeper_cards += f'''
    <div class="keeper-card">
      <div class="keeper-head">
        <span class="keeper-slot">Pick {slot}</span>
        {team_pill(team)}
      </div>
      <div class="keeper-body">{keeper_lines}</div>
    </div>'''

    keeper_rule_rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in D.KEEPER_TRADE_RULES_2027)

    body = f'''
<section class="page-hero">
  <p class="eyebrow">2026 Draft &middot; August 22, 2026 &middot; 10:00pm CDT</p>
  <h1>Keepers</h1>
  <p class="hero-sub">This is a keeper league &mdash; every team locks in two keepers before the clock starts. Below: each team's confirmed 2026 keepers, the longest active streaks, and the new keeper rules taking effect in 2027.</p>
</section>

<section class="section">
  <h2 class="section-title">2026 Keepers</h2>
  <p class="section-note">Each team's two keepers, the draft round it costs them, and how many years running they've been kept &mdash; verified against Yahoo's draft records back to 2022.</p>
  <div class="keeper-grid">{keeper_cards}</div>
</section>

<section class="section">
  <h2 class="section-title">Longest Active Keeper Streaks</h2>
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>Player</th><th>Team</th><th>Consecutive Years Kept</th><th>Since</th></tr></thead>
      <tbody>
        <tr><td class="champ-cell">Jordan Love</td><td>{team_pill("Ali Khalid LLC")}</td><td>4</td><td>Drafted 2022, kept every year since</td></tr>
        <tr><td class="champ-cell">Christian McCaffrey</td><td>{team_pill("Christian My Calf Hurt")}</td><td>4</td><td>Drafted 2022, kept every year since</td></tr>
        <tr><td>De'Von Achane</td><td>{team_pill("Scypher")}</td><td>3</td><td>Joined 2023, kept every year since 2024</td></tr>
        <tr><td>Justin Jefferson</td><td>{team_pill("Chase the Baker Ladd!")}</td><td>3</td><td>Traded in 2023, kept every year since 2024</td></tr>
        <tr><td>Garrett Wilson</td><td>{team_pill("Sahara and Sahil")}</td><td>3</td><td>Traded from Ilyas Oct 3, 2023, kept every year since 2024</td></tr>
        <tr><td>Puka Nacua</td><td>{team_pill("Hakka PUKA!!")}</td><td>3</td><td>Joined 2023, kept every year since 2024</td></tr>
      </tbody>
    </table>
  </div>
  <p class="table-footnote">Streaks verified from Yahoo's "This player is a keeper" flags on the 2022&ndash;2025 draft boards, plus the confirmed 2026 keeper list. A player's very first season on a roster (drafted or traded for) doesn't count as a "kept" year &mdash; only the years they were actively retained do.</p>
</section>

<section class="section">
  <h2 class="section-title">Heads Up: New Keeper Rules Start in 2027</h2>
  <p class="section-note">Voted on by the league in 2026. None of this changes anything for the 2026 draft above &mdash; it's still 2 keepers per team under the existing rules. But it's a big deal for 2027: the max-2-year-hold rule means every player above with a 3&ndash;4 year streak (Jordan Love, Christian McCaffrey, De'Von Achane, Justin Jefferson, Garrett Wilson, Puka Nacua) will already be past the new 2-year cap and hits free agency in 2027 unless the team re-drafts them. Full detail on the <a href="rules.html">Rules page</a>.</p>
  <div class="table-wrap">
    <table class="data-table two-col"><tbody>{keeper_rule_rows}</tbody></table>
  </div>
</section>
'''
    return page("Keepers", "keepers.html", body, "2026 keepers by team, longest active keeper streaks, and the new keeper rules starting in 2027 for the Low Ballerz league.")

# ---------------------------------------------------------------
# TRASH TALK
# ---------------------------------------------------------------
TRASH_TALK = [
    ("THE NUMBERS DON'T LIE", "Champ Scypher went 14-0 in the regular season, best record in franchise history — and still didn't win the title. 3rd place. Choke of the century, or just a really deep league?"),
    ("RAZOR THIN", "Mamba Mentality won the 2025 championship by exactly 0.48 points over Christian My Calf Hurt. A single lucky stat correction either way and this whole banner gets an asterisk."),
    ("THE BASEMENT", "This hill I die on finished dead last in points scored (2026.46) AND allowed the most points against (2480.28). Historically bad on both sides of the ball."),
    ("ICE COLD", "Chig-Chig Boom posted a 74.98 in Week 11 — the single lowest score by any team all season. That's not a lineup, that's a cry for help."),
    ("SPENT IT ALL AND GOT NOTHING", "Ali Khalid LLC made the fewest roster moves in the league (11) and sat on $70 of unused FAAB all year — and still finished 11th. Sometimes doing nothing doesn't pay off either."),
    ("PAPER CHAMPS", "Champ Scypher dropped 246.08 in Week 12, one of the biggest weeks of the season — and still lost in the semifinals a few weeks later. Regular season stats don't play in the playoffs."),
    ("OPENING DAY DISRESPECT", "You're Ma Nanga Guy beat the eventual champion, Mamba Mentality, in Week 1. Mamba then won the title anyway. Statement win, zero impact."),
    ("FREE WEEK", "In Week 9, Ali Khalid LLC and Chig-Chig Boom combined for the lowest-scoring matchup of the season (85.92 to 86.56). Somebody had to win. Nobody deserved to."),
]

def build_trash_talk():
    cards = ""
    for headline, body_txt in TRASH_TALK:
        cards += f'''
    <div class="talk-card">
      <h3>{headline}</h3>
      <p>{body_txt}</p>
    </div>'''
    body = f'''
<section class="page-hero">
  <p class="eyebrow">The Receipts</p>
  <h1>Trash Talk Board</h1>
  <p class="hero-sub">Stat-backed disrespect from the 2025 season, plus a live board below where anyone in the league can drop their own take in real time.</p>
</section>
<section class="section">
  <h2 class="section-title">The Official Burns</h2>
  <div class="talk-grid">{cards}</div>
</section>

<section class="section">
  <h2 class="section-title">Live Board</h2>
  <p class="section-note">Post something and it shows up for everyone instantly &mdash; no login, no refresh needed. Be a good sport about it.</p>

  <div id="talk-live-status" class="notice-card" style="display:none;"></div>

  <form id="talk-form" class="talk-form">
    <input id="talk-name" class="talk-input" type="text" maxlength="40" placeholder="Your name (e.g. Turab)" required>
    <textarea id="talk-message" class="talk-textarea" maxlength="400" rows="3" placeholder="Say what you came to say..." required></textarea>
    <button type="submit" class="btn btn-gold talk-submit">Post It</button>
  </form>

  <div id="talk-feed" class="talk-feed">
    <p class="talk-empty">Loading the board&hellip;</p>
  </div>
</section>

<script src="firebase-config.js"></script>
<script type="module" src="comments.js"></script>
'''
    return page("Trash Talk Board", "trash-talk.html", body, "Stat-backed trash talk and a live comment board for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# RULES
# ---------------------------------------------------------------
def build_rules():
    settings_rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in D.LEAGUE_SETTINGS)
    scoring_rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in D.SCORING)
    keeper_rule_rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in D.KEEPER_TRADE_RULES_2027)
    body = f'''
<section class="page-hero">
  <p class="eyebrow">Official</p>
  <h1>League Rules</h1>
  <p class="hero-sub">Straight from Yahoo's Scoring &amp; Settings page for League #40967, plus the league's own keeper and trade bylaws.</p>
</section>

<section class="section">
  <h2 class="section-title">Heads Up: Scoring Changes for 2026</h2>
  <p class="section-note">The commissioner made scoring changes on August 16, 2026 (check your email). The headline change: <strong>TE Premium is now on</strong> &mdash; tight ends score 1.5 pts per reception instead of the usual 1 pt. There were also a few defensive scoring tweaks, most notably <strong>sacks now worth 1.5 pts</strong> (up from 1). The full Scoring Settings table below reflects the current, up-to-date rules.</p>
</section>

<section class="section">
  <h2 class="section-title">League Settings</h2>
  <div class="table-wrap">
    <table class="data-table two-col"><tbody>{settings_rows}</tbody></table>
  </div>
</section>

<section class="section">
  <h2 class="section-title">Scoring Settings</h2>
  <div class="table-wrap">
    <table class="data-table two-col"><tbody>{scoring_rows}</tbody></table>
  </div>
</section>

<section class="section">
  <h2 class="section-title">Keeper &amp; Trade Rules <span class="eyebrow" style="display:inline-block;margin-left:8px;">Effective 2027</span></h2>
  <p class="section-note">Voted on by the league in 2026. These don't change anything about the upcoming 2026 draft &mdash; that's still 2 keepers per team under the existing rules. They kick in starting with the 2027 season. See the <a href="keepers.html">Keepers page</a> for how this affects each team's current keepers.</p>
  <div class="table-wrap">
    <table class="data-table two-col"><tbody>{keeper_rule_rows}</tbody></table>
  </div>
</section>
'''
    return page("League Rules", "rules.html", body, "Official rules, scoring settings, and keeper/trade bylaws for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# NEWSLETTER / RECAP
# ---------------------------------------------------------------
def compute_best_comeback():
    # Team with the biggest improvement from 1st-half (wks 1-7) win% to 2nd-half (wks 8-14) win%
    half1 = {}
    half2 = {}
    for w, games in D.WEEKLY_SCORES_2025.items():
        for a, sa, b, sb in games:
            bucket = half1 if w <= 7 else half2
            bucket.setdefault(a, [0, 0])
            bucket.setdefault(b, [0, 0])
            if sa > sb:
                bucket[a][0] += 1; bucket[b][1] += 1
            else:
                bucket[b][0] += 1; bucket[a][1] += 1
    best_team, best_delta, best_detail = None, -99, None
    for team in half1:
        w1, l1 = half1.get(team, [0, 0])
        w2, l2 = half2.get(team, [0, 0])
        pct1 = w1 / (w1 + l1) if (w1 + l1) else 0
        pct2 = w2 / (w2 + l2) if (w2 + l2) else 0
        delta = pct2 - pct1
        if delta > best_delta:
            best_team, best_delta, best_detail = team, delta, (w1, l1, w2, l2)
    return best_team, best_detail

def build_superlatives_section():
    champ_team, champ_mgr, champ_cur = D.CHAMPIONS_BY_MANAGER[2025]
    runner = next((t for y, p, t, m in D.PODIUM_FINISHES if y == 2025 and p == 2), None)
    runner_mgr = D.MANAGERS.get(runner, "")

    all_games = []
    for w, games in D.WEEKLY_SCORES_2025.items():
        for a, sa, b, sb in games:
            all_games.append((w, a, sa, b, sb))
    high = max(all_games, key=lambda g: max(g[2], g[4]))
    low = min(all_games, key=lambda g: min(g[2], g[4]))
    high_team, high_score = (high[1], high[2]) if high[2] > high[4] else (high[3], high[4])
    low_team, low_score = (low[1], low[2]) if low[2] < low[4] else (low[3], low[4])

    worst = D.STANDINGS_2025[-1]
    comeback_team, comeback_detail = compute_best_comeback()

    superlatives = [
        ("Champion", f'{champ_cur or champ_team} — {champ_mgr}'),
        ("Runner-Up", f'{runner} — {runner_mgr}'),
        ("Best Regular Season", f'Champ Scypher — Sadiq (14-0, league-best 2660.16 PF)'),
        ("Highest Single-Week Score", f'{fmt_score(high_score)} — {high_team} (Week {high[0]})'),
        ("Lowest Single-Week Score", f'{fmt_score(low_score)} — {low_team} (Week {low[0]})'),
        ("Best Second-Half Turnaround", f'{comeback_team} — {D.MANAGERS.get(comeback_team,"")} ({comeback_detail[0]}-{comeback_detail[1]} first half &rarr; {comeback_detail[2]}-{comeback_detail[3]} second half)' if comeback_team else "—"),
        ("Wall of Shame", f'{worst[1]} — {D.MANAGERS.get(worst[1],"")} ({worst[2]})'),
    ]
    sup_rows = "".join(f"<tr><td>{label}</td><td>{val}</td></tr>" for label, val in superlatives)

    # Custom awards - all derived from real STANDINGS_2025 columns (waiver $ left, moves)
    most_moves = max(D.STANDINGS_2025, key=lambda r: r[6])
    least_moves = min(D.STANDINGS_2025, key=lambda r: r[6])
    most_spent = min(D.STANDINGS_2025, key=lambda r: r[5])   # least waiver $ left = spent most
    least_spent = max(D.STANDINGS_2025, key=lambda r: r[5])  # most waiver $ left = spent least
    closest = min(all_games, key=lambda g: abs(g[2] - g[4]))
    blowout = max(all_games, key=lambda g: abs(g[2] - g[4]))

    awards = [
        ("The Waiver Wire Warrior Award", "Most roster moves", f'{most_moves[1]} — {D.MANAGERS.get(most_moves[1],"")} ({most_moves[6]} moves)'),
        ("The Set-It-And-Forget-It Award", "Fewest roster moves", f'{least_moves[1]} — {D.MANAGERS.get(least_moves[1],"")} ({least_moves[6]} moves)'),
        ("The Big Spender Award", "Most FAAB spent", f'{most_spent[1]} — {D.MANAGERS.get(most_spent[1],"")} (${100-most_spent[5] if most_spent[5]<=100 else 0} spent, ${most_spent[5]} left)'),
        ("The Tightwad Award", "Least FAAB spent", f'{least_spent[1]} — {D.MANAGERS.get(least_spent[1],"")} (${least_spent[5]} left unspent)'),
        ("The Nail-Biter Award", "Closest matchup of the season", f'{closest[1]} {fmt_score(closest[2])} &ndash; {fmt_score(closest[4])} {closest[3]} (Week {closest[0]}, margin {fmt_score(abs(closest[2]-closest[4]))})'),
        ("The Mercy Rule Award", "Biggest blowout of the season", f'{blowout[1]} {fmt_score(blowout[2])} &ndash; {fmt_score(blowout[4])} {blowout[3]} (Week {blowout[0]}, margin {fmt_score(abs(blowout[2]-blowout[4]))})'),
    ]
    award_rows = "".join(f"<tr><td>{name}<br><span class='table-footnote' style='margin:0'>{desc}</span></td><td>{val}</td></tr>" for name, desc, val in awards)

    return f'''
<section class="section">
  <h2 class="section-title">2025 Superlatives</h2>
  <div class="table-wrap">
    <table class="data-table two-col"><tbody>{sup_rows}</tbody></table>
  </div>
</section>

<section class="section">
  <h2 class="section-title">2025 League Awards</h2>
  <p class="section-note">Named for what earned the rep &mdash; every award below is tied to a real, verifiable 2025 stat.</p>
  <div class="table-wrap">
    <table class="data-table two-col"><tbody>{award_rows}</tbody></table>
  </div>
</section>
'''

def build_recap():
    body = f'''
<section class="page-hero">
  <p class="eyebrow">Issue #1</p>
  <h1>Weekly Recaps &amp; Newsletter</h1>
  <p class="hero-sub">A season-in-review to kick things off, plus a template ready for weekly 2026 recaps.</p>
</section>

<section class="section">
  <article class="newsletter-article">
    <h2>2025 Season Recap: The Closest Title Ever</h2>
    <p class="article-meta">Final Recap &middot; Published after Week 17</p>
    <p>The 2025 Low Ballerz season will be remembered for one number: <strong>0.48</strong>. That's the margin by which <strong>Mamba Mentality (kumail)</strong> beat <strong>Christian My Calf Hurt (Sarosh)</strong> in the championship &mdash; 141.56 to 141.08 &mdash; capping off the closest title game in recent memory.</p>
    <p>But the real story of the year belonged to <strong>Champ Scypher (Sadiq)</strong>, who authored the best regular season in franchise history at a perfect <strong>14-0</strong>, powered by a league-best 2660.16 points scored &mdash; including a 246.08-point explosion in Week 12, one of the biggest weeks of the season. As the #1 seed, Champ Scypher earned a bye into the semifinals... and lost to Mamba Mentality, the #4 seed, 204.02 to 182.94. A late run to the 3rd-place game salvaged some pride with a win over Hells Angels, but the undefeated season ended without a ring.</p>
    <p>Mamba Mentality's title run is the better story anyway: a 7-7 team that snuck into the playoffs as the 4-seed, upset the league's best regular-season team in the semifinal, then survived a photo finish in the championship. Total 2025 vindication for kumail.</p>
    <p>At the bottom of the standings, <strong>This hill I die on (wajahat z)</strong> endured a rough 3-11 season with the league's lowest scoring offense, while <strong>Chig-Chig Boom</strong> posted the season's single lowest score &mdash; a 74.98 disaster in Week 11.</p>
    <p>Now it's on to 2026. The draft went down on <strong>August 22</strong> &mdash; see the full results on <a href="draft.html">Draft Recap &amp; Grades</a> &mdash; and every team gets a clean slate. Except Scypher, who still has some explaining to do.</p>
  </article>

  <article class="newsletter-article template-card">
    <h2>Week 1, 2026 &mdash; Coming Soon</h2>
    <p class="article-meta">Template &middot; Ready to fill in once the season starts</p>
    <p>This slot is reserved for the first weekly recap of the 2026 season. After Week 1 wraps, drop in: top scorer of the week, biggest upset, closest matchup, waiver wire winners, and one bold prediction for Week 2.</p>
  </article>
</section>
{build_superlatives_section()}
'''
    return page("Newsletter", "recap.html", body, "Weekly recaps and season newsletter for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# MANAGERS
# ---------------------------------------------------------------
def build_managers():
    mgrs = list(D.CURRENT_TEAM_BY_MANAGER.keys())
    careers = [compute_manager_career(m) for m in mgrs]
    careers.sort(key=lambda c: (-c["titles"], -c["podiums_total"], c["row2025"][0] if c["row2025"] else 99))

    cards = ""
    for c in careers:
        team = c["team"]
        row = c["row2025"]
        rank_txt = ordinal(row[0]) if row else "—"
        rec_txt = row[2] if row else "—"
        trophies = TROPHY_SVG * c["titles"] if c["titles"] else '<span class="banner-mgr">Trophy case empty — for now</span>'
        keepers = D.KEEPERS_2026.get(team, [])
        keeper_txt = ", ".join(f"{p} (Rd {r})" for p, r in keepers) if keepers else "—"
        photo = D.MANAGER_PHOTOS.get(c["mgr"])
        if photo:
            avatar_html = f'<div class="manager-avatar has-photo"><img src="{photo}" alt="{c["mgr"]}" loading="lazy"></div>'
        else:
            avatar_html = f'<div class="manager-avatar">{initials(c["mgr"])}</div>'
        slug = mgr_slug(c["mgr"])
        cards += f'''
    <a class="manager-card" href="records.html#mgr-{slug}">
      <div class="manager-head">
        {avatar_html}
        <div>
          <h3>{c["mgr"]}</h3>
          <span class="manager-team">{team}</span>
        </div>
      </div>
      <div class="manager-trophy-case">{trophies}</div>
      <p class="manager-bio">{manager_bio(c)}</p>
      <div class="table-wrap">
        <table class="data-table two-col">
          <tbody>
            <tr><td>2025 Finish</td><td>{rank_txt} &middot; {rec_txt}</td></tr>
            <tr><td>Championships</td><td>{c["titles"]}</td></tr>
            <tr><td>Podium Finishes</td><td>{c["podiums_total"]} ({c["p1"]}-{c["p2"]}-{c["p3"]})</td></tr>
            <tr><td>2026 Keepers</td><td>{keeper_txt}</td></tr>
          </tbody>
        </table>
      </div>
      <span class="manager-card-cta">View full career record &rarr;</span>
    </a>'''

    body = f'''
<section class="page-hero">
  <p class="eyebrow">2026 Season</p>
  <h1>Managers</h1>
  <p class="hero-sub">Every current manager's trophy case and career highlights, based on real championship and podium data since 2011 plus the completed 2025 season.</p>
</section>
<section class="section">
  <div class="manager-grid">{cards}</div>
  <p class="table-footnote">Podium and championship counts are verified against Yahoo's manager records for 2011&ndash;2025 (2008&ndash;2010 identities are hidden by Yahoo's privacy settings on those old seasons and aren't included here). Full career win-loss records aren't shown yet &mdash; that requires pulling every season's complete standings, which is a future addition.</p>
</section>
'''
    return page("Managers", "managers.html", body, "Manager profile cards for the Low Ballerz fantasy football league — trophy cases, podiums and career highlights.")

# ---------------------------------------------------------------
# RECORDS (career highlights ledger)
# ---------------------------------------------------------------
def build_records():
    mgrs = list(D.CURRENT_TEAM_BY_MANAGER.keys())
    careers = [compute_manager_career(m) for m in mgrs]
    careers.sort(key=lambda c: -c["career_win_pct"])

    rows = ""
    for c in careers:
        row = c["row2025"]
        rank = row[0] if row else ""
        rec = row[2] if row else "—"
        pf = fmt_score(row[3]) if row else "—"
        career_rec = f'{c["career_w"]}-{c["career_l"]}' + (f'-{c["career_t"]}' if c["career_t"] else "")
        win_pct_str = f'{c["career_win_pct"]*100:.1f}%'
        first_year = c["career_first_year"] or "—"
        slug = mgr_slug(c["mgr"])
        rows += f'''
    <tr id="mgr-{slug}" data-titles="{c["titles"]}" data-podiums="{c["podiums_total"]}" data-rank2025="{rank or 99}" data-pf="{row[3] if row else 0}" data-careerw="{c["career_w"]}" data-careerl="{c["career_l"]}" data-winpct="{c["career_win_pct"]:.4f}" data-seasons="{c["career_seasons"]}">
      <td class="champ-cell">{c["mgr"]}</td>
      <td>{c["team"]}</td>
      <td>{career_rec}</td>
      <td>{win_pct_str}</td>
      <td>{c["career_seasons"]}</td>
      <td>{first_year}</td>
      <td>{c["titles"]}</td>
      <td>{c["p1"]}</td>
      <td>{c["p2"]}</td>
      <td>{c["p3"]}</td>
      <td>{c["podiums_total"]}</td>
      <td>{rec}</td>
      <td>{pf}</td>
      <td>{ordinal(rank) if row else "—"}</td>
    </tr>'''

    body = f'''
<section class="page-hero">
  <p class="eyebrow">Career Ledger</p>
  <h1>All-Time Records</h1>
  <p class="hero-sub">Career win-loss-tie totals, championships and podium finishes for every current manager, summed across every season they've actually been in the league &mdash; attributed by manager identity, not team name, since teams get renamed constantly. Click any column header to sort.</p>
</section>
<section class="section">
  <div class="table-wrap">
    <table class="data-table sortable" id="records-table">
      <thead>
        <tr>
          <th data-sort="text">Manager</th>
          <th data-sort="text">Current Team</th>
          <th data-sort="text" data-key="careerw">Career W-L(-T)</th>
          <th data-sort="num" data-key="winpct">Win %</th>
          <th data-sort="num" data-key="seasons">Seasons</th>
          <th data-sort="num">First Year</th>
          <th data-sort="num" data-key="titles">Titles</th>
          <th data-sort="num" data-key="p1">1st</th>
          <th data-sort="num" data-key="p2">2nd</th>
          <th data-sort="num" data-key="p3">3rd</th>
          <th data-sort="num" data-key="podiums">Total Podiums</th>
          <th data-sort="text">2025 Record</th>
          <th data-sort="num" data-key="pf">2025 PF</th>
          <th data-sort="num" data-key="rank2025">2025 Finish</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  </div>
  <p class="table-footnote">Career win-loss-tie totals pulled from Yahoo's final standings for every season 2008&ndash;2025 via the league's own season archive, and summed by manager identity (not team name &mdash; teams get renamed constantly, e.g. "Sahara and Sahil" was "Footballerz" through 2020, "Draft Party not on me" in 2023). 2008&ndash;2010 seasons aren't included in anyone's totals because Yahoo's privacy settings hide manager names on those old archived years, so there's no way to attribute them. "Seasons" and "First Year" reflect actual years on record, which isn't necessarily a consecutive run &mdash; a few managers had gaps (e.g. Sarosh was out of the league 2019&ndash;2021).</p>
</section>
'''
    return page("All-Time Records", "records.html", body, "Career win-loss-tie records, championships and podium finishes for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# RIVALRIES (2025 head-to-head)
# ---------------------------------------------------------------
def build_rivalries():
    # All-time grid (2011-2025), ordered by career win % (matches Records page ordering)
    h2h_all, mgrs_all = compute_h2h_alltime()
    careers = {m: compute_manager_career(m) for m in mgrs_all}
    order_all = sorted(mgrs_all, key=lambda m: -careers[m]["career_win_pct"])

    header_all = "<th>Manager</th>" + "".join(f'<th>{m}</th>' for m in order_all)
    body_rows_all = ""
    for row_mgr in order_all:
        cells = f'<td class="champ-cell">{row_mgr}</td>'
        for col_mgr in order_all:
            if row_mgr == col_mgr:
                cells += '<td>&mdash;</td>'
            else:
                w, l, t = h2h_all[row_mgr][col_mgr]
                if w == 0 and l == 0 and t == 0:
                    cells += '<td class="table-footnote">n/a</td>'
                elif t:
                    cells += f'<td>{w}-{l}-{t}</td>'
                else:
                    cells += f'<td>{w}-{l}</td>'
        body_rows_all += f'<tr>{cells}</tr>'

    # 2025-only grid (kept for reference), ordered by final 2025 standing
    h2h_25, mgrs_25 = compute_h2h_2025()
    order_25 = sorted(mgrs_25, key=lambda m: STANDINGS_BY_TEAM_2025.get(D.CURRENT_TEAM_BY_MANAGER[m], [99])[0])

    header_25 = "<th>Manager</th>" + "".join(f'<th>{m}</th>' for m in order_25)
    body_rows_25 = ""
    for row_mgr in order_25:
        cells = f'<td class="champ-cell">{row_mgr}</td>'
        for col_mgr in order_25:
            if row_mgr == col_mgr:
                cells += '<td>&mdash;</td>'
            else:
                w, l = h2h_25[row_mgr][col_mgr]
                if w == 0 and l == 0:
                    cells += '<td class="table-footnote">n/a</td>'
                else:
                    cells += f'<td>{w}-{l}</td>'
        body_rows_25 += f'<tr>{cells}</tr>'

    body = f'''
<section class="page-hero">
  <p class="eyebrow">2011&ndash;2025 &middot; 15 Seasons</p>
  <h1>Rivalries &mdash; Head-to-Head</h1>
  <p class="hero-sub">Every manager's all-time regular-season record against every other manager, pulled from real weekly matchup results across 15 archived seasons (749 qualifying games). Rows/columns are ordered by career win percentage. 2008&ndash;2010 aren't included &mdash; Yahoo hides manager identities on those archived seasons.</p>
</section>
<section class="section">
  <h2 class="section-title">All-Time (2011&ndash;2025)</h2>
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr>{header_all}</tr></thead>
      <tbody>{body_rows_all}</tbody>
    </table>
  </div>
  <p class="table-footnote">Read as row vs. column, formatted Wins-Losses (or Wins-Losses-Ties where relevant). "n/a" means those two managers have never faced each other &mdash; not every pair has overlapped in the league at the same time.</p>
</section>
<section class="section">
  <h2 class="section-title">2025 Regular Season Only</h2>
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr>{header_25}</tr></thead>
      <tbody>{body_rows_25}</tbody>
    </table>
  </div>
  <p class="table-footnote">Same read as above, scoped to just the completed 2025 regular season (12 teams, 14 weeks &mdash; not every pair meets in a single season).</p>
</section>
'''
    return page("Rivalries", "rivalries.html", body, "All-time (2011-2025) and 2025 head-to-head records between every manager in the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# DRAFT CENTRAL (live prep for the 2026 draft)
# ---------------------------------------------------------------
def build_draft_central():
    order_rows = ""
    for slot, team, mgr in D.DRAFT_ORDER_2026:
        order_rows += f'''
    <tr data-slot="{slot}" data-team="{team}" data-mgr="{mgr}">
      <td class="rank-cell">{slot}</td>
      <td>{team_pill(team)}</td>
    </tr>'''

    # Yahoo Top 200 pre-draft rankings, with the 24 keepers marked (off the board)
    keeper_owner = {}
    for team, keepers in D.KEEPERS_2026.items():
        for player, rnd in keepers:
            keeper_owner[player] = team
    rank_items = ""
    kept_count = 0
    for rank, player in D.YAHOO_RANKINGS_2026:
        team = keeper_owner.get(player)
        if team:
            kept_count += 1
            mgr = D.MANAGERS.get(team, "")
            rank_items += f'<span class="rank-item is-kept"><span class="rank-num">{rank}.</span><span class="rank-player">{player}</span><span class="rank-kept-tag">&nbsp;&middot; {mgr}</span></span>'
        else:
            rank_items += f'<span class="rank-item"><span class="rank-num">{rank}.</span><span class="rank-player">{player}</span></span>'

    # live draft board grid: 16 rounds x 12 slots, each cell synced via Firestore
    board_header = "<th>Rd</th>" + "".join(f'<th>{team.split()[0]}<br><small>{mgr.split()[0]}</small></th>' for slot, team, mgr in D.DRAFT_ORDER_2026)
    board_rows = ""
    for rnd in range(1, 17):
        cells = f"<td class='rank-cell'>{rnd}</td>"
        for slot, team, mgr in D.DRAFT_ORDER_2026:
            cell_id = f"r{rnd}_s{slot}"
            cells += f'<td><div class="draft-cell" contenteditable="true" data-cell-id="{cell_id}" data-placeholder="—"></div></td>'
        board_rows += f"<tr>{cells}</tr>"

    body = f'''
<section class="page-hero">
  <p class="eyebrow">2026 Draft &middot; Completed Saturday, August 22, 2026</p>
  <h1>Draft Central</h1>
  <p class="hero-sub">The 2026 draft is complete &mdash; the full live board below is the final record of every pick. Head to the <a href="draft.html">Draft Recap &amp; Grades</a> page for the round-by-round board and team-by-team grades.</p>
</section>

<section class="section">
  <div class="notice-card">
    <p><strong>Draft complete.</strong> All 16 rounds are locked in below, color-coded by position. See the <a href="draft.html">Draft Recap &amp; Grades</a> page for the clean round-by-round board and grades, or the <a href="keepers.html">Keepers page</a> for this year's keeper details.</p>
  </div>
</section>

<section class="section">
  <h2 class="section-title">Final Draft Order</h2>
  <div class="table-wrap">
    <table class="data-table" id="draft-order-table">
      <thead><tr><th>Pick</th><th>Manager</th></tr></thead>
      <tbody>{order_rows}</tbody>
    </table>
  </div>
</section>

<section class="section">
  <h2 class="section-title">Yahoo Pre-Draft Rankings &mdash; Top 200 (Archive)</h2>
  <p class="section-note">Yahoo's official pre-draft rankings, snapshotted before the draft &mdash; kept here for reference now that the draft is complete.</p>
  <p class="rank-legend"><span class="legend-dot"></span>Gold &middot; Manager = was a 2026 keeper ({kept_count} total) &mdash; locked in before the draft.</p>
  <div class="rank-list-wrap">
    <div class="rank-list">{rank_items}</div>
  </div>
  <p class="table-footnote">Source: Yahoo Fantasy Football's Top 200 Default Rankings (Standard), football.fantasysports.yahoo.com/f1/public_prerank, snapshotted August 17, 2026.</p>
</section>

<section class="section">
  <h2 class="section-title">Live Draft Board &mdash; Final Results</h2>
  <div id="draft-live-status" class="notice-card" style="display:none;"></div>
  <p class="section-note">The completed board, synced live during the draft. Still editable if a correction is ever needed. Snake order: even rounds reverse.</p>
  <div class="table-wrap">
    <table class="data-table draft-board-table">
      <thead><tr>{board_header}</tr></thead>
      <tbody>{board_rows}</tbody>
    </table>
  </div>
  <p class="pos-legend">
    <span><span class="pos-swatch pos-QB"></span>QB</span>
    <span><span class="pos-swatch pos-RB"></span>RB</span>
    <span><span class="pos-swatch pos-WR"></span>WR</span>
    <span><span class="pos-swatch pos-TE"></span>TE</span>
    <span><span class="pos-swatch pos-K"></span>K</span>
    <span><span class="pos-swatch pos-DEF"></span>DEF</span>
  </p>
  <p class="table-footnote">Cells auto-color by position as soon as a typed name matches a known 2026 player.</p>
</section>

<script>window.LOW_BALLERZ_PLAYER_POSITIONS = {json.dumps(D.PLAYER_POSITIONS)};</script>
<script src="firebase-config.js"></script>
<script type="module" src="draftboard.js"></script>
'''
    return page("Draft Central", "draft-central.html", body, "The completed 2026 draft board, final order and results for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# FUTURES & BALLOT
# ---------------------------------------------------------------
def build_futures():
    odds_list = compute_futures()
    odds_rows = ""
    for mgr, team, prob, odds, c in odds_list:
        odds_rows += f'''
    <tr>
      <td class="champ-cell">{mgr}</td>
      <td>{team}</td>
      <td>{odds}</td>
      <td>{manager_bio(c)}</td>
    </tr>'''

    body = f'''
<section class="page-hero">
  <p class="eyebrow">2026 Preseason &middot; For Fun Only</p>
  <h1>Futures &amp; Ballot</h1>
  <p class="hero-sub">Championship odds computed from real career data (titles, podiums, 2025 finish) &mdash; not a sportsbook, just bragging-rights math. Cast your predictions below and see everyone else's live.</p>
</section>

<section class="section">
  <h2 class="section-title">2026 Championship Odds</h2>
  <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>Manager</th><th>Team</th><th>Odds</th><th>Why</th></tr></thead>
      <tbody>{odds_rows}</tbody>
    </table>
  </div>
  <p class="table-footnote">Odds formula: 3 points per title + 1 point per career podium finish + a bonus for 2025 finish, converted to implied probability then American odds format. Purely for fun.</p>
</section>

<section class="section">
  <h2 class="section-title">Predictions Ballot</h2>
  <p class="section-note">Submit your picks now that rosters are set &mdash; everyone's predictions show up live below.</p>

  <div id="predictions-live-status" class="notice-card" style="display:none;"></div>

  <form id="predictions-form" class="talk-form">
    <input id="pred-name" class="talk-input" type="text" maxlength="40" placeholder="Your name" required>
    <input id="pred-champion" class="talk-input" type="text" maxlength="60" placeholder="Predicted 2026 Champion" required>
    <input id="pred-lastplace" class="talk-input" type="text" maxlength="60" placeholder="Predicted Last Place (Wall of Shame)" required>
    <textarea id="pred-bold" class="talk-textarea" maxlength="400" rows="3" placeholder="One bold prediction for 2026..." required></textarea>
    <button type="submit" class="btn btn-gold talk-submit">Lock In My Picks</button>
  </form>

  <div id="predictions-feed" class="talk-feed">
    <p class="talk-empty">Loading predictions&hellip;</p>
  </div>
</section>

<script src="firebase-config.js"></script>
<script type="module" src="predictions.js"></script>
'''
    return page("Futures & Ballot", "futures.html", body, "2026 championship odds and league predictions ballot for the Low Ballerz fantasy football league.")

# ---------------------------------------------------------------
# TRADE NEWSLETTER
# ---------------------------------------------------------------
def hist_team_pill(year, team):
    mgr = D.TRADE_TEAM_MANAGERS.get(year, {}).get(team, "")
    return f'<span class="team-pill">{team}<small>{mgr}</small></span>'

def grade_badge_class(grade):
    if grade == "VETOED":
        return "grade-badge grade-veto badge-wide"
    if grade == "—" or grade == "-":
        return "grade-badge grade-na"
    return f"grade-badge grade-{grade[0].lower()}"

def fmt_trade_date(iso_date):
    y, m, d = iso_date.split("-")
    months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{months[int(m)]} {int(d)}, {y}"

def build_trades():
    years = sorted(D.TRADES_LOG.keys(), reverse=True)
    total_trades = sum(len(v) for v in D.TRADES_LOG.values())
    total_vetoed = sum(1 for v in D.TRADES_LOG.values() for t in v if t.get("vetoed"))

    sections = ""
    for year in years:
        trades = D.TRADES_LOG[year]
        cards = ""
        for t in trades:
            veto = t.get("vetoed", False)
            side_html = ""
            for side in t["sides"]:
                gets = ", ".join(side["gets"])
                side_html += f'''
        <div class="trade-side">
          <div class="trade-side-team">{hist_team_pill(year, side["team"])}</div>
          <div class="trade-side-gets"><span class="trade-gets-label">Receives</span>{gets}</div>
        </div>'''
            card_cls = "trade-card vetoed" if veto else "trade-card"
            badge_cls = grade_badge_class(t["grade"])
            cards += f'''
    <div class="{card_cls}">
      <div class="trade-card-top">
        <span class="trade-date">{fmt_trade_date(t["date"])}{' &middot; VETOED' if veto else ''}</span>
        <div class="{badge_cls}">{t["grade"]}</div>
      </div>
      <div class="trade-sides">{side_html}
        <div class="trade-side-arrow">&#8646;</div>
      </div>
      <p class="trade-verdict">{t["verdict"]}</p>
    </div>'''
        sections += f'''
<section class="section">
  <h2 class="section-title">{year} Season</h2>
  <div class="grade-list">{cards}
  </div>
</section>'''

    body = f'''
<section class="page-hero">
  <p class="eyebrow">2021&ndash;2025 &middot; {total_trades} Trades &middot; {total_vetoed} Vetoed</p>
  <h1>Trade Newsletter</h1>
  <p class="hero-sub">Every trade the league has made over the last five seasons (2021-2025), pulled directly from Yahoo's archived season pages. Grades and verdicts below are the site's own retrospective commentary, judged with the benefit of hindsight on how each deal actually played out. Vetoed trades are shown grayed out and ungraded.</p>
</section>
{sections}
'''
    return page("Trade Newsletter", "trades.html", body, "Every Low Ballerz fantasy football trade from 2021-2025, graded with hindsight.")

# ---------------------------------------------------------------

PAGES = {
    "index.html": build_index,
    "standings.html": build_standings,
    "scores.html": build_scores,
    "power-rankings.html": build_power_rankings,
    "history.html": build_history,
    "managers.html": build_managers,
    "records.html": build_records,
    "rivalries.html": build_rivalries,
    "draft-central.html": build_draft_central,
    "draft.html": build_draft,
    "keepers.html": build_keepers,
    "trades.html": build_trades,
    "trash-talk.html": build_trash_talk,
    "futures.html": build_futures,
    "rules.html": build_rules,
    "recap.html": build_recap,
}

for fname, fn in PAGES.items():
    html = fn()
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", fname, len(html), "bytes")
