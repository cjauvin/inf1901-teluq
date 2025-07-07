---
title: "Représentation des données"
weight: 5
---

# Comment représenter les données?

Un problème crucial qui se pose en AA est comment adéquatement
représenter les données, pour qu'elles soient traitables et
compréhensibles à la fois par l'ordinateur ainsi que le modèle (ou
algorithme) d'apprentissage qu'on veut utiliser. Il existe de
nombreuses manières de faire cela, mais un thème récurrent est
l'utilisation d'espaces vectoriels pour représenter les données, ce
qui est très étroitement relié au fait que la plupart des techniques
d'AA touchent de près ou de loin l'algèbre linéaire. Une image, par
exemple, sera un point dans un espace vectoriel à très haute dimension
(autant de dimensions qu'il y a de pixels!), et un mot pourrait être
un point dans un espace vectoriel extrêmement épars ("sparse") pour
représenter la présence ou l'absence d'un mot. Il est également
possible de représenter le sens des mots à l'aide d'un espace
vectoriel, dont les grands modèles de langage (GML) font usage, comme
nous le verrons au module 4.

On parle souvent de "caractéristiques" ("features" en anglais) en AA,
qui sont les valeurs souvent numériques, mais pas toujours, qui
décrivent les instances (donc des "objets") que l'on tente de traiter.
Classiquement, on fait de "l'ingénierie de caractéristiques" sur les
données, pour tenter de les transformer de manière à améliorer les
performances d'un algorithme. Le AA très moderne qui utilise les
réseaux de neurones profonds tend à faire en sorte qu'on a moins
besoin de ce genre de techniques, car les transformations sont faites
automatiquement, par le réseau de neurones lui-même, comme nous le
verrons au module 3.

