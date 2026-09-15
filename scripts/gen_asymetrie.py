"""Les deux erreurs ne coûtent pas la même chose : le seuil d'alerte se règle sur la plus grave."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, BLEU, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#3a6ea5", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "


def panneau(ox, titre, fp, fn, grave_est_fn, pos, o):
    """fp / fn : (résumé, coût). grave_est_fn : la case grave. pos : position du seuil, 0 (indulgent) à 1 (strict)."""
    W = 296
    o.append(f'<rect x="{ox}" y="58" width="{W}" height="250" rx="10" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1.2"/>')
    o.append(f'<text x="{ox + W / 2:.0f}" y="84" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="700">{titre}</text>')
    # les deux erreurs
    for i, (nom, (resume, cout), grave) in enumerate((("Faux positif", fp, not grave_est_fn), ("Faux négatif", fn, grave_est_fn))):
        y = 104 + i * 66
        col = ROUGE if grave else TEAL
        o.append(f'<rect x="{ox + 14}" y="{y}" width="{W - 28}" height="54" rx="7" fill="{col}" fill-opacity="{0.16 if grave else 0.08}" stroke="{col}" stroke-width="{2 if grave else 1}"/>')
        o.append(f'<text x="{ox + 26}" y="{y + 20}" font-size="12.5" fill="{ENCRE}" font-weight="600">{nom}{NB}: {resume}</text>')
        o.append(f'<text x="{ox + 26}" y="{y + 40}" font-size="12" fill="{col}" font-weight="{700 if grave else 400}">{cout}</text>')
    # le seuil
    y = 274
    x0, x1 = ox + 40, ox + W - 40
    o.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{AXE}" stroke-width="3" stroke-linecap="round"/>')
    o.append(f'<text x="{x0}" y="{y + 26}" font-size="11.5" fill="{GRIS}" text-anchor="start">indulgent</text>')
    o.append(f'<text x="{x1}" y="{y + 26}" font-size="11.5" fill="{GRIS}" text-anchor="end">strict</text>')
    o.append(f'<text x="{(x0 + x1) / 2:.0f}" y="{y - 22}" font-size="12" fill="{ENCRE_PALE}" text-anchor="middle">seuil d\'alerte</text>')
    xs = x0 + pos * (x1 - x0)
    o.append(f'<polygon points="{xs - 8},{y - 16} {xs + 8},{y - 16} {xs},{y - 4}" fill="{BRUN}"/>')
    o.append(f'<circle cx="{xs:.1f}" cy="{y}" r="7" fill="{BRUN}" stroke="{FOND}" stroke-width="2"/>')


o = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<svg viewBox="0 0 660 360" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Les deux erreurs ne coûtent pas la même chose</title>",
     f"<desc>Deux panneaux. À gauche, le détecteur de fumée{NB}: le faux positif (une alarme pour un toast brûlé) coûte un agacement, le faux négatif (un incendie sans alarme) coûte la maison{FINE}; le curseur du seuil d'alerte est placé du côté indulgent, pour ne rater aucun incendie. À droite, le filtre anti-pourriel{NB}: le faux positif (un vrai courriel jeté) coûte un message perdu, le faux négatif (un pourriel dans la boîte) coûte une seconde d'agacement{FINE}; le curseur est placé du côté strict, pour ne jeter que ce dont on est sûr.</desc>",
     f'<rect x="0" y="0" width="660" height="360" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="330" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le seuil se règle sur l\'erreur la plus grave</text>']
panneau(24, "Détecteur de fumée",
        ("alarme pour un toast brûlé", f"coût{NB}: un agacement"),
        ("un incendie sans alarme", f"coût{NB}: la maison, ou pire"),
        grave_est_fn=True, pos=0.2, o=o)
panneau(340, "Filtre anti-pourriel",
        ("un vrai courriel jeté", f"coût{NB}: un message important perdu"),
        ("un pourriel dans la boîte", f"coût{NB}: une seconde d'agacement"),
        grave_est_fn=False, pos=0.8, o=o)
o.append(f'<text x="330" y="338" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">L\'alarme tolère les fausses alertes pour ne rien rater{FINE}; le filtre tolère ce qui passe pour ne rien jeter à tort.</text>')
o.append('</svg>')
(OUT / "erreurs-asymetriques.svg").write_text("\n".join(o) + "\n")
print("erreurs-asymetriques.svg écrit")
