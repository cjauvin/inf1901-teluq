---
title: "Un modèle qui s'entraîne"
weight: 50
slug: entrainer-un-modele
---

# Un modèle qui s'entraîne

Le chapitre précédent s'est achevé sur un souhait : un modèle qui ne se contente
pas de mémoriser les exemples, mais qui en *extrait* quelque chose — une tendance
générale, résumée en quelques paramètres, qu'on pourra ensuite appliquer sans
traîner toutes les données derrière soi.

Construisons-le. Et puisque nous cherchons le plus simple, faisons le geste le
plus élémentaire qu'on puisse imaginer devant un nuage de points : **y faire
passer une droite.**

## Un modèle qui tient en deux nombres

Reprenons notre nuage de maisons — la superficie en horizontale, le prix en
verticale. Faire passer une droite à travers ce nuage, c'est parier qu'il existe
une relation simple et régulière entre la taille d'une maison et son prix :
« chaque mètre carré supplémentaire ajoute, en gros, tant de dollars ». Cette
droite, c'est notre modèle.

{{< image src="/images/module2/maisons-droite.svg" alt="Le nuage de maisons traversé par une droite inclinée qui en épouse la tendance : le modèle de régression linéaire." title="La droite qui épouse le nuage : voilà notre modèle." loading="lazy" >}}

Et une droite, en mathématiques, se résume à deux nombres :

$$\text{prix} = m \times \text{superficie} + b$$

- **m**, la *pente* : de combien le prix monte quand la superficie augmente d'une
  unité ;
- **b**, l'*ordonnée à l'origine* : le point de départ, là où la droite croise
  l'axe vertical.

Ces deux nombres, m et b, sont les **paramètres** du modèle — et, cette fois, ils
veulent dire quelque chose. Là où le modèle bête de la page 20 distillait tout en
un seul nombre (la moyenne), et où kNN n'en avait aucun, notre droite en a deux :
juste assez pour capturer une *tendance* — une direction et une hauteur. Changez
m et b, et vous obtenez une autre droite, donc un autre modèle. Tout le jeu va
consister à trouver le bon couple (m, b) : celui de la droite qui épouse le mieux
le nuage.

Essayez vous-même. Dans l'applet ci-dessous, déplacez la droite — vous ajustez
ainsi m et b à la main — et cherchez la position qui colle le mieux aux points.

{{< applet src="/html/applets/linear-regression.html" >}}

## Mesurer l'erreur

En déplaçant la droite, vous avez forcément cherché à « bien » la placer. Mais
qu'est-ce que « bien », au juste ? Il nous faut une mesure — et nous l'avons déjà
croisée, page 20, sans lui donner encore de définition précise : l'**erreur**.

Pour une droite donnée, l'erreur sur une maison, c'est l'écart entre le prix que
la droite *prédit* (le point de la droite à la verticale de cette maison) et son
prix *réel*. C'est, exactement comme à la page 20, un segment vertical — sauf
qu'ici la droite est *inclinée*, et qu'elle peut donc serrer les points de bien
plus près qu'une droite plate.

{{< image src="/images/module2/maisons-erreurs-droite.svg" alt="Le nuage de maisons et la droite de régression inclinée, avec un court segment rouge reliant chaque maison à la droite : l'erreur, bien plus courte qu'avec la droite plate de la page 20." title="Les mêmes erreurs qu'à la page 20, mais contre une droite inclinée : bien plus courtes." loading="lazy" >}}

L'erreur totale du modèle combine tous ces écarts. On les met au carré (pour que
les écarts au-dessus et en dessous ne s'annulent pas, et pour pénaliser
davantage les grosses bourdes), puis on en fait la moyenne. Ce nombre unique — la
moyenne des carrés des écarts — porte un nom un peu technique, l'*erreur
quadratique moyenne*, mais l'idée est simple : **plus il est petit, mieux la
droite épouse le nuage.**

Une jolie façon de *sentir* cette erreur : imaginez que chaque point est relié à
la droite par un petit ressort vertical. Un point éloigné tire fort ; un point
proche, à peine. La meilleure droite est celle où tous ces ressorts, tirant
chacun de leur côté, s'équilibrent — la position de moindre tension. C'est
*exactement* la droite de plus petite erreur. Jouez avec :

{{< applet src="/html/applets/linear-regression-with-springs.html" >}}

Trouver cette droite idéale à la main, comme dans l'applet, reste faisable en
deux dimensions. Mais comment une machine y parvient-elle *seule* — et même quand
il n'y a plus deux paramètres, mais des milliers ? C'est la dernière pièce, et la
plus belle.

## Apprendre, c'est descendre la pente

Voici l'idée maîtresse — celle qui, sous une forme ou une autre, fait tourner
*tout* l'apprentissage automatique moderne, jusqu'aux plus grands modèles
d'aujourd'hui.

Repartons de l'erreur. Pour chaque choix de paramètres (m, b), le modèle commet
une certaine erreur totale : l'erreur est donc elle-même une *fonction* des
paramètres. Imaginons alors un **paysage** : les deux paramètres sont les
coordonnées sur une carte (est-ouest pour m, nord-sud pour b), et l'erreur est
l'**altitude** en chaque point. Les hauteurs sont les mauvais modèles (grande
erreur) ; les vallées, les bons. Trouver le meilleur modèle, c'est trouver le
**point le plus bas** de ce paysage.

{{< image src="/images/module2/descente-gradient.svg" alt="Une vallée en U représentant l'erreur selon les réglages du modèle. Une bille lâchée au hasard sur le versant gauche descend pas à pas vers le creux, marqué « meilleur modèle »." title="La descente de gradient, vue en coupe : la bille dévale la vallée d'erreur jusqu'au creux." loading="lazy" >}}

Comment l'atteindre, sans carte du relief ? La machine fait ce que ferait un
randonneur dans le brouillard : elle tâte la **pente** sous ses pieds et fait un
pas dans la direction qui descend le plus. Puis elle recommence. Pas après pas,
elle dévale vers le creux — comme une bille lâchée sur le flanc d'une vallée
roule vers le fond. Quand la pente s'annule, le fond est atteint : les meilleurs
paramètres sont trouvés. Cette méthode porte un nom — la **descente de gradient**
(le « gradient » étant simplement la direction de plus forte pente) — et c'est
*le* moteur de l'apprentissage.

Un détail compte : la taille des pas. Trop grands, on risque d'enjamber le creux
et de zigzaguer sans fin ; trop petits, la descente dure une éternité. Ce réglage
— le *taux d'apprentissage* — n'est pas un paramètre du modèle, mais un réglage
de la *procédure* : on l'appelle un **hyper-paramètre**.

Reconnaissez-vous quelque chose ? À la toute fin du Module 1, nous annoncions
qu'*« apprendre, c'est encore chercher, mais dans un autre espace »* — non plus
fouiller les coups d'une partie d'échecs, mais l'immensité des réglages possibles
d'un modèle. Nous y sommes : la descente de gradient *est* cette recherche. Là où
le GOFAI cherchait *la solution*, l'apprentissage cherche *de quoi la fabriquer*
— les paramètres. Et sa beauté est de ne pas changer d'échelle : que le paysage
ait deux dimensions (m et b) ou plusieurs milliards (les poids d'un grand réseau
de neurones), c'est toujours la même marche vers le bas.

{{% details "Les mathématiques de la régression linéaire (optionnel)" %}}

L'erreur quadratique moyenne, pour $n$ maisons, s'écrit :

$$J(m, b) = \frac{1}{n} \sum_{i=1}^{n} \big(y_i - (m x_i + b)\big)^2$$

où $x_i$ est la superficie de la maison $i$, $y_i$ son vrai prix, et $m x_i + b$
le prix prédit. C'est la « carte d'altitude » du paysage : à chaque couple
$(m, b)$, une hauteur d'erreur.

La descente de gradient mesure, en un point, la pente de cette surface dans
chaque direction (les *dérivées partielles*) :

$$\frac{\partial J}{\partial m} = -\frac{2}{n} \sum_{i=1}^{n} x_i\big(y_i - (m x_i + b)\big), \qquad \frac{\partial J}{\partial b} = -\frac{2}{n} \sum_{i=1}^{n} \big(y_i - (m x_i + b)\big)$$

puis fait un pas en sens inverse de la pente, d'une taille réglée par le taux
d'apprentissage $\alpha$ :

$$m \leftarrow m - \alpha\,\frac{\partial J}{\partial m}, \qquad b \leftarrow b - \alpha\,\frac{\partial J}{\partial b}$$

On répète jusqu'à ce que l'erreur ne diminue plus. *(Pour la régression
linéaire, il existe même une formule directe — les moindres carrés de Gauss —
qui donne la solution d'un coup ; mais la descente de gradient, elle, marche pour
des modèles bien plus complexes, jusqu'aux réseaux de neurones.)*

{{% /details %}}

## Et pour prédire une catégorie ?

Nous avons maintenant un vrai modèle qui apprend : une droite, deux paramètres,
une erreur à minimiser, une descente vers le creux. Et il prédit un **nombre** —
un prix.

Mais quantité de questions n'attendent pas un nombre pour réponse, plutôt une
**catégorie**. Ce courriel est-il un pourriel, oui ou non ? Cette photo
montre-t-elle un chat ou un chien ? Nous avons rencontré ce type de tâche au
chapitre kNN : la **classification**. Mais kNN, justement, n'apprenait rien. Nous
aimerions cette fois un modèle qui *s'entraîne* — comme notre droite — mais dont
la sortie soit une catégorie plutôt qu'une valeur.

Bonne nouvelle : presque toute la machinerie que nous venons de bâtir va
resservir. Un modèle réglé par des paramètres, une fonction d'erreur, une
descente de gradient pour la minimiser — ce trio est si général qu'il s'adapte
aussi bien à la classification qu'à la régression. Il suffira de revoir la
*forme* du modèle (une droite qui *sépare*, plutôt qu'une droite qui *suit*) et
la *façon de compter l'erreur*. C'est l'objet du prochain chapitre.
