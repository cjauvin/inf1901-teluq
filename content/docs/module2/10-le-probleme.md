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

## Notre fil rouge : des maisons à vendre

{{< image src="/images/module2/maison-a-vendre.jpg" alt="Une pancarte « FOR SALE » plantée sur la pelouse d'une maison résidentielle, devant un jardin fleuri et l'entrée du garage." title="Combien vaut cette maison ? Et partira-t-elle vite ? Deux questions que ce module va apprendre à une machine." loading="lazy" >}}

<p class="image-credit">Photo : Kindel Media, <a href="https://www.pexels.com/photo/for-sale-sign-on-green-grass-lawn-7578849/">Pexels</a>.</p>

Tout au long de ce module, nous suivrons un seul et même exemple — volontairement
banal, pour que rien ne nous échappe : **un registre de ventes immobilières**. Un
même jeu de données, donc, auquel nous poserons plus d'une question.

Imaginez qu'on vous remette une liste de maisons récemment vendues, chacune
accompagnée de quelques renseignements — sa superficie, son année de
construction, son nombre de chambres — et, surtout, de son **prix de vente** :

| Superficie (m²) | Année | Chambres | Prix |
|---|---|---|---|
| 180 | 1995 | 4 | 420 000 \\$ |
| 150 | 1980 | 3 | 350 000 \\$ |
| 220 | 2010 | 5 | 580 000 \\$ |
| 130 | 1972 | 3 | 310 000 \\$ |
| … | … | … | … |

La première question est la plus naturelle qui soit — **combien vaut une
maison ?** — et elle est simple à énoncer : *une nouvelle maison se présente,
dont on connaît la superficie, l'année et le nombre de chambres, mais pas le
prix. Que faut-il prédire ?*

Chacun sent bien qu'il y a là une régularité à exploiter : une grande maison
récente vaut généralement plus cher qu'une petite et ancienne. Mais
« généralement » n'est pas une règle — c'est une tendance, noyée dans les
exceptions.

{{< image src="/images/module2/maisons-nuage.svg" alt="Nuage de points reliant la superficie des maisons (axe horizontal) à leur prix de vente (axe vertical) : le prix tend à croître avec la superficie, sans alignement parfait." title="Chaque maison est un point. Le prix monte avec la superficie — mais pas parfaitement." loading="lazy" >}}

En ne gardant que deux colonnes — la superficie et le prix — on peut déjà voir
cette tendance à l'œil nu : les points montent vers la droite, sans pour autant
s'aligner parfaitement. C'est précisément ce genre de savoir flou que nous
voulons faire *émerger des exemples*.

## Une seconde question, d'une tout autre nature

Avant d'aller plus loin, remarquons quelque chose. Un agent immobilier ne se pose
pas *une* question sur une maison, mais au moins deux. La première, on vient de
la voir : **combien vaut-elle ?** La seconde est tout aussi pratique :
**va-t-elle partir vite ?** Nos registres de ventes le savent, eux aussi — il
suffit d'y regarder deux colonnes de plus. La réponse, bien sûr ; mais aussi un
renseignement qui ne nous avait servi à rien jusqu'ici, et qui va se révéler
décisif : à quelle **distance du centre-ville** se trouve la maison.

| Superficie (m²) | Année | Chambres | Distance du centre (km) | Prix | Vendue en moins de 30 jours ? |
|---|---|---|---|---|---|
| 180 | 1995 | 4 | 8 | 420 000 \\$ | oui |
| 150 | 1980 | 3 | 21 | 350 000 \\$ | non |
| 220 | 2010 | 5 | 9 | 580 000 \\$ | oui |
| 130 | 1972 | 3 | 16 | 310 000 \\$ | non |
| … | … | … | … | … | … |

Les deux questions portent sur les **mêmes maisons**, décrites par les **mêmes
renseignements**. Et pourtant les réponses attendues n'ont rien à voir : d'un
côté un **nombre** — 420 000 \\$, 385 200 \\$, n'importe quelle valeur sur une
échelle continue ; de l'autre un **choix entre deux réponses possibles**, oui ou
non. On ne peut pas faire la « moyenne » de *oui* et de *non*.

Cette différence n'est pas cosmétique : elle change jusqu'au sens du mot **se
tromper**. Prédire 405 000 \\$ pour une maison vendue 420 000 \\$, c'est se
tromper — mais de peu, et on sait exactement de combien : 15 000 \\$. Répondre
*oui* pour une maison qui a traîné, en revanche, c'est se tromper, point. Il n'y
a pas de « presque oui », pas de demi-erreur, aucune distance entre les deux
réponses possibles. D'un côté un écart qu'on peut mesurer ; de l'autre, une
réponse juste ou fausse. Nous verrons que cette asymétrie se propage à tout le
reste : à la manière de deviner bêtement, à la manière de mesurer l'erreur, et
jusqu'à la forme du modèle.

Remarquez au passage un détail qui a son importance : pour cette seconde
question, le **prix devient un renseignement comme un autre** — une colonne parmi
les autres, au même titre que l'année de construction ou la distance du centre.
Ce qui était la *réponse* à trouver dans le premier cas devient une *donnée de
départ* dans le second. La table, elle, n'a pas bougé : c'est la **question qu'on
lui pose** qui change.

On peut d'ailleurs *voir* ce changement — à condition de regarder au bon endroit.
Laissons de côté la superficie et le prix, et dessinons nos maisons dans un tout
autre plan : la **distance du centre** en abscisse, l'**année de construction**
en ordonnée. Puis colorons chacune selon la réponse à notre nouvelle question :

{{< image src="/images/module2/maisons-vendues.svg" alt="Les mêmes maisons, dans un tout autre plan : la distance du centre-ville en abscisse, l'année de construction en ordonnée. Chaque point est coloré selon qu'il s'est vendu en moins de 30 jours (en bleu) ou qu'il a traîné (en rouge). Les points forment deux amas compacts, logés dans des coins opposés du dessin et séparés par un large vide : en haut à gauche, en bleu, les maisons proches du centre et récentes ; en bas à droite, en rouge, les maisons éloignées et anciennes. Deux points traversent ce vide — une vieille maison éloignée partie vite, une récente et proche qui a traîné." title="Les mêmes maisons, une autre question — et un autre plan. Ce n'est plus la hauteur du point qu'on cherche à deviner, mais sa couleur." loading="lazy" >}}

Le contraste avec le premier dessin saute aux yeux. Là, ce qu'on cherchait à
deviner était la **hauteur** du point — sa position sur une échelle continue.
Ici, les deux coordonnées sont *données* : ce qu'on cherche, c'est la
**couleur**. Et le motif saute aux yeux — les points se rassemblent en **deux
amas** logés dans des coins opposés, avec un large vide entre eux. Proche du
centre et récente : la maison part vite. Éloignée et ancienne : elle traîne.
Deux exceptions seulement traversent ce vide.

Pourquoi avoir changé de plan, au fait ? Parce que dans le dessin précédent — la
superficie et le prix — les deux couleurs se seraient mêlées sans rien laisser
voir. Le motif était bien là, dans le registre, mais pas dans ces
renseignements-là. Retenez ce détail : il annonce une leçon qui reviendra tout au
long du module. La difficulté d'un problème tient souvent moins à la machinerie
qu'on lui oppose qu'au choix de **ce qu'on décide de regarder**.

Un mot sur cette couleur, justement. Elle règle un problème d'encombrement : nous
avons désormais **trois** renseignements à faire tenir sur une page plate — la
distance, l'année, et la réponse. Les deux premiers occupent les axes ; pour le
troisième, il ne reste plus de place, alors on l'encode autrement. Ce n'est là
qu'une commodité de dessin, et nous verrons bientôt qu'on peut faire mieux.

Dans les **prochains chapitres**, c'est surtout la première question que nous
suivrons — le prix se prête mieux aux dessins et aux premières explications. Mais
la seconde n'attendra pas longtemps : elle finira par occuper le devant de la
scène, avec un chapitre pour elle seule — et c'est même une question de ce type,
*ce courriel est-il un pourriel ?*, qui vous occupera au travail noté. Nous
verrons alors que presque tout ce qu'on aura appris sur l'une vaut aussi pour
l'autre. C'est d'ailleurs à cette seconde famille qu'appartiennent **plusieurs**
des exemples du début de ce chapitre — reconnaître un chat, repérer un pourriel :
autant de questions dont la réponse n'est pas un nombre, mais **une catégorie**.

Et rien n'oblige une catégorie à n'avoir que deux valeurs. *Quel animal est sur
cette photo — un chat, un chien, un cheval ?* *Quel chiffre est écrit sur cette
enveloppe ?* — dix réponses possibles. *Dans quelle langue ce message est-il
rédigé ?* Ce qui compte n'est pas le *nombre* de réponses, mais leur **nature** :
une liste de possibilités distinctes, qu'on ne peut ni moyenner ni ranger sur une
échelle. Entre *chat* et *chien*, il n'y a rien — pas plus qu'entre *oui* et
*non*. La question que posent nos registres, avec ses deux réponses, n'est que le
cas le plus simple de cette famille.

Par où commencer ? Avant de bâtir quoi que ce soit de sophistiqué, posons-nous
une question presque naïve : quelle est la prédiction la plus *bête* qu'on
puisse imaginer — celle en dessous de laquelle il serait absurde de descendre ?
C'est par là, étonnamment, que tout commence.
