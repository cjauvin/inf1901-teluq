# gen_deux_axes.py
# Génère : (abandonné — panneau 2D remplacé par la version 3D)
# Usage  : python3 scripts/gen_deux_axes.py > (abandonné — panneau 2D remplacé par la version 3D)
#
# Prévisualiser : qlmanage -t -s 900 -o /tmp <fichier>.svg

import sys

TEAL, BLUE, RED = "#2f6f6a", "#3a6ea5", "#c4564a"

# Mêmes maisons que maisons-vendues.svg
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
    DATA.append((m2, trend(m2) + off, lab))

W, H = 780, 350
L = []
L.append('<?xml version="1.0" encoding="UTF-8"?>')
L.append(f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">')
L.append("<title>Un axe continu ou un axe à deux barreaux</title>")
L.append("<desc>Deux graphiques côte à côte. À gauche, « combien vaut-elle ? » : le prix de vente en fonction de la superficie ; les points se répartissent librement sur toute la hauteur, car l'axe des réponses est continu. À droite, « va-t-elle partir vite ? » : la réponse en fonction du prix ; l'axe des réponses ne comporte que deux barreaux, 0 pour non et 1 pour oui, et les points ne peuvent se poser que sur l'un ou l'autre. Les maisons les moins chères se posent surtout sur le barreau du haut, les plus chères sur celui du bas.</desc>")
L.append(f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="#efe7d3" stroke="#d9cbac"/>')

TOP, BOT = 78, 258

def frame(x0, x1, title, sub):
    L.append(f'<line x1="{x0}" y1="{TOP-10}" x2="{x0}" y2="{BOT}" stroke="#b8a888" stroke-width="1.6"/>')
    L.append(f'<line x1="{x0}" y1="{BOT}" x2="{x1+14}" y2="{BOT}" stroke="#b8a888" stroke-width="1.6"/>')
    L.append(f'<text x="{(x0+x1)/2:.0f}" y="30" font-size="15" fill="#3a3531" text-anchor="middle" font-weight="700">{title}</text>')
    L.append(f'<text x="{(x0+x1)/2:.0f}" y="52" font-size="11.5" fill="#7a6f63" text-anchor="middle" font-style="italic">{sub}</text>')

# ---------------- panneau gauche : prix (axe continu) ----------------
LX0, LX1 = 82, 330
def lx(m2):   return LX0 + (m2 - 105) * (LX1 - LX0) / 170.0
def ly(p):    return BOT - (p - 280) * (BOT - TOP) / 440.0

frame(LX0, LX1, "combien vaut-elle ?", "axe continu : n'importe quelle hauteur")
for m2 in (150, 200, 250):
    L.append(f'<line x1="{lx(m2):.1f}" y1="{BOT}" x2="{lx(m2):.1f}" y2="{BOT+6}" stroke="#b8a888" stroke-width="1.3"/>')
    L.append(f'<text x="{lx(m2):.1f}" y="{BOT+20}" font-size="11.5" fill="#5b5249" text-anchor="middle">{m2}</text>')
for p in (300, 400, 500, 600, 700):
    L.append(f'<line x1="{LX0}" y1="{ly(p):.1f}" x2="{LX1+14}" y2="{ly(p):.1f}" stroke="#e5dac0" stroke-width="1"/>')
    L.append(f'<line x1="{LX0-6}" y1="{ly(p):.1f}" x2="{LX0}" y2="{ly(p):.1f}" stroke="#b8a888" stroke-width="1.3"/>')
    L.append(f'<text x="{LX0-10}" y="{ly(p)+4:.1f}" font-size="11.5" fill="#5b5249" text-anchor="end">{p} k$</text>')
L.append('<g fill="%s" stroke="#efe7d3" stroke-width="1.4">' % TEAL)
for m2, p, lab in DATA:
    L.append(f'<circle cx="{lx(m2):.1f}" cy="{ly(p):.1f}" r="6"/>')
L.append('</g>')
L.append(f'<text x="{(LX0+LX1)/2:.0f}" y="{BOT+40}" font-size="13" fill="#3a3531" text-anchor="middle">superficie (m²)</text>')
L.append(f'<text x="20" y="{(TOP+BOT)/2:.0f}" font-size="13" fill="#3a3531" text-anchor="middle" transform="rotate(-90 20 {(TOP+BOT)/2:.0f})">prix de vente</text>')

# ---------------- panneau droit : réponse 0/1 (deux barreaux) ----------------
RX0, RX1 = 500, 736
def rx(p):    return RX0 + (p - 285) * (RX1 - RX0) / 420.0
Y1, Y0 = 122, 216          # barreau 1 (oui) et barreau 0 (non)

frame(RX0, RX1, "va-t-elle partir vite ?", "deux barreaux seulement : 0 ou 1")
for yy, lab, sub in ((Y1, "1", "oui"), (Y0, "0", "non")):
    L.append(f'<line x1="{RX0}" y1="{yy}" x2="{RX1+14}" y2="{yy}" stroke="#e5dac0" stroke-width="1.4" stroke-dasharray="6 5"/>')
    L.append(f'<line x1="{RX0-6}" y1="{yy}" x2="{RX0}" y2="{yy}" stroke="#b8a888" stroke-width="1.3"/>')
    L.append(f'<text x="{RX0-10}" y="{yy+4}" font-size="13" fill="#3a3531" text-anchor="end" font-weight="700">{lab}</text>')
    L.append(f'<text x="{RX0-10}" y="{yy+19}" font-size="11" fill="#7a6f63" text-anchor="end">({sub})</text>')
for p in (300, 400, 500, 600, 700):
    L.append(f'<line x1="{rx(p):.1f}" y1="{BOT}" x2="{rx(p):.1f}" y2="{BOT+6}" stroke="#b8a888" stroke-width="1.3"/>')
    L.append(f'<text x="{rx(p):.1f}" y="{BOT+20}" font-size="11.5" fill="#5b5249" text-anchor="middle">{p} k$</text>')
for m2, p, lab in DATA:
    yy = Y1 if lab == "oui" else Y0
    col = BLUE if lab == "oui" else RED
    L.append(f'<circle cx="{rx(p):.1f}" cy="{yy}" r="6" fill="{col}" stroke="#efe7d3" stroke-width="1.4"/>')
L.append(f'<text x="{(RX0+RX1)/2:.0f}" y="{BOT+40}" font-size="13" fill="#3a3531" text-anchor="middle">prix de vente</text>')
L.append(f'<text x="440" y="{(TOP+BOT)/2:.0f}" font-size="13" fill="#3a3531" text-anchor="middle" transform="rotate(-90 440 {(TOP+BOT)/2:.0f})">vendue vite ?</text>')

# ---------------- légende ----------------
L.append(f'<text x="{W/2:.0f}" y="332" font-size="13" fill="#5b5249" text-anchor="middle">Même geste des deux côtés : deviner la hauteur d\'un point à partir de sa position horizontale.</text>')

L.append('</svg>')
sys.stdout.write('\n'.join(L))
