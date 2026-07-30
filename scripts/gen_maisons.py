#!/usr/bin/env python3
"""Génère les figures du fil rouge « maisons » du Module 2.

Source de vérité unique : la liste MAISONS ci-dessous. Toutes les figures des
pages 10, 20 et 50 en découlent — et gen_troisieme_dim.py l'importe pour la
p. 30 —, ce qui garantit ce que le texte affirme :

  * la p. 10 peut dire « les mêmes maisons » d'une figure à l'autre ;
  * le prix moyen vaut exactement 500 k$, comme l'annonce la p. 20 ;
  * 12 maisons sur 20 se vendent vite, soit exactement les 60 % de l'étalon.

Deux plans, deux histoires — c'est le point de conception central :

  * dans le plan **superficie × prix**, les points forment une droite bruitée :
    c'est le terrain de la régression (p. 10, 20, 50) ;
  * la catégorie « vendue en moins de 30 jours » n'y est pas lisible. Elle se
    lit dans le plan **superficie × année** : les maisons récentes partent vite,
    les anciennes traînent (p. 10, 20).

Autrement dit, la seconde question ne se lit pas dans les mêmes axes que la
première. C'est voulu : cela laisse au nuage de prix sa forme de droite, et
sème l'idée qu'il faut regarder les bons renseignements.

Usage :
    uv run scripts/gen_maisons.py

Prévisualisation (rsvg-convert n'est plus installé) :
    qlmanage -t -s 900 -o /tmp static/images/module2/maisons-nuage.svg
"""

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"

# ── Le jeu de données canonique ───────────────────────────────────────────────
# (superficie m², année de construction, prix k$, vendue en moins de 30 jours)
#
# Contrainte : les quatre maisons des tables de la p. 10 doivent s'y trouver
# avec leurs valeurs exactes — la p. 30 reprend deux d'entre elles comme
# vecteurs dans nf_house.png. Elles sont marquées « table » ci-dessous, et ce
# sont elles qui ont dicté le reste : leurs quatre années séparent déjà
# parfaitement les oui des non.
#
# Le prix suit la tendance ~3 k$ par m², avec un bruit de quelques dizaines de
# milliers : dans ce plan-là, le nuage doit se lire comme une droite.
#
# Deux exigences gouvernent les années, et elles comptent autant l'une que
# l'autre :
#
#   1. un **vide franc** entre 1984 et 1994. Sans lui, les deux couleurs
#      forment des bandes accolées, pas deux amas ; le vide joue pour la
#      classification le rôle que la droite joue pour la régression ;
#   2. les deux classes se **répartissent pareillement sur la superficie**.
#      Sinon la catégorie transparaîtrait dans le plan superficie × prix, et la
#      p. 10 ne pourrait plus dire qu'on ne l'y voit pas.
#
# Deux rebelles traversent le vide, une dans chaque sens.
MAISONS = [
    (112, 1997, 271, True),
    (120, 2013, 272, True),
    (130, 1972, 310, False),   # table
    (142, 2004, 361, True),
    (150, 1980, 350, False),   # table
    (158, 1971, 364, True),    # exception : ancienne, et pourtant partie vite
    (168, 1976, 437, False),
    (176, 2016, 445, True),
    (180, 1995, 420, True),    # table
    (190, 1968, 457, False),
    (198, 2008, 519, True),
    (208, 2011, 561, False),   # exception : récente, et pourtant a traîné
    (216, 2001, 545, True),
    (220, 2010, 580, True),    # table
    (232, 1983, 607, False),
    (242, 2019, 637, True),
    (252, 1970, 674, False),
    (262, 1999, 701, True),
    (272, 2006, 729, True),
    (280, 1974, 760, False),
]

# Le nombre de chambres de la table suit la superficie ; il ne sert à aucune
# figure, mais gen_troisieme_dim.py et les tables du texte doivent s'accorder.
def chambres(m2):
    return round(m2 / 45)


# ── Palette parchemin ─────────────────────────────────────────────────────────
FOND, BORD, GRILLE, AXE = "#efe7d3", "#d9cbac", "#e0d4b8", "#b8a888"
ENCRE, ENCRE_PALE = "#3a3531", "#5b5249"
TEAL, BRUN, ROUGE, BLEU = "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5"

# ── Repères ───────────────────────────────────────────────────────────────────
# Abscisse commune : superficie, 100 m² → x=80 puis 2,894 px par m².
# Ordonnée « prix »  : 300 k$ → y=351,7 ; 500 k$ → 238,3 ; 700 k$ → 125.
# Ordonnée « année » : 1970  → y=351,7 ; 1990  → 238,3 ; 2010  → 125.
def px(m2):
    return 80 + (m2 - 100) * 2.894


def py(prix_k):
    return 351.7 - (prix_k - 300) * 0.567


def pa(annee):
    return 351.7 - (annee - 1970) * 5.67


def cadre(hauteur, ordonnee="prix"):
    """Le fond, la grille, les axes et leurs étiquettes."""
    if ordonnee == "prix":
        crans = [("300 k$", 351.7), ("500 k$", 238.3), ("700 k$", 125)]
        titre_y = "prix de vente"
    else:
        crans = [("1970", 351.7), ("1990", 238.3), ("2010", 125)]
        titre_y = "année de construction"

    grille = "\n".join(f'<line x1="80" y1="{y}" x2="630" y2="{y}"/>' for _, y in crans)
    crans_y = "\n".join(f'<line x1="74" y1="{y}" x2="80" y2="{y}"/>' for _, y in crans)
    etiq_y = "\n".join(
        f'<text x="68" y="{y + 4.5}">{lab}</text>' for lab, y in crans
    )

    return f"""<rect x="0" y="0" width="660" height="{hauteur}" rx="14" fill="{FOND}" stroke="{BORD}"/>

<g stroke="{GRILLE}" stroke-width="1">
{grille}
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
{crans_y}
</g>
<g font-size="13" fill="{ENCRE_PALE}" text-anchor="end">
{etiq_y}
</g>
<text x="18" y="210" font-size="15" fill="{ENCRE}" text-anchor="middle" transform="rotate(-90 18 210)">{titre_y}</text>"""


def entete(hauteur, titre, desc, ordonnee="prix", defs=""):
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg viewBox="0 0 660 {hauteur}" xmlns="http://www.w3.org/2000/svg" role="img" '
        'font-family="system-ui, -apple-system, sans-serif">\n'
        f"<title>{titre}</title>\n<desc>{desc}</desc>\n{defs}\n{cadre(hauteur, ordonnee)}\n"
    )


def points(couleur=TEAL, rayon=6.5, ordonnee="prix", seulement=None):
    def y(m):
        return py(m[2]) if ordonnee == "prix" else pa(m[1])

    corps = "\n".join(
        f'<circle cx="{px(m[0]):.1f}" cy="{y(m):.1f}" r="{rayon}"/>'
        for m in MAISONS
        if seulement is None or m[3] is seulement
    )
    return f'<g fill="{couleur}" stroke="{FOND}" stroke-width="1.5">\n{corps}\n</g>'


# ── La droite de régression, ajustée aux moindres carrés ──────────────────────
n = len(MAISONS)
MOYENNE = sum(m[2] for m in MAISONS) / n
m_moy = sum(m[0] for m in MAISONS) / n
pente = sum((m[0] - m_moy) * (m[2] - MOYENNE) for m in MAISONS) / sum(
    (m[0] - m_moy) ** 2 for m in MAISONS
)
ordonnee_origine = MOYENNE - pente * m_moy


def ajuste(m2):
    return pente * m2 + ordonnee_origine


BASELINE = f"""<line x1="80" y1="{py(MOYENNE):.1f}" x2="630" y2="{py(MOYENNE):.1f}" stroke="{BRUN}" stroke-width="2.6" stroke-dasharray="7 4"/>
<text x="624" y="{py(MOYENNE) - 8:.1f}" font-size="13" fill="{BRUN}" text-anchor="end" font-weight="600">toujours {MOYENNE:.0f} k$</text>"""

DROITE = (
    f'<line x1="{px(105):.1f}" y1="{py(ajuste(105)):.1f}" '
    f'x2="{px(287):.1f}" y2="{py(ajuste(287)):.1f}" stroke="{BRUN}" stroke-width="2.6"/>'
)


def segments(vers_droite):
    cible = (lambda m: py(ajuste(m[0]))) if vers_droite else (lambda m: py(MOYENNE))
    corps = "\n".join(
        f'<line x1="{px(m[0]):.1f}" y1="{py(m[2]):.1f}" x2="{px(m[0]):.1f}" y2="{cible(m):.1f}"/>'
        for m in MAISONS
    )
    opacite = "0.9" if vers_droite else "0.85"
    return f'<g stroke="{ROUGE}" stroke-width="1.8" opacity="{opacite}">\n{corps}\n</g>'


def croix(demi=10, epaisseur=1.8):
    """Un ✗ centré sur chaque maison qui a traîné : les ratés du modèle."""
    corps = "\n".join(
        f'<path d="M{px(m[0]) - demi:.1f} {pa(m[1]) - demi:.1f} L{px(m[0]) + demi:.1f} {pa(m[1]) + demi:.1f} '
        f'M{px(m[0]) - demi:.1f} {pa(m[1]) + demi:.1f} L{px(m[0]) + demi:.1f} {pa(m[1]) - demi:.1f}"/>'
        for m in MAISONS
        if not m[3]
    )
    return f'<g stroke="{ROUGE}" stroke-width="{epaisseur}" fill="none" stroke-linecap="round">\n{corps}\n</g>'


FIGURES = {}

# ── p. 10 — le nuage nu ───────────────────────────────────────────────────────
FIGURES["maisons-nuage"] = entete(
    460,
    "Prix des maisons en fonction de la superficie",
    "Nuage de points : chaque maison est un point situé selon sa superficie (axe horizontal) et "
    "son prix de vente (axe vertical). Les points dessinent une montée franche — le prix croît "
    "avec la superficie — sans pour autant s'aligner parfaitement.",
) + points() + "\n</svg>\n"

# ── p. 10 — la seconde question, dans le plan où elle se lit ──────────────────
FIGURES["maisons-vendues"] = entete(
    500,
    "Les mêmes maisons, mais la réponse est maintenant une catégorie",
    "Les mêmes maisons, dans un autre plan : la superficie reste en abscisse, mais l'ordonnée "
    "porte cette fois l'année de construction. Chaque point est colorié selon la réponse à la "
    "seconde question : en bleu les maisons vendues en moins de 30 jours, en rouge celles qui ont "
    "traîné. Les deux couleurs forment deux amas nettement détachés, séparés par une bande vide : "
    "les maisons récentes en haut, en bleu ; les anciennes en bas, en rouge — avec deux "
    "exceptions, une de chaque côté.",
    ordonnee="annee",
) + points(BLEU, 7, "annee", seulement=True) + "\n" + points(ROUGE, 7, "annee", seulement=False) + f"""
<circle cx="176" cy="458" r="7" fill="{BLEU}" stroke="{FOND}" stroke-width="1.5"/>
<text x="192" y="462" font-size="14" fill="{ENCRE}" text-anchor="start">vendue en moins de 30 jours</text>
<circle cx="412" cy="458" r="7" fill="{ROUGE}" stroke="{FOND}" stroke-width="1.5"/>
<text x="428" y="462" font-size="14" fill="{ENCRE}" text-anchor="start">a traîné</text>
</svg>
"""

# ── p. 20 — le prédicteur le plus bête ────────────────────────────────────────
FIGURES["maisons-baseline"] = entete(
    460,
    "Le modèle le plus bête : toujours prédire le prix moyen",
    f"Le même nuage de maisons, traversé par une droite horizontale à {MOYENNE:.0f} 000 $ (le prix "
    "moyen). Cette droite représente un modèle qui prédit toujours la même valeur, sans tenir "
    "compte de la superficie : elle passe au milieu du nuage, au-dessus des maisons bon marché et "
    "en dessous des plus chères.",
) + BASELINE + "\n" + points() + "\n</svg>\n"

MARQUEUR = (
    f'<defs>\n<marker id="arrErr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" '
    f'markerHeight="7" orient="auto"><path d="M1 1 L9 5 L1 9" fill="none" stroke="{ROUGE}" '
    'stroke-width="1.7"/></marker>\n</defs>'
)

# ── p. 20 — ses erreurs, en dollars ───────────────────────────────────────────
FIGURES["maisons-erreurs"] = entete(
    460,
    "L'erreur du modèle moyen : l'écart de chaque maison à la prédiction",
    f"Le nuage de maisons et la droite plate à {MOYENNE:.0f} 000 $. Pour chaque maison, un segment "
    "vertical rouge relie son vrai prix à la prédiction : c'est l'erreur du modèle sur cette "
    "maison. Les segments sont longs aux extrêmes (maisons très bon marché ou très chères) et "
    "courts près du centre.",
    defs=MARQUEUR,
) + BASELINE + "\n" + segments(False) + "\n" + points() + f"""
<text x="250" y="62" font-size="15" fill="{ROUGE}" text-anchor="middle" font-weight="700">erreur du modèle</text>
<g stroke="{ROUGE}" stroke-width="1.6" fill="none" stroke-dasharray="5 3">
<line x1="215" y1="74" x2="117.5" y2="300" marker-end="url(#arrErr)"/>
<line x1="300" y1="74" x2="427.3" y2="218" marker-end="url(#arrErr)"/>
</g>
</svg>
"""

# ── p. 20 — ses erreurs, en oui/non ───────────────────────────────────────────
FIGURES["maisons-erreurs-oui-non"] = entete(
    505,
    "Le prédicteur bête pour la question en oui/non : ses erreurs",
    "Exactement le nuage de la page précédente — les mêmes maisons, aux mêmes places, la "
    "superficie en abscisse et l'année de construction en ordonnée. Mais toutes sont maintenant "
    "bleues : le prédicteur bête répond « oui » — vendue en moins de 30 jours — pour chacune, sans "
    "jamais les regarder. Un ✗ rouge barre celles qui avaient en réalité traîné : ce sont ses "
    "erreurs, et ce sont précisément les maisons qui étaient rouges sur la figure d'origine.",
    ordonnee="annee",
) + f"""
<text x="96" y="64" font-size="15" fill="{BLEU}" text-anchor="start" font-weight="700">le modèle a répondu « oui » pour toutes les maisons</text>
""" + points(BLEU, 7, "annee") + "\n" + croix() + f"""
<circle cx="147" cy="452" r="7" fill="{BLEU}" stroke="{FOND}" stroke-width="1.5"/>
<text x="163" y="456" font-size="14" fill="{ENCRE}" text-anchor="start">prédiction du modèle : « oui », vendue en moins de 30 jours</text>
<path d="M228 468 L248 488 M228 488 L248 468" stroke="{ROUGE}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
<text x="256" y="482" font-size="14" fill="{ENCRE}" text-anchor="start">cette maison avait en fait traîné</text>
</svg>
"""

# ── p. 50 — la droite ajustée, et ses erreurs ─────────────────────────────────
FIGURES["maisons-droite"] = entete(
    460,
    "La régression linéaire : une droite qui épouse la tendance",
    "Le nuage de maisons (superficie en horizontale, prix en verticale) traversé par une droite "
    "inclinée qui en épouse la tendance : c'est le modèle de régression linéaire. La droite monte "
    "vers la droite, suivant la montée du prix avec la superficie.",
) + DROITE + "\n" + points() + "\n</svg>\n"

FIGURES["maisons-erreurs-droite"] = entete(
    460,
    "L'erreur de la droite ajustée : de bien plus courts écarts",
    "Le nuage de maisons traversé par la droite de régression inclinée. Pour chaque maison, un "
    "court segment vertical rouge relie son vrai prix à la prédiction de la droite : l'erreur. Ces "
    "segments sont bien plus courts qu'avec la droite plate de la page précédente, car la droite "
    "inclinée épouse la tendance.",
) + DROITE + "\n" + segments(True) + "\n" + points() + "\n</svg>\n"


if __name__ == "__main__":
    for nom, contenu in FIGURES.items():
        (OUT / f"{nom}.svg").write_text(contenu)

    n_vite = sum(1 for m in MAISONS if m[3])
    ecart_plat = max(abs(m[2] - MOYENNE) for m in MAISONS)
    ecart_droite = max(abs(m[2] - ajuste(m[0])) for m in MAISONS)
    print(f"{n} maisons — prix moyen {MOYENNE:.1f} k$ — {n_vite} vendues vite "
          f"({100 * n_vite / n:.0f} %)")
    print(f"droite ajustée : prix ≈ {pente:.2f} × m² {ordonnee_origine:+.0f}")
    print(f"écart max — droite plate {ecart_plat:.0f} k$, droite ajustée {ecart_droite:.0f} k$")
    print(f"{len(FIGURES)} figures écrites dans {OUT}")
