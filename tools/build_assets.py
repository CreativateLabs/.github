#!/usr/bin/env python3
"""Renders the organisation profile graphics as SVG and PNG, light and dark.

Drawn in GitHub's own palette and a neutral system face, so they read as part
of the page instead of as an advertisement pasted into it. The wordmark keeps
the brand violet: one colour, carrying the identity, and nothing else competing
with it.

The figures in the graph panel are typed in below and dated. They are not
pulled live: there is no public endpoint that reports them, so STATS and
STATS_AS_OF are edited by hand when the graph is re-measured, and the date on
the page moves with them.

Needs `rsvg-convert`.

    python3 tools/build_assets.py      # writes into profile/assets/
"""
from __future__ import annotations

import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "profile" / "assets"
UI = "Helvetica Neue, Liberation Sans, Arial, sans-serif"
VIOLET = "#6B5BCD"

STATS_AS_OF = "November 2026"
STATS = [
    ("52,000+", "concepts", "EU and German law down to the article, case law, ontologies"),
    ("106,000+", "typed relations", "between norms, authorities, companies and markets"),
    ("33", "domains", "finance, public administration, health, energy and more"),
    ("3.1 million+", "company records", "from public registers, refreshed by a daily ingest"),
    ("51,000+", "public tenders", "procurement notices linked to the authorities issuing them"),
    ("99.9%+", "anchored to a source", "measured on the graph itself, before any question"),
]

THEMES = {
    "light": dict(canvas="#ffffff", subtle="#f6f8fa", border="#d1d9e0",
                  fg="#1f2328", muted="#59636e", faint="#818b98", mark="#3B2E7E"),
    "dark": dict(canvas="#0d1117", subtle="#151b23", border="#3d444d",
                 fg="#e6edf3", muted="#9198a1", faint="#6e7681", mark="#B9A9FF"),
}


def wordmark(x, y, w, colour):
    """The Creativate wordmark, recoloured through currentColor."""
    inner = (ROOT / "tools" / "wordmark.svg").read_text()
    inner = re.sub(r'^<svg[^>]*>', '', inner.strip()).rsplit("</svg>", 1)[0]
    h = w * 5034 / 22699
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h:.1f}" '
            f'viewBox="0 0 22699 5034" color="{colour}">{inner}</svg>')


def t(x, y, s, size=14, weight=400, fill="fg", anchor="start", th=None):
    col = th[fill] if (th and fill in th) else fill
    a = f' text-anchor="{anchor}"' if anchor != "start" else ""
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (f'<text x="{x}" y="{y}" font-family="{UI}" font-size="{size}" '
            f'font-weight="{weight}" fill="{col}"{a}>{s}</text>')


def svg(w, h, body, th):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}" role="img">\n'
            f'<rect width="{w}" height="{h}" fill="{th["canvas"]}"/>\n{body}\n</svg>\n')


def banner(th):
    W, H = 1200, 248
    p = [wordmark(40, 44, 352, th["mark"])]
    p.append(t(40, 150, "AI research and consultancy · makers of c:node · Frankfurt, Germany",
               16, 500, "muted", th=th))
    p.append(f'<line x1="40" y1="178" x2="{W-40}" y2="178" '
             f'stroke="{th["border"]}" stroke-width="1"/>')
    p.append(t(40, 212, "AI that has to justify its answers: a source for every "
                        "statement, a record for every decision,", 17, 400, "fg", th=th))
    p.append(t(40, 236, "and a person approving anything that leaves the system.",
               17, 400, "fg", th=th))
    return svg(W, H, "\n".join(p), th)


def graph_panel(th):
    W, H = 1200, 318
    p = [t(40, 44, "The c:node Graph", 20, 600, "fg", th=th),
         t(40, 68, f"one continuously ingested knowledge graph · figures as of "
                   f"{STATS_AS_OF}", 13.5, 400, "muted", th=th)]
    cols, colw, x0, y0 = 3, 373, 40, 112
    for i, (big, label, note) in enumerate(STATS):
        cx = x0 + (i % cols) * colw
        cy = y0 + (i // cols) * 104
        p.append(f'<line x1="{cx}" y1="{cy - 26}" x2="{cx + colw - 34}" '
                 f'y2="{cy - 26}" stroke="{th["border"]}" stroke-width="1"/>')
        p.append(t(cx, cy + 6, big, 28, 600, "fg", th=th))
        p.append(t(cx, cy + 30, label, 14, 600, "muted", th=th))
        p.append(t(cx, cy + 52, note, 12.5, 400, "faint", th=th))
    return svg(W, H, "\n".join(p), th)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in (("banner", banner), ("graph", graph_panel)):
        for theme, th in THEMES.items():
            s = OUT / f"{name}-{theme}.svg"
            s.write_text(fn(th), encoding="utf-8")
            subprocess.run(["rsvg-convert", "-z", "2", str(s), "-o",
                            str(OUT / f"{name}-{theme}.png")], check=True)
            print("  ", s.stem)


if __name__ == "__main__":
    main()
