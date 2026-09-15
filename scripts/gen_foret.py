"""La forêt aléatoire sur les vingt maisons : trois arbres tirés au sort, puis le vote de cinquante.

Chaque arbre est appris sur un tirage avec remise des vingt maisons (bootstrap)
et laissé pousser librement ; en haut, trois de ces arbres et leurs frontières
en rectangles ; en bas, la frontière du vote majoritaire de cinquante arbres.
"""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from arbre import apprendre, predire  # noqa: E402
from gen_maisons import BLEU, ENCRE, ENCRE_PALE, FOND, MAISONS, OUT, ROUGE  # noqa: E402

AXE, BORD, GRIS, BRUN = "#b8a888", "#d9cbac", "#7a6f63", "#9a5b33"
NB, FINE = " ", " "
EX = [((m[2], m[1]), m[4]) for m in MAISONS]
rng = random.Random(3)
N_ARBRES = 50


def tirage():
    return [EX[rng.randrange(len(EX))] for _ in range(len(EX))]


tirages = [tirage() for _ in range(N_ARBRES)]
arbres = [apprendre(t, 6) for t in tirages]


def vote(x):
    return sum(1 for a in arbres if predire(a, x)) * 2 > len(arbres)


def panneau(ox, oy, L, H, classer, exemples, titre, o, pas=4, rayon=4, absents=()):
    """Un plan distance × année dans le rectangle (ox, oy)-(ox+L, oy+H), fond teinté par `classer`.
    `absents` : les maisons que l'arbre n'a pas vues, dessinées en creux."""
    sx = lambda km: ox + km / 25 * L
    sy = lambda an: oy + H - (an - 1965) / 62 * H
    for i in range(0, L, pas):
        for j in range(0, H, pas):
            km = (i + pas / 2) / L * 25
            an = 1965 + (1 - (j + pas / 2) / H) * 62
            o.append(f'<rect x="{ox + i}" y="{oy + j}" width="{pas}" height="{pas}" fill="{BLEU if classer((km, an)) else ROUGE}" fill-opacity="0.18"/>')
    o.append(f'<rect x="{ox}" y="{oy}" width="{L}" height="{H}" fill="none" stroke="{AXE}" stroke-width="1.2"/>')
    for (km, an), vite in absents:
        o.append(f'<circle cx="{sx(km):.1f}" cy="{sy(an):.1f}" r="{rayon}" fill="none" stroke="{GRIS}" stroke-width="1.2" stroke-dasharray="2 2"/>')
    for (km, an), vite in exemples:
        o.append(f'<circle cx="{sx(km):.1f}" cy="{sy(an):.1f}" r="{rayon}" fill="{BLEU if vite else ROUGE}" stroke="{FOND}" stroke-width="1"/>')
    o.append(f'<text x="{ox + L / 2:.0f}" y="{oy - 8}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{titre}</text>')


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 470" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>La forêt aléatoire : des arbres différents, un vote</title>",
     f"<desc>En haut, trois petits plans distance × année{NB}: trois arbres, chacun appris sur une partie seulement des vingt maisons, tirée au sort (les maisons laissées de côté sont dessinées en creux, et un compte indique combien l'arbre en a vues), et laissé pousser librement, avec des frontières en rectangles toutes différentes et des îlots à des endroits différents. En bas, un plan plus grand{NB}: la frontière obtenue en faisant voter cinquante arbres de ce genre, plus régulière, où les bandes et les îlots des arbres isolés se sont fondus, ne laissant que deux petits îlots autour des exceptions.</desc>",
     f'<rect x="0" y="0" width="660" height="470" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="330" y="32" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="600">Chaque arbre ne voit qu\'une partie des maisons, tirée au sort</text>']
for k in range(3):
    ox = 40 + k * 200
    vues = {(x, y) for x, y in tirages[k]}          # les maisons tirées (sans les doublons)
    ex_k = sorted(vues)
    absents = [e for e in EX if e not in vues]
    panneau(ox, 64, 180, 120, lambda x, a=arbres[k]: predire(a, x), ex_k, f"Arbre {k + 1}", o, absents=absents)
    o.append(f'<text x="{ox + 90}" y="{64 + 120 + 18}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">a vu {len(vues)} maisons sur 20</text>')
o.append(f'<circle cx="190" cy="{64 + 120 + 40}" r="4" fill="{BLEU}"/><text x="200" y="{64 + 120 + 44}" font-size="11.5" fill="{ENCRE_PALE}">maison vue par l\'arbre</text>')
o.append(f'<circle cx="390" cy="{64 + 120 + 40}" r="4" fill="none" stroke="{GRIS}" stroke-width="1.2" stroke-dasharray="2 2"/><text x="400" y="{64 + 120 + 44}" font-size="11.5" fill="{ENCRE_PALE}">maison laissée de côté</text>')
o.append(f'<text x="330" y="258" font-size="14" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le vote de cinquante arbres</text>')
panneau(180, 276, 300, 150, vote, EX, "", o, pas=3, rayon=5)
o.append(f'<text x="330" y="452" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">Chaque arbre se trompe à sa façon{FINE}; leurs erreurs, différentes, se compensent dans le vote.</text>')
o.append('</svg>')
(OUT / "foret-aleatoire.svg").write_text("\n".join(o) + "\n")
err = sum(1 for x, y in EX if vote(x) != y)
print(f"foret-aleatoire.svg écrit ; le vote se trompe sur {err} maison(s) sur 20")
