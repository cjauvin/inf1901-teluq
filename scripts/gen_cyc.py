"""Quelques assertions et règles de CYC, dans sa langue (CycL), avec leur traduction.

Exemples tirés de la documentation de CycL (article « CycL » de Wikipédia).
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "static" / "images" / "module1"
FOND, BORD, ENCRE, ENCRE_PALE, GRIS, TEAL, BRUN, AXE, PANNEAU = (
    "#efe7d3", "#d9cbac", "#3a3531", "#5b5249", "#7a6f63", "#2f6f6a", "#9a5b33", "#b8a888", "#fbf7ee")
NB, FINE = " ", " "
MONO = "ui-monospace, 'SF Mono', Menlo, Consolas, monospace"

ENTREES = [
    (["(#$isa #$BillClinton", "      #$UnitedStatesPresident)"], "Bill Clinton fait partie des", "présidents des États-Unis."),
    (["(#$genls #$Tree-ThePlant #$Plant)"], "Tous les arbres sont", "des plantes."),
    (["(#$capitalCity #$France #$Paris)"], "Paris est la capitale", "de la France."),
    (["(#$relationAllExists", "   #$biologicalMother", "   #$ChordataPhylum #$FemaleAnimal)"],
     "Tout animal à colonne vertébrale", "a une mère biologique, un animal femelle."),
    (["(#$implies", "   (#$and (#$isa ?OBJ ?SUBSET)", "          (#$genls ?SUBSET ?SUPERSET))", "   (#$isa ?OBJ ?SUPERSET))"],
     "Règle : si un objet appartient à une", "catégorie, il appartient aussi à toutes", "celles qui la contiennent."),
]

W = 660
o_corps, y = [], 76
for code, *trad in ENTREES:
    h = max(len(code), len(trad)) * 17 + 18
    o_corps.append(f'<rect x="28" y="{y}" width="{W - 56}" height="{h}" rx="7" fill="{PANNEAU}" stroke="{AXE}" stroke-width="1"/>')
    for i, l in enumerate(code):
        o_corps.append(f'<text x="44" y="{y + 22 + i * 17}" font-size="12.5" fill="{TEAL}" font-family="{MONO}" xml:space="preserve">{l}</text>')
    for i, l in enumerate(trad):
        o_corps.append(f'<text x="{W - 44}" y="{y + 22 + i * 17}" font-size="12.5" fill="{ENCRE}" text-anchor="end">{l}</text>')
    y += h + 10
H = y + 44
o = ['<?xml version="1.0" encoding="UTF-8"?>',
     f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" font-family="system-ui, -apple-system, sans-serif">',
     "<title>Quelques assertions de CYC, dans sa langue (CycL)</title>",
     f"<desc>Cinq entrées de la base de CYC, écrites dans son langage, CycL, avec leur traduction en français. «{FINE}#$isa #$BillClinton #$UnitedStatesPresident{FINE}»{NB}: Bill Clinton fait partie des présidents des États-Unis. «{FINE}#$genls #$Tree-ThePlant #$Plant{FINE}»{NB}: tous les arbres sont des plantes. «{FINE}#$capitalCity #$France #$Paris{FINE}»{NB}: Paris est la capitale de la France. Une assertion dit que tout animal à colonne vertébrale a une mère biologique. Enfin, une règle générale{NB}: si un objet appartient à une catégorie, il appartient aussi à toutes celles qui la contiennent.</desc>",
     f'<rect x="0" y="0" width="{W}" height="{H}" rx="14" fill="{FOND}" stroke="{BORD}"/>',
     f'<text x="{W / 2}" y="36" font-size="15" fill="{ENCRE}" text-anchor="middle" font-weight="600">Le sens commun, écrit à la main{NB}: quelques entrées de CYC</text>',
     f'<text x="44" y="62" font-size="11.5" fill="{GRIS}" font-style="italic">dans la langue de CYC (CycL)</text>',
     f'<text x="{W - 44}" y="62" font-size="11.5" fill="{GRIS}" font-style="italic" text-anchor="end">ce que cela veut dire</text>']
o += o_corps
o.append(f'<text x="{W / 2}" y="{H - 18}" font-size="12.5" fill="{ENCRE_PALE}" text-anchor="middle">Des millions d\'entrées de ce genre, saisies une à une pendant des décennies.</text>')
o.append('</svg>')
(OUT / "cyc-assertions.svg").write_text("\n".join(o) + "\n")
print("cyc-assertions.svg écrit, hauteur", H)
