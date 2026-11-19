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


def banner(_th=None):
    """One dark card for both themes: the wordmark is only ever used in white."""
    W, H = 1200, 252
    GROUND, HAIR = "#0D0F1A", "#2A3047"
    p = [f'<rect width="{W}" height="{H}" rx="8" fill="{GROUND}"/>',
         wordmark(40, 46, 352, "#FFFFFF")]
    p.append(t(40, 152, "AI research and consultancy · makers of c:node · Frankfurt, Germany",
               16, 500, "#9AA3BD"))
    p.append(f'<line x1="40" y1="180" x2="{W-40}" y2="180" '
             f'stroke="{HAIR}" stroke-width="1"/>')
    p.append(t(40, 214, "AI that has to justify its answers: a source for every "
                        "statement, a record for every decision,", 17, 400, "#E8EDF5"))
    p.append(t(40, 238, "and a person approving anything that leaves the system.",
               17, 400, "#E8EDF5"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" role="img">\n' + "\n".join(p) + "\n</svg>\n")


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


# The five marks we may actually show: the ministry and the research-allowance
# seal because the certification grants them, the two regulations because they
# are the law we build against, and the association because we are a member.
# All five already appear on c-node.ai. Drawn on a light card deliberately:
# four of them are black artwork on transparency and would vanish on a dark
# page.
LOGOS = [
    ("bmftr.png", "Bundesministerium für Forschung, Technologie und Raumfahrt"),
    ("bsfz-siegel.png", "BSFZ — research allowance certified"),
    ("eu-ai-act.png", "EU AI Act"),
    ("gdpr.png", "GDPR"),
    ("ki-bundesverband.png", "KI Bundesverband member"),
]


def _png(path: pathlib.Path):
    import base64, struct
    raw = path.read_bytes()
    w, h = struct.unpack(">II", raw[16:24])
    return base64.b64encode(raw).decode(), w, h


def partners(_th=None):
    """One light card, because four of the five marks are black on transparent."""
    W, H = 1200, 196
    BOX_W, BOX_H = 196, 58
    p = [f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="6" fill="none" '
         f'stroke="#d1d9e0" stroke-width="1"/>']
    p.append(t(32, 40, "Certified, bound and affiliated", 15, 600, "#1f2328"))
    slot = (W - 64) / len(LOGOS)
    for i, (fn, label) in enumerate(LOGOS):
        data, iw, ih = _png(OUT / "logos" / fn)
        scale = min(BOX_W / iw, BOX_H / ih)
        w, h = iw * scale, ih * scale
        cx = 32 + i * slot + slot / 2
        p.append(f'<image x="{cx - w/2:.1f}" y="{92 - h/2:.1f}" width="{w:.1f}" '
                 f'height="{h:.1f}" href="data:image/png;base64,{data}"/>')
        p.append(t(cx, 150, label.split(" — ")[0].split(" für ")[0][:30], 11.5,
                   400, "#59636e", anchor="middle"))
    p.append(t(32, H - 18, "Research allowance under § 6 FZulG, certified by the BSFZ in 2026 "
                           "· EU AI Act and GDPR are what we build against, not a certification",
               11.5, 400, "#818b98"))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" role="img">\n' + "\n".join(p) + "\n</svg>\n")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in (("graph", graph_panel),):
        for theme, th in THEMES.items():
            s = OUT / f"{name}-{theme}.svg"
            s.write_text(fn(th), encoding="utf-8")
            subprocess.run(["rsvg-convert", "-z", "2", str(s), "-o",
                            str(OUT / f"{name}-{theme}.png")], check=True)
            print("  ", s.stem)
    sb = OUT / "banner.svg"
    sb.write_text(banner(), encoding="utf-8")
    subprocess.run(["rsvg-convert", "-z", "2", str(sb), "-o",
                    str(OUT / "banner.png")], check=True)
    print("   banner")
    sp = OUT / "partners.svg"
    sp.write_text(partners(), encoding="utf-8")
    subprocess.run(["rsvg-convert", "-z", "2", str(sp), "-o",
                    str(OUT / "partners.png")], check=True)
    print("   partners")


if __name__ == "__main__":
    main()
