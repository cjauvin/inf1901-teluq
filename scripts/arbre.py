"""Un arbre de décision minimal (CART), sans dépendance, pour les figures du cours.

Classification : impureté de Gini ; régression : variance. À chaque nœud, on
essaie chaque caractéristique et chaque seuil à mi-chemin entre deux valeurs
consécutives, et l'on garde la coupe qui réduit le plus l'impureté.
"""


class Noeud:
    def __init__(self, exemples, profondeur):
        self.exemples = exemples          # liste de (x: tuple, y)
        self.profondeur = profondeur
        self.j = None                     # caractéristique de la question
        self.seuil = None
        self.gauche = self.droite = None  # x[j] <= seuil → gauche

    @property
    def feuille(self):
        return self.j is None

    def __len__(self):
        return len(self.exemples)


def gini(ys):
    n = len(ys)
    if n == 0:
        return 0.0
    p = sum(1 for y in ys if y) / n
    return 2 * p * (1 - p)


def variance(ys):
    n = len(ys)
    if n == 0:
        return 0.0
    m = sum(ys) / n
    return sum((y - m) ** 2 for y in ys) / n


def apprendre(exemples, profondeur_max, regression=False, min_feuille=1, profondeur=0):
    noeud = Noeud(exemples, profondeur)
    impurete = variance if regression else gini
    ys = [y for _, y in exemples]
    if profondeur >= profondeur_max or len(exemples) < 2 * min_feuille or impurete(ys) == 0:
        return noeud
    meilleur = None
    n = len(exemples)
    for j in range(len(exemples[0][0])):
        valeurs = sorted(set(x[j] for x, _ in exemples))
        for a, b in zip(valeurs, valeurs[1:]):
            seuil = (a + b) / 2
            g = [y for x, y in exemples if x[j] <= seuil]
            d = [y for x, y in exemples if x[j] > seuil]
            if len(g) < min_feuille or len(d) < min_feuille:
                continue
            score = (len(g) * impurete(g) + len(d) * impurete(d)) / n
            if meilleur is None or score < meilleur[0] - 1e-12:
                meilleur = (score, j, seuil)
    if meilleur is None or meilleur[0] >= impurete(ys) - 1e-12:
        return noeud
    _, noeud.j, noeud.seuil = meilleur
    noeud.gauche = apprendre([e for e in exemples if e[0][noeud.j] <= noeud.seuil], profondeur_max, regression, min_feuille, profondeur + 1)
    noeud.droite = apprendre([e for e in exemples if e[0][noeud.j] > noeud.seuil], profondeur_max, regression, min_feuille, profondeur + 1)
    return noeud


def predire(noeud, x, regression=False):
    while not noeud.feuille:
        noeud = noeud.gauche if x[noeud.j] <= noeud.seuil else noeud.droite
    ys = [y for _, y in noeud.exemples]
    if regression:
        return sum(ys) / len(ys)
    return sum(1 for y in ys if y) * 2 >= len(ys)


def feuilles(noeud):
    if noeud.feuille:
        return [noeud]
    return feuilles(noeud.gauche) + feuilles(noeud.droite)


def profondeur_reelle(noeud):
    if noeud.feuille:
        return 0
    return 1 + max(profondeur_reelle(noeud.gauche), profondeur_reelle(noeud.droite))
