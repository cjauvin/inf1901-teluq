---
title: "Généraliser"
weight: 70
slug: generaliser
---

# Généraliser

Le chapitre précédent s'est clos sur un doute dérangeant. Nous savons désormais
entraîner toutes sortes de modèles (une droite qui prédit un prix, des
classificateurs qui rangent en catégories), et tous apprennent de la même façon :
en rendant leur erreur la plus petite possible *sur les exemples qu'on leur
montre*. Mais cette réussite-là ne prouve rien. Ce qui compte, ce n'est pas qu'un
modèle excelle sur les données d'hier ; c'est qu'il se débrouille face à celles,
inédites, de demain.

Tout le problème tient dans une distinction : un modèle a-t-il vraiment **appris**
quelque chose des données (une régularité qu'il saura transposer ailleurs) ou
s'est-il contenté de les **retenir** ? Les deux se ressemblent à s'y méprendre
tant qu'on regarde les exemples d'entraînement. C'est seulement devant du neuf
qu'ils se séparent, et que l'on découvre, parfois, que le beau modèle ne valait
rien.

Cette capacité à bien se comporter au-delà des exemples appris porte un nom :
la **généralisation**. C'est elle, et non l'erreur d'entraînement, qui mesure la
vraie valeur d'un modèle. Ce chapitre lui est consacré : comment la mesurer,
pourquoi elle est si difficile à obtenir, et ce qu'elle révèle sur la nature même
des modèles.

## Un modèle se juge sur ce qu'il n'a jamais vu

La solution est presque embarrassante de simplicité : **on cache des exemples au
modèle.** Avant l'entraînement, on met de côté une partie des données, disons un
cinquième. Le modèle apprend sur le reste, sans jamais voir cette réserve. Puis,
une fois entraîné, on l'interroge dessus : ces exemples-là sont neufs *pour lui*,
mais nous, nous connaissons les bonnes réponses. Sa performance sur cette réserve
est une estimation honnête de ce qu'il fera face à du vrai neuf.

{{< image src="/images/module2/jeu-de-test.svg" alt="L'ensemble des données est coupé en deux : un grand bloc « entraînement » sur lequel le modèle apprend, et un petit bloc « test » mis de côté, que le modèle ne voit jamais pendant l'entraînement et qui sert à mesurer sa généralisation." title="On scinde les données : le modèle apprend sur l'ensemble d'entraînement ; l'ensemble de test, gardé sous scellés, sert à juger sa généralisation." loading="lazy" >}}

L'analogie de l'examen tombe juste. Un enseignant qui noterait ses étudiants
uniquement sur les questions distribuées d'avance pour réviser ne mesurerait pas
grand-chose : rien n'empêche d'apprendre ces réponses par cœur sans
comprendre ; c'est le sur-apprentissage (*overfitting*) de l'étudiant, et le
jeu de test est ce qui permet de le détecter.
Pour évaluer la *compréhension*, il faut des questions nouvelles, jamais vues.
C'est exactement ce qu'on fait à un modèle.

On donne des noms à ces deux paquets. L'**ensemble d'entraînement**, sur lequel le
modèle apprend (et où l'on mesure l'**erreur d'entraînement**). Et l'**ensemble de
test**, mis sous scellés jusqu'au bout, qui sert à mesurer l'**erreur de test**,
la seule qui estime la généralisation. La règle d'or : *on ne touche jamais au
jeu de test pendant l'entraînement.* Le jour où le modèle apprend, même
indirectement, sur ses propres données d'examen, le test ne veut plus rien dire.

{{% hint info %}}

Et lorsqu'il faut *régler* quelque chose (la valeur de $k$ pour kNN, ou le taux
d'apprentissage rencontré dans [*Un modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele)), on ne peut pas non plus se servir du
jeu de test pour choisir, sous peine de le « griller ». On réserve alors un
troisième paquet, l'**ensemble de validation**, dédié à ces réglages ; le jeu de
test, lui, reste vierge pour l'ultime verdict.

{{% /hint %}}

{{% hint warning %}}
**La règle d'or, à l'échelle d'aujourd'hui : les grands modèles de langage.**
Toute cette section suppose qu'on sache ce que le modèle a vu pendant
l'entraînement. Pour un LLM, ce n'est plus vraiment possible : ses données
d'entraînement, des milliers de milliards de mots aspirés sur le Web, sont si
vastes que personne n'en connaît le contenu précis, pas même ceux qui l'ont
entraîné. Or l'examen qu'on croit lui faire passer, un problème de
mathématiques, une question d'un test standardisé, un exercice de
programmation, a fort probablement circulé sur le Web, avec son corrigé. Le
modèle a-t-il *raisonné*, ou *retrouvé* ? On ne peut plus le savoir avec
certitude. C'est le cas interdit par la règle d'or, un modèle qui a vu, même
indirectement, ses données d'examen, mais porté à une échelle où plus personne
ne peut le contrôler. D'où une saine méfiance devant les scores impressionnants
qu'on annonce.

Le problème dépasse la mesure. Rappelez-vous la 1001ᵉ image du début du
module : tout reposait sur le fait de savoir si elle faisait partie des 1000.
Pour un LLM, on ne peut plus répondre. Distinguer ce qu'un modèle *sait déjà*
(parce que c'était dans ses données) de ce qu'il *apporte de nouveau* (parce
qu'il généralise) est devenu, pour ces systèmes, une question ouverte, et au
fond philosophique : où finit la mémoire, où commence la compréhension ? Ce
chapitre l'a posée sur vingt maisons ; le [Module 4](docs/module4) la retrouvera devant un
modèle qui a lu une bonne partie de ce que l'humanité a écrit.
{{% /hint %}}

## Linéaire ou non-linéaire : ce qu'un modèle peut dessiner

Revenons un instant sur ce que nous avons construit. La régression linéaire d'[*Un
modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele) : une droite. La frontière de la régression logistique : une droite.
Celle de Bayes naïf : une droite, encore (nous l'avions noté avec surprise). Et
même notre filtre anti-pourriel, sous ses montagnes de mots, prenait *lui aussi*
une décision linéaire. Un air de famille se dessine.

Ces modèles ont tous en commun de tirer leur décision d'une **somme pondérée** des
caractéristiques : chaque attribut pousse d'un côté ou de l'autre,
proportionnellement à son poids, et l'on tranche selon le total. Géométriquement,
cela donne toujours la même chose : une droite (un plan en trois dimensions ; un
*hyperplan* au-delà). On les appelle des **modèles linéaires**.

Est-ce grave ? Autrement dit : y a-t-il des choses qu'**aucune droite** ne peut
apprendre ?

La réponse est oui — et vous connaissez déjà la victime la plus célèbre de cette
limite. Souvenez-vous du **perceptron**, au [Module 1](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969) : c'est exactement là-dessus
qu'il s'est brisé, en 1969. L'exemple fatal s'appelle le **XOR**, *l'un ou
l'autre, mais pas les deux*, la règle du va-et-vient qui commande une lampe au
bout d'un couloir. Placez ses quatre cas dans le plan : les deux « éteint »
tombent sur une diagonale, les deux « allumé » sur l'autre.

{{< image src="/images/module2/xor.svg" alt="Deux panneaux illustrant le XOR. Dans chacun, quatre points aux coins d'un carré : deux bleus sur une diagonale (bas-gauche et haut-droit), deux rouges sur l'autre (haut-gauche et bas-droit). Chaque panneau montre une droite différente traversant le plan pour tenter de séparer les couleurs ; dans les deux cas, un point bleu reste du côté des rouges, cerclé de rouge et marqué d'une croix. Aucune droite ne réussit." title="Le XOR : quelle que soit la droite tracée, un point reste toujours du mauvais côté — la limite même d'un modèle linéaire." loading="lazy" >}}

Essayez. Prenez n'importe quelle droite, inclinez-la comme vous voulez : il
restera toujours un point du mauvais côté. Ce n'est pas un manque d'astuce — c'est
une impossibilité.

Et voici le point crucial, à bien distinguer de tout ce qui précède : **cet échec
n'a rien à voir avec le bruit, ni avec le manque de données**. Donnez à votre
modèle linéaire un million d'exemples parfaits, sans la moindre erreur de mesure :
il échouera exactement pareil. Ce n'est pas un modèle mal réglé, ni un modèle qui
manque d'entraînement. C'est un modèle dont le **répertoire de formes** ne
contient tout simplement pas la réponse. On appelle cela sa **capacité** (ou son
*expressivité*) : l'ensemble des frontières qu'il est seulement capable de
dessiner. Un modèle linéaire n'en connaît qu'une famille : les droites.

À l'inverse, souvenez-vous de kNN. Sa frontière, elle, se contorsionne à volonté,
épouse des îlots, contourne des amas : aucune contrainte de forme ne pèse sur
elle. Le XOR ? Il le règle sans même s'en apercevoir : chaque point regarde ses
voisins, et les voisins d'un coin bleu sont bleus. kNN est un modèle
**non-linéaire**, et c'était donc, sans qu'on le dise, notre premier.

Et l'arbre de décision de la page précédente, lui, règle le XOR en deux
questions, « à droite ? » puis « en haut ? » : quatre rectangles, un
par coin, la frontière que le perceptron ne pouvait pas tracer. Ses coupes
parallèles aux axes sont une autre façon, très différente de celle de kNN,
d'être non-linéaire.

Deux familles, donc, et une question à se poser avant toute autre devant un
problème : *la vérité que je cherche a-t-elle une chance de tenir dans le
répertoire de mon modèle ?* Si elle n'y est pas, aucun réglage, aucune donnée
supplémentaire ne l'y mettra.

Comment franchir le mur, alors ? L'apprentissage automatique classique offre deux
échappatoires. La première, nous venons de la voir : prendre un modèle
non-linéaire, comme kNN. La seconde est plus rusée : **fabriquer soi-même la bonne
caractéristique**. Ajoutez aux deux entrées leur produit $x_1 \cdot x_2$, et le
XOR devient, comme par magie, séparable par une droite dans ce nouvel espace. Mais
remarquez le prix : c'est *vous*, l'humain, qui avez dû trouver l'astuce. Et si
personne ne sait quelle caractéristique inventer ?

C'est précisément la question que le [Module 3](docs/module3) viendra trancher : les réseaux de
neurones apprendront à **fabriquer eux-mêmes** les caractéristiques qui rendent le
problème séparable, en empilant des couches. Le mur dressé en 1969 tombera en
1986 : c'est la dette que le [Module 1](docs/module1/60-hivers/#le-premier-hiver-la-mort-du-perceptron-1969) avait laissée ouverte, et c'est là qu'elle
sera payée.

Mais attention : pouvoir se courber n'est pas un bien en soi. Un modèle capable
d'épouser n'importe quelle forme peut aussi épouser… n'importe quoi. C'est tout le
sujet de la section suivante.

## Trop coller, ou trop lisser : le compromis biais-variance

Nous venons de voir qu'un modèle doit être assez *expressif* pour que la vérité
tienne dans son répertoire. Mais l'excès inverse guette aussitôt : un modèle trop
souple finit par épouser le hasard autant que le signal. Pour voir ce compromis à
l'œuvre (et le *mesurer*, maintenant que nous savons le faire), revenons à notre
vieille connaissance, kNN, dont l'unique réglage, le nombre de voisins $k$, agit
précisément comme un curseur de souplesse. Reprenez l'applet ; cette fois, faites
lentement glisser $k$ d'un bout à l'autre, et observez la frontière.

{{< applet src="/html/applets/knn.html" height="692" >}}

À **$k = 1$**, chaque point ne consulte que son unique plus proche voisin : la
frontière se contorsionne pour entourer le moindre exemple, forme des îlots
autour des points isolés, épouse jusqu'au dernier détail. L'erreur
d'entraînement tombe à *zéro* : forcément, chaque exemple est son propre voisin
le plus proche. Mais cette frontière torturée a pris pour argent comptant le
moindre hasard des données : un point un peu aberrant, du bruit, et elle se plie
quand même pour l'accommoder. C'est le **sur-apprentissage** (*overfitting*) : notre étudiant qui
a appris le corrigé par cœur, jusqu'aux coquilles, sans rien comprendre. Sur des
données neuves, il trébuche.

À l'autre extrême, **$k$ très grand**, chaque prédiction moyenne tant de voisins
que la frontière se lisse en une courbe placide, presque droite. Si placide,
parfois, qu'elle gomme des structures pourtant bien réelles. C'est le travers
inverse, le **sous-apprentissage** (*underfitting*) : le modèle est trop rigide pour épouser la
vraie forme des données.

Deux façons d'échouer, donc, et elles portent chacune un nom :

- la **variance**, c'est la sensibilité du modèle au hasard de l'échantillon
  (côté $k$ petit) : changez quelques points d'entraînement, et un modèle à haute
  variance se redessine du tout au tout ;
- le **biais**, c'est sa rigidité de naissance (côté $k$ grand) : son incapacité
  *systématique* à capturer la vraie forme, quels que soient les points qu'on lui
  montre.

{{% hint info %}}
**Qu'est-ce que le bruit ?** Nous allons dire qu'un modèle trop souple
« épouse le bruit ». Il faut entendre par là que des données ne sont jamais le
signal pur. Le prix d'une maison, c'est une tendance (plus c'est grand, plus
c'est cher) *plus* un aléa : l'humeur du vendeur, la saison, une négociation,
mille choses que le registre n'a pas notées. Nos vingt maisons ne sont pas
*sur* la droite, elles sont *autour* : l'écart de chacune est ce bruit. Un bon
modèle apprend la tendance et laisse le bruit ; un modèle trop souple apprend
les deux, et le bruit qu'il a appris ne se reproduira pas dans la maison
suivante, puisque c'est du hasard. Toute la courbe en U découle de là : il y
a, dans toute donnée, une part qu'il ne faut *pas* apprendre.
{{% /hint %}}

Et voici le nœud — l'une des idées les plus profondes du domaine. Quand on rend
un modèle plus souple (ici, en diminuant $k$), son erreur d'entraînement ne fait
que baisser : un modèle flexible colle toujours mieux à ce qu'il a déjà vu. Mais
son erreur de *test*, elle, suit une courbe en **U** : elle baisse d'abord (on
capture enfin les vraies régularités), puis **remonte** dès qu'on se met à épouser
le bruit. Le bon modèle se cache tout au fond du U, à l'équilibre exact entre
biais et variance.

{{< image src="/images/module2/bias-vs-variance-with-errors.png" alt="Deux courbes en fonction de k. L'erreur d'entraînement (rouge) croît régulièrement de k=1 à k=21. L'erreur de test (bleu) a une forme en U : elle décroît, atteint un minimum, puis remonte. Deux droites diagonales figurent la variance (décroissante) et le biais (croissant) ; leur croisement marque le minimum de l'erreur de test." title="L'erreur de test (en bleu) suit une courbe en U : trop de variance à gauche, trop de biais à droite. Le meilleur modèle est au creux." loading="lazy" >}}

Le point crucial : **rien de tout cela n'est propre à kNN.** Chaque modèle possède
son curseur de souplesse : le nombre de termes d'une courbe plus souple qu'une
droite (nous allons le voir à l'instant), la profondeur d'un arbre de décision,
le nombre de paramètres d'un réseau de neurones. Et
chacun affronte le même U, le même arbitrage entre coller et lisser. C'est le
**compromis biais-variance**, et savoir le régler est l'un des vrais savoir-faire
de l'apprentissage automatique.


## Garder un modèle riche, mais le tenir en laisse : la régularisation

Le compromis biais-variance semble nous laisser un seul levier : tourner le
curseur de souplesse vers le bas, comme nous l'avons fait avec kNN en
augmentant $k$, ou avec l'arbre en limitant sa profondeur. C'est une solution, mais elle est brutale : elle bride le modèle
*avant* même de l'avoir laissé regarder les données, et le curseur est
grossier, un cran à la fois. Or il arrive qu'on veuille un modèle riche, capable
de dessiner des formes compliquées si les données l'exigent, sans pour autant
lui permettre d'épouser le moindre hasard.

Il existe une troisième voie, plus fine, et elle tient en une phrase : **au lieu
de limiter la souplesse du modèle, on la fait payer.** Souvenez-vous de la
fonction d'erreur d'[*Un modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele) :
elle mesure de combien le modèle se trompe sur les exemples, et l'entraînement
consiste à la faire descendre. On y ajoute un second terme, une **pénalité** qui
grandit avec la *complexité* du modèle :

$$\text{erreur totale} = \text{erreur sur les données} + \lambda \times \text{complexité}$$

Le modèle doit désormais négocier : coller aux points fait baisser le premier
terme, mais coûte du second. Il ne se contorsionnera que si le gain en vaut la
peine. La bille de la descente de gradient roule toujours vers le creux, mais
dans un paysage remodelé, où les régions « trop compliquées » ont été
surélevées.

Pour voir la pénalité à l'œuvre, il nous faut un modèle assez souple pour
surapprendre. Prenons la droite d'*Un modèle qui s'entraîne* et donnons-lui du
jeu : au lieu de $\text{prix} = m \times \text{superficie} + b$, autorisons
aussi des termes en superficie², superficie³, et ainsi de suite, jusqu'à la
puissance 12. Une telle courbe s'appelle un *polynôme*, et chaque terme ajouté
apporte un paramètre de plus : de deux, nous passons à treize. Le curseur de
souplesse, ici, c'est ce nombre de termes, le *degré*. Et treize paramètres pour
vingt maisons, c'est largement de quoi zigzaguer entre les points.

Reste à dire ce qu'est, concrètement, la complexité. La réponse la plus courante
est d'une simplicité désarmante : **la taille des paramètres.** Regardez ce que
fait un polynôme qui zigzague entre les points : pour monter et descendre si
vite, il lui faut des coefficients énormes, qui se compensent presque pour ne
laisser dépasser que de petites bosses. Forcer les coefficients à rester petits,
c'est donc forcer la courbe à rester calme. La pénalité s'écrit alors simplement
comme la somme des carrés des paramètres, et tout le reste est inchangé : même
modèle, même degré, même descente.

{{< image src="/images/module2/regularisation.svg" alt="Deux panneaux montrant le même nuage de maisons (superficie en abscisse, prix en ordonnée) et le même polynôme de degré 12 ajusté aux données. À gauche, sans pénalité : la courbe ondule pour passer au plus près de chaque point, avec des bosses et des creux entre eux, et s'envole aux bords. À droite, avec une pénalité sur la taille des coefficients : le même polynôme se calme et suit la tendance générale, presque une droite." title="Même modèle, même degré ; seule la pénalité change. À gauche, le polynôme libre épouse le bruit ; à droite, tenu en laisse, il retrouve la tendance." loading="lazy" >}}

Le nombre $\lambda$ règle la sévérité de la pénalité. À zéro, on retrouve le
modèle libre ; trop grand, tout est écrasé et l'on retombe dans le
sous-apprentissage (*underfitting*) : une droite plate, pour finir. C'est un hyper-paramètre de
plus, et on le choisit comme les autres : sur l'ensemble de validation, jamais
sur le jeu de test.

Cette idée porte, selon les modèles, des noms différents : pour la droite et ses
cousines, *régression ridge* (pénalité sur les carrés) ou *lasso* (sur les
valeurs absolues, qui a la propriété remarquable de mettre certains paramètres
exactement à zéro, donc d'*éliminer* des caractéristiques) ; pour les réseaux
de neurones, *weight decay*, le même terme sous un autre nom. Elle a aussi des
cousines qui ne passent pas par la fonction d'erreur, mais visent le même but,
empêcher le modèle d'épouser le bruit : arrêter l'entraînement avant qu'il ne
colle trop (l'*arrêt précoce*), ou éteindre au hasard une partie des neurones à
chaque pas (le *dropout*) ; et pour l'arbre, l'**élagage**, qui le laisse
pousser puis coupe les branches qui n'apportent que du détail. Le
[Module 3](docs/module3) les retrouvera. Sous
leurs noms divers, toutes disent la même chose : la souplesse est une
ressource, et un bon modèle est un modèle riche qu'on tient en laisse.

{{% hint info %}}

Une énigme pour plus tard : si trop de souplesse nuit, comment les réseaux de
neurones géants d'aujourd'hui (des centaines de *milliards* de paramètres,
soit une souplesse vertigineuse) parviennent-ils malgré tout à généraliser ?
La réponse, surprenante, bousculera cette jolie courbe en U… au [Module 3](docs/module3).

{{% /hint %}}

## Paramétrique ou non-paramétrique

Il existe une seconde grande façon de classer les modèles : non plus selon leur
souplesse, mais selon ce qu'il en reste une fois l'entraînement terminé. La
question est simple : le modèle a-t-il **distillé** les données en une poignée de
réglages, ou les **garde-t-il** auprès de lui ?

Repensez à kNN et à son [angle mort](docs/module2/40-predire-par-ressemblance/#langle-mort-de-knn) : il n'a, à proprement parler, rien
à apprendre. Pas de paramètres à régler ; pour prédire, il consulte directement
les exemples mémorisés. *Les données sont le modèle.* Conséquence : sa taille
grossit avec le jeu de données. Mille exemples, mille exemples à trimballer ;
un million, un million. On dit d'un tel modèle qu'il est **non-paramétrique** :
il ne résume pas les données dans un nombre fixe de réglages, il s'appuie sur
elles, telles quelles, jusqu'au bout.

À l'opposé, notre droite de régression : une fois trouvés sa pente et son
ordonnée, on peut **jeter les données**, et il ne reste que deux nombres, $m$ et
$b$, et ils suffisent à prédire. Pareil pour la régression logistique (un poids
par caractéristique) ou pour Bayes naïf (une moyenne et une dispersion par
classe, ou une probabilité par mot). Ces modèles sont **paramétriques** : ils
compressent toute leur connaissance dans un jeu de paramètres de taille *fixée
d'avance*, que l'on ait appris sur cent exemples ou sur cent millions. Vous
reconnaissez là un fil tendu depuis *Un modèle qui s'entraîne* : le modèle bête distillait tout en *un*
nombre, la droite en *deux*, kNN en *aucun*. C'était déjà, sans le dire, l'axe
paramétrique / non-paramétrique.

Chaque famille a son tempérament :

- le modèle **paramétrique** est léger, rapide à la prédiction, et généralise par
  l'effet même de la compression qu'il s'impose, mais il *parie sur une forme*
  (une droite, par exemple). Si la vraie structure des données n'a pas cette
  forme, aucun réglage ne le sauvera : c'est du **biais** ;
- le modèle **non-paramétrique** ne présume presque rien de la forme et peut
  épouser des structures très complexes, mais il est lourd (tout garder), lent à
  prédire, et plus exposé à coller au bruit : c'est de la **variance**.

On retrouve, en filigrane, le compromis de la section précédente. Distiller ou
tout garder, parier sur une forme ou suivre les données : il n'existe pas de
réponse universelle, seulement des choix adaptés au problème, et c'est tout l'art
de la discipline que de les faire avec discernement.

{{< image src="/images/module2/parametrique-vs-non.svg" alt="À gauche, un nuage de points est résumé par une droite réduite à deux réglages m et b : le modèle paramétrique distille les données et peut ensuite les jeter. À droite, les mêmes points sont conservés tels quels : le modèle non-paramétrique garde toutes les données et s'appuie dessus pour prédire." title="Paramétrique : distiller les données en quelques réglages, puis les jeter. Non-paramétrique : garder toutes les données et s'appuyer dessus." loading="lazy" >}}

Nous savons maintenant ce qu'un modèle peut dessiner, jusqu'où le laisser se
courber, et comment le tenir en laisse. Il reste à savoir *mesurer* tout cela
sans se raconter d'histoires : un score, nous allons le voir, peut mentir de
bien des façons. C'est l'objet de la page suivante.
