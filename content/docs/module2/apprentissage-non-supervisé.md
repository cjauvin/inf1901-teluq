---
title: "Apprentissage non supervisé"
weight: 70
draft: false
---

# L'apprentissage non supervisé

Contrairement à l'apprentissage supervisé, où les données d'entraînement
incluent explicitement les "bonnes réponses" (sous forme d'étiquettes ou de
valeurs cibles), l'apprentissage non supervisé opère sur des données brutes,
sans aucune guidance externe. L'algorithme doit découvrir par lui-même des
structures cachées, des patterns ou des regroupements dans les données. C'est un
peu comme explorer un territoire inconnu sans carte : on observe les
similarités, les regroupements naturels, ou les anomalies, pour en déduire une
organisation. Cela rend l'approche plus exploratoire et moins directive, idéale
pour des tâches comme la segmentation de clients en marketing, la compression de
données, ou la détection d'anomalies en cybersécurité.

Parmi les tâches courantes en non supervisé, on trouve le clustering (regrouper
des éléments similaires), la réduction de dimensionnalité (simplifier des
données complexes sans perdre trop d'information), ou l'apprentissage de
représentations (comme trouver des features latentes dans des images). Nous
allons nous concentrer sur un algorithme classique de clustering : $k$-means, qui
illustre bien les principes de base. Mais avant d'entrer dans les détails,
notons qu'il existe de nombreux autres algorithmes dans cette famille, comme
DBSCAN (qui gère mieux les formes irrégulières et le bruit), le clustering
hiérarchique (qui construit une arborescence de regroupements), la PCA (Analyse
en Composantes Principales, pour réduire la dimensionnalité en projetant les
données sur des axes optimaux), ou encore les autoencodeurs (des réseaux de
neurones qui apprennent à compresser et reconstruire les données, révélant ainsi
des structures sous-jacentes).

## Clustering avec $k$-means

$k$-means est l'un des algorithmes les plus simples et les plus utilisés pour le
clustering. L'idée de base est de partitionner un ensemble de points en $k$
groupes (ou clusters), où $k$ est un nombre que l'on choisit à l'avance. Chaque
cluster est représenté par un "centroïde" (le point moyen du groupe), et
l'algorithme vise à minimiser la distance totale entre les points et leur
centroïde assigné. C'est comme organiser une fête où vous voulez regrouper les
invités en $k$ tables, en plaçant chaque table au centre de son groupe pour que
tout le monde soit le plus proche possible de sa table.

Voici comment ça fonctionne intuitivement :

1. Choisissez aléatoirement $k$ points initiaux comme centroïdes (ils peuvent être des points réels des données ou générés aléatoirement).
2. Assignez chaque point de données au centroïde le plus proche (généralement en utilisant la distance euclidienne, comme la distance en ligne droite dans un plan).
3. Recalculez la position de chaque centroïde comme la moyenne des points assignés à son cluster.
4. Répétez les étapes 2 et 3 jusqu'à ce que les assignments ne changent plus (ou que le changement soit négligeable).

À la fin, vous obtenez $k$ clusters bien définis, où les points à l'intérieur d'un même cluster sont plus similaires entre eux qu'avec ceux des autres clusters. C'est particulièrement utile pour des données en 2D ou 3D, comme des coordonnées géographiques ou des caractéristiques de produits, mais ça s'étend à plus de dimensions.

{{% hint info %}}

Matière à réflexion : Comment choisir la valeur optimale de $k$? Que se
passe-t-il si les clusters ne sont pas sphériques ou si les données ont du bruit
? (Indice : des méthodes comme la "méthode du coude" aident pour $k$, et d'autres
algorithmes comme DBSCAN gèrent mieux les irrégularités.)

{{% /hint %}}

{{% details "Les mathématiques de $k$-means (optionnel)" %}}

Mathématiquement, $k$-means vise à minimiser une fonction d'erreur appelée l'inertie (ou somme des carrés intra-cluster) :

$$ J = \sum_{i=1}^{n} \min_{j=1}^{k} \| \mathbf{x}_i - \boldsymbol{\mu}_j \|^2 $$

où :

* $\mathbf{x}_i$ est le i-ème point de données,
* $\boldsymbol{\mu}_j$ est le centroïde du j-ème cluster,
* $| \cdot |^2$ est la distance euclidienne au carré,
* La minimisation assigne chaque $\mathbf{x}_i$ au $\boldsymbol{\mu}_j$ le plus proche.

L'algorithme est itératif et utilise une optimisation de type EM (Expectation-Maximization) :

* Étape d'assignation (Expectation) : Pour chaque point $\mathbf{x}_i$, trouvez l'indice $c_i = \arg\min_j | \mathbf{x}_i - \boldsymbol{\mu}_j |^2$.
* Étape de mise à jour (Maximization) : Pour chaque cluster $j$, recalculez $\boldsymbol{\mu}j = \frac{1}{n_j} \sum{i: c_i = j} \mathbf{x}_i$, où $n_j$ est le nombre de points dans le cluster $j$.

Ces étapes sont répétées jusqu'à convergence (par exemple, quand les centroïdes
bougent de moins qu'un seuil $\epsilon$). Notez que $k$-means peut converger vers
un minimum local (pas toujours global), donc on lance souvent plusieurs
initialisations aléatoires et on choisit la meilleure (celle avec la plus petite
$J$).

{{% /details %}}

Voici une applet interactive pour illustrer le fonctionnement de $k$-means. Notez
que bien qu'on pourrait penser, à priori, qu'il s'agit d'une méthode de
classification, ce n'est pas le cas, car les points à la base n'ont pas
d'étiquettes ! La seule chose que vous décidez (contrôlez) c'est le nombre
d'étiquettes, et l'algorithme s'occupe du reste. Il existe même des algorithmes
qui peuvent faire ce choix pour vous automatiquement.

{{< applet src="/html/applets/kmeans.html" >}}

