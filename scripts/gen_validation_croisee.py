"""La validation croisée en cinq tours sur les vingt maisons du jeu canonique."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_maisons import MAISONS, OUT  # noqa: E402

FOND, BORD, ENCRE, ENCRE_PALE, TEAL, BRUN, AXE = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#2f6f6a", "#9a5b33", "#b8a888")
N, K = len(MAISONS), 5
X0, Y0, PAS, R, LIGNE = 118, 88, 22, 7, 46

o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 380" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     '<title>La validation croisée : cinq tours, chaque maison testée une fois</title>',
     f"<desc>Cinq rangées de vingt points, une par tour. Dans chaque rangée, seize points en vert-bleu forment l'ensemble d'entraînement et quatre points en brun, encadrés, l'ensemble de test ; le bloc de test se déplace de quatre places d'une rangée à l'autre, si bien que chaque maison sert de test exactement une fois. À droite de chaque rangée, un score ; en bas, leur moyenne.</desc>",
     f'<rect x="0" y="0" width="660" height="380" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="330" y="44" font-size="16" fill="{ENCRE}" text-anchor="middle" font-weight="600">Vingt maisons, cinq tours : chaque maison sert de test une fois</text>']
for t in range(K):
    y = Y0 + t * LIGNE
    a, b = t * (N // K), (t + 1) * (N // K)
    o.append(f'<text x="{X0 - 22}" y="{y + 5}" font-size="13" fill="{ENCRE_PALE}" text-anchor="end">Tour {t + 1}</text>')
    o.append(f'<rect x="{X0 + a * PAS - 12}" y="{y - 15}" width="{(b - a) * PAS}" height="30" rx="8" fill="{BRUN}" fill-opacity="0.10" stroke="{BRUN}" stroke-width="1.3" stroke-dasharray="5 4"/>')
    for i in range(N):
        c = BRUN if a <= i < b else TEAL
        o.append(f'<circle cx="{X0 + i * PAS}" cy="{y}" r="{R}" fill="{c}" stroke="{FOND}" stroke-width="1.3"/>')
    o.append(f'<text x="{X0 + N * PAS + 4}" y="{y + 5}" font-size="13" fill="{ENCRE_PALE}" text-anchor="start">Score {t + 1}</text>')
yl = Y0 + K * LIGNE + 8
o.append(f'<circle cx="{X0 + 10}" cy="{yl + 4}" r="{R}" fill="{TEAL}" stroke="{FOND}" stroke-width="1.3"/>')
o.append(f'<text x="{X0 + 24}" y="{yl + 8}" font-size="13" fill="{ENCRE}">entraînement</text>')
o.append(f'<circle cx="{X0 + 150}" cy="{yl + 4}" r="{R}" fill="{BRUN}" stroke="{FOND}" stroke-width="1.3"/>')
o.append(f'<text x="{X0 + 164}" y="{yl + 8}" font-size="13" fill="{ENCRE}">test</text>')
o.append(f'<text x="330" y="{yl + 44}" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">Le score final est la moyenne des cinq'+' '+': il ne dépend plus du hasard d\'une seule coupe.</text>')
o.append('</svg>')
(OUT / "validation-croisee.svg").write_text("\n".join(o) + "\n")
print("validation-croisee.svg écrit")
