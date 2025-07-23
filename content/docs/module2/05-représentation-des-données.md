---
title: "Que sont les données?"
weight: 5
---

# Que sont les données, et comment les représenter?

Il y a une tension fondamentale en informatique entre les différentes manières
de représenter les données, et ce qu'elles peuvent signifier. Quand on ajoute
l'apprentissage automatique, la situation devient encore plus complexe. Tentons
de clarifier le tout.

## Niveau des bits, physiques et mathématiques

Au niveau le plus fondamental, l'ordinateur, physiquement et logiquement, ne
peut traiter qu'un seul type de donnée : le bit, qui est à la fois un concept
mathématique (un symbole dont la valeur ne peut être que 0 ou 1 généralement, ou
*vrai* ou *faux* plus spécifiquement en logique) et physique, au niveau de
l'implémentation, soit en terme électrique (mémoire RAM, CPU, disque SSD), de
magnétisme (disque dur) ou de caractéristiques optiques (CD). Les bits
*représentent* les nombres via la convention de l'encodage binaire.

## Niveau de l'ordinateur et de son langage

Au niveau suivant, on trouve l'ordinateur lui-même, dont le mécanisme central
est le microprocesseur (CPU). Un CPU traite les bits sous leur forme physique,
et il interprète des "paquets" (ou *mots*) de bits de taille déterminée (souvent
32, 64 ou 128 bits) de deux manière fondamentalement différentes :

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
des valeurs (dans la réalité c'est un peu plus complexe que cela, mais l'idée
est semblable, il s'agit de conventions préétablies). Qu'est-ce que le CPU doit
"faire" pour exécuter une instruction particulière? Il s'agit en fait d'un
mini-programme (pour cette instruction particulière) qui est implémenté
directement dans les circuits du CPU. C'est l'endroit où la logique et la
matière se touchent.

## Niveau de la programmation symbolique

Le prochain niveau est implémenté en terme du langage du niveau précédent : tout
comme il est possible d'écrire un jeu, un système d'exploitation ou tout autre
type de programme dans le langage natif du CPU (le langage machine), il est
également possible d'écrire.. un autre langage ! Cet autre langage sera en
général plus *abstrait* (plus éloigné donc de la réalité physique de
l'ordinateur), ce qui permettra au programmeur d'exprimer des idées
computationnelles plus complexes, d'une manière plus naturelle et expressive
(C++, Python ou JavaScript sont des exemples de langage de cette catégorie).
Pour mieux comprendre la notion d'un langage en tant que *programme*, on peut
imaginer qu'il s'agit d'un "ordinateur virtuel", implémenté en terme d'un
langage moins abstrait. Ce langage de "plus haut niveau" (plus abstrait) doit
encore une fois traiter avec des instructions et des valeurs (toujours,
ultimement, représentées en termes de bits), mais cette fois on voit apparaître
des représentations plus complexes, pouvant encoder des structures plus diverses
:

- des nombres entiers
- des nombres réels (beaucoup plus complexe à représenter!)
- des chaînes de caractères (strings)
- des listes de nombres
- des listes de mots
- des listes de listes de mots
- des images
- des sons
- etc!

## Niveau de l'apprentissage automatique et des mathématiques

L'aspect "algorithmique" d'un algorithme d'apprentissage automatique réfère au
fait qu'on effectue en général une procédure, une séquence d'opérations (ou de
transformations) sur des données qui sont essentiellement de nature numérique.
Cette procédure est généralement écrite dans un langage du niveau précédent, par
exemple Python. L'aspect mathématique des algorithmes d'apprentissage
automatique exige des structures des données et des représentations plus
sophistiquées et performante. L'outil conceptuel le plus souvent utilisé pour
les données d'AA est l'espace vectoriel, souvent de très haute dimensionnalité
(bien au-delà des trois dimensions dans lesquelles nous vivons quotidiennement).
Prenons l'exemple de l'image d'une maison. On pourrait imaginer qu'étant donné
qu'il s'agit d'un objet existant dans un espace tridimensionnel, sa
représentation devrait l'être aussi. Si cette maison était un objet dans un jeu
vidéo, sa représentation pourrait être 3D, mais étant donné qu'il s'agit d'une
image, sa représentation se fait dans un espace à dimensionnalité beaucoup plus
élevée : un espace où il y a autant de dimensions que de pixels. S'il agit d'une
image de 1000 X 2000 pixels par exemple, il s'agira donc d'un espace à 6,000,000
dimensions (1000 x 2000 x trois couleurs de base pour chaque pixel : rouge, bleu
et vert). Il s'agit d'un espace absolument énorme, qu'il n'est pas possible de
se représenter visuellement. Un "point" dans cet espace représente une image
entière et particulière, correspondant aux valeurs de sa position relative aux
6,000,000 dimensions. Si on modifie qu'un seul pixel de cette image, il s'agira
d'un autre point, proche, mais tout de même différent du premier. Les images ne
sont utilisées qu'avec certains types d'algorithmes d'apprentissage, mais l'idée
générale de l'espace vectoriel à plusieurs dimensions, pour représenter des
objets ou des concepts, est très importante et répandue.

### Les GPUs

Il serait possible d'implémenter un espace vectoriel entièrement avec les
primitives offertes au niveau précédent (langage de programmation symbolique)
mais il est maintenant établi que l'utilisation de GPUs est plus performante.
Les GPUs sont des puces spéciales qui sont spécialisées dans le calcul numérique
parallèle. Cette technologie a été introduite tout d'abort dans le contexte des
jeux vidéos, pour le calcul 3D, mais a trouvé rapidement un usage dans les
applications numériques d'apprentissage automatique. Les environnements de
programmation spécialisés en AA (PyTorch et TensorFlow en sont de bons exemples)
permettent à un programme écrit dans un langage symbolique (par exemple Python)
de communiquer directement avec ce matériel spécialisé. Le même calcul,
implémenté sur un CPU au lieu d'un GPU, serait beaucoup moins performant.

### Retour vers les symboles

On comprend mieux maintenant la distinction mentionnée souvent entre l'IA au
sens classique, qui manipule des symboles, et l'apprentissage automatique, qui
manipule plutôt des valeurs numériques. Dans un certain sens les deux manipulent
des données qui sont ultimement des valeurs numériques (et même au final des
entités physiques, les bits), mais il y a tout de même un sens clair à
distinguer les deux types de mathématiques sur lesquels sont fondés l'IA
classique et l'AA.

Il se trouve que la distinction peut apparaître moins claire, selon le type
d'algorithme d'apprentissage dont on parle. Avec les grands modèles de langage
(GML), les données de base sont les mots (ou souvent des morceaux de mots, les
"tokens") qui sont au départ des données de nature résolument symbolique (un mot
est un symbole par excellence, après tout). Un GML fonctionne pourtant en fait à
partir d'une représentation vectorielle des mots. Chaque mot est associé à un
vecteur arbitraire dans un espace de grande dimensionnalité (par exemple 512),
et ce sont ces vecteurs qui sont manipulés, transformés et *appris*, à
l'interne, par un GML. Il n'est pas nécessairement clair à priori ce que
représente chaque dimension de cet espace particulier. Mais il se trouve
qu'après la phase d'apprentissage d'un GML, les mots se trouvant près les uns
des autres, dans cet espace, auront tendance à être sémantiquement rapprochés.
Les mots "chien" et "chat" seront donc probablement relativement proches (en
terme de distance euclidienne), dans cet espace à 512 dimensions. Le
fonctionnement du GML fait donc en sorte de reproduire, dans son fonctionnement
et sa représentation interne (c-à-d ses paramètres) son propre système
symbolique, dans un format qui peut être particulièrement opaque pour un
interprète humain.

![](/images/module2/schema_repr_donnees.png)

