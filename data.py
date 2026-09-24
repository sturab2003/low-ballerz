# Real data pulled from Yahoo Fantasy Football - Low Ballerz (League ID# 40967 / iaba_ballers)

# Real photos for manager cards, keyed by manager name (matches CURRENT_TEAM_BY_MANAGER
# keys). Falls back to the initials avatar on the Managers page for anyone not listed here.
MANAGER_PHOTOS = {
    "Turab": "assets/turab.jpg",
}

MANAGERS = {
    "Ali Khalid LLC": "wiseonekms",
    "Chig-Chig Boom": "Hassnain",
    "Christian My Calf Hurt": "Sarosh",
    "Hakka PUKA!!": "Parvez",
    "Hells Angels": "omar",
    "Hurts My Brain": "Hussain",
    "Mamba Mentality": "kumail",
    "Sahara and Sahil": "Meisam",
    "Champ Scypher": "Sadiq",
    "Tera Boutte Mein Danda": "Ilyas",
    "This hill I die on": "wajahat z",
    "You're Ma Nanga Guy": "Turab",
    # 2026-season renames (kept alongside the old names above so historical pages
    # showing the pre-rename team name still resolve to the right manager).
    "Scypher": "Sadiq",
    "Philly Illy": "Ilyas",
    "Immaculate Concepcion": "Hassnain",
    "Chase the Baker Ladd!": "Turab",
    # Additional 2026 in-season renames, confirmed directly against Yahoo's
    # Managers page (football.fantasysports.yahoo.com/f1/40967/teams) on 2026-09-15.
    "Hakka PUKA!! Jr Jr": "Parvez",
    "Reed A (little) Mor": "wajahat z",
    "Rico Suave": "Hussain",
}

# Career win-loss-tie totals per manager, summed across every season each
# manager has actually been in the league (attributed by manager identity,
# not team name, since team names get renamed/rebranded constantly). Pulled
# from Yahoo's final standings for every season 2008-2025 via the league's
# season-archive selector. 2008-2010 seasons have no recoverable manager
# names (Yahoo privacy settings hide them on those old archived seasons) so
# they aren't included in anyone's totals below. first_year/last_year mark
# the first and most recent season on record for that manager (last_year is
# 2025 for everyone currently active; it is NOT necessarily an indicator
# they've played every year in between - see individual gaps, e.g. Sarosh
# was out of the league 2019-2021).
CAREER_RECORDS = {
    "Turab": {"W": 116, "L": 84, "T": 0, "seasons": 15, "first_year": 2011, "last_year": 2025},
    "Meisam": {"W": 115, "L": 85, "T": 0, "seasons": 15, "first_year": 2011, "last_year": 2025},
    "omar": {"W": 88, "L": 111, "T": 1, "seasons": 15, "first_year": 2011, "last_year": 2025},
    "Hussain": {"W": 86, "L": 75, "T": 0, "seasons": 12, "first_year": 2014, "last_year": 2025},
    "wiseonekms": {"W": 66, "L": 69, "T": 0, "seasons": 10, "first_year": 2016, "last_year": 2025},
    "Ilyas": {"W": 101, "L": 86, "T": 0, "seasons": 14, "first_year": 2012, "last_year": 2025},
    "Sadiq": {"W": 115, "L": 85, "T": 0, "seasons": 15, "first_year": 2011, "last_year": 2025},
    "kumail": {"W": 111, "L": 89, "T": 0, "seasons": 15, "first_year": 2011, "last_year": 2025},
    "Hassnain": {"W": 58, "L": 51, "T": 0, "seasons": 8, "first_year": 2018, "last_year": 2025},
    "Parvez": {"W": 37, "L": 59, "T": 0, "seasons": 7, "first_year": 2019, "last_year": 2025},
    "wajahat z": {"W": 40, "L": 69, "T": 0, "seasons": 8, "first_year": 2018, "last_year": 2025},
    "Sarosh": {"W": 23, "L": 46, "T": 0, "seasons": 5, "first_year": 2018, "last_year": 2025},
}

# All-time head-to-head tallies among the 12 current managers, regular season
# 2011-2025 (2008-2010 excluded: Yahoo hides all manager names on those
# archived seasons, so no attribution is possible). Pulled directly from
# every season's weekly matchup pages via the league's season-archive
# selector - one full pass over every regular-season week for every manager
# pairing where BOTH sides are among today's 12 managers (games against
# departed/former members are excluded since this is a head-to-head grid of
# current managers only). 749 total qualifying games across 15 seasons.
# key: (mgrA, mgrB) alphabetically sorted; value: {w1: mgrA's wins, w2: mgrB's wins, ties: ties}
ALL_TIME_H2H = {
    ('Hassnain', 'Hussain'): {'w1': 9, 'w2': 5, 'ties': 0},
    ('Hassnain', 'Ilyas'): {'w1': 4, 'w2': 7, 'ties': 0},
    ('Hassnain', 'Meisam'): {'w1': 3, 'w2': 6, 'ties': 0},
    ('Hassnain', 'Parvez'): {'w1': 5, 'w2': 2, 'ties': 0},
    ('Hassnain', 'Sadiq'): {'w1': 4, 'w2': 5, 'ties': 0},
    ('Hassnain', 'Sarosh'): {'w1': 4, 'w2': 3, 'ties': 0},
    ('Hassnain', 'Turab'): {'w1': 5, 'w2': 4, 'ties': 0},
    ('Hassnain', 'kumail'): {'w1': 3, 'w2': 7, 'ties': 0},
    ('Hassnain', 'omar'): {'w1': 4, 'w2': 5, 'ties': 0},
    ('Hassnain', 'wajahat z'): {'w1': 5, 'w2': 4, 'ties': 0},
    ('Hassnain', 'wiseonekms'): {'w1': 8, 'w2': 2, 'ties': 0},
    ('Hussain', 'Ilyas'): {'w1': 8, 'w2': 4, 'ties': 0},
    ('Hussain', 'Meisam'): {'w1': 6, 'w2': 5, 'ties': 0},
    ('Hussain', 'Parvez'): {'w1': 8, 'w2': 0, 'ties': 0},
    ('Hussain', 'Sadiq'): {'w1': 4, 'w2': 11, 'ties': 0},
    ('Hussain', 'Sarosh'): {'w1': 4, 'w2': 1, 'ties': 0},
    ('Hussain', 'Turab'): {'w1': 2, 'w2': 11, 'ties': 0},
    ('Hussain', 'kumail'): {'w1': 10, 'w2': 6, 'ties': 0},
    ('Hussain', 'omar'): {'w1': 6, 'w2': 9, 'ties': 0},
    ('Hussain', 'wajahat z'): {'w1': 7, 'w2': 3, 'ties': 0},
    ('Hussain', 'wiseonekms'): {'w1': 5, 'w2': 7, 'ties': 0},
    ('Ilyas', 'Meisam'): {'w1': 9, 'w2': 10, 'ties': 0},
    ('Ilyas', 'Parvez'): {'w1': 4, 'w2': 4, 'ties': 0},
    ('Ilyas', 'Sadiq'): {'w1': 9, 'w2': 7, 'ties': 0},
    ('Ilyas', 'Sarosh'): {'w1': 3, 'w2': 2, 'ties': 0},
    ('Ilyas', 'Turab'): {'w1': 8, 'w2': 6, 'ties': 0},
    ('Ilyas', 'kumail'): {'w1': 7, 'w2': 10, 'ties': 0},
    ('Ilyas', 'omar'): {'w1': 10, 'w2': 9, 'ties': 0},
    ('Ilyas', 'wajahat z'): {'w1': 8, 'w2': 1, 'ties': 0},
    ('Ilyas', 'wiseonekms'): {'w1': 8, 'w2': 6, 'ties': 0},
    ('Meisam', 'Parvez'): {'w1': 7, 'w2': 2, 'ties': 0},
    ('Meisam', 'Sadiq'): {'w1': 11, 'w2': 8, 'ties': 0},
    ('Meisam', 'Sarosh'): {'w1': 6, 'w2': 1, 'ties': 0},
    ('Meisam', 'Turab'): {'w1': 8, 'w2': 12, 'ties': 0},
    ('Meisam', 'kumail'): {'w1': 7, 'w2': 10, 'ties': 0},
    ('Meisam', 'omar'): {'w1': 13, 'w2': 5, 'ties': 0},
    ('Meisam', 'wajahat z'): {'w1': 7, 'w2': 3, 'ties': 0},
    ('Meisam', 'wiseonekms'): {'w1': 7, 'w2': 6, 'ties': 0},
    ('Parvez', 'Sadiq'): {'w1': 2, 'w2': 7, 'ties': 0},
    ('Parvez', 'Sarosh'): {'w1': 5, 'w2': 1, 'ties': 0},
    ('Parvez', 'Turab'): {'w1': 5, 'w2': 4, 'ties': 0},
    ('Parvez', 'kumail'): {'w1': 4, 'w2': 6, 'ties': 0},
    ('Parvez', 'omar'): {'w1': 5, 'w2': 3, 'ties': 0},
    ('Parvez', 'wajahat z'): {'w1': 5, 'w2': 5, 'ties': 0},
    ('Parvez', 'wiseonekms'): {'w1': 3, 'w2': 5, 'ties': 0},
    ('Sadiq', 'Sarosh'): {'w1': 3, 'w2': 3, 'ties': 0},
    ('Sadiq', 'Turab'): {'w1': 7, 'w2': 11, 'ties': 0},
    ('Sadiq', 'kumail'): {'w1': 11, 'w2': 8, 'ties': 0},
    ('Sadiq', 'omar'): {'w1': 14, 'w2': 6, 'ties': 0},
    ('Sadiq', 'wajahat z'): {'w1': 4, 'w2': 5, 'ties': 0},
    ('Sadiq', 'wiseonekms'): {'w1': 7, 'w2': 4, 'ties': 0},
    ('Sarosh', 'Turab'): {'w1': 1, 'w2': 3, 'ties': 0},
    ('Sarosh', 'kumail'): {'w1': 0, 'w2': 5, 'ties': 0},
    ('Sarosh', 'omar'): {'w1': 3, 'w2': 3, 'ties': 0},
    ('Sarosh', 'wajahat z'): {'w1': 3, 'w2': 4, 'ties': 0},
    ('Sarosh', 'wiseonekms'): {'w1': 5, 'w2': 3, 'ties': 0},
    ('Turab', 'kumail'): {'w1': 10, 'w2': 6, 'ties': 0},
    ('Turab', 'omar'): {'w1': 8, 'w2': 9, 'ties': 0},
    ('Turab', 'wajahat z'): {'w1': 5, 'w2': 3, 'ties': 0},
    ('Turab', 'wiseonekms'): {'w1': 5, 'w2': 5, 'ties': 0},
    ('kumail', 'omar'): {'w1': 9, 'w2': 10, 'ties': 0},
    ('kumail', 'wajahat z'): {'w1': 10, 'w2': 1, 'ties': 0},
    ('kumail', 'wiseonekms'): {'w1': 4, 'w2': 7, 'ties': 0},
    ('omar', 'wajahat z'): {'w1': 5, 'w2': 4, 'ties': 0},
    ('omar', 'wiseonekms'): {'w1': 4, 'w2': 6, 'ties': 0},
    ('wajahat z', 'wiseonekms'): {'w1': 4, 'w2': 6, 'ties': 0},
}

# 2025 final standings (post-playoffs), rank order
STANDINGS_2025 = [
    # rank, team, record, PF, PA, waiver_left, moves
    (1, "Mamba Mentality", "7-7-0", 2378.32, 2354.16, 0, 18),
    (2, "Christian My Calf Hurt", "7-7-0", 2239.66, 2251.52, 6, 45),
    (3, "Champ Scypher", "14-0-0", 2660.16, 2100.72, 1, 44),
    (4, "Hells Angels", "9-5-0", 2369.38, 2068.40, 55, 12),
    (5, "Hakka PUKA!!", "7-7-0", 2337.56, 2257.82, 0, 44),
    (6, "Sahara and Sahil", "9-5-0", 2359.34, 2031.44, 4, 78),
    (7, "This hill I die on", "3-11-0", 2026.46, 2480.28, 6, 36),
    (8, "Hurts My Brain", "5-9-0", 2180.62, 2392.00, 26, 22),
    (9, "Chig-Chig Boom", "7-7-0", 2048.02, 2209.64, 24, 23),
    (10, "You're Ma Nanga Guy", "6-8-0", 2258.72, 2337.22, 2, 56),
    (11, "Ali Khalid LLC", "5-9-0", 2112.20, 2366.34, 70, 11),
    (12, "Tera Boutte Mein Danda", "5-9-0", 2339.14, 2460.04, 0, 34),
]

PLAYOFF_SEEDS_2025 = [
    (1, "Champ Scypher"), (2, "Hells Angels"), (3, "Sahara and Sahil"),
    (4, "Mamba Mentality"), (5, "Hakka PUKA!!"), (6, "Christian My Calf Hurt"),
]

PLAYOFF_BRACKET_2025 = {
    "Quarterfinals (Week 15)": [
        ("Champ Scypher", None, "BYE", None),
        ("Hells Angels", None, "BYE", None),
        ("Mamba Mentality", 162.40, "Hakka PUKA!!", 126.34),
        ("Christian My Calf Hurt", 161.92, "Sahara and Sahil", 139.30),
    ],
    "Semifinals (Week 16)": [
        ("Mamba Mentality", 204.02, "Champ Scypher", 182.94),
        ("Christian My Calf Hurt", 200.66, "Hells Angels", 165.08),
    ],
    "5th Place Game (Week 16)": [
        ("Hakka PUKA!!", 195.30, "Sahara and Sahil", 155.80),
    ],
    "Championship (Week 17)": [
        ("Mamba Mentality", 141.56, "Christian My Calf Hurt", 141.08),
    ],
    "3rd Place Game (Week 17)": [
        ("Champ Scypher", 134.60, "Hells Angels", 92.76),
    ],
}

WEEKLY_SCORES_2025 = {
    1: [
        ("You're Ma Nanga Guy", 136.32, "Mamba Mentality", 136.12),
        ("Champ Scypher", 198.46, "Hurts My Brain", 171.12),
        ("Christian My Calf Hurt", 150.72, "Chig-Chig Boom", 122.14),
        ("Hakka PUKA!!", 191.84, "This hill I die on", 111.80),
        ("Hells Angels", 139.12, "Tera Boutte Mein Danda", 191.16),
        ("Ali Khalid LLC", 176.90, "Sahara and Sahil", 163.96),
    ],
    2: [
        ("You're Ma Nanga Guy", 123.92, "Champ Scypher", 154.04),
        ("Christian My Calf Hurt", 249.36, "Ali Khalid LLC", 169.88),
        ("Hakka PUKA!!", 168.88, "Mamba Mentality", 138.80),
        ("Hells Angels", 200.24, "Hurts My Brain", 101.08),
        ("Tera Boutte Mein Danda", 171.00, "Chig-Chig Boom", 145.72),
        ("Sahara and Sahil", 198.78, "This hill I die on", 184.64),
    ],
    3: [
        ("You're Ma Nanga Guy", 134.60, "Hells Angels", 163.92),
        ("Champ Scypher", 159.22, "Mamba Mentality", 142.28),
        ("Christian My Calf Hurt", 143.28, "This hill I die on", 123.88),
        ("Hakka PUKA!!", 127.00, "Sahara and Sahil", 167.44),
        ("Hurts My Brain", 155.66, "Chig-Chig Boom", 198.62),
        ("Ali Khalid LLC", 129.74, "Tera Boutte Mein Danda", 202.54),
    ],
    4: [
        ("You're Ma Nanga Guy", 188.28, "Chig-Chig Boom", 202.22),
        ("Champ Scypher", 209.36, "Hakka PUKA!!", 191.56),
        ("Christian My Calf Hurt", 144.18, "Sahara and Sahil", 176.36),
        ("Hells Angels", 181.20, "Mamba Mentality", 178.58),
        ("Hurts My Brain", 173.54, "Ali Khalid LLC", 167.24),
        ("Tera Boutte Mein Danda", 153.06, "This hill I die on", 159.62),
    ],
    5: [
        ("You're Ma Nanga Guy", 194.70, "Ali Khalid LLC", 210.76),
        ("Champ Scypher", 172.64, "Hells Angels", 130.56),
        ("Christian My Calf Hurt", 188.52, "Hakka PUKA!!", 159.58),
        ("Hurts My Brain", 187.88, "This hill I die on", 130.20),
        ("Tera Boutte Mein Danda", 182.38, "Sahara and Sahil", 216.24),
        ("Mamba Mentality", 189.04, "Chig-Chig Boom", 169.20),
    ],
    6: [
        ("You're Ma Nanga Guy", 188.72, "This hill I die on", 127.78),
        ("Champ Scypher", 182.36, "Chig-Chig Boom", 111.48),
        ("Christian My Calf Hurt", 180.44, "Tera Boutte Mein Danda", 138.88),
        ("Hakka PUKA!!", 155.70, "Hells Angels", 145.04),
        ("Hurts My Brain", 136.38, "Sahara and Sahil", 200.92),
        ("Ali Khalid LLC", 197.70, "Mamba Mentality", 205.80),
    ],
    7: [
        ("You're Ma Nanga Guy", 183.80, "Sahara and Sahil", 170.50),
        ("Champ Scypher", 176.18, "Ali Khalid LLC", 137.28),
        ("Christian My Calf Hurt", 127.54, "Hurts My Brain", 177.40),
        ("Hakka PUKA!!", 204.34, "Tera Boutte Mein Danda", 186.20),
        ("Hells Angels", 190.68, "Chig-Chig Boom", 194.84),
        ("Mamba Mentality", 156.18, "This hill I die on", 131.72),
    ],
    8: [
        ("You're Ma Nanga Guy", 145.28, "Christian My Calf Hurt", 144.24),
        ("Champ Scypher", 188.98, "This hill I die on", 153.54),
        ("Hakka PUKA!!", 146.78, "Chig-Chig Boom", 210.54),
        ("Hells Angels", 168.32, "Ali Khalid LLC", 124.38),
        ("Hurts My Brain", 216.40, "Tera Boutte Mein Danda", 156.82),
        ("Mamba Mentality", 113.80, "Sahara and Sahil", 139.56),
    ],
    9: [
        ("You're Ma Nanga Guy", 204.90, "Tera Boutte Mein Danda", 195.06),
        ("Champ Scypher", 142.12, "Sahara and Sahil", 139.44),
        ("Christian My Calf Hurt", 181.70, "Mamba Mentality", 219.74),
        ("Hakka PUKA!!", 161.82, "Hurts My Brain", 181.64),
        ("Hells Angels", 235.24, "This hill I die on", 142.46),
        ("Ali Khalid LLC", 85.92, "Chig-Chig Boom", 86.56),
    ],
    10: [
        ("You're Ma Nanga Guy", 173.92, "Hurts My Brain", 114.82),
        ("Champ Scypher", 242.58, "Christian My Calf Hurt", 168.08),
        ("Hakka PUKA!!", 146.42, "Ali Khalid LLC", 143.06),
        ("Hells Angels", 178.60, "Sahara and Sahil", 148.60),
        ("Tera Boutte Mein Danda", 198.32, "Mamba Mentality", 180.74),
        ("Chig-Chig Boom", 211.06, "This hill I die on", 133.24),
    ],
    11: [
        ("You're Ma Nanga Guy", 135.96, "Hakka PUKA!!", 183.86),
        ("Champ Scypher", 211.42, "Tera Boutte Mein Danda", 137.74),
        ("Christian My Calf Hurt", 126.10, "Hells Angels", 116.56),
        ("Hurts My Brain", 144.50, "Mamba Mentality", 170.34),
        ("Ali Khalid LLC", 155.48, "This hill I die on", 148.22),
        ("Chig-Chig Boom", 74.98, "Sahara and Sahil", 194.98),
    ],
    12: [
        ("You're Ma Nanga Guy", 156.34, "Mamba Mentality", 197.14),
        ("Champ Scypher", 246.08, "Hurts My Brain", 173.28),
        ("Christian My Calf Hurt", 165.50, "Chig-Chig Boom", 98.40),
        ("Hakka PUKA!!", 152.90, "This hill I die on", 154.06),
        ("Hells Angels", 202.84, "Tera Boutte Mein Danda", 115.98),
        ("Ali Khalid LLC", 97.00, "Sahara and Sahil", 174.80),
    ],
    13: [
        ("You're Ma Nanga Guy", 158.04, "Champ Scypher", 170.82),
        ("Christian My Calf Hurt", 122.84, "Ali Khalid LLC", 161.92),
        ("Hakka PUKA!!", 183.60, "Mamba Mentality", 187.36),
        ("Hells Angels", 151.12, "Hurts My Brain", 148.34),
        ("Tera Boutte Mein Danda", 156.90, "Chig-Chig Boom", 113.58),
        ("Sahara and Sahil", 169.72, "This hill I die on", 126.38),
    ],
    14: [
        ("You're Ma Nanga Guy", 133.94, "Hells Angels", 165.94),
        ("Champ Scypher", 205.90, "Mamba Mentality", 162.40),
        ("Christian My Calf Hurt", 147.16, "This hill I die on", 198.92),
        ("Hakka PUKA!!", 163.28, "Sahara and Sahil", 98.04),
        ("Hurts My Brain", 98.58, "Chig-Chig Boom", 108.68),
        ("Ali Khalid LLC", 154.94, "Tera Boutte Mein Danda", 153.10),
    ],
}

# 2026 in-season weekly scores, built up week by week from Yahoo's live matchup
# pages (football.fantasysports.yahoo.com/f1/40967/matchup?week=N) as each week
# finalizes. Same format as WEEKLY_SCORES_2025: (teamA, scoreA, teamB, scoreB).
WEEKLY_SCORES_2026 = {
    1: [
        ("Chase the Baker Ladd!", 164.94, "Immaculate Concepcion", 96.68),
        ("Scypher", 249.70, "Sahara and Sahil", 238.88),
        ("Ali Khalid LLC", 191.62, "Rico Suave", 152.16),
        ("Hells Angels", 180.98, "Christian My Calf Hurt", 165.82),
        ("Mamba Mentality", 196.28, "Hakka PUKA!! Jr Jr", 149.46),
        ("Reed A (little) Mor", 206.56, "Philly Illy", 162.22),
    ],
    2: [
        ("Chase the Baker Ladd!", 195.14, "Scypher", 157.38),
        ("Ali Khalid LLC", 144.58, "Reed A (little) Mor", 134.46),
        ("Immaculate Concepcion", 156.54, "Christian My Calf Hurt", 184.06),
        ("Hakka PUKA!! Jr Jr", 150.42, "Sahara and Sahil", 203.34),
        ("Hells Angels", 201.80, "Philly Illy", 114.80),
        ("Rico Suave", 177.56, "Mamba Mentality", 150.58),
    ],
}

# 2026 in-season standings, updated weekly from Yahoo's Standings module
# (football.fantasysports.yahoo.com/f1/40967). Same format as STANDINGS_2025:
# (rank, team, record, PF, PA, waiver_left, moves). waiver_left is FAAB $ left
# of the $100 season budget. Refreshed 2026-09-23 after Week 2 finalized
# (Yahoo "Last standings update: Wed Sep 23 01:45am CDT").
STANDINGS_2026 = [
    (1, "Hells Angels", "2-0-0", 382.78, 280.62, 100, 2),
    (2, "Chase the Baker Ladd!", "2-0-0", 360.08, 254.06, 95, 9),
    (3, "Ali Khalid LLC", "2-0-0", 336.20, 286.62, 80, 3),
    (4, "Sahara and Sahil", "1-1-0", 442.22, 400.12, 92, 26),
    (5, "Scypher", "1-1-0", 407.08, 434.02, 85, 11),
    (6, "Christian My Calf Hurt", "1-1-0", 349.88, 337.52, 93, 7),
    (7, "Mamba Mentality", "1-1-0", 346.86, 327.02, 100, 5),
    (8, "Reed A (little) Mor", "1-1-0", 341.02, 306.80, 71, 10),
    (9, "Rico Suave", "1-1-0", 329.72, 342.20, 100, 2),
    (10, "Hakka PUKA!! Jr Jr", "0-2-0", 299.88, 399.62, 70, 1),
    (11, "Philly Illy", "0-2-0", 277.02, 408.36, 71, 26),
    (12, "Immaculate Concepcion", "0-2-0", 253.22, 349.00, 81, 2),
]

ALL_TIME = [
    (2025, "Mamba Mentality", "Christian My Calf Hurt", "Champ Scypher", "10th"),
    (2024, "Scypher", "Sahara and Sahil", "Love Thy Naber", "4th"),
    (2023, "Hurts My Brain", "TLaw & Order", "Waji", "2nd"),
    (2022, "Mamba Mentality", "Vez", "Footballerz", "9th"),
    (2021, "Dalvin and the Chipmunks", "Scypher", "KSolo", "6th"),
    (2020, "The Dynasty", "King of the JuJu's", "Philly Illy", "6th"),
    (2019, "The Champion", "Footballerz", "HereComesRetirement", "3rd"),
    (2018, "KSolo", "Philly Illy", "Footballerz", "4th"),
    (2017, "Scypher = poop", "Brady's Revenge", "Philly Illy", "2nd"),
    (2016, "Scypher", "Footballerz", "Brady's Revenge", "3rd"),
    (2015, "Brady's Revenge", "Hussain's Team", "Texans Revolution", "1st"),
    (2014, "Hussain's Team", "Hells Angels", "KSolo", "12th"),
    (2013, "Texans Revolution", "Footballerz", "Bushleague", "3rd"),
    (2012, "Wheeling and Dealing", "Texans Revolution", "BeastModeUnleashed", "3rd"),
    (2011, "The footballerz 1", "The Sadiqs", "Junglees", "3rd"),
    (2010, "Bombay Baby Bandits", "NothingButHeart", "2 Legit", "--"),
    (2009, "comebackidz", "DemBoysGotHeat", "Rizvi14", "--"),
    (2008, "txns 4 AFC", "NothingbutHeart", "The Sadiqs", "--"),
]

# Every current manager's true final placement (post-playoff, including
# consolation-bracket results) for every season 2011-2025. Pulled directly
# from each archived season's Standings module on Yahoo (the "Rank" column,
# which reflects the actual final order after every playoff/consolation
# game -- not just regular-season record). 2008-2010 excluded: Yahoo hides
# manager identities on those archived seasons. A manager only appears in a
# given year's dict if they were actually in the league that year -- see
# CAREER_RECORDS above for each manager's first_year, and note Sarosh was
# out of the league 2019-2021. Cross-validated against every year's "Turab's
# Finish" value already stored in ALL_TIME above -- all 15 years matched
# exactly with zero discrepancies.
# key: year; value: {manager: final_rank (1-12)}
ALL_TIME_FINISHES = {
    2025: {"kumail": 1, "Sarosh": 2, "Sadiq": 3, "omar": 4, "Parvez": 5, "Meisam": 6,
           "wajahat z": 7, "Hussain": 8, "Hassnain": 9, "Turab": 10, "wiseonekms": 11, "Ilyas": 12},
    2024: {"Sadiq": 1, "Meisam": 2, "Ilyas": 3, "Turab": 4, "wiseonekms": 5, "kumail": 6,
           "Parvez": 7, "omar": 8, "Hussain": 9, "wajahat z": 10, "Hassnain": 11, "Sarosh": 12},
    2023: {"Hussain": 1, "Turab": 2, "wajahat z": 3, "Ilyas": 4, "kumail": 5, "Hassnain": 6,
           "Parvez": 7, "Meisam": 8, "omar": 9, "wiseonekms": 10, "Sadiq": 11, "Sarosh": 12},
    2022: {"kumail": 1, "Parvez": 2, "Meisam": 3, "Hassnain": 4, "Hussain": 5, "Ilyas": 6,
           "Sarosh": 7, "wiseonekms": 8, "Turab": 9, "Sadiq": 10, "wajahat z": 11, "omar": 12},
    2021: {"Hassnain": 1, "Sadiq": 2, "wiseonekms": 3, "kumail": 4, "Ilyas": 5, "Turab": 6,
           "Parvez": 7, "Hussain": 8, "omar": 9, "Meisam": 10, "wajahat z": 12},
    2020: {"Hassnain": 2, "Ilyas": 3, "Hussain": 4, "Sadiq": 5, "Turab": 6, "Meisam": 7,
           "wiseonekms": 8, "kumail": 9, "omar": 10, "Parvez": 11, "wajahat z": 12},
    2019: {"Meisam": 2, "Turab": 3, "omar": 4, "kumail": 5, "wajahat z": 6, "Sadiq": 7,
           "Ilyas": 8, "Hussain": 9, "Parvez": 10, "wiseonekms": 11, "Hassnain": 12},
    2018: {"wiseonekms": 1, "Ilyas": 2, "Meisam": 3, "Turab": 4, "Hussain": 5, "omar": 6,
           "Sarosh": 7, "wajahat z": 8, "Hassnain": 10, "Sadiq": 11, "kumail": 12},
    2017: {"Turab": 2, "Ilyas": 3, "wiseonekms": 4, "Sadiq": 5, "kumail": 6, "Meisam": 7,
           "omar": 8, "Hussain": 9},
    2016: {"Sadiq": 1, "Meisam": 2, "Turab": 3, "Hussain": 5, "Ilyas": 7, "omar": 8,
           "kumail": 9, "wiseonekms": 11},
    2015: {"Turab": 1, "Hussain": 2, "kumail": 3, "Sadiq": 4, "Meisam": 6, "Ilyas": 10, "omar": 12},
    2014: {"Hussain": 1, "omar": 2, "Ilyas": 5, "kumail": 7, "Sadiq": 8, "Meisam": 9, "Turab": 12},
    2013: {"kumail": 1, "Meisam": 2, "Turab": 3, "Ilyas": 5, "Sadiq": 10, "omar": 11},
    2012: {"Meisam": 1, "kumail": 2, "Turab": 3, "Ilyas": 5, "Sadiq": 10, "omar": 11},
    2011: {"Meisam": 1, "Sadiq": 2, "Turab": 3, "kumail": 6, "omar": 11},
}

DRAFT_2025 = {
1: [("Ashton Jeanty","Mamba Mentality"),("Jahmyr Gibbs","Champ Scypher"),("Saquon Barkley","This hill I die on"),("Derrick Henry","Hurts My Brain"),("CeeDee Lamb","Hakka PUKA!!"),("Lamar Jackson","Tera Boutte Mein Danda"),("Nico Collins","Hells Angels"),("Bijan Robinson","Ali Khalid LLC"),("Malik Nabers","Sahara and Sahil"),("Jonathan Taylor","Chig-Chig Boom"),("Christian McCaffrey","Christian My Calf Hurt"),("Drake London","You're Ma Nanga Guy")],
2: [("Chase Brown","You're Ma Nanga Guy"),("Amon-Ra St. Brown","Christian My Calf Hurt"),("Omarion Hampton","Chig-Chig Boom"),("A.J. Brown","Sahara and Sahil"),("Ladd McConkey","Ali Khalid LLC"),("Josh Jacobs","Hells Angels"),("Terry McLaurin","Tera Boutte Mein Danda"),("Jayden Daniels","Hakka PUKA!!"),("Breece Hall","Hurts My Brain"),("Kenneth Walker III","This hill I die on"),("Josh Allen","Champ Scypher"),("Marvin Harrison Jr.","Mamba Mentality")],
3: [("Tee Higgins","Mamba Mentality"),("Jaxon Smith-Njigba","Champ Scypher"),("Tyreek Hill","This hill I die on"),("Bo Nix","Hurts My Brain"),("Justin Herbert","Hakka PUKA!!"),("Trey McBride","Tera Boutte Mein Danda"),("Davante Adams","Hells Angels"),("Mike Evans","Ali Khalid LLC"),("Alvin Kamara","Sahara and Sahil"),("DeVonta Smith","Chig-Chig Boom"),("Jaylen Waddle","Christian My Calf Hurt"),("Dak Prescott","You're Ma Nanga Guy")],
4: [("TreVeyon Henderson","You're Ma Nanga Guy"),("Jameson Williams","Christian My Calf Hurt"),("Courtland Sutton","Chig-Chig Boom"),("Tetairoa McMillan","Sahara and Sahil"),("Baker Mayfield","Ali Khalid LLC"),("James Cook III","Hells Angels"),("Tony Pollard","Tera Boutte Mein Danda"),("Isiah Pacheco","Hakka PUKA!!"),("Xavier Worthy","Hurts My Brain"),("Brock Purdy","This hill I die on"),("James Conner","Champ Scypher"),("Kyler Murray","Mamba Mentality")],
5: [("George Pickens","Mamba Mentality"),("George Kittle","Champ Scypher"),("RJ Harvey","This hill I die on"),("Jalen Hurts","Hurts My Brain"),("DK Metcalf","Hakka PUKA!!"),("Emeka Egbuka","Tera Boutte Mein Danda"),("J.J. McCarthy","Hells Angels"),("D'Andre Swift","Ali Khalid LLC"),("Drake Maye","Sahara and Sahil"),("Joe Burrow","Chig-Chig Boom"),("Travis Etienne Jr.","Christian My Calf Hurt"),("Patrick Mahomes","You're Ma Nanga Guy")],
6: [("Travis Hunter","You're Ma Nanga Guy"),("Mark Andrews","Christian My Calf Hurt"),("Ricky Pearsall","Chig-Chig Boom"),("Justin Fields","Sahara and Sahil"),("Zay Flowers","Ali Khalid LLC"),("T.J. Hockenson","Hells Angels"),("Ja'Marr Chase","Tera Boutte Mein Danda"),("Cam Ward","Hakka PUKA!!"),("DJ Moore","Hurts My Brain"),("Jayden Reed","This hill I die on"),("Jerry Jeudy","Champ Scypher"),("Travis Kelce","Mamba Mentality")],
7: [("Rashee Rice","Mamba Mentality"),("Calvin Ridley","Champ Scypher"),("Trevor Lawrence","This hill I die on"),("Stefon Diggs","Hurts My Brain"),("Kaleb Johnson","Hakka PUKA!!"),("Caleb Williams","Tera Boutte Mein Danda"),("Tyrone Tracy Jr.","Hells Angels"),("Sam LaPorta","Ali Khalid LLC"),("Tyler Warren","Sahara and Sahil"),("Tucker Kraft","Chig-Chig Boom"),("Jared Goff","Christian My Calf Hurt"),("Jordan Mason","You're Ma Nanga Guy")],
8: [("Matthew Golden","You're Ma Nanga Guy"),("Rome Odunze","Christian My Calf Hurt"),("Rashid Shaheed","Chig-Chig Boom"),("Aaron Jones Sr.","Sahara and Sahil"),("Jaylen Warren","Ali Khalid LLC"),("Michael Pittman Jr.","Hells Angels"),("Jacory Croskey-Merritt","Tera Boutte Mein Danda"),("Jakobi Meyers","Hakka PUKA!!"),("David Montgomery","Hurts My Brain"),("Brian Thomas Jr.","This hill I die on"),("Bryce Young","Champ Scypher"),("Sam Darnold","Mamba Mentality")],
9: [("Chris Olave","Mamba Mentality"),("Deebo Samuel Sr.","Champ Scypher"),("Chris Godwin Jr.","This hill I die on"),("Tua Tagovailoa","Hurts My Brain"),("Brian Robinson","Hakka PUKA!!"),("Michael Penix Jr.","Tera Boutte Mein Danda"),("Matthew Stafford","Hells Angels"),("Nick Chubb","Ali Khalid LLC"),("Zach Charbonnet","Sahara and Sahil"),("Eagles","Chig-Chig Boom"),("Evan Engram","Christian My Calf Hurt"),("David Njoku","You're Ma Nanga Guy")],
10: [("Geno Smith","You're Ma Nanga Guy"),("Packers","Christian My Calf Hurt"),("C.J. Stroud","Chig-Chig Boom"),("Jauan Jennings","Sahara and Sahil"),("Cooper Kupp","Ali Khalid LLC"),("Darnell Mooney","Hells Angels"),("Jaxson Dart","Tera Boutte Mein Danda"),("J.K. Dobbins","Hakka PUKA!!"),("Jordan Addison","Hurts My Brain"),("Christian Kirk","This hill I die on"),("Khalil Shakir","Champ Scypher"),("Austin Ekeler","Mamba Mentality")],
11: [("Spencer Rattler","Mamba Mentality"),("Aaron Rodgers","Champ Scypher"),("Zach Ertz","This hill I die on"),("Josh Downs","Hurts My Brain"),("Dalton Kincaid","Hakka PUKA!!"),("Keon Coleman","Tera Boutte Mein Danda"),("Keenan Allen","Hells Angels"),("Javonte Williams","Ali Khalid LLC"),("Bhayshul Tuten","Sahara and Sahil"),("Braelon Allen","Chig-Chig Boom"),("Russell Wilson","Christian My Calf Hurt"),("Rhamondre Stevenson","You're Ma Nanga Guy")],
12: [("Joe Flacco","You're Ma Nanga Guy"),("Rachaad White","Christian My Calf Hurt"),("Rashod Bateman","Chig-Chig Boom"),("Chuba Hubbard","Sahara and Sahil"),("Jake Ferguson","Ali Khalid LLC"),("Wan'Dale Robinson","Hells Angels"),("Dylan Sampson","Tera Boutte Mein Danda"),("Cam Skattebo","Hakka PUKA!!"),("Brock Bowers","Hurts My Brain"),("Amari Cooper","This hill I die on"),("De'Von Achane","Champ Scypher"),("Steelers","Mamba Mentality")],
13: [("Raheem Mostert","Mamba Mentality"),("Trey Benson","Champ Scypher"),("Tre' Harris","This hill I die on"),("Colston Loveland","Hurts My Brain"),("Marvin Mims Jr.","Hakka PUKA!!"),("Tank Bigsby","Tera Boutte Mein Danda"),("Ravens","Hells Angels"),("Jayden Higgins","Ali Khalid LLC"),("Garrett Wilson","Sahara and Sahil"),("Cedric Tillman","Chig-Chig Boom"),("Najee Harris","Christian My Calf Hurt"),("Ollie Gordon II","You're Ma Nanga Guy")],
14: [("Justin Jefferson","You're Ma Nanga Guy"),("Romeo Doubs","Christian My Calf Hurt"),("Chig Okonkwo","Chig-Chig Boom"),("Daniel Jones","Sahara and Sahil"),("Tyler Allgeier","Ali Khalid LLC"),("Ray Davis","Hells Angels"),("Brandon Aiyuk","Tera Boutte Mein Danda"),("Hunter Henry","Hakka PUKA!!"),("Joshua Palmer","Hurts My Brain"),("Shedeur Sanders","This hill I die on"),("Kyle Pitts Sr.","Champ Scypher"),("Blake Corum","Mamba Mentality")],
15: [("Dallas Goedert","Mamba Mentality"),("Roschon Johnson","Champ Scypher"),("Laviska Shenault Jr.","This hill I die on"),("DeMario Douglas","Hurts My Brain"),("Puka Nacua","Hakka PUKA!!"),("Broncos","Tera Boutte Mein Danda"),("Darren Waller","Hells Angels"),("Dolphins","Ali Khalid LLC"),("Jaydon Blue","Sahara and Sahil"),("Lions","Chig-Chig Boom"),("Chris Rodriguez Jr.","Christian My Calf Hurt"),("Anthony Richardson Sr.","You're Ma Nanga Guy")],
16: [("Brenton Strange","You're Ma Nanga Guy"),("Xavier Legette","Christian My Calf Hurt"),("Rico Dowdle","Chig-Chig Boom"),("Joe Mixon","Sahara and Sahil"),("Jordan Love","Ali Khalid LLC"),("Hollywood Brown","Hells Angels"),("Bucky Irving","Tera Boutte Mein Danda"),("Texans","Hakka PUKA!!"),("Chiefs","Hurts My Brain"),("Vikings","This hill I die on"),("Bills","Champ Scypher"),("Kyren Williams","Mamba Mentality")],
}

# The real 2026 draft, scraped from Yahoo's draftresults page immediately after the
# live draft on August 22, 2026 (16 rounds, snake order, pick order preserved within
# each round). Team names reflect each manager's 2026 rebrand where applicable
# (e.g. "Champ Scypher" -> "Scypher"). Keepers appear at their locked-in round/team.
DRAFT_2026 = {
1: [("Ashton Jeanty","Mamba Mentality"),("Lamar Jackson","This hill I die on"),("Ja'Marr Chase","Hakka PUKA!!"),("Jaxon Smith-Njigba","Hells Angels"),("Josh Allen","Sahara and Sahil"),("Joe Burrow","Hurts My Brain"),("Bijan Robinson","Ali Khalid LLC"),("Jahmyr Gibbs","Scypher"),("CeeDee Lamb","Philly Illy"),("Christian McCaffrey","Christian My Calf Hurt"),("Jonathan Taylor","Immaculate Concepcion"),("Chase Brown","Chase the Baker Ladd!")],
2: [("Omarion Hampton","Chase the Baker Ladd!"),("Saquon Barkley","Immaculate Concepcion"),("Jalen Hurts","Christian My Calf Hurt"),("A.J. Brown","Philly Illy"),("Nico Collins","Scypher"),("Drake London","Ali Khalid LLC"),("Rashee Rice","Hurts My Brain"),("Kenneth Walker III","Sahara and Sahil"),("Josh Jacobs","Hells Angels"),("Jayden Daniels","Hakka PUKA!!"),("Amon-Ra St. Brown","This hill I die on"),("Jeremiyah Love","Mamba Mentality")],
3: [("Malik Nabers","Mamba Mentality"),("Derrick Henry","This hill I die on"),("Kyren Williams","Hakka PUKA!!"),("Trey McBride","Hells Angels"),("Breece Hall","Sahara and Sahil"),("DeVonta Smith","Hurts My Brain"),("Colston Loveland","Ali Khalid LLC"),("Zay Flowers","Scypher"),("Justin Herbert","Philly Illy"),("Tee Higgins","Christian My Calf Hurt"),("Jaylen Waddle","Immaculate Concepcion"),("Dak Prescott","Chase the Baker Ladd!")],
4: [("Ladd McConkey","Chase the Baker Ladd!"),("Terry McLaurin","Immaculate Concepcion"),("Travis Kelce","Christian My Calf Hurt"),("Javonte Williams","Philly Illy"),("Jaxson Dart","Scypher"),("David Montgomery","Ali Khalid LLC"),("Tetairoa McMillan","Hurts My Brain"),("Tyler Warren","Sahara and Sahil"),("James Cook III","Hells Angels"),("Brock Purdy","Hakka PUKA!!"),("TreVeyon Henderson","This hill I die on"),("Patrick Mahomes","Mamba Mentality")],
5: [("George Pickens","Mamba Mentality"),("Luther Burden III","This hill I die on"),("Travis Etienne Jr.","Hakka PUKA!!"),("Bo Nix","Hells Angels"),("Drake Maye","Sahara and Sahil"),("Matthew Stafford","Hurts My Brain"),("Jameson Williams","Ali Khalid LLC"),("D'Andre Swift","Scypher"),("Emeka Egbuka","Philly Illy"),("Bucky Irving","Christian My Calf Hurt"),("Sam LaPorta","Immaculate Concepcion"),("Davante Adams","Chase the Baker Ladd!")],
6: [("Tucker Kraft","Chase the Baker Ladd!"),("Kyler Murray","Immaculate Concepcion"),("Mike Evans","Christian My Calf Hurt"),("DJ Moore","Philly Illy"),("Carnell Tate","Scypher"),("Jared Goff","Ali Khalid LLC"),("Christian Watson","Hurts My Brain"),("Parker Washington","Sahara and Sahil"),("DK Metcalf","Hells Angels"),("Marvin Harrison Jr.","Hakka PUKA!!"),("Jaylen Warren","This hill I die on"),("Michael Wilson","Mamba Mentality")],
7: [("Sam Darnold","Mamba Mentality"),("Trevor Lawrence","This hill I die on"),("Brian Thomas Jr.","Hakka PUKA!!"),("Texans","Hells Angels"),("Chris Godwin Jr.","Sahara and Sahil"),("Bhayshul Tuten","Hurts My Brain"),("Jadarian Price","Ali Khalid LLC"),("Harold Fannin Jr.","Scypher"),("Caleb Williams","Philly Illy"),("Stefon Diggs","Christian My Calf Hurt"),("Jonathon Brooks","Immaculate Concepcion"),("Michael Pittman Jr.","Chase the Baker Ladd!")],
8: [("Baker Mayfield","Chase the Baker Ladd!"),("Tony Pollard","Immaculate Concepcion"),("Rome Odunze","Christian My Calf Hurt"),("Kyle Pitts Sr.","Philly Illy"),("Tyler Shough","Scypher"),("Tank Dell","Ali Khalid LLC"),("Rico Dowdle","Hurts My Brain"),("Josh Downs","Sahara and Sahil"),("Rhamondre Stevenson","Hells Angels"),("Dalton Kincaid","Hakka PUKA!!"),("Jayden Reed","This hill I die on"),("Blake Corum","Mamba Mentality")],
9: [("Chris Olave","Mamba Mentality"),("Mark Andrews","This hill I die on"),("Chuba Hubbard","Hakka PUKA!!"),("Xavier Worthy","Hells Angels"),("Daniel Jones","Sahara and Sahil"),("Malik Willis","Hurts My Brain"),("Fernando Mendoza","Ali Khalid LLC"),("Alec Pierce","Scypher"),("De'Zhaun Stribling","Philly Illy"),("J.K. Dobbins","Christian My Calf Hurt"),("Jordan Addison","Immaculate Concepcion"),("George Kittle","Chase the Baker Ladd!")],
10: [("Jacoby Brissett","Chase the Baker Ladd!"),("C.J. Stroud","Immaculate Concepcion"),("Courtland Sutton","Christian My Calf Hurt"),("Rachaad White","Philly Illy"),("Jacory Croskey-Merritt","Scypher"),("Quentin Johnston","Ali Khalid LLC"),("Jordan Mason","Hurts My Brain"),("Kyle Monangai","Sahara and Sahil"),("Bryce Young","Hells Angels"),("Dallas Goedert","Hakka PUKA!!"),("Cam Ward","This hill I die on"),("Juwan Johnson","Mamba Mentality")],
11: [("Carson Beck","Mamba Mentality"),("Wan'Dale Robinson","This hill I die on"),("RJ Harvey","Hakka PUKA!!"),("Jakobi Meyers","Hells Angels"),("Malik Washington","Sahara and Sahil"),("Cam Skattebo","Hurts My Brain"),("Jalen Coker","Ali Khalid LLC"),("Isaiah Likely","Scypher"),("Kenny Gainwell","Philly Illy"),("Matthew Golden","Christian My Calf Hurt"),("Aaron Jones Sr.","Immaculate Concepcion"),("Makai Lemon","Chase the Baker Ladd!")],
12: [("Jordyn Tyson","Chase the Baker Ladd!"),("KC Concepcion","Immaculate Concepcion"),("Romeo Doubs","Christian My Calf Hurt"),("Dylan Sampson","Philly Illy"),("De'Von Achane","Scypher"),("Chig Okonkwo","Ali Khalid LLC"),("Brock Bowers","Hurts My Brain"),("Keaton Mitchell","Sahara and Sahil"),("Khalil Shakir","Hells Angels"),("Broncos","Hakka PUKA!!"),("Eagles","This hill I die on"),("Mike Washington Jr.","Mamba Mentality")],
13: [("Tyler Allgeier","Mamba Mentality"),("Rashid Shaheed","This hill I die on"),("Aaron Rodgers","Hakka PUKA!!"),("Jake Ferguson","Hells Angels"),("Garrett Wilson","Sahara and Sahil"),("Denzel Boston","Hurts My Brain"),("Brian Robinson","Ali Khalid LLC"),("Jalen Nailor","Scypher"),("Jonah Coleman","Philly Illy"),("Chris Rodriguez Jr.","Christian My Calf Hurt"),("Deebo Samuel Sr.","Immaculate Concepcion"),("Keenan Allen","Chase the Baker Ladd!")],
14: [("Justin Jefferson","Chase the Baker Ladd!"),("Hunter Henry","Immaculate Concepcion"),("Geno Smith","Christian My Calf Hurt"),("Rams","Philly Illy"),("Tyrone Tracy Jr.","Scypher"),("Omar Cooper Jr.","Ali Khalid LLC"),("Woody Marks","Hurts My Brain"),("Tre Tucker","Sahara and Sahil"),("Kirk Cousins","Hells Angels"),("Tyjae Spears","Hakka PUKA!!"),("Brenton Strange","This hill I die on"),("Seahawks","Mamba Mentality")],
15: [("Zach Charbonnet","Mamba Mentality"),("Tank Bigsby","This hill I die on"),("Puka Nacua","Hakka PUKA!!"),("Patriots","Hells Angels"),("Braelon Allen","Sahara and Sahil"),("Adonai Mitchell","Hurts My Brain"),("Bills","Ali Khalid LLC"),("Tua Tagovailoa","Scypher"),("Dalton Schultz","Philly Illy"),("Vikings","Christian My Calf Hurt"),("Chargers","Immaculate Concepcion"),("Greg Dulcich","Chase the Baker Ladd!")],
16: [("Quinshon Judkins","Chase the Baker Ladd!"),("Shedeur Sanders","Immaculate Concepcion"),("AJ Barner","Christian My Calf Hurt"),("MarShawn Lloyd","Philly Illy"),("Jaguars","Scypher"),("Jordan Love","Ali Khalid LLC"),("Ravens","Hurts My Brain"),("Alvin Kamara","Sahara and Sahil"),("Isiah Pacheco","Hells Angels"),("T.J. Hockenson","Hakka PUKA!!"),("Isaac TeSlaa","This hill I die on"),("Travis Hunter","Mamba Mentality")],
}

LEAGUE_SETTINGS = [
    ("League ID", "40967"),
    ("Custom URL", "football.fantasysports.yahoo.com/league/iaba_ballers"),
    ("Founded", "2008 (18th season in 2026)"),
    ("Teams", "12"),
    ("Draft Type", "Live Standard Draft"),
    ("2026 Draft Time", "Saturday, August 22, 2026 - 10:00pm CDT"),
    ("Draft Pick Clock", "1 minute, 30 seconds"),
    ("Keepers", "2 per team through the 2026 draft; 3 per team starting 2027 (see Keeper &amp; Trade Rules below)"),
    ("Scoring Type", "Head-to-Head, Full PPR (1 pt/reception, 1.5 pts/reception for TEs &mdash; TE Premium, new for 2026)"),
    ("Regular Season", "Weeks 1-14"),
    ("Playoffs", "6 teams - Weeks 15, 16 & 17"),
    ("Playoff Tiebreaker", "Best regular season record vs. opponent"),
    ("Divisions", "None"),
    ("Waivers", "FAAB bidding &mdash; $100 budget per team for the full season, $0 bids allowed, weekly rolling standings tiebreak, processes Tuesdays"),
    ("Trade Review", "Commissioner review, 1-day reject window"),
    ("Trade Deadline", "November 28 (last week of the regular season) &mdash; see Keeper &amp; Trade Rules below for what's still allowed after"),
    ("Roster", "QB, WR, WR, WR, RB, RB, TE, W/T, Q/W/R/T, DEF, BN x6, IR"),
    ("Commissioner", "Sadiq (Scypher)"),
    ("Asst. Commissioners", "Turab (Chase the Baker Ladd!), Meisam (Sahara and Sahil)"),
    ("Last-Place Punishment", "Buys the group food at next year's draft party"),
]

# Keeper & trade bylaws effective starting the 2027 season (posted 2026).
# These are league-specific rules the managers agreed to, distinct from the
# Yahoo platform settings above.
KEEPER_TRADE_RULES_2027 = [
    ("Keeper Count", "3 keepers per team, up from 2 &mdash; effective the 2027 draft."),
    ("Max Keeper Years", "A player can be kept for a maximum of 2 years. Starting in 2027, any player already kept 2+ years becomes a free agent."),
    ("Keeper Cost", "Round drafted minus 1 round &mdash; effective 2027."),
    ("2nd-Year Keeper Restrictions", "A 2nd-year keeper can't be kept again or traded for next-season purposes. It can only be traded in-season."),
    ("In-Season Trade Cutoff", "No in-season trades are allowed after the last week of the regular season."),
    ("Post-Season Trade Window", "After the regular season ends, only keeper trades and draft pick trades are allowed."),
    ("Draft Pick Trading", "Draft picks can't be traded for in-season purposes &mdash; only for keepers or other draft picks, for next season."),
    ("Keeper Year Transition", "1st-year keepers become 2nd-year keepers after the last week of the regular season's Monday Night Football game."),
    ("Keeper Deadline Changes", "Once the keeper deadline passes, changes are only allowed if a keeper gets injured. No changes are allowed within 2 hours of the draft."),
]

# Pulled directly from Yahoo's Scoring & Settings page (football.fantasysports.yahoo.com/f1/40967/settings)
# on 2026-08-17, after the commissioner's rule-change email the night before. Two confirmed changes from
# that email: TE Premium (1.5 pts/reception for TEs, up from the standard 1 pt) and Sack value increased
# to 1.5 pts (up from 1 pt). The rest of the table below is the full current settings, not all of which
# were previously documented on this site.
SCORING = [
    ("Passing Yards", "25 yds/pt (+2 at 300, +3 at 350, +4 at 400 yds)"),
    ("Passing Touchdowns", "6 pts"),
    ("Interceptions Thrown", "-2 pts"),
    ("Rushing Attempts", "0.5 pts"),
    ("Rushing Yards", "10 yds/pt (+3 at 100, +4 at 150, +5 at 200 yds)"),
    ("Rushing Touchdowns", "6 pts"),
    ("Receptions (QB/RB/WR)", "1 pt (Full PPR)"),
    ("Receptions (TE)", "1.5 pts &mdash; TE Premium, new for 2026"),
    ("Receiving Yards", "10 yds/pt (+3 at 100, +4 at 150, +5 at 200 yds)"),
    ("Receiving Touchdowns", "6 pts"),
    ("Return Touchdowns", "6 pts"),
    ("2-Point Conversions", "2 pts"),
    ("Fumbles Lost", "-2 pts"),
    ("Offensive Fumble Return TD", "6 pts"),
    ("Pick Sixes Thrown", "-3 pts"),
    ("40+ Yard Bonuses", "+1 completion, +2 passing TD, +2 run, +3 rushing TD, +1 reception, +2 receiving TD"),
    ("Sack (DEF)", "1.5 pts &mdash; up from 1 pt for 2026"),
    ("Interception (DEF)", "3 pts"),
    ("Fumble Recovery (DEF)", "2 pts"),
    ("Defensive/Return Touchdown", "6 pts"),
    ("Safety", "4 pts"),
    ("Blocked Kick", "3 pts"),
    ("Kickoff/Punt Return Touchdown", "8 pts"),
    ("Points Allowed", "7-13: -1, 14-20: -2, 21-27: -3, 28-34: -4, 35+: -5"),
    ("4th Down Stops", "1 pt"),
    ("Tackles for Loss", "0.5 pts"),
    ("Yards Allowed (DEF)", "300-399: -2, 400-499: -3, 500+: -5"),
    ("Three-and-Outs Forced", "0.5 pts"),
]

# 2026 Draft order (custom order set by commissioner) and keepers
# format: (draft_slot, team, manager)
DRAFT_ORDER_2026 = [
    (1, "Mamba Mentality", "kumail"),
    (2, "This hill I die on", "wajahat z"),
    (3, "Hakka PUKA!!", "Parvez"),
    (4, "Hells Angels", "omar"),
    (5, "Sahara and Sahil", "Meisam"),
    (6, "Hurts My Brain", "Hussain"),
    (7, "Ali Khalid LLC", "wiseonekms (Khasim)"),
    (8, "Scypher", "Sadiq"),
    (9, "Philly Illy", "Ilyas"),
    (10, "Christian My Calf Hurt", "Sarosh"),
    (11, "Immaculate Concepcion", "Hasnain"),
    (12, "Chase the Baker Ladd!", "Turab"),
]

# format: team -> [(player, round_cost), (player, round_cost)]
KEEPERS_2026 = {
    "Scypher": [("Jahmyr Gibbs", 1), ("De'Von Achane", 12)],
    "Mamba Mentality": [("Chris Olave", 9), ("George Pickens", 5)],
    "Sahara and Sahil": [("Drake Maye", 5), ("Garrett Wilson", 13)],
    "This hill I die on": [("Amon-Ra St. Brown", 2), ("Trevor Lawrence", 7)],
    "Philly Illy": [("Emeka Egbuka", 5), ("Caleb Williams", 7)],
    "Chase the Baker Ladd!": [("Justin Jefferson", 14), ("Quinshon Judkins", 16)],
    "Hurts My Brain": [("Brock Bowers", 12), ("Cam Skattebo", 11)],
    "Hells Angels": [("James Cook III", 4), ("Josh Jacobs", 2)],
    "Ali Khalid LLC": [("Jordan Love", 16), ("Bijan Robinson", 1)],
    "Christian My Calf Hurt": [("Christian McCaffrey", 1), ("Rome Odunze", 8)],
    "Immaculate Concepcion": [("Jonathan Taylor", 1), ("C.J. Stroud", 10)],
    "Hakka PUKA!!": [("Puka Nacua", 15), ("Jayden Daniels", 2)],
}

# Yahoo's official Top 200 Default Pre-Draft Rankings (Standard scoring), pulled
# directly from football.fantasysports.yahoo.com/f1/public_prerank on 2026-08-17.
# format: (rank, player_name)
YAHOO_RANKINGS_2026 = [
    (1, "Josh Allen"), (2, "Jahmyr Gibbs"), (3, "Bijan Robinson"), (4, "Jayden Daniels"),
    (5, "Joe Burrow"), (6, "Dak Prescott"), (7, "Jalen Hurts"), (8, "Lamar Jackson"),
    (9, "Drake Maye"), (10, "Ja'Marr Chase"), (11, "Jaxson Dart"), (12, "Trevor Lawrence"),
    (13, "Patrick Mahomes"), (14, "Jared Goff"), (15, "Christian McCaffrey"), (16, "Caleb Williams"),
    (17, "Justin Herbert"), (18, "Puka Nacua"), (19, "Bo Nix"), (20, "Jonathan Taylor"),
    (21, "Jordan Love"), (22, "Brock Purdy"), (23, "Amon-Ra St. Brown"), (24, "Matthew Stafford"),
    (25, "Kyler Murray"), (26, "Malik Willis"), (27, "C.J. Stroud"), (28, "Daniel Jones"),
    (29, "Baker Mayfield"), (30, "Tyler Shough"), (31, "Jaxon Smith-Njigba"), (32, "Sam Darnold"),
    (33, "De'Von Achane"), (34, "James Cook III"), (35, "CeeDee Lamb"), (36, "Derrick Henry"),
    (37, "Justin Jefferson"), (38, "Drake London"), (39, "Aaron Rodgers"), (40, "Bryce Young"),
    (41, "Cam Ward"), (42, "Chase Brown"), (43, "George Pickens"), (44, "Saquon Barkley"),
    (45, "Kenneth Walker III"), (46, "Josh Jacobs"), (47, "Ashton Jeanty"), (48, "Omarion Hampton"),
    (49, "Jacoby Brissett"), (50, "Jeremiyah Love"), (51, "Kyren Williams"), (52, "Geno Smith"),
    (53, "Tee Higgins"), (54, "Nico Collins"), (55, "Javonte Williams"), (56, "Zay Flowers"),
    (57, "A.J. Brown"), (58, "Breece Hall"), (59, "Rashee Rice"), (60, "Cam Skattebo"),
    (61, "Chris Olave"), (62, "Fernando Mendoza"), (63, "Trey McBride"), (64, "DeVonta Smith"),
    (65, "Terry McLaurin"), (66, "David Montgomery"), (67, "Travis Etienne Jr."), (68, "D'Andre Swift"),
    (69, "TreVeyon Henderson"), (70, "Tetairoa McMillan"), (71, "Brock Bowers"), (72, "Davante Adams"),
    (73, "Malik Nabers"), (74, "Jaylen Waddle"), (75, "Jaylen Warren"), (76, "Bucky Irving"),
    (77, "Alec Pierce"), (78, "Luther Burden III"), (79, "Jameson Williams"), (80, "Garrett Wilson"),
    (81, "Quinshon Judkins"), (82, "Chuba Hubbard"), (83, "Jadarian Price"), (84, "Rhamondre Stevenson"),
    (85, "Emeka Egbuka"), (86, "Rico Dowdle"), (87, "Tyler Warren"), (88, "Ladd McConkey"),
    (89, "Bhayshul Tuten"), (90, "Colston Loveland"), (91, "Mike Evans"), (92, "Rome Odunze"),
    (93, "Christian Watson"), (94, "DJ Moore"), (95, "Tony Pollard"), (96, "Kyle Monangai"),
    (97, "DK Metcalf"), (98, "Aaron Jones Sr."), (99, "RJ Harvey"), (100, "Kenny Gainwell"),
    (101, "Tucker Kraft"), (102, "Sam LaPorta"), (103, "Josh Downs"), (104, "Jayden Reed"),
    (105, "Parker Washington"), (106, "Chris Godwin Jr."), (107, "Harold Fannin Jr."), (108, "Courtland Sutton"),
    (109, "Blake Corum"), (110, "Kyle Pitts Sr."), (111, "Rachaad White"), (112, "J.K. Dobbins"),
    (113, "Marvin Harrison Jr."), (114, "Tua Tagovailoa"), (115, "Carnell Tate"), (116, "Michael Wilson"),
    (117, "Brian Thomas Jr."), (118, "Travis Kelce"), (119, "Romeo Doubs"), (120, "Michael Pittman Jr."),
    (121, "Jacory Croskey-Merritt"), (122, "Jordan Addison"), (123, "Jason Myers"), (124, "Tyler Loop"),
    (125, "Harrison Mevis"), (126, "Cameron Dicker"), (127, "Brandon Aubrey"), (128, "Evan McPherson"),
    (129, "Jake Bates"), (130, "Mark Andrews"), (131, "Jordyn Tyson"), (132, "Jakobi Meyers"),
    (133, "Ka'imi Fairbairn"), (134, "Quentin Johnston"), (135, "Hunter Henry"), (136, "Tyler Bass"),
    (137, "Xavier Worthy"), (138, "Khalil Shakir"), (139, "Eddy Pineiro"), (140, "Jordan Mason"),
    (141, "Harrison Butker"), (142, "Andy Borregales"), (143, "Cairo Santos"), (144, "Stefon Diggs"),
    (145, "Jake Ferguson"), (146, "Cam Little"), (147, "Wil Lutz"), (148, "Dallas Goedert"),
    (149, "Chase McLaughlin"), (150, "Rams"), (151, "Will Reichard"), (152, "Jake Elliott"),
    (153, "Wan'Dale Robinson"), (154, "Jonathon Brooks"), (155, "Blake Grupe"), (156, "Broncos"),
    (157, "Chris Boswell"), (158, "Texans"), (159, "Nick Folk"), (160, "Jason Sanders"),
    (161, "Jake Moody"), (162, "Matthew Golden"), (163, "Charlie Smyth"), (164, "Ricky Pearsall"),
    (165, "Seahawks"), (166, "Chris Rodriguez Jr."), (167, "George Kittle"), (168, "Ryan Fitzgerald"),
    (169, "Matt Gay"), (170, "KC Concepcion"), (171, "Jalen Coker"), (172, "Patriots"),
    (173, "Isaiah Likely"), (174, "Vikings"), (175, "Dalton Kincaid"), (176, "Makai Lemon"),
    (177, "Jayden Higgins"), (178, "Joey Slye"), (179, "Trey Smack"), (180, "Brenton Strange"),
    (181, "Juwan Johnson"), (182, "Eagles"), (183, "Tyjae Spears"), (184, "Oronde Gadsden"),
    (185, "Tyrone Tracy Jr."), (186, "Lions"), (187, "Chad Ryland"), (188, "Michael Penix Jr."),
    (189, "Woody Marks"), (190, "Andre Szmyt"), (191, "Chargers"), (192, "Steelers"),
    (193, "Jaguars"), (194, "Bills"), (195, "Ravens"), (196, "Dalton Schultz"),
    (197, "Jauan Jennings"), (198, "Chiefs"), (199, "Deebo Samuel Sr."), (200, "Rashid Shaheed"),
]

# NFL position for every player in YAHOO_RANKINGS_2026 (QB/RB/WR/TE/K/DEF), used to
# color-code the live draft board cells by position. Verified against each player's
# actual 2026 depth chart / draft slot as of August 2026.
PLAYER_POSITIONS = {
    "Josh Allen": "QB", "Jahmyr Gibbs": "RB", "Bijan Robinson": "RB", "Jayden Daniels": "QB",
    "Joe Burrow": "QB", "Dak Prescott": "QB", "Jalen Hurts": "QB", "Lamar Jackson": "QB",
    "Drake Maye": "QB", "Ja'Marr Chase": "WR", "Jaxson Dart": "QB", "Trevor Lawrence": "QB",
    "Patrick Mahomes": "QB", "Jared Goff": "QB", "Christian McCaffrey": "RB", "Caleb Williams": "QB",
    "Justin Herbert": "QB", "Puka Nacua": "WR", "Bo Nix": "QB", "Jonathan Taylor": "RB",
    "Jordan Love": "QB", "Brock Purdy": "QB", "Amon-Ra St. Brown": "WR", "Matthew Stafford": "QB",
    "Kyler Murray": "QB", "Malik Willis": "QB", "C.J. Stroud": "QB", "Daniel Jones": "QB",
    "Baker Mayfield": "QB", "Tyler Shough": "QB", "Jaxon Smith-Njigba": "WR", "Sam Darnold": "QB",
    "De'Von Achane": "RB", "James Cook III": "RB", "CeeDee Lamb": "WR", "Derrick Henry": "RB",
    "Justin Jefferson": "WR", "Drake London": "WR", "Aaron Rodgers": "QB", "Bryce Young": "QB",
    "Cam Ward": "QB", "Chase Brown": "RB", "George Pickens": "WR", "Saquon Barkley": "RB",
    "Kenneth Walker III": "RB", "Josh Jacobs": "RB", "Ashton Jeanty": "RB", "Omarion Hampton": "RB",
    "Jacoby Brissett": "QB", "Jeremiyah Love": "RB", "Kyren Williams": "RB", "Geno Smith": "QB",
    "Tee Higgins": "WR", "Nico Collins": "WR", "Javonte Williams": "RB", "Zay Flowers": "WR",
    "A.J. Brown": "WR", "Breece Hall": "RB", "Rashee Rice": "WR", "Cam Skattebo": "RB",
    "Chris Olave": "WR", "Fernando Mendoza": "QB", "Trey McBride": "TE", "DeVonta Smith": "WR",
    "Terry McLaurin": "WR", "David Montgomery": "RB", "Travis Etienne Jr.": "RB", "D'Andre Swift": "RB",
    "TreVeyon Henderson": "RB", "Tetairoa McMillan": "WR", "Brock Bowers": "TE", "Davante Adams": "WR",
    "Malik Nabers": "WR", "Jaylen Waddle": "WR", "Jaylen Warren": "RB", "Bucky Irving": "RB",
    "Alec Pierce": "WR", "Luther Burden III": "WR", "Jameson Williams": "WR", "Garrett Wilson": "WR",
    "Quinshon Judkins": "RB", "Chuba Hubbard": "RB", "Jadarian Price": "RB", "Rhamondre Stevenson": "RB",
    "Emeka Egbuka": "WR", "Rico Dowdle": "RB", "Tyler Warren": "TE", "Ladd McConkey": "WR",
    "Bhayshul Tuten": "RB", "Colston Loveland": "TE", "Mike Evans": "WR", "Rome Odunze": "WR",
    "Christian Watson": "WR", "DJ Moore": "WR", "Tony Pollard": "RB", "Kyle Monangai": "RB",
    "DK Metcalf": "WR", "Aaron Jones Sr.": "RB", "RJ Harvey": "RB", "Kenny Gainwell": "RB",
    "Tucker Kraft": "TE", "Sam LaPorta": "TE", "Josh Downs": "WR", "Jayden Reed": "WR",
    "Parker Washington": "WR", "Chris Godwin Jr.": "WR", "Harold Fannin Jr.": "TE", "Courtland Sutton": "WR",
    "Blake Corum": "RB", "Kyle Pitts Sr.": "TE", "Rachaad White": "RB", "J.K. Dobbins": "RB",
    "Marvin Harrison Jr.": "WR", "Tua Tagovailoa": "QB", "Carnell Tate": "WR", "Michael Wilson": "WR",
    "Brian Thomas Jr.": "WR", "Travis Kelce": "TE", "Romeo Doubs": "WR", "Michael Pittman Jr.": "WR",
    "Jacory Croskey-Merritt": "RB", "Jordan Addison": "WR", "Jason Myers": "K", "Tyler Loop": "K",
    "Harrison Mevis": "K", "Cameron Dicker": "K", "Brandon Aubrey": "K", "Evan McPherson": "K",
    "Jake Bates": "K", "Mark Andrews": "TE", "Jordyn Tyson": "WR", "Jakobi Meyers": "WR",
    "Ka'imi Fairbairn": "K", "Quentin Johnston": "WR", "Hunter Henry": "TE", "Tyler Bass": "K",
    "Xavier Worthy": "WR", "Khalil Shakir": "WR", "Eddy Pineiro": "K", "Jordan Mason": "RB",
    "Harrison Butker": "K", "Andy Borregales": "K", "Cairo Santos": "K", "Stefon Diggs": "WR",
    "Jake Ferguson": "TE", "Cam Little": "K", "Wil Lutz": "K", "Dallas Goedert": "TE",
    "Chase McLaughlin": "K", "Rams": "DEF", "Will Reichard": "K", "Jake Elliott": "K",
    "Wan'Dale Robinson": "WR", "Jonathon Brooks": "RB", "Blake Grupe": "K", "Broncos": "DEF",
    "Chris Boswell": "K", "Texans": "DEF", "Nick Folk": "K", "Jason Sanders": "K",
    "Jake Moody": "K", "Matthew Golden": "WR", "Charlie Smyth": "K", "Ricky Pearsall": "WR",
    "Seahawks": "DEF", "Chris Rodriguez Jr.": "RB", "George Kittle": "TE", "Ryan Fitzgerald": "K",
    "Matt Gay": "K", "KC Concepcion": "WR", "Jalen Coker": "WR", "Patriots": "DEF",
    "Isaiah Likely": "TE", "Vikings": "DEF", "Dalton Kincaid": "TE", "Makai Lemon": "WR",
    "Jayden Higgins": "WR", "Joey Slye": "K", "Trey Smack": "K", "Brenton Strange": "TE",
    "Juwan Johnson": "TE", "Eagles": "DEF", "Tyjae Spears": "RB", "Oronde Gadsden": "TE",
    "Tyrone Tracy Jr.": "RB", "Lions": "DEF", "Chad Ryland": "K", "Michael Penix Jr.": "QB",
    "Woody Marks": "RB", "Andre Szmyt": "K", "Chargers": "DEF", "Steelers": "DEF",
    "Jaguars": "DEF", "Bills": "DEF", "Ravens": "DEF", "Dalton Schultz": "TE",
    "Jauan Jennings": "WR", "Chiefs": "DEF", "Deebo Samuel Sr.": "WR", "Rashid Shaheed": "WR",
}

# Consecutive years each 2026 keeper has been KEPT (not counting the season they were
# first drafted/acquired) by the SAME team, verified against Yahoo's keeper flags in the
# 2022-2025 draft results. 1 = first time being kept (2026 will be their 1st keeper year).
# format: team -> {player: (consecutive_keeper_years_including_2026, note)}
KEEPER_HISTORY = {
    "Scypher": {
        "Jahmyr Gibbs": (1, "Fresh 1st-round pick in 2025; 2026 is his first year as a keeper."),
        "De'Von Achane": (3, "Kept every year since 2024 (3rd straight year as a keeper)."),
    },
    "Mamba Mentality": {
        "Chris Olave": (1, "New 2026 keeper selection (Round 9 cost); first year as a keeper on this roster."),
        "George Pickens": (1, "Fresh 2025 pick; 2026 is his first year as a keeper."),
    },
    "Sahara and Sahil": {
        "Drake Maye": (1, "Fresh 2025 pick; 2026 is his first year as a keeper."),
        "Garrett Wilson": (3, "Acquired via in-season trade from Ilyas on Oct 3, 2023 (for Alvin Kamara). First kept in 2024; 2026 is his 3rd straight year as a keeper."),
    },
    "This hill I die on": {
        "Amon-Ra St. Brown": (1, "Acquired via in-season trade in 2025; 2026 is his first year as a keeper on this roster."),
        "Trevor Lawrence": (1, "New 2026 keeper selection (Round 7 cost); first year as a keeper on this roster."),
    },
    "Philly Illy": {
        "Emeka Egbuka": (1, "New 2026 keeper selection (Round 5 cost); first year as a keeper on this roster."),
        "Caleb Williams": (1, "Fresh 2025 pick (Round 6); 2026 is his first year as a keeper."),
    },
    "Chase the Baker Ladd!": {
        "Justin Jefferson": (3, "On this roster since a 2023 trade; kept every year since 2024 (3rd straight year as a keeper)."),
        "Quinshon Judkins": (1, "Added off waivers in 2025; 2026 is his first year as a keeper."),
    },
    "Hurts My Brain": {
        "Brock Bowers": (2, "Kept since 2025 (2nd straight year as a keeper)."),
        "Cam Skattebo": (1, "Acquired via in-season trade in 2025; 2026 is his first year as a keeper on this roster."),
    },
    "Hells Angels": {
        "James Cook III": (2, "Kept since 2025 (2nd straight year as a keeper)."),
        "Josh Jacobs": (2, "Kept since 2025 (2nd straight year as a keeper)."),
    },
    "Ali Khalid LLC": {
        "Jordan Love": (4, "Kept every year since 2023 - drafted back in 2022 and never let go. Tied for the longest active keeper streak in the league."),
        "Bijan Robinson": (2, "Kept since 2025 (2nd straight year as a keeper)."),
    },
    "Christian My Calf Hurt": {
        "Christian McCaffrey": (4, "Kept every year since 2023 - drafted back in 2022 and never let go. Tied for the longest active keeper streak in the league."),
        "Rome Odunze": (2, "Kept since 2025 (2nd straight year as a keeper)."),
    },
    "Immaculate Concepcion": {
        "Jonathan Taylor": (1, "Fresh 2025 pick; 2026 is his first year as a keeper."),
        "C.J. Stroud": (1, "New 2026 keeper selection (Round 10 cost); first year as a keeper on this roster."),
    },
    "Hakka PUKA!!": {
        "Puka Nacua": (3, "Kept every year since 2024 (3rd straight year as a keeper)."),
        "Jayden Daniels": (2, "Kept since 2025 (2nd straight year as a keeper)."),
    },
}

# Championship winners re-attributed to the actual account/manager (not team name),
# verified year-by-year against Yahoo's "Managers" page for each season (2011-2025).
# 2008-2010 manager names are hidden by Yahoo privacy settings on those old seasons
# and cannot be recovered. "m" is a former league member (last seen 2021) who is no
# longer part of the league - not one of today's 12 managers.
# format: year -> (team_name_that_year, manager, current_team_or_None)
CHAMPIONS_BY_MANAGER = {
    2025: ("Mamba Mentality", "kumail", "Mamba Mentality"),
    2024: ("Scypher", "Sadiq", "Scypher"),
    2023: ("Hurts My Brain", "Hussain", "Hurts My Brain"),
    2022: ("Mamba Mentality", "kumail", "Mamba Mentality"),
    2021: ("Dalvin and the Chipmunks", "Hassnain", "Immaculate Concepcion"),
    2020: ("The Dynasty", "m", None),
    2019: ("The Champion", "m", None),
    2018: ("KSolo", "wiseonekms", "Ali Khalid LLC"),
    2017: ("Scypher = poop", "m", None),
    2016: ("Scypher", "Sadiq", "Scypher"),
    2015: ("Brady's Revenge", "Turab", "Chase the Baker Ladd!"),
    2014: ("Hussain's Team", "Hussain", "Hurts My Brain"),
    2013: ("Texans Revolution", "kumail", "Mamba Mentality"),
    2012: ("Wheeling and Dealing", "Meisam", "Sahara and Sahil"),
    2011: ("The footballerz 1", "Meisam", "Sahara and Sahil"),
    2010: ("Bombay Baby Bandits", None, None),
    2009: ("comebackidz", None, None),
    2008: ("txns 4 AFC", None, None),
}

# All 1st/2nd/3rd place finishes (2008-2025) re-attributed to the actual manager
# account behind each team that year, cross-referenced against Yahoo's "Managers"
# roster page for every season 2011-2025. 2008-2010 identities are hidden by Yahoo's
# privacy settings on those old seasons. "m" was a 13th league member (last seen in
# 2021) who is no longer part of the league. Where a team's displayed nickname
# changed over time but continuity was clearly the same account (e.g. "KSolo" ->
# "wiseonekms"), finishes are merged under the current nickname.
# format: year -> (place, team_name, manager)
PODIUM_FINISHES = [
    (2025, 1, "Mamba Mentality", "kumail"), (2025, 2, "Christian My Calf Hurt", "Sarosh"), (2025, 3, "Champ Scypher", "Sadiq"),
    (2024, 1, "Scypher", "Sadiq"), (2024, 2, "Sahara and Sahil", "Meisam"), (2024, 3, "Love Thy Naber", "Ilyas"),
    (2023, 1, "Hurts My Brain", "Hussain"), (2023, 2, "TLaw & Order", "Turab"), (2023, 3, "Waji", "wajahat z"),
    (2022, 1, "Mamba Mentality", "kumail"), (2022, 2, "Vez", "Parvez"), (2022, 3, "Footballerz", "Meisam"),
    (2021, 1, "Dalvin and the Chipmunks", "Hassnain"), (2021, 2, "Scypher", "Sadiq"), (2021, 3, "KSolo", "wiseonekms"),
    (2020, 1, "The Dynasty", "m"), (2020, 2, "King of the JuJu's", "Hassnain"), (2020, 3, "Philly Illy", "Ilyas"),
    (2019, 1, "The Champion", "m"), (2019, 2, "Footballerz", "Meisam"), (2019, 3, "HereComesRetirement", "Turab"),
    (2018, 1, "KSolo", "wiseonekms"), (2018, 2, "Philly Illy", "Ilyas"), (2018, 3, "Footballerz", "Meisam"),
    (2017, 1, "Scypher = poop", "m"), (2017, 2, "Brady's Revenge", "Turab"), (2017, 3, "Philly Illy", "Ilyas"),
    (2016, 1, "Scypher", "Sadiq"), (2016, 2, "Footballerz", "Meisam"), (2016, 3, "Brady's Revenge", "Turab"),
    (2015, 1, "Brady's Revenge", "Turab"), (2015, 2, "Hussain's Team", "Hussain"), (2015, 3, "Texans Revolution", "kumail"),
    (2014, 1, "Hussain's Team", "Hussain"), (2014, 2, "Hells Angels", "omar"), (2014, 3, "KSolo", "wiseonekms"),
    (2013, 1, "Texans Revolution", "kumail"), (2013, 2, "Footballerz", "Meisam"), (2013, 3, "Bushleague", "Turab"),
    (2012, 1, "Wheeling and Dealing", "Meisam"), (2012, 2, "Texans Revolution", "kumail"), (2012, 3, "BeastModeUnleashed", "Turab"),
    (2011, 1, "The footballerz 1", "Meisam"), (2011, 2, "The Sadiqs", "Sadiq"), (2011, 3, "Junglees", "Turab"),
    (2010, 1, "Bombay Baby Bandits", None), (2010, 2, "NothingButHeart", None), (2010, 3, "2 Legit", None),
    (2009, 1, "comebackidz", None), (2009, 2, "DemBoysGotHeat", None), (2009, 3, "Rizvi14", None),
    (2008, 1, "txns 4 AFC", None), (2008, 2, "NothingbutHeart", None), (2008, 3, "The Sadiqs", None),
]

CURRENT_TEAM_BY_MANAGER = {
    "kumail": "Mamba Mentality", "Sadiq": "Scypher", "Hussain": "Hurts My Brain",
    "Meisam": "Sahara and Sahil", "Turab": "Chase the Baker Ladd!", "Hassnain": "Immaculate Concepcion",
    "wiseonekms": "Ali Khalid LLC", "Ilyas": "Philly Illy", "Sarosh": "Christian My Calf Hurt",
    "Parvez": "Hakka PUKA!!", "omar": "Hells Angels", "wajahat z": "This hill I die on",
}

# Team name -> manager nickname, per season, for the Trade Newsletter page (historical
# team names differ year to year, unlike the current-season-only D.MANAGERS dict).
# "m" (2021's "The Dynasty") is a departed former league member - shown as-is.
TRADE_TEAM_MANAGERS = {
    2021: {
        "Dalvin and the Chipmunks": "Hassnain", "FitzTragic Travesty": "Turab", "Footballerz": "Meisam",
        "Hells Angels": "omar", "KSolo": "wiseonekms", "Mamba Mentality": "kumail", "Philly Illy": "Ilyas",
        "Scypher": "Sadiq", "Silence of the Lamb": "Hussain", "The Dynasty": "m", "Vez": "Parvez", "Watwattson": "wajahat z",
    },
    2022: {
        "AutoDraft Kings": "Sarosh", "Bulletproof": "Ilyas", "Dak Street Boyz": "Hassnain", "Footballerz": "Meisam",
        "Hells Angels": "omar", "Hurts My Brain": "Hussain", "KSolo": "wiseonekms", "Mamba Mentality": "kumail",
        "Rebuild": "wajahat z", "Scypher": "Sadiq", "The Late Bloomers": "Turab", "Vez": "Parvez",
    },
    2023: {
        "AutoDraft Kings": "Sarosh", "BijanMustard": "Hassnain", "Draft Party not on me": "Meisam",
        "Hakka PUKA!!": "Parvez", "Hells Angels": "omar", "Hurts My Brain": "Hussain", "KSolo": "wiseonekms",
        "Mamba Mentality": "kumail", "Scypher": "Sadiq", "The Return of the (Short) King": "Ilyas",
        "TLaw & Order": "Turab", "Waji": "wajahat z",
    },
    2024: {
        "GetSwiftie": "Sarosh", "Hakka PUKA!!": "Parvez", "Hells Angels": "omar", "Hurts My Brain": "Hussain",
        "JJettas & MaHomies": "Turab", "KSolo": "wiseonekms", "Love Thy Naber": "Ilyas", "Mamba Mentality": "kumail",
        "Olave Oil": "Hassnain", "Sahara and Sahil": "Meisam", "Scypher": "Sadiq", "Waji": "wajahat z",
    },
    2025: {
        "Ali Khalid LLC": "wiseonekms", "Chig-Chig Boom": "Hassnain", "Christian My Calf Hurt": "Sarosh",
        "Hakka PUKA!!": "Parvez", "Hells Angels": "omar", "Hurts My Brain": "Hussain", "Mamba Mentality": "kumail",
        "Sahara and Sahil": "Meisam", "Champ Scypher": "Sadiq", "Tera Boutte Mein Danda": "Ilyas",
        "This hill I die on": "wajahat z", "You're Ma Nanga Guy": "Turab",
    },
}

# Full trade log 2021-2025, reconciled leg-by-leg from historical_scrape_raw.py's
# TRADES_BY_YEAR (Yahoo's archived league Trades pages). Each entry pairs the two
# adjacent legs that share a trade date into one two-sided trade. Grades/verdicts are
# the site's own retrospective commentary based on how the trade actually played out
# that season - not pulled from any external source.
TRADES_LOG = {
    2025: [
        {
            "date": "2025-11-19", "vetoed": False,
            "sides": [
                {"team": "Chig-Chig Boom", "gets": ["J.J. McCarthy"]},
                {"team": "You're Ma Nanga Guy", "gets": ["Courtland Sutton"]},
            ],
            "verdict": "McCarthy was banged up and inconsistent down the stretch for Minnesota while Sutton was a steady if unspectacular possession piece in Denver. A late-season shrug.",
            "grade": "C",
        },
        {
            "date": "2025-11-14", "vetoed": False,
            "sides": [
                {"team": "You're Ma Nanga Guy", "gets": ["Parker Washington"]},
                {"team": "Tera Boutte Mein Danda", "gets": ["Rachaad White"]},
            ],
            "verdict": "Washington was a fringe piece in Jacksonville's offense and White had already lost his lead-back role in Tampa to Bucky Irving by this point. Low-stakes swap.",
            "grade": "C",
        },
        {
            "date": "2025-11-12", "vetoed": False,
            "sides": [
                {"team": "This hill I die on", "gets": ["Tez Johnson", "DK Metcalf"]},
                {"team": "Hakka PUKA!!", "gets": ["Kenneth Walker III"]},
            ],
            "verdict": "Metcalf gave a real weekly WR2 floor in Pittsburgh on top of a flier in Johnson, nosing out a solid-but-crowded Walker backfield share in Seattle.",
            "grade": "B",
        },
        {
            "date": "2025-11-12", "vetoed": False,
            "sides": [
                {"team": "This hill I die on", "gets": ["Chase Brown", "Brock Purdy", "TreVeyon Henderson"]},
                {"team": "You're Ma Nanga Guy", "gets": ["Saquon Barkley", "Mark Andrews", "Darius Slayton"]},
            ],
            "verdict": "Barkley stayed one of the league's true workhorse RB1s, which alone tips this heavy 3-for-3 toward You're Ma Nanga Guy even with Chase Brown's strong Cincinnati breakout on the other side.",
            "grade": "B",
        },
        {
            "date": "2025-11-06", "vetoed": False,
            "sides": [
                {"team": "Christian My Calf Hurt", "gets": ["Matthew Golden"]},
                {"team": "You're Ma Nanga Guy", "gets": ["Rachaad White"]},
            ],
            "verdict": "Golden was a promising but still up-and-down rookie in Green Bay, and White had already ceded touches in Tampa. Low-stakes swap.",
            "grade": "C",
        },
        {
            "date": "2025-10-15", "vetoed": False,
            "sides": [
                {"team": "Tera Boutte Mein Danda", "gets": ["Jameson Williams"]},
                {"team": "Christian My Calf Hurt", "gets": ["Michael Penix Jr."]},
            ],
            "verdict": "Williams broke out as a legit big-play, high-touchdown WR1 for Detroit, outproducing Penix's solid-but-streaky first full season as Atlanta's starter.",
            "grade": "B",
        },
        {
            "date": "2025-10-07", "vetoed": False,
            "sides": [
                {"team": "You're Ma Nanga Guy", "gets": ["Brock Purdy"]},
                {"team": "This hill I die on", "gets": ["Geno Smith"]},
            ],
            "verdict": "Two fine, unspectacular starting QBs who gave streaming-caliber floor without much ceiling. A wash.",
            "grade": "C",
        },
        {
            "date": "2025-10-02", "vetoed": False,
            "sides": [
                {"team": "Chig-Chig Boom", "gets": ["Malik Washington"]},
                {"team": "Sahara and Sahil", "gets": ["Rico Dowdle"]},
            ],
            "verdict": "Dowdle caught fire on a surprise breakout stretch as Carolina's lead back, well ahead of Washington's marginal role in Miami.",
            "grade": "B",
        },
        {
            "date": "2025-09-21", "vetoed": False,
            "sides": [
                {"team": "Chig-Chig Boom", "gets": ["Romeo Doubs", "Carson Wentz", "Rhamondre Stevenson"]},
                {"team": "You're Ma Nanga Guy", "gets": ["Rashid Shaheed", "Ricky Pearsall"]},
            ],
            "verdict": "Pearsall broke out as a legitimate target earner for San Francisco once given the opportunity, and paired with a talented if oft-hurt Shaheed, that edges a Doubs/Wentz/Stevenson package leaning on complementary pieces.",
            "grade": "B",
        },
        {
            "date": "2025-09-21", "vetoed": False,
            "sides": [
                {"team": "Christian My Calf Hurt", "gets": ["Joe Flacco", "David Njoku"]},
                {"team": "You're Ma Nanga Guy", "gets": ["Romeo Doubs", "Spencer Rattler"]},
            ],
            "verdict": "Njoku gave steady TE1 production in Cleveland, well clear of a Doubs/Rattler package leaning on a WR2 and a fringe backup QB.",
            "grade": "B",
        },
        {
            "date": "2025-09-01", "vetoed": False,
            "sides": [
                {"team": "This hill I die on", "gets": ["Mark Andrews", "Amon-Ra St. Brown"]},
                {"team": "Christian My Calf Hurt", "gets": ["RJ Harvey", "Brian Thomas Jr."]},
            ],
            "verdict": "Amon-Ra St. Brown was, again, one of the best PPR receivers in football; adding him plus Andrews for a rookie RB and a Thomas who took a step back in year two was a clear win.",
            "grade": "A-",
        },
        {
            "date": "2025-08-31", "vetoed": False,
            "sides": [
                {"team": "Mamba Mentality", "gets": ["Shedeur Sanders"]},
                {"team": "This hill I die on", "gets": ["Dallas Goedert"]},
            ],
            "verdict": "Goedert gave a reliable, every-week TE1 floor in Philadelphia while Sanders spent much of the year in an inconsistent, backup-adjacent role in Cleveland.",
            "grade": "B",
        },
    ],
    2024: [
        {
            "date": "2024-12-07", "vetoed": False,
            "sides": [
                {"team": "GetSwiftie", "gets": ["Zach Charbonnet"]},
                {"team": "JJettas & MaHomies", "gets": ["Ricky Pearsall"]},
            ],
            "verdict": "Late-season depth swap - Pearsall was still working back into a full role after his preseason injury, Charbonnet a committee back behind Walker. Minor either way.",
            "grade": "C",
        },
        {
            "date": "2024-12-06", "vetoed": False,
            "sides": [
                {"team": "Sahara and Sahil", "gets": ["Rhamondre Stevenson"]},
                {"team": "Waji", "gets": ["Brian Thomas Jr.", "Derek Carr"]},
            ],
            "verdict": "Brian Thomas Jr. was in the middle of a sensational rookie season for Jacksonville (over 1,200 yards, double-digit touchdowns) - getting him plus a streamer QB for a battered Stevenson was a big win.",
            "grade": "A-",
        },
        {
            "date": "2024-12-05", "vetoed": False,
            "sides": [
                {"team": "GetSwiftie", "gets": ["Rachaad White", "Buccaneers", "Rome Odunze", "Ricky Pearsall"]},
                {"team": "JJettas & MaHomies", "gets": ["Zach Charbonnet", "Cardinals", "Jakobi Meyers"]},
            ],
            "verdict": "A complex 3-for-3-plus-DEF swap of role players and rookie WRs (Odunze, Pearsall) still finding their footing. No clear standout, roughly balanced.",
            "grade": "C",
        },
        {
            "date": "2024-12-01", "vetoed": True,
            "sides": [
                {"team": "Love Thy Naber", "gets": ["Amari Cooper"]},
                {"team": "Waji", "gets": ["Courtland Sutton"]},
            ],
            "verdict": "Blocked by the commissioner before it could go through.",
            "grade": "VETOED",
        },
        {
            "date": "2024-11-30", "vetoed": False,
            "sides": [
                {"team": "Sahara and Sahil", "gets": ["Derek Carr"]},
                {"team": "Scypher", "gets": ["Keenan Allen"]},
            ],
            "verdict": "Allen was banged up and inconsistent for a bad Bears passing attack down the stretch, Carr a steady game-manager. Fair-ish either way.",
            "grade": "C",
        },
        {
            "date": "2024-11-29", "vetoed": False,
            "sides": [
                {"team": "Waji", "gets": ["Elijah Moore", "Tank Bigsby"]},
                {"team": "Love Thy Naber", "gets": ["Courtland Sutton"]},
            ],
            "verdict": "Depth-level pieces on both sides that never became league-winners. A wash.",
            "grade": "C",
        },
        {
            "date": "2024-11-20", "vetoed": False,
            "sides": [
                {"team": "Scypher", "gets": ["Cooper Rush", "Nick Chubb"]},
                {"team": "Sahara and Sahil", "gets": ["Brian Thomas Jr."]},
            ],
            "verdict": "Chubb was still working back from his serious knee injury and never got back to full speed, while Brian Thomas Jr. was in the middle of a huge rookie breakout - lopsided in Sahara and Sahil's favor.",
            "grade": "A-",
        },
        {
            "date": "2024-11-12", "vetoed": False,
            "sides": [
                {"team": "Waji", "gets": ["Taysom Hill", "Rhamondre Stevenson"]},
                {"team": "Sahara and Sahil", "gets": ["Sam Darnold"]},
            ],
            "verdict": "Darnold had a surprising bounce-back season as Minnesota's starter with strong weekly QB1 numbers, outproducing a Taysom Hill/battered Stevenson package.",
            "grade": "B",
        },
        {
            "date": "2024-11-07", "vetoed": False,
            "sides": [
                {"team": "Waji", "gets": ["Jake Ferguson"]},
                {"team": "JJettas & MaHomies", "gets": ["Rachaad White"]},
            ],
            "verdict": "Ferguson's role got murkier as Dallas's season fell apart, White a fine but unspectacular committee back. Roughly even.",
            "grade": "C",
        },
        {
            "date": "2024-11-07", "vetoed": False,
            "sides": [
                {"team": "Love Thy Naber", "gets": ["Braelon Allen"]},
                {"team": "Sahara and Sahil", "gets": ["Eagles"]},
            ],
            "verdict": "A depth RB for a streaming defense - negligible either way.",
            "grade": "C",
        },
        {
            "date": "2024-10-25", "vetoed": False,
            "sides": [
                {"team": "Olave Oil", "gets": ["Javonte Williams"]},
                {"team": "GetSwiftie", "gets": ["George Pickens"]},
            ],
            "verdict": "Pickens gave consistent WR1-touch upside for stretches of the season, while Javonte Williams stayed stuck in an unproductive committee in Denver.",
            "grade": "B",
        },
        {
            "date": "2024-10-15", "vetoed": False,
            "sides": [
                {"team": "Waji", "gets": ["Darius Slayton", "Spencer Rattler"]},
                {"team": "Love Thy Naber", "gets": ["Michael Wilson", "Ty Chandler"]},
            ],
            "verdict": "Depth-level pieces across the board, none of whom became consistent starters. A wash.",
            "grade": "C",
        },
        {
            "date": "2024-10-11", "vetoed": False,
            "sides": [
                {"team": "Waji", "gets": ["Amari Cooper", "James Conner"]},
                {"team": "Sahara and Sahil", "gets": ["A.J. Brown"]},
            ],
            "verdict": "A.J. Brown was banged up for parts of the year but still an elite ceiling WR1 when healthy, edging a Cooper (dealt away from Cleveland midseason) and Conner (solid but oft-injured) pairing.",
            "grade": "B",
        },
        {
            "date": "2024-10-10", "vetoed": False,
            "sides": [
                {"team": "GetSwiftie", "gets": ["Dalton Kincaid", "Javonte Williams", "Jordan Mason", "Andy Dalton"]},
                {"team": "JJettas & MaHomies", "gets": ["Travis Kelce", "Alvin Kamara"]},
            ],
            "verdict": "Kamara had a strong bounce-back season and Kelce was still a locked-in TE1 target hog, giving JJettas & MaHomies the clear edge in a heavy 4-for-2 swap.",
            "grade": "B",
        },
        {
            "date": "2024-09-20", "vetoed": False,
            "sides": [
                {"team": "Sahara and Sahil", "gets": ["Keenan Allen"]},
                {"team": "Scypher", "gets": ["Zack Moss"]},
            ],
            "verdict": "Allen was solid but inconsistent in a down Bears year, Moss a committee back. Fairly even.",
            "grade": "C",
        },
        {
            "date": "2024-09-05", "vetoed": False,
            "sides": [
                {"team": "JJettas & MaHomies", "gets": ["Diontae Johnson"]},
                {"team": "GetSwiftie", "gets": ["Khalil Shakir", "Ezekiel Elliott"]},
            ],
            "verdict": "Johnson had a rocky, trade-interrupted season, while Shakir/Elliott gave modest complementary value. Close to even.",
            "grade": "C",
        },
        {
            "date": "2024-08-18", "vetoed": False,
            "sides": [
                {"team": "GetSwiftie", "gets": ["Diontae Johnson", "Russell Wilson"]},
                {"team": "Sahara and Sahil", "gets": ["Amari Cooper"]},
            ],
            "verdict": "Preseason value swap - Cooper had a fine year before his midseason trade, the Johnson/Wilson combo was middling. Fair enough.",
            "grade": "C",
        },
    ],
    2023: [
        {
            "date": "2023-11-23", "vetoed": False,
            "sides": [
                {"team": "TLaw & Order", "gets": ["Hollywood Brown"]},
                {"team": "AutoDraft Kings", "gets": ["Bryce Young"]},
            ],
            "verdict": "Young struggled as a rookie behind a shaky Panthers line, and Brown flashed occasionally for Arizona but was often quiet or hurt too. Low-impact swap.",
            "grade": "C",
        },
        {
            "date": "2023-10-25", "vetoed": False,
            "sides": [
                {"team": "AutoDraft Kings", "gets": ["Darrell Henderson Jr."]},
                {"team": "TLaw & Order", "gets": ["Chuba Hubbard"]},
            ],
            "verdict": "Both committee/handcuff-caliber backs in 2023. A wash.",
            "grade": "C",
        },
        {
            "date": "2023-10-18", "vetoed": False,
            "sides": [
                {"team": "Hakka PUKA!!", "gets": ["Chris Godwin Jr."]},
                {"team": "TLaw & Order", "gets": ["Brian Robinson"]},
            ],
            "verdict": "Robinson took over as Washington's clear lead back down the stretch, a better weekly floor than Godwin stuck as Tampa's WR2.",
            "grade": "B",
        },
        {
            "date": "2023-10-18", "vetoed": False,
            "sides": [
                {"team": "The Return of the (Short) King", "gets": ["Jerry Jeudy", "Jake Ferguson"]},
                {"team": "Hakka PUKA!!", "gets": ["Romeo Doubs"]},
            ],
            "verdict": "Ferguson broke out as Dallas's every-down TE that year, a nice add on top of a solid WR3 in Jeudy, versus a more matchup-dependent Doubs.",
            "grade": "B",
        },
        {
            "date": "2023-10-14", "vetoed": False,
            "sides": [
                {"team": "AutoDraft Kings", "gets": ["Jimmy Garoppolo", "Round 15"]},
                {"team": "Draft Party not on me", "gets": ["Rondale Moore", "Round 7"]},
            ],
            "verdict": "Garoppolo was hurt for chunks of that Raiders season and Moore was a low-volume slot piece - minor pieces plus late-round throw-ins, close to even.",
            "grade": "C",
        },
        {
            "date": "2023-10-13", "vetoed": False,
            "sides": [
                {"team": "AutoDraft Kings", "gets": ["Kenneth Walker III", "Round 6"]},
                {"team": "Hakka PUKA!!", "gets": ["Lamar Jackson", "Round 16"]},
            ],
            "verdict": "Lamar Jackson turned in an MVP-caliber 2023 season, making this one of the more lopsided value grabs of the year for Hakka PUKA!!, even after sweetening it with a mid-round pick for Sarosh.",
            "grade": "B",
        },
        {
            "date": "2023-10-12", "vetoed": False,
            "sides": [
                {"team": "Waji", "gets": ["A.J. Brown", "Round 16"]},
                {"team": "Draft Party not on me", "gets": ["Jimmy Garoppolo", "Round 1"]},
            ],
            "verdict": "A.J. Brown was a bonafide top-5 fantasy WR for Philadelphia in 2023; getting him for an injury-prone backup QB, even with a 1st-rounder attached, was a heist.",
            "grade": "A-",
        },
        {
            "date": "2023-10-11", "vetoed": False,
            "sides": [
                {"team": "TLaw & Order", "gets": ["Justin Jefferson", "Round 16"]},
                {"team": "Hakka PUKA!!", "gets": ["James Cook III", "Round 2"]},
            ],
            "verdict": "A hamstring injury cost Jefferson about half the 2023 season, but at full strength his weekly ceiling towered over Cook, who had a nice-but-not-elite season for Buffalo.",
            "grade": "A-",
        },
        {
            "date": "2023-10-11", "vetoed": False,
            "sides": [
                {"team": "TLaw & Order", "gets": ["Logan Thomas", "Zach Charbonnet"]},
                {"team": "The Return of the (Short) King", "gets": ["Romeo Doubs"]},
            ],
            "verdict": "Charbonnet was buried behind Zach Moss for much of his rookie year in Seattle, Doubs had a fine but unspectacular season in Green Bay. Close to even.",
            "grade": "C",
        },
        {
            "date": "2023-10-03", "vetoed": False,
            "sides": [
                {"team": "The Return of the (Short) King", "gets": ["Alvin Kamara"]},
                {"team": "Draft Party not on me", "gets": ["Garrett Wilson"]},
            ],
            "verdict": "Kamara was suspended for three weeks but still productive when active, while Wilson slumped through the Jets' brutal QB situation after Rodgers went down. Roughly a wash.",
            "grade": "C",
        },
        {
            "date": "2023-10-03", "vetoed": False,
            "sides": [
                {"team": "Waji", "gets": ["Jimmy Garoppolo"]},
                {"team": "AutoDraft Kings", "gets": ["Zach Wilson"]},
            ],
            "verdict": "Backup-caliber QB swap - neither moved the needle.",
            "grade": "C",
        },
        {
            "date": "2023-10-03", "vetoed": True,
            "sides": [
                {"team": "Mamba Mentality", "gets": ["Courtland Sutton"]},
                {"team": "AutoDraft Kings", "gets": ["Robert Woods"]},
            ],
            "verdict": "Blocked by the commissioner before it could go through.",
            "grade": "VETOED",
        },
        {
            "date": "2023-10-02", "vetoed": True,
            "sides": [
                {"team": "AutoDraft Kings", "gets": ["Jerry Jeudy", "Michael Gallup"]},
                {"team": "Hakka PUKA!!", "gets": ["Hollywood Brown"]},
            ],
            "verdict": "Blocked by the commissioner before it could go through.",
            "grade": "VETOED",
        },
        {
            "date": "2023-09-20", "vetoed": False,
            "sides": [
                {"team": "TLaw & Order", "gets": ["Kenny Gainwell"]},
                {"team": "AutoDraft Kings", "gets": ["Courtland Sutton"]},
            ],
            "verdict": "Gainwell stayed stuck in a timeshare in Philly, Sutton had a middling season as Denver's possession receiver. Low-impact either way.",
            "grade": "C",
        },
        {
            "date": "2023-09-14", "vetoed": False,
            "sides": [
                {"team": "KSolo", "gets": ["CeeDee Lamb", "Jaylen Warren"]},
                {"team": "Draft Party not on me", "gets": ["Alvin Kamara", "Amari Cooper", "Alexander Mattison"]},
            ],
            "verdict": "Lamb had a monster 2023 (135 catches, elite WR1 season), which alone outweighs the 3-piece return even with Kamara and Cooper both contributing solidly.",
            "grade": "B",
        },
        {
            "date": "2023-09-02", "vetoed": False,
            "sides": [
                {"team": "TLaw & Order", "gets": ["Trevor Lawrence"]},
                {"team": "Draft Party not on me", "gets": ["Tee Higgins"]},
            ],
            "verdict": "Lawrence had a fine but unspectacular season for Jacksonville, Higgins a solid WR2 in Cincy behind Chase. Even value.",
            "grade": "C",
        },
    ],
    2022: [
        {
            "date": "2022-11-23", "vetoed": False,
            "sides": [
                {"team": "Rebuild", "gets": ["Cordarrelle Patterson", "Kirk Cousins"]},
                {"team": "Footballerz", "gets": ["Kyler Murray"]},
            ],
            "verdict": "Late-season QB/skill swap - Murray had a mixed, injury-flecked stretch run, Cousins was steady if unspectacular, and Patterson had cooled off hard after a hot start. Reasonably fair.",
            "grade": "C",
        },
        {
            "date": "2022-11-22", "vetoed": False,
            "sides": [
                {"team": "Scypher", "gets": ["Antonio Gibson"]},
                {"team": "Hurts My Brain", "gets": ["Darius Slayton"]},
            ],
            "verdict": "Gibson was stuck in a maddening committee in Washington down the stretch while Slayton was touchdown-or-bust for a bad Giants offense. Low-impact challenge trade.",
            "grade": "C",
        },
        {
            "date": "2022-11-22", "vetoed": False,
            "sides": [
                {"team": "AutoDraft Kings", "gets": ["Jerry Jeudy", "Jared Goff", "Van Jefferson"]},
                {"team": "The Late Bloomers", "gets": ["Marcus Mariota", "Tyler Lockett"]},
            ],
            "verdict": "Jeudy broke out as a legit weekly starter for Denver late in the year, and Goff was a quietly solid streamer, giving Sarosh the better end against a Mariota who lost his job late and an inconsistent Lockett.",
            "grade": "B",
        },
        {
            "date": "2022-11-22", "vetoed": False,
            "sides": [
                {"team": "Rebuild", "gets": ["Cole Kmet"]},
                {"team": "AutoDraft Kings", "gets": ["Devin Duvernay"]},
            ],
            "verdict": "Two mid-season TE/WR3 fliers that never amounted to much of anything. A coin flip.",
            "grade": "C",
        },
        {
            "date": "2022-11-19", "vetoed": False,
            "sides": [
                {"team": "KSolo", "gets": ["Amari Cooper", "Tua Tagovailoa"]},
                {"team": "The Late Bloomers", "gets": ["Patrick Mahomes"]},
            ],
            "verdict": "Giving up peak Mahomes, who went on an MVP-caliber tear down the stretch, for Cooper/Tua was a rough miscalculation by Turab even though Tua had his own big moments before the concussion scares.",
            "grade": "A-",
        },
        {
            "date": "2022-11-19", "vetoed": False,
            "sides": [
                {"team": "The Late Bloomers", "gets": ["Tua Tagovailoa"]},
                {"team": "Rebuild", "gets": ["Kyler Murray"]},
            ],
            "verdict": "Same-day reshuffle - Tua's scary concussion issues capped his value late in the year while Murray was banged up too. A wash.",
            "grade": "C",
        },
        {
            "date": "2022-11-19", "vetoed": False,
            "sides": [
                {"team": "Footballerz", "gets": ["Cordarrelle Patterson"]},
                {"team": "Rebuild", "gets": ["Matt Ryan", "Kadarius Toney"]},
            ],
            "verdict": "Patterson had already cooled from his early-season role, Ryan was a late-career game-manager, and Toney barely played before his midseason trade to Kansas City. Nobody won this one.",
            "grade": "C",
        },
        {
            "date": "2022-11-11", "vetoed": False,
            "sides": [
                {"team": "Footballerz", "gets": ["Devin Singletary"]},
                {"team": "Bulletproof", "gets": ["Garrett Wilson"]},
            ],
            "verdict": "Garrett Wilson had a strong, productive rookie season as the Jets' clear WR1, a better long-term and immediate asset than a committee back in Singletary.",
            "grade": "B",
        },
        {
            "date": "2022-11-04", "vetoed": False,
            "sides": [
                {"team": "The Late Bloomers", "gets": ["Tee Higgins"]},
                {"team": "Footballerz", "gets": ["CeeDee Lamb"]},
            ],
            "verdict": "Lamb was in the midst of establishing himself as Dallas's true #1 target and finished the year red-hot, edging out an also-good but slightly less explosive Higgins season.",
            "grade": "B",
        },
        {
            "date": "2022-11-02", "vetoed": False,
            "sides": [
                {"team": "AutoDraft Kings", "gets": ["Alec Pierce"]},
                {"team": "Vez", "gets": ["Kareem Hunt"]},
            ],
            "verdict": "Pierce was a boom/bust rookie deep threat, Hunt a committee back in Cleveland. Low-stakes swap.",
            "grade": "C",
        },
        {
            "date": "2022-11-01", "vetoed": False,
            "sides": [
                {"team": "Rebuild", "gets": ["Sam Ehlinger"]},
                {"team": "The Late Bloomers", "gets": ["Davis Mills", "Joshua Palmer"]},
            ],
            "verdict": "None of these three ever became consistent fantasy starters in 2022. Negligible trade.",
            "grade": "C",
        },
        {
            "date": "2022-10-27", "vetoed": False,
            "sides": [
                {"team": "Rebuild", "gets": ["Gabe Davis"]},
                {"team": "Vez", "gets": ["Jimmy Garoppolo"]},
            ],
            "verdict": "Davis had a few big spike weeks but was wildly inconsistent, Garoppolo streamable. Fair-ish.",
            "grade": "C",
        },
        {
            "date": "2022-10-23", "vetoed": False,
            "sides": [
                {"team": "The Late Bloomers", "gets": ["Rashod Bateman", "Amari Cooper"]},
                {"team": "Bulletproof", "gets": ["Derek Carr"]},
            ],
            "verdict": "Two useful, if unspectacular, WRs for a middling Raiders QB - volume-wise the Late Bloomers got the better half.",
            "grade": "B",
        },
        {
            "date": "2022-10-23", "vetoed": False,
            "sides": [
                {"team": "Rebuild", "gets": ["D'Onta Foreman", "Davis Mills", "Michael Gallup"]},
                {"team": "The Late Bloomers", "gets": ["Jared Goff"]},
            ],
            "verdict": "Foreman had a strong breakout stretch as Carolina's lead back in the second half of 2022, giving Rebuild real difference-making value against a fine-but-unspectacular Goff.",
            "grade": "B",
        },
        {
            "date": "2022-10-18", "vetoed": False,
            "sides": [
                {"team": "AutoDraft Kings", "gets": ["Kareem Hunt", "Diontae Johnson"]},
                {"team": "The Late Bloomers", "gets": ["D'Andre Swift"]},
            ],
            "verdict": "Swift was banged up for chunks of 2022 while Hunt/Johnson gave a steadier if unspectacular floor. Roughly balanced.",
            "grade": "C",
        },
        {
            "date": "2022-10-18", "vetoed": False,
            "sides": [
                {"team": "Scypher", "gets": ["DK Metcalf"]},
                {"team": "AutoDraft Kings", "gets": ["Ezekiel Elliott"]},
            ],
            "verdict": "Metcalf had a quieter, touchdown-starved 2022 while Elliott's role shrank behind Pollard's emergence. Both underwhelmed relative to draft price.",
            "grade": "C",
        },
        {
            "date": "2022-10-11", "vetoed": False,
            "sides": [
                {"team": "Rebuild", "gets": ["Jimmy Garoppolo"]},
                {"team": "Footballerz", "gets": ["Garrett Wilson"]},
            ],
            "verdict": "Moving from a streamer QB into the Jets' clear rookie WR1 was a smart value grab given how Wilson's role only grew.",
            "grade": "B",
        },
        {
            "date": "2022-10-06", "vetoed": False,
            "sides": [
                {"team": "Rebuild", "gets": ["Jerry Jeudy", "J.K. Dobbins", "Garrett Wilson"]},
                {"team": "Footballerz", "gets": ["Tee Higgins"]},
            ],
            "verdict": "Higgins was a steady, productive WR2 in a loaded Bengals offense, a better return than a Jeudy/Dobbins/Wilson package still finding its footing at that point in the year.",
            "grade": "B",
        },
        {
            "date": "2022-10-04", "vetoed": False,
            "sides": [
                {"team": "Scypher", "gets": ["Brandin Cooks", "Darren Waller", "Melvin Gordon III"]},
                {"team": "Mamba Mentality", "gets": ["Courtland Sutton", "Chris Olave", "Tyler Conklin"]},
            ],
            "verdict": "Olave had one of the better rookie WR seasons of 2022, and that alone tips a fairly even 3-for-3 package in Mamba Mentality's favor.",
            "grade": "B",
        },
        {
            "date": "2022-09-22", "vetoed": False,
            "sides": [
                {"team": "Scypher", "gets": ["Raheem Mostert", "Adam Thielen"]},
                {"team": "AutoDraft Kings", "gets": ["Robert Woods", "Jamaal Williams"]},
            ],
            "verdict": "Jamaal Williams quietly had a strong touchdown-heavy season in Detroit, balancing out Mostert's usual injury flakiness. A fair swap.",
            "grade": "C",
        },
        {
            "date": "2022-09-03", "vetoed": False,
            "sides": [
                {"team": "Rebuild", "gets": ["Jarvis Landry"]},
                {"team": "Footballerz", "gets": ["Kadarius Toney"]},
            ],
            "verdict": "Landry was in decline in Cleveland and Toney barely played for the Giants before being dealt. Low value both ways.",
            "grade": "C",
        },
    ],
    2021: [
        {
            "date": "2021-11-18", "vetoed": False,
            "sides": [
                {"team": "FitzTragic Travesty", "gets": ["Derek Carr"]},
                {"team": "Vez", "gets": ["Damien Harris"]},
            ],
            "verdict": "Carr gave a steady but unspectacular QB streamer, while Parvez got a Patriots RB in a crowded backfield - neither side hit big.",
            "grade": "C",
        },
        {
            "date": "2021-11-05", "vetoed": False,
            "sides": [
                {"team": "Watwattson", "gets": ["Jimmy Garoppolo"]},
                {"team": "Philly Illy", "gets": ["Julio Jones"]},
            ],
            "verdict": "Julio's injury-marred Titans stint made him nearly unplayable down the stretch, while Garoppolo at least gave the Niners' backup body streaming value. Edge Watwattson.",
            "grade": "B",
        },
        {
            "date": "2021-11-03", "vetoed": False,
            "sides": [
                {"team": "Vez", "gets": ["Derek Carr"]},
                {"team": "Scypher", "gets": ["Myles Gaskin", "Khalil Herbert"]},
            ],
            "verdict": "Khalil Herbert emerged as a nice change-of-pace back for Chicago late in 2021 once Montgomery got hurt, while Gaskin flatlined after an early hot start. Carr was solid too - slight edge Scypher.",
            "grade": "B-",
        },
        {
            "date": "2021-09-30", "vetoed": False,
            "sides": [
                {"team": "Watwattson", "gets": ["Mike Davis", "Zack Moss", "Kenny Golladay"]},
                {"team": "FitzTragic Travesty", "gets": ["Damien Harris", "Noah Fant"]},
            ],
            "verdict": "Golladay was one of the biggest fantasy busts of 2021, essentially unplayable in the Giants offense, dragging that side down hard while Harris gave flex-worthy RB production.",
            "grade": "B",
        },
        {
            "date": "2021-09-28", "vetoed": False,
            "sides": [
                {"team": "Watwattson", "gets": ["James Robinson", "Noah Fant", "Julio Jones"]},
                {"team": "Footballerz", "gets": ["Tyreek Hill"]},
            ],
            "verdict": "Turning a 3-piece package into the league's top-tier WR1 in Tyreek Hill was one of the shrewdest moves of the year - Hill was an every-week league-winner while Robinson/Fant/Jones were merely solid complementary pieces.",
            "grade": "A-",
        },
        {
            "date": "2021-09-07", "vetoed": False,
            "sides": [
                {"team": "KSolo", "gets": ["Gus Edwards", "JuJu Smith-Schuster"]},
                {"team": "Footballerz", "gets": ["Allen Robinson"]},
            ],
            "verdict": "A wash of misfortune - Edwards tore his ACL in the preseason and missed the whole year, Smith-Schuster got hurt early too, and Allen Robinson had arguably his worst statistical season ever in a moribund Bears passing game.",
            "grade": "C",
        },
    ],
}
