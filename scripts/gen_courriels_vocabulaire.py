import math
OX, OY = 80, 390
L = 300
axes = [("gratuit", 90), ("réunion", 62), ("bonjour", 38), ("zèbre", 0)]
def tip(a, r=L):
    return OX + r*math.cos(math.radians(a)), OY - r*math.sin(math.radians(a))
def dist_to_axis(px, py, a):
    # distance from point to the ray
    ux, uy = math.cos(math.radians(a)), -math.sin(math.radians(a))
    t = (px-OX)*ux + (py-OY)*uy
    t = max(0, min(L, t))
    cx, cy = OX+t*ux, OY+t*uy
    return math.hypot(px-cx, py-cy)
pts_red = [(150, 120), (125, 180), (222, 196), (300, 170)]
pts_blue = [(204, 236), (215, 325), (250, 340), (330, 330)]
for p in pts_red+pts_blue:
    print(p, [round(dist_to_axis(*p, a)) for _, a in axes])
out = []
out.append('<?xml version="1.0" encoding="UTF-8"?>')
out.append('<svg viewBox="0 0 660 480" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">')
out.append("<title>L'espace du vocabulaire : un axe par mot, un courriel par point</title>")
out.append("<desc>Le même dessin que pour l'image faite de pixels, transposé aux mots. D'une origine partent en éventail des axes, un par mot du vocabulaire : « gratuit », « réunion », « bonjour », puis des points de suspension pour les dizaines de milliers d'autres mots, et enfin « zèbre », le dernier. Au milieu, un petit nuage de points : chaque courriel est un point de cet espace, rouge s'il s'agit d'un pourriel, bleu s'il est légitime. L'un d'eux est désigné : « un courriel ».</desc>")
out.append('<rect x="0" y="0" width="660" height="480" rx="14" fill="#efe7d3" stroke="#d9cbac"/>')
out.append('<defs><marker id="fl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#b8a888"/></marker></defs>')
out.append('<g stroke="#b8a888" stroke-width="1.6" marker-end="url(#fl)">')
for name, a in axes:
    x, y = tip(a)
    out.append(f'<line x1="{OX}" y1="{OY}" x2="{x:.1f}" y2="{y:.1f}"/>')
out.append('</g>')
# labels
out.append('<g font-size="15" fill="#3a3531">')
out.append(f'<text x="{OX}" y="74" text-anchor="middle">« gratuit »</text>')
x, y = tip(62); out.append(f'<text x="{x+12:.0f}" y="{y-4:.0f}" text-anchor="start">« réunion »</text>')
x, y = tip(38); out.append(f'<text x="{x+12:.0f}" y="{y+2:.0f}" text-anchor="start">« bonjour »</text>')
x, y = tip(0); out.append(f'<text x="{x+12:.0f}" y="{y+5:.0f}" text-anchor="start">« zèbre »</text>')
out.append('</g>')
# ellipsis dots on an arc
out.append('<g fill="#8c8175">')
for a in (24, 17, 10):
    x, y = tip(a, 306)
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="2.6"/>')
out.append('</g>')
out.append('<g font-size="13" fill="#5b5249" font-style="italic" text-anchor="start">')
out.append('<text x="418" y="292">et des dizaines de milliers</text>')
out.append('<text x="418" y="310">d\'autres mots du vocabulaire</text>')
out.append('</g>')
# leader + label
out.append('<text x="292" y="140" font-size="13" fill="#3a3531" font-style="italic" text-anchor="start">un courriel</text>')
out.append('<line x1="309" y1="146" x2="302" y2="162" stroke="#8c8175" stroke-width="1.2" stroke-dasharray="3 3"/>')
out.append('<g fill="#c4564a" stroke="#efe7d3" stroke-width="1.5">')
for x, y in pts_red: out.append(f'<circle cx="{x}" cy="{y}" r="7"/>')
out.append('</g><g fill="#3a6ea5" stroke="#efe7d3" stroke-width="1.5">')
for x, y in pts_blue: out.append(f'<circle cx="{x}" cy="{y}" r="7"/>')
out.append('</g>')
out.append('<circle cx="170" cy="430" r="7" fill="#c4564a" stroke="#efe7d3" stroke-width="1.5"/>')
out.append('<text x="186" y="434" font-size="14" fill="#3a3531" text-anchor="start">pourriel</text>')
out.append('<circle cx="300" cy="430" r="7" fill="#3a6ea5" stroke="#efe7d3" stroke-width="1.5"/>')
out.append('<text x="316" y="434" font-size="14" fill="#3a3531" text-anchor="start">courriel légitime</text>')
out.append('<text x="330" y="462" font-size="13" fill="#5b5249" text-anchor="middle">Un axe par mot du vocabulaire : chaque courriel est un point de cet espace.</text>')
out.append('</svg>')
open('static/images/module2/courriels-vocabulaire.svg', 'w').write('\n'.join(out)+'\n')
for _, a in axes: print(_, [round(v) for v in tip(a)])
