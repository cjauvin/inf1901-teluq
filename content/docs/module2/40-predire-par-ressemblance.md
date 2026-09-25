---
title: "Prédire par ressemblance"
weight: 40
slug: predire-par-ressemblance
---

# Prédire par ressemblance

La page précédente s'est achevée sur une promesse : si décrire des objets par des
nombres transforme leur ressemblance en une *distance*, alors il doit exister une
façon très simple de prédire. La voici, sans doute l'idée la plus intuitive de
tout l'apprentissage automatique : **pour deviner la réponse sur un nouveau cas,
regardons les cas connus qui lui ressemblent le plus, et copions la leur.**

Pour estimer le prix d'une maison qu'on n'a jamais vue, on cherche les maisons
déjà vendues qui lui ressemblent le plus (même quartier, même taille, même âge),
et on s'attend à un prix comparable. C'est, au fond, ce que fait un agent
immobilier quand il sort ses « comparables ». Reste à transformer cette intuition
en une procédure précise. Et tout repose sur un seul mot : *ressembler*.
Commençons par le rendre mesurable.

## Mesurer la ressemblance : la distance

« Se ressembler », pour deux objets décrits par des nombres, a une traduction
géométrique immédiate : être **proches** dans leur espace. Et la proximité entre
deux points, ça se mesure — c'est la **distance**.

Pour deux points dans un plan, c'est la distance la plus familière qui soit : la
longueur du trait droit qui les relie, celle qu'on mesurerait à la règle. (Les
mathématiciens l'appellent la *distance euclidienne*, mais l'idée est exactement
celle de tous les jours.)

{{< image src="/images/module2/distance_2d.png" alt="Deux points dans un plan reliés par un segment droit : la distance euclidienne entre eux." title="La distance entre deux points : la longueur du trait droit qui les relie." loading="lazy" >}}

Cette longueur, on sait la calculer depuis l'école : c'est le théorème de
Pythagore. Pour deux points d'un plan, on prend l'écart entre eux sur le premier
axe, l'écart sur le second, on élève chacun au carré, on additionne, et on prend
la racine carrée du tout :

$$\text{distance} = \sqrt{(\text{écart sur l'axe 1})^2 + (\text{écart sur l'axe 2})^2}$$

Le point remarquable, c'est que rien dans cette recette ne dépend du nombre
d'axes. Six caractéristiques pour nos maisons ? Six écarts au lieu de deux,
chacun au carré, additionnés, et la racine carrée du tout. On compare les objets
coordonnée par coordonnée, et on en tire un seul nombre : petit s'ils se
ressemblent, grand s'ils diffèrent. Et, comme on l'a vu au chapitre précédent,
rien n'oblige à s'arrêter là : la même formule vaut jusqu'à une image, dont les
millions de pixels forment autant de coordonnées. Pour deux photos, l'écart sur
un axe, c'est simplement la différence entre le *même* pixel de l'une et de
l'autre. En notant $A_1$ la valeur du premier pixel de la photo $A$, $B_1$ celle
du premier pixel de la photo $B$, et ainsi de suite jusqu'au $n$-ième :

$$\text{distance}(A, B) = \sqrt{(A_1 - B_1)^2 + (A_2 - B_2)^2 + \cdots + (A_n - B_n)^2}$$

Deux photos identiques donnent zéro : chaque écart est nul. Deux photos qui ne
diffèrent que par un pixel donnent un nombre minuscule. Et plus les pixels
diffèrent, nombreux ou fortement, plus le nombre grandit. Une seule formule, du
plan à la photo, et *n* peut valoir deux comme des millions.

{{< image src="/images/module2/distance_high_dim.png" alt="La même idée de distance, transposée à un espace de haute dimension." title="La même distance se calcule, quel que soit le nombre de dimensions." loading="lazy" >}}

{{% hint warning %}}
**Une nuance importante.** Que la distance se *calcule* sur des pixels ne veut pas
dire qu'elle y *mesure bien* la ressemblance. Sur des caractéristiques choisies
par un humain (superficie, nombre de pièces…), la proximité a un sens clair. Sur
des pixels bruts, beaucoup moins : deux photos du *même* chat, dans deux poses,
peuvent être très éloignées pixel à pixel ; une photo et sa version simplement
assombrie, quasi identiques pour notre œil, le seront tout autant. Faire en sorte
que la distance reflète la ressemblance *réelle* d'objets complexes est un
problème à part entière, celui des **bonnes représentations**, que nous
retrouverons avec les réseaux de neurones (Module&nbsp;3) et les plongements
(Module&nbsp;4). Pour des données tabulaires comme nos maisons, en revanche, la
distance brute fait déjà très bien l'affaire.
{{% /hint %}}

{{% hint warning %}}
**La malédiction de la dimension.** Il y a une autre raison, plus mathématique,
pour laquelle la distance perd de son sens quand les dimensions se
multiplient. Dans un plan, vingt maisons suffisent à peupler l'espace : chacune
a des voisines proches. Dans un espace à un million de dimensions, celui des
pixels, vingt exemples, ou vingt millions, sont perdus dans une immensité vide,
et *tout* est loin de *tout* : les distances entre les points se ressemblent
toutes, et « le plus proche voisin » ne l'est plus guère. C'est la
**malédiction de la dimension** (*curse of dimensionality*) : chaque
caractéristique ajoutée agrandit l'espace d'un facteur, et le nombre d'exemples
nécessaire pour le remplir explose. Elle frappe kNN de plein fouet, et c'est
l'une des raisons pour lesquelles, sur des images ou du texte, on cherche
d'abord à *réduire* le nombre de dimensions à quelques-unes qui comptent, une
idée que les [Modules 3](docs/module3) et [4](docs/module4) développeront.
Vous avez déjà croisé cette fatalité sous un autre nom : l'[explosion
combinatoire](docs/module1/30-chercher-raisonner/#lexplosion-combinatoire) du
Module 1. Là, chaque coup de plus multipliait les parties à explorer ; ici,
chaque caractéristique de plus multiplie l'espace à remplir. C'est la même
croissance exponentielle, qui résiste à la force brute et qu'on ne dompte
qu'avec une astuce.
{{% /hint %}}

Nous tenons donc notre mesure de ressemblance, fiable pour des données
tabulaires comme nos maisons. Il ne reste plus qu'à nous en servir pour prédire.

## Les k plus proches voisins

Nous y voilà. Pour prédire le prix d'une maison inconnue, la recette est d'un
naturel désarmant : on calcule sa distance à toutes les maisons connues, on
retient celles qui lui ressemblent le plus, et on prédit la moyenne de leurs
prix. Pourquoi plusieurs voisins plutôt qu'un seul ? Parce que s'appuyer sur un
unique voisin serait fragile : il pourrait être un cas exceptionnel, une aubaine
ou une arnaque. En consultant plusieurs voisins et en les moyennant, on lisse ces
accidents.

Ce nombre de voisins consultés, on le note **k**, d'où le nom de l'algorithme :
les **k plus proches voisins** (*k-nearest neighbors*, ou kNN).
L'idée a été formalisée en 1951 par deux statisticiens, Evelyn Fix et Joseph
Hodges, dans un rapport rédigé pour l'armée de l'air américaine : c'est de la
statistique avant d'être de l'informatique.

Nous venons de faire une **régression** : la cible était un prix, un nombre, et
nous l'avons obtenu en *moyennant* nos voisins. Et pour une **classification** ?
Il suffit de changer la toute dernière étape : au lieu de moyenner les réponses
des voisins, on retient la plus fréquente, un **vote majoritaire**. Pour deviner
si une maison partira vite, on regarde ce qu'il en a été de ses plus proches
voisines, et on suit la majorité.

C'est là ce que kNN a de remarquable : il fait *les deux* sans rien changer
d'essentiel. Même distance, mêmes voisins — seule diffère la façon de combiner
leurs réponses. La plupart des algorithmes que nous verrons ensuite, eux, se
spécialiseront dans l'une ou l'autre tâche.

{{< image src="/images/module2/knn-regression-vs-classification.svg" alt="La recette kNN, illustrée comme un tronc commun qui se sépare en deux à la fin. Tronc commun : une nouvelle maison, puis les distances à tous les exemples connus, puis les k plus proches voisins. Ces étapes sont communes aux deux tâches. Puis une seule bifurcation, à l'étape d'agrégation : en haut, la moyenne des prix des voisins donne un nombre (250 000 $), la régression ; en bas, le vote majoritaire des réponses des voisins donne une catégorie (« vendue vite »), la classification." title="Un seul tronc, une seule fourche : kNN suit exactement les mêmes étapes pour la régression et la classification ; seule la toute dernière (moyenne ou majorité) les distingue." loading="lazy" >}}

{{% hint info %}}
**La recette des _k_ plus proches voisins**, pour prédire à propos d'une nouvelle maison :

1. Calculer la **distance** entre cette maison et *chacune* des maisons déjà connues (à partir de leurs caractéristiques).
2. Garder les **k** maisons les plus proches, ses « voisins ».
3. Combiner les réponses de ces voisins :
   - pour un **nombre** (régression) → prendre leur **moyenne** ;
   - pour une **catégorie** (classification) → prendre leur **majorité**.

Seule cette dernière étape distingue les deux tâches ; tout le reste est identique.
{{% /hint %}}

Revenons à nos maisons, dans le plan de la seconde question (distance du
centre, année de construction). Que répond kNN à une maison *nouvelle*, placée
n'importe où dans ce plan ? On peut le lui demander pour chaque point du plan,
un par un, et teinter ce point de la réponse obtenue : bleu pâle si ses *k*
voisins votent « vendue vite », rouge pâle s'ils votent « a traîné ». Voici le
résultat pour *k* = 3 :

{{< image src="/images/module2/maisons-frontiere-k3.svg" alt="Le nuage coloré des maisons, dans le plan distance du centre × année de construction, avec le fond teinté : bleu pâle là où kNN (k = 3) répondrait « vendue vite » à une maison qui s'y trouverait, rouge pâle là où il répondrait « a traîné ». La ligne où la teinte bascule serpente dans la bande vide entre les deux amas : c'est la frontière de décision. Les deux exceptions sont absorbées par leur territoire adverse." title="La frontière de décision de kNN (k = 3) sur nos maisons : le fond donne la réponse du modèle en chaque point du plan, et la ligne où la couleur bascule est la frontière." loading="lazy" >}}

Le plan se trouve découpé en deux **territoires**. La ligne où la teinte
bascule, celle qui serpente dans la bande vide entre les deux amas, porte un
nom : c'est la **frontière de décision**. Personne ne l'a tracée ; elle est la
conséquence de la règle, appliquée partout. Et elle est tout ce qui compte pour
prédire : une maison qui tombe d'un côté sera classée « vendue vite », de
l'autre « a traîné », sans autre nuance. Regardez aussi ce qu'il advient des deux
exceptions du premier chapitre : à *k* = 3, chacune est absorbée par le
territoire adverse, puisque ses trois voisins les plus proches votent contre
elle.

Retenez cette image, car elle vaut pour tout classificateur, et pas seulement
pour kNN : **classer, c'est découper l'espace en territoires, et un modèle de
classification se résume à la frontière qu'il trace.** C'est d'ailleurs pourquoi
la classification est plus parlante à l'œil que la régression : une frontière se
*voit* d'un seul coup en deux dimensions. Nous rencontrerons au chapitre
« Classer » des modèles dont la frontière est une simple droite ; celle de kNN,
elle, peut prendre n'importe quelle forme.

L'applet ci-dessous permet de jouer avec cette frontière. Deux catégories, des
points rouges et des points bleus : chaque point coloré est un exemple connu, et
le fond montre, comme ci-dessus, la prédiction de kNN pour tout nouveau point.
Ajoutez des points, déplacez-les, faites varier *k*, et observez la frontière de
décision se redessiner.

{{< applet src="/html/applets/knn.html" height="692" >}}

## Le choix de k

En jouant avec l'applet, une question s'impose vite : quelle valeur donner à
**k** ?

Les deux extrêmes sont instructifs. Avec **k = 1**, chaque prédiction ne s'appuie
que sur l'unique voisin le plus proche : la frontière épouse alors le moindre
détail, contourne chaque point individuel et se tortille à l'excès. Le modèle
colle si bien aux exemples connus qu'il en devient esclave, réagissant au
moindre point un peu aberrant. Ce travers a un nom, et il est central dans
tout ce qui suit : le **sur-apprentissage** (*overfitting*), apprendre les
exemples au lieu d'apprendre d'eux. Nous y reviendrons longuement dans
[*Généraliser*](docs/module2/70-generaliser). Nos maisons le montrent : à *k* = 1, chacune des
deux exceptions se taille un îlot de sa couleur en plein territoire adverse, et
la frontière se découpe en cellules anguleuses.

{{< image src="/images/module2/maisons-frontiere-k1.svg" alt="Même plan, même fond teinté, mais avec k = 1 : chaque maison impose sa couleur à tout ce qui l'entoure. Les deux exceptions creusent chacune un îlot de leur couleur en plein territoire adverse, et la frontière se découpe en cellules anguleuses." title="La même frontière avec k = 1 : chaque exception se taille un îlot, et la frontière épouse le moindre point." loading="lazy" >}}

À l'autre bout, avec un **k très grand**, chaque
prédiction moyenne tant de voisins que les particularités locales s'effacent : la
frontière devient lisse, paisible… parfois au point d'ignorer des structures
pourtant bien réelles.

Entre les deux se cache une « bonne » valeur — ni trop petite, ni trop grande.
Mais comment la trouver ? La question semble anodine ; elle est en réalité l'une
des plus profondes de tout l'apprentissage automatique. Car elle n'a rien de
propre à kNN : *tout* modèle affronte le même dilemme, être assez souple pour
saisir les vraies régularités, sans l'être au point d'épouser le moindre hasard
des données.

Cette question est si centrale que nous lui consacrerons une page entière,
[*Généraliser*](docs/module2/70-generaliser), une fois que nous aurons en main quelques modèles de plus pour
l'éclairer. Pour l'instant, retenez seulement l'intuition : **k règle un curseur
entre « coller aux exemples » et « lisser à l'excès ».**

## L'angle mort de kNN

kNN a un charme particulier : il n'a, à proprement parler, **rien à apprendre**.
Pas d'entraînement, pas de paramètres à régler : il lui suffit de garder en
mémoire tous les exemples connus et de les consulter au moment de prédire. Les
données *sont* le modèle.

Cette élégance cache pourtant deux faiblesses, qui vont motiver toute la suite.

D'abord, c'est **lourd**. Pour chaque nouvelle prédiction, kNN doit calculer la
distance à *tous* les exemples connus, sans exception. Avec quelques dizaines de
maisons, aucun souci. Mais imaginez un système qui doit reconnaître un visage
parmi des millions d'images, ou répondre en une fraction de seconde à des
millions d'utilisateurs : tout recalculer à chaque fois devient ruineux. kNN
repousse tout le travail au dernier moment, là où il coûte le plus cher.

Ensuite, plus profondément : kNN **ne dégage aucune compréhension**. Aucune
règle, aucune tendance, aucune *forme* générale tirée des données. Il ne « sait »
pas que les grandes maisons coûtent plus cher : il se contente de retrouver des
voisins. Rappelez-vous [le modèle le plus bête](docs/module2/20-modele-le-plus-bete) : il avait, lui, distillé toute sa
connaissance en **un seul nombre**, le prix moyen. kNN fait l'inverse : il ne
distille rien, il garde tout.

Or c'est justement cette *distillation* qui nous intéresse. D'un vrai modèle, on
aimerait qu'il **apprenne** quelque chose des données : qu'il en extraie une
poignée de paramètres capturant la tendance générale, quitte à oublier ensuite
les exemples eux-mêmes. Léger à l'usage, et porteur d'une forme de compréhension.

Comment fabriquer un tel modèle ? C'est tout l'objet du prochain chapitre.
