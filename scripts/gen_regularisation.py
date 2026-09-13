"""Même polynôme, avec ou sans pénalité : la régularisation sur le nuage des maisons.

Deux panneaux, le même nuage superficie × prix (jeu canonique de gen_maisons.py)
et le même polynôme de degré DEGRE ajusté aux moindres carrés : à gauche sans
pénalité (il ondule entre les points), à droite avec une pénalité ridge sur les
coefficients (il se calme). Aucune dépendance : les moindres carrés sont résolus
à la main.

Usage :
    uv run scripts/gen_regularisation.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_maisons import MAISONS, OUT  # noqa: E402

FOND, BORD, AXE, ENCRE, ENCRE_PALE, TEAL, BRUN = (
    "#efe7d3", "#d9cbac", "#b8a888", "#3a3531", "#5b5249", "#2f6f6a", "#9a5b33")
DEGRE = 12
LAMBDA = 5.0

XS = [m[0] for m in MAISONS]
YS = [m[3] for m in MAISONS]
X0, X1 = 100, 292            # superficie (m²) de chaque panneau
Y0, Y1 = 230, 850            # prix (k$)


def norm(x):
    return 2 * (x - X0) / (X1 - X0) - 1   # dans [-1, 1]


def resoudre(A, b):
    """Gauss avec pivot partiel."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n + 1):
                M[r][k] -= f * M[c][k]
    w = [0.0] * n
    for r in range(n - 1, -1, -1):
        w[r] = (M[r][n] - sum(M[r][k] * w[k] for k in range(r + 1, n))) / M[r][r]
    return w


def ajuster(lam):
    d = DEGRE + 1
    X = [[norm(x) ** j for j in range(d)] for x in XS]
    XtX = [[sum(X[i][a] * X[i][b] for i in range(len(XS))) + (lam if a == b and a > 1 else 0)
            for b in range(d)] for a in range(d)]
    Xty = [sum(X[i][a] * YS[i] for i in range(len(XS))) for a in range(d)]
    return resoudre(XtX, Xty)


def evaluer(w, x):
    t = norm(x)
    return sum(c * t ** j for j, c in enumerate(w))


def panneau(ox, w, etiquette):
    """Un panneau de 245 × 230 px dont le coin haut-gauche des axes est (ox, 55)."""
    L, H = 245, 230
    sx = lambda x: ox + (x - X0) / (X1 - X0) * L
    sy = lambda y: 55 + H - (y - Y0) / (Y1 - Y0) * H
    courbe = " ".join(f"{sx(x):.1f},{sy(evaluer(w, x)):.1f}"
                      for x in [X0 + i * (X1 - X0) / 300 for i in range(301)])
    points = "\n".join(f'<circle cx="{sx(x):.1f}" cy="{sy(y):.1f}" r="5.5"/>' for x, y in zip(XS, YS))
    cid = f"clip{ox}"
    return f"""<clipPath id="{cid}"><rect x="{ox}" y="{55 - 8}" width="{L + 4}" height="{H + 8}"/></clipPath>
<g stroke="{AXE}" stroke-width="1.6" fill="none">
<line x1="{ox}" y1="55" x2="{ox}" y2="{55 + H}"/>
<line x1="{ox}" y1="{55 + H}" x2="{ox + L}" y2="{55 + H}"/>
</g>
<polyline points="{courbe}" fill="none" stroke="{BRUN}" stroke-width="2.6" stroke-linejoin="round" clip-path="url(#{cid})"/>
<g fill="{TEAL}" stroke="{FOND}" stroke-width="1.4">
{points}
</g>
<text x="{ox + L / 2:.0f}" y="{55 + H + 40}" font-size="17" fill="{ENCRE}" text-anchor="middle" font-weight="600">{etiquette}</text>"""


w_libre = ajuster(0.0)
w_ridge = ajuster(LAMBDA)
print("coefficients sans pénalité :", [round(c) for c in w_libre])
print("coefficients avec pénalité :", [round(c) for c in w_ridge])

svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg viewBox="0 0 660 400" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">
<title>Même polynôme, sans ou avec pénalité : la régularisation</title>
<desc>Deux panneaux montrant le même nuage de maisons (superficie en abscisse, prix en ordonnée) et le même polynôme de degré {DEGRE} ajusté aux données. À gauche, sans pénalité : la courbe ondule pour passer au plus près de chaque point, avec des bosses et des creux entre eux. À droite, avec une pénalité sur la taille des coefficients : le même polynôme se calme et suit la tendance générale, presque une droite.</desc>
<rect x="0" y="0" width="660" height="400" rx="14" fill="{FOND}" stroke="{BORD}"/>
{panneau(55, w_libre, "sans pénalité")}
{panneau(375, w_ridge, "avec pénalité")}
<text x="330" y="372" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">Le même polynôme de degré {DEGRE}, ajusté aux mêmes maisons ; seule la pénalité change.</text>
</svg>
"""
(OUT / "regularisation.svg").write_text(svg)
print("regularisation.svg écrit")
