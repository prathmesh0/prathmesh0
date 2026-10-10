"""Builds profile/stats.svg (contributions, streaks, heatmap, top languages) from public GitHub data.
Run: python assets/stats.py [username]   (set GITHUB_TOKEN to avoid API rate limits)"""
import json, os, re, sys, urllib.request
from collections import Counter
from datetime import date, datetime, timedelta
from xml.sax.saxutils import escape

USER = sys.argv[1] if len(sys.argv) > 1 else "prathmesh0"
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "profile")
SANS = "Oxanium,'Segoe UI',Ubuntu,'Helvetica Neue',Helvetica,Arial,sans-serif"
PRIMARY, SKY, AMBER, GREEN = "#f97316", "#0ea5e9", "#eab308", "#3fb950"
TEXT, MUTED = "#f5f5f4", "#a8a29e"
LEVELS = ["#292524", "#7c2d12", "#c2410c", "#f97316", "#fdba74"]
LANG_COL = [PRIMARY, SKY, AMBER, "#fb923c", "#fbbf24", GREEN, "#fb923c", MUTED]


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "profile-stats"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok and "api.github.com" in url:
        req.add_header("Authorization", f"Bearer {tok}")
    return urllib.request.urlopen(req, timeout=30).read().decode("utf-8")


# ---- contributions (public calendar, last 12 months)
html = get(f"https://github.com/users/{USER}/contributions")
tips = {m[0]: m[1] for m in re.findall(r'for="(contribution-day-component-\d+-\d+)"[^>]*>([^<]*)</tool-tip>', html)}
days = []
for m in re.finditer(r'data-date="([\d-]+)" id="(contribution-day-component-\d+-\d+)" data-level="(\d)"', html):
    t = re.match(r"(\d+) contribution", tips.get(m[2], ""))
    days.append((date.fromisoformat(m[1]), int(t[1]) if t else 0, int(m[3])))
days.sort()
total = sum(c for _, c, _ in days)

longest = run = 0
for _, c, _ in days:
    run = run + 1 if c else 0
    longest = max(longest, run)
cur, i = 0, len(days) - 1
if i >= 0 and days[i][1] == 0:  # today may not be counted yet
    i -= 1
while i >= 0 and days[i][1]:
    cur += 1
    i -= 1

# ---- profile / repos
prof = json.loads(get(f"https://api.github.com/users/{USER}"))
repos = [r for r in json.loads(get(f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner")) if not r["fork"]]
stars = sum(r["stargazers_count"] for r in repos)
langs = Counter(r["language"] for r in repos if r["language"]).most_common(6)
lt = sum(n for _, n in langs) or 1

# ---- svg
W, H = 1200, 400
tiles = [
    ("CONTRIBUTIONS", f"{total:,}", "in the last year", PRIMARY),
    ("CURRENT STREAK", f"{cur}", "days" if cur != 1 else "day", AMBER),
    ("LONGEST STREAK", f"{longest}", "days · last year", SKY),
    ("PUBLIC REPOS", f"{prof['public_repos']}", f"{stars} stars · {prof['followers']} followers", GREEN),
]
tw = (W - 48 - 3 * 16) / 4
o = []
for k, (lab, val, sub, col) in enumerate(tiles):
    x = 24 + k * (tw + 16)
    o.append(
        f'<g><rect x="{x:.0f}" y="24" width="{tw:.0f}" height="104" rx="16" fill="#1c1917" stroke="{col}55"/>'
        f'<rect x="{x:.0f}" y="24" width="{tw:.0f}" height="104" rx="16" fill="{col}12"/>'
        f'<text x="{x+22:.0f}" y="52" font-size="12" font-weight="700" letter-spacing="1.6" fill="{MUTED}">{lab}</text>'
        f'<text x="{x+22:.0f}" y="96" font-size="40" font-weight="800" fill="{col}">{val}</text>'
        f'<text x="{x+22:.0f}" y="116" font-size="13" fill="{MUTED}">{escape(sub)}</text></g>'
    )
# heatmap
cell, gap = 17, 4
x0, y0 = 24, 172
o.append(f'<text x="24" y="156" font-size="13" font-weight="700" letter-spacing="1.6" fill="{MUTED}">CONTRIBUTION ACTIVITY</text>')
if days:
    start = days[0][0]
    for d, c, lv in days:
        wk = ((d - start).days + start.weekday() + 1) // 7  # weeks start Sunday
        dow = (d.weekday() + 1) % 7
        o.append(f'<rect x="{x0 + wk*(cell+gap)}" y="{y0 + dow*(cell+gap)}" width="{cell}" height="{cell}" rx="4" fill="{LEVELS[lv]}"><title>{c} on {d}</title></rect>')
# languages
ly = 340
o.append(f'<text x="24" y="{ly-12}" font-size="13" font-weight="700" letter-spacing="1.6" fill="{MUTED}">TOP LANGUAGES · BY REPOS</text>')
bx, bw = 24, W - 48
o.append(f'<clipPath id="lc"><rect x="{bx}" y="{ly}" width="{bw}" height="12" rx="6"/></clipPath><g clip-path="url(#lc)">')
cx = bx
for k, (name, n) in enumerate(langs):
    sw = bw * n / lt
    o.append(f'<rect x="{cx:.1f}" y="{ly}" width="{sw:.1f}" height="12" fill="{LANG_COL[k]}"/>')
    cx += sw
o.append("</g>")
cx = bx
for k, (name, n) in enumerate(langs):
    o.append(f'<circle cx="{cx+5}" cy="{ly+34}" r="5" fill="{LANG_COL[k]}"/><text x="{cx+16}" y="{ly+39}" font-size="13" fill="{TEXT}">{escape(name)} <tspan fill="{MUTED}">{n*100//lt}%</tspan></text>')
    cx += len(name) * 8 + 70
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="GitHub stats for {USER}: {total} contributions, {cur} day current streak, {longest} day longest streak">
<style>text{{font-family:{SANS}}}@keyframes up{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}.t{{animation:up .7s ease-out both}}@media (prefers-reduced-motion: reduce){{*{{animation:none!important}}}}</style>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1c1917"/><stop offset="1" stop-color="#292524"/></linearGradient></defs>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="22" fill="url(#bg)" stroke="#44403c"/>
{''.join(o)}
</svg>'''
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "stats.svg"), "w", encoding="utf-8") as f:
    f.write(svg)
print(f"ok: {total} contributions, streak {cur}/{longest}, repos {prof['public_repos']}, langs {langs}")
