---
title: "Classer"
weight: 60
slug: classer
---

# Classer

Le chapitre précédent nous a donné un vrai modèle qui apprend : une droite, deux
paramètres, une erreur à minimiser, une descente vers le creux. Mais il répond
toujours par un **nombre** — un prix. Or quantité de questions n'attendent pas un
nombre, plutôt une **catégorie** : ce courriel est-il un pourriel ? cette tumeur
est-elle bénigne ou maligne ? cette photo montre-t-elle un chat ou un chien ?
C'est la tâche de **classification**, déjà croisée au chapitre kNN — mais cette
fois, nous voulons un modèle qui *s'entraîne*.

Bonne nouvelle, annoncée en fin de chapitre : presque toute la machinerie va
resservir. Des paramètres réglables, une fonction d'erreur, une descente de
gradient pour la minimiser — ce trio est si général qu'il s'adapte aussi bien à
la classification qu'à la régression. Deux choses seulement changent : la
**forme** du modèle et la **façon de compter l'erreur**.

Pour la forme, le glissement est d'une simplicité élégante. En régression, la
droite *suivait* le nuage : elle passait *à travers* les points pour en épouser
la tendance. En classification, la droite *sépare* le nuage : elle passe *entre*
deux groupes pour les départager. Même objet — une droite, deux paramètres —
mais un rôle inversé.

{{< image src="/images/module2/suivre-vs-separer.svg" alt="Deux nuages de points côte à côte. À gauche, une droite traverse le nuage de maisons en suivant sa tendance : c'est la régression. À droite, une droite passe entre un groupe de points bleus et un groupe de points rouges pour les départager : c'est la classification." title="Deux usages de la même droite : à gauche elle suit le nuage (régression), à droite elle le sépare (classification)." loading="lazy" >}}

Pour fixer les idées, abandonnons un instant les maisons et imaginons le cas le
plus simple : des points de deux couleurs, `bleus` et `rouges`, dispersés dans
le plan (deux caractéristiques, $x_1$ et $x_2$). Apprendre à classer, ce sera
trouver la droite qui range le mieux les bleus d'un côté et les rouges de
l'autre. Et il y a, pour y arriver, deux grandes façons de penser — deux
philosophies que nous allons explorer tour à tour.
