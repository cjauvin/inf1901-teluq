---
title: "Généraliser"
weight: 70
slug: generaliser
---

# Généraliser

Le chapitre précédent s'est clos sur un doute dérangeant. Nous savons désormais
entraîner toutes sortes de modèles — une droite qui prédit un prix, des
classificateurs qui rangent en catégories —, et tous apprennent de la même façon :
en rendant leur erreur la plus petite possible *sur les exemples qu'on leur
montre*. Mais cette réussite-là ne prouve rien. Ce qui compte, ce n'est pas qu'un
modèle excelle sur les données d'hier ; c'est qu'il se débrouille face à celles,
inédites, de demain.

Tout le problème tient dans une distinction : un modèle a-t-il vraiment **appris**
quelque chose des données — une régularité qu'il saura transposer ailleurs — ou
s'est-il contenté de les **retenir** ? Les deux se ressemblent à s'y méprendre
tant qu'on regarde les exemples d'entraînement. C'est seulement devant du neuf
qu'ils se séparent — et que l'on découvre, parfois, que le beau modèle ne valait
rien.

Cette capacité à bien se comporter au-delà des exemples appris porte un nom :
la **généralisation**. C'est elle, et non l'erreur d'entraînement, qui mesure la
vraie valeur d'un modèle. Ce chapitre lui est consacré : comment la mesurer,
pourquoi elle est si difficile à obtenir, et ce qu'elle révèle sur la nature même
des modèles.

## Un modèle se juge sur ce qu'il n'a jamais vu

La solution est presque embarrassante de simplicité : **on cache des exemples au
modèle.** Avant l'entraînement, on met de côté une partie des données — disons un
cinquième. Le modèle apprend sur le reste, sans jamais voir cette réserve. Puis,
une fois entraîné, on l'interroge dessus : ces exemples-là sont neufs *pour lui*,
mais nous, nous connaissons les bonnes réponses. Sa performance sur cette réserve
est une estimation honnête de ce qu'il fera face à du vrai neuf.

{{< image src="/images/module2/jeu-de-test.svg" alt="L'ensemble des données est coupé en deux : un grand bloc « entraînement » sur lequel le modèle apprend, et un petit bloc « test » mis de côté, que le modèle ne voit jamais pendant l'entraînement et qui sert à mesurer sa généralisation." title="On scinde les données : le modèle apprend sur l'ensemble d'entraînement ; l'ensemble de test, gardé sous scellés, sert à juger sa généralisation." loading="lazy" >}}

L'analogie de l'examen tombe juste. Un enseignant qui noterait ses étudiants
uniquement sur les questions distribuées d'avance pour réviser ne mesurerait pas
grand-chose : rien n'empêche d'apprendre ces réponses par cœur sans comprendre.
Pour évaluer la *compréhension*, il faut des questions nouvelles, jamais vues.
C'est exactement ce qu'on fait à un modèle.

On donne des noms à ces deux paquets. L'**ensemble d'entraînement**, sur lequel le
modèle apprend (et où l'on mesure l'**erreur d'entraînement**). Et l'**ensemble de
test**, mis sous scellés jusqu'au bout, qui sert à mesurer l'**erreur de test** —
la seule qui estime la généralisation. La règle d'or : *on ne touche jamais au
jeu de test pendant l'entraînement.* Le jour où le modèle apprend, même
indirectement, sur ses propres données d'examen, le test ne veut plus rien dire.

{{% hint info %}}

Et lorsqu'il faut *régler* quelque chose — la valeur de $k$ pour kNN, ou un autre
hyper-paramètre rencontré à la page 50 —, on ne peut pas non plus se servir du
jeu de test pour choisir, sous peine de le « griller ». On réserve alors un
troisième paquet, l'**ensemble de validation**, dédié à ces réglages ; le jeu de
test, lui, reste vierge pour l'ultime verdict.

{{% /hint %}}

## Trop coller, ou trop lisser : le compromis biais-variance

Maintenant que nous savons *mesurer* la généralisation, regardons-la varier. Le
meilleur terrain d'observation est notre vieille connaissance, kNN — car son
unique réglage, le nombre de voisins $k$, agit précisément comme un curseur de
souplesse. Reprenez l'applet ; cette fois, faites lentement glisser $k$ d'un bout
à l'autre, et observez la frontière.

{{< applet src="/html/applets/knn.html" >}}

À **$k = 1$**, chaque point ne consulte que son unique plus proche voisin : la
frontière se contorsionne pour entourer le moindre exemple, forme des îlots
autour des points isolés, épouse jusqu'au dernier détail. L'erreur
d'entraînement tombe à *zéro* — forcément, chaque exemple est son propre voisin
le plus proche. Mais cette frontière torturée a pris pour argent comptant le
moindre hasard des données : un point un peu aberrant, du bruit, et elle se plie
quand même pour l'accommoder. C'est le **surapprentissage** — notre étudiant qui
a appris le corrigé par cœur, jusqu'aux coquilles, sans rien comprendre. Sur des
données neuves, il trébuche.

À l'autre extrême, **$k$ très grand**, chaque prédiction moyenne tant de voisins
que la frontière se lisse en une courbe placide, presque droite. Si placide,
parfois, qu'elle gomme des structures pourtant bien réelles. C'est le travers
inverse, le **sous-apprentissage** : le modèle est trop rigide pour épouser la
vraie forme des données.

Deux façons d'échouer, donc, et elles portent chacune un nom :

- la **variance**, c'est la sensibilité du modèle au hasard de l'échantillon
  (côté $k$ petit) : changez quelques points d'entraînement, et un modèle à haute
  variance se redessine du tout au tout ;
- le **biais**, c'est sa rigidité de naissance (côté $k$ grand) : son incapacité
  *systématique* à capturer la vraie forme, quels que soient les points qu'on lui
  montre.

Et voici le nœud — l'une des idées les plus profondes du domaine. Quand on rend
un modèle plus souple (ici, en diminuant $k$), son erreur d'entraînement ne fait
que baisser : un modèle flexible colle toujours mieux à ce qu'il a déjà vu. Mais
son erreur de *test*, elle, suit une courbe en **U** : elle baisse d'abord — on
capture enfin les vraies régularités — puis **remonte** dès qu'on se met à épouser
le bruit. Le bon modèle se cache tout au fond du U, à l'équilibre exact entre
biais et variance.

{{< image src="/images/module2/bias-vs-variance-with-errors.png" alt="Deux courbes en fonction de k. L'erreur d'entraînement (rouge) croît régulièrement de k=1 à k=21. L'erreur de test (bleu) a une forme en U : elle décroît, atteint un minimum, puis remonte. Deux droites diagonales figurent la variance (décroissante) et le biais (croissant) ; leur croisement marque le minimum de l'erreur de test." title="L'erreur de test (en bleu) suit une courbe en U : trop de variance à gauche, trop de biais à droite. Le meilleur modèle est au creux." loading="lazy" >}}

Le point crucial : **rien de tout cela n'est propre à kNN.** Chaque modèle possède
son curseur de souplesse — le degré d'un polynôme en régression, la profondeur
d'un arbre de décision, le nombre de paramètres d'un réseau de neurones — et
chacun affronte le même U, le même arbitrage entre coller et lisser. C'est le
**compromis biais-variance**, et savoir le régler est l'un des vrais savoir-faire
de l'apprentissage automatique.

{{% hint info %}}

Une énigme pour plus tard : si trop de souplesse nuit, comment les réseaux de
neurones géants d'aujourd'hui — des centaines de *milliards* de paramètres,
soit une souplesse vertigineuse — parviennent-ils malgré tout à généraliser ?
La réponse, surprenante, bousculera cette jolie courbe en U… au Module 3.

{{% /hint %}}
