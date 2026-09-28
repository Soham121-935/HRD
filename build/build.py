#!/usr/bin/env python3
"""
Builds a styled A4 answer-key PDF for the HRD (OE) Question Bank.

Content lives in build/content/unit*.md using a small markdown-like syntax:
  # Title                       -> unit title (used on divider page + running header)
  ## Q1 | 8 | Question text     -> question heading block
  ### Heading                   -> section heading
  #### Heading                  -> sub heading
  - bullet / 1. numbered
  | a | b |                     -> table (first row = header)
  > [key|tip|note|warn] text    -> highlighted callout box
  ``` ... ```                   -> diagram / flow block (monospace, boxed)
  ---                           -> thin rule
Inline: **bold**
"""

import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Frame, HRFlowable,
                                KeepTogether, PageBreak, PageTemplate, Paragraph,
                                Preformatted, Spacer, Table, TableStyle)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "HRD_OE_Answer_Key_60_Questions.pdf")

FONTS = "/usr/share/fonts/truetype/dejavu"
BODY, BODY_B = "DJVSerif", "DJVSerif-Bold"
HEAD, HEAD_B = "DJVHead", "DJVHead-Bold"
MONO = "DJVMono"

pdfmetrics.registerFont(TTFont(BODY, os.path.join(FONTS, "DejaVuSerif.ttf")))
pdfmetrics.registerFont(TTFont(BODY_B, os.path.join(FONTS, "DejaVuSerif-Bold.ttf")))
pdfmetrics.registerFont(TTFont(HEAD, os.path.join(FONTS, "DejaVuSans.ttf")))
pdfmetrics.registerFont(TTFont(HEAD_B, os.path.join(FONTS, "DejaVuSans-Bold.ttf")))
pdfmetrics.registerFont(TTFont(MONO, os.path.join(FONTS, "DejaVuSansMono.ttf")))
pdfmetrics.registerFontFamily(BODY, normal=BODY, bold=BODY_B, italic=BODY, boldItalic=BODY_B)
pdfmetrics.registerFontFamily(HEAD, normal=HEAD, bold=HEAD_B, italic=HEAD, boldItalic=HEAD_B)

NAVY = colors.HexColor("#12335C")
NAVY_D = colors.HexColor("#0B2138")
BLUE_L = colors.HexColor("#EAF0F8")
TEAL = colors.HexColor("#0E6E62")
TEAL_L = colors.HexColor("#E6F3F1")
AMBER = colors.HexColor("#8A5300")
AMBER_L = colors.HexColor("#FDF3E2")
GREEN = colors.HexColor("#1F6B2E")
GREEN_L = colors.HexColor("#EDF6EE")
GREY = colors.HexColor("#5A6472")
GREY_L = colors.HexColor("#F2F4F7")
LINE = colors.HexColor("#C9D3E0")
INK = colors.HexColor("#1A1A1A")

PW, PH = A4
LM = RM = 18 * mm
TM = 20 * mm
BM = 18 * mm
CW = PW - LM - RM  # content width


def st(name, **kw):
    base = dict(fontName=BODY, fontSize=10, leading=14.6, textColor=INK,
                alignment=TA_JUSTIFY, spaceAfter=4)
    base.update(kw)
    return ParagraphStyle(name, **base)


S = {
    "body": st("body"),
    "h2": st("h2", fontName=HEAD_B, fontSize=12, leading=16, textColor=NAVY,
             alignment=TA_LEFT, spaceBefore=8, spaceAfter=3),
    "h3": st("h3", fontName=HEAD_B, fontSize=10.5, leading=14, textColor=TEAL,
             alignment=TA_LEFT, spaceBefore=6, spaceAfter=3),
    "bullet": st("bullet", leftIndent=14, bulletIndent=4, spaceAfter=2.6),
    "num": st("num", leftIndent=17, bulletIndent=3, spaceAfter=2.6),
    "cell": st("cell", fontSize=9.1, leading=12.4, alignment=TA_LEFT, spaceAfter=0),
    "cellb": st("cellb", fontSize=9.1, leading=12.4, alignment=TA_LEFT, spaceAfter=0,
                fontName=BODY_B, textColor=colors.white),
    "callout": st("callout", fontSize=9.5, leading=13.4, alignment=TA_LEFT, spaceAfter=0),
    "mono": ParagraphStyle("mono", fontName=MONO, fontSize=8.1, leading=11.4,
                           textColor=NAVY_D, alignment=TA_LEFT),
    "qnum": st("qnum", fontName=HEAD_B, fontSize=15, leading=18, textColor=colors.white,
               alignment=TA_LEFT, spaceAfter=0),
    "qtext": st("qtext", fontName=HEAD_B, fontSize=11, leading=15,
                textColor=colors.HexColor("#12233A"), alignment=TA_LEFT, spaceAfter=0),
    "qmeta": st("qmeta", fontName=HEAD, fontSize=8.3, leading=11, textColor=GREY,
                alignment=TA_LEFT, spaceAfter=0),
    "toc": st("toc", fontSize=9.1, leading=12.4, alignment=TA_LEFT, spaceAfter=0),
    "tocp": st("tocp", fontSize=9.1, leading=12.4, alignment=TA_RIGHT, spaceAfter=0,
               fontName=BODY_B, textColor=NAVY),
    "toc_u": st("toc_u", fontName=HEAD_B, fontSize=10.3, leading=14, textColor=NAVY,
                alignment=TA_LEFT, spaceBefore=6, spaceAfter=2),
}

_BOLD = re.compile(r"\*\*(.+?)\*\*")


def inline(text):
    out = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    out = _BOLD.sub(r"<b>\1</b>", out)
    return out


# ------------------------------------------------------------------- flowables
def rule(color=LINE, w=1, before=2, after=4):
    return HRFlowable(width="100%", thickness=w, color=color, spaceBefore=before, spaceAfter=after)


def callout(text, kind="note"):
    style_map = {
        "note": (AMBER_L, AMBER, "Note"),
        "key": (GREEN_L, GREEN, "Key point"),
        "tip": (TEAL_L, TEAL, "Exam tip"),
        "warn": (AMBER_L, AMBER, "Caution"),
    }
    bg, fg, label = style_map.get(kind, style_map["note"])
    p = Paragraph('<font face="%s" color="%s" size="8.6"><b>%s:</b></font>&nbsp; %s'
                  % (HEAD_B, "#" + fg.hexval()[2:], label, inline(text)), S["callout"])
    t = Table([[p]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("LINEBEFORE", (0, 0), (0, -1), 2.6, fg),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 5)])


def diagram(lines):
    maxlen = max((len(l) for l in lines), default=1)
    avail = CW - 18                     # minus left+right padding
    fs = min(8.1, avail / (maxlen * 0.6025))   # DejaVu Sans Mono advance = 0.6025 em
    style = ParagraphStyle("mono_fit", parent=S["mono"], fontSize=fs, leading=fs * 1.4)
    body = Preformatted("\n".join(lines), style)
    t = Table([[body]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7F9FC")),
        ("BOX", (0, 0), (-1, -1), 0.9, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return KeepTogether([Spacer(1, 3), t, Spacer(1, 6)])


def make_table(rows, widths=None):
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    data = [[Paragraph(inline(c), S["cellb" if i == 0 else "cell"]) for c in r]
            for i, r in enumerate(rows)]
    if widths is None:
        if ncol == 2:
            widths = [0.30, 0.70]
        elif ncol == 3:
            widths = [0.22, 0.39, 0.39]
        else:
            widths = [1.0 / ncol] * ncol
    tot = sum(widths)
    widths = [w / tot * CW for w in widths]
    t = Table(data, colWidths=widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.5),
    ]
    for i in range(1, len(rows)):
        if i % 2 == 0:
            style.append(("BACKGROUND", (0, i), (-1, i), GREY_L))
    t.setStyle(TableStyle(style))
    return t


class QuestionHead(Table):
    """Q-number chip + question text + marks badge."""

    def __init__(self, number, text, marks, unit):
        self.qnum = number
        chip = Paragraph("Q%d" % number, S["qnum"])
        qt = Paragraph(inline(text), S["qtext"])
        meta = Paragraph("Unit %d &nbsp;|&nbsp; %d Marks" % (unit, marks), S["qmeta"])
        inner = Table([[qt], [meta]], colWidths=[CW - 22 * mm - 16])
        inner.setStyle(TableStyle([
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (0, 0), 3),
            ("BOTTOMPADDING", (0, 1), (0, 1), 0),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ]))
        Table.__init__(self, [[chip, inner]], colWidths=[22 * mm, CW - 22 * mm])
        self.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, 0), NAVY),
            ("BACKGROUND", (1, 0), (1, 0), BLUE_L),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (0, 0), 7),
            ("TOPPADDING", (0, 0), (0, 0), 5),
            ("BOTTOMPADDING", (0, 0), (0, 0), 5),
            ("LEFTPADDING", (1, 0), (1, 0), 8),
            ("RIGHTPADDING", (1, 0), (1, 0), 8),
            ("TOPPADDING", (1, 0), (1, 0), 5),
            ("BOTTOMPADDING", (1, 0), (1, 0), 5),
            ("LINEBELOW", (0, 0), (-1, -1), 1.4, NAVY),
        ]))


class UnitMarker(Spacer):
    """Zero-height flowable that switches the running header text."""

    def __init__(self, title):
        Spacer.__init__(self, 0, 0)
        self.title = title

    def draw(self):
        pass


# ------------------------------------------------------------------ md parsing
class Block:
    def __init__(self, kind, **kw):
        self.kind = kind
        self.__dict__.update(kw)


def parse(path, unit_no):
    lines = open(path, encoding="utf-8").read().split("\n")
    unit_title = ""
    blocks = []
    para = []

    def flush_para():
        nonlocal para
        if para:
            blocks.append(Block("p", text=" ".join(para).strip()))
            para = []

    i = 0
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if s.startswith("# ") and not s.startswith("## "):
            flush_para()
            unit_title = s[2:].strip()
        elif s.startswith("## "):
            flush_para()
            m = re.match(r"##\s*Q(\d+)\s*\|\s*(\d+)\s*\|\s*(.+)$", s)
            if not m:
                raise ValueError("Bad question line in %s: %r" % (path, s))
            blocks.append(Block("q", n=int(m.group(1)), marks=int(m.group(2)),
                                text=m.group(3).strip(), unit=unit_no))
        elif s.startswith("### "):
            flush_para()
            blocks.append(Block("h2", text=s[4:].strip()))
        elif s.startswith("#### "):
            flush_para()
            blocks.append(Block("h3", text=s[5:].strip()))
        elif s.startswith("|"):
            flush_para()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r":?-{2,}:?", c or "--") for c in cells):
                    rows.append(cells)
                i += 1
            i -= 1
            blocks.append(Block("table", rows=rows))
        elif s.startswith("```"):
            flush_para()
            dl = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                dl.append(lines[i].rstrip())
                i += 1
            while dl and not dl[0].strip():
                dl.pop(0)
            while dl and not dl[-1].strip():
                dl.pop()
            blocks.append(Block("diagram", lines=dl))
        elif s.startswith(">"):
            flush_para()
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            i -= 1
            txt = " ".join(buf)
            kind = "note"
            m = re.match(r"\[(note|key|tip|warn)\]\s*(.*)", txt, re.S)
            if m:
                kind, txt = m.group(1), m.group(2)
            blocks.append(Block("callout", text=txt, style=kind))
        elif re.match(r"^[-*]\s+", s):
            flush_para()
            blocks.append(Block("bullet", text=re.match(r"^[-*]\s+(.*)", s).group(1).strip()))
        elif re.match(r"^\d+\.\s+", s):
            flush_para()
            mm_ = re.match(r"^(\d+)\.\s+(.*)", s)
            blocks.append(Block("number", num=int(mm_.group(1)), text=mm_.group(2).strip()))
        elif s == "---":
            flush_para()
            blocks.append(Block("rule"))
        elif not s:
            flush_para()
        else:
            if blocks and not para and blocks[-1].kind in ("bullet", "number") and raw.startswith("  "):
                blocks[-1].text += " " + s
            else:
                para.append(s)
        i += 1
    flush_para()

    intro = []
    for k, b in enumerate(blocks):
        if b.kind == "q":
            intro, blocks = blocks[:k], blocks[k:]
            break
    return unit_title, intro, blocks


# ------------------------------------------------------------------- doc build
UNITS = [("1", "unit1.md"), ("2", "unit2.md"), ("3", "unit3.md")]


class NumberedCanvas(rl_canvas.Canvas):
    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self._saved = []

    def showPage(self):
        self._saved.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        total = len(self._saved)
        for state in self._saved:
            self.__dict__.update(state)
            if self._pageNumber > 1:
                self.setFont(HEAD, 8)
                self.setFillColor(GREY)
                self.drawRightString(PW - RM, BM - 9.5 * mm,
                                     "Page %d of %d" % (self._pageNumber, total))
            super().showPage()
        super().save()


class AnswerDoc(BaseDocTemplate):
    def __init__(self, *a, **kw):
        BaseDocTemplate.__init__(self, *a, **kw)
        self.qpage = {}
        self.current_unit = ""

    def afterFlowable(self, flowable):
        if isinstance(flowable, QuestionHead):
            self.qpage[flowable.qnum] = self.page
        elif isinstance(flowable, UnitMarker):
            self.current_unit = flowable.title


def decorate(canv, doc):
    canv.saveState()
    if doc.page > 1:
        canv.setFont(HEAD, 8)
        canv.setFillColor(GREY)
        canv.drawString(LM, PH - 13 * mm, "HRD (Open Elective)  |  Question Bank Answer Key")
        canv.drawRightString(PW - RM, PH - 13 * mm, doc.current_unit)
        canv.setStrokeColor(LINE)
        canv.setLineWidth(0.6)
        canv.line(LM, PH - 14.5 * mm, PW - RM, PH - 14.5 * mm)
        canv.setStrokeColor(NAVY)
        canv.setLineWidth(1.1)
        canv.line(LM, BM - 5 * mm, PW - RM, BM - 5 * mm)
        canv.setFont(HEAD, 8)
        canv.setFillColor(GREY)
        canv.drawString(LM, BM - 9.5 * mm, "60 questions  x  8 marks  |  Units 1-3")
    canv.restoreState()


def load_units():
    units = []
    for no, fname in UNITS:
        title, intro, blocks = parse(os.path.join(HERE, "content", fname), int(no))
        units.append((no, title, intro, blocks))
    return units


def cover_and_front(flow, units, qpage):
    # ---------------------------------------------------------------- cover
    flow.append(UnitMarker(""))
    flow.append(Spacer(1, 30 * mm))
    band = Table([[Paragraph(
        '<font color="#0E6E62"><b>HUMAN RESOURCE DEVELOPMENT</b></font><br/>'
        '<font color="#5A6472" size="10">Open Elective &nbsp;|&nbsp; Question Bank - Descriptive Answer Key</font>',
        ParagraphStyle("cv1", fontName=HEAD_B, fontSize=15, leading=21, alignment=TA_CENTER))]],
        colWidths=[CW])
    band.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0)]))
    flow.append(band)
    flow.append(Spacer(1, 7 * mm))
    flow.append(Paragraph("HRD (OE) - Complete Answer Key",
                          ParagraphStyle("cv2", fontName=HEAD_B, fontSize=27, leading=33,
                                         textColor=NAVY, alignment=TA_CENTER)))
    flow.append(Spacer(1, 3 * mm))
    flow.append(Paragraph("Model answers for all <b>60 questions</b> of the prescribed question bank, "
                          "written in a structured, exam-ready and easy-to-understand form.",
                          ParagraphStyle("cv3", fontName=BODY, fontSize=11.5, leading=16,
                                         alignment=TA_CENTER, textColor=colors.HexColor("#31363F"))))
    flow.append(Spacer(1, 10 * mm))

    stat_style = ParagraphStyle("stat", fontName=HEAD_B, fontSize=13, leading=17,
                                textColor=NAVY, alignment=TA_CENTER)
    stat = [[Paragraph("60<br/><font size=8.5 color='#5A6472'>QUESTIONS</font>", stat_style),
             Paragraph("8<br/><font size=8.5 color='#5A6472'>MARKS EACH</font>", stat_style),
             Paragraph("480<br/><font size=8.5 color='#5A6472'>TOTAL MARKS</font>", stat_style),
             Paragraph("3<br/><font size=8.5 color='#5A6472'>UNITS</font>", stat_style)]]
    stb = Table(stat, colWidths=[CW / 4] * 4)
    stb.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), BLUE_L),
        ("BOX", (0, 0), (-1, -1), 0.8, LINE),
        ("INNERGRID", (0, 0), (-1, -1), 1.2, colors.white),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    flow.append(stb)
    flow.append(Spacer(1, 11 * mm))

    cover_points = [
        ["Unit", "Topic area", "Questions", "Marks"],
        ["Unit 1", "HRD concept and objectives, evolution, HRD vs HRM, HRD climate and culture, "
                   "role of HRD professional, HRD framework", "Q1 - Q20", "160"],
        ["Unit 2", "HRD system and subsystems: performance appraisal, potential appraisal, training, "
                   "career planning, feedback and counselling; design principles; strategy alignment",
         "Q21 - Q40", "160"],
        ["Unit 3", "Training Needs Assessment, training design and delivery, on-the-job / off-the-job / "
                   "e-learning methods, Kirkpatrick evaluation model", "Q41 - Q60", "160"],
    ]
    flow.append(make_table(cover_points, widths=[0.12, 0.64, 0.14, 0.10]))
    flow.append(Spacer(1, 9 * mm))
    flow.append(callout("Every answer follows the same pattern so that it is easy to revise: "
                        "**meaning and definition -> explanation in points -> table / diagram / example -> conclusion**. "
                        "Application-type questions also carry a step-wise **action plan**.", "key"))
    flow.append(Spacer(1, 12 * mm))
    flow.append(Paragraph("Compiled for examination preparation from the prescribed question bank and class notes",
                          ParagraphStyle("cv4", fontName=HEAD, fontSize=9.5, leading=13,
                                         alignment=TA_CENTER, textColor=GREY)))
    flow.append(PageBreak())

    # ---------------------------------------------------------------- how to use
    flow.append(UnitMarker("How to use this answer key"))
    flow.append(Paragraph("How to use this answer key", S["h2"]))
    flow.append(rule(NAVY, 1.2))
    flow.append(Paragraph(
        "This document contains a complete, self-contained answer for each of the 60 questions of the "
        "prescribed HRD (Open Elective) question bank. Each question carries 8 marks, and each answer is "
        "written as a full-length 8-mark response covering the definition, the theoretical explanation, "
        "suitable examples and a concluding remark. Short 'state any two' questions are also answered in "
        "full so that you have enough material even if the examiner asks the question in a longer form.",
        S["body"]))
    flow.append(Spacer(1, 2 * mm))
    how = [
        ["Element of every answer", "Why it is written this way"],
        ["Definition / meaning", "Earns the first 1-2 marks. Examiners look for a precise opening statement and, where relevant, a scholar's definition (Nadler, T. V. Rao, Kirkpatrick)."],
        ["Structured points", "Body of the answer. Each point has a bold heading so that the breadth of the answer is visible at a glance."],
        ["Table / diagram", "Compares, contrasts or sequences information. One diagram can replace a page of text during revision."],
        ["Example", "Connects theory to a workplace situation - this is what separates an average answer from a good one."],
        ["Conclusion", "A two-line closing remark that directly answers the question and gives the answer a finished look."],
        ["Action plan", "Appears in application / case-based questions (Q9, Q10, Q20, Q29, Q30, Q39, Q40, Q49, Q50, Q59, Q60). Write it in numbered steps."],
    ]
    flow.append(make_table(how, widths=[0.28, 0.72]))
    flow.append(Spacer(1, 3 * mm))
    flow.append(callout("**Strategy for 8-mark answers:** spend about 8-9 minutes per answer. Write the definition, "
                        "then 5-7 numbered points with underlined headings, then one example or a small diagram, and "
                        "finish with a two-line conclusion. Neat presentation earns marks even when the content is standard.", "tip"))
    flow.append(Spacer(1, 2 * mm))
    flow.append(callout("The answers are aligned with the prescribed notes (Unit 1 - HRD concepts and climate; "
                        "Unit 2 - HRD strategies and systems; Unit 3 - Training and Development) and with standard "
                        "HRD literature (Leonard Nadler, T. V. Rao, Udai Pareek, Donald Kirkpatrick, Raymond Noe).", "note"))
    flow.append(PageBreak())

    # ---------------------------------------------------------------- contents
    flow.append(UnitMarker("Contents"))
    flow.append(Paragraph("Contents", S["h2"]))
    flow.append(rule(NAVY, 1.2))
    all_q = []
    for no, title, intro, blocks in units:
        for b in blocks:
            if b.kind == "q":
                all_q.append((title, b))
    per_page = 22
    for ci in range(0, len(all_q), per_page):
        chunk = all_q[ci:ci + per_page]
        if ci:
            flow.append(PageBreak())
        rows = []
        cur = None
        for title, b in chunk:
            if title != cur:
                cur = title
                rows.append([Paragraph(inline(title), S["toc_u"]), ""])
            rows.append([Paragraph("<b>Q%d</b>&nbsp;&nbsp;%s" % (b.n, inline(b.text)), S["toc"]),
                         Paragraph(str(qpage.get(b.n, "")), S["tocp"])])
        t = Table(rows, colWidths=[CW - 14 * mm, 14 * mm])
        t.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2),
            ("TOPPADDING", (0, 0), (-1, -1), 1.4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.4),
            ("LINEBELOW", (0, 0), (-1, -2), 0.35, colors.HexColor("#E1E7EF")),
        ]))
        flow.append(t)
    flow.append(PageBreak())


SHORT_TITLES = {
    "1": "Unit 1 - HRD Concepts, Climate and the HRD Professional",
    "2": "Unit 2 - HRD Systems, Subsystems and Strategy",
    "3": "Unit 3 - TNA, Training Design, Methods and Evaluation",
}


def unit_flow(flow, no, title, intro, blocks):
    flow.append(UnitMarker(SHORT_TITLES.get(no, title)))
    # divider page
    flow.append(Spacer(1, 52 * mm))
    flow.append(Paragraph("UNIT %s" % no, ParagraphStyle("ud0", fontName=HEAD_B, fontSize=13, leading=16,
                                                          textColor=TEAL, alignment=TA_CENTER)))
    flow.append(Spacer(1, 4 * mm))
    short = re.sub(r"^Unit\s*\d+\s*[-:]\s*", "", title)
    flow.append(Paragraph(short, ParagraphStyle("ud1", fontName=HEAD_B, fontSize=21, leading=28,
                                                textColor=NAVY, alignment=TA_CENTER)))
    flow.append(Spacer(1, 6 * mm))
    flow.append(HRFlowable(width="35%", thickness=2, color=TEAL, hAlign="CENTER"))
    flow.append(Spacer(1, 7 * mm))
    for b in intro:
        if b.kind == "p":
            flow.append(Paragraph(inline(b.text), ParagraphStyle(
                "ui", parent=S["body"], alignment=TA_CENTER, fontSize=10.3, leading=15,
                leftIndent=10 * mm, rightIndent=10 * mm, textColor=colors.HexColor("#31363F"))))
        elif b.kind == "callout":
            flow.append(callout(b.text, b.style))
        elif b.kind == "table":
            flow.append(Spacer(1, 3 * mm))
            flow.append(make_table(b.rows))
        elif b.kind == "bullet":
            flow.append(Paragraph(inline(b.text), S["bullet"], bulletText="\u2022"))
    qs = [b.n for b in blocks if b.kind == "q"]
    flow.append(Spacer(1, 8 * mm))
    flow.append(Paragraph("Questions %d to %d &nbsp;|&nbsp; %d marks" % (qs[0], qs[-1], len(qs) * 8),
                          ParagraphStyle("ud2", fontName=HEAD, fontSize=10, leading=14,
                                         textColor=GREY, alignment=TA_CENTER)))
    flow.append(PageBreak())

    first = True
    for b in blocks:
        if b.kind == "q":
            if not first:
                flow.append(CondPageBreak(50 * mm))
                flow.append(Spacer(1, 8))
            first = False
            flow.append(QuestionHead(b.n, b.text, b.marks, b.unit))
            flow.append(Spacer(1, 5))
        elif b.kind == "h2":
            flow.append(CondPageBreak(22 * mm))
            flow.append(Paragraph(inline(b.text), S["h2"]))
            flow.append(rule(LINE, 0.7, 0, 3))
        elif b.kind == "h3":
            flow.append(CondPageBreak(16 * mm))
            flow.append(Paragraph(inline(b.text), S["h3"]))
        elif b.kind == "p":
            flow.append(Paragraph(inline(b.text), S["body"]))
        elif b.kind == "bullet":
            flow.append(Paragraph(inline(b.text), S["bullet"], bulletText="\u2022"))
        elif b.kind == "number":
            flow.append(Paragraph(inline(b.text), S["num"], bulletText="%d." % b.num))
        elif b.kind == "table":
            flow.append(Spacer(1, 2))
            flow.append(make_table(b.rows))
            flow.append(Spacer(1, 5))
        elif b.kind == "callout":
            flow.append(callout(b.text, b.style))
        elif b.kind == "diagram":
            flow.append(diagram(b.lines))
        elif b.kind == "rule":
            flow.append(rule())
    flow.append(PageBreak())


def build(units, qpage, out):
    doc = AnswerDoc(out, pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
                    title="HRD (Open Elective) - Question Bank Answer Key",
                    author="Answer Key", subject="HRD OE - 60 Questions x 8 Marks")
    frame = Frame(LM, BM, CW, PH - TM - BM, id="n", leftPadding=0, rightPadding=0,
                  topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPageEnd=decorate)])
    flow = []
    cover_and_front(flow, units, qpage)
    for no, title, intro, blocks in units:
        unit_flow(flow, no, title, intro, blocks)
    # drop the final trailing PageBreak to avoid a blank page
    if flow and isinstance(flow[-1], PageBreak):
        flow.pop()
    doc.build(flow, canvasmaker=NumberedCanvas)
    return doc.qpage


def main():
    units = load_units()
    nq = sum(1 for u in units for b in u[3] if b.kind == "q")
    print("questions found:", nq)
    tmp = os.path.join(HERE, "_pass1.pdf")
    qpage = build(units, {}, tmp)               # pass 1: learn page numbers
    qpage2 = build(units, qpage, OUT)           # pass 2: real TOC
    if qpage2 != qpage:                          # TOC length changed pagination -> one more pass
        build(units, qpage2, OUT)
    os.remove(tmp)
    print("written:", OUT)


if __name__ == "__main__":
    main()
