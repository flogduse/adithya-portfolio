"""Generate a clean one-page resume PDF — no external dependencies.

Usage:  python scripts/make_resume.py
Output: public/resume.pdf  (activates the RESUME button on the site)

Design: single column, typographic, ATS-parseable (real text, no images).
"""
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from resume_data import RESUME  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "public" / "resume.pdf"

PAGE_W, PAGE_H = 595, 842  # A4 at 72dpi
MARGIN = 48
INK = (0.07, 0.07, 0.07)
MUTED = (0.35, 0.35, 0.35)
ACCENT = (0.75, 0.15, 0.08)
LINE = (0.8, 0.8, 0.8)

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
        # Helvetica avg width factors (good enough for our wrapping)
        factor = 0.56 if font == REG else 0.60
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

    def rule(self, gap: float = 6, thickness: float = 0.7, color=LINE):
        self.y -= gap
        self.parts.append(f"0.7 {color[0]} {color[1]} {color[2]} RG {MARGIN} {self.y:.2f} m {PAGE_W - MARGIN} {self.y:.2f} l {thickness} w S")
        self.y -= gap

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
        objs.append(
            (
                f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] "
                f"/Contents 4 0 R /Resources << /Font << /F1 5 0 R /F2 6 0 R /F3 7 0 R >> >> >>"
            ).encode()
        )
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
        out += (
            f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF"
        ).encode()
        return bytes(out)


def h2(p: PDF, text: str):
    p.ensure(46)
    p.space(14)
    p.txt(MARGIN, 11.5, text.upper(), BOLD, ACCENT)
    p.space(6)
    p.rule(gap=3, thickness=0.8, color=(0.45, 0.45, 0.45))


def bullet(p: PDF, text: str, size: float = 9.3, indent: float = 14):
    p.ensure(30)
    p.txt(MARGIN + indent, size, "•", REG, ACCENT, dy=1)
    max_w = PAGE_W - MARGIN * 2 - indent - 10
    lines = p.wrap(text, size, max_w)
    for i, line in enumerate(lines):
        p.ensure(size + 3)
        if i == 0:
            p.txt(MARGIN + indent + 10, size, line, REG, INK, dy=1)
        else:
            p.txt(MARGIN + indent + 10, size, line, REG, INK, dy=1)
        p.space(size + 2.6)


def project(p: PDF, pr: dict):
    p.ensure(58)
    p.space(10)
    p.txt(MARGIN, 10.6, pr["name"], BOLD, INK)
    p.txt(PAGE_W - MARGIN, 8.6, pr["stack"], OBL, MUTED, dx=-p.width(pr["stack"], 8.6, OBL), dy=1.5)
    p.space(12.5)
    for b in pr["bullets"]:
        bullet(p, b)
    p.space(2)


def main():
    p = PDF()

    # --- header ---
    p.txt(MARGIN, 22, RESUME["name"], BOLD, INK)
    p.space(21)
    p.txt(MARGIN, 10, RESUME["tagline"], REG, ACCENT)
    p.space(15)
    contact = f"{RESUME['email']}   ·   {RESUME['github']}   ·   {RESUME['linkedin']}   ·   {RESUME['location']}"
    p.txt(MARGIN, 9, contact, REG, MUTED)
    p.rule(gap=7, thickness=1.4, color=INK)

    # --- summary ---
    h2(p, "Summary")
    p.ensure(34)
    for line in p.wrap(RESUME["summary"], 9.4, PAGE_W - MARGIN * 2):
        p.txt(MARGIN, 9.4, line, REG, INK)
        p.space(12.4)

    # --- projects ---
    h2(p, "Projects")
    for pr in RESUME["projects"]:
        project(p, pr)

    # --- skills ---
    h2(p, "Skills")
    for cat, items in RESUME["skills"].items():
        p.ensure(16)
        p.txt(MARGIN, 9.3, cat.upper(), BOLD, INK)
        p.txt(MARGIN + 120, 9.3, items, REG, INK)
        p.space(13.5)

    # --- education ---
    h2(p, "Education")
    for e in RESUME["education"]:
        p.ensure(30)
        p.txt(MARGIN, 10, e["degree"], BOLD, INK)
        p.space(13)
        p.txt(MARGIN, 9.2, e["school"], REG, INK)
        p.txt(PAGE_W - MARGIN, 9.2, e["meta"], REG, MUTED, dx=-p.width(e["meta"], 9.2), dy=0)
        p.space(13)

    # --- extras ---
    h2(p, "Additional")
    for item in RESUME["extra"]:
        bullet(p, item, size=9.1)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_bytes(p.build())
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes) — RESUME button is now live")


if __name__ == "__main__":
    main()
