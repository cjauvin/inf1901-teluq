"""Le découpage entraînement / test, et sa version avec une fuite (deux jumeaux)."""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module2"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, ROUGE, AXE = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#c4564a", "#b8a888")

# blocs
TX, TY, TW, TH = 40, 70, 395, 176          # entraînement
SX, SY, SW, SH = 475, 70, 145, 176         # test
ROWS = [115, 147, 179, 211]                # centrées sous l'étiquette « ≈ … cinquièmes »
COLS_T = [TX + (TW - 7 * 46) / 2 + i * 46 for i in range(8)]
COLS_S = [SX + SW / 2 - 37.5, SX + SW / 2 + 37.5]
JUMEAUX = [(COLS_T[6], ROWS[1], COLS_S[0], ROWS[1]), (COLS_T[7], ROWS[3], COLS_S[1], ROWS[3])]


def figure(fuite):
    h = 356 if fuite else 326
    titre = ("Une fuite : deux exemples du test ont un jumeau dans l'entraînement" if fuite
             else "On scinde les données avant d'entraîner")
    o = ['<svg viewBox="0 0 660 %d" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">' % h]
    if fuite:
        o.append("<title>Une fuite de données : le test n'est plus neuf</title>")
        o.append("<desc>Le même découpage entraînement / test, mais deux exemples du bloc de test ont un jumeau dans le bloc d'entraînement, reliés par un trait pointillé : les mêmes exemples, sous un déguisement. Le modèle les reconnaît au lieu de généraliser, et le score du test ment.</desc>")
    else:
        o.append("<title>Découpage entraînement / test</title>")
        o.append("<desc>L'ensemble des données est scindé en deux : un grand bloc d'entraînement (environ quatre cinquièmes) sur lequel le modèle apprend, et un petit bloc de test (environ un cinquième), mis de côté et jamais vu pendant l'entraînement, qui sert à mesurer la généralisation.</desc>")
    o.append(f'<rect x="0" y="0" width="660" height="{h}" rx="14" fill="{FOND}" stroke="{BORD}"/>')
    o.append(f'<text x="330" y="40" font-size="16" fill="{ENCRE}" text-anchor="middle" font-weight="600">{titre}</text>')
    o.append(f'<rect x="{TX}" y="{TY}" width="{TW}" height="{TH}" rx="11" fill="{TEAL}" fill-opacity="0.07" stroke="{AXE}" stroke-width="1.4"/>')
    jum = {(x, y) for x, y, _, _ in JUMEAUX} if fuite else set()
    o.append(f'<g fill="{TEAL}" stroke="{FOND}" stroke-width="1.3">')
    for y in ROWS:
        for x in COLS_T:
            if (x, y) not in jum:
                o.append(f'<circle cx="{x:.1f}" cy="{y}" r="7"/>')
    o.append('</g>')
    if fuite:
        o.append(f'<g fill="{BRUN}" stroke="{ROUGE}" stroke-width="2">')
        for x, y, _, _ in JUMEAUX:
            o.append(f'<circle cx="{x:.1f}" cy="{y}" r="7"/>')
        o.append('</g>')
        o.append(f'<g stroke="{ROUGE}" stroke-width="1.4" fill="none" stroke-dasharray="4 4">')
        for x1, y1, x2, y2 in JUMEAUX:
            o.append(f'<path d="M{x1 + 9:.1f} {y1 - 2} C {x1 + 60:.1f} {y1 - 22}, {x2 - 50:.1f} {y2 - 22}, {x2 - 9:.1f} {y2 - 2}"/>')
        o.append('</g>')
    cx = TX + TW / 2
    o.append(f'<text x="{cx:.0f}" y="93" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">≈ 4 cinquièmes</text>')
    o.append(f'<text x="{cx:.0f}" y="{TY + TH + 24}" font-size="15" fill="{TEAL}" text-anchor="middle" font-weight="600">Ensemble d\'entraînement</text>')
    o.append(f'<text x="{cx:.0f}" y="{TY + TH + 44}" font-size="12.5" fill="{GRIS}" text-anchor="middle">Le modèle apprend ici</text>')
    o.append(f'<rect x="{SX}" y="{SY}" width="{SW}" height="{SH}" rx="11" fill="{BRUN}" fill-opacity="0.08" stroke="{BRUN}" stroke-width="1.5" stroke-dasharray="6 5" opacity="0.95"/>')
    o.append(f'<g fill="{BRUN}" stroke="{FOND}" stroke-width="1.3">')
    for y in ROWS:
        for x in COLS_S:
            o.append(f'<circle cx="{x:.1f}" cy="{y}" r="7"/>')
    o.append('</g>')
    sx = SX + SW / 2
    o.append(f'<text x="{sx:.0f}" y="93" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">≈ 1 cinquième</text>')
    o.append(f'<text x="{sx:.0f}" y="{SY + SH + 24}" font-size="15" fill="{BRUN}" text-anchor="middle" font-weight="600">Ensemble de test</text>')
    o.append(f'<text x="{sx:.0f}" y="{SY + SH + 44}" font-size="12.5" fill="{GRIS}" text-anchor="middle">{"Censé être neuf" if fuite else "Gardé sous scellés"}</text>')
    if fuite:
        o.append(f'<text x="330" y="{h - 26}" font-size="13" fill="{ENCRE_PALE}" text-anchor="middle">Le modèle reconnaît ces deux-là au lieu de généraliser : le score du test le récompense pour sa mémoire.</text>')
    o.append('</svg>')
    return "\n".join(o) + "\n"


(OUT / "jeu-de-test.svg").write_text(figure(False))
(OUT / "fuite-de-donnees.svg").write_text(figure(True))
print("jeu-de-test.svg et fuite-de-donnees.svg écrits")
