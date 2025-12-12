---
title: "Module 2 - Apprentissage automatique"
weight: 200
bookCollapseSection: true
---

# Module 2 - Apprentissage automatique

![](/images/machine-learning.webp)

##  Qu'est-ce que l'apprentissage automatique?

L'apprentissage automatique (AA) est un ensemble de techniques mathématiques qui
permettent de résoudre des problèmes ardus en informatique, souvent associés à
l'intelligence artificielle (IA) : classifier ou reconnaître des images (est-ce
un chien ou un chat?), estimer la valeur d'une maison, jouer aux échecs,
converser en anglais, résoudre des problèmes généraux, etc.

Ces problèmes sont considérés difficiles car il serait ardu d'écrire un
programme classique pour les résoudre. Un programme classique encode
essentiellement une série de règles et de procédures logiques pour résoudre un
problème, tandis qu'un modèle d'AA dérive plutôt son fonctionnement à partir
d'exemples. Le fait qu'on parle d'intelligence de manière plus explicite dans le
cas d'un modèle d'AA (par rapport à un programme classique) est un peu
arbitraire et culturel, et matière à débat. Il reste que fondamentalement, l'AA
est associé à des courants philosophiques, comme le connexionnisme par exemple,
qui sont généralement associés à l'étude de l'intelligence humaine ou animale.

En général, l'apprentissage automatique utilise des données (qu'on appelle
parfois des exemples) pour "entraîner" un modèle à l'aide d'un algorithme
d'apprentissage. Une fois l'entraînement accompli, on peut utiliser l'algorithme
dans un contexte où c'est utile. Le modèle est dynamique et changeant seulement
dans la phase d'entraînement; dans la phase d'utilisation, il devient un objet
statique, qui ne change généralement pas.

La notion probablement la plus profonde et philosophique de l'AA, et celle qui
fait en sorte qu'on rattache ce domaine à l'IA, est qu'un algorithme
d'apprentissage devrait être en mesure de généraliser : si j'ai entrainé un
modèle à distinguer entre un chien et un chat avec 1000 images d'entraînement,
je ne suis pas intéressé par la performance du modèle sur l'une des images
particulières qui ont servi à l'entraînement (une photo particulière de mon
chien Fido par exemple). Par construction et quasiment par définition, cette
classification particulière devrait être correcte. Je suis plutôt intéressé par
la classification de la 1001ième image, qui n'a *pas* servi à l'entraînement du
modèle, et qui est donc entièrement nouvelle, pour le modèle. Si ce dernier a
été entrainé avec succès, il devrait pouvoir généraliser à n'importe quelle
image (par contre, la question se pose à savoir ce qui devrait arriver si je lui
présente l'image d'une vache!). Une bonne capacité de généralisation est le
but fondamental de l'AA et de l'IA en général, et est reliée à ce qu'on entend
par intelligence, scientifiquement parlant.

## Les objectifs du module

* Comprendre la différence entre la programmation traditionnelle et
  l'apprentissage automatique
* Explorer les différentes manières de représenter les données
* Explorer les fondements de l'apprentissage automatique (machine learning), ainsi
que certains de ses algorithmes classiques

## Durée

Trois semaines ou 27 heures.

## Évaluation

L’évaluation de ce module repose sur un travail noté où vous appliquerez la classification naïve bayésienne pour détecter les pourriels, en répondant à des questions d’interprétation et en expliquant les étapes de l’algorithme.


