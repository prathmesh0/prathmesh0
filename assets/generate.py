"""Regenerates the animated SVGs in ./assets. Edit text/colours, then run: python assets/generate.py"""
import os
from xml.sax.saxutils import escape

OUT = os.path.dirname(os.path.abspath(__file__))
SANS = "Oxanium,'Segoe UI',Ubuntu,'Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "'Fira Code',ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

PRIMARY, SKY, AMBER, GREEN = "#f97316", "#0ea5e9", "#eab308", "#3fb950"
BG0, BG1, PANEL, LINE, MUTED, TEXT = "#1c1917", "#292524", "#1c1917", "#44403c", "#a8a29e", "#f5f5f4"

REDUCED = """@media (prefers-reduced-motion: reduce){*{animation:none!important}.cover,.cur{display:none}.rv{opacity:1!important}}"""


def w(path, s):
    with open(path, "w", encoding="utf-8") as f:
        f.write(s)


# --------------------------------------------------------------------------- hero
def hero():
    W, H = 1200, 400
    T = 18.0  # terminal loop length (s)
    tx, ty, tw, th = 690, 52, 470, 296
    lines = [  # (kind, text, colour)
        ("cmd", "whoami", None),
        ("out", "prathmesh-parab · full-stack engineer", TEXT),
        ("cmd", "cat focus.txt", None),
        ("out", "React · Next.js · TypeScript · Node.js", SKY),
        ("out", "AI-powered apps · REST APIs · AWS", SKY),
        ("cmd", "git status", None),
        ("out", "✓ open to SDE / Full Stack roles", GREEN),
    ]
    css, body = [], []
    t = 0.6
    y0 = ty + 76
    char_w = 9.0  # 15px mono
    for i, (kind, text, col) in enumerate(lines):
        y = y0 + i * 30
        if kind == "cmd":
            dur = 0.07 * len(text) + 0.15
            tw_px = len(text) * char_w + 12
            a, b = t / T * 100, (t + dur) / T * 100
            css.append(
                f"@keyframes c{i}{{0%,{a:.2f}%{{transform:translateX(0)}}{b:.2f}%,100%{{transform:translateX({tw_px:.0f}px)}}}}"
                f".c{i}{{animation:c{i} {T}s steps({len(text)},end) infinite}}"
                f"@keyframes p{i}{{0%,{max(a-0.3,0):.2f}%{{opacity:0}}{a:.2f}%,100%{{opacity:1}}}}.p{i}{{opacity:0;animation:p{i} {T}s infinite}}"
            )
            body.append(
                f'<text class="rv p{i}" x="{tx+24}" y="{y}" font-family="{MONO}" font-size="15" fill="{AMBER}">❯</text>'
                f'<text x="{tx+44}" y="{y}" font-family="{MONO}" font-size="15" fill="{TEXT}">{escape(text)}</text>'
                f'<rect class="cover c{i}" x="{tx+42}" y="{y-16}" width="{tw_px+10:.0f}" height="22" fill="{PANEL}"/>'
            )
            t += dur + 0.35
        else:
            a, b = t / T * 100, (t + 0.25) / T * 100
            css.append(
                f"@keyframes o{i}{{0%,{a:.2f}%{{opacity:0;transform:translateY(6px)}}{b:.2f}%,100%{{opacity:1;transform:translateY(0)}}}}"
                f".o{i}{{opacity:0;animation:o{i} {T}s ease-out infinite}}"
            )
            body.append(
                f'<text class="rv o{i}" x="{tx+44}" y="{y}" font-family="{MONO}" font-size="15" fill="{col}">{escape(text)}</text>'
            )
            t += 0.45
    # final prompt + blinking cursor
    yl = y0 + len(lines) * 30
    a = t / T * 100
    css.append(
        f"@keyframes pl{{0%,{a:.2f}%{{opacity:0}}{a+0.5:.2f}%,100%{{opacity:1}}}}.pl{{opacity:0;animation:pl {T}s infinite}}"
        "@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}.cur{animation:blink 1s steps(1) infinite}"
    )
    body.append(
        f'<g class="rv pl"><text x="{tx+24}" y="{yl}" font-family="{MONO}" font-size="15" fill="{AMBER}">❯</text>'
        f'<rect class="cur" x="{tx+44}" y="{yl-14}" width="9" height="18" rx="1" fill="{SKY}"/></g>'
    )
    css.append(
        f"@keyframes fadeall{{0%,93%{{opacity:1}}97%,100%{{opacity:0}}}}.term{{animation:fadeall {T}s infinite}}"
    )

    roles = ["Full Stack Engineer", "React · Next.js · TypeScript", "Node.js · MongoDB · AWS", "Building AI-powered products"]
    rT = 12
    css.append(
        "@keyframes role{0%{opacity:0;transform:translateY(14px)}4%,21%{opacity:1;transform:translateY(0)}25%,100%{opacity:0;transform:translateY(-14px)}}"
        + "".join(f".r{i}{{opacity:0;animation:role {rT}s ease-in-out {i*3}s infinite}}" for i in range(4))
    )
    role_svg = "".join(
        f'<text class="r{i}" x="66" y="236" font-family="{SANS}" font-size="30" font-weight="600" fill="{TEXT}">{escape(r)}</text>'
        for i, r in enumerate(roles)
    )

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Prathmesh Parab - Full Stack Engineer · React, Next.js, TypeScript, Node.js, AWS">
<title>Prathmesh Parab - Full Stack Engineer</title>
<style>
@keyframes drift1{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(90px,40px)}}}}
@keyframes drift2{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(-110px,-30px)}}}}
@keyframes drift3{{0%,100%{{transform:translate(0,0)}}50%{{transform:translate(60px,-50px)}}}}
.b1{{animation:drift1 14s ease-in-out infinite}}.b2{{animation:drift2 18s ease-in-out infinite}}.b3{{animation:drift3 16s ease-in-out infinite}}
@keyframes up{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:translateY(0)}}}}
.u1{{animation:up .9s ease-out both}}.u2{{animation:up .9s ease-out .25s both}}.u3{{animation:up .9s ease-out .5s both}}.u4{{animation:up .9s ease-out .75s both}}
@keyframes pulse{{0%{{transform:scale(1);opacity:1}}70%,100%{{transform:scale(2.8);opacity:0}}}}.ring{{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-8px)}}}}.fl{{animation:float 6s ease-in-out infinite}}
@keyframes scan{{from{{transform:translateX(-300px)}}to{{transform:translateX(1500px)}}}}.scan{{animation:scan 7s linear infinite}}
{''.join(css)}
{REDUCED}
</style>
<defs>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/></linearGradient>
  <linearGradient id="name" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="640" y2="0" spreadMethod="reflect">
    <stop offset="0" stop-color="{PRIMARY}"/><stop offset=".5" stop-color="{SKY}"/><stop offset="1" stop-color="{AMBER}"/>
    <animateTransform attributeName="gradientTransform" type="translate" from="0 0" to="1280 0" dur="8s" repeatCount="indefinite"/>
  </linearGradient>
  <linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="{PRIMARY}"/><stop offset=".5" stop-color="{SKY}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient>
  <linearGradient id="sheen" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="55"/></filter>
  <pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.3" fill="#fff" opacity=".07"/></pattern>
  <clipPath id="card"><rect width="{W}" height="{H}" rx="26"/></clipPath>
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <g filter="url(#blur)" opacity=".55">
    <circle class="b1" cx="180" cy="90" r="150" fill="{PRIMARY}"/>
    <circle class="b2" cx="980" cy="320" r="170" fill="{AMBER}" opacity=".7"/>
    <circle class="b3" cx="620" cy="40" r="120" fill="{SKY}" opacity=".6"/>
  </g>
  <rect width="{W}" height="{H}" fill="url(#dots)"/>
  <rect class="scan" x="0" y="0" width="260" height="{H}" fill="url(#sheen)" transform="skewX(-18)"/>

  <text class="u1" x="66" y="110" font-family="{MONO}" font-size="16" letter-spacing="4" fill="{SKY}">HELLO, WORLD - I'M</text>
  <text class="u2" x="62" y="180" font-family="{SANS}" font-size="70" font-weight="800" letter-spacing="-1" fill="url(#name)">Prathmesh Parab</text>
  <g class="u3">{role_svg}</g>
  <g class="u4">
    <text x="66" y="282" font-family="{SANS}" font-size="17" fill="{MUTED}">Mumbai, India  ·  2+ yrs experience  ·  AWS Certified SA - Associate</text>
    <rect x="66" y="308" width="292" height="38" rx="19" fill="#3fb95018" stroke="#3fb95066"/>
    <circle class="ring" cx="88" cy="327" r="5" fill="none" stroke="{GREEN}" stroke-width="2"/>
    <circle cx="88" cy="327" r="5" fill="{GREEN}"/>
    <text x="104" y="333" font-family="{SANS}" font-size="16" font-weight="600" fill="#7ee787">Open to SDE / Full Stack roles</text>
  </g>

  <g class="fl">
    <rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="16" fill="{PANEL}" stroke="{LINE}"/>
    <rect x="{tx}" y="{ty}" width="{tw}" height="{th}" rx="16" fill="none" stroke="url(#edge)" stroke-opacity=".55"/>
    <circle cx="{tx+24}" cy="{ty+24}" r="6" fill="#ff5f57"/><circle cx="{tx+44}" cy="{ty+24}" r="6" fill="#febc2e"/><circle cx="{tx+64}" cy="{ty+24}" r="6" fill="#28c840"/>
    <text x="{tx+tw/2}" y="{ty+29}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="{MUTED}">~/prathmesh - zsh</text>
    <line x1="{tx}" y1="{ty+46}" x2="{tx+tw}" y2="{ty+46}" stroke="{LINE}"/>
    <g class="term">{''.join(body)}</g>
  </g>
</g>
</svg>'''
    w(f"{OUT}/hero.svg", svg)


# ------------------------------------------------------------------ project cards
def pills(items, x, y, accent):
    out, cx = [], x
    for it in items:
        pw = len(it) * 7.4 + 24
        out.append(
            f'<rect x="{cx}" y="{y}" width="{pw:.0f}" height="26" rx="13" fill="{accent}1a" stroke="{accent}55"/>'
            f'<text x="{cx+pw/2:.0f}" y="{y+17.5}" text-anchor="middle" font-family="{SANS}" font-size="13" font-weight="600" fill="{accent}">{escape(it)}</text>'
        )
        cx += pw + 8
    return "".join(out)


def card(slug, title, tag, desc_lines, metric, tech, accent, accent2, mono):
    W, H = 580, 220
    per = 2 * (W + H - 40)
    tag_svg = ""
    if tag:
        live = tag == "LIVE"
        tw_ = len(tag) * 8 + (34 if live else 22)
        tx_ = W - 28 - tw_
        dot = (
            f'<circle class="ring" cx="{tx_+15}" cy="45" r="4" fill="none" stroke="{GREEN}" stroke-width="2"/><circle cx="{tx_+15}" cy="45" r="4" fill="{GREEN}"/>'
            if live else ""
        )
        col = "#7ee787" if live else accent
        tag_svg = (
            f'<rect x="{tx_}" y="32" width="{tw_}" height="26" rx="13" fill="{col}14" stroke="{col}55"/>{dot}'
            f'<text x="{tx_ + (tw_ + (22 if live else 0))/2:.0f}" y="50" text-anchor="middle" font-family="{MONO}" font-size="12" font-weight="700" letter-spacing="1.5" fill="{col}">{tag}</text>'
        )
    desc = "".join(
        f'<text x="32" y="{100 + i*22}" font-family="{SANS}" font-size="15" fill="#d6d3d1">{escape(l)}</text>'
        for i, l in enumerate(desc_lines)
    )
    metric_svg = (
        f'<text x="32" y="{100 + len(desc_lines)*22 + 8}" font-family="{SANS}" font-size="15" font-weight="700" fill="{accent2}">{escape(metric)}</text>'
        if metric else ""
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{escape(title)} - {escape(' '.join(desc_lines))}">
<title>{escape(title)}</title>
<style>
@keyframes run{{to{{stroke-dashoffset:-{per}}}}}.run{{stroke-dasharray:180 {per-180};animation:run 6s linear infinite}}
@keyframes sweep{{0%,60%{{transform:translateX(-200px)}}100%{{transform:translateX(800px)}}}}.sw{{animation:sweep 5s ease-in-out infinite}}
@keyframes pulse{{0%{{transform:scale(1);opacity:1}}70%,100%{{transform:scale(2.8);opacity:0}}}}.ring{{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite}}
@keyframes glow{{0%,100%{{opacity:.35}}50%{{opacity:.7}}}}.gl{{animation:glow 4s ease-in-out infinite}}
{REDUCED}
</style>
<defs>
  <linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{accent2}"/></linearGradient>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#1c1917"/><stop offset="1" stop-color="#292524"/></linearGradient>
  <linearGradient id="sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".07"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <radialGradient id="halo" cx=".9" cy="0" r=".9"><stop offset="0" stop-color="{accent}" stop-opacity=".35"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
  <clipPath id="c"><rect x="2" y="2" width="{W-4}" height="{H-4}" rx="18"/></clipPath>
</defs>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect class="gl" width="{W}" height="{H}" fill="url(#halo)"/>
  <rect class="sw" x="0" y="0" width="140" height="{H}" fill="url(#sh)" transform="skewX(-20)"/>
</g>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="18" fill="none" stroke="#44403c" stroke-width="1.5"/>
<rect class="run" x="2" y="2" width="{W-4}" height="{H-4}" rx="18" fill="none" stroke="url(#bd)" stroke-width="2.5" stroke-linecap="round"/>
<rect x="28" y="28" width="38" height="38" rx="10" fill="url(#bd)"/>
<text x="47" y="54" text-anchor="middle" font-family="{SANS}" font-size="18" font-weight="800" fill="#1c1917">{escape(mono)}</text>
<text x="80" y="55" font-family="{SANS}" font-size="24" font-weight="800" fill="{TEXT}">{escape(title)}</text>
{tag_svg}
{desc}
{metric_svg}
{pills(tech, 32, H-50, accent)}
</svg>'''
    w(f"{OUT}/projects/{slug}.svg", svg)


def cards():
    card("repolens", "RepoLens", "LIVE",
         ["AI repository assistant - embeds repo files and answers",
          "questions with context-aware chat + visual file explorer."],
         "⚡ Up to 80% faster repo analysis",
         ["Next.js", "Node.js", "MongoDB", "Tailwind", "Shadcn UI"], PRIMARY, SKY, "R")
    card("innerbalance", "InnerBalance", None,
         ["Mental-wellness mobile app - mood tracking, journaling,",
          "guided assessments and a chatbot for personal insights."],
         "⚡ 35% higher engagement in testing",
         ["Flutter", "Firebase", "SQL", "Chatbot"], SKY, GREEN, "I")
    card("rbac", "RBAC Backend", "BACKEND",
         ["Production-grade role-based access control API -",
          "roles, permissions and protected routes done right."],
         None, ["TypeScript", "Auth", "RBAC", "REST API"], AMBER, PRIMARY, "A")
    card("visitlume", "VisitLume AI", "PRIVATE",
         ["AI-powered visitor intelligence for small businesses -",
          "lead capture, next-best-actions, revenue attribution."],
         None, ["AI", "Analytics", "Full Stack", "Attribution"], "#fb923c", AMBER, "V")
    card("simpliadmission", "SimpliAdmission", None,
         ["Engineering college admission guide - colleges, details",
          "and contact info in one place, with less stress."],
         None, ["Guide App", "Colleges", "Contacts"], "#fbbf24", AMBER, "S")
    card("videostreaming", "Video Streaming Backend", "BACKEND",
         ["Backend for a video streaming platform -",
          "uploads, auth and content APIs."],
         None, ["JavaScript", "Node.js", "REST API"], PRIMARY, AMBER, "V")
    card("dishdelight", "DishDelight", None,
         ["Recipe app with browsable categories",
          "and community ratings."],
         None, ["Flutter", "Dart", "Mobile"], GREEN, SKY, "D")


# ------------------------------------------------------------------ about card
def about():
    W, H = 1200, 270
    rows = [
        ("ROLE", "Full Stack Engineer @ Lauren Information Technologies", PRIMARY),
        ("EXPERIENCE", "2+ years · 5+ enterprise apps for Indian & US clients", SKY),
        ("FOCUS", "Frontend architecture · Full-stack products · AI-powered apps", AMBER),
        ("STACK", "React · Next.js · TypeScript · Node.js · MongoDB · SQL · AWS", PRIMARY),
        ("CERTIFIED", "AWS Certified Solutions Architect - Associate", GREEN),
        ("DSA", "500+ problems solved (TakeUForward + LeetCode)", SKY),
        ("EDUCATION", "B.E. Computer Engineering · CGPA 8.93", AMBER),
        ("LOOKING FOR", "SDE / Frontend / Full Stack roles with end-to-end ownership", GREEN),
    ]
    out = []
    for i, (k, v, col) in enumerate(rows):
        c, r = divmod(i, 4)
        x, y = 40 + c * 580, 38 + r * 56
        out.append(
            f'<g><rect x="{x}" y="{y}" width="4" height="34" rx="2" fill="{col}"/>'
            f'<text x="{x+18}" y="{y+13}" font-family="{MONO}" font-size="11" font-weight="700" letter-spacing="1.8" fill="{col}">{k}</text>'
            f'<text x="{x+18}" y="{y+32}" font-family="{SANS}" font-size="15" fill="{TEXT}">{escape(v)}</text></g>'
        )
    w(f"{OUT}/about-me.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="About Prathmesh Parab">
<style>@keyframes up{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:none}}}}.rv{{animation:up .7s ease-out both}}
@keyframes run{{to{{stroke-dashoffset:-2800}}}}.run{{stroke-dasharray:240 2560;animation:run 10s linear infinite}}{REDUCED}</style>
<defs><linearGradient id="bd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{PRIMARY}"/><stop offset=".5" stop-color="{SKY}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/></linearGradient></defs>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="22" fill="url(#bg)" stroke="{LINE}" stroke-width="1.5"/>
<rect class="run" x="2" y="2" width="{W-4}" height="{H-4}" rx="22" fill="none" stroke="url(#bd)" stroke-width="2.5" stroke-linecap="round"/>
<line x1="600" y1="40" x2="600" y2="262" stroke="{LINE}"/>
{"".join(out)}
</svg>''')


def impact():
    W, H = 1200, 170
    tiles = [
        ("85%", "less manual operations", "Role-based financial automation", "platform · Next.js, TypeScript", PRIMARY),
        ("40%", "faster onboarding", "Project onboarding & approval", "tool for internal teams", SKY),
        ("30%", "better response & accuracy", "Flutter field app · Google Maps,", "offline sync, text-to-speech", AMBER),
        ("US", "large-scale platform", "Sprint features for a US transport", "platform · performance, a11y", GREEN),
    ]
    tw = (W - 48 - 3 * 16) / 4
    out = []
    for i, (big, lab, l1, l2, col) in enumerate(tiles):
        x = 24 + i * (tw + 16)
        out.append(
            f'<rect x="{x:.0f}" y="20" width="{tw:.0f}" height="130" rx="16" fill="#1c1917" stroke="{col}55"/>'
            f'<rect x="{x:.0f}" y="20" width="{tw:.0f}" height="130" rx="16" fill="{col}12"/>'
            f'<text x="{x+22:.0f}" y="72" font-family="{SANS}" font-size="38" font-weight="800" fill="{col}">{big}</text>'
            f'<text x="{x+22:.0f}" y="96" font-family="{SANS}" font-size="14" font-weight="700" fill="{TEXT}">{escape(lab)}</text>'
            f'<text x="{x+22:.0f}" y="118" font-family="{SANS}" font-size="12.5" fill="{MUTED}">{escape(l1)}</text>'
            f'<text x="{x+22:.0f}" y="135" font-family="{SANS}" font-size="12.5" fill="{MUTED}">{escape(l2)}</text>'
        )
    w(f"{OUT}/impact.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Impact at work: 85% less manual operations, 40% faster onboarding, 30% better response, US-scale platform">
{"".join(out)}
</svg>''')


# ------------------------------------------------------------- divider + footer
def divider():
    W = 1200
    w(f"{OUT}/divider.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 24" width="{W}" height="24" role="img" aria-label="divider">
<style>@keyframes mv{{from{{transform:translateX(-300px)}}to{{transform:translateX({W+300}px)}}}}.m{{animation:mv 4s ease-in-out infinite}}{REDUCED}</style>
<defs><linearGradient id="l" x1="0" x2="1"><stop offset="0" stop-color="{PRIMARY}" stop-opacity="0"/><stop offset=".2" stop-color="{PRIMARY}"/><stop offset=".5" stop-color="{SKY}"/><stop offset=".8" stop-color="{AMBER}"/><stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></linearGradient>
<radialGradient id="g"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".4" stop-color="{SKY}" stop-opacity=".6"/><stop offset="1" stop-color="{SKY}" stop-opacity="0"/></radialGradient></defs>
<rect x="0" y="11" width="{W}" height="2" rx="1" fill="url(#l)" opacity=".7"/>
<ellipse class="m" cx="0" cy="12" rx="120" ry="6" fill="url(#g)"/>
</svg>''')


def footer():
    W, H = 1200, 190
    def wave(amp, yb, ph):
        pts = f"M0 {yb}"
        seg = 300
        for i in range(0, 2 * W // seg + 1):
            x = i * seg
            pts += f" Q{x+seg/4} {yb - amp if (i+ph)%2==0 else yb + amp} {x+seg/2} {yb} T{x+seg} {yb}"
        return pts + f" V{H} H0 Z"
    w(f"{OUT}/footer.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Thanks for stopping by">
<style>@keyframes s1{{to{{transform:translateX(-600px)}}}}@keyframes s2{{to{{transform:translateX(-600px)}}}}
.w1{{animation:s1 9s linear infinite}}.w2{{animation:s2 14s linear infinite}}.w3{{animation:s1 20s linear infinite}}
@keyframes up{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}.t{{animation:up 1.2s ease-out both}}{REDUCED}</style>
<defs><linearGradient id="a" x1="0" x2="1"><stop offset="0" stop-color="{PRIMARY}"/><stop offset=".5" stop-color="{SKY}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient>
<clipPath id="c"><rect width="{W}" height="{H}" rx="26"/></clipPath></defs>
<g clip-path="url(#c)">
<path class="w3" d="{wave(18, 96, 1)}" fill="url(#a)" opacity=".18"/>
<path class="w2" d="{wave(14, 116, 0)}" fill="url(#a)" opacity=".3"/>
<path class="w1" d="{wave(10, 136, 1)}" fill="url(#a)" opacity=".85"/>
</g>
<text class="t" x="{W/2}" y="60" text-anchor="middle" font-family="{SANS}" font-size="26" font-weight="700" fill="url(#a)">Thanks for stopping by - let’s build something great.</text>
</svg>''')


hero(); about(); impact(); cards(); divider(); footer()
print("ok")
