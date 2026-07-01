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

## Une seule grande idée, déclinée

Plutôt qu'un catalogue d'algorithmes, ce module construit **un modèle mental
unique et transférable**, qui revient de page en page :

> partir de **données** → choisir un **modèle** (une fonction réglable par des
> paramètres) → mesurer son **erreur** → régler les paramètres pour la
> **minimiser** → vérifier qu'il **généralise** à des cas nouveaux.

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
