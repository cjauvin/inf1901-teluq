---
title: "Prédire par ressemblance"
weight: 40
slug: predire-par-ressemblance
---

# Prédire par ressemblance

La page précédente s'est achevée sur une promesse : si décrire des objets par des
nombres transforme leur ressemblance en une *distance*, alors il doit exister une
façon très simple de prédire. La voici — sans doute l'idée la plus intuitive de
tout l'apprentissage automatique : **pour deviner la réponse sur un nouveau cas,
regardons les cas connus qui lui ressemblent le plus, et copions la leur.**

Pour estimer le prix d'une maison qu'on n'a jamais vue, on cherche les maisons
déjà vendues qui lui ressemblent le plus — même quartier, même taille, même âge —
et on s'attend à un prix comparable. C'est, au fond, ce que fait un agent
immobilier quand il sort ses « comparables ». Reste à transformer cette intuition
en une procédure précise. Et tout repose sur un seul mot : *ressembler*.
Commençons par le rendre mesurable.

## Mesurer la ressemblance : la distance

« Se ressembler », pour deux objets décrits par des nombres, a une traduction
géométrique immédiate : être **proches** dans leur espace. Et la proximité entre
deux points, ça se mesure — c'est la **distance**.

Pour deux points dans un plan, c'est la distance la plus familière qui soit : la
longueur du trait droit qui les relie, celle qu'on mesurerait à la règle. (Les
mathématiciens l'appellent la *distance euclidienne*, mais l'idée est exactement
celle de tous les jours.)

{{< image src="/images/module2/distance_2d.png" alt="Deux points dans un plan reliés par un segment droit : la distance euclidienne entre eux." title="La distance entre deux points : la longueur du trait droit qui les relie." loading="lazy" >}}

Cette mesure se calcule de la même façon dès qu'il y a plusieurs
caractéristiques : deux (un plan), six (notre tableau de maisons)… on compare les
objets coordonnée par coordonnée et on en tire un seul nombre — petit s'ils se
ressemblent, grand s'ils diffèrent. Et, comme on l'a vu au chapitre précédent,
rien n'oblige à s'arrêter là : la même formule vaut jusqu'à une image, dont les
millions de pixels forment autant de coordonnées.

{{< image src="/images/module2/distance_high_dim.png" alt="La même idée de distance, transposée à un espace de haute dimension." title="La même distance se calcule, quel que soit le nombre de dimensions." loading="lazy" >}}

{{% hint warning %}}
**Une nuance importante.** Que la distance se *calcule* sur des pixels ne veut pas
dire qu'elle y *mesure bien* la ressemblance. Sur des caractéristiques choisies
par un humain (superficie, nombre de pièces…), la proximité a un sens clair. Sur
des pixels bruts, beaucoup moins : deux photos du *même* chat, dans deux poses,
peuvent être très éloignées pixel à pixel ; une photo et sa version simplement
assombrie, quasi identiques pour notre œil, le seront tout autant. Faire en sorte
que la distance reflète la ressemblance *réelle* d'objets complexes est un
problème à part entière — celui des **bonnes représentations** —, que nous
retrouverons avec les réseaux de neurones (Module&nbsp;3) et les plongements
(Module&nbsp;4). Pour des données tabulaires comme nos maisons, en revanche, la
distance brute fait déjà très bien l'affaire.
{{% /hint %}}

Nous tenons donc notre mesure de ressemblance — fiable pour des données
tabulaires comme nos maisons. Il ne reste plus qu'à nous en servir pour prédire.

## Les k plus proches voisins

Nous y voilà. Pour prédire le prix d'une maison inconnue, la recette est d'un
naturel désarmant : on calcule sa distance à toutes les maisons connues, on
retient celles qui lui ressemblent le plus, et on prédit la moyenne de leurs
prix. Pourquoi plusieurs voisins plutôt qu'un seul ? Parce que s'appuyer sur un
unique voisin serait fragile — il pourrait être un cas exceptionnel, une aubaine
ou une arnaque. En consultant plusieurs voisins et en les moyennant, on lisse ces
accidents.

Ce nombre de voisins consultés, on le note **k** — d'où le nom de l'algorithme :
les **k plus proches voisins** (*k-nearest neighbors*, ou kNN).

{{% hint info %}}
**La recette des _k_ plus proches voisins** — pour prédire le prix d'une nouvelle maison :

1. Calculer la **distance** entre cette maison et *chacune* des maisons déjà connues (à partir de leurs caractéristiques).
2. Garder les **k** maisons les plus proches — ses « voisins ».
3. Prédire la **moyenne** des prix de ces voisins.

*(Pour une catégorie plutôt qu'un nombre — pourriel ou non, chat ou chien — une seule étape change : à l'étape 3, on prend la **majorité** des voisins au lieu de leur moyenne.)*
{{% /hint %}}

Ce simple basculement — moyenne ou majorité — recouvre la grande partition des
tâches de prédiction : la **régression** (prédire un nombre, comme un prix) et la
**classification** (prédire une catégorie, comme « pourriel » ou « courriel »).
kNN a ceci de remarquable qu'il fait *les deux* sans rien changer d'essentiel ;
la plupart des algorithmes que nous verrons ensuite, eux, se spécialiseront dans
l'un ou l'autre.

L'applet ci-dessous illustre le cas de la **classification**, en deux dimensions,
avec deux catégories — des points rouges et des points bleus. Chaque point
coloré est un exemple connu ; le fond coloré, lui, montre la prédiction de kNN
pour *tout* nouveau point qui s'y trouverait. Ajoutez des points, déplacez-les,
faites varier **k**, et observez la frontière entre territoire rouge et
territoire bleu se redessiner.

{{< applet src="/html/applets/knn.html" >}}

## Le choix de k

En jouant avec l'applet, une question s'impose vite : quelle valeur donner à
**k** ?

Les deux extrêmes sont instructifs. Avec **k = 1**, chaque prédiction ne s'appuie
que sur l'unique voisin le plus proche : la frontière épouse alors le moindre
détail, contourne chaque point individuel et se tortille à l'excès. Le modèle
colle si bien aux exemples connus qu'il en devient esclave — réagissant au
moindre point un peu aberrant. À l'autre bout, avec un **k très grand**, chaque
prédiction moyenne tant de voisins que les particularités locales s'effacent : la
frontière devient lisse, paisible… parfois au point d'ignorer des structures
pourtant bien réelles.

Entre les deux se cache une « bonne » valeur — ni trop petite, ni trop grande.
Mais comment la trouver ? La question semble anodine ; elle est en réalité l'une
des plus profondes de tout l'apprentissage automatique. Car elle n'a rien de
propre à kNN : *tout* modèle affronte le même dilemme — être assez souple pour
saisir les vraies régularités, sans l'être au point d'épouser le moindre hasard
des données.

Cette question est si centrale que nous lui consacrerons une page entière —
« Généraliser » — une fois que nous aurons en main quelques modèles de plus pour
l'éclairer. Pour l'instant, retenez seulement l'intuition : **k règle un curseur
entre « coller aux exemples » et « lisser à l'excès ».**

## L'angle mort de kNN

kNN a un charme particulier : il n'a, à proprement parler, **rien à apprendre**.
Pas d'entraînement, pas de paramètres à régler — il lui suffit de garder en
mémoire tous les exemples connus et de les consulter au moment de prédire. Les
données *sont* le modèle.

Cette élégance cache pourtant deux faiblesses, qui vont motiver toute la suite.

D'abord, c'est **lourd**. Pour chaque nouvelle prédiction, kNN doit calculer la
distance à *tous* les exemples connus, sans exception. Avec quelques dizaines de
maisons, aucun souci. Mais imaginez un système qui doit reconnaître un visage
parmi des millions d'images, ou répondre en une fraction de seconde à des
millions d'utilisateurs : tout recalculer à chaque fois devient ruineux. kNN
repousse tout le travail au dernier moment, là où il coûte le plus cher.

Ensuite, plus profondément : kNN **ne dégage aucune compréhension**. Aucune
règle, aucune tendance, aucune *forme* générale tirée des données. Il ne « sait »
pas que les grandes maisons coûtent plus cher — il se contente de retrouver des
voisins. Rappelez-vous le modèle de la page 20 : il avait, lui, distillé toute sa
connaissance en **un seul nombre**, le prix moyen. kNN fait l'inverse : il ne
distille rien, il garde tout.

Or c'est justement cette *distillation* qui nous intéresse. D'un vrai modèle, on
aimerait qu'il **apprenne** quelque chose des données — qu'il en extraie une
poignée de paramètres capturant la tendance générale, quitte à oublier ensuite
les exemples eux-mêmes. Léger à l'usage, et porteur d'une forme de compréhension.

Comment fabriquer un tel modèle ? C'est tout l'objet du prochain chapitre.
