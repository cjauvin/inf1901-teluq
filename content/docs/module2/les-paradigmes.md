---
title: "Les paradigmes de l'AA"
weight: 50
---

# Les différents paradigmes de l'apprentissage automatique

Il existe plusieurs manières de catégoriser les algorithmes d'apprentissage
automatique, selon leur nature et la structure des problèmes qu'ils tentent de
résoudre. Nous allons brièvement discuter de trois schémas de classement :

- L'apprentissage *supervisé* versus *non-supervisé*
- L'apprentissage *paramétrique* versus *non-paramétrique*
- L'apprentissage *inductif* versus *transductif*

Nous allons également parler de l'*apprentissage par renforcement*, qui est dans
une classe à part.

## Apprentissage supervisé versus non-supervisé

La distinction la plus connue oppose l’apprentissage supervisé à l’apprentissage non-supervisé.

Apprentissage supervisé : les données d’entraînement sont accompagnées de labels
(la "bonne réponse" est fournie). L’algorithme apprend à prédire ces labels à
partir des caractéristiques des données.

Exemples d’algorithmes :
* Régression linéaire ou logistique
* Machines à vecteurs de support (SVM)
* Réseaux de neurones supervisés (perceptron multicouche, CNN pour l’image, etc.)
* Arbres de décision et forêts aléatoires (Random Forests)

Apprentissage non-supervisé : aucun label n’est fourni. L’algorithme cherche à
découvrir une structure cachée dans les données.

Exemples d’algorithmes :
* k-means (clustering)
* Algorithmes hiérarchiques de regroupement
* Analyse en composantes principales (ACP / PCA) pour la réduction de dimension
* Méthodes de factorisation de matrices (ex. : SVD, NMF)

Cette distinction est fondamentale, car elle reflète le type d’information dont
nous disposons au départ.

## Apprentissage paramétrique versus non-paramétrique

Un deuxième axe de distinction concerne le caractère paramétrique ou
non-paramétrique des modèles.

Modèles paramétriques : ces modèles supposent une forme prédéfinie de la
fonction reliant les données à la sortie.

Exemples d’algorithmes :
* Régression linéaire
* Régression logistique
* Réseaux de neurones “classiques” (avec un nombre de paramètres fixé à l’avance)
* Naïve Bayes (avec hypothèse de distribution gaussienne ou multinomiale)

Modèles non-paramétriques : pas d’hypothèse forte sur la forme de la fonction ;
le nombre de paramètres peut croître avec les données.

Exemples d’algorithmes :
* k-plus proches voisins (k-NN)
* Arbres de décision non contraints
* Méthodes à noyau (SVM avec noyaux non-linéaires)
* Processus gaussiens

On voit que certains algorithmes, comme les SVM, peuvent être considérés
paramétriques ou non-paramétriques selon leur formulation (linéaire vs noyau).

## Apprentissage inductif versus transductif

Une troisième distinction concerne la manière dont un algorithme généralise.

Apprentissage inductif : l’algorithme apprend une règle générale, applicable à
de nouvelles données non vues.

Exemples d’algorithmes :
* Régression linéaire/logistique
* Réseaux de neurones profonds (deep learning)
* Forêts aléatoires
* SVM (dans leur version standard)

Apprentissage transductif : l’algorithme ne cherche pas à apprendre une règle
universelle, mais uniquement à prédire pour les cas particuliers fournis.

Exemples d’algorithmes :
* k-plus proches voisins (k-NN) : il ne construit pas de règle globale, il se contente de comparer aux points connus.
* SVM transductifs (une variante spécifique adaptée aux ensembles de données partiellement étiquetés)

Cette distinction est utile pour comprendre la nature de la généralisation :
universelle (inductive) ou ciblée (transductive).

## L’apprentissage par renforcement

Enfin, il existe un paradigme qui ne s’inscrit pas directement dans les
oppositions précédentes : l’apprentissage par renforcement (Reinforcement
Learning, RL).

Dans ce cadre, un agent apprend en interagissant avec un environnement et en
recevant des récompenses ou des punitions selon ses actions.

Exemples d’algorithmes :
* Q-learning (apprentissage de valeurs d’action)
* Deep Q-Networks (DQN, combinaison de Q-learning et réseaux de neurones)
* Méthodes d’optimisation de politique (Policy Gradient, REINFORCE, PPO)
* Algorithmes acteur-critique (Actor-Critic, A3C)
* RLHF (utilisé avec les grands modèles de langage)

Ces approches sont largement utilisées en robotique, en jeux (ex. : AlphaGo), et
en optimisation de systèmes complexes.

## Conclusion

On peut résumer les distinctions précédentes en s’appuyant sur une analogie avec
la cognition humaine.

Les paradigmes supervisé et non-supervisé relèvent de la reconnaissance de motifs (pattern recognition). Ils sont liés aux fonctions cognitives de la perception. Par exemple :
* Lorsque mes yeux perçoivent une forme que j’ai appris à associer au concept de balle, mon esprit effectue une classification supervisée.
* Inversement, si en me promenant en forêt je remarque une combinaison particulière de formes et de couleurs qui m’intrigue sans que je sache l’identifier, je vis une expérience comparable à un clustering non-supervisé : mon esprit a détecté une structure sans l’avoir reliée à un label précis.

En revanche, l’apprentissage par renforcement (APR) s’inscrit dans une autre
dimension cognitive : il concerne moins la perception que le comportement. Il
s’agit de déterminer quelle action poser dans un contexte donné, en fonction de
ses conséquences futures. C’est ce qui en fait un paradigme privilégié pour
modéliser la prise de décision, notamment dans les domaines des jeux ou de la
robotique, où un agent apprend en explorant, en essayant, et en ajustant ses
actions selon les récompenses ou les punitions reçues.

Ainsi, si l’on voulait simplifier au maximum :
* Les apprentissages supervisés et non-supervisés s’apparentent à voir et reconnaître.
* L’apprentissage par renforcement s’apparente plutôt à agir et apprendre de ses actions.

Cette distinction illustre bien que les paradigmes de l’apprentissage
automatique ne décrivent pas seulement des techniques, mais aussi des modèles
différents de l’intelligence elle-même.

