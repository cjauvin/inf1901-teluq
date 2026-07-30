#!/usr/bin/env python3
"""Génère les cinq figures du fil rouge « maisons » du Module 2.

Source de vérité unique : la liste MAISONS ci-dessous. Toutes les figures des
pages 10 et 20 en découlent, ce qui garantit trois choses que la version
précédente ne tenait pas :

  * la p. 10 peut dire « reprenons exactement le même dessin » — c'est vrai ;
  * le prix moyen vaut exactement 500 k$, comme l'annonce la p. 20 ;
  * 12 maisons sur 20 se vendent vite, soit exactement les 60 % de l'étalon.

Usage :
    uv run scripts/gen_maisons.py

Écrit dans static/images/module2/ :
    maisons-nuage.svg            (p. 10) le nuage prix / superficie
    maisons-vendues.svg          (p. 10) le même, colorié par vendue-vite
    maisons-baseline.svg         (p. 20) le nuage + la droite du prix moyen
    maisons-erreurs.svg          (p. 20) idem + les écarts verticaux
    maisons-erreurs-oui-non.svg  (p. 20) le prédicteur majoritaire et ses ratés

Prévisualisation (rsvg-convert n'est plus installé) :
    qlmanage -t -s 900 -o /tmp static/images/module2/maisons-nuage.svg
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"

# ── Le jeu de données canonique ───────────────────────────────────────────────
# (superficie m², prix k$, vendue en moins de 30 jours)
#
# Contrainte : les quatre maisons des tables de la p. 10 doivent s'y trouver,
# avec leurs valeurs exactes — la p. 30 reprend d'ailleurs deux d'entre elles
# comme vecteurs dans nf_house.png. Elles sont marquées « table » ci-dessous.
#
# Structure : à superficie comparable, les maisons les moins chères partent
# vite. La séparation suit à peu près 2,55 k$ par m² ; trois maisons refusent
# d'entrer dans le rang, et deux d'entre elles viennent justement de la table —
# ce sont les données qui commandent, pas l'inverse.
MAISONS = [
    (112, 275, True),
    (120, 300, True),
    (126, 440, False),
    (130, 310, False),   # table — exception : bon marché pour sa taille, et pourtant traînée
    (140, 345, True),
    (150, 350, False),   # table — exception : bon marché pour sa taille, et pourtant traînée
    (156, 520, False),
    (160, 395, True),
    (170, 425, True),
    (176, 570, False),
    (180, 420, True),    # table
    (188, 635, False),
    (196, 590, True),    # exception : chère pour sa taille, et pourtant partie vite
    (208, 515, True),
    (220, 580, True),    # table
    (226, 705, False),
    (232, 578, True),
    (248, 617, True),
    (256, 792, False),
    (264, 638, True),
]

# ── Palette parchemin ─────────────────────────────────────────────────────────
FOND, BORD, GRILLE, AXE = "#efe7d3", "#d9cbac", "#e0d4b8", "#b8a888"
ENCRE, ENCRE_PALE = "#3a3531", "#5b5249"
TEAL, BRUN, ROUGE, BLEU = "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5"

# ── Repère : superficie 100 m² → x=80, 150 m² → x=224.7 ; 300 k$ → y=351.7 ────
def px(m2):
    return 80 + (m2 - 100) * 2.894


def py(prix_k):
    return 351.7 - (prix_k - 300) * 0.567


def cadre(hauteur):
    """Le fond, la grille, les axes et leurs étiquettes — identiques partout."""
    return f"""<rect x="0" y="0" width="660" height="{hauteur}" rx="14" fill="{FOND}" stroke="{BORD}"/>

<g stroke="{GRILLE}" stroke-width="1">
<line x1="80" y1="351.7" x2="630" y2="351.7"/>
<line x1="80" y1="238.3" x2="630" y2="238.3"/>
<line x1="80" y1="125" x2="630" y2="125"/>
</g>

<g stroke="{AXE}" stroke-width="1.6">
<line x1="80" y1="40" x2="80" y2="380"/>
<line x1="80" y1="380" x2="630" y2="380"/>
</g>

<g stroke="{AXE}" stroke-width="1.4">
<line x1="80" y1="380" x2="80" y2="386"/>
<line x1="224.7" y1="380" x2="224.7" y2="386"/>
<line x1="369.5" y1="380" x2="369.5" y2="386"/>
<line x1="514.2" y1="380" x2="514.2" y2="386"/>
</g>
<g font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">
<text x="80" y="402">100</text>
<text x="224.7" y="402">150</text>
<text x="369.5" y="402">200</text>
<text x="514.2" y="402">250</text>
<text x="355" y="430" font-size="15" fill="{ENCRE}">superficie (m²)</text>
</g>

<g stroke="{AXE}" stroke-width="1.4">
<line x1="74" y1="351.7" x2="80" y2="351.7"/>
<line x1="74" y1="238.3" x2="80" y2="238.3"/>
<line x1="74" y1="125" x2="80" y2="125"/>
</g>
<g font-size="13" fill="{ENCRE_PALE}" text-anchor="end">
<text x="68" y="356">300 k$</text>
<text x="68" y="242.8">500 k$</text>
<text x="68" y="129.5">700 k$</text>
</g>
<text x="18" y="210" font-size="15" fill="{ENCRE}" text-anchor="middle" transform="rotate(-90 18 210)">prix de vente</text>"""


def entete(hauteur, titre, desc, defs=""):
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg viewBox="0 0 660 {hauteur}" xmlns="http://www.w3.org/2000/svg" role="img" '
        'font-family="system-ui, -apple-system, sans-serif">\n'
        f"<title>{titre}</title>\n<desc>{desc}</desc>\n{defs}\n{cadre(hauteur)}\n"
    )


def points(couleur=TEAL, rayon=6.5, seulement=None):
    corps = "\n".join(
        f'<circle cx="{px(m):.1f}" cy="{py(p):.1f}" r="{rayon}"/>'
        for m, p, v in MAISONS
        if seulement is None or v is seulement
    )
    return f'<g fill="{couleur}" stroke="{FOND}" stroke-width="1.5">\n{corps}\n</g>'


def croix(demi=10, epaisseur=1.8):
    """Un ✗ centré sur chaque maison qui a traîné : les ratés du modèle."""
    corps = "\n".join(
        f'<path d="M{px(m) - demi:.1f} {py(p) - demi:.1f} L{px(m) + demi:.1f} {py(p) + demi:.1f} '
        f'M{px(m) - demi:.1f} {py(p) + demi:.1f} L{px(m) + demi:.1f} {py(p) - demi:.1f}"/>'
        for m, p, v in MAISONS
        if not v
    )
    return f'<g stroke="{ROUGE}" stroke-width="{epaisseur}" fill="none" stroke-linecap="round">\n{corps}\n</g>'


MOYENNE = sum(p for _, p, _ in MAISONS) / len(MAISONS)
BASELINE = f"""<line x1="80" y1="{py(MOYENNE):.1f}" x2="630" y2="{py(MOYENNE):.1f}" stroke="{BRUN}" stroke-width="2.6" stroke-dasharray="7 4"/>
<text x="624" y="{py(MOYENNE) - 8:.1f}" font-size="13" fill="{BRUN}" text-anchor="end" font-weight="600">toujours {MOYENNE:.0f} k$</text>"""


# ── 1. Le nuage nu (p. 10) ────────────────────────────────────────────────────
nuage = entete(
    460,
    "Prix des maisons en fonction de la superficie",
    "Nuage de points : chaque maison est un point situé selon sa superficie (axe horizontal) et "
    "son prix de vente (axe vertical). À mesure que la superficie augmente, le prix tend à "
    "augmenter — mais les points ne sont pas parfaitement alignés.",
) + points() + "\n</svg>\n"

# ── 2. Le même nuage, colorié par la seconde question (p. 10) ─────────────────
vendues = entete(
    500,
    "Les mêmes maisons, mais la réponse est maintenant une catégorie",
    "Le même nuage de points : chaque maison est placée selon sa superficie (axe horizontal) et "
    "son prix (axe vertical). Cette fois, ce n'est plus la hauteur du point qu'on cherche à "
    "prédire, mais sa couleur : en bleu les maisons vendues en moins de 30 jours, en rouge celles "
    "qui ont traîné. Les maisons peu chères pour leur superficie (sous la tendance générale) "
    "partent vite ; les plus chères pour ce qu'elles offrent traînent — avec trois exceptions.",
) + points(BLEU, 7, seulement=True) + "\n" + points(ROUGE, 7, seulement=False) + f"""
<circle cx="176" cy="458" r="7" fill="{BLEU}" stroke="{FOND}" stroke-width="1.5"/>
<text x="192" y="462" font-size="14" fill="{ENCRE}" text-anchor="start">vendue en moins de 30 jours</text>
<circle cx="412" cy="458" r="7" fill="{ROUGE}" stroke="{FOND}" stroke-width="1.5"/>
<text x="428" y="462" font-size="14" fill="{ENCRE}" text-anchor="start">a traîné</text>
</svg>
"""

# ── 3. Le prédicteur le plus bête (p. 20) ─────────────────────────────────────
baseline = entete(
    460,
    "Le modèle le plus bête : toujours prédire le prix moyen",
    f"Le même nuage de maisons, traversé par une droite horizontale à {MOYENNE:.0f} 000 $ (le prix "
    "moyen). Cette droite représente un modèle qui prédit toujours la même valeur, sans tenir "
    "compte de la superficie : elle passe au milieu du nuage, au-dessus des maisons bon marché et "
    "en dessous des plus chères.",
) + BASELINE + "\n" + points() + "\n</svg>\n"

# ── 4. Ses erreurs, en dollars (p. 20) ────────────────────────────────────────
segments = "\n".join(
    f'<line x1="{px(m):.1f}" y1="{py(p):.1f}" x2="{px(m):.1f}" y2="{py(MOYENNE):.1f}"/>'
    for m, p, _ in MAISONS
)
erreurs = entete(
    460,
    "L'erreur du modèle moyen : l'écart de chaque maison à la prédiction",
    f"Le nuage de maisons et la droite plate à {MOYENNE:.0f} 000 $. Pour chaque maison, un segment "
    "vertical rouge relie son vrai prix à la prédiction : c'est l'erreur du modèle sur cette "
    "maison. Les segments sont longs aux extrêmes (maisons très bon marché ou très chères) et "
    "courts près du centre.",
    defs=f'<defs>\n<marker id="arrErr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" '
    f'markerHeight="7" orient="auto"><path d="M1 1 L9 5 L1 9" fill="none" stroke="{ROUGE}" '
    'stroke-width="1.7"/></marker>\n</defs>',
) + BASELINE + f"""
<g stroke="{ROUGE}" stroke-width="1.8" opacity="0.85">
{segments}
</g>
""" + points() + f"""
<text x="250" y="62" font-size="15" fill="{ROUGE}" text-anchor="middle" font-weight="700">erreur du modèle</text>
<g stroke="{ROUGE}" stroke-width="1.6" fill="none" stroke-dasharray="5 3">
<line x1="215" y1="74" x2="117.5" y2="292" marker-end="url(#arrErr)"/>
<line x1="300" y1="74" x2="427.3" y2="218" marker-end="url(#arrErr)"/>
</g>
</svg>
"""

# ── 5. Ses erreurs, en oui/non (p. 20) ────────────────────────────────────────
n_vite = sum(1 for _, _, v in MAISONS if v)
oui_non = entete(
    505,
    "Le prédicteur bête pour la question en oui/non : ses erreurs",
    "Exactement le même nuage que précédemment — les mêmes maisons, aux mêmes places, la "
    "superficie en abscisse et le prix en ordonnée. Mais toutes sont maintenant bleues : le "
    "prédicteur bête répond « oui » — vendue en moins de 30 jours — pour chacune, sans jamais les "
    "regarder. Un ✗ rouge barre celles qui avaient en réalité traîné : ce sont ses erreurs, et ce "
    "sont précisément les maisons qui étaient rouges sur la figure de la page précédente.",
) + f"""
<text x="96" y="64" font-size="15" fill="{BLEU}" text-anchor="start" font-weight="700">le modèle a répondu « oui » pour toutes les maisons</text>
""" + points(BLEU, 7) + "\n" + croix() + f"""
<circle cx="147" cy="452" r="7" fill="{BLEU}" stroke="{FOND}" stroke-width="1.5"/>
<text x="163" y="456" font-size="14" fill="{ENCRE}" text-anchor="start">prédiction du modèle : « oui », vendue en moins de 30 jours</text>
<path d="M228 468 L248 488 M228 488 L248 468" stroke="{ROUGE}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
<text x="256" y="482" font-size="14" fill="{ENCRE}" text-anchor="start">cette maison avait en fait traîné</text>
</svg>
"""

for nom, contenu in [
    ("maisons-nuage", nuage),
    ("maisons-vendues", vendues),
    ("maisons-baseline", baseline),
    ("maisons-erreurs", erreurs),
    ("maisons-erreurs-oui-non", oui_non),
]:
    (OUT / f"{nom}.svg").write_text(contenu)

print(f"{len(MAISONS)} maisons — prix moyen {MOYENNE:.1f} k$ — "
      f"{n_vite} vendues vite ({100 * n_vite / len(MAISONS):.0f} %)")
