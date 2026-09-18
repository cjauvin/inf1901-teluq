"""Fac-similé recomposé de la première page de l'article de Turing dans Mind (octobre 1950)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module1"
PAPIER, BORD, ENCRE, FOND = "#f6f0df", "#d9cbac", "#2b2622", "#efe7d3"
SERIF = "Georgia, 'Times New Roman', Times, serif"

corps = [
    "I PROPOSE to consider the question, ‘Can machines think?’",
    "This should begin with definitions of the meaning of the terms",
    "‘machine’ and ‘think’. The definitions might be framed so as to",
    "reflect so far as possible the normal use of the words, but this",
    "attitude is dangerous. If the meaning of the words ‘machine’",
    "and ‘think’ are to be found by examining how they are commonly",
    "used it is difficult to escape the conclusion that the meaning",
    "and the answer to the question, ‘Can machines think?’ is to be",
    "sought in a statistical survey such as a Gallup poll. But this is",
    "absurd. Instead of attempting such a definition I shall replace the",
    "question by another, which is closely related to it and is expressed",
    "in relatively unambiguous words.",
]

W, H = 660, 560
PX, PY, PW, PH = 90, 26, 480, 508     # la feuille
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img">',
     "<title>La première page de « Computing Machinery and Intelligence », Mind, octobre 1950</title>",
     "<desc>Fac-similé recomposé de la première page de l'article d'Alan Turing dans la revue Mind, volume LIX, numéro 236, octobre 1950 : l'en-tête de la revue, le titre « I.—Computing Machinery and Intelligence », « By A. M. Turing », le sous-titre « 1. The Imitation Game », puis les premières lignes, qui s'ouvrent sur « I propose to consider the question, ‘Can machines think?’ ».</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<rect x="{PX + 5}" y="{PY + 6}" width="{PW}" height="{PH}" fill="#000" opacity="0.10"/>',
     f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" fill="{PAPIER}" stroke="{BORD}"/>',
     f'<g font-family="{SERIF}" fill="{ENCRE}">']
cx = PX + PW / 2
o.append(f'<text x="{PX + 34}" y="{PY + 46}" font-size="11.5">VOL. LIX. No. 236.]</text>')
o.append(f'<text x="{PX + PW - 34}" y="{PY + 46}" font-size="11.5" text-anchor="end">[October, 1950</text>')
o.append(f'<text x="{cx}" y="{PY + 104}" font-size="40" text-anchor="middle" letter-spacing="10">MIND</text>')
o.append(f'<text x="{cx}" y="{PY + 132}" font-size="12.5" text-anchor="middle" letter-spacing="2">A QUARTERLY REVIEW</text>')
o.append(f'<text x="{cx}" y="{PY + 148}" font-size="9.5" text-anchor="middle" letter-spacing="1">OF</text>')
o.append(f'<text x="{cx}" y="{PY + 166}" font-size="12.5" text-anchor="middle" letter-spacing="2">PSYCHOLOGY AND PHILOSOPHY</text>')
o.append(f'<line x1="{cx - 46}" y1="{PY + 186}" x2="{cx + 46}" y2="{PY + 186}" stroke="{ENCRE}" stroke-width="1"/>')
o.append(f'<text x="{cx}" y="{PY + 222}" font-size="15" text-anchor="middle" letter-spacing="1.2">I.—COMPUTING MACHINERY AND</text>')
o.append(f'<text x="{cx}" y="{PY + 244}" font-size="15" text-anchor="middle" letter-spacing="1.2">INTELLIGENCE</text>')
o.append(f'<text x="{cx}" y="{PY + 274}" font-size="12.5" text-anchor="middle">B<tspan font-size="10">Y</tspan> A. M. T<tspan font-size="10">URING</tspan></text>')
o.append(f'<text x="{cx}" y="{PY + 308}" font-size="13" text-anchor="middle" font-style="italic">1. The Imitation Game.</text>')
y = PY + 336
for i, ligne in enumerate(corps):
    x = PX + 34
    derniere = i == len(corps) - 1
    attrs = "" if derniere else f' textLength="{PW - 68}" lengthAdjust="spacing"'
    o.append(f'<text x="{x}" y="{y + i * 14.6:.1f}" font-size="12"{attrs}>{ligne}</text>')
o.append('</g>')
o.append('</svg>')
(OUT / "turing-mind-1950.svg").write_text("\n".join(o) + "\n")
print("turing-mind-1950.svg écrit")
