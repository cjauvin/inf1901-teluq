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

## Un arbre qui prédit un nombre

Rien, dans ce qui précède, ne tient à ce que la réponse soit une catégorie.
Reprenons la première question du module, le prix, et une seule
caractéristique, la superficie. Un arbre peut la traiter de la même façon :
des questions sur la superficie, et dans chaque feuille, au lieu d'une couleur
majoritaire, le **prix moyen** des maisons qui s'y trouvent. Seule la mesure du
mélange change : plutôt que des couleurs mélangées, on regarde à quel point
les prix d'une feuille sont dispersés autour de leur moyenne, et la bonne
question est celle qui resserre le plus les prix de chaque côté.

Voici l'arbre à deux niveaux appris sur nos vingt maisons. Première
question : « plus de 194 m² ? ». Puis, chez les petites, « plus de
154 m² ? », et chez les grandes, « plus de 237 m² ? ». Quatre feuilles,
quatre prix : 308 000, 430 000, 557 000 et 706 000 \\$.

{{< image src="/images/module2/arbre-prix-escalier.svg" alt="Le nuage des maisons (superficie, prix) avec, en pointillé pâle, la droite ajustée, et en trait plein brun un escalier à quatre marches : l'arbre de régression à deux niveaux de questions coupe la superficie à 194 m², puis à 154 et à 237, et prédit dans chaque intervalle le prix moyen des maisons qui s'y trouvent." title="L'arbre de régression, dessiné sur le nuage : un escalier à quatre paliers, un par feuille. En pointillé, la droite, pour comparer." loading="lazy" >}}

Dessiné sur le nuage, l'arbre est un **escalier** : quatre paliers
horizontaux, un par feuille, avec une marche à chaque seuil. C'est une drôle de
courbe. Elle ne monte pas, elle saute ; entre 154 et 194 m², toutes les
maisons valent 430 000 \\$, qu'elles fassent 155 ou 193 m². Et pourtant, avec
ses quatre paliers, elle colle déjà mieux au nuage que la droite d'[*Un modèle
qui s'entraîne*](docs/module2/50-entrainer-un-modele) : elle se trompe de
32 000 \\$ en moyenne, contre 41 000 pour la droite. Un niveau de plus, huit
paliers, et l'erreur tombe à 23 000 \\$.

Cette comparaison en dit long sur les deux modèles. La droite *parie* sur une
forme, la ligne droite, et ne peut rien faire d'autre ; si les prix suivaient
une courbe, elle la manquerait. L'escalier ne parie sur rien : avec assez de
marches, il épouse n'importe quelle forme. C'est sa force. Mais chaque palier
est calculé sur une poignée de maisons seulement, cinq ici, et c'est aussi sa
faiblesse : la droite lisse ses vingt maisons en deux nombres, l'escalier les
découpe en petits groupes qui ne se parlent plus. Et surtout, l'escalier ne
sait pas *extrapoler* : au-delà de 280 m², il répond 706 000 \\$ pour
toujours, quand la droite, elle, continue de monter. Laquelle a raison hors du
nuage ? Nous verrons, dans [*Bien évaluer un
modèle*](docs/module2/75-bien-evaluer), que la question est mal posée : ni
l'une ni l'autre n'a de garantie là-bas.

Un arbre de régression, donc : les mêmes questions, les mêmes feuilles, et
une moyenne à la place d'un vote. Exactement la bifurcation que kNN nous avait
montrée, à sa toute dernière étape.

## Jusqu'où laisser pousser l'arbre ?

Revenons à la classification et laissons l'arbre poser d'autres questions.
Après « à plus de 11 km du centre ? », il en cherche une dans chaque
feuille, puis dans chaque nouvelle feuille, jusqu'à ce que plus aucune ne
mélange les couleurs. Voici ce qu'il devient sur trois niveaux :

{{< image src="/images/module2/arbre-maisons-profond.svg" alt="L'arbre laissé pousser sur trois niveaux : après « à plus de 11 km du centre ? », il pose des questions sur l'année puis sur la distance jusqu'à isoler chacune des deux exceptions dans une feuille à elle. Six feuilles, chacune annotée du nombre de maisons vendues vite sur le nombre de maisons de la feuille : plus aucune erreur sur les vingt maisons." title="Le même arbre, laissé pousser sur trois niveaux : six feuilles, zéro erreur, et une feuille sur mesure pour chaque exception." loading="lazy" >}}

Six feuilles, et plus une seule erreur. L'arbre a trouvé le moyen de rattraper
les deux exceptions : une question sur l'année, puis une sur la distance, et
voilà la vieille maison partie vite isolée dans une feuille à elle ; deux
questions de plus, et la maison récente qui a traîné a la sienne. Dans le
plan, chaque question ajoute une coupe, et la frontière devient un assemblage
de rectangles :

{{< image src="/images/module2/arbre-maisons-frontiere-profond.svg" alt="Le même plan distance × année, découpé par plusieurs coupes verticales et horizontales en rectangles teintés : l'arbre a isolé chacune des deux exceptions dans un petit rectangle de sa couleur, au prix d'une frontière en escalier." title="La frontière de l'arbre à trois niveaux : des rectangles, dont deux taillés sur mesure autour des exceptions." loading="lazy" >}}

Regardez ces deux petits rectangles taillés sur mesure autour des exceptions.
Vous les avez déjà vus, sous une autre forme : ce sont les îlots que kNN
dessinait avec *k* = 1, dans [*Prédire par
ressemblance*](docs/module2/40-predire-par-ressemblance/#le-choix-de-k). Le
même phénomène, dans un autre modèle. Un arbre laissé libre pousse jusqu'à ce
que chaque feuille soit pure, au besoin en donnant une feuille à chaque
maison : il *colle* aux vingt maisons jusqu'au dernier détail, et prend pour
argent comptant les deux qui n'obéissent pas à la règle. Une maison nouvelle,
vieille et loin du centre, qui tomberait dans le rectangle de l'exception,
serait déclarée « vendue vite » sur la foi d'un seul précédent.

Il y a donc, chez l'arbre comme chez kNN, un curseur à régler : la
**profondeur**, le nombre de questions qu'on l'autorise à poser à la suite.
Trop peu, et l'arbre est grossier ; sur des données où les deux amas
n'auraient pas été si nets, une seule coupe verticale ne suffirait pas. Trop,
et il apprend par cœur. Entre les deux, la bonne profondeur est celle qui
capte les vraies régularités sans épouser les accidents ; et rien, dans les
vingt maisons, ne la désigne. Nous avons rencontré ce dilemme avec *k*, nous le
retrouverons pour tout modèle dans [*Généraliser*](docs/module2/70-generaliser),
où l'arbre servira d'emblème. Retenez pour l'instant les deux façons de tenir
un arbre en laisse : lui interdire de dépasser une profondeur, ou le laisser
pousser puis **l'élaguer**, en coupant après coup les branches qui n'apportent
que du détail.

L'applet ci-dessous vous laisse faire l'expérience. Des points rouges et
bleus, un arbre appris en direct, et son fond dans le plan ; à droite, l'arbre
lui-même, qui se redessine à chaque changement. Faites glisser la profondeur
maximale de 1 à 8 et regardez les rectangles se multiplier autour des points
isolés ; ajoutez un point d'une couleur au milieu de l'autre, et observez ce
que l'arbre invente pour l'accommoder. Survolez une zone du plan : son chemin
s'allume dans l'arbre.

{{< applet src="/html/applets/decision-tree.html" height="605" >}}

## L'arbre du *Titanic*

Quittons nos maisons pour de vraies données, celles que nous croiserons à
propos des fuites dans [*Bien évaluer un modèle*](docs/module2/75-bien-evaluer) :
la liste des 1309 passagers du *Titanic*, avec pour chacun la classe, le sexe,
l'âge, et s'il a survécu. Trente-huit pour cent ont survécu. Le modèle le plus
bête, « tout le monde meurt », obtient donc 62 % de bonnes réponses ;
c'est l'étalon. Laissons un arbre apprendre sur ces passagers, avec deux
niveaux de questions :

{{< image src="/images/module2/arbre-titanic.svg" alt="Un arbre à deux niveaux appris sur les 1309 passagers du Titanic. Première question : une femme ? Pour les hommes, la question suivante est « plus de 9 ans ? » : les garçons (43) ont survécu à 58 %, les hommes adultes (800) à 17 %. Pour les femmes, « en troisième classe ? » : celles de première ou deuxième classe (250) ont survécu à 93 %, celles de troisième (216) à 49 %." title="L'arbre du Titanic, appris sur les vraies données : trois questions, 79 % de bonnes réponses, et une histoire qu'on peut lire." loading="lazy" >}}

La première question que l'arbre trouve, à lui seul, sans qu'on lui souffle
rien : « une femme ? ». Elle vaut, seule, 78 % de bonnes réponses, seize
points de mieux que l'étalon. Puis les deux branches posent des questions
différentes. Chez les hommes : « plus de 9 ans ? » ; les 43 garçons ont
survécu à 58 %, les 800 hommes adultes à 17 %. Chez les femmes : « en
troisième classe ? » ; celles de première et deuxième classe ont survécu à
93 %, celles de troisième à 49 %. Trois questions, et 79 % de bonnes
réponses.

Ce que cet arbre a appris, chacun peut le lire : « les femmes et les enfants
d'abord », la consigne donnée cette nuit-là, avec un correctif que l'histoire
confirme : les femmes de troisième classe, logées dans les entreponts, loin
des canots, ont eu une chance sur deux. L'arbre n'a pas lu de livre
d'histoire ; il a compté, et il retrouve en trois questions ce que les
historiens racontent en chapitres. C'est aussi l'occasion de voir le comptage à
l'œuvre sur un cas ambigu : la feuille des femmes de troisième classe, à
49 %, est presque moitié-moitié, et l'arbre y répond « a péri » à une voix
près. Une profondeur de plus la découperait selon l'âge, sans grand gain :
passé trois questions, le taux de bonnes réponses ne bouge presque plus. Sur
ces données, l'essentiel tient en trois questions, et le reste est du détail.

Un dernier point, sur lequel [*Bien évaluer un
modèle*](docs/module2/75-bien-evaluer) reviendra : ce 79 % a été mesuré sur
les passagers mêmes qui ont servi à apprendre. Sur un jeu de test, il serait
un peu plus bas ; avec un arbre plus profond, l'écart se creuserait.

## Ce qu'un arbre dit, et ce qu'il tait

La grande force de l'arbre, vous l'avez vue sur le *Titanic* : il
**s'explique**. Pour toute prédiction, le chemin de la racine à la feuille est
la justification, lisible en clair : « une femme, en troisième classe, donc
une chance sur deux ». Aucun autre modèle de ce module n'offre cela. La droite
donne une pente, la régression logistique des poids, kNN une liste de
voisins ; rien qu'on puisse raconter à un client, à un patient, à un juge. Dans
les domaines où une décision doit pouvoir être contestée (un prêt refusé, un
diagnostic, un dossier trié), cette lisibilité vaut souvent plus que quelques
points de performance, et c'est l'une des raisons pour lesquelles les arbres,
nés dans les années 1960 et 1980, n'ont jamais quitté la boîte à outils.

Ses faiblesses sont l'envers de sa méthode. D'abord, un arbre est
**instable** : rappelez-vous l'égalité entre la distance et l'année ; retirez
deux maisons, et la première question change, et avec elle tout l'arbre. Deux
jeux de données presque identiques peuvent donner deux arbres sans rapport,
qui prédisent pourtant à peu près la même chose. Ensuite, ses coupes sont
toujours parallèles aux axes : une question ne regarde qu'une
caractéristique. Devant deux amas séparés par une **diagonale**, l'arbre
s'épuise en escalier là où une simple droite, comme celle de la régression
logistique, passerait d'un trait. Un modèle non linéaire, donc, mais d'une
non-linéarité particulière, faite de marches.

La parade à l'instabilité est l'une des idées les plus fécondes de la
discipline, et elle tient en une phrase : si un arbre est fragile, prenez-en
**cent**. On entraîne des centaines d'arbres, chacun sur une variante des
données (un tirage au sort des maisons, un sous-ensemble des
caractéristiques), et l'on fait voter l'ensemble, ou l'on moyenne ses
réponses. Les erreurs de chaque arbre, différentes, se compensent ; la réponse
collective est plus stable et plus juste que celle de n'importe quel arbre
seul. C'est la **forêt aléatoire**, et sa cousine plus ambitieuse, le
*gradient boosting*, qui fait pousser chaque arbre pour corriger les erreurs
des précédents. Sur des données en tableau, comme nos maisons ou les passagers
du *Titanic*, ces forêts restent, encore aujourd'hui, ce qu'il y a de plus
fort, et elles remportent la plupart des compétitions Kaggle dont [*Bien
évaluer un modèle*](docs/module2/75-bien-evaluer) parle. Au prix, il est vrai,
de la lisibilité : cent arbres ne se racontent plus.

## Et sur des données neuves ?

Faisons le point. Nous avons maintenant tout un arsenal : une droite qui
prédit un nombre, deux classificateurs qui prédisent une catégorie, un arbre
qui fait les deux en posant des questions, et deux moteurs pour les
entraîner : minimiser une fonction d'erreur, ou chercher la question la plus
pure. Chacun apprend en collant le mieux possible **aux exemples qu'on lui a
montrés**.

Mais relisons cette dernière phrase. *Aux exemples qu'on lui a montrés.* Or ce
n'est pas du tout ce qui nous intéresse ! Un filtre anti-pourriel qui classe
parfaitement les courriels d'hier (ceux qui ont servi à l'entraîner) ne vaut
rien s'il se trompe sur ceux qui arriveront demain. Depuis la première page de
ce module, le but n'a jamais été de *mémoriser* des exemples, mais d'en tirer
de quoi traiter des cas **encore jamais vus**.

Et là se cache un piège. Un modèle peut très bien réussir un sans-faute sur ses
données d'entraînement *et* s'effondrer sur des données neuves, un peu comme un
étudiant qui aurait appris les réponses du corrigé par cœur sans rien
comprendre au sujet. Nous venons d'en voir l'image la plus nette : l'arbre
laissé pousser jusqu'à isoler chaque exception, qui ne se trompe plus jamais
sur les vingt maisons, et qui n'a rien appris d'elles qu'il ne puisse réciter.
Nous avions déjà croisé l'ombre de ce problème à propos de kNN et de son
réglage de $k$ : trop coller aux exemples peut être une *faiblesse*, pas une
force.

Comment, alors, mesurer si un modèle a vraiment *appris* plutôt que
*retenu* ? Comment déjouer le piège ? C'est toute la question de la
**généralisation**, et le sujet de la page suivante.
