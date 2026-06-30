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
