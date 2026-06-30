---
title: "Classer"
weight: 60
slug: classer
---

# Classer

Le chapitre précédent nous a donné un vrai modèle qui apprend : une droite, deux
paramètres, une erreur à minimiser, une descente vers le creux. Mais il répond
toujours par un **nombre** — un prix. Or quantité de questions n'attendent pas un
nombre, plutôt une **catégorie** : ce courriel est-il un pourriel ? cette tumeur
est-elle bénigne ou maligne ? cette photo montre-t-elle un chat ou un chien ?
C'est la tâche de **classification**, déjà croisée au chapitre kNN — mais cette
fois, nous voulons un modèle qui *s'entraîne*.

Bonne nouvelle, annoncée en fin de chapitre : presque toute la machinerie va
resservir. Des paramètres réglables, une fonction d'erreur, une descente de
gradient pour la minimiser — ce trio est si général qu'il s'adapte aussi bien à
la classification qu'à la régression. Deux choses seulement changent : la
**forme** du modèle et la **façon de compter l'erreur**.

Pour la forme, le glissement est d'une simplicité élégante. En régression, la
droite *suivait* le nuage : elle passait *à travers* les points pour en épouser
la tendance. En classification, la droite *sépare* le nuage : elle passe *entre*
deux groupes pour les départager. Même objet — une droite, deux paramètres —
mais un rôle inversé.

{{< image src="/images/module2/suivre-vs-separer.svg" alt="Deux nuages de points côte à côte. À gauche, une droite traverse le nuage de maisons en suivant sa tendance : c'est la régression. À droite, une droite passe entre un groupe de points bleus et un groupe de points rouges pour les départager : c'est la classification." title="Deux usages de la même droite : à gauche elle suit le nuage (régression), à droite elle le sépare (classification)." loading="lazy" >}}

Pour fixer les idées, abandonnons un instant les maisons et imaginons le cas le
plus simple : des points de deux couleurs, `bleus` et `rouges`, dispersés dans
le plan (deux caractéristiques, $x_1$ et $x_2$). Apprendre à classer, ce sera
trouver la droite qui range le mieux les bleus d'un côté et les rouges de
l'autre. Et il y a, pour y arriver, deux grandes façons de penser — deux
philosophies que nous allons explorer tour à tour.

## Tracer une frontière : la régression logistique

La première façon de penser est la plus directe : si je veux séparer les bleus
des rouges, je n'ai qu'à **tracer la frontière** entre eux. Pas besoin de
comprendre ce qui distingue un bleu d'un rouge dans le fond — il me suffit de
trouver *où passe la ligne*. C'est l'approche dite **discriminative** : le modèle
apprend à discriminer les classes, sans chercher à les décrire.

Cette frontière, dans notre plan, c'est une droite — et nous savons déjà qu'une
droite tient en deux paramètres, une pente et une hauteur. Mais son rôle a
changé. En régression, on lisait la droite *verticalement* : à telle superficie,
tel prix. Ici, on la lit *latéralement* : de quel **côté** de la ligne tombe le
point ? D'un côté, on répond `bleu` ; de l'autre, `rouge`. La même équation,
$m x_1 + b$, ne sert plus à calculer une valeur mais à partager le plan en deux.

Cet algorithme porte un nom — la **régression logistique** — et, malgré ce nom
trompeur (il contient « régression » alors qu'il *classe*), c'est l'un des
classificateurs les plus utilisés au monde. Essayez-le : dans l'applet, déplacez
la ligne de décision pour séparer au mieux les deux groupes. Vous ajustez ainsi
ses deux paramètres à la main — exactement comme vous déplaciez la droite de
régression au chapitre précédent. Vous pouvez aussi ajouter, retirer ou déplacer
des points.

{{< applet src="/html/applets/logistic-regression.html" >}}

Et l'erreur ? C'est le second changement. On ne peut plus mesurer une « distance
verticale au point », puisqu'on ne prédit plus une valeur. Ce qu'on compte
désormais, c'est à quel point le modèle se **trompe de côté** : un point bien
rangé ne coûte rien, un point du mauvais côté coûte cher. La barre à droite de
l'applet affiche cette erreur. Cherchez à la rendre la plus petite possible —
idéalement zéro, quand la ligne sépare parfaitement les deux couleurs.

Vous remarquerez deux choses en jouant. D'abord, ce n'est **pas toujours
possible** d'atteindre zéro : si les couleurs se chevauchent, aucune droite ne
les sépare proprement. Ensuite, l'erreur ne dépasse jamais **50 %** : même la
pire ligne classe correctement la moitié des points par accident — et s'il fait
pire, le modèle n'a qu'à inverser sa convention (« ce côté-ci est rouge, pas
bleu ») pour repasser sous la barre.

{{% hint info %}}

Matière à réflexion : pourquoi n'est-il pas toujours possible de séparer
parfaitement les deux groupes par une droite ? Dans quelles conditions y
arrive-t-on ? Et qu'est-ce qui pourrait rendre la chose possible quand elle ne
l'est pas ? *(Nous y reviendrons : c'est l'une des grandes affaires du Module 3.)*

{{% /hint %}}

Reste la question de fond : comment la machine trouve-t-elle *seule* la bonne
ligne, sans qu'on la déplace à la souris ? La réponse ne vous surprendra pas —
c'est, mot pour mot, celle du chapitre précédent. L'erreur est une fonction des
deux paramètres ; cela dessine un paysage ; et la **descente de gradient** dévale
ce paysage jusqu'à son creux. Le même moteur, réutilisé tel quel. Seule la forme
de la fonction d'erreur diffère — pour ceux que les détails intéressent, les
voici.

{{% details "Les mathématiques de la régression logistique (optionnel)" %}}

Bien que nous en ayons parlé en termes purement géométriques, la régression
logistique est en réalité une méthode *probabiliste* : plutôt que de trancher
sèchement `bleu` ou `rouge`, elle estime la **probabilité** qu'un point soit
bleu. Un point loin de la frontière, du côté bleu, sera bleu « à 99 % » ; un
point juste sur la ligne, bleu « à 50 % » — l'hésitation maximale.

Pour transformer la position d'un point (une valeur quelconque) en une
probabilité (un nombre forcément entre 0 et 1), on emploie la **fonction
sigmoïde**, ou logistique — c'est elle qui donne son nom à l'algorithme. Sa
courbe en S écrase n'importe quelle valeur dans l'intervalle $[0, 1]$ :

![](/images/module2/Logistic-curve-02.png)

Adoptons la notation classique de l'apprentissage automatique. Un point est un
vecteur $\mathbf{x} = [x_1, x_2]$ ; sa vraie classe est $y \in \{0, 1\}$ (0 pour
rouge, 1 pour bleu, arbitrairement) ; les paramètres forment un vecteur
$\mathbf{w} = [w_1, w_2]$ accompagné de $b$. On calcule d'abord un **score** —
combien, et de quel côté, le point s'écarte de la frontière :

$$z = w_1 x_1 + w_2 x_2 + b$$

puis on le passe dans la sigmoïde pour obtenir la probabilité estimée :

$$\hat{y} = \frac{1}{1 + e^{-z}}$$

où $\hat{y} \in [0, 1]$ est une *probabilité*, à distinguer de $y \in \{0, 1\}$,
la *vraie* classe. La décision finale est alors : bleu si $\hat{y} \ge 0{,}5$,
rouge sinon.

L'erreur sur un point compare la probabilité prédite $\hat{y}$ à la vérité $y$.
On utilise l'**entropie croisée** :

$$E(y, \hat{y}) = -\big[\,y \log(\hat{y}) + (1 - y)\log(1 - \hat{y})\,\big]$$

Son comportement est exactement celui qu'on souhaite : si le point est bleu
($y = 1$) et que le modèle en est sûr ($\hat{y} = 0{,}9$), l'erreur est minime
($-\log 0{,}9 \approx 0{,}1$) ; mais s'il se trompe avec aplomb
($\hat{y} = 0{,}1$ pour un vrai bleu), l'erreur explose
($-\log 0{,}1 \approx 2{,}3$). La confiance mal placée est lourdement punie.

L'erreur totale, sur les $n$ points, en est la moyenne :

$$J(\mathbf{w}, b) = \frac{1}{n} \sum_{i=1}^{n} E\big(y^{(i)}, \hat{y}^{(i)}\big)$$

C'est cette fonction $J(\mathbf{w}, b)$ qui joue le rôle de « paysage » : à chaque
choix de paramètres, une hauteur d'erreur. La descente de gradient en mesure la
pente,

$$\frac{\partial J}{\partial \mathbf{w}} = \frac{1}{n} \sum_{i=1}^n \big(\hat{y}^{(i)} - y^{(i)}\big)\,\mathbf{x}^{(i)}, \qquad \frac{\partial J}{\partial b} = \frac{1}{n} \sum_{i=1}^n \big(\hat{y}^{(i)} - y^{(i)}\big)$$

et fait un pas en sens inverse, d'une taille réglée par le taux d'apprentissage
$\alpha$ :

$$\mathbf{w} \leftarrow \mathbf{w} - \alpha\,\frac{\partial J}{\partial \mathbf{w}}, \qquad b \leftarrow b - \alpha\,\frac{\partial J}{\partial b}$$

On répète jusqu'à ce que l'erreur ne diminue plus. C'est, trait pour trait, la
mécanique du chapitre précédent — seule la fonction d'erreur a changé de visage.

{{% /details %}}
