---
title: "Le concept de similarité"
weight: 35
---

# Le concept de similarité

Nous avons vu avec l'algorithme des [plus proches voisins]({{< relref
"docs/module2/algo-le-plus-simple/" >}}) qu'une notion essentielle est de
pouvoir mesurer la distance entre deux objets, afin de déterminer à quel point
ils sont similaires. Mais que veut-on dire exactement par cela? Pour de simples
points en deux dimensions, nous avons une conception intuitive raisonnable : il
s'agit de la [distance
euclidienne](https://fr.wikipedia.org/wiki/Distance_euclidienne) entre les deux
points.

![](/images/module2/distance_2d.png)

Pour d'autres types d'objets (ou de données), comme des images, par exemple,
bien que cela soit plus difficile à imaginer, il faut transposer son intuition
géométrique dans un espace à plus haute dimension, par exemple un espace où
chaque pixel d'une image correspond à une dimension :

![](/images/module2/distance_high_dim.png)

Dans ce sens particulier, une image correspond donc à un vecteur en très haute
dimension. En fait pour la plupart des données de type numérique (comme par
exemple les rangées d'un tableau Excel) il est possible d'utiliser la même
représentation, comme nous l'avons vu déjà :

![](/images/module2/distance_high_dim2.png)

## Distance entre les mots ou les concepts

Mais supposons maintenant que nous voulions mesurer la distance entre deux mots,
ou deux concepts, que pourrions-nous faire?

![](/images/module2/distance_mots.png)

Une possibilité serait de considérer un espace composé par les 26 lettres de
l'alphabet, où la présence d'une lettre dans un mot serait représentée par la
valeur 1 dans la dimension correspondante, ou 0 sinon.

![](/images/module2/distance_mots2.png)

## Distance de Levenshtein

Une autre possibilité, très utilisée en pratique, est la [distance de
Levenshtein](https://fr.wikipedia.org/wiki/Distance_de_Levenshtein), (aussi
appelée distance d'édition), qui permet de quantifier la différence entre deux
chaines de caractères, en terme du nombre d'opérations à effectuer, pour
transformer une chaîne en une autre. Utilisez l'application interactive ci-dessous
pour mesurer la distance de Levenshtein entre les mots "navire" et "bateau" :

{{< applet src="/html/applets/levenshtein.html" width="140%" scale="0.9" >}}

Bien que cette notion particulière de distance soit très utile pour faire des
applications qui permettent par exemple de corriger des erreurs d'orthographe
(ou de faire en sorte que les requêtes Google soient plus flexibles), elle est
moins utile pour l'apprentissage automatique. Comment ChatGPT peut faire en
sorte, par exemple, de considérer que les mots "navire" et "bateau" sont
_sémantiquement_ proches (et possiblement interchangeables), si les notions de
distance que nous avons considérées jusqu'à maintenant ne permettent pas d'en
offrir une mesure concrète?

## Modélisation du contexte des mots

Une manière de résoudre et de modéliser le sens des mots (ce qu'ils veulent
dire)  est de considérer les mots qui ont tendance à accompagner certains mots.
On peut ainsi construire un espace vectoriel où chaque dimension correspond à un
mot du vocabulaire. Un mot particulier, comme "chat", par exemple, aura des
valeurs qui correspondront aux mots qu'on a tendance à retrouver dans son
contexte, comme par exemple : ronronner, souris, miauler, etc. On peut
considérer que le sens du mot chat est déterminé par le champ lexical des mots
qui ont tendance à l'accompagner.

![](/images/module2/distance_mots3.png)

Cette approche fonctionne et est utilisée en pratique, mais elle présente des
problèmes pour les algorithmes d'apprentissage automatique. Premièrement
l'espace comporte un très grand nombre de dimensions (si on considère un
vocabulaire de 100,000 mots, par exemple), dont la plupart seront de valeur zéro
(car la plupart des mots ne se retrouvent pas dans le contexte immédiat d'un mot
particulier). Les algorithmes d'apprentissage ont de la difficulté à opérer dans
un tel type d'espace (beaucoup de dimensions, dont la plupart à zéro, donc de
_densité_ très faible).

## Les plongements lexicaux (word embeddings)

Une autre solution est de représenter les mots dans un espace de dimension
moyenne (par exemple 512), dont la densité sera beaucoup plus grande (toutes les
dimensions seront non-zéro, donc "utilisées"). La contrepartie, ce que l'on
perd, avec un tel espace, est la signification des dimensions. Si la dimension
127 du précédent modèle correspondait au mot "chat", par exemple, ici, dans cet
espace, elle ne correspond à aucun mot en particulier. On parle d'un espace
_latent_. L'avantage d'une tel espace est qu'il constitue un substrat malléable,
à partir duquel un algorithme d'apprentissage peut façonner sa propre
représentation des mots et de leur sens, de manière interne. La position des
mots, ainsi que la signification de ses dimensions, n'est pas déterminée
d'avance, avant le début de l’entraînement. C'est plutôt le processus
d’entraînement qui entraîne leur définition, par optimisation. L'algorithme
apprend le sens des mots, et s'en construit une représentation, avec un
"vocabulaire" qui lui est propre. Ce mécanisme de représentation particulier est
ce qui explique, en partie, l'extraordinaire puissance de ChatGPT.

![](/images/module2/distance_mots4.png)
