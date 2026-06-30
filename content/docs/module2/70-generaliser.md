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
