---
title: "Les paradigmes de l'AA"
weight: 50
---

# Les différents paradigmes de l'apprentissage automatique

Il existe plusieurs manières de catégoriser les algorithmes d'apprentissage
automatique, selon leur nature et la structure des problèmes qu'ils tentent de
résoudre. Nous allons considérer deux schémas de classement fondamentaux :

- L'apprentissage supervisé versus non-supervisé
- L'apprentissage paramétrique versus non-paramétrique

## Apprentissage non-supervisé

Nous avons vu qu'une caractéristique essentielle de l'apprentissage
supervisé est que la "bonne réponse" (qu'il s'agisse du prix réel
d'une maison, ou la variable binaire oui/non correspondant au fait
qu'un étudiant ait échoué ou non) est fournie avec les données
d’entraînement. Un algorithme d'apprentissage supervisé (nous avons vu
qu'il y en avait plusieurs) utilise cette "bonne réponse" comme une
cible cruciale qu'il doit s'efforcer d'atteindre, de modéliser donc.
En contraste, un algorithme non-supervisé n'a pas cette "bonne
réponse", il n'a que des données non-étiquetées. Les algorithmes de
cette famille ont donc une tâche entièrement différente que celle de
l'apprentissage supervisé. Il doivent découvrir la structure inhérente
aux données, de manière autonome, tout en étant guidé possible par des
hypothèses. Par exemple, si les données sont des mesures décrivant un
ensemble de fleurs de différentes espèces, il est possible que je
sache à priori combien d'espèces l'ensemble d’entraînement contient.
Dans ce cas, supposons que je sache qu'il y a trois espèces, alors
l'algorithme n'aura qu'à découvrir ces trois groupes, et associer
chaque exemple à un groupe en particulier. Il pourrait être également
possible que le nombre d'espèces soit à priori inconnu, ce qui rendrait
la tâche de l'algorithme de classification encore plus difficile.

### Partitionnement (clustering)

Avec un algorithme de partitionnement, on peut découvrir des
"agrégats", ou des groupes naturels dans les données.

- k-Means
- DBScan
- Hierarchical clustering
*** Réduction de la dimensionnalité
En tentant de réduire la dimensionnalité des données, on peut
découvrir sa structure inhérente, ce qui est souvent utile en
visualisation (par exemple, une donnée exprimée en très haute
dimension peut être plus facile à comprendre ou visualiser en 2d ou
3d).

- PCA

## Apprentissage paramétrique versus non-paramétrique

Il existe une autre manière, complètement différente, de classifier les
algorithmes d'apprentissage : si l'algorithme est implémenté à l'aide d'une
fonction mathématique essentiellement définie par des paramètres, qui sont
indépendants des données qui seront traitées par l'algorithme, on parle
d'apprentissage paramétrique. Avec l'apprentissage non-paramétrique, en
contraste, la fonction de décision est définie à partir des données
d'entraînement. Les données elles-mêmes constituent l'algorithme.

Exemples d'algorithmes paramétriques :

- Régression linéaire (apprentissage supervisé)
- Régression logistique (supervisé)
- Réseau de neurones

Exemples d'algorithmes non-paramétriques :

- Arbres de décision
- k-NN

Pour certains algorithmes, la frontière entre ces deux classes est un peu plus
floue.

## Apprentissage inductif versus transductif

TODO

## Apprentissage par renforcement (RL)

L'apprentissage par renforcement (APR) est un autre paradigme
d'apprentissage automatique, très différent des précédents dont nous avons
parlés. On peut généraliser les apprentissages supervisé et
non-supervisé en considérant qu'ils sont une forme de "reconnaissance
de motifs" (en anglais "pattern recognition"). Les mécanismes de ce
genre sont souvent associés aux fonctions cognitives de la perception,
chez les humains. Par exemple, mes yeux perçoivent une information
visuelle qu'on m'a appris à classifier en tant que "balle", alors
quand je vois une balle, la classification appropriée est effectuée
par mon esprit (exemple d'apprentissage supervisé). D'une manière
apparentée mais un peu différente, il se peut que mes yeux détectent,
lors d'une promenade en forêt, une forme ou des couleurs
particulières, que je ne parviens pas à identifier, mais qui vont tout
de même attirer mon attention (exemple d'apprentissage non-supervisé).
En contraste de cette reconnaissance de motifs, l'apprentissage par
renforcement est plutôt une modélisation du comportement, plutôt que
de la perception (quelle action devrait être posée dans ce contexte
particulier). L'APR est souvent utilisé dans les jeux et la robotique.
