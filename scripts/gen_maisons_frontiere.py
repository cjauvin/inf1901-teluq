"""La frontière de décision de kNN dans le plan distance × année des 20 maisons.

Importe le jeu de données canonique de gen_maisons.py. Pour chaque petite case
du plan, on cherche les k maisons les plus proches (distance mesurée dans le
plan tel qu'il est dessiné) et on teinte la case de la couleur majoritaire :
la ligne où la teinte bascule est la frontière de décision.

Usage :
    uv run scripts/gen_maisons_frontiere.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_maisons import (BLEU, ENCRE, ENCRE_PALE, FOND, MAISONS, OUT, coord, entete,
                         points)

CASE = 5
X0, X1, Y0, Y1 = 80, 630, 40, 380


def majorite(x, y, k):
    d = sorted((((x - cx) ** 2 + (y - cy) ** 2), m[4])
               for m in MAISONS for cx, cy in [coord(m, "categorie")])
    return sum(1 for _, v in d[:k] if v) * 2 > k


def fond(k):
    cases = []
    for x in range(X0, X1, CASE):
        for y in range(Y0, Y1, CASE):
            bleu = majorite(x + CASE / 2, y + CASE / 2, k)
            cases.append(f'<rect x="{x}" y="{y}" width="{CASE}" height="{CASE}" '
                         f'fill="{BLEU if bleu else ROUGE}"/>')
    return '<g opacity="0.16" stroke="none">\n' + "\n".join(cases) + "\n</g>"


from gen_maisons import ROUGE  # noqa: E402


def figure(k, nom, titre, desc):
    return entete(500, titre, desc, plan="categorie") + fond(k) + "\n" + \
        points(BLEU, 7, "categorie", seulement=True) + "\n" + \
        points(ROUGE, 7, "categorie", seulement=False) + f"""
<circle cx="150" cy="458" r="7" fill="{BLEU}" stroke="{FOND}" stroke-width="1.5"/>
<text x="166" y="462" font-size="14" fill="{ENCRE}" text-anchor="start">vendue en moins de 30 jours</text>
<circle cx="386" cy="458" r="7" fill="{ROUGE}" stroke="{FOND}" stroke-width="1.5"/>
<text x="402" y="462" font-size="14" fill="{ENCRE}" text-anchor="start">a traîné</text>
<text x="355" y="490" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">fond : la réponse de kNN (k = {k}) pour une maison qui se trouverait là</text>
</svg>
"""


FIGURES = {
    "maisons-frontiere-k3": figure(
        3, "maisons-frontiere-k3",
        "La frontière de décision de kNN (k = 3) sur les maisons",
        "Le nuage coloré des maisons, dans le plan distance du centre × année de construction, "
        "avec le fond teinté : bleu pâle là où kNN (k = 3) répondrait « vendue vite » à une "
        "maison qui s'y trouverait, rouge pâle là où il répondrait « a traîné ». La ligne où la "
        "teinte bascule, qui serpente dans la bande vide entre les deux amas, est la frontière "
        "de décision. Les deux exceptions sont absorbées par leur territoire adverse."),
    "maisons-frontiere-k1": figure(
        1, "maisons-frontiere-k1",
        "La frontière de décision de kNN (k = 1) sur les maisons",
        "Même plan, même fond teinté, mais avec k = 1 : chaque maison impose sa couleur à tout "
        "ce qui l'entoure. Les deux exceptions creusent chacune un îlot de leur couleur en plein "
        "territoire adverse, et la frontière se découpe en cellules anguleuses."),
}

if __name__ == "__main__":
    for nom, contenu in FIGURES.items():
        (OUT / f"{nom}.svg").write_text(contenu)
    print(f"{len(FIGURES)} figures écrites dans {OUT}")
