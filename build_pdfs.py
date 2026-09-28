#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether, HRFlowable, Table, TableStyle
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY

from long_answers_u1 import U1
from long_answers_u1b import U1B
from long_answers_u2 import U2
from long_answers_u2b import U2B
from long_answers_u3 import U3
from long_answers_u3b import U3B

ALL = {}
ALL.update(U1); ALL.update(U1B); ALL.update(U2); ALL.update(U2B); ALL.update(U3); ALL.update(U3B)

NAVY = HexColor("#1a365d")
TEAL = HexColor("#0d7377")
GOLD = HexColor("#c9a227")
GRAY = HexColor("#4a5568")

def header_footer(canvas, doc):
    canvas.saveState()
    w, h = A4
    canvas.setFillColor(NAVY)
    canvas.rect(0, h - 18, w, 18, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Bold", 8)
    canvas.drawString(18 * mm, h - 13, "HRD (OE)  |  Full 8-mark solutions  |  60 questions")
    canvas.drawRightString(w - 18 * mm, h - 13, "Exam-style theoretical answers")
    canvas.setFillColor(NAVY)
    canvas.rect(0, 0, w, 16, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont("Times-Roman", 8)
    canvas.drawString(18 * mm, 6, "Human Resource Development — Open Elective")
    canvas.drawRightString(w - 18 * mm, 6, f"Page {doc.page}")
    canvas.restoreState()

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverTitle", fontName="Times-Bold", fontSize=20, leading=24,
    alignment=TA_CENTER, textColor=NAVY, spaceAfter=8))
styles.add(ParagraphStyle(name="CoverSub", fontName="Times-Italic", fontSize=11, leading=15,
    alignment=TA_CENTER, textColor=TEAL, spaceAfter=6))
styles.add(ParagraphStyle(name="QHead", fontName="Times-Bold", fontSize=12, leading=16,
    textColor=NAVY, spaceBefore=8, spaceAfter=3))
styles.add(ParagraphStyle(name="QText", fontName="Times-Bold", fontSize=11, leading=15,
    textColor=HexColor("#1a202c"), spaceAfter=6, alignment=TA_JUSTIFY))
styles.add(ParagraphStyle(name="Meta", fontName="Times-Bold", fontSize=10, leading=13,
    textColor=TEAL, spaceAfter=4, spaceBefore=4))
styles.add(ParagraphStyle(name="Body", fontName="Times-Roman", fontSize=10.5, leading=14.5,
    alignment=TA_JUSTIFY, textColor=black, spaceAfter=6))
styles.add(ParagraphStyle(name="Pt", fontName="Times-Roman", fontSize=10.5, leading=14.5,
    alignment=TA_JUSTIFY, textColor=black, leftIndent=12, spaceAfter=7))
styles.add(ParagraphStyle(name="Conc", fontName="Times-Italic", fontSize=10.5, leading=14.5,
    alignment=TA_JUSTIFY, textColor=GRAY, spaceBefore=4, spaceAfter=10))
styles.add(ParagraphStyle(name="Sec", fontName="Times-Bold", fontSize=13, leading=17,
    textColor=white, alignment=TA_CENTER))
styles.add(ParagraphStyle(name="Intro", fontName="Times-Roman", fontSize=10.5, leading=14.5,
    alignment=TA_JUSTIFY, spaceAfter=8))

def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            .replace("\n", " "))

def section_banner(title):
    t = Table([[Paragraph(title, styles["Sec"])]], colWidths=[170*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), TEAL),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    return t

def question_flow(n, a):
    u = 1 if n <= 20 else 2 if n <= 40 else 3
    flow = []
    flow.append(Paragraph(f"Question {n}  &nbsp;·&nbsp;  Unit {u}  &nbsp;·&nbsp;  8 Marks", styles["QHead"]))
    flow.append(HRFlowable(width="100%", thickness=0.6, color=GOLD, spaceAfter=6))
    flow.append(Paragraph(esc(a["q"]), styles["QText"]))
    flow.append(Paragraph("Introduction", styles["Meta"]))
    for para in a["intro"].strip().split("\n\n"):
        if para.strip():
            flow.append(Paragraph(esc(para.strip()), styles["Body"]))
    flow.append(Paragraph("Detailed points", styles["Meta"]))
    for i, (title, body) in enumerate(a["pts"], 1):
        flow.append(Paragraph(f"<b>{i}. {esc(title)}.</b> {esc(body.strip())}", styles["Pt"]))
    flow.append(Paragraph(f"<b>Conclusion.</b> {esc(a['conc'])}", styles["Conc"]))
    return flow

def build_combined():
    out = "/home/user/HRD/HRD_QB_Solutions_8Marks.pdf"
    doc = SimpleDocTemplate(out, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
        topMargin=24*mm, bottomMargin=20*mm,
        title="HRD (OE) Full 8-mark solutions", author="HRD Solutions")
    story = []
    story.append(Spacer(1, 28))
    story.append(Paragraph("HUMAN RESOURCE DEVELOPMENT", styles["CoverTitle"]))
    story.append(Paragraph("(Open Elective)", styles["CoverSub"]))
    story.append(HRFlowable(width="80%", thickness=2, color=GOLD, spaceBefore=6, spaceAfter=8, hAlign="CENTER"))
    story.append(Paragraph("QUESTION BANK SOLUTIONS", styles["CoverTitle"]))
    story.append(Paragraph("Full exam-style theoretical answers · 8 marks each · 60 questions", styles["CoverSub"]))
    story.append(Paragraph(
        "These answers are written so a reader who is new to HRD can understand the topic and then write "
        "an 8-mark answer. Each solution has a teaching introduction, eight explained points with examples, "
        "and a conclusion you can adapt in the answer book. In the exam, compress each point to about 5–8 handwritten lines.",
        styles["Intro"]))
    story.append(PageBreak())
    unit_titles = {
        1: "UNIT 1 — Concept of HRD, Climate, Roles and Strategy",
        2: "UNIT 2 — HRD System and Subsystems",
        3: "UNIT 3 — Training: TNA, Design, Methods, Evaluation",
    }
    cur = None
    for n in range(1, 61):
        u = 1 if n <= 20 else 2 if n <= 40 else 3
        if u != cur:
            cur = u
            story.append(section_banner(unit_titles[u]))
            story.append(Spacer(1, 10))
        story.extend(question_flow(n, ALL[n]))
        story.append(Spacer(1, 4))
    doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
    print("Wrote", out)

def build_individual():
    outdir = "/home/user/HRD/solutions_by_question"
    os.makedirs(outdir, exist_ok=True)
    for n in range(1, 61):
        u = 1 if n <= 20 else 2 if n <= 40 else 3
        path = os.path.join(outdir, f"Q{n:02d}_Unit{u}_8Marks.pdf")
        def hf(canvas, doc, n=n, u=u):
            canvas.saveState()
            w, h = A4
            canvas.setFillColor(NAVY)
            canvas.rect(0, h - 18, w, 18, fill=1, stroke=0)
            canvas.setFillColor(white)
            canvas.setFont("Times-Bold", 8)
            canvas.drawString(18 * mm, h - 13, f"HRD (OE)  |  Q{n}  |  Unit {u}  |  8 Marks")
            canvas.setFillColor(NAVY)
            canvas.rect(0, 0, w, 16, fill=1, stroke=0)
            canvas.setFillColor(white)
            canvas.setFont("Times-Roman", 8)
            canvas.drawRightString(w - 18 * mm, 6, f"Page {doc.page}")
            canvas.restoreState()
        d = SimpleDocTemplate(path, pagesize=A4, leftMargin=16*mm, rightMargin=16*mm,
            topMargin=24*mm, bottomMargin=20*mm, title=f"HRD Q{n} 8-mark solution")
        d.build(question_flow(n, ALL[n]), onFirstPage=hf, onLaterPages=hf)
    print("Wrote 60 individual PDFs")

if __name__ == "__main__":
    build_combined()
    build_individual()
