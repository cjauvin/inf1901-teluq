---
title: "L'âge d'or symbolique : chercher et raisonner"
weight: 30
slug: chercher-raisonner
---

# L'âge d'or symbolique : chercher et raisonner

## Résoudre, c'est explorer

Une fois le pari symbolique posé, une question pratique se pose : par où commencer
pour faire *raisonner* une machine ? Les pionniers de l'IA trouvent une réponse
d'une grande puissance, parce qu'elle s'applique à une foule de problèmes très
différents. L'idée : presque tout problème peut se reformuler comme
l'**exploration d'un espace de possibilités**.

Prenons un labyrinthe. À chaque instant, vous êtes dans une certaine position —
appelons ça un **état**. À partir de cet état, quelques actions s'offrent à vous
(avancer, tourner à gauche, à droite), et chacune vous mène à un nouvel état. De
proche en proche, l'ensemble de tous les états atteignables forme une sorte
d'arborescence géante : l'**espace d'états**. Résoudre le labyrinthe, ce n'est
alors rien d'autre que **trouver un chemin** dans cette arborescence, depuis
l'état de départ jusqu'à l'état-but (la sortie).

Ce qui rend l'idée si féconde, c'est qu'une multitude de problèmes en apparence
sans rapport prennent soudain la *même forme*. Le casse-tête du taquin (ces
petites tuiles numérotées qu'on fait glisser), une partie d'échecs, la
planification d'un itinéraire, la démonstration d'un théorème : dans chaque cas,
on a un état de départ, des actions qui font passer d'un état à un autre, un but
à atteindre — et résoudre revient à **chercher un chemin** vers ce but. Newell et
Simon, les auteurs du Logic Theorist, pousseront l'idée jusqu'à bâtir un
programme au nom révélateur, le *General Problem Solver* (« solutionneur général
de problèmes »), censé attaquer n'importe quel problème exprimé sous cette forme.

Retenez ce verbe — **chercher** —, car il est bien plus qu'une technique parmi
d'autres : c'est la *signature* de toute l'IA symbolique. Démontrer un théorème,
planifier un trajet, diagnostiquer une panne, lever l'ambiguïté d'une phrase :
sous le capot, le GOFAI ramène presque tout à une seule et même opération —
*explorer un espace de possibilités jusqu'à y trouver une solution*. Nous le
reverrons à l'œuvre dans les chapitres suivants. Et, tout à la fin du module,
c'est précisément ce verbe qui tracera la ligne de partage avec la tradition
rivale : là où le symbolique *cherche*, l'autre, un jour, *apprendra*.

## L'explosion combinatoire

L'idée d'explorer un arbre de possibilités est séduisante… mais elle se heurte
vite à un mur. Pour la plupart des problèmes intéressants, cet arbre est d'une
taille **proprement astronomique**.

Les échecs en sont l'exemple emblématique. À chaque tour, un joueur dispose en
moyenne d'une trentaine de coups possibles ; chacun ouvre une trentaine de
réponses adverses, et ainsi de suite. Regarder seulement quelques coups à
l'avance fait déjà exploser le nombre de branches à examiner. Si l'on voulait
dérouler *toutes* les parties d'échecs possibles, on obtiendrait un nombre si
grand — le **nombre de Shannon**, environ un 1 suivi de 120 zéros — qu'il dépasse
de très loin le nombre d'atomes dans l'univers observable. Aucune machine, si
rapide soit-elle, ne pourra jamais explorer un tel espace en entier.

Pour les jeux à deux adversaires, les chercheurs mettent au point une stratégie
élégante, le **minimax**. L'idée : la machine explore l'arbre des coups en
supposant que son adversaire jouera toujours du mieux possible. À chaque étape,
elle cherche à *maximiser* son avantage, tout en tenant pour acquis que
l'adversaire cherchera, lui, à le *minimiser* — d'où le nom. En remontant les
conséquences de chaque coup, elle choisit celui qui lui garantit le meilleur sort
dans le pire des cas.

Mais comme l'arbre reste trop grand pour être exploré jusqu'au bout, il faut
**ruser**. Plutôt que d'aller jusqu'aux fins de partie, la machine s'arrête à une
certaine profondeur et *estime* la qualité d'une position à l'aide d'une **règle
empirique** (une « heuristique ») : compter les pièces, évaluer le contrôle du
centre, etc. D'autres astuces, comme l'**élagage** (ignorer d'emblée les branches
qui ne peuvent pas changer la décision), évitent d'explorer inutilement.

La même ruse vaut hors des jeux, lorsqu'il s'agit de **trouver un chemin** — par
exemple notre labyrinthe du début, ou le calcul d'un itinéraire routier. Plutôt
que d'explorer aveuglément dans toutes les directions, un algorithme célèbre
nommé **A\*** (prononcé « A étoile ») se laisse guider par une heuristique : à
chaque embranchement, il privilégie la direction qui *semble* se rapprocher le
plus du but (par exemple, la distance à vol d'oiseau jusqu'à la destination). Le
GPS qui vous calcule une route emprunte, au fond, ce genre de stratégie. La leçon
profonde de tout l'âge d'or est là : être intelligent, ce n'est pas tout explorer
— c'est explorer **au bon endroit**. Tout l'art réside dans la qualité des
heuristiques.

<!-- APPLET À CRÉER (M1, ép. 3) : arbre de jeu minimax interactif, ou A* sur une grille. Repère laissé volontairement ; voir PLAN-v2.md §5 (interactivité M1). -->

## L'apogée : Deep Blue bat Kasparov (1997)

En mai 1997, à New York, se joue un match devenu légendaire. D'un côté, **Garry
Kasparov**, champion du monde d'échecs en titre, considéré par beaucoup comme le
plus grand joueur de l'histoire. De l'autre, **Deep Blue**, un superordinateur
conçu par IBM. Au terme de six parties, la machine l'emporte. Pour la première
fois, un champion du monde en exercice s'incline face à un ordinateur dans un
match en conditions officielles. Le retentissement est mondial : la presse y voit
le jour où la machine a « dépassé » l'humain.

Deep Blue est l'aboutissement direct de tout ce que nous venons de décrire. Aucun
réseau de neurones, aucun apprentissage : seulement de la **recherche par force
brute** — la machine évalue jusqu'à 200 millions de positions par seconde —
guidée par des **heuristiques** affinées avec l'aide de grands maîtres, et
appuyée sur d'immenses bibliothèques d'ouvertures et de fins de partie. C'est du
GOFAI à l'état pur, porté à son sommet par la puissance de calcul.

Le match lui-même fut tendu et théâtral. Déstabilisé par un coup étrangement
subtil de la machine en début de rencontre — trop « humain » à son goût —,
Kasparov en vint à soupçonner une intervention humaine et accusa IBM de
tricherie. Il réclama une revanche que l'entreprise lui refusa, démontant Deep
Blue dans la foulée. L'ironie est savoureuse : ce coup déroutant aurait en réalité
résulté d'un simple bogue dans le programme.

Mais au-delà de l'anecdote, la victoire laisse un goût étrange, et relance
aussitôt *la* question. Car Deep Blue ne « comprend » pas les échecs comme
Kasparov les comprend. Il ne sait même pas qu'il joue aux échecs ; il ne ressent
ni la beauté d'une combinaison ni la tension d'une partie ; il ne saurait rien
faire d'autre, pas même expliquer pourquoi il a joué tel coup. Est-ce alors de
l'*intelligence*, ou une prodigieuse machine à calculer déguisée en joueur
d'échecs ?

{{% hint info %}}
Le cas Deep Blue illustre une ironie qui traverse toute l'histoire de l'IA : les
tâches que nous jugeons les plus « intellectuelles » (jouer aux échecs, démontrer
un théorème) se sont révélées **relativement faciles** à mécaniser, tandis que ce
qu'un enfant de trois ans fait sans effort — comprendre une phrase, reconnaître
une scène, exercer son bon sens — a longtemps résisté. Nous touchons là au
**paradoxe de Moravec**, sur lequel nous reviendrons.
{{% /hint %}}

Cette résistance dessine déjà les limites de l'âge d'or, sur lesquelles nous
reviendrons. Mais la même époque nous réserve une tout autre histoire — non plus
une machine qui *calcule* pour gagner, mais une qui semble *parler* et écouter.
Et elle est, à sa façon, encore plus déroutante.

## L'autre visage : ELIZA, ou l'illusion de comprendre

L'âge d'or symbolique ne fut pas que recherche et calcul. Un de ses moments les
plus marquants — et les plus troublants — concerne une machine qui semblait, non
pas *jouer*, mais *parler*. En 1966, au MIT, l'informaticien **Joseph
Weizenbaum** écrit **ELIZA**, un programme qui imite un psychothérapeute. La
conversation paraît étonnamment naturelle : vous tapez « je me sens seul ces
temps-ci », ELIZA répond « depuis quand vous sentez-vous seul ? ».

Pourtant, sous le capot, il n'y a *aucune compréhension*. ELIZA se contente de
repérer des mots-clés et de **renvoyer les phrases de l'utilisateur sous forme de
questions**, selon une poignée de règles toutes simples. Dites « ma mère ne
m'écoute jamais » et le mot « mère » déclenche « parlez-moi de votre famille ».
C'est un tour de passe-passe, sans le moindre savoir sur le monde, sur la
solitude ou sur les mères.

Le plus fascinant est ce qui se produisit alors. Les gens s'attachèrent à ELIZA.
La propre secrétaire de Weizenbaum, qui savait pourtant pertinemment qu'il
s'agissait d'un programme, lui demanda un jour de quitter la pièce pour pouvoir
« parler en privé » avec la machine. Des utilisateurs lui confièrent leurs
tourments intimes, persuadés d'être écoutés. Weizenbaum en fut si troublé qu'il
devint l'un des grands critiques de l'IA. On appelle aujourd'hui **« effet
ELIZA »** cette tendance puissante que nous avons à *projeter* de la
compréhension, voire des émotions, sur la moindre machine qui manie le langage.

ELIZA est en quelque sorte le négatif du test de Turing : elle montre à quel
point il peut être *facile* de donner l'illusion de penser sans rien comprendre
du tout. C'est une mise en garde dont nous mesurerons toute la portée à l'ère des
agents conversationnels (module 4) et dans le débat, jamais clos, sur ce que
« comprendre » veut dire pour une machine (module 5).

**Un mot sur l'outil.** ELIZA, comme la quasi-totalité des programmes de l'âge
d'or, était écrite en **Lisp**, un langage inventé par John McCarthy en 1958 —
l'année même du perceptron. C'est l'un des plus anciens langages de programmation
encore vivants aujourd'hui, et il a profondément marqué l'informatique (la
récursion, le ramasse-miettes de mémoire, l'invite interactive… nombre d'idées
qu'on tient pour acquises y sont nées). Son nom dit déjà beaucoup : *Lisp* pour
*LISt Processing*, le « traitement de listes ». Là où la plupart des langages
sont d'abord pensés pour calculer des nombres, Lisp est taillé pour **manipuler
des symboles** — des mots, des concepts, des relations —, ce qui en faisait
l'outil rêvé du pari symbolique.

{{% details "Pour aller plus loin : à quoi ressemble du Lisp ?" %}}
En Lisp, à peu près *tout* s'écrit sous forme de listes entre parenthèses, avec
l'opération placée en tête. Une addition s'écrit ainsi :

```lisp
(+ 1 2 3)      ; vaut 6
(* 3 (+ 2 4))  ; vaut 18, soit 3 × (2 + 4)
```

Rien d'extraordinaire jusqu'ici. Mais voici l'idée féconde : une liste peut tout
aussi bien contenir des *symboles* (des mots) que des nombres. On peut écrire une
liste de concepts…

```lisp
(chien chat oiseau)
```

…ou même représenter une connaissance, un fait sur le monde :

```lisp
(est-un Socrate humain)   ; « Socrate est un humain »
```

Le point crucial est que, en Lisp, **un programme a exactement la même forme que
les données qu'il manipule** : dans les deux cas, des listes. Un programme peut
donc lire, transformer et même *fabriquer* d'autres programmes aussi aisément
qu'il manie une liste d'épicerie. Cette propriété — « le code est une donnée
comme une autre » — est précisément ce qui rendait Lisp si naturel pour bâtir des
systèmes censés *raisonner* sur des symboles.
{{% /details %}}

Pendant des décennies, Lisp resta la langue maternelle de l'IA symbolique. On
construisit même des ordinateurs spécialisés, les **« machines Lisp »**, pour le
faire tourner au mieux. Nous recroiserons leur effondrement, vers 1987, dans
« [Les hivers et la bascule](docs/module1/60-hivers) » : il y marquera l'un des
hivers de l'IA.

Deep Blue *cherchait*, ELIZA *bricolait du langage* — mais ni l'un ni l'autre ne
*connaissait* véritablement le monde. Pour aller plus loin, il fallait doter la
machine de quelque chose qui lui manquait cruellement : une façon de
**représenter ce qu'elle sait**. C'est le grand chantier — et la grande
déconvenue — de « [Représenter le monde](docs/module1/40-representer-le-monde) ».

