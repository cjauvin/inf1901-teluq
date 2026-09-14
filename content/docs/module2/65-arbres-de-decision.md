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
