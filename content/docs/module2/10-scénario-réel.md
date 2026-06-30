---
title: "Le problème"
weight: 10
slug: le-probleme
---

# Le problème

Vous regardez votre téléphone, et il se déverrouille. Un courriel arrive et file
droit dans les indésirables, sans que vous ayez rien fait. Sur une chaîne de
montage, une caméra repère, parmi des milliers de téléviseurs presque
identiques, le seul dont l'écran présente un défaut à peine visible. Une
application vous suggère exactement le film que vous aviez envie de voir ce soir.

Ces tâches n'ont rien d'extraordinaire — elles font partie du quotidien. Et
pourtant, elles partagent toutes un trait déroutant : **personne ne sait écrire,
ligne par ligne, les règles qui permettraient de les accomplir.** Comment
décririez-vous, par une suite d'instructions précises, ce qui distingue *votre*
visage de tous les autres ? Ou ce qui fait qu'un courriel « sent » le pourriel ?
Vous le reconnaissez en un instant, mais vous seriez bien en peine de le
*formuler*.

C'est précisément le mur sur lequel butait l'IA classique du [Module
1](docs/module1/60-hivers) : ce savoir trop vaste, trop tacite pour tenir dans
une liste de règles. L'apprentissage automatique commence là où s'arrête cette
stratégie — non plus *dicter* les règles à la machine, mais les lui faire
**découvrir**.

## Pourquoi on ne peut pas simplement le programmer

Pour saisir ce qui change, rappelons ce qu'est un programme informatique
classique — celui qui fait tourner un tableur, un site de réservation ou une
calculatrice. C'est une **suite d'instructions explicites**, écrites une à une
par un programmeur, qui dicte à l'ordinateur quoi faire, étape par étape : *si*
telle condition, *alors* telle action. Tant qu'une tâche se laisse décrire par
des règles claires, cette approche est imbattable.

Le problème, c'est que nos exemples du début refusent de se réduire à des règles
claires. Essayez, pour voir, d'écrire la recette qui reconnaît un chat sur une
photo. « Un chat a deux oreilles pointues » — sauf de dos, ou couché, ou à demi
caché derrière un meuble. « Il a le poil gris » — ou roux, ou noir, ou c'est un
tigré sur un canapé tigré. Chaque règle que vous posez appelle dix exceptions,
et vous n'en voyez jamais le bout.

Ce renversement porte un nom : le **paradoxe de Moravec**. Les tâches que *nous*
trouvons difficiles — jouer aux échecs, extraire une racine carrée — sont
justement les plus faciles à programmer, car elles reposent sur des règles
explicites. À l'inverse, ce qu'un enfant de trois ans fait sans effort —
reconnaître un visage, attraper une balle, comprendre une phrase — résiste
obstinément à la mise en règles, parce que cette compétence est *perceptive* et
largement inconsciente. Nous ne savons pas *comment* nous faisons ; comment, dès
lors, l'écrire ?

<p style="text-align: center;">
    <a href="https://xkcd.com/1425/"><img src="/images/xkcd1425.png" alt="XKCD 1425" style="width: 50%;"></a>
</p>

{{% hint info %}}
Traduction :<br />
&#8208; « Quand un usager prend une photo, l'app devrait vérifier s'il est dans un parc national… »<br />
&#8208; « Facile : un simple appel cartographique. Donne-moi quelques heures. »<br />
&#8208; « … et vérifier si la photo est celle d'un oiseau. »<br />
&#8208; « Là, j'ai besoin d'une équipe de recherche et de cinq ans. »<br />
En informatique, la frontière entre le facile et le presque impossible n'est pas là où l'intuition la place.
{{% /hint %}}

Cette bande dessinée a plus de dix ans, et son exemple a vieilli — identifier un
oiseau dans une photo est devenu facile, *précisément* grâce à l'apprentissage
automatique. Mais son idée de fond reste exacte, et c'est tout ce qui compte
ici : certaines tâches d'apparence anodine sont, pour un programme classique,
d'une difficulté abyssale.

## Changer de stratégie : apprendre à partir d'exemples

Puisque nous ne savons pas *énoncer* les règles, renversons le problème. Plutôt
que de les dicter à la machine, **donnons-lui des exemples** — des cas où la
bonne réponse est déjà connue — et laissons-la trouver d'elle-même la régularité
qui les relie.

L'idée est étonnamment proche de la façon dont un enfant apprend ce qu'est un
chat : non pas en mémorisant une définition, mais en en voyant des dizaines,
jusqu'à ce que « ça fasse chat » sans qu'il sache l'expliquer. On ne lui a jamais
donné la règle ; il l'a *extraite* des exemples.

C'est tout le pari de l'**apprentissage automatique** (*machine learning*) :
fournir à un programme un grand nombre d'exemples, et le munir d'une procédure
qui lui permet d'ajuster son comportement jusqu'à reproduire les bonnes réponses
— puis, on l'espère, de bien répondre sur des cas qu'il n'a jamais vus. C'est
précisément le renversement annoncé à la fin du Module 1 : non plus *chercher*
une solution dans un labyrinthe de règles posées d'avance, mais *apprendre* à en
fabriquer une à partir des données.

Reste à savoir comment, concrètement. Et pour le comprendre sans se perdre, rien
ne vaut un exemple modeste — qu'on pourra suivre d'un bout à l'autre, et triturer
dans tous les sens.

## Notre fil rouge : prédire le prix d'une maison

Tout au long de ce module, nous suivrons un seul et même exemple — volontairement
banal, pour que rien ne nous échappe : **estimer le prix d'une maison**.

Imaginez qu'on vous remette une liste de maisons récemment vendues, chacune
accompagnée de quelques renseignements — sa superficie, son année de
construction, son nombre de chambres — et, surtout, de son **prix de vente** :

| Superficie (m²) | Année | Chambres | Prix |
|---|---|---|---|
| 180 | 1995 | 4 | 420 000 \$ |
| 150 | 1980 | 3 | 350 000 \$ |
| 220 | 2010 | 5 | 580 000 \$ |
| 130 | 1972 | 3 | 310 000 \$ |
| … | … | … | … |

La question est simple à énoncer : **une nouvelle maison se présente, dont on
connaît la superficie, l'année et le nombre de chambres — mais pas le prix. Que
faut-il prédire ?**

Chacun sent bien qu'il y a là une régularité à exploiter : une grande maison
récente vaut généralement plus cher qu'une petite et ancienne. Mais
« généralement » n'est pas une règle — c'est une tendance, noyée dans les
exceptions.

{{< image src="/images/module2/maisons-nuage.svg" alt="Nuage de points reliant la superficie des maisons (axe horizontal) à leur prix de vente (axe vertical) : le prix tend à croître avec la superficie, sans alignement parfait." title="Chaque maison est un point. Le prix monte avec la superficie — mais pas parfaitement." loading="lazy" >}}

En ne gardant que deux colonnes — la superficie et le prix — on peut déjà voir
cette tendance à l'œil nu : les points montent vers la droite, sans pour autant
s'aligner parfaitement. C'est précisément ce genre de savoir flou que nous
voulons faire *émerger des exemples*.

Par où commencer ? Avant de bâtir quoi que ce soit de sophistiqué, posons-nous
une question presque naïve : quelle est la prédiction la plus *bête* qu'on
puisse imaginer — celle en dessous de laquelle il serait absurde de descendre ?
C'est par là, étonnamment, que tout commence.
