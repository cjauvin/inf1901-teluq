"""Hors distribution : la droite se prolonge au-delà du nuage, sans garantie."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_maisons import MAISONS, OUT, ajuste  # noqa: E402

FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, AXE, GRILLE = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#b8a888", "#e0d4b8")
NB, FINE = " ", " "
X0, X1 = 80, 630            # zone tracée
M0, M1 = 100, 640           # superficie (m²) couverte par l'axe
P0, P1 = 200, 1900          # prix (k$) couvert par l'axe


def sx(m2):
    return X0 + (m2 - M0) / (M1 - M0) * (X1 - X0)


def sy(prix):
    return 380 - (prix - P0) / (P1 - P0) * 330

MANOIR = 600
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 470" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Hors distribution : la droite répond, mais plus rien ne la garantit</title>",
     f"<desc>Le nuage des vingt maisons (de 112 à 280 m²) et sa droite, avec la zone couverte par les données ombrée. Loin à droite, un manoir de {MANOIR} m² pour lequel la droite, prolongée en pointillé, annonce un prix d'environ {ajuste(MANOIR):.0f} 000 dollars, accompagné d'un point d'interrogation{NB}: le modèle répond avec le même aplomb, mais aucune donnée ne le soutient plus.</desc>",
     f'<rect x="0" y="0" width="660" height="470" rx="14" fill="{FOND}" stroke="{BORD}"/>']
# zone couverte
o.append(f'<rect x="{sx(105):.1f}" y="46" width="{sx(290) - sx(105):.1f}" height="334" fill="{TEAL}" fill-opacity="0.07"/>')
o.append(f'<text x="{(sx(105) + sx(290)) / 2:.0f}" y="66" font-size="12.5" fill="{TEAL}" text-anchor="middle">La zone que les données couvrent</text>')
# grille et axes
for p in (500, 1000, 1500):
    o.append(f'<line x1="{X0}" y1="{sy(p):.1f}" x2="{X1}" y2="{sy(p):.1f}" stroke="{GRILLE}" stroke-width="1"/>')
    o.append(f'<text x="{X0 - 10}" y="{sy(p) + 4.5:.1f}" font-size="13" fill="{ENCRE_PALE}" text-anchor="end">{p if p < 1000 else f"{p // 1000} {p % 1000:03d}"} k$</text>')
o.append(f'<g stroke="{AXE}" stroke-width="1.6"><line x1="{X0}" y1="40" x2="{X0}" y2="380"/><line x1="{X0}" y1="380" x2="{X1}" y2="380"/></g>')
for m in (100, 200, 300, 400, 500, 600):
    o.append(f'<line x1="{sx(m):.1f}" y1="380" x2="{sx(m):.1f}" y2="386" stroke="{AXE}" stroke-width="1.4"/>')
    o.append(f'<text x="{sx(m):.1f}" y="402" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">{m}</text>')
o.append(f'<text x="355" y="430" font-size="15" fill="{ENCRE}" text-anchor="middle">superficie (m²)</text>')
o.append(f'<text x="18" y="210" font-size="15" fill="{ENCRE}" text-anchor="middle" transform="rotate(-90 18 210)">prix de vente</text>')
# droite : pleine dans la zone, pointillée au-delà
o.append(f'<line x1="{sx(105):.1f}" y1="{sy(ajuste(105)):.1f}" x2="{sx(290):.1f}" y2="{sy(ajuste(290)):.1f}" stroke="{BRUN}" stroke-width="2.6"/>')
o.append(f'<line x1="{sx(290):.1f}" y1="{sy(ajuste(290)):.1f}" x2="{sx(MANOIR):.1f}" y2="{sy(ajuste(MANOIR)):.1f}" stroke="{BRUN}" stroke-width="2.2" stroke-dasharray="7 6"/>')
# maisons
o.append(f'<g fill="{TEAL}" stroke="{FOND}" stroke-width="1.4">')
o += [f'<circle cx="{sx(m[0]):.1f}" cy="{sy(m[3]):.1f}" r="5.5"/>' for m in MAISONS]
o.append('</g>')
# manoir
mx, my = sx(MANOIR), sy(ajuste(MANOIR))
o.append(f'<circle cx="{mx:.1f}" cy="{my:.1f}" r="7" fill="none" stroke="{ROUGE}" stroke-width="2"/>')
o.append(f'<text x="{mx + 13:.0f}" y="{my - 6:.0f}" font-size="22" fill="{ROUGE}" text-anchor="start" font-weight="700">?</text>')
o.append(f'<text x="470" y="112" font-size="13" fill="{ENCRE}" text-anchor="end">Un manoir de {MANOIR} m²{NB}: la droite annonce {ajuste(MANOIR):.0f} k$,</text>')
o.append(f'<text x="470" y="130" font-size="12" fill="{GRIS}" text-anchor="end">avec le même aplomb, mais plus rien ne la garantit</text>')
o.append(f'<text x="330" y="458" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">Dans la zone couverte, le score du test veut dire quelque chose{FINE}; au-delà, il ne dit plus rien.</text>')
o.append('</svg>')
(OUT / "hors-distribution.svg").write_text("\n".join(o) + "\n")
print("hors-distribution.svg écrit ; prix du manoir :", round(ajuste(MANOIR)))
