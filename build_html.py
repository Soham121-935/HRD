#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import html, os
from long_answers_u1 import U1
from long_answers_u1b import U1B
from long_answers_u2 import U2
from long_answers_u2b import U2B
from long_answers_u3 import U3
from long_answers_u3b import U3B

ALL = {}
ALL.update(U1); ALL.update(U1B); ALL.update(U2); ALL.update(U2B); ALL.update(U3); ALL.update(U3B)
assert len(ALL) == 60, len(ALL)

CSS = r"""
:root { --navy:#1a365d; --teal:#0d7377; --gold:#b8860b; --bg:#efe8d8; --paper:#fffdf6; }
* { box-sizing: border-box; }
body { margin:0; font-family: Georgia, "Times New Roman", serif; background: var(--bg); color:#1a202c; line-height:1.55; }
header { background: var(--navy); color:#fff; padding: 22px 16px 16px; text-align:center; position:sticky; top:0; z-index:10; box-shadow:0 2px 12px rgba(0,0,0,.25); }
header h1 { margin:0 0 6px; font-size:1.45rem; }
header p { margin:0; opacity:.92; font-size:.92rem; }
nav { display:flex; gap:8px; justify-content:center; flex-wrap:wrap; margin-top:10px; }
nav a { color:#fff; text-decoration:none; background:rgba(255,255,255,.14); padding:6px 12px; border-radius:999px; font-size:.82rem; }
nav a:hover { background: var(--gold); color:#1a202c; }
main { max-width: 900px; margin: 20px auto 70px; padding: 0 14px; }
.note { background:#fff; border-left:4px solid var(--gold); padding:12px 16px; margin: 12px 0 22px; font-size:.95rem; }
.q { background: var(--paper); border:1px solid #e4d8bc; border-radius:12px; padding:22px 24px 16px; margin: 22px 0; box-shadow: 0 1px 4px rgba(0,0,0,.06); }
.meta { color: var(--teal); font-size:.82rem; font-weight:700; letter-spacing:.04em; text-transform:uppercase; }
.q h2 { margin:8px 0 12px; font-size:1.18rem; color: var(--navy); line-height:1.4; }
.intro p { text-align:justify; margin: 0 0 10px; }
ol.pts { margin: 8px 0 8px; padding-left: 22px; }
ol.pts li { margin: 0 0 12px; text-align:justify; }
ol.pts li b { color: var(--navy); }
.conc { font-style:italic; color:#2d3748; text-align:justify; border-top:1px solid #eadfca; padding-top:12px; }
.exam { background:#eef6f6; padding:8px 12px; border-radius:8px; font-size:.92rem; margin-top:8px; }
.unit-banner { background: var(--teal); color:#fff; text-align:center; padding:12px; border-radius:8px; margin-top:28px; font-weight:700; }
footer { text-align:center; color:#555; padding: 24px; font-size:.85rem; }
"""

unit_titles = {
    1: ("u1", "UNIT 1 — Concept of HRD, Climate, Roles and Strategy (Q1–20)"),
    2: ("u2", "UNIT 2 — HRD System and Subsystems (Q21–40)"),
    3: ("u3", "UNIT 3 — Training: TNA, Design, Methods, Evaluation (Q41–60)"),
}

parts = [f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>HRD (OE) Full Exam Solutions — 8 Marks</title>
<style>{CSS}</style>
</head>
<body>
<header>
  <h1>Human Resource Development (Open Elective)</h1>
  <p>Full exam-style solutions · 8 marks each · 60 questions · written so a beginner can learn and write</p>
  <nav>
    <a href="#u1">Unit 1 (Q1–20)</a>
    <a href="#u2">Unit 2 (Q21–40)</a>
    <a href="#u3">Unit 3 (Q41–60)</a>
  </nav>
</header>
<main>
<div class="note">
<b>How to use this in the exam:</b> For each 8-mark question write (1) a short introduction with definition and scholar if any,
(2) 6–8 numbered points, each explained in 4–6 lines with an example where possible, (3) a 3–4 line conclusion.
Do not stop at one-line bullets. Answers below are longer than you will write by hand — they are teaching notes.
In the answer book, compress each point to about 5–8 lines.
</div>
"""]

cur = None
for n in range(1, 61):
    a = ALL[n]
    u = 1 if n <= 20 else 2 if n <= 40 else 3
    if u != cur:
        cur = u
        uid, title = unit_titles[u]
        parts.append(f'<div class="unit-banner" id="{uid}">{html.escape(title)}</div>')
    intro_html = "".join(f"<p>{html.escape(p.strip())}</p>" for p in a["intro"].strip().split("\n\n") if p.strip())
    lis = []
    for title, body in a["pts"]:
        lis.append(f"<li><b>{html.escape(title)}.</b> {html.escape(body.strip())}</li>")
    parts.append(f"""
<article class="q" id="q{n}">
  <div class="meta">Question {n} · Unit {u} · 8 Marks · Point-wise theoretical answer</div>
  <h2>{html.escape(a["q"])}</h2>
  <div class="intro"><p><b>Answer — Introduction</b></p>{intro_html}</div>
  <p><b>Detailed points</b></p>
  <ol class="pts">{''.join(lis)}</ol>
  <p class="conc"><b>Conclusion (write this in the exam).</b> {html.escape(a["conc"])}</p>
</article>
""")

parts.append("""
</main>
<footer>Revise: Nadler (1969), T.V. Rao, HRD vs HRM, OCTAPAC climate, HRD subsystems, four-stage training cycle, Kirkpatrick four levels.</footer>
</body></html>
""")
out = "/home/user/HRD/HRD_QB_Solutions_8Marks.html"
open(out, "w", encoding="utf-8").write("".join(parts))
print("wrote", out, os.path.getsize(out), "bytes")
