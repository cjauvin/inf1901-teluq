---
title: "Poser des questions : les arbres de décision"
weight: 65
slug: arbres-de-decision
---

# Poser des questions : les arbres de décision

Tous les modèles rencontrés jusqu'ici raisonnent en nombres. kNN mesure des
distances ; la droite multiplie et additionne ; la régression logistique et
Bayes calculent des probabilités. C'est puissant, mais ce n'est pas ainsi que
*nous* décidons, la plupart du temps. Un médecin devant un patient ne calcule
pas : il pose des questions, l'une après l'autre, et chaque réponse oriente la
suivante. Le jeu des vingt questions fonctionne pareil, et le guide de dépannage
à la fin d'un manuel aussi : « l'appareil s'allume-t-il ? si non, est-il
branché ? ». Une suite de questions à réponse oui ou non, qui se ramifie, et
qui aboutit à une conclusion.

Cette façon de décider a son modèle, et c'est l'un des plus anciens et des plus
intuitifs de l'apprentissage automatique : l'**arbre de décision**. Comme kNN,
il traite aussi bien la régression que la classification, et comme lui il tient
en une idée qu'on peut dessiner. Mais il apporte deux choses qu'aucun modèle du
module n'offrait encore : une frontière qui n'a rien d'une droite, et une
décision qu'on peut *lire*.

## Une question suffit presque

Reprenons la seconde question du module, dans le plan où elle se lit : la
distance du centre en abscisse, l'année de construction en ordonnée, et la
couleur qui dit si la maison est partie vite. Laissons un arbre apprendre sur
ces vingt maisons, avec une seule question permise. Voici ce qu'il trouve :

{{< image src="/images/module2/arbre-maisons.svg" alt="Un arbre à une seule question, « à plus de 11 km du centre ? » : la branche « non » mène à une feuille bleue, 11 maisons sur 12 vendues vite ; la branche « oui » à une feuille rouge, 1 sur 8. Deux erreurs sur vingt, les deux exceptions." title="Un arbre à une question : une racine, deux branches, deux feuilles. Dix-huit maisons sur vingt bien classées." loading="lazy" >}}

« À plus de 11 km du centre ? » Si non, la maison va dans la feuille de
gauche, où 11 maisons sur 12 sont parties vite : l'arbre répond *oui, vendue
vite*. Si oui, elle va dans la feuille de droite, où 1 maison sur 8 seulement
est partie vite : l'arbre répond *non*. Une question, deux feuilles, et 18
maisons sur 20 correctement classées. Les deux qui restent sont nos vieilles
connaissances, les deux exceptions du nuage coloré, chacune du mauvais côté de
la question.

Le vocabulaire est celui d'un arbre, dessiné à l'envers : la première question
est la **racine**, chaque réponse est une **branche**, et les cases du bas, où
l'on ne pose plus de question mais où l'on répond, sont les **feuilles**. Pour
prédire, on part de la racine avec une maison nouvelle, on répond aux
questions, et l'on descend jusqu'à une feuille : sa couleur majoritaire est la
prédiction.

Que dessine cet arbre dans le plan ? Une question sur la distance, c'est une
**coupe verticale** à 11 km : tout ce qui est à gauche est bleu, tout ce qui
est à droite est rouge. Voici sa frontière de décision, avec le même fond
teinté que pour kNN :

{{< image src="/images/module2/arbre-maisons-frontiere.svg" alt="Le plan distance × année des vingt maisons, coupé par une seule ligne verticale pointillée à 11 km : à gauche, le fond est teinté en bleu (vendue vite), à droite en rouge (a traîné). Les deux exceptions se retrouvent chacune du mauvais côté." title="La frontière de l'arbre à une question : une coupe verticale à 11 km, et rien d'autre." loading="lazy" >}}

Comparez-la à [celle de kNN](docs/module2/40-predire-par-ressemblance) sur les
mêmes maisons. Là, une ligne qui serpentait entre les amas ; ici, un trait
droit, parfaitement vertical, parce qu'une question ne regarde qu'*une*
caractéristique à la fois. Et l'arbre, contrairement à kNN, ne garde rien des
vingt maisons : une fois la question trouvée, il peut les oublier. Il est du
côté des modèles qui *distillent*, comme la droite, avec pour tout paramètre un
seuil et deux réponses.

Une chose devrait vous intriguer : l'arbre n'a rien demandé sur l'année de
construction, alors que le nuage coloré semblait dire que les maisons
anciennes traînent. C'est que, sur ces vingt maisons, la distance sépare déjà
presque tout, et l'année n'y ajouterait rien, sauf pour rattraper les deux
exceptions. Laisser l'arbre poser d'autres questions, c'est précisément ce que
nous allons faire ; mais d'abord, comment a-t-il choisi celle-ci ?

## Comment l'arbre choisit ses questions

Il n'y a pas de magie dans le choix de la question, seulement du **comptage**.
Pour chaque caractéristique et chaque seuil possible, l'arbre fait comme si :
il coupe les vingt maisons en deux et regarde, de chaque côté, à quel point les
couleurs sont **mélangées**. Une feuille où toutes les maisons sont de la même
couleur est *pure* ; une feuille où elles sont moitié-moitié est le pire des
cas, puisqu'elle ne renseigne sur rien. La bonne question est celle dont les
deux côtés sont, ensemble, les plus purs possible.

Les seuils candidats ne sont pas infinis : entre deux maisons voisines sur une
caractéristique, toutes les coupes se valent, et il suffit d'essayer celle du
milieu. Vingt maisons, deux caractéristiques, cela fait une quarantaine de
questions à essayer ; un ordinateur les évalue toutes en un clin d'œil, et
garde la meilleure. Sur nos maisons, « à plus de 11 km du centre ? » donne
d'un côté 11 bleues sur 12, de l'autre 7 rouges sur 8 : deux feuilles presque
pures. « Construite après 1995 ? » aurait laissé 2 rouges parmi 11 d'un côté
et 2 bleues parmi 9 de l'autre : plus de mélange, question écartée.

Une surprise, tout de même : « construite après 1989 ? » aurait fait
*exactement* aussi bien que la distance, 11 sur 12 et 1 sur 8, avec les mêmes
deux exceptions. Les deux questions étaient à égalité parfaite, et l'arbre a
pris la première venue. Retenez-le : quand deux caractéristiques disent la
même chose, l'arbre en choisit une et ignore l'autre, sans que cela signifie
que l'autre ne compte pas. Un arbre n'est pas une explication du monde ; c'est
un chemin qui marche.

Une fois la première question posée, on recommence, séparément, dans chacune
des deux feuilles : la meilleure question pour les maisons proches du centre,
la meilleure pour les maisons éloignées, et ainsi de suite, jusqu'à ce que les
feuilles soient pures ou qu'on décide d'arrêter. Chaque question est choisie
sans se soucier des suivantes, ce que les informaticiens appellent une
stratégie *gloutonne* : on prend le meilleur pas immédiat, sans regarder plus
loin. Ce n'est pas garanti optimal ; c'est rapide, et en pratique
remarquablement bon.

Remarquez ce que cet apprentissage n'est *pas*. Le modèle bête moyennait ; la
droite et ses cousines descendaient la pente d'une fonction d'erreur, pas à
pas ; l'arbre, lui, **cherche** : il énumère des questions, les essaie, garde
la meilleure. Pas de paramètres qu'on ajuste en continu, pas de gradient : une
exploration parmi des choix discrets, un peu comme la recherche dans un arbre
de coups du [Module 1](docs/module1/30-chercher-raisonner), ramenée à
l'apprentissage. C'est la troisième façon d'apprendre que rencontre ce module,
et elle a la même ossature que les deux autres : des données, une mesure de ce
qui est bon (la pureté), et une procédure qui la maximise.

{{% hint info %}}
**Sous le capot : mesurer le mélange.** La mesure la plus courante est l'*indice
de Gini* : dans une feuille où une proportion $p$ des maisons est bleue, il
vaut $2p(1-p)$, soit 0 pour une feuille pure et 0,5 pour une feuille
moitié-moitié. Le score d'une question est la moyenne des indices de ses deux
côtés, pondérée par leur taille. Sur nos maisons, l'indice de départ vaut
0,48 ; après la question sur la distance, il tombe à 0,18. Une autre mesure,
l'*entropie*, venue de la théorie de l'information, donne presque toujours le
même arbre.
{{% /hint %}}
