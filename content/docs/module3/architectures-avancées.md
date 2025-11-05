---
title: "Architectures avancées"
weight: 20
draft: false
---

# Les architectures neuronales avancées

Une fois que les principes de base des réseaux de neurones sont bien compris, et
que les idées de l'apprentissage profond sont plus claires, les choses
deviennent foisonnantes et très intéressantes avec ce sujet !

Un peu comme on l'a fait avec l'ajout de couches cachées supplémentaires pour un
réseau de neurones, si on prend un moment pour considérer son architecture, il
est relativement facile d'imaginer des variations "topologiques" (des manières
pour ses éléments d'être connectés en un graphe).

L'essor de l'apprentissage profond est venu avec une explosion de créativité à
ce niveau, comme le démontre le fameux [Zoo des réseaux de
neurones](https://www.asimovinstitute.org/neural-network-zoo/) :

![](/images/module3/nn_zoo.png)

Nous allons faire un survol des architectures les plus importantes.

## Les réseaux de neurones convolutifs (CNNs)

Une limitation fondamentale des réseaux de neurones "traditionnels" (aussi
appelés "feedforward") est le fait que leurs neurones sont organisés en rangées
unidimensionnelles. Si les données d'entrée du réseau sont une image, par
exemple, la correspondance entre la structure 2D de l'image et la structure 1D
de la couche d'entrée impose une difficulté supplémentaire au réseau, qui doit
alors "découvrir", par lui-même, le fait que certains pixels sont corrélés entre
eux. Par exemple s'il y a une pelouse dans le coin inférieur gauche de mon
image, les pixels qui se trouvent dans cette zone auront tendance à être verts,
et le fait qu'un pixel particulier de cette zone soit vert "influence", de ce
fait, les pixels voisins.

![](/images/module3/christmas.png)

Les réseaux de neurones à convolution (CNN en anglais, ou ConvNet) sont
particulièrement adéquats pour le traitement des images, parce qu'ils utilisent
des convolutions, qui sont des petits "filtres" 2D (de quelques pixels de
dimension) qui sont "glissés" sur l'image d'entrée, de manière à détecter
efficacement certaines structures, à différentes échelles, dans une image (comme
la boule de Noel bleue dans l'image par exemple, ou un oeil dans un visage). Un
CNN est une collection de convolutions distinctes, dont la tâche est de détecter
différents motifs dans les données, mais leurs paramètres exacts sont appris,
plutôt que déterminés d'avance. Avant l’entraînement, les convolutions sont
aléatoires, et si on entraîne avec un jeu de données qui contient des visages
humains, elles deviendront progressivement spécialisées pour la détection de
caractéristiques anatomiques. Si on entraînait plutôt avec un jeu de données de
véhicules, la spécialisation prendrait une autre direction. Ceci veut donc dire
que l'on ne décide pas d'avance de ce qu'on l'on voudra détecter, le réseau
décidera par lui-même, et cela dépendra évidemment de la nature des images
d’entraînement.

Les CNNs ont des architectures complexes, avec de nombreux détails :

![](/images/module3/cnn.png)

### ImageNet

Les CNNs ont joué un rôle particulièrement important dans l'avènement de
l'apprentissage profond, en grande partie en raison d'un tournant, arrivé en
2012, lors du concours "Large Scale Visual Recognition Challenge" (ILSVRC), avec
la base de données d'images [ImageNet](https://fr.wikipedia.org/wiki/ImageNet).
Ce défi consistait à classer plus d’un million d’images en 1000 catégories
différentes. Cette année-là, l’architecture AlexNet, un CNN profond entraîné sur
GPU, a pulvérisé les performances de toutes les méthodes classiques (SVM, random
forests, etc.), réduisant l’erreur de près de moitié. Ce succès a marqué le
début de la révolution de l'apprentissage profond en vision par ordinateur : les
CNN sont rapidement devenus la méthode dominante pour la reconnaissance
d’images, puis pour de nombreuses autres tâches (détection d’objets,
segmentation, analyse vidéo, etc.). Depuis, des architectures toujours plus
sophistiquées (VGG, ResNet, EfficientNet, etc.) ont pris le relais, mais le
point de bascule historique reste la victoire d’AlexNet sur ImageNet en 2012.

### Avantages et applications

Les CNNs sont plus efficaces que les RDN standards pour les images car ils
partagent les poids (réduisant le nombre de paramètres) et exploitent
l'invariance à la translation (un motif détecté, comme un oeil, n'importe où
dans l'image est reconnu).

Applications courantes : reconnaissance d'objets (ex. : ResNet pour la
classification d'images), détection faciale, ou même dans les voitures autonomes
pour analyser les flux vidéo en temps réel.

## Les réseaux de neurones récurrents (RNNs) et leurs variantes

Tous les types de données d'entrée pour les réseaux de neurones que nous avons
vus jusqu'à présent étaient statiques, fixés dans le temps : une image, un point
dans l'espace, les attributs d'une maison (son prix, ses dimensions, etc).
Est-ce qu'il serait possible de prendre en considération des données
séquentielles, qui s'articulent dans le temps, comme la musique, les mots
(prononcés ou écrits), etc?

Il est tout à fait possible de présenter à un réseau de neurones une série
d'images séquentielles, comme celles d'un film par exemple. Mais le problème est
que chaque image sera traitée de manière indépendante. C'est comme si le réseau
repartait de zéro, à chaque exemple qu'il traite. Il faudrait introduire un
mécanisme pour modéliser un "état" dans lequel se trouve le réseau. Par exemple,
si on lui présente une suite de mots, et que les trois premiers sont `bonjour`,
`comment` et `ça`, il devrait être possible pour le réseau d'avoir un certain
"souvenir" de ceux-ci, quand il traite le prochain mot (probablement le mot
`va`). Les réseaux de neurones dits *récurrents* (RNNs en anglais) introduisent
dans leur architecture des boucles de rétroaction, permettant au réseau de
conserver une "mémoire" des états précédents.

Concrètement, et dans sa version la plus simple, ceci veut dire ajouter une
couche de poids récurrents (ou réentrants) à la couche cachée. Si la couche
cachée a $h$ neurones, ceci introduira donc une matrice de poids (paramètres)
additionnels de $h \times h$ éléments.

![](/images/module3/rnn.png)

Le problème du "gradient qui devient trop petit", dont nous avons discuté dans
une [section précédente]({{< relref
"docs/module3/réseaux-de-neurones/#plus-de-couches-cachées" >}}) est
particulièrement important avec les réseaux récurrents. Si on y pense un peu,
ceci est à prévoir, car si on "déroule" un réseau récurrent, il est clair que ça
correspond à une structure avec plusieurs couches successives, ce qui fait en
sorte d'introduire de l'instabilité numérique au niveau du calcul de gradient
(en gros, parce que les multiplications répétées de nombres très petits
deviennent de plus en plus difficiles, pour un ordinateur digital). Une des
méthodes pour remédier à ce problème est de rendre l'architecture encore plus
complexe, comme c'est le cas par exemple avec un réseau LSTM (Long Short-Term
Memory) :

![](/images/module3/lstm.png)

L'idée du LSTM est d'introduire des "portes" (sortes d'interrupteurs) qui
régissent le flot de l'information, en faisant en sorte que la topologie (les
connexions entre les éléments) devienne dynamique et changeante, au lieu d'être
fixée d'avance. Si une porte est fermée (valeur 0) alors c'est comme si la
connexion correspondante ne se faisait plus. L'état de ces portes n'est pas fixé
d'avance cependant, il est plutôt "appris" par le réseau, c'est-à-dire qu'il est
soumis lui aussi au régime de le rétropropagation, ce qui implique donc que ces
portes doivent avoir leur propre jeu de paramètres qui leur sont propres.

Il est à noter qu'il est possible d'utiliser un réseau récurrent pour créer un
*modèle de langage* (le mécanisme qui se trouve au coeur d'applications comme
ChatGPT, par exemple), mais comme nous allons le voir plus loin, il existe
maintenant un type de réseau de neurones encore plus puissant (les
transformers) qui permettent de faire cela encore plus efficacement.

Applications : prévision de séries temporelles (ex. : bourse), traduction
automatique (ex. : Seq2Seq), ou reconnaissance vocale (ex. : dans les assistants
comme Siri).

## Les autoencodeurs

Un autoencodeur est une idée simple mais intrigante : supposons que nous
connections ensemble deux réseaux de neurones, le deuxième inversé par rapport au
premier, que pourrions nous en tirer?

![](/images/module3/autoencoder.png)

Il faut tout d'abord distinguer les deux parties de ce réseau de neurones particulier,
soit l'encodeur, à gauche, et le décodeur, à droite :

![](/images/module3/enc_dec.png)

Un autoencodeur est un algorithme d'apprentissage dit *auto-supervisé*, car sa tâche
est de tenter de reconstruire l'image d'entrée. Autrement dit, si on donne une
image en entrée à un autoencodeur, et que sa sortie (c-à-d les neurones
complètement à droite) la reproduit parfaitement, alors l'erreur est nulle (ce
que l'on souhaite). Mais quel est donc l'intérêt de faire cela? L'intérêt réside
dans la partie centrale du diagramme, soit la sortie de la couche d'activation
de la couche cachée la plus petite au milieu de l'autoencodeur. Étant donné la
structure du réseau et la fonction de reconstruction qu'il optimise, la couche
centrale contiendra, une fois entraînée, une version correspondante de l'entrée
(qui vit dans un espace à haute dimensionnalité, comme c'est le cas par exemple
d'une image avec ses pixels), projetée dans un espace de plus faible
dimensionnalité, dit *latent*.

![](/images/module3/funnel.png)

Cet espace latent est intéressant pour plusieurs raisons. Il constitue
premièrement une représentation compressée des données d'entrée, et en
considérant le diagramme et le fonctionnement de l'autoencodeur (la tâche de
reconstruction qu'il accomplit), la raison devrait apparaître intuitivement
assez claire : étant donné que le nombre de neurones de la couche latente est,
par design, plus petit que celui des couches d'entrée et de sortie, c'est comme
si on forçait les données dans un goulot d'étranglement (l'encodage), pour les
rendre plus "compactes". Mais étant donné que, de cette représentation réduite,
on *doit* ensuite être capable de reconstruire l'image de sortie le mieux
possible (soit la *décoder*), cela pousse la représentation compacte à préserver
un maximum d'information (car si ce n'était pas le cas, la reconstruction ne
serait tout simplement pas possible). On constate donc que, de par son design et
son architecture, un autoencodeur constitue un mécanisme de compression (et de
reconstruction) des données.

Quand on pense à la compression d'une image, on pourrait imaginer qu'il s'agit
d'un mécanisme similaire à la compression
[JPEG](https://fr.wikipedia.org/wiki/JPEG) par exemple, qui réduit la taille
d'un fichier d'image, tout en la conservant visuellement identique (malgré qu'il
y a une dégradation de la qualité qui peut être perceptible à des degrés variés).

![](/images/module3/jpeg.png)

Les espaces latents sont un sujet très riches et profonds, et ils ont de
nombreux usages en apprentissage automatique. Par exemple, nous verrons que les
transformers, qui sont un type de réseaux de neurones profonds qui servent de
fondements aux grands modèles de langage (comme ChatGPT par exemple), en font
usage. Nous avons déjà brièvement touché ce sujet dans la section sur les
[placements lexicaux]({{< relref
"docs/module2/les-données/#vers-des-représentations-plus-compactes--les-plongements-lexicaux"
>}}) (word embeddings).


![](/images/module3/encoder.png)

<!--
Si on revient à l'exemple de nos données qui seraient des images, il est important de
comprendre que .. zip vs autoenc

TODO: Encodeur vs décodeur

## Les réseaux de neurones sur graphes (GNNs)

Les GNNs, ou *Graph Neural Networks*, traitent des données structurées en graphes, comme les réseaux sociaux ou les molécules.

### Principe de base

Un GNN propage des informations à travers les nœuds et arêtes d'un graphe. Chaque nœud agrège les features de ses voisins via des convolutions graphiques (ex. : Graph Convolutional Networks, GCN). Cela capture les relations structurelles.

Variantes : Graph Attention Networks (GAT) qui ajoutent de l'attention pour pondérer les voisins.

![](/images/module3/gnn.png)

### Avantages et applications

Contrairement aux CNNs (pour grilles) ou RNNs (pour séquences), les GNNs gèrent des structures irrégulières. Applications : recommandation (ex. : Netflix), chimie (prédiction de propriétés moléculaires), ou analyse de réseaux sociaux.

TODO: neural machine
-->