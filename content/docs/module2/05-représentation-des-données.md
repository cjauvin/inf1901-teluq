---
title: "Que sont les données?"
weight: 5
---

# Que sont les données, et comment les représenter?

Il y a une tension fondamentale en informatique entre les différentes manières
de représenter les données, et ce qu'elles veulent signifier. Quand on ajoute
l'apprentissage automatique, la situation devient encore plus complexe. Tentons
de clarifier le tout.

## Niveau des bits, physiques et mathématiques

Au niveau le plus fondamental, l'ordinateur, physiquement et logiquement, ne
peut traiter qu'un seul type de donnée : le bit, qui est à la fois un concept
mathématique (un symbole dont la valeur ne peut être que 0 ou 1 généralement, ou
*vrai* ou *faux* plus spécifiquement en logique) et physique, au niveau de
l'implémentation, soit en terme électrique (mémoire RAM, CPU, disque SSD), de
magnétisme (disque dur) ou de caractéristiques optiques (CD).

## Niveau de l'ordinateur et de son langage

Au niveau suivant, on trouve l'ordinateur lui-même, dont le mécanisme central
est le microprocesseur (CPU). Un CPU traite les bits sous leur forme physique,
et il interprète des "paquets" de bits de taille déterminée (souvent 32, 64 ou
128 bits) de deux manière fondamentalement différentes :

1. En tant que *nombre* (ou plus généralement *valeur*)
2. En tant qu'*instruction*

Le flot de bits auquel est exposé le CPU (soit via sa mémoire physique, ou via
un autre médium physique comme un disque) constitue un *programme*, et le CPU
*exécute* ce programme, de manière séquentielle. Un programme en "langage
machine" (le langage du CPU) pourrait être par exemple :

```
MOV 1000
ADD 0001
STR 2000
```

Les symboles `MOV`, `ADD` et `STR` sont des instructions, qui correspondent en fait
elles-mêmes à des nombres (donc des séries de bits). La signification de ce programme
pourrait être la suivante :

```
- Prendre la valeur à l'adresse mémoire 1000 et la mettre dans un registre spécial
- Ajouter 1 à cette valeur dans le registre
- Prendre le contenu du registre et l'enregistrer à l'adresse mémoire 2000
```

Comment le CPU peut-il distinguer entre les instructions et les valeurs? Une
manière simple serait de simplement respecter la convention selon laquelle les
"paquets de bits" (de taille fixe) aux positions paires (dans la séquence du
programme) sont des instructions, tandis que ceux aux positions impaires sont
des valeurs (dans la réalité c'est un peu plux complexe que cela, mais l'idée
est semblable, il s'agit de conventions préétablies).

# Niveau de la programmation symbolique

Le prochain niveau est implémenté en terme du langage du niveau précédent : tout
comme il est possible d'écrire un jeu, ou un système d'exploitation dans le
langage brut du CPU (langage machine) il est également possible d'écrire.. un
autre langage ! Cet autre langage sera en général plus *abstrait* (plus éloigné
donc de la réalité physique de l'ordinateur), ce qui permettra au programmeur
d'exprimer des idées computationnelles plus complexes, d'une manière plus
naturelle et expressive.

---------------------

Un problème crucial qui se pose en AA est comment adéquatement représenter les
données, pour qu'elles soient traitables et compréhensibles à la fois par
l'ordinateur ainsi que le modèle (ou algorithme) d'apprentissage qu'on veut
utiliser. Il existe de nombreuses manières de faire cela, mais un thème
récurrent est l'utilisation d'espaces vectoriels pour représenter les données,
ce qui est très étroitement relié au fait que la plupart des techniques d'AA
touchent de près ou de loin l'algèbre linéaire. Une image, par exemple, sera un
point dans un espace vectoriel à très haute dimension (autant de dimensions
qu'il y a de pixels!), et un mot pourrait être un point dans un espace vectoriel
extrêmement épars ("sparse") pour représenter la présence ou l'absence d'un mot.
Il est également possible de représenter le sens des mots à l'aide d'un espace
vectoriel, dont les grands modèles de langage (GML) font usage, comme nous le
verrons au module 4.

TODO
* Idée d'un objet en tant que "point dans un espace"
* notion de manifold

On parle souvent de "caractéristiques" ("features" en anglais) en AA, qui sont
les valeurs souvent numériques, mais pas toujours, qui décrivent les instances
(donc des "objets") que l'on tente de traiter. Classiquement, on fait de
"l'ingénierie de caractéristiques" sur les données, pour tenter de les
transformer de manière à améliorer les ppperformances d'un algorithme. Le AA
très moderne qui utilise les réseaux de neurones profonds tend à faire en sorte
qu'on a moins besoin de ce genre de techniques, car les transformations sont
faites automatiquement, par le réseau de neurones lui-même, comme nous le
verrons au module 3.

