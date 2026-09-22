"""Generate a clean one-page resume PDF — no external dependencies.

Usage:  python scripts/make_resume.py
Output: public/resume.pdf  (activates the RESUME button on the site)

Layout modeled on Adithya's reference DOCX (July 2026):
header / objective / education / internship experience / projects /
technical skills / certifications. Single column, ATS-parseable.
"""
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from resume_data import RESUME  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "public" / "resume.pdf"

PAGE_W, PAGE_H = 595, 842  # A4 at 72dpi
MARGIN = 46
INK = (0.07, 0.07, 0.07)
MUTED = (0.38, 0.38, 0.38)
ACCENT = (0.75, 0.15, 0.08)
RULE = (0.55, 0.55, 0.55)

BOLD = "Helvetica-Bold"
REG = "Helvetica"
OBL = "Helvetica-Oblique"


class PDF:
    def __init__(self):
        self.parts = []
        self.y = PAGE_H - MARGIN

    def esc(self, s: str) -> str:
        return html.escape(s, quote=False).replace("(", "\\(").replace(")", "\\)")

    def width(self, text: str, size: float, font: str = REG) -> float:
        factor = 0.55 if font == REG else 0.60
        return len(text) * size * factor

    def wrap(self, text: str, size: float, max_w: float, font: str = REG):
        words, lines, cur = text.split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if self.width(t, size, font) <= max_w:
                cur = t
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
        return lines

    def txt(self, x: float, size: float, text: str, font: str = REG,
            color=INK, dx: float = 0.0, dy: float = 0.0):
        r, g, b = color
        self.parts.append(
            f"BT /{font} {size} Tf {r} {g} {b} rg 1 0 0 1 {x + dx:.2f} {self.y + dy:.2f} Tm ({self.esc(text)}) Tj ET"
        )

    def rule(self, gap: float, thickness: float = 0.8, color=RULE):
        self.y -= gap
        self.parts.append(f"{color[0]} {color[1]} {color[2]} RG {MARGIN} {self.y:.2f} m {PAGE_W - MARGIN} {self.y:.2f} l {thickness} w S")
        self.y -= 2

    def space(self, n: float):
        self.y -= n

    def ensure(self, need: float):
        if self.y - need < MARGIN:
            raise RuntimeError("Content exceeded one page — trim resume_data.py")

    def build(self) -> bytes:
        content = "\n".join(self.parts)
        stream = content.encode("latin-1", errors="replace")
        objs = []
        objs.append(b"<< /Type /Catalog /Pages 2 0 R >>")
        objs.append(b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>")
        objs.append((
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R /F3 7 0 R >> >> >>"
        ).encode())
        objs.append(b"<< /Length " + str(len(stream)).encode() + b" >>\nstream\n" + stream + b"\nendstream")
        objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
        objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
        objs.append(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Oblique >>")

        out = bytearray(b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n")
        offsets = [0]
        for i, o in enumerate(objs, 1):
            offsets.append(len(out))
            out += f"{i} 0 obj\n".encode() + o + b"\nendobj\n"
        xref_pos = len(out)
        out += b"xref\n0 " + str(len(objs) + 1).encode() + b"\n0000000000 65535 f \n"
        for off in offsets[1:]:
            out += f"{off:010d} 00000 n \n".encode()
        out += (f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF").encode()
        return bytes(out)


def section(p: PDF, title: str):
    p.space(11)
    p.txt(MARGIN, 11, title.upper(), BOLD, ACCENT)
    p.rule(gap=3.5, thickness=0.9)


def bullet(p: PDF, text: str, size: float = 9.2):
    p.ensure(size + 4)
    p.txt(MARGIN + 2, size, "\u2022", REG, ACCENT, dy=0.8)
    for line in p.wrap(text, size, PAGE_W - MARGIN * 2 - 12):
        p.ensure(size + 2.5)
        p.txt(MARGIN + 12, size, line, REG, INK, dy=0.8)
        p.space(size + 2.4)


def entry_header(p: PDF, left: str, left_size: float, right: str, right_size: float,
                 left_font: str = BOLD, right_color=MUTED):
    """Left-aligned title with right-aligned meta on the same baseline."""
    p.ensure(left_size + 5)
    p.txt(MARGIN, left_size, left, left_font, INK)
    if right:
        w = p.width(right, right_size)
        p.txt(PAGE_W - MARGIN, right_size, right, REG, right_color, dx=-w, dy=0.6)
    p.space(left_size + 2.6)


def main():
    p = PDF()

    # ---------- header ----------
    p.txt(MARGIN, 21, RESUME["name"], BOLD, INK)
    p.space(19)
    if RESUME.get("target"):
        p.txt(MARGIN, 9.6, RESUME["target"], REG, ACCENT)
        p.space(12)
    p.space(2)
    bits = [RESUME["location"], RESUME["phone"], RESUME["email"], RESUME["github"], RESUME["linkedin"]]
    if RESUME.get("credly"):
        bits.append(RESUME["credly"])
    line = "   |   ".join(bits)
    p.txt(MARGIN, 8.8, line, REG, MUTED)
    p.rule(gap=6, thickness=1.3, color=INK)

    # ---------- objective ----------
    section(p, "Objective")
    for line in p.wrap(RESUME["summary"], 9.3, PAGE_W - MARGIN * 2):
        p.ensure(13)
        p.txt(MARGIN, 9.3, line, REG, INK)
        p.space(12.2)

    # ---------- education ----------
    section(p, "Education")
    for e in RESUME["education"]:
        entry_header(p, e["degree"], 10, e["meta"], 9)
        right = e.get("grade", "")
        w = p.width(right, 9, REG)
        p.ensure(13)
        p.txt(MARGIN, 9.2, e["school"], REG, INK)
        if right:
            p.txt(PAGE_W - MARGIN, 9.2, right, BOLD, INK, dx=-w)
        p.space(11.5)

    # ---------- experience ----------
    section(p, "Internship Experience")
    for x in RESUME["experience"]:
        entry_header(p, x["role"], 10, x["meta"], 9)
        p.txt(MARGIN, 9, x["org"], OBL, MUTED)
        p.space(11)
        for b in x["bullets"]:
            bullet(p, b)
        p.space(2)

    # ---------- projects ----------
    section(p, "Projects")
    for pr in RESUME["projects"]:
        entry_header(p, pr["name"], 10, pr["stack"], 8.2, right_color=MUTED)
        for b in pr["bullets"]:
            bullet(p, b)
        p.space(2.5)

    # ---------- skills ----------
    section(p, "Technical Skills")
    for cat, items in RESUME["skills"].items():
        p.ensure(13)
        p.txt(MARGIN, 9.2, cat, BOLD, INK)
        p.txt(MARGIN + 110, 9.2, items, REG, INK)
        p.space(12.6)

    # ---------- certifications ----------
    section(p, "Certifications")
    for c in RESUME["certifications"]:
        bullet(p, c, size=9.1)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(p.build())
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes) at y={p.y:.0f} (page bottom {MARGIN})")


if __name__ == "__main__":
    main()
