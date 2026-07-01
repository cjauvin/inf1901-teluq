---
title: "Trois façons d'apprendre"
weight: 80
slug: trois-facons-d-apprendre
---

# Trois façons d'apprendre

Nous avons refermé le chapitre précédent sur une prise de conscience : tout ce
que nous avons construit dans ce module — régression, classification, la droite,
Bayes — appartenait à une seule et même famille, l'**apprentissage supervisé**,
celle où chaque exemple arrive accompagné de sa bonne réponse. Mais nous avons
aussi entrevu que ce n'était pas la seule façon d'apprendre.

Ce qui distingue les grandes familles de l'apprentissage automatique, c'est la
nature du **signal** dont le modèle se nourrit — ce qui, dans les données, lui
tient lieu de guide. Et il n'en existe, au fond, que trois grands types :

- une **réponse fournie** pour chaque exemple : c'est l'apprentissage
  **supervisé**, notre terrain depuis le début ;
- **aucune réponse**, juste des données brutes dans lesquelles il faut débusquer
  une structure : l'apprentissage **non supervisé** ;
- ni réponse ni structure donnée, mais une **récompense** qui arrive après coup,
  au fil de l'action : l'apprentissage par **renforcement**.

{{< image src="/images/module2/trois-paradigmes.svg" alt="Trois panneaux. « Supervisé » : des points étiquetés en bleu et rouge — la réponse est donnée. « Non supervisé » : les mêmes points, tous gris et sans étiquette, que l'algorithme regroupe en cercles pointillés — on découvre des groupes. « Renforcement » : une boucle entre un agent et son environnement, reliés par une flèche « action » et une flèche « récompense »." title="Les trois grandes familles, par la nature de leur signal : réponse donnée (supervisé), structure à découvrir (non supervisé), récompense au fil de l'action (renforcement)." loading="lazy" >}}

Trois signaux, trois façons d'apprendre. Nous avons passé tout le module dans la
première ; ce dernier chapitre part à la rencontre des deux autres — moins pour
les maîtriser que pour situer ce que nous avons appris dans un paysage plus vaste,
et apercevoir les routes qui mènent aux modules suivants.

## Apprendre avec un professeur : le supervisé

Commençons par ce que nous connaissons déjà par cœur. En apprentissage supervisé,
le signal est une **réponse toute prête**, attachée à chaque exemple : le prix de
cette maison, l'étiquette *pourriel* de ce courriel, la couleur de ce point. Le
modèle n'a qu'un but — apprendre à relier l'entrée à cette réponse —, et une fois
entraîné, il l'applique à des cas neufs. C'est l'image même du professeur qui
corrige : il connaît la bonne réponse, et c'est en s'y comparant que l'élève
progresse.

Nous en avons rencontré les deux visages : la **régression**, quand la réponse
est un nombre (un prix), et la **classification**, quand c'est une catégorie
(pourriel ou non). Malgré leurs différences, tous deux carburent au même
signal — une cible fournie d'avance — et à la même mécanique : régler des
paramètres pour minimiser l'écart à cette cible.

Cette dépendance à des réponses toutes prêtes est la grande force du supervisé…
et son talon d'Achille. Car ces étiquettes, il faut bien que *quelqu'un* les
fournisse — souvent à la main, un exemple à la fois.

{{% hint info %}}
**Étiqueter les données : une industrie à part entière**

Derrière chaque modèle supervisé se cache une montagne de travail humain.
Quelqu'un a dû regarder des centaines de milliers d'images pour dire « ceci est
un chat », transcrire des heures d'audio, ou trancher « ce message est haineux,
celui-là non ». Cette tâche — l'**étiquetage** (ou *annotation*) des données —
est devenue un véritable secteur économique mondial : des plateformes comme
Amazon Mechanical Turk, ou des entreprises spécialisées telles Scale AI,
emploient des centaines de milliers de personnes, souvent dans des pays à bas
salaires, pour produire ces étiquettes une par une.

Ce travail est le plus souvent invisible, peu rémunéré, et parfois éprouvant —
pensez à la modération de contenus violents. Même les assistants les plus récents
en dépendent : une part de l'entraînement de ChatGPT repose sur des humains qui
notent et corrigent ses réponses (nous y reviendrons au Module 4). L'« intelligence »
de ces systèmes s'appuie ainsi sur un socle très humain — et soulève des questions
que nous retrouverons au Module 5.
{{% /hint %}}

Que faire, alors, quand personne n'a fourni ces réponses ?

## Apprendre sans réponses : le non-supervisé

Souvent, personne n'a fourni d'étiquettes. On dispose d'un grand tas de données
brutes — des clients, des photos, des textes — et rien d'autre : aucune « bonne
réponse » à imiter. Peut-on quand même apprendre quelque chose ? Oui, mais le but
change du tout au tout. Il ne s'agit plus de *prédire* une réponse donnée, mais
de **découvrir une structure** cachée dans les données elles-mêmes. C'est
l'apprentissage **non supervisé** : explorer un territoire sans carte, et en
dresser une.

La tâche la plus courante est le **regroupement** (ou *clustering*) : rassembler
les exemples qui se ressemblent. Et « se ressembler », nous savons déjà ce que ça
veut dire — c'est être **proches** dans l'espace des caractéristiques (page 40).
Regrouper, c'est donc repérer les amas naturels de points : les zones denses,
séparées par du vide.

L'algorithme classique pour cela s'appelle **k-means**. Son idée tient en une
image : pour organiser une fête, vous voulez répartir les invités autour de $k$
tables, en plaçant chaque table au centre de son petit groupe, pour que chacun
soit au plus près de la sienne. k-means fait exactement cela, par tâtonnements :

1. placer $k$ « centres » au hasard ;
2. rattacher chaque point au centre le plus proche (voilà les groupes provisoires) ;
3. déplacer chaque centre au milieu de son groupe ;
4. répéter les étapes 2 et 3 jusqu'à ce que plus rien ne bouge.

Essayez : dans l'applet, choisissez le nombre de groupes et regardez les centres
migrer, pas à pas, vers le cœur des amas.

{{< applet src="/html/applets/kmeans.html" >}}

Un point mérite qu'on s'y arrête. À première vue, ce résultat ressemble à de la
classification — des points répartis en groupes de couleurs. Mais la différence
est de fond : ici, **les points n'avaient aucune étiquette au départ.** Vous
n'avez pas dit à l'algorithme ce qu'était chaque groupe ; vous lui avez seulement
donné leur *nombre*, et il a inventé le reste. Il n'y a pas de « bonne réponse »
à retrouver — juste une structure à révéler.

Ce genre de méthode est partout : segmenter une clientèle en profils-types pour
le marketing, repérer une transaction anormale au milieu de millions d'autres
(détection de fraude), ou compresser des données en les résumant par leurs
groupes.

Et le regroupement n'est qu'une porte d'entrée. Le non-supervisé recouvre aussi
la **réduction de dimension** (simplifier des données à mille variables sans trop
perdre) et, plus profond encore, l'**apprentissage de représentations** :
découvrir *tout seul*, sans étiquettes, de bonnes caractéristiques pour décrire
les données. Cette idée — laisser la machine forger ses propres descripteurs — est
l'un des grands moteurs de l'IA moderne ; nous la retrouverons avec les
**autoencodeurs** (Module 3) et les **plongements** de mots (Module 4).

{{% details "Les mathématiques de k-means (optionnel)" %}}

k-means cherche à minimiser une fonction d'erreur, l'**inertie** (la somme des
carrés des distances de chaque point à son centre) :

$$J = \sum_{i=1}^{n} \min_{j=1}^{k} \lVert \mathbf{x}_i - \boldsymbol{\mu}_j \rVert^2$$

où $\mathbf{x}_i$ est le $i$-ème point et $\boldsymbol{\mu}_j$ le centre du groupe
$j$. Les deux étapes de l'algorithme alternent :

- **assignation** : chaque point rejoint le centre le plus proche,
  $c_i = \arg\min_j \lVert \mathbf{x}_i - \boldsymbol{\mu}_j \rVert^2$ ;
- **mise à jour** : chaque centre se replace à la moyenne de ses points,
  $\boldsymbol{\mu}_j = \frac{1}{n_j} \sum_{i : c_i = j} \mathbf{x}_i$.

On répète jusqu'à convergence. Deux remarques : le nombre de groupes $k$ est un
**hyper-paramètre** (on le choisit d'avance, comme le $k$ de kNN), et
l'algorithme peut se figer dans un minimum *local* — d'où l'usage de le relancer
plusieurs fois avec des centres initiaux différents, pour garder la meilleure
solution.

{{% /details %}}
