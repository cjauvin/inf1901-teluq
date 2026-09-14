"""L'arbre de décision classique du Titanic (profondeur 2), appris sur les vraies données.

Caractéristiques : sexe, âge (médiane pour les âges manquants), classe.
Usage : uv run scripts/gen_arbre_titanic.py
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from arbre import apprendre, predire  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"
CSV = Path(__file__).resolve().parent / "data" / "titanic3.csv"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "

rows = [r for r in csv.DictReader(open(CSV, encoding="utf-8")) if r["survived"] in ("0", "1")]
ages = sorted(float(r["age"]) for r in rows if r["age"])
mediane = ages[len(ages) // 2]
EX = [((1.0 if r["sex"] == "female" else 0.0, float(r["age"]) if r["age"] else mediane, float(r["pclass"])),
       r["survived"] == "1") for r in rows]
T = apprendre(EX, 2, min_feuille=20)
justes = sum(1 for x, y in EX if predire(T, x) == y) / len(EX)


def question(n):
    return {0: f"Une femme{FINE}?", 1: f"Plus de {int(n.seuil)} ans{FINE}?", 2: f"En troisième classe{FINE}?"}[n.j]


def nb_feuilles(n):
    return 1 if n.feuille else nb_feuilles(n.gauche) + nb_feuilles(n.droite)


def glose(n, chemin):
    """Qui est dans cette feuille, en clair."""
    sexe = "femmes" if chemin.get(0) == "oui" else "hommes"
    if chemin.get(1) == "non":
        sexe = "garçons" if sexe == "hommes" else "filles"
    if chemin.get(1) == "oui" and sexe == "hommes":
        sexe = "hommes adultes"
    if chemin.get(2) == "oui":
        sexe += " de 3ᵉ classe"
    elif chemin.get(2) == "non":
        sexe += " de 1ʳᵉ ou 2ᵉ classe"
    return sexe


def dessiner(n, x0, y, o, chemin, lf=150, pas_y=88):
    w_sub = nb_feuilles(n) * lf
    x = x0 + w_sub / 2
    if n.feuille:
        ys = [v for _, v in n.exemples]
        k, tot = sum(ys), len(ys)
        taux = 100 * k / tot
        couleur = BLEU if 2 * k >= tot else ROUGE
        o.append(f'<circle cx="{x:.1f}" cy="{y + 14}" r="12" fill="{couleur}" stroke="{FOND}" stroke-width="1.5"/>')
        g = glose(n, chemin)
        l1, l2 = (g.split(" de ", 1) + [""])[:2]
        o.append(f'<text x="{x:.1f}" y="{y + 44}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="600">{tot} {l1}</text>')
        if l2:
            o.append(f'<text x="{x:.1f}" y="{y + 60}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="600">de {l2}</text>')
        o.append(f'<text x="{x:.1f}" y="{y + 76 if l2 else y + 60}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">{taux:.0f}{NB}% ont survécu</text>')
        return
    q = question(n)
    w = 7.4 * len(q) + 24
    o.append(f'<rect x="{x - w / 2:.1f}" y="{y}" width="{w:.1f}" height="30" rx="7" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{x:.1f}" y="{y + 20}" font-size="13" fill="{ENCRE}" text-anchor="middle" font-weight="600">{q}</text>')
    wg = nb_feuilles(n.gauche) * lf
    for enfant, xe0, rep in ((n.gauche, x0, "non"), (n.droite, x0 + wg, "oui")):
        xe = xe0 + nb_feuilles(enfant) * lf / 2
        o.append(f'<line x1="{x:.1f}" y1="{y + 30}" x2="{xe:.1f}" y2="{y + pas_y}" stroke="{AXE}" stroke-width="1.4"/>')
        mx, my = (x + xe) / 2, (y + 30 + y + pas_y) / 2
        dx = -10 if rep == "non" else 10
        o.append(f'<text x="{mx + dx:.1f}" y="{my + 4:.1f}" font-size="12" fill="{GRIS}" text-anchor="{"end" if rep == "non" else "start"}" font-style="italic">{rep}</text>')
        dessiner(enfant, xe0, y + pas_y, o, {**chemin, n.j: rep}, lf, pas_y)


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 345" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>L'arbre de décision du Titanic</title>",
     f"<desc>Un arbre à deux niveaux appris sur les 1309 passagers du Titanic. Première question{NB}: une femme{FINE}? Pour les hommes, la question suivante est « plus de 9 ans{FINE}? »{NB}: les garçons (43) ont survécu à 58{NB}%, les hommes adultes (800) à 17{NB}%. Pour les femmes, « en troisième classe{FINE}? »{NB}: celles de première ou deuxième classe (250) ont survécu à 93{NB}%, celles de troisième (216) à 49{NB}%. Trois questions, {100 * justes:.0f}{NB}% de bonnes réponses.</desc>",
     f'<rect x="0" y="0" width="660" height="345" rx="14" fill="{FOND}" stroke="{BORD}"/>']
dessiner(T, 330 - nb_feuilles(T) * 150 / 2, 36, o, {})
o.append(f'<circle cx="200" cy="316" r="7" fill="{BLEU}"/><text x="212" y="320" font-size="12.5" fill="{ENCRE}">La majorité a survécu</text>')
o.append(f'<circle cx="380" cy="316" r="7" fill="{ROUGE}"/><text x="392" y="320" font-size="12.5" fill="{ENCRE}">La majorité a péri</text>')
o.append('</svg>')
(OUT / "arbre-titanic.svg").write_text("\n".join(o) + "\n")
print(f"arbre-titanic.svg écrit ; {100 * justes:.1f} % de bonnes réponses sur {len(EX)} passagers")
