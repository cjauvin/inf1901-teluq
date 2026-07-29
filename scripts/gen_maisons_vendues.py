# gen_maisons_vendues.py
# Génère : static/images/module2/maisons-vendues.svg
# Usage  : python3 scripts/gen_maisons_vendues.py > static/images/module2/maisons-vendues.svg
#
# Prévisualiser : qlmanage -t -s 900 -o /tmp <fichier>.svg

import sys

BLUE, RED = "#3a6ea5", "#c4564a"

def px(m2):    return 80 + (m2 - 100) * 2.894
def py(price):  return 351.7 - (price - 300) * 0.567   # price en k$

def trend(m2):  return 380 + 1.50 * (m2 - 110)

# (superficie, écart au prix de tendance en k$) — écart négatif = bonne affaire → part vite
HOUSES = [
    (114, -95), (120, +45), (127, -48), (133, +82), (140, -72),
    (147, +58), (162, +92), (170, -60), (178, +50),
    (186, -88), (194, +70), (202, -55), (218, -78),
    (226, +86), (234, -42), (242, +62), (250, -66), (258, +95),
    (266, -90),
    (155, -63, "non"), (210, +76, "oui"),
]

L = []
L.append('<?xml version="1.0" encoding="UTF-8"?>')
L.append('<svg viewBox="0 0 660 500" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">')
L.append('<title>Les mêmes maisons, mais la réponse est maintenant une catégorie</title>')
L.append("<desc>Le même nuage de points : chaque maison est placée selon sa superficie (axe horizontal) et son prix (axe vertical). Cette fois, ce n'est plus la hauteur du point qu'on cherche à prédire, mais sa couleur : en bleu les maisons vendues en moins de 30 jours, en rouge celles qui ont traîné. Les maisons peu chères pour leur superficie (sous la tendance générale) partent vite ; les plus chères pour ce qu'elles offrent traînent — avec quelques exceptions.</desc>")
L.append('<rect x="0" y="0" width="660" height="500" rx="14" fill="#efe7d3" stroke="#d9cbac"/>')

# lignes de repère
L.append('<g stroke="#e0d4b8" stroke-width="1">')
for y in (351.7, 238.3, 125):
    L.append(f'<line x1="80" y1="{y}" x2="630" y2="{y}"/>')
L.append('</g>')

# axes
L.append('<g stroke="#b8a888" stroke-width="1.6">')
L.append('<line x1="80" y1="40" x2="80" y2="380"/>')
L.append('<line x1="80" y1="380" x2="630" y2="380"/>')
L.append('</g>')

# graduations X
L.append('<g stroke="#b8a888" stroke-width="1.4">')
for x in (80, 224.7, 369.5, 514.2):
    L.append(f'<line x1="{x}" y1="380" x2="{x}" y2="386"/>')
L.append('</g>')
L.append('<g font-size="13" fill="#5b5249" text-anchor="middle">')
for x, lab in ((80, "100"), (224.7, "150"), (369.5, "200"), (514.2, "250")):
    L.append(f'<text x="{x}" y="402">{lab}</text>')
L.append('<text x="355" y="430" font-size="15" fill="#3a3531">superficie (m²)</text>')
L.append('</g>')

# graduations Y
L.append('<g stroke="#b8a888" stroke-width="1.4">')
for y in (351.7, 238.3, 125):
    L.append(f'<line x1="74" y1="{y}" x2="80" y2="{y}"/>')
L.append('</g>')
L.append('<g font-size="13" fill="#5b5249" text-anchor="end">')
for y, lab in ((356, "300 k$"), (242.8, "500 k$"), (129.5, "700 k$")):
    L.append(f'<text x="68" y="{y}">{lab}</text>')
L.append('</g>')
L.append('<text x="18" y="210" font-size="15" fill="#3a3531" text-anchor="middle" transform="rotate(-90 18 210)">prix de vente</text>')

# points
L.append('<g stroke="#efe7d3" stroke-width="1.5">')
for h in HOUSES:
    m2, off = h[0], h[1]
    forced = h[2] if len(h) > 2 else None
    lab = forced if forced else ("oui" if off < 0 else "non")
    col = BLUE if lab == "oui" else RED
    L.append(f'<circle cx="{px(m2):.1f}" cy="{py(trend(m2)+off):.1f}" r="7" fill="{col}"/>')
L.append('</g>')

# légende
LY = 462
L.append(f'<circle cx="176" cy="{LY-4}" r="7" fill="{BLUE}" stroke="#efe7d3" stroke-width="1.5"/>')
L.append(f'<text x="192" y="{LY}" font-size="14" fill="#3a3531" text-anchor="start">vendue en moins de 30 jours</text>')
L.append(f'<circle cx="412" cy="{LY-4}" r="7" fill="{RED}" stroke="#efe7d3" stroke-width="1.5"/>')
L.append(f'<text x="428" y="{LY}" font-size="14" fill="#3a3531" text-anchor="start">a traîné</text>')

L.append('</svg>')
sys.stdout.write('\n'.join(L))
