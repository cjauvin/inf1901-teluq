---
title: "Classer"
weight: 60
slug: classer
---

# Classer

Le chapitre précédent nous a donné un vrai modèle qui apprend : une droite, deux
paramètres, une erreur à minimiser, une descente vers le creux. Mais il répond
toujours par un **nombre** — un prix. Or quantité de questions n'attendent pas un
nombre, plutôt une **catégorie** : ce courriel est-il un pourriel ? cette tumeur
est-elle bénigne ou maligne ? cette photo montre-t-elle un chat ou un chien ?
C'est la tâche de **classification**, déjà croisée au chapitre kNN — mais cette
fois, nous voulons un modèle qui *s'entraîne*.

Bonne nouvelle, annoncée en fin de chapitre : presque toute la machinerie va
resservir. Des paramètres réglables, une fonction d'erreur, une descente de
gradient pour la minimiser — ce trio est si général qu'il s'adapte aussi bien à
la classification qu'à la régression. Deux choses seulement changent : la
**forme** du modèle et la **façon de compter l'erreur**.

Pour la forme, le glissement est d'une simplicité élégante. En régression, la
droite *suivait* le nuage : elle passait *à travers* les points pour en épouser
la tendance. En classification, la droite *sépare* le nuage : elle passe *entre*
deux groupes pour les départager. Même objet — une droite, deux paramètres —
mais un rôle inversé.

{{< image src="/images/module2/suivre-vs-separer.svg" alt="Deux nuages de points côte à côte. À gauche, une droite traverse le nuage de maisons en suivant sa tendance : c'est la régression. À droite, une droite passe entre un groupe de points bleus et un groupe de points rouges pour les départager : c'est la classification." title="Deux usages de la même droite : à gauche elle suit le nuage (régression), à droite elle le sépare (classification)." loading="lazy" >}}

Pour fixer les idées, abandonnons un instant les maisons et imaginons le cas le
plus simple : des points de deux couleurs, `bleus` et `rouges`, dispersés dans
le plan (deux caractéristiques, $x_1$ et $x_2$). Apprendre à classer, ce sera
trouver la droite qui range le mieux les bleus d'un côté et les rouges de
l'autre. Et il y a, pour y arriver, deux grandes façons de penser — deux
philosophies que nous allons explorer tour à tour.

## Tracer une frontière : la régression logistique

La première façon de penser est la plus directe : si je veux séparer les bleus
des rouges, je n'ai qu'à **tracer la frontière** entre eux. Pas besoin de
comprendre ce qui distingue un bleu d'un rouge dans le fond — il me suffit de
trouver *où passe la ligne*. C'est l'approche dite **discriminative** : le modèle
apprend à discriminer les classes, sans chercher à les décrire.

Cette frontière, dans notre plan, c'est une droite — et nous savons déjà qu'une
droite tient en deux paramètres, une pente et une hauteur. Mais son rôle a
changé. En régression, on lisait la droite *verticalement* : à telle superficie,
tel prix. Ici, on la lit *latéralement* : de quel **côté** de la ligne tombe le
point ? D'un côté, on répond `bleu` ; de l'autre, `rouge`. La même équation,
$m x_1 + b$, ne sert plus à calculer une valeur mais à partager le plan en deux.

Cet algorithme porte un nom — la **régression logistique** — et, malgré ce nom
trompeur (il contient « régression » alors qu'il *classe*), c'est l'un des
classificateurs les plus utilisés au monde. Essayez-le : dans l'applet, déplacez
la ligne de décision pour séparer au mieux les deux groupes. Vous ajustez ainsi
ses deux paramètres à la main — exactement comme vous déplaciez la droite de
régression au chapitre précédent. Vous pouvez aussi ajouter, retirer ou déplacer
des points.

{{< applet src="/html/applets/logistic-regression.html" >}}

Et l'erreur ? C'est le second changement. On ne peut plus mesurer une « distance
verticale au point », puisqu'on ne prédit plus une valeur. Ce qu'on compte
désormais, c'est à quel point le modèle se **trompe de côté** : un point bien
rangé ne coûte rien, un point du mauvais côté coûte cher. La barre à droite de
l'applet affiche cette erreur. Cherchez à la rendre la plus petite possible —
idéalement zéro, quand la ligne sépare parfaitement les deux couleurs.

Vous remarquerez deux choses en jouant. D'abord, ce n'est **pas toujours
possible** d'atteindre zéro : si les couleurs se chevauchent, aucune droite ne
les sépare proprement. Ensuite, l'erreur ne dépasse jamais **50 %** : même la
pire ligne classe correctement la moitié des points par accident — et s'il fait
pire, le modèle n'a qu'à inverser sa convention (« ce côté-ci est rouge, pas
bleu ») pour repasser sous la barre.

{{% hint info %}}

Matière à réflexion : pourquoi n'est-il pas toujours possible de séparer
parfaitement les deux groupes par une droite ? Dans quelles conditions y
arrive-t-on ? Et qu'est-ce qui pourrait rendre la chose possible quand elle ne
l'est pas ? *(Nous y reviendrons : c'est l'une des grandes affaires du Module 3.)*

{{% /hint %}}

Reste la question de fond : comment la machine trouve-t-elle *seule* la bonne
ligne, sans qu'on la déplace à la souris ? La réponse ne vous surprendra pas —
c'est, mot pour mot, celle du chapitre précédent. L'erreur est une fonction des
deux paramètres ; cela dessine un paysage ; et la **descente de gradient** dévale
ce paysage jusqu'à son creux. Le même moteur, réutilisé tel quel. Seule la forme
de la fonction d'erreur diffère — pour ceux que les détails intéressent, les
voici.

{{% details "Les mathématiques de la régression logistique (optionnel)" %}}

Bien que nous en ayons parlé en termes purement géométriques, la régression
logistique est en réalité une méthode *probabiliste* : plutôt que de trancher
sèchement `bleu` ou `rouge`, elle estime la **probabilité** qu'un point soit
bleu. Un point loin de la frontière, du côté bleu, sera bleu « à 99 % » ; un
point juste sur la ligne, bleu « à 50 % » — l'hésitation maximale.

Pour transformer la position d'un point (une valeur quelconque) en une
probabilité (un nombre forcément entre 0 et 1), on emploie la **fonction
sigmoïde**, ou logistique — c'est elle qui donne son nom à l'algorithme. Sa
courbe en S écrase n'importe quelle valeur dans l'intervalle $[0, 1]$ :

![](/images/module2/Logistic-curve-02.png)

Adoptons la notation classique de l'apprentissage automatique. Un point est un
vecteur $\mathbf{x} = [x_1, x_2]$ ; sa vraie classe est $y \in \{0, 1\}$ (0 pour
rouge, 1 pour bleu, arbitrairement) ; les paramètres forment un vecteur
$\mathbf{w} = [w_1, w_2]$ accompagné de $b$. On calcule d'abord un **score** —
combien, et de quel côté, le point s'écarte de la frontière :

$$z = w_1 x_1 + w_2 x_2 + b$$

puis on le passe dans la sigmoïde pour obtenir la probabilité estimée :

$$\hat{y} = \frac{1}{1 + e^{-z}}$$

où $\hat{y} \in [0, 1]$ est une *probabilité*, à distinguer de $y \in \{0, 1\}$,
la *vraie* classe. La décision finale est alors : bleu si $\hat{y} \ge 0{,}5$,
rouge sinon.

L'erreur sur un point compare la probabilité prédite $\hat{y}$ à la vérité $y$.
On utilise l'**entropie croisée** :

$$E(y, \hat{y}) = -\big[\,y \log(\hat{y}) + (1 - y)\log(1 - \hat{y})\,\big]$$

Son comportement est exactement celui qu'on souhaite : si le point est bleu
($y = 1$) et que le modèle en est sûr ($\hat{y} = 0{,}9$), l'erreur est minime
($-\log 0{,}9 \approx 0{,}1$) ; mais s'il se trompe avec aplomb
($\hat{y} = 0{,}1$ pour un vrai bleu), l'erreur explose
($-\log 0{,}1 \approx 2{,}3$). La confiance mal placée est lourdement punie.

L'erreur totale, sur les $n$ points, en est la moyenne :

$$J(\mathbf{w}, b) = \frac{1}{n} \sum_{i=1}^{n} E\big(y^{(i)}, \hat{y}^{(i)}\big)$$

C'est cette fonction $J(\mathbf{w}, b)$ qui joue le rôle de « paysage » : à chaque
choix de paramètres, une hauteur d'erreur. La descente de gradient en mesure la
pente,

$$\frac{\partial J}{\partial \mathbf{w}} = \frac{1}{n} \sum_{i=1}^n \big(\hat{y}^{(i)} - y^{(i)}\big)\,\mathbf{x}^{(i)}, \qquad \frac{\partial J}{\partial b} = \frac{1}{n} \sum_{i=1}^n \big(\hat{y}^{(i)} - y^{(i)}\big)$$

et fait un pas en sens inverse, d'une taille réglée par le taux d'apprentissage
$\alpha$ :

$$\mathbf{w} \leftarrow \mathbf{w} - \alpha\,\frac{\partial J}{\partial \mathbf{w}}, \qquad b \leftarrow b - \alpha\,\frac{\partial J}{\partial b}$$

On répète jusqu'à ce que l'erreur ne diminue plus. C'est, trait pour trait, la
mécanique du chapitre précédent — seule la fonction d'erreur a changé de visage.

{{% /details %}}

## Renverser le problème : la classification bayésienne

La seconde façon de penser prend le problème par l'autre bout. Plutôt que de
tracer d'emblée la frontière, elle commence par **décrire chaque classe**. À quoi
ressemble un point bleu, typiquement ? Et un rouge ? Si je dispose d'un bon
portrait de chacun, je peux classer un nouveau point en demandant simplement :
*ressemble-t-il davantage à un bleu ou à un rouge ?*

{{< image src="/images/module2/qui-je-ressemble.svg" alt="Deux nuages de points, l'un bleu, l'autre rouge, chacun entouré d'un halo qui figure son « portrait » (sa répartition). Un point neuf, posé entre les deux, demande : à qui je ressemble le plus ? On le compare à chaque portrait pour décider de sa classe." title="L'approche générative : on décrit le « portrait » de chaque classe, puis on demande auquel le nouveau point ressemble le plus." loading="lazy" >}}

C'est l'approche dite **générative**, et le mot mérite qu'on s'y arrête. Décrire
une classe assez finement pour reconnaître ses membres, c'est aussi savoir, en
principe, en *fabriquer* de nouveaux : un modèle qui connaît le portrait-robot du
« bleu typique » pourrait inventer des bleus plausibles qu'il n'a jamais vus.
D'où *génératif* — il pourrait générer des données, pas seulement les trancher.
Retenez cette idée : elle paraît modeste ici, mais c'est elle qui, poussée à
l'extrême, donnera plus tard l'IA *générative* — celle qui produit textes et
images (Module 4).

Comment dresse-t-on le portrait d'une classe ? En décrivant **comment ses points
se répartissent** le long de chaque caractéristique. Les maisons bleues se
concentrent-elles autour de telle valeur de $x_1$ ? Les rouges, plus haut ? Cette
répartition se résume par une courbe familière, la fameuse **courbe en cloche**
(ou *gaussienne*) : un sommet là où les points sont denses, des bords qui
s'amincissent là où ils se raréfient. Un portrait de classe, c'est une poignée de
ces cloches — une par caractéristique.

Pour garder le calcul simple, on fait une hypothèse délibérément grossière : on
traite **chaque caractéristique séparément**, comme si elles étaient
indépendantes. C'est rarement tout à fait vrai (la superficie et le nombre de
pièces, par exemple, vont de pair), et c'est précisément ce que veut dire le mot
**naïve** dans le nom de la méthode. Naïve, mais redoutablement efficace en
pratique.

Reste alors un dernier tour de passe-passe. Nos portraits répondent à la
question : « *si* ce point est bleu, à quel point est-il typique ? » — autrement
dit, la probabilité du point *sachant* la classe. Mais ce qu'on veut, c'est
l'inverse : « ce point étant donné, quelle est la probabilité qu'il soit bleu ? »
Renverser ainsi le conditionnement — passer de *probabilité du point sachant la
classe* à *probabilité de la classe sachant le point* — est exactement ce que
permet un résultat fondamental des probabilités, le **théorème de Bayes**. C'est
lui qui donne son nom à la méthode, la **classification bayésienne naïve**.

Voilà donc deux routes vers le même but :

| | **Régression logistique** | **Bayes naïf** |
|---|---|---|
| Philosophie | **discriminative** | **générative** |
| Stratégie | tracer la frontière | décrire chaque classe |
| Question posée | *de quel côté ?* | *à quel portrait ressemble-t-il le plus ?* |
| Bonus | — | pourrait *générer* de nouveaux exemples |

Fait remarquable : sur nos données en deux dimensions, ces deux chemins si
différents aboutissent à la **même forme de frontière** — une droite. Mais la
distinction entre apprendre à *séparer* et apprendre à *décrire* est l'une des
plus profondes de tout le domaine. Nous la retrouverons, en grand, au Module 4 :
les modèles qui *classent* d'un côté, ceux qui *engendrent* du contenu de
l'autre.

{{% details "Les mathématiques de la classification bayésienne naïve (optionnel)" %}}

Chaque couple **caractéristique + classe** est modélisé par une gaussienne à une
dimension — soit, sur nos deux caractéristiques et nos deux classes, quatre
cloches en tout. La gaussienne (ou loi normale) décrit comment la « masse de
probabilité » se répartit autour d'une valeur centrale, la moyenne :

![](/images/module2/gaussian.png)

Un point subtil : la hauteur de la courbe en un endroit n'est *pas* la
probabilité de ce point. Comme la courbe est continue, une probabilité
correspond à une **aire** sous la courbe (entre deux bornes) ; l'aire totale vaut
1, et l'aire à gauche de la moyenne vaut donc 0,5.

Concrètement, on projette d'abord les points sur l'axe $x_1$, ce qui les rend
unidimensionnels…

![](/images/module2/nb_x1_proj.png)

…puis on ajuste une cloche par classe, dont la largeur épouse la dispersion des
points projetés :

![](/images/module2/nb_x1_gauss.png)

et on recommence sur l'axe $x_2$ :

![](/images/module2/nb_x2_proj.png)

![](/images/module2/nb_x2_gauss.png)

On dispose alors de quatre modèles $p(x_j \mid \text{classe})$. La moyenne $\mu$
et l'écart-type $\sigma$ de chaque cloche s'obtiennent **directement** par un
simple calcul de moyenne et de dispersion sur les points concernés — pas besoin,
ici, de descente de gradient itérative :

$$\hat\mu_{j,c} = \frac{1}{N_c}\sum_{i \in c} x_{ij}, \qquad \hat\sigma^2_{j,c} = \frac{1}{N_c}\sum_{i \in c} \big(x_{ij} - \hat\mu_{j,c}\big)^2$$

L'hypothèse *naïve* d'indépendance permet de combiner les caractéristiques par
simple multiplication :

$$p(\mathbf{x} \mid c) = p(x_1 \mid c)\,\cdot\,p(x_2 \mid c)$$

Ce modèle est *génératif* : il décrit la probabilité d'un point $\mathbf{x}$
*sachant* sa classe, $P(\mathbf{x} \mid y)$. Mais la classification réclame
l'inverse, $P(y \mid \mathbf{x})$. Le **théorème de Bayes** opère le
renversement :

$$P(y \mid \mathbf{x}) = \frac{P(\mathbf{x} \mid y)\,P(y)}{P(\mathbf{x})}$$

où $P(y)$ est la proportion de chaque classe (souvent 50/50 si les données sont
équilibrées). Comme le dénominateur $P(\mathbf{x})$ ne dépend pas de la classe,
on peut l'ignorer pour décider :

$$\text{classe}(\mathbf{x}) = \begin{cases} \mathtt{rouge} & \text{si } P(\mathbf{x}\mid\text{rouge})\,P(\text{rouge}) \ge P(\mathbf{x}\mid\text{bleu})\,P(\text{bleu}) \\ \mathtt{bleu} & \text{sinon} \end{cases}$$

On compare donc, pour le point observé, lequel des deux portraits le rend le plus
**vraisemblable** — et c'est le portrait gagnant qui donne la classe.

{{% /details %}}
