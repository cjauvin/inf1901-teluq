"""Les arbres de décision sur les vingt maisons du jeu canonique.

  * arbre-maisons.svg : deux arbres côte à côte, à une question et à trois
    niveaux, appris sur (distance, année) → vendue vite ;
  * arbre-maisons-frontiere.svg : le plan distance × année découpé par l'arbre
    à une question (même cadre que maisons-frontiere-k3.svg) ;
  * arbre-maisons-frontiere-profond.svg : le même plan découpé par l'arbre à
    trois niveaux, qui isole les deux exceptions ;
  * arbre-prix-escalier.svg : l'arbre de régression (profondeur 2) sur
    superficie → prix, en escalier sur le nuage, à côté de la droite.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from arbre import apprendre, feuilles  # noqa: E402
from gen_maisons import (BLEU, ENCRE, ENCRE_PALE, FOND, MAISONS, OUT, ROUGE, TEAL, BRUN,  # noqa: E402
                         ajuste, cadre, coord, entete, pa, pd, points, px, py)

NB, FINE = " ", " "
AXE, BORD, GRIS, PANNEAU = "#b8a888", "#d9cbac", "#7a6f63", "#fbf7ee"
NOMS = ["distance du centre", "année de construction"]
UNITES = [" km", ""]
EX = [((m[2], m[1]), m[4]) for m in MAISONS]


def fr(x):
    return f"{x:g}".replace(".", ",")


def question(n, racine=False):
    if n.j == 0:
        return f"à plus de {fr(n.seuil)} km du centre{FINE}?" if racine else f"à plus de {fr(n.seuil)} km{FINE}?"
    return f"construite après {int(n.seuil)}{FINE}?"


def nb_feuilles(n):
    return 1 if n.feuille else nb_feuilles(n.gauche) + nb_feuilles(n.droite)
# NB : « oui » à la question ci-dessus correspond à la branche DROITE (x > seuil).


def dessiner_arbre(n, x0, y, o, pas_y=76, largeur_feuille=92, racine=True, glose=True):
    """Dessine le sous-arbre n dont les feuilles occupent [x0, x0 + nb_feuilles × largeur_feuille]."""
    w_sub = nb_feuilles(n) * largeur_feuille
    x = x0 + w_sub / 2
    if n.feuille:
        ys = [v for _, v in n.exemples]
        k, tot = sum(ys), len(ys)
        couleur = BLEU if 2 * k >= tot else ROUGE
        o.append(f'<circle cx="{x:.1f}" cy="{y + 14}" r="12" fill="{couleur}" stroke="{FOND}" stroke-width="1.5"/>')
        o.append(f'<text x="{x:.1f}" y="{y + 44}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">{k} sur {tot}</text>')
        if glose:
            o.append(f'<text x="{x:.1f}" y="{y + 58}" font-size="11.5" fill="{ENCRE_PALE}" text-anchor="middle">vendues vite</text>')
        return x
    q = question(n, racine)
    w = 7.2 * len(q) + 22
    o.append(f'<rect x="{x - w / 2:.1f}" y="{y}" width="{w:.1f}" height="30" rx="7" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{x:.1f}" y="{y + 20}" font-size="12.5" fill="{ENCRE}" text-anchor="middle" font-weight="600">{q}</text>')
    wg = nb_feuilles(n.gauche) * largeur_feuille
    for enfant, xe0, rep in ((n.gauche, x0, "non"), (n.droite, x0 + wg, "oui")):
        xe = xe0 + nb_feuilles(enfant) * largeur_feuille / 2
        o.append(f'<line x1="{x:.1f}" y1="{y + 30}" x2="{xe:.1f}" y2="{y + pas_y}" stroke="{AXE}" stroke-width="1.4"/>')
        mx, my = (x + xe) / 2, (y + 30 + y + pas_y) / 2
        dx = -10 if rep == "non" else 10
        o.append(f'<text x="{mx + dx:.1f}" y="{my + 4:.1f}" font-size="11.5" fill="{GRIS}" text-anchor="{"end" if rep == "non" else "start"}" font-style="italic">{rep}</text>')
        dessiner_arbre(enfant, xe0, y + pas_y, o, pas_y, largeur_feuille, False, glose)
    return x


# ── arbre-maisons.svg (une question) et arbre-maisons-profond.svg (trois niveaux) ──
t1, t3 = apprendre(EX, 1), apprendre(EX, 3)
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 230" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Un arbre de décision à une seule question</title>",
     f"<desc>Un arbre à une seule question, « à plus de 11 km du centre{FINE}? »{NB}: la branche « non » mène à une feuille bleue, 11 maisons sur 12 vendues vite{FINE}; la branche « oui » à une feuille rouge, 1 sur 8. Deux erreurs sur vingt, les deux exceptions.</desc>",
     f'<rect x="0" y="0" width="660" height="230" rx="14" fill="{FOND}" stroke="{BORD}"/>']
dessiner_arbre(t1, 330 - 140, 40, o, largeur_feuille=140)
o.append(f'<text x="330" y="208" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">une question, deux feuilles{NB}: 2 erreurs sur 20, les deux exceptions</text>')
o.append('</svg>')
(OUT / "arbre-maisons.svg").write_text("\n".join(o) + "\n")

o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 360" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Le même arbre, laissé pousser sur trois niveaux</title>",
     f"<desc>L'arbre laissé pousser sur trois niveaux{NB}: après « à plus de 11 km du centre{FINE}? », il pose des questions sur l'année puis sur la distance jusqu'à isoler chacune des deux exceptions dans une feuille à elle. Six feuilles, chacune annotée du nombre de maisons vendues vite sur le nombre de maisons de la feuille{NB}: plus aucune erreur sur les vingt maisons.</desc>",
     f'<rect x="0" y="0" width="660" height="360" rx="14" fill="{FOND}" stroke="{BORD}"/>']
lf = 96
dessiner_arbre(t3, 330 - nb_feuilles(t3) * lf / 2, 36, o, pas_y=78, largeur_feuille=lf, glose=False)
o.append(f'<text x="330" y="338" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">chaque feuille{NB}: maisons vendues vite sur maisons de la feuille{NB}; 0 erreur sur 20, mais six feuilles</text>')
o.append('</svg>')
(OUT / "arbre-maisons-profond.svg").write_text("\n".join(o) + "\n")


# ── frontières dans le plan distance × année ──────────────────────────────────
def rectangles(n, x0, x1, y0, y1, out):
    """Découpe récursive du plan (en unités : km et années)."""
    if n.feuille:
        ys = [v for _, v in n.exemples]
        out.append((x0, x1, y0, y1, 2 * sum(ys) >= len(ys)))
        return
    if n.j == 0:
        rectangles(n.gauche, x0, n.seuil, y0, y1, out)
        rectangles(n.droite, n.seuil, x1, y0, y1, out)
    else:
        rectangles(n.gauche, x0, x1, y0, n.seuil, out)
        rectangles(n.droite, x0, x1, n.seuil, y1, out)


def frontiere(t, nom, titre, desc, legende):
    rects = []
    rectangles(t, 0, 25, 1965, 2027.3, rects)   # pa(2027.3) ≈ 20 → haut du cadre
    fond = []
    for x0, x1, y0, y1, bleu in rects:
        X0, X1 = pd(x0), pd(x1)
        Y1, Y0 = pa(y0), pa(y1)
        Y0 = max(Y0, 40)
        fond.append(f'<rect x="{X0:.1f}" y="{Y0:.1f}" width="{X1 - X0:.1f}" height="{Y1 - Y0:.1f}" fill="{BLEU if bleu else ROUGE}" fill-opacity="0.16"/>')
    coupes = []
    def tracer(n, x0, x1, y0, y1):
        if n.feuille:
            return
        if n.j == 0:
            coupes.append(f'<line x1="{pd(n.seuil):.1f}" y1="{max(pa(y1), 40):.1f}" x2="{pd(n.seuil):.1f}" y2="{pa(y0):.1f}"/>')
            tracer(n.gauche, x0, n.seuil, y0, y1); tracer(n.droite, n.seuil, x1, y0, y1)
        else:
            coupes.append(f'<line x1="{pd(x0):.1f}" y1="{pa(n.seuil):.1f}" x2="{pd(x1):.1f}" y2="{pa(n.seuil):.1f}"/>')
            tracer(n.gauche, x0, x1, y0, n.seuil); tracer(n.droite, x0, x1, n.seuil, y1)
    tracer(t, 0, 25, 1965, 2027.3)
    svg = entete(500, titre, desc, plan="categorie") + "\n".join(fond) + f'\n<g stroke="{BRUN}" stroke-width="2" stroke-dasharray="7 5">\n' + "\n".join(coupes) + "\n</g>\n" + \
        points(BLEU, 7, "categorie", seulement=True) + "\n" + points(ROUGE, 7, "categorie", seulement=False) + f"""
<circle cx="150" cy="458" r="7" fill="{BLEU}" stroke="{FOND}" stroke-width="1.5"/>
<text x="166" y="462" font-size="14" fill="{ENCRE}" text-anchor="start">vendue en moins de 30 jours</text>
<circle cx="386" cy="458" r="7" fill="{ROUGE}" stroke="{FOND}" stroke-width="1.5"/>
<text x="402" y="462" font-size="14" fill="{ENCRE}" text-anchor="start">a traîné</text>
<text x="355" y="490" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">{legende}</text>
</svg>
"""
    (OUT / f"{nom}.svg").write_text(svg)


frontiere(t1, "arbre-maisons-frontiere",
          "La frontière de l'arbre à une question",
          f"Le plan distance × année des vingt maisons, coupé par une seule ligne verticale pointillée à 11 km{NB}: à gauche, le fond est teinté en bleu (vendue vite), à droite en rouge (a traîné). Les deux exceptions se retrouvent chacune du mauvais côté.",
          "fond : la réponse de l'arbre à une question ; la coupe pointillée est sa frontière")
frontiere(t3, "arbre-maisons-frontiere-profond",
          "La frontière de l'arbre à trois niveaux",
          f"Le même plan, découpé par plusieurs coupes verticales et horizontales en rectangles teintés{NB}: l'arbre a isolé chacune des deux exceptions dans un petit rectangle de sa couleur, au prix d'une frontière en escalier.",
          "fond : la réponse de l'arbre à trois niveaux ; il a taillé un rectangle autour de chaque exception")

# ── arbre-prix-escalier.svg : régression ──────────────────────────────────────
tr = apprendre([((m[0],), m[3]) for m in MAISONS], 2, regression=True)
marches = []
def paliers(n, x0, x1):
    if n.feuille:
        ys = [v for _, v in n.exemples]
        marches.append((x0, x1, sum(ys) / len(ys)))
        return
    paliers(n.gauche, x0, n.seuil); paliers(n.droite, n.seuil, x1)
paliers(tr, 100, 290)
chemin = " ".join(f"{'M' if i == 0 else 'L'}{px(x0):.1f} {py(p):.1f} L{px(x1):.1f} {py(p):.1f}" for i, (x0, x1, p) in enumerate(marches))
svg = entete(460, "L'arbre de régression : le prix par paliers",
             f"Le nuage des maisons (superficie, prix) avec, en pointillé pâle, la droite ajustée, et en trait plein brun un escalier à quatre marches{NB}: l'arbre de régression à deux niveaux de questions coupe la superficie à 194 m², puis à 154 et à 237, et prédit dans chaque intervalle le prix moyen des maisons qui s'y trouvent.") + \
    f'<line x1="{px(100):.1f}" y1="{py(ajuste(100)):.1f}" x2="{px(290):.1f}" y2="{py(ajuste(290)):.1f}" stroke="{BRUN}" stroke-width="1.6" stroke-dasharray="5 5" opacity="0.5"/>\n' + \
    f'<path d="{chemin}" fill="none" stroke="{BRUN}" stroke-width="3" stroke-linejoin="round"/>\n' + points() + \
    f'\n<text x="355" y="450" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">en pointillé, la droite d\'*Un modèle qui s\'entraîne*{NB}; en plein, l\'arbre à deux niveaux (quatre paliers)</text>\n</svg>\n'
svg = svg.replace("d'*Un modèle qui s'entraîne*", "d'Un modèle qui s'entraîne")
(OUT / "arbre-prix-escalier.svg").write_text(svg)
print("5 figures écrites ; paliers :", [(x0, x1, round(p)) for x0, x1, p in marches])
