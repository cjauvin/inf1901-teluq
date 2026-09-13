"""L'espace du vocabulaire : le courriel entier est un point (miroir de nd_house.png)."""
import math

OX, OY = 70, 340
L = 270
AXES = [("gratuit", 90), ("réunion", 62), ("bonjour", 38), ("zèbre", 0)]


def tip(a, r=L):
    return OX + r * math.cos(math.radians(a)), OY - r * math.sin(math.radians(a))


def dist_to_axis(px, py, a):
    ux, uy = math.cos(math.radians(a)), -math.sin(math.radians(a))
    t = max(0, min(L, (px - OX) * ux + (py - OY) * uy))
    return math.hypot(px - (OX + t * ux), py - (OY + t * uy))


# vignette (le courriel, vu de loin) et panneau (le même, agrandi)
VX, VY, VW, VH = 206, 139, 32, 42
PX, PY, PW, PH = 430, 100, 210, 210
ROUGES = [(172, 202), (255, 250)]
BLEUS = [(160, 220), (145, 240), (290, 275)]
AUTRES = ROUGES + BLEUS

for p in [(VX, VY), (VX + VW, VY), (VX, VY + VH), (VX + VW, VY + VH)] + AUTRES:
    print(p, [round(dist_to_axis(*p, a)) for _, a in AXES])

o = []
o.append('<?xml version="1.0" encoding="UTF-8"?>')
o.append('<svg viewBox="0 0 660 450" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">')
o.append("<title>L'espace du vocabulaire : le courriel entier est un seul point</title>")
o.append("<desc>Le même dessin que pour l'image faite de pixels, transposé aux mots. D'une origine partent en éventail des axes, un par mot du vocabulaire : « gratuit », « réunion », « bonjour », trois points pour les dizaines de milliers d'autres mots, puis « zèbre », le dernier. Dans cet espace est posée une vignette minuscule, un courriel vu de loin, reliée par des pointillés à un panneau agrandi où on le lit : « Objet : Cliquez ici, c'est gratuit ! », suivi d'un boniment publicitaire. La vignette et le panneau sont bordés de rouge, c'est un pourriel. À côté, d'autres courriels : des points rouges (pourriels) et bleus (courriels légitimes).</desc>")
o.append('<rect x="0" y="0" width="660" height="450" rx="14" fill="#efe7d3" stroke="#d9cbac"/>')
o.append('<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#b8a888"/></marker></defs>')
o.append('<g stroke="#b8a888" stroke-width="1.6" marker-end="url(#fl)">')
for _, a in AXES:
    x, y = tip(a)
    o.append(f'<line x1="{OX}" y1="{OY}" x2="{x:.1f}" y2="{y:.1f}"/>')
o.append('</g>')
o.append('<g font-size="15" fill="#3a3531">')
o.append(f'<text x="{OX}" y="54" text-anchor="middle">« gratuit »</text>')
x, y = tip(62); o.append(f'<text x="{x:.0f}" y="{y-14:.0f}" text-anchor="middle">« réunion »</text>')
x, y = tip(38); o.append(f'<text x="{x+12:.0f}" y="{y+4:.0f}" text-anchor="start">« bonjour »</text>')
x, y = tip(0); o.append(f'<text x="{x+12:.0f}" y="{y+5:.0f}" text-anchor="start">« zèbre »</text>')
o.append('</g>')
o.append('<g fill="#8c8175">')
for a in (20, 13, 6):
    x, y = tip(a, 255)
    o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6"/>')
o.append('</g>')

# pointillés vignette → panneau
o.append('<g stroke="#8c8175" stroke-width="1.2" stroke-dasharray="4 4" fill="none">')
o.append(f'<line x1="{VX+VW}" y1="{VY}" x2="{PX}" y2="{PY}"/>')
o.append(f'<line x1="{VX+VW}" y1="{VY+VH}" x2="{PX}" y2="{PY+PH}"/>')
o.append('</g>')

# autres courriels
o.append('<g fill="#c4564a" stroke="#efe7d3" stroke-width="1.5">')
for x, y in ROUGES:
    o.append(f'<circle cx="{x}" cy="{y}" r="6"/>')
o.append('</g><g fill="#3a6ea5" stroke="#efe7d3" stroke-width="1.5">')
for x, y in BLEUS:
    o.append(f'<circle cx="{x}" cy="{y}" r="6"/>')
o.append('</g>')

# vignette
o.append(f'<rect x="{VX}" y="{VY}" width="{VW}" height="{VH}" fill="#fbf7ee" stroke="#c4564a" stroke-width="1.6"/>')
o.append('<g stroke="#b8a888" stroke-width="1" stroke-linecap="round">')
lignes = [(0.8, "#8c8175"), (0.9, None), (0.7, None), (0.85, None), (0.6, None), (0.9, None), (0.4, None)]
for i, (f, c) in enumerate(lignes):
    y = VY + 6 + i * 5
    col = f' stroke="{c}"' if c else ''
    o.append(f'<line x1="{VX+4}" y1="{y}" x2="{VX+4+f*(VW-8):.1f}" y2="{y}"{col}/>')
o.append('</g>')

# panneau
o.append('<text x="535" y="88" font-size="13" fill="#5b5249" font-style="italic" text-anchor="middle">le même courriel, de près</text>')
o.append(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="4" fill="#fbf7ee" stroke="#c4564a" stroke-width="1.6"/>')
o.append(f'<text x="{PX+12}" y="{PY+24}" font-size="11" fill="#3a3531" font-weight="700">Objet : Cliquez ici, c\'est gratuit !</text>')
o.append(f'<line x1="{PX+12}" y1="{PY+34}" x2="{PX+PW-12}" y2="{PY+34}" stroke="#d9cbac" stroke-width="1"/>')
corps = ["Félicitations ! Vous avez été", "choisi pour recevoir un", "téléphone dernier cri. Cliquez", "ici avant minuit : livraison", "offerte, sans engagement.", "Offre réservée aux 100", "premiers, ne tardez pas !"]
o.append('<g font-size="12" fill="#5b5249">')
for i, l in enumerate(corps):
    o.append(f'<text x="{PX+12}" y="{PY+58+i*20}">{l}</text>')
o.append('</g>')

o.append('<circle cx="200" cy="376" r="6" fill="#c4564a" stroke="#efe7d3" stroke-width="1.5"/>')
o.append('<text x="214" y="380" font-size="14" fill="#3a3531">pourriel</text>')
o.append('<circle cx="320" cy="376" r="6" fill="#3a6ea5" stroke="#efe7d3" stroke-width="1.5"/>')
o.append('<text x="334" y="380" font-size="14" fill="#3a3531">courriel légitime</text>')
o.append('<g font-size="13" fill="#5b5249" text-anchor="middle">')
o.append('<text x="330" y="410">Le courriel entier est un seul point de cet espace ; les autres points, d\'autres courriels.</text>')
o.append('<text x="330" y="430">Un axe par mot du vocabulaire, donc des dizaines de milliers d\'axes.</text>')
o.append('</g>')
o.append('</svg>')
open('static/images/module2/courriels-vocabulaire.svg', 'w').write('\n'.join(o) + '\n')
