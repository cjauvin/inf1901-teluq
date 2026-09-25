"""Un petit arbre de jeu : minimax et élagage.

MAX joue à la racine, MIN aux trois nœuds du milieu, et les feuilles portent
l'estimation heuristique de la position. Les valeurs remontent (minimum chez
MIN, maximum chez MAX) ; au deuxième nœud MIN, dès qu'une feuille vaut 2
(moins que le 3 déjà garanti ailleurs), les deux autres feuilles sont élaguées.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module1"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
FEUILLES = [[3, 12, 8], [2, 4, 6], [14, 5, 2]]
ELAGUEES = {(1, 1), (1, 2)}          # (nœud MIN, rang de la feuille)

valeurs_min = [3, 2, 2]              # le 2 du deuxième nœud est une borne : « au plus 2 »
racine = max(valeurs_min)

W, H = 660, 430
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Minimax et élagage sur un petit arbre de jeu</title>",
     f"<desc>Un arbre de jeu à trois niveaux. À la racine, c'est à la machine (MAX) de jouer{NB}; au niveau suivant, trois coups de l'adversaire (MIN){NB}; en bas, neuf positions estimées par une heuristique. Chaque nœud MIN prend le minimum de ses feuilles{NB}: 3, au plus 2, et 2. La racine prend le maximum{NB}: 3, et la flèche épaisse montre le coup choisi. Au deuxième nœud MIN, dès que la feuille 2 est vue, les deux autres feuilles sont barrées{NB}: l'élagage, car ce coup ne peut plus battre le 3 déjà garanti.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>']
RY, MY, FY = 62, 175, 300
rx = 300
mx = [115, 300, 485]
fx = [[m - 60, m, m + 60] for m in mx]

# arêtes
for i, m in enumerate(mx):
    choisi = i == 0
    o.append(f'<line x1="{rx}" y1="{RY + 24}" x2="{m}" y2="{MY - 24}" stroke="{TEAL if choisi else AXE}" stroke-width="{4 if choisi else 1.6}"/>')
    for j, x in enumerate(fx[i]):
        el = (i, j) in ELAGUEES
        o.append(f'<line x1="{m}" y1="{MY + 24}" x2="{x}" y2="{FY - 18}" stroke="{AXE}" stroke-width="1.6"' + (' stroke-dasharray="4 4" opacity="0.6"' if el else '') + '/>')
        if el:
            cx, cy = (m + x) / 2, (MY + 24 + FY - 18) / 2
            o.append(f'<path d="M{cx - 9} {cy - 9} L{cx + 9} {cy + 9} M{cx - 9} {cy + 9} L{cx + 9} {cy - 9}" stroke="{ROUGE}" stroke-width="2.4" stroke-linecap="round"/>')

# racine (MAX) : triangle pointe en haut
o.append(f'<polygon points="{rx},{RY - 26} {rx - 30},{RY + 24} {rx + 30},{RY + 24}" fill="{PANNEAU}" stroke="{TEAL}" stroke-width="2"/>')
o.append(f'<text x="{rx}" y="{RY + 16}" font-size="16" fill="{ENCRE}" text-anchor="middle" font-weight="700">{racine}</text>')
o.append(f'<text x="{rx + 44}" y="{RY + 6}" font-size="12.5" fill="{TEAL}" font-weight="600">MAX{NB}: la machine joue</text>')
o.append(f'<text x="{rx + 44}" y="{RY + 22}" font-size="11.5" fill="{GRIS}">elle prend le plus grand</text>')
# nœuds MIN : triangles pointe en bas
for i, m in enumerate(mx):
    v = "≤" + NB + "2" if i == 1 else str(valeurs_min[i])
    o.append(f'<polygon points="{m - 30},{MY - 24} {m + 30},{MY - 24} {m},{MY + 26}" fill="{PANNEAU}" stroke="{BRUN}" stroke-width="2"/>')
    o.append(f'<text x="{m}" y="{MY - 4}" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="700">{v}</text>')
o.append(f'<text x="{mx[2] + 44}" y="{MY - 6}" font-size="12.5" fill="{BRUN}" font-weight="600">MIN{NB}: l\'adversaire</text>')
o.append(f'<text x="{mx[2] + 44}" y="{MY + 10}" font-size="11.5" fill="{GRIS}">il prend le plus petit</text>')
# feuilles
for i in range(3):
    for j, x in enumerate(fx[i]):
        el = (i, j) in ELAGUEES
        o.append(f'<rect x="{x - 18}" y="{FY - 18}" width="36" height="32" rx="6" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.3"' + (' stroke-dasharray="4 3" opacity="0.55"' if el else '') + '/>')
        o.append(f'<text x="{x}" y="{FY + 4}" font-size="14" fill="{ENCRE if not el else GRIS}" text-anchor="middle"' + (' opacity="0.6"' if el else '') + f'>{FEUILLES[i][j] if not el else "?"}</text>')
o.append(f'<text x="330" y="{FY + 46}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">En bas{NB}: l\'estimation heuristique de chaque position (compter les pièces, le contrôle du centre…)</text>')
o.append(f'<text x="330" y="{FY + 72}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">Élagage{NB}: au milieu, dès que l\'adversaire peut obtenir 2, ce coup ne battra plus le 3 déjà garanti{FINE};</text>')
o.append(f'<text x="330" y="{FY + 90}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">inutile d\'examiner les deux dernières positions.</text>')
o.append('</svg>')
(OUT / "minimax-elagage.svg").write_text("\n".join(o) + "\n")
print("minimax-elagage.svg écrit")
