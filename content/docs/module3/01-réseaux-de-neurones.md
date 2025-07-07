---
title: "Les réseaux de neurones"
weight: 1
---

# Qu'est-ce qu'un réseau de neurones?

Un réseau de neurones artificiel est un système inspiré du cerveau
humain, composé d'unités appelées *neurones* organisées en couches.
Chaque neurone réalise une opération mathématique simple, et
l'ensemble du réseau transforme des données d'entrée en une prédiction
ou une décision.

## Les données
Les données sont la matière première. Elles peuvent être des images,
du texte, du son ou des tableaux de nombres. Chaque exemple de données
est représenté sous forme numérique, souvent sous forme de vecteurs ou
de matrices. C'est à partir de ces données que le réseau apprend à
reconnaître des motifs.

## La couche de poids
Une couche de poids est un ensemble de connexions entre les neurones.
Chaque connexion possède un *poids*, un nombre qui détermine
l'importance de la donnée transmise. Lorsqu'une entrée passe dans une
couche, elle est multipliée par ces poids. Les poids sont les
paramètres que l'apprentissage va ajuster.

## Les noeuds
Un noeud (ou neurone) reçoit des entrées pondérées et applique une
fonction dite *d'activation* (comme ReLU ou sigmoïde) qui introduit de
la non-linéarité. C'est cette étape qui permet au réseau de modéliser
des relations complexes et non simplement des relations linéaires.

## La fonction d'erreur
La fonction d'erreur (ou fonction de perte) mesure à quel point les
prédictions du réseau s'écartent de la vérité connue (l'étiquette
attendue). Plus l'erreur est grande, plus le modèle est mauvais.
Exemples de fonctions d'erreur : l'erreur quadratique moyenne,
l'entropie croisée.

## Le gradient de la fonction d'erreur
Le gradient indique comment modifier les poids pour réduire l'erreur.
C'est une mesure de la pente locale de la fonction d'erreur par
rapport à chaque poids. Le calcul de ces gradients est essentiel pour
apprendre.

## La backpropagation
La backpropagation est l'algorithme qui calcule efficacement les
gradients pour tous les poids du réseau en partant de la sortie et en
"remontant" couche par couche. C'est grâce à cet algorithme que
l'entraînement des réseaux de neurones est devenu possible à grande
échelle.

## L'inférence
L'inférence correspond à l'utilisation d'un réseau déjà entraîné pour
faire une prédiction sur de nouvelles données. À ce stade, les poids
sont fixés, et le réseau applique simplement ses transformations pour
produire un résultat.

## Quels sont les problèmes avec les réseaux de neurones classiques?
Les premiers réseaux de neurones avaient souvent seulement une ou deux
couches cachées et souffraient de plusieurs limitations :
- Difficulté à capturer des relations complexes.
- Problèmes d'optimisation, comme le gradient qui disparaît quand on
  ajoute trop de couches.
- Manque de puissance de calcul pour entraîner des modèles plus
  profonds sur de gros ensembles de données.
Ces obstacles expliquent pourquoi, malgré leur ancienneté, les réseaux
de neurones profonds n'ont été largement utilisés que récemment.

## La relation entre le feature engineering classique et l'apprentissage profond
Dans l'apprentissage machine classique, il fallait définir
manuellement des *features*, c'est-à-dire des représentations
pertinentes des données. Cela demandait une expertise importante et
beaucoup d'essais. L'apprentissage profond a permis d'apprendre
automatiquement ces représentations hiérarchiques, rendant inutile,
dans de nombreux cas, le feature engineering manuel.

## Réseaux de neurones profonds (plus de couches)
Un réseau profond comporte plusieurs couches cachées (parfois des
dizaines, voire des centaines). Chaque couche apprend une
transformation de plus en plus abstraite des données. Par exemple,
pour une image, les premières couches apprennent à détecter des bords,
puis des formes simples, puis des objets.

## La hiérarchie de la représentation et des concepts
Dans un réseau profond, les couches successives construisent une
hiérarchie de représentations. Cela signifie que le réseau apprend à
recomposer des concepts simples en concepts plus complexes. Cette
hiérarchie est l'une des raisons principales des performances élevées
de l'apprentissage profond.

## Qu'est-ce que la topologie d'un réseau de neurones?
La topologie désigne la manière dont les neurones sont connectés entre
eux. Cela inclut :
- Le nombre de couches.
- Le nombre de neurones par couche.
- Les types de connexions (par exemple convolutionnelles, récurrentes, résiduelles).
La topologie influence fortement les capacités d'un réseau à apprendre.

## Explosition de créativité dans les types de topologies
Au cours des années 2010, on a assisté à une explosion d'innovations :
- Les réseaux convolutifs (CNN) pour l'image.
- Les réseaux récurrents (RNN, LSTM) pour le texte et les séries temporelles.
- Les réseaux résiduels (ResNet) qui permettent d'entraîner des centaines de couches.
- Les architectures de type Transformer pour le langage naturel.
Ces topologies ont permis des progrès spectaculaires dans de nombreux domaines.

## Qu'est-ce qu'un GPU?
Un GPU (processeur graphique) est initialement conçu pour traiter les
images et les graphismes en parallèle. Il peut exécuter des milliers
d'opérations simultanément. Comme l'entraînement d'un réseau de
neurones consiste à faire beaucoup de calculs en parallèle (produits
matriciels), les GPU se sont révélés idéaux pour accélérer
l'apprentissage profond.

## Qu'est-ce qu'un framework de calcul pour l'apprentissage profond?
Les frameworks comme Theano, TensorFlow ou PyTorch sont des
bibliothèques logicielles qui facilitent :
- La définition des réseaux (topologie).
- Le calcul automatique des gradients (différentiation automatique).
- L'exécution efficace sur GPU.
Historiquement, Theano a été l'un des premiers à proposer cette
approche, suivi par TensorFlow (Google) et PyTorch (Facebook). Ces
outils ont permis à la fois la démocratisation et l'accélération des
recherches en apprentissage profond.

## Qu'est-ce qu'une Neural Turing Machine?
Une Neural Turing Machine (NTM) est un modèle avancé qui combine un
réseau de neurones avec un système de mémoire externe que le réseau
peut apprendre à lire et à écrire.

L'idée est inspirée de la notion de machine de Turing, un modèle
théorique de calcul qui dispose d'une mémoire illimitée et qui peut
exécuter n'importe quel algorithme en lisant et en modifiant cette
mémoire.

Les NTMs cherchent à reproduire cette capacité en permettant au réseau
de neurones de manipuler des informations de manière plus flexible et
plus structurée qu'un réseau classique. Concrètement, une NTM comprend
deux grandes parties :
- **Un contrôleur** : généralement un réseau de neurones récurrent qui décide quoi faire.
- **Une mémoire externe** : une sorte de tableau que le contrôleur peut interroger ou modifier via des mécanismes d'attention différentiables.

Grâce à cette combinaison, une NTM peut apprendre des tâches complexes
qui nécessitent de stocker et rappeler des séquences d'informations,
comme copier des chaînes, trier des données ou exécuter des procédures
étape par étape.

Les NTMs sont un exemple de l'évolution des réseaux de neurones vers
des systèmes de plus en plus généraux et puissants, capables de
simuler des formes de calcul proches de celles des ordinateurs
traditionnels, mais en restant entraînables de bout en bout par
gradient.
