---
title: "Module 2 - Apprentissage automatique"
weight: 200
bookCollapseSection: true
---

# Module 2 — Apprentissage automatique

![](/images/machine-learning.webp)

## Qu'est-ce que l'apprentissage automatique ?

L'apprentissage automatique (AA, ou *machine learning*) est un ensemble de
techniques qui permettent à un ordinateur de résoudre des problèmes qu'il serait
très ardu de programmer à la main : reconnaître un chat sur une photo, estimer le
prix d'une maison, filtrer les pourriels, jouer aux échecs, converser…

La différence avec la programmation classique est profonde. Un programme
traditionnel encode une série de **règles** écrites par un humain. Un modèle d'AA,
lui, **dérive son fonctionnement à partir d'exemples** : on ne lui dicte pas la
règle, on la lui fait découvrir dans les données. C'est ce déplacement — des
règles vers les exemples — qui rapproche l'AA de ce qu'on appelle l'intelligence,
et le rattache à des courants comme le connexionnisme.

Vu autrement, les deux démarches **échangent leurs entrées et leurs sorties**. En
programmation classique, un humain écrit les *règles* ; l'ordinateur les applique
aux *données* pour produire des *réponses*. En apprentissage automatique, on
renverse la chose : on fournit à l'ordinateur les *données* **et** les *réponses*
(ce sont nos exemples), et c'est *lui* qui en dégage les *règles* — ce qu'on
appelle alors le **modèle**. Ce qui était fourni par l'humain (les règles) devient
le résultat ; ce qui était le résultat (les réponses) devient une donnée d'entrée.
Le schéma ci-dessous rend cette permutation visible : suivez les « règles » (en
brun) et les « réponses » (en teal) passer d'un côté à l'autre.

{{< image src="/images/module2/regles-vs-exemples.svg" alt="Deux schémas de flux. À gauche, « programmation classique » : on fournit à l'ordinateur les règles et les données, il produit les réponses. À droite, « apprentissage automatique » : on lui fournit les données et les réponses, il produit les règles — le modèle. Les « règles » (en brun) et les « réponses » (en teal) échangent leur place d'un panneau à l'autre." title="Le renversement au cœur de l'apprentissage automatique : ce qu'on fournit et ce que l'ordinateur produit s'inversent. En programmation classique, on écrit les règles ; en AA, c'est l'ordinateur qui les découvre." loading="lazy" >}}

## Une seule grande idée, déclinée

Plutôt qu'un catalogue d'algorithmes, ce module construit **un modèle mental
unique et transférable**, qui revient de page en page :

> partir de **données** → choisir un **modèle** (une fonction réglable par des
> paramètres) → mesurer son **erreur** → régler les paramètres pour la
> **minimiser** → vérifier qu'il **généralise** à des cas nouveaux.

{{< image src="/images/module2/fil-conducteur.svg" alt="Le fil conducteur du module en quatre stations : « données » (un nuage de points), « modèle » (une boîte-fonction « f », avec une flèche d'entrée et de sortie, surmontée de deux sliders figurant des paramètres réglables), « erreur » (une cible dont le tir a manqué le centre, l'écart marqué en rouge), et « généraliser » (un point neuf marqué d'un « ? » face à une frontière). Une boucle de retour relie « erreur » à « modèle », étiquetée : régler les paramètres pour minimiser — et répéter." title="L'épine dorsale du module : données → modèle → erreur → généraliser, avec au cœur la boucle d'entraînement (régler les paramètres pour minimiser l'erreur, encore et encore)." loading="lazy" >}}

Chaque algorithme classique que nous rencontrerons — du plus bête au plus
astucieux — n'est qu'une **variation** sur cette même trame. Une fois cette trame
en main, l'apprentissage automatique cesse d'être une boîte noire.

## Le but ultime : généraliser

La notion la plus profonde de l'AA est cette capacité à **généraliser**. Si
j'entraîne un modèle à distinguer chien et chat avec 1000 images, sa performance
sur ces 1000 images-là ne m'intéresse guère : par construction, il devrait les
reconnaître. Ce qui compte, c'est la **1001ᵉ** image — inédite pour lui. Un modèle
qui a vraiment *appris*, plutôt que *mémorisé*, saura la classer correctement (et
la question devient passionnante si on lui montre… une vache !). Bien généraliser
est le véritable objectif de l'AA — et l'un des sens les plus concrets qu'on
puisse donner au mot « apprendre ».

## Le parcours du module

Nous partirons du **modèle le plus simple imaginable**, puis le perfectionnerons
en butant, chaque fois, sur un obstacle qui appelle l'idée suivante : prédire par
ressemblance, puis un modèle qui *s'entraîne* vraiment (la descente de gradient),
puis classer, puis mesurer la généralisation — pour finir par un panorama des
**trois grandes façons d'apprendre** (supervisé, non supervisé, par renforcement).

![](/images/module2/ai-venn.png)

## Objectifs

* Distinguer clairement programmation traditionnelle et apprentissage automatique ;
* Maîtriser le fil conducteur *données → modèle → erreur → généralisation* ;
* Comprendre, de l'intérieur, quelques algorithmes classiques (baseline, kNN,
  régression, classification, k-means) et l'idée de descente de gradient ;
* Saisir ce que veut dire *généraliser*, et pourquoi c'est le cœur du sujet.

## Durée

Trois semaines, soit environ 27 heures.

## Évaluation

Un travail noté (20 % de la note finale) où vous construirez, pas à pas, un
filtre anti-pourriel par classification bayésienne naïve, avec des questions
d'interprétation sur le fonctionnement de l'algorithme.
