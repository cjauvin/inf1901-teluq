"""Précision et rappel, illustrés avec les nombres de la matrice de confusion.

À gauche, les courriels comme des points (rouge = pourriel, bleu = légitime) et
le lasso de ce que le filtre a jeté ; à droite, les deux fractions sous forme de
barres : précision (parmi les jetés) et rappel (parmi les pourriels).
"""
import math
import random
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
VP, FN, FP = 40, 10, 20          # mêmes nombres que la matrice de confusion
CX, CY, RX, RY = 165, 215, 98, 78   # le lasso
rng = random.Random(7)


def dans_lasso(x, y, marge=0):
    return ((x - CX) / (RX - marge)) ** 2 + ((y - CY) / (RY - marge)) ** 2 <= 1


# positions sur une grille, légèrement chahutées
interieur, exterieur = [], []
for gx in range(46, 320, 15):
    for gy in range(96, 340, 15):
        x, y = gx + rng.uniform(-3, 3), gy + rng.uniform(-3, 3)
        if CX - 100 <= x <= CX + 100 and CY - RY - 30 <= y <= CY - RY - 2:
            continue  # zone réservée au label du lasso
        if dans_lasso(x, y, 11):
            interieur.append((x, y))
        elif not dans_lasso(x, y, -11):
            exterieur.append((x, y))
rng.shuffle(interieur)
rng.shuffle(exterieur)
assert len(interieur) >= VP + FP and len(exterieur) >= FN + 48
rouges = interieur[:VP] + exterieur[:FN]
bleus = interieur[VP:VP + FP] + exterieur[FN:FN + 48]

o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 440" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     '<title>Précision et rappel</title>',
     f"<desc>À gauche, des courriels figurés par des points, rouges pour les pourriels, bleus pour les légitimes, et un lasso pointillé autour de ce que le filtre a jeté{NB}: 40 rouges et 20 bleus à l'intérieur, 10 rouges restés dehors. À droite, deux barres. La barre de la précision représente les 60 courriels jetés, dont 40 rouges{NB}: 67{NB}%. La barre du rappel représente les 50 vrais pourriels, dont 40 attrapés{NB}: 80{NB}%.</desc>",
     f'<rect x="0" y="0" width="660" height="440" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="330" y="40" font-size="16" fill="{ENCRE}" text-anchor="middle" font-weight="600">Deux questions, deux dénominateurs</text>']
# panneau de gauche
o.append(f'<rect x="32" y="82" width="300" height="270" rx="10" fill="{TEAL}" fill-opacity="0.05" stroke="{AXE}" stroke-width="1.2"/>')
o.append(f'<text x="182" y="372" font-size="12.5" fill="{GRIS}" text-anchor="middle">Les courriels (une partie des 950 légitimes est montrée)</text>')
o.append(f'<ellipse cx="{CX}" cy="{CY}" rx="{RX}" ry="{RY}" fill="{BRUN}" fill-opacity="0.10" stroke="{BRUN}" stroke-width="1.6" stroke-dasharray="6 5"/>')
o.append(f'<g fill="{BLEU}" stroke="{FOND}" stroke-width="1">')
o += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.6"/>' for x, y in bleus]
o.append('</g>')
o.append(f'<g fill="{ROUGE}" stroke="{FOND}" stroke-width="1">')
o += [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.6"/>' for x, y in rouges]
o.append('</g>')
o.append(f'<text x="{CX}" y="{CY - RY - 12}" font-size="13" fill="{BRUN}" text-anchor="middle" font-weight="600">Ce que le filtre a jeté</text>')
# barres à droite
BX, BW, BH = 362, 270, 30


def barre(y, titre, parts, formule, glose1, glose2):
    o.append(f'<text x="{BX}" y="{y - 12}" font-size="14" fill="{ENCRE}" font-weight="600">{titre}</text>')
    total = sum(n for n, _ in parts)
    x = BX
    for n, col in parts:
        w = BW * n / total
        o.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{BH}" fill="{col}" stroke="{FOND}" stroke-width="1.2"/>')
        o.append(f'<text x="{x + w / 2:.1f}" y="{y + BH / 2 + 5}" font-size="13" fill="{PANNEAU}" text-anchor="middle" font-weight="700">{n}</text>')
        x += w
    o.append(f'<text x="{BX}" y="{y + BH + 22}" font-size="13" fill="{ENCRE}">{formule}</text>')
    o.append(f'<text x="{BX}" y="{y + BH + 40}" font-size="12" fill="{GRIS}">{glose1}</text>')
    o.append(f'<text x="{BX}" y="{y + BH + 56}" font-size="12" fill="{GRIS}">{glose2}</text>')


barre(118, "Précision", [(VP, ROUGE), (FP, BLEU)],
      f"= 40 / 60 = 67{NB}%", "Parmi ce que le filtre a jeté,", "la part de vrais pourriels")
barre(262, "Rappel", [(VP, ROUGE), (FN, "#e0a89f")],
      f"= 40 / 50 = 80{NB}%", "Parmi les vrais pourriels,", "la part que le filtre a attrapée")
# légende
ly = 402
o.append(f'<circle cx="150" cy="{ly}" r="5" fill="{ROUGE}"/><text x="160" y="{ly + 4}" font-size="12.5" fill="{ENCRE}">pourriel</text>')
o.append(f'<circle cx="240" cy="{ly}" r="5" fill="{BLEU}"/><text x="250" y="{ly + 4}" font-size="12.5" fill="{ENCRE}">courriel légitime</text>')
o.append(f'<rect x="380" y="{ly - 6}" width="14" height="12" fill="#e0a89f"/><text x="400" y="{ly + 4}" font-size="12.5" fill="{ENCRE}">pourriels passés au travers</text>')
o.append('</svg>')
(OUT / "precision-rappel.svg").write_text("\n".join(o) + "\n")
print(f"precision-rappel.svg écrit ({len(rouges)} rouges, {len(bleus)} bleus)")
