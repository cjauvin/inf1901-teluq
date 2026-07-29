# gen_troisieme_dim.py
# Génère : static/images/module2/troisieme-dimension.svg
# Usage  : python3 scripts/gen_troisieme_dim.py > static/images/module2/troisieme-dimension.svg
#
# Prévisualiser : qlmanage -t -s 900 -o /tmp <fichier>.svg

import sys

BLUE, RED = "#3a6ea5", "#c4564a"

HOUSES = [
    (114, -95), (120, +45), (127, -48), (133, +82), (140, -72),
    (147, +58), (162, +92), (170, -60), (178, +50),
    (186, -88), (194, +70), (202, -55), (218, -78),
    (226, +86), (234, -42), (242, +62), (250, -66), (258, +95),
    (266, -90),
    (155, -63, "non"), (210, +76, "oui"),
]
def trend(m2): return 380 + 1.50 * (m2 - 110)

DATA = []
for h in HOUSES:
    m2, off = h[0], h[1]
    lab = h[2] if len(h) > 2 else ("oui" if off < 0 else "non")
    DATA.append(((m2 - 100) / 182.0, (trend(m2) + off - 280) / 440.0, lab))

W, H = 700, 470
OX, OY = 150, 348
AXx, AXy = 250.0, 52.0     # axe superficie : vers la droite, un peu vers le bas
AYx, AYy = 104.0, -84.0    # axe prix : vers la droite, vers le haut (profondeur)
ZH = 168.0                 # hauteur entre le barreau 0 et le barreau 1

def P(nx, ny, z):
    return (OX + nx*AXx + ny*AYx, OY + nx*AXy + ny*AYy - z*ZH)

L = []
L.append('<?xml version="1.0" encoding="UTF-8"?>')
L.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">')
L.append("<title>La réponse comme troisième dimension, à deux valeurs</title>")
L.append("<desc>Une vue en perspective. Le plan horizontal porte les deux mêmes axes qu'auparavant : la superficie et le prix. La réponse à la question « vendue en moins de 30 jours ? » occupe un troisième axe, vertical — mais un axe qui ne comporte que deux niveaux : 0 pour non, en bas, et 1 pour oui, en haut. Chaque maison se pose donc sur l'un ou l'autre de deux plans superposés. Vu d'en haut, ce dessin redonne exactement le nuage où la réponse était codée par une couleur.</desc>")
L.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="#efe7d3" stroke="#d9cbac"/>')

def sheet(z, fill, stroke):
    pts = [P(0,0,z), P(1,0,z), P(1,1,z), P(0,1,z)]
    d = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    L.append(f'<polygon points="{d}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')

def dots(z, lab, col):
    L.append(f'<g fill="{col}" stroke="#efe7d3" stroke-width="1.4">')
    for nx, ny, l in DATA:
        if l == lab:
            x, y = P(nx, ny, z)
            L.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6.5"/>')
    L.append('</g>')

# ---- plan du bas : réponse = 0 (non) ----
sheet(0, "rgba(196,86,74,0.07)", "#cbbd9c")
dots(0, "non", RED)

# ---- axe vertical de la réponse (arête avant-gauche) ----
x0, y0 = P(0, 0, 0)
x1, y1 = P(0, 0, 1)
L.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1-26:.1f}" stroke="#8a7d6e" stroke-width="1.8"/>')
for z, lab, sub in ((0, "0", "non"), (1, "1", "oui")):
    xx, yy = P(0, 0, z)
    L.append(f'<line x1="{xx-7:.1f}" y1="{yy:.1f}" x2="{xx:.1f}" y2="{yy:.1f}" stroke="#8a7d6e" stroke-width="1.6"/>')
    L.append(f'<text x="{xx-14:.1f}" y="{yy+5:.1f}" font-size="15" fill="#3a3531" text-anchor="end" font-weight="700">{lab}</text>')
    L.append(f'<text x="{xx-14:.1f}" y="{yy+22:.1f}" font-size="11.5" fill="#7a6f63" text-anchor="end">({sub})</text>')
L.append(f'<text x="{x1-74:.1f}" y="{y1-44:.1f}" font-size="13.5" fill="#3a3531" text-anchor="middle" font-weight="600">vendue vite ?</text>')
L.append(f'<text x="{x1-74:.1f}" y="{y1-27:.1f}" font-size="11.5" fill="#7a6f63" text-anchor="middle" font-style="italic">deux niveaux seulement</text>')

# ---- plan du haut : réponse = 1 (oui) ----
sheet(1, "rgba(58,110,165,0.07)", "#cbbd9c")
dots(1, "oui", BLUE)

# ---- étiquettes des deux axes du plan ----
import math
ax, ay = P(0.5, 0, 0)
angA = math.degrees(math.atan2(AXy, AXx))
L.append(f'<text x="{ax-9:.1f}" y="{ay+34:.1f}" font-size="13.5" fill="#3a3531" text-anchor="middle" transform="rotate({angA:.1f} {ax-9:.1f} {ay+34:.1f})">superficie</text>')
bx, by = P(0, 0.55, 0)
angB = math.degrees(math.atan2(AYy, AYx))
L.append(f'<text x="{bx-12:.1f}" y="{by-13:.1f}" font-size="13.5" fill="#3a3531" text-anchor="middle" transform="rotate({angB:.1f} {bx-12:.1f} {by-13:.1f})">prix</text>')

# ---- légende ----
L.append(f'<text x="{W/2:.0f}" y="{H-24}" font-size="13" fill="#5b5249" text-anchor="middle">La réponse a bel et bien son propre axe — mais un axe qui ne compte que deux barreaux.</text>')

L.append('</svg>')
sys.stdout.write('\n'.join(L))
