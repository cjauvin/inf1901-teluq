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

## Linéaire ou non-linéaire : ce qu'un modèle peut dessiner

Revenons un instant sur ce que nous avons construit. La droite de régression du
chapitre 50 : une droite. La frontière de la régression logistique : une droite.
Celle de Bayes naïf : une droite, encore — nous l'avions noté avec surprise. Et
même notre filtre anti-pourriel, sous ses montagnes de mots, prenait *lui aussi*
une décision linéaire. Un air de famille se dessine.

Ces modèles ont tous en commun de tirer leur décision d'une **somme pondérée** des
caractéristiques : chaque attribut pousse d'un côté ou de l'autre,
proportionnellement à son poids, et l'on tranche selon le total. Géométriquement,
cela donne toujours la même chose — une droite (un plan en trois dimensions ; un
*hyperplan* au-delà). On les appelle des **modèles linéaires**.

Est-ce grave ? Autrement dit : y a-t-il des choses qu'**aucune droite** ne peut
apprendre ?

La réponse est oui — et vous connaissez déjà la victime la plus célèbre de cette
limite. Souvenez-vous du **perceptron**, au Module 1 : c'est exactement là-dessus
qu'il s'est brisé, en 1969. L'exemple fatal s'appelle le **XOR** — *l'un ou
l'autre, mais pas les deux* —, la règle du va-et-vient qui commande une lampe au
bout d'un couloir. Placez ses quatre cas dans le plan : les deux « éteint »
tombent sur une diagonale, les deux « allumé » sur l'autre.

{{< image src="/images/module2/xor.svg" alt="Deux panneaux illustrant le XOR. Dans chacun, quatre points aux coins d'un carré : deux bleus sur une diagonale (bas-gauche et haut-droit), deux rouges sur l'autre (haut-gauche et bas-droit). Chaque panneau montre une droite différente traversant le plan pour tenter de séparer les couleurs ; dans les deux cas, un point bleu reste du côté des rouges, cerclé de rouge et marqué d'une croix. Aucune droite ne réussit." title="Le XOR : quelle que soit la droite tracée, un point reste toujours du mauvais côté — la limite même d'un modèle linéaire." loading="lazy" >}}

Essayez. Prenez n'importe quelle droite, inclinez-la comme vous voulez : il
restera toujours un point du mauvais côté. Ce n'est pas un manque d'astuce — c'est
une impossibilité.

Et voici le point crucial, à bien distinguer de tout ce qui précède : **cet échec
n'a rien à voir avec le bruit, ni avec le manque de données**. Donnez à votre
modèle linéaire un million d'exemples parfaits, sans la moindre erreur de mesure :
il échouera exactement pareil. Ce n'est pas un modèle mal réglé, ni un modèle qui
manque d'entraînement. C'est un modèle dont le **répertoire de formes** ne
contient tout simplement pas la réponse. On appelle cela sa **capacité** (ou son
*expressivité*) : l'ensemble des frontières qu'il est seulement capable de
dessiner. Un modèle linéaire n'en connaît qu'une famille — les droites.

À l'inverse, souvenez-vous de kNN. Sa frontière, elle, se contorsionne à volonté,
épouse des îlots, contourne des amas : aucune contrainte de forme ne pèse sur
elle. Le XOR ? Il le règle sans même s'en apercevoir — chaque point regarde ses
voisins, et les voisins d'un coin bleu sont bleus. kNN est un modèle
**non-linéaire**, et c'était donc, sans qu'on le dise, notre premier.

Deux familles, donc, et une question à se poser avant toute autre devant un
problème : *la vérité que je cherche a-t-elle une chance de tenir dans le
répertoire de mon modèle ?* Si elle n'y est pas, aucun réglage, aucune donnée
supplémentaire ne l'y mettra.

Comment franchir le mur, alors ? L'apprentissage automatique classique offre deux
échappatoires. La première, nous venons de la voir : prendre un modèle
non-linéaire, comme kNN. La seconde est plus rusée — **fabriquer soi-même la bonne
caractéristique** : ajoutez aux deux entrées leur produit $x_1 \cdot x_2$, et le
XOR devient, comme par magie, séparable par une droite dans ce nouvel espace. Mais
remarquez le prix : c'est *vous*, l'humain, qui avez dû trouver l'astuce. Et si
personne ne sait quelle caractéristique inventer ?

C'est précisément la question que le Module 3 viendra trancher : les réseaux de
neurones apprendront à **fabriquer eux-mêmes** les caractéristiques qui rendent le
problème séparable, en empilant des couches. Le mur dressé en 1969 tombera en
1986 — c'est la dette que le Module 1 avait laissée ouverte, et c'est là qu'elle
sera payée.

Mais attention : pouvoir se courber n'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelle forme peut aussi épouser… n'importe quoi. C'est tout le
sujet de la section suivante.

## Trop coller, ou trop lisser : le compromis biais-variance

Nous venons de voir qu'un modèle doit être assez *expressif* pour que la vérité
tienne dans son répertoire. Mais l'excès inverse guette aussitôt : un modèle trop
souple finit par épouser le hasard autant que le signal. Pour voir ce compromis à
l'œuvre — et le *mesurer*, maintenant que nous savons le faire —, revenons à notre
vieille connaissance, kNN, dont l'unique réglage, le nombre de voisins $k$, agit
précisément comme un curseur de souplesse. Reprenez l'applet ; cette fois, faites
lentement glisser $k$ d'un bout à l'autre, et observez la frontière.

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

## Paramétrique ou non-paramétrique

Il existe une seconde grande façon de classer les modèles — non plus selon leur
souplesse, mais selon ce qu'il en reste une fois l'entraînement terminé. La
question est simple : le modèle a-t-il **distillé** les données en une poignée de
réglages, ou les **garde-t-il** auprès de lui ?

Repensez à kNN et à son angle mort (page 40) : il n'a, à proprement parler, rien
à apprendre. Pas de paramètres à régler ; pour prédire, il consulte directement
les exemples mémorisés. *Les données sont le modèle.* Conséquence : sa taille
grossit avec le jeu de données — mille exemples, mille exemples à trimballer ;
un million, un million. On dit d'un tel modèle qu'il est **non-paramétrique** :
il ne résume pas les données dans un nombre fixe de réglages, il s'appuie sur
elles, telles quelles, jusqu'au bout.

À l'opposé, notre droite de régression : une fois trouvés sa pente et son
ordonnée, on peut **jeter les données** — il ne reste que deux nombres, $m$ et
$b$, et ils suffisent à prédire. Pareil pour la régression logistique (un poids
par caractéristique) ou pour Bayes naïf (une moyenne et une dispersion par
classe, ou une probabilité par mot). Ces modèles sont **paramétriques** : ils
compressent toute leur connaissance dans un jeu de paramètres de taille *fixée
d'avance*, que l'on ait appris sur cent exemples ou sur cent millions. Vous
reconnaissez là le fil de la page 50 : le modèle bête distillait tout en *un*
nombre, la droite en *deux*, kNN en *aucun*. C'était déjà, sans le dire, l'axe
paramétrique / non-paramétrique.

Chaque famille a son tempérament :

- le modèle **paramétrique** est léger, rapide à la prédiction, et généralise par
  l'effet même de la compression qu'il s'impose — mais il *parie sur une forme*
  (une droite, par exemple). Si la vraie structure des données n'a pas cette
  forme, aucun réglage ne le sauvera : c'est du **biais** ;
- le modèle **non-paramétrique** ne présume presque rien de la forme et peut
  épouser des structures très complexes — mais il est lourd (tout garder), lent à
  prédire, et plus exposé à coller au bruit : c'est de la **variance**.

On retrouve, en filigrane, le compromis de la section précédente. Distiller ou
tout garder, parier sur une forme ou suivre les données : il n'existe pas de
réponse universelle, seulement des choix adaptés au problème — et c'est tout l'art
de la discipline que de les faire avec discernement.

{{< image src="/images/module2/parametrique-vs-non.svg" alt="À gauche, un nuage de points est résumé par une droite réduite à deux réglages m et b : le modèle paramétrique distille les données et peut ensuite les jeter. À droite, les mêmes points sont conservés tels quels : le modèle non-paramétrique garde toutes les données et s'appuie dessus pour prédire." title="Paramétrique : distiller les données en quelques réglages, puis les jeter. Non-paramétrique : garder toutes les données et s'appuyer dessus." loading="lazy" >}}

## Tout cela portait un nom : l'apprentissage supervisé

Prenons un peu de recul. Depuis la première page de ce module, une chose n'a
jamais changé, si discrète qu'on l'a à peine remarquée : **la bonne réponse était
toujours là.** Chaque maison venait avec son prix ; chaque courriel, avec son
étiquette pourriel ou non ; chaque point, avec sa couleur. Le modèle n'avait qu'à
apprendre le chemin de la question vers une réponse *qu'on lui fournissait
d'avance*.

Cette situation porte un nom — que nous pouvons enfin prononcer, maintenant que
nous l'avons vécue de bout en bout : l'**apprentissage supervisé**. « Supervisé »,
comme un élève qu'un professeur corrige, parce qu'il connaît, lui, la réponse
attendue. Régression ou classification, droite ou Bayes, paramétrique ou non :
tout ce que nous avons construit relève de cette grande famille, celle où l'on
apprend à partir d'exemples **étiquetés**.

Mais cette réponse toute prête, d'où vient-elle ? Quelqu'un a dû, quelque part,
étiqueter ces milliers d'exemples un à un — travail souvent long, coûteux,
parfois impossible. Et le monde déborde de données *sans* étiquette : des
millions de photos que personne n'a triées, des historiques d'achats sans
catégories, des textes en vrac. Peut-on apprendre quelque chose de données
brutes, livrées sans la moindre bonne réponse ? Et à l'inverse, quand un robot
apprend à marcher, nul ne lui souffle le « bon » mouvement à chaque instant — il
ne reçoit qu'un encouragement ou une chute, bien plus tard. Est-ce encore de
l'apprentissage ?

Oui — mais d'une autre sorte. Ce qui distingue ces situations, c'est la nature du
**signal** dont le modèle apprend : une réponse donnée, une structure à découvrir
sans guide, ou une récompense différée. C'est cette typologie — et les nouveaux
mondes qu'elle ouvre — que nous explorons au chapitre suivant.
