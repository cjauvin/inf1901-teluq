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
et le rattache au **connexionnisme**, croisé au [module
1](docs/module1/20-deux-paris) : le pari — rival de l'approche symbolique — que
l'intelligence ne s'écrit pas en règles explicites, mais **émerge d'un réseau de
connexions qui s'ajustent à l'expérience**. L'apprentissage automatique en hérite
l'idée maîtresse, sans nécessairement en garder les neurones : ce qui s'ajuste
ici s'appelle des **paramètres**, et c'est en les réglant sur des exemples que le
modèle finit par « savoir » quelque chose.

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

> partir de **données** → choisir un **modèle** (une fonction de prédiction,
> réglable par des paramètres) → mesurer son **erreur** de prédiction → régler
> les paramètres du modèle pour la **minimiser** → vérifier qu'il **généralise**
> à des cas nouveaux.

{{< image src="/images/module2/fil-conducteur.svg" alt="Le fil conducteur du module en quatre stations, chacune glosée sous son nom. « Données » — les exemples dont on dispose — figurées par un nuage de points. « Modèle » — une fonction de prédiction, réglable par des paramètres — figuré par une boîte-fonction « f », avec une flèche d'entrée et de sortie, surmontée de deux sliders. « Erreur » — à quel point le modèle est bon pour prédire les exemples — figurée par une cible dont le tir a manqué le centre, l'écart marqué en rouge. « Généraliser » — bien prédire des exemples jamais vus — figuré par un point neuf marqué d'un « ? » face à une frontière. Une boucle de retour relie « erreur » à « modèle », étiquetée : régler les paramètres du modèle pour minimiser l'erreur de prédiction — et répéter." title="L'épine dorsale du module : données → modèle → erreur → généraliser, avec au cœur la boucle d'entraînement (régler les paramètres du modèle pour minimiser l'erreur de prédiction, encore et encore)." loading="lazy" >}}

Chaque algorithme classique que nous rencontrerons — du plus bête au plus
astucieux — n'est qu'une **variation** sur cette même trame. Une fois cette trame
en main, l'apprentissage automatique cesse d'être une boîte noire.

## Le but ultime : généraliser

La notion la plus profonde de l'AA, celle qui fait en sorte de l'associer au
domaine de l'intelligence, est cette capacité à **généraliser**. Si j'entraîne
un modèle à distinguer chien et chat avec 1000 images, sa performance sur ces
1000 images-là ne m'intéresse guère : par construction, il devrait les
reconnaître. Après tout, *mémoriser* ces 1000 images est **trivial** pour un
ordinateur — ranger des données et les ressortir à l'identique, c'est exactement
ce qu'une machine fait sans le moindre effort, et il n'y a là aucune trace
d'intelligence. Ce qui compte, c'est la **1001ᵉ** image — inédite pour lui. Un
modèle qui a vraiment *appris*, plutôt que *mémorisé*, saura la classer
correctement (et la question devient passionnante si on lui montre, au lieu d'un
chat ou d'un chien… une vache !). Bien généraliser est le véritable objectif de
l'AA — et l'un des sens les plus concrets qu'on puisse donner au mot
« apprendre ».

{{< image src="/images/module2/memoriser-vs-apprendre.svg" alt="Une image marquée d'un point d'interrogation se présente, et une question la trie : « fait-elle partie des 1000 images déjà vues ? ». À gauche, la branche « oui — elle est dans le lot » : une grille de vignettes dont l'une, en ambre, est justement celle qu'on cherchait ; « elle est là, il suffit de la retrouver ». Verdict : facile, et sans intérêt — une machine range et retrouve sans effort. À droite, la branche « non — elle est inédite » : la même grille, mais l'image se tient à l'écart, séparée par un trait pointillé ; « elle n'est nulle part dans le lot ». Verdict : difficile, et c'est tout l'enjeu — trancher sans l'avoir jamais vue, c'est-à-dire généraliser. En bas : un modèle ne vaut que par ce qu'il fait du second cas." title="Les deux sorts possibles d'une image qui se présente. Si elle figure parmi les 1000 déjà vues, la retrouver est trivial ; si elle est inédite, il faut trancher sans précédent — et c'est là, et seulement là, qu'un modèle se juge." loading="lazy" >}}

## Le parcours du module

Nous partirons du **modèle le plus simple imaginable**, puis le perfectionnerons
en butant, chaque fois, sur un obstacle qui appelle l'idée suivante : prédire par
ressemblance, puis un modèle qui *s'entraîne* vraiment (la descente de gradient),
puis classer, puis mesurer la généralisation — pour finir par un panorama des
**trois grandes façons d'apprendre** (supervisé, non supervisé, par renforcement).

Et pour situer ce module dans l'ensemble : l'apprentissage automatique n'est
qu'une région d'un paysage plus vaste, celui de l'intelligence artificielle — que
le cours parcourt module par module.

{{< image src="/images/module2/ai-venn.svg" alt="Carte en régions imbriquées de l'intelligence artificielle. À l'intérieur de « Intelligence artificielle (IA) » : d'un côté « IA classique » ; de l'autre « Apprentissage automatique (AA) » (machine learning), qui contient « Méthodes d'AA diverses » et « Réseaux de neurones / apprentissage profond », lesquels contiennent à leur tour « IA générative » et « ChatGPT ». Un repère « Module 2 » pointe vers l'ensemble « Apprentissage automatique » et vers les « Méthodes d'AA diverses », qui sont le sujet du module." title="La carte de l'IA : le Module 2 explore l'apprentissage automatique classique — l'ensemble « Apprentissage automatique » et, en son cœur, les méthodes d'AA diverses." loading="lazy" >}}

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
