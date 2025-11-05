---
title: "Qu'est-ce qu'un modèle?"
weight: 40
---

# Qu'est-ce qu'on veut dire par modèle?

Le mot "modèle" est polysémique et peut prêter à confusion selon qu’on parle d’apprentissage automatique, de statistiques, de sciences ou de mathématiques pures. Ce chapitre clarifie ces sens et propose un vocabulaire pratique pour les distinguer dans le contexte de ce cours.

## Le sens central en apprentissage automatique

Dans l’AA, un modèle est avant tout une fonction paramétrée qui prend des données en entrée et produit une sortie utile (prédiction, score, probabilité, texte, etc.) :

$$
f_{\boldsymbol{\theta}} : \mathcal{X} \rightarrow \mathcal{Y}
$$

- Données : voir [Que sont les données?]({{< relref "docs/module2/les-données" >}})
- Tâche : voir [Apprentissage supervisé]({{< relref "docs/module2/apprentissage-supervisé" >}}) et [Les paradigmes]({{< relref "docs/module2/les-paradigmes" >}})
- Paramètres : les valeurs numériques internes du modèle (par ex. les pentes et l’ordonnée en régression linéaire, ou les "poids" d’un réseau de neurones)
- Apprentissage : ajuster les paramètres pour minimiser une fonction d’erreur (aussi appelée "perte")

On distingue généralement :

- Architecture : la forme de la fonction (linéaire, arbre de décision, réseau de neurones, transformeur, etc.). C’est la "classe de modèles".
- Paramètres/poids \(\boldsymbol{\theta}\) : les valeurs concrètes qui rendent l’architecture opérationnelle sur une tâche et des données données.
- Modèle entraîné : l’architecture + un jeu spécifique de paramètres appris (souvent sauvegardé sous forme de "checkpoint").
- Hyperparamètres : des réglages extérieurs à l’optimisation (taux d’apprentissage, profondeur de l’arbre, taille du batch, etc.).

{{% hint info %}}
Raccourci de langage courant : on utilise souvent "modèle" pour parler indifféremment de l’architecture ("un modèle de type transformeur") ou d’une instance entraînée ("le modèle que j’ai fine-tuné hier"). Quand un doute subsiste, préciser "architecture" vs "poids/paramètres" aide beaucoup.
{{% /hint %}}

## Modèle au sens statistique

En statistique, un modèle spécifie une famille de distributions de probabilité paramétrée, et la question est d’estimer ces paramètres à partir de données. Deux cadres fréquents en AA :

- Modèles discriminatifs : apprennent \(p(y\mid x)\) ou directement une frontière de décision (ex. régression logistique, SVM).
- Modèles génératifs : apprennent \(p(x)\) ou \(p(x, y)\) pour échantillonner/simuler des données (ex. mélanges gaussiens, autoencodeurs variationnels, modèles de diffusion).

Un "modèle de langage" moderne (LLM) est un modèle génératif sur des séquences de tokens, qui approxime \(p(\text{token}_t \mid \text{contexte})\). Voir [Grands modèles de langage]({{< relref "docs/module4/02-grands-modèles-de-langage" >}}).

## Exemples concrets et repères

- Régression linéaire : architecture linéaire; paramètres = coefficients et biais; sortie = valeur réelle.
- Arbre de décision : architecture arborescente; paramètres = seuils/splits appris; sortie = classe/valeur.
- Réseau de neurones : architecture composée de couches; paramètres = matrices de poids; peut être discriminatif ou génératif. Introduction : [Réseaux de neurones]({{< relref "docs/module3/réseaux-de-neurones" >}}).

Termes utiles :

- Checkpoint : fichier(s) contenant les paramètres entraînés d’un modèle.
- Inférence : utilisation d’un modèle entraîné pour produire des sorties (sans changer ses paramètres).
- Baseline : modèle simple de référence (ex. moyenne, majorité) pour évaluer si un modèle "apprend" vraiment.
- Capacité : richesse de la famille de fonctions (risques : sous-ajustement vs surajustement).

## Autres sens en sciences et en pratique

Au-delà de l’AA, "modèle" peut signifier :

- Modèle scientifique (conceptuel/numérique) : représentation simplifiée d’un phénomène (ex. modèle SIR en épidémiologie, modèles climatiques). On explicite des hypothèses, on simule, on compare aux données.
- Modèle "jouet" (toy model) : version volontairement simplifiée pour comprendre un mécanisme, tester rapidement une idée, enseigner un principe.

Ces sens sont proches de l’AA dès qu’on formalise en équations et qu’on ajuste des paramètres à des observations.

## Sens en mathématiques (logique et théorie des modèles)

En logique mathématique, un "modèle" d’une théorie est une structure dans laquelle tous les axiomes de la théorie sont vrais. Par exemple, les entiers naturels avec addition et multiplication forment un modèle de l’arithmétique de Peano; le plan euclidien usuel est un modèle de la géométrie euclidienne.

- Théorie : ensemble d’axiomes (énoncés formels).
- Modèle : interprétation concrète (structure) qui satisfait ces axiomes.

Ce sens est plus abstrait et ne concerne pas l’apprentissage à partir de données. Il reste utile pour comprendre le mot dans la littérature mathématique.

{{% details "Pourquoi ce détour par la logique?" %}}
Parce que ce sens explique l’intuition générale du mot : un "modèle" est une instanciation qui rend vrai un certain cadre (théorie/architecture). En AA, on "rendra vrai" un ensemble d’exemples via l’ajustement de paramètres; en logique, on rend vrais des axiomes via une structure.
{{% /details %}}

## Lever les ambiguïtés : quelques formulations pratiques

- Préciser "architecture" vs "instance entraînée" : "Nous utilisons l’architecture ResNet; le modèle checkpointé date du 3 juin."
- Nommer les "poids"/"paramètres" séparément : "Même architecture, nouveaux poids fine-tunés."
- Distinguer "hyperparamètres" des "paramètres" : "Nous balayons trois profondeurs d’arbre (hyperparamètres); les seuils sont appris (paramètres)."
- Clarifier "discriminatif" vs "génératif" : "Le modèle produit une probabilité de classe (discriminatif)" vs "Le modèle échantillonne des images (génératif)."

## Où cela s’insère dans le cours

- Les données et leur représentation : [Que sont les données?]({{< relref "docs/module2/les-données" >}})
- Les grandes familles : [Les paradigmes]({{< relref "docs/module2/les-paradigmes" >}})
- L’entraînement supervisé : [Apprentissage supervisé]({{< relref "docs/module2/apprentissage-supervisé" >}})
- Les réseaux et LLMs : [Réseaux de neurones]({{< relref "docs/module3/réseaux-de-neurones" >}}), [Grands modèles de langage]({{< relref "docs/module4/02-grands-modèles-de-langage" >}})

{{% hint info %}}
À retenir : en AA, un "modèle" = une fonction paramétrée; en stats, une famille de distributions paramétrée; en sciences, une représentation d’un phénomène; en logique, une structure qui satisfait des axiomes. Préciser le contexte dissipe 95% des ambiguïtés.
{{% /hint %}}
