---
title: "L'algorithme le plus simple"
weight: 35
---

# L'algorithme d'apprentissage le plus simple (les $k$ plus proches voisins)

Commençons par étudier le problème le plus fondamental et représentatif de
l'apprentissage automatique, celui de la classification d'objets. Par exemple,
pouvoir dire si l'image sur cette photo est celle d'un chien, ou d'un chat. Si
on considère de nouveau notre [scénario initial]({{< relref
"docs/module2/scénario-réel" >}}), on peut synthétiser la structure du problème
de la manière suivante :

* Nous avons à priori une série d'**objets** existants (des données)
* Chaque objet a des **caractéristiques** qui le décrivent, ainsi qu'une **classe** (on parle parfois aussi d'une _étiquette_, ou label en anglais)
* Il est possible de mesurer la **distance** qui sépare deux objets (en se basant sur les caractéristiques)
* Pour un _nouvel_ objet qu'on nous donne, dont on connaît les caractéristiques
  mais **pas** la classe (parce que personne nous l'a donnée), nous aimerions la
  _prédire_ (la classe)

L'algorithme le plus simple pour faire cela est assurément celui des $k$ plus
proches voisins ($k$-NN, $k$ Nearest Neighbors). Pour chaque point que l'on désire
classer, il suffit de considérer ses $k$ plus proches voisins (_proche_, dans la
plupart des contextes géométriques, veut dire en terme de la [distance
euclidienne](https://fr.wikipedia.org/wiki/Distance_euclidienne)) et de choisir
la classe majoritaire. L'applet interactive suivante illustre ce
fonctionnement, à l'aide de points rouges et bleus en deux dimensions.

Dans cet exemple :

* Les caractéristiques des points 2D sont leurs coordonnées $x$ et $y$
* Leurs classes sont `rouge` ou `bleu`
* La distance entre les points est la [distance euclidienne](https://fr.wikipedia.org/wiki/Distance_euclidienne)
* Les régions en bleu et rouge pâle correspondent à la classification de tout
  nouveau point ajouté dans cette région (un point apparaît en cliquant)

{{< applet src="/html/applets/knn.html" >}}

Pourquoi dit-on que cet algorithme est le plus simple? Parce que contrairement à d'autres
algorithmes d'apprentissage que nous verrons plus tard :

* Il y a un seul paramètres qui doit être "appris" : $k$, soit le nombre de voisins consultés;
* Il n'y a pas de processus d’entraînement, à proprement parler : dès qu'on a un
  ensemble de données étiquetées, l'algorithme est prêt à être utilisé; si on ajoute un nouveau point, il est
  instantanément classé, en fonction de ses $k$ plus proches voisins

{{% hint info %}}

Dans un sens, les données d’entraînement, accompagnées d'un choix de valeur pour
$k$, constitue l'algorithme, ou le modèle lui-même.

{{% /hint %}}

## Le compromis, ou dilemme biais-variance

Nous allons maintenant introduire deux notions fondamentales en apprentissage
automatique, qui vont nous permettre d'en comprendre l'enjeu, ou la difficulté
principale.

Le **biais** d'un modèle est l'erreur qu'il introduit avec ses hypothèses de
départ, ce qu'il considère comme étant vrai à priori, avant même de commencer à
apprendre. Par exemple, si mon "modèle" du temps estimé pour me rendre au
travail est que "ça prend toujours 20 minutes", alors dans certains cas, il sera en erreur, car il
n'aura pas pris en considération le fait qu'il pleut aujourd'hui, ou que c'est
le jour du Tour de l'Ile à Montréal.

La **variance** d'un modèle est l'erreur qui est introduite quand j'essaie de
bâtir un modèle à partir de _ces_ exemples particuliers (les données
d’entraînement particulières) plutôt que _ceux-là_. Il s'agit donc de l'erreur
qui correspond aux variations naturelles, ou accidentelles, qu'on observe dans
la nature, ce qu'on nomme parfois aussi le **bruit**. Par exemple, si mon
"modèle" du temps estimé pour me rendre au travail est "20 minutes le lundi",
"30 minutes le mardi", et ainsi de suite, il est très probable que ce modèle
colle de trop près à la réalité, et qu'il tente trop de généraliser à partir de
ce qui n'est, au fond, que des fluctuations aléatoires (le fait que ça m'a pris
20 minutes pour me rendre au travail lundi passé est assez peu corrélé avec le
temps que ça me prendra le lundi suivant, et c'est probablement une erreur de
trop vouloir généraliser).

Nous pouvons analyser notre algorithme des plus proches voisins à la lumière de
ces notions : quand $k$ est petit, la variance du modèle est très élevée, et les
particularités individuelles des données (le fait que _ce_ point rouge soit
exactement _ici_, plutôt que _là_) ont une grande importance. On parle ici de
**sur-apprentissage** (overfitting). À l'inverse, quand $k$ est très grand,
c'est le biais qui devient très élevé : le modèle prend en considération un très
grand nombre de facteurs (c-à-d de points) pour prendre une décision, et
probablement qu'il s'agit d'une généralisation excessive. On parle alors de
**sous-apprentissage** (underfitting). Le modèle aurait probablement avantage,
dans ce cas, à considérer les données de manière un peu plus spécifique.

On considère en général que ces deux notions sont l'inverse, l'une de l'autre :
quand le biais d'un modèle augmente, sa variance diminue, et vice versa.
L'apprentissage automatique constitue donc l'art de trouver un bon compromis
entre ces deux extrêmes.

![](/images/module2/bias-vs-variance.png)

## Deux types d'erreur

Quand on joue avec l'applet interactive ci-haut, et qu'on choisit $k=1$, on
remarque que l'erreur est zéro. Ceci est dû au fait que par définition, un point
est lui-même inclus dans ses $k$ voisins, donc quand le point est seul, il ne
peut y avoir aucune erreur. En augmentant $k$, le nombre d'erreurs augmente
généralement. On pourrait imaginer qu'un algorithme qui ne commet aucune erreur
est désirable, mais dans le cas de $k$-NN, ce résultat en apparence
impressionnant est tout simplement trivial, car il est obtenu par définition.
Comme cette erreur est calculée sur le jeu de données correspondant à
l’entraînement, on parle alors d'**erreur d’entraînement**. En apprentissage
automatique, il est souvent possible, avec différents algorithmes, de faire en
sorte que cette erreur soit très proche de zéro. Pourtant, l'erreur qui nous
intéresse réellement est celle calculée à partir d'un autre jeu de données, qui
n'a _pas_ participé à l’entraînement du modèle : on parle alors de l'**erreur de
test**. Contrairement à l'erreur d’entraînement, qui est minimisée dans le cas
des $k$ plus proches voisins quand $k=1$, l'erreur de test aura tendance à être
minimisée à la valeur de $k$ qui correspond au meilleur compromis
biais-variance, comme l'illustre ce diagramme :

![](/images/module2/bias-vs-variance-with-errors.png)

Nous verrons que ce principe est très général en apprentissage automatique, et
qu'il permet de guider la recherche du "meilleur" modèle, celui dont les
capacités de généralisation sont les plus grandes, ce qui constitue un des buts
fondamentaux de l'intelligence artificielle.

{{% hint warning %}}

Des résultats récents en apprentissage profond ont toutefois apporté de grandes
surprises, car il semble que ce principe, qui était considéré comme étant
immuable et indiscutable depuis des décennies, peut être, dans certaines
circonstances, [remis en
question](https://en.wikipedia.org/wiki/Double_descent)!

{{% /hint %}}

