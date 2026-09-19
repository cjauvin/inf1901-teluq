"""Une machine de Turing complète : l'incrément binaire (n ↦ n + 1).

La figure montre les trois pièces d'une machine (ses états, sa table de règles,
son ruban) et une exécution complète, simulée ici même : 1011 (onze) devient
1100 (douze).
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module1"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, AXE, PANNEAU, AMBRE = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#b8a888", "#fbf7ee", "#b8862b")
NB, FINE = " ", " "
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"
VIDE = "␣"

# (état, symbole lu) → (symbole écrit, déplacement, nouvel état)
REGLES = {
    ("droite", "0"): ("0", "D", "droite"),
    ("droite", "1"): ("1", "D", "droite"),
    ("droite", VIDE): (VIDE, "G", "retenue"),
    ("retenue", "1"): ("0", "G", "retenue"),
    ("retenue", "0"): ("1", "G", "arrêt"),
    ("retenue", VIDE): ("1", "G", "arrêt"),
}


def executer(mot):
    ruban = {i: c for i, c in enumerate(mot)}
    pos, etat, trace = 0, "droite", []
    while True:
        trace.append((dict(ruban), pos, etat))
        if etat == "arrêt":
            return trace
        ecrit, dep, etat = REGLES[(etat, ruban.get(pos, VIDE))]
        ruban[pos] = ecrit
        pos += 1 if dep == "D" else -1


TRACE = executer("1011")
resultat = "".join(TRACE[-1][0].get(i, VIDE) for i in range(-1, 5)).strip(VIDE)
assert resultat == "1100", resultat

W, H = 660, 640
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Une machine de Turing complète : ajouter 1 à un nombre binaire</title>",
     f"<desc>Une machine de Turing à trois états qui calcule la fonction n ↦ n + 1 sur un nombre écrit en binaire. En haut à gauche, le diagramme de ses états{NB}: « droite » (aller au bout du nombre), « retenue » (propager la retenue vers la gauche) et « arrêt ». En haut à droite, sa table de six règles. En bas, l'exécution complète sur le ruban{NB}: en neuf instantanés, la tête parcourt 1011 (onze) vers la droite, atteint la case vide, revient en transformant les 1 en 0, puis change le premier 0 rencontré en 1 et s'arrête{NB}: le ruban porte 1100 (douze).</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<defs><marker id="fm" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{ENCRE_PALE}"/></marker></defs>',
     f'<text x="330" y="36" font-size="16" fill="{ENCRE}" text-anchor="middle" font-weight="600">Une machine complète{NB}: la fonction n ↦ n + 1, en binaire</text>']

# ── diagramme d'états ────────────────────────────────────────────────────────
o.append(f'<text x="160" y="70" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">Ses trois états</text>')
etats = {"droite": (70, 150), "retenue": (170, 150), "arrêt": (270, 150)}
for nom, (x, y) in etats.items():
    final = nom == "arrêt"
    o.append(f'<circle cx="{x}" cy="{y}" r="30" fill="{PANNEAU}" stroke="{TEAL if not final else BRUN}" stroke-width="2"/>')
    if final:
        o.append(f'<circle cx="{x}" cy="{y}" r="25" fill="none" stroke="{BRUN}" stroke-width="1.2"/>')
    o.append(f'<text x="{x}" y="{y + 4}" font-size="12" fill="{ENCRE}" text-anchor="middle" font-weight="600">{nom}</text>')
o.append(f'<line x1="22" y1="150" x2="38" y2="150" stroke="{ENCRE_PALE}" stroke-width="1.4" marker-end="url(#fm)"/>')
o.append(f'<line x1="101" y1="150" x2="138" y2="150" stroke="{ENCRE_PALE}" stroke-width="1.4" marker-end="url(#fm)"/>')
o.append(f'<line x1="201" y1="150" x2="238" y2="150" stroke="{ENCRE_PALE}" stroke-width="1.4" marker-end="url(#fm)"/>')
o.append(f'<text x="120" y="141" font-size="10.5" fill="{GRIS}" text-anchor="middle">{VIDE}</text>')
o.append(f'<text x="220" y="141" font-size="10.5" fill="{GRIS}" text-anchor="middle">0 ou {VIDE}</text>')
for x, lab in ((70, "0, 1"), (170, "1")):
    o.append(f'<path d="M{x - 14} {150 - 27} C {x - 30} {150 - 70}, {x + 30} {150 - 70}, {x + 14} {150 - 27}" fill="none" stroke="{ENCRE_PALE}" stroke-width="1.4" marker-end="url(#fm)"/>')
    o.append(f'<text x="{x}" y="{150 - 66}" font-size="10.5" fill="{GRIS}" text-anchor="middle">{lab}</text>')
o.append(f'<text x="70" y="202" font-size="10.5" fill="{GRIS}" text-anchor="middle">aller au bout</text>')
o.append(f'<text x="70" y="215" font-size="10.5" fill="{GRIS}" text-anchor="middle">du nombre</text>')
o.append(f'<text x="170" y="202" font-size="10.5" fill="{GRIS}" text-anchor="middle">propager</text>')
o.append(f'<text x="170" y="215" font-size="10.5" fill="{GRIS}" text-anchor="middle">la retenue</text>')
o.append(f'<text x="270" y="202" font-size="10.5" fill="{GRIS}" text-anchor="middle">c\'est fini</text>')

# ── table de règles ──────────────────────────────────────────────────────────
TX, TY = 330, 86
cols = [("État", 0), ("Lit", 72), ("Écrit", 112), ("Va à", 162), ("Passe à", 246)]
o.append(f'<text x="{TX + 148}" y="70" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">Sa table de règles</text>')
o.append(f'<rect x="{TX - 10}" y="{TY - 4}" width="316" height="{20 + 6 * 19 + 8}" rx="8" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.1"/>')
for lab, dx in cols:
    o.append(f'<text x="{TX + dx}" y="{TY + 12}" font-size="11" fill="{ENCRE_PALE}" font-weight="600">{lab}</text>')
o.append(f'<line x1="{TX - 4}" y1="{TY + 18}" x2="{TX + 300}" y2="{TY + 18}" stroke="{AXE}" stroke-width="1"/>')
for i, ((etat, lu), (ecrit, dep, nouv)) in enumerate(REGLES.items()):
    y = TY + 34 + i * 19
    vals = [etat, lu, ecrit, "droite →" if dep == "D" else "← gauche", nouv]
    for (lab, dx), v in zip(cols, vals):
        mono = lab in ("Lit", "Écrit")
        o.append(f'<text x="{TX + dx}" y="{y}" font-size="11.5" fill="{ENCRE}"' + (f' font-family="{MONO}"' if mono else "") + f'>{v}</text>')

# ── exécution sur le ruban ───────────────────────────────────────────────────
RY = 262
o.append(f'<text x="330" y="{RY - 14}" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle" font-style="italic">Son exécution sur le ruban{NB}: 1011 (onze) devient 1100 (douze)</text>')
C, X0 = 30, 225            # taille d'une case, abscisse de la case -1
for k, (ruban, pos, etat) in enumerate(TRACE):
    y = RY + k * 38
    o.append(f'<text x="60" y="{y + 20}" font-size="11.5" fill="{GRIS}" text-anchor="start">étape {k}</text>')
    o.append(f'<text x="{X0 - 16}" y="{y + 20}" font-size="12" fill="{TEAL if etat != "arrêt" else BRUN}" text-anchor="end" font-weight="600">{etat}</text>')
    for j, i in enumerate(range(-1, 6)):
        x = X0 + j * C
        tete = i == pos
        o.append(f'<rect x="{x}" y="{y}" width="{C}" height="{C}" fill="{"#f4e3b5" if tete else PANNEAU}" stroke="{AMBRE if tete else AXE}" stroke-width="{2 if tete else 1}"/>')
        s = ruban.get(i, VIDE)
        o.append(f'<text x="{x + C / 2}" y="{y + 20}" font-size="14" fill="{ENCRE if s != VIDE else "#b8a888"}" text-anchor="middle" font-family="{MONO}">{s}</text>')
    if k < len(TRACE) - 1:
        lu = ruban.get(pos, VIDE)
        ecrit, dep, nouv = REGLES[(etat, lu)]
        o.append(f'<text x="{X0 + 7 * C + 16}" y="{y + 20}" font-size="11" fill="{GRIS}">lit {lu}, écrit {ecrit}, va à {"droite" if dep == "D" else "gauche"}</text>')
    else:
        o.append(f'<text x="{X0 + 7 * C + 16}" y="{y + 20}" font-size="11.5" fill="{BRUN}" font-weight="600">résultat{NB}: 1100</text>')
o.append(f'<rect x="{X0 + 8}" y="{RY + len(TRACE) * 38 + 2}" width="14" height="14" fill="#f4e3b5" stroke="{AMBRE}" stroke-width="2"/>')
o.append(f'<text x="{X0 + 30}" y="{RY + len(TRACE) * 38 + 14}" font-size="11.5" fill="{ENCRE_PALE}">la case sous la tête de lecture</text>')
o.append('</svg>')
(OUT / "machine-turing-increment.svg").write_text("\n".join(o) + "\n")
print(f"machine-turing-increment.svg écrit ; {len(TRACE)} instantanés ; résultat {resultat}")
