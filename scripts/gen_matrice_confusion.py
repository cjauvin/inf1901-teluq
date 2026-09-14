"""La matrice de confusion d'un filtre anti-pourriel sur 1000 courriels."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
VP, FN, FP, VN = 40, 10, 20, 930
NB = " "; FINE = " "

X0, Y0, W, H = 210, 120, 190, 96   # coin de la grille, taille d'une case
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 420" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La matrice de confusion d'un filtre anti-pourriel</title>",
     f"<desc>Un tableau à quatre cases croisant la réalité (pourriel ou courriel légitime, en lignes) et la décision du filtre (jeté ou gardé, en colonnes), pour 1000 courriels dont 50 pourriels. Vrais positifs{NB}: {VP} pourriels jetés. Faux négatifs{NB}: {FN} pourriels gardés. Faux positifs{NB}: {FP} courriels légitimes jetés. Vrais négatifs{NB}: {VN} courriels légitimes gardés. Les deux cases d'erreur sont teintées en rouge.</desc>",
     f'<rect x="0" y="0" width="660" height="420" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="330" y="44" font-size="16" fill="{ENCRE}" text-anchor="middle" font-weight="600">1000 courriels, dont 50 pourriels{NB}: ce que le filtre en a fait</text>']
# en-têtes de colonnes (décision du filtre)
o.append(f'<text x="{X0 + W}" y="78" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">décision du filtre</text>')
o.append(f'<text x="{X0 + W / 2}" y="104" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="600">jeté</text>')
o.append(f'<text x="{X0 + 3 * W / 2}" y="104" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="600">gardé</text>')
# en-têtes de lignes (réalité)
o.append(f'<text x="24" y="{Y0 + H}" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic" transform="rotate(-90 24 {Y0 + H})">réalité</text>')
o.append(f'<text x="{X0 - 16}" y="{Y0 + H / 2 - 4}" font-size="14" fill="{ENCRE}" text-anchor="end" font-weight="600">pourriel</text>')
o.append(f'<text x="{X0 - 16}" y="{Y0 + H / 2 + 14}" font-size="12" fill="{GRIS}" text-anchor="end">50 en tout</text>')
o.append(f'<text x="{X0 - 16}" y="{Y0 + 3 * H / 2 - 4}" font-size="14" fill="{ENCRE}" text-anchor="end" font-weight="600">légitime</text>')
o.append(f'<text x="{X0 - 16}" y="{Y0 + 3 * H / 2 + 14}" font-size="12" fill="{GRIS}" text-anchor="end">950 en tout</text>')
cases = [(0, 0, VP, "vrais positifs", "pourriels bien jetés", False),
         (1, 0, FN, "faux négatifs", "pourriels passés au travers", True),
         (0, 1, FP, "faux positifs", "vrais courriels jetés", True),
         (1, 1, VN, "vrais négatifs", "vrais courriels bien gardés", False)]
for col, row, n, nom, glose, erreur in cases:
    x, y = X0 + col * W, Y0 + row * H
    fill = ROUGE if erreur else TEAL
    o.append(f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="{fill}" fill-opacity="{0.16 if erreur else 0.10}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{x + W / 2}" y="{y + 40}" font-size="26" fill="{ROUGE if erreur else TEAL}" text-anchor="middle" font-weight="700">{n}</text>')
    o.append(f'<text x="{x + W / 2}" y="{y + 62}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{nom}</text>')
    o.append(f'<text x="{x + W / 2}" y="{y + 80}" font-size="11.5" fill="{GRIS}" text-anchor="middle">{glose}</text>')
yb = Y0 + 2 * H + 40
o.append(f'<g font-size="13" fill="{ENCRE}" text-anchor="middle">')
o.append(f'<text x="330" y="{yb}">Taux de bonnes réponses{NB}: ({VP} + {VN}) / 1000 = {(VP + VN) / 10:.0f}{NB}%, à peine mieux que « jamais un pourriel » (95{NB}%)</text>')
o.append(f'<text x="330" y="{yb + 24}">Précision{NB}: {VP} / ({VP} + {FP}) = {100 * VP / (VP + FP):.0f}{NB}%  ·  Rappel{NB}: {VP} / ({VP} + {FN}) = {100 * VP / (VP + FN):.0f}{NB}%</text>')
o.append('</g>')
o.append('</svg>')
(OUT / "matrice-confusion.svg").write_text("\n".join(o) + "\n")
print("matrice-confusion.svg écrit")
