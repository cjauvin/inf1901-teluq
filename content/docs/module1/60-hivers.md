---
title: "Épisode 6 — Les hivers et la bascule"
weight: 60
slug: hivers-et-bascule
---

# Épisode 6 — Les hivers et la bascule

## Le premier hiver : la mort du perceptron (1969)

Souvenez-vous : à l'épisode 2, nous avions laissé le **perceptron** de Rosenblatt au
sommet de sa promesse — *une machine qui apprend de ses erreurs* —, salué par le *New
York Times* comme l'aube d'une intelligence électronique. Nous avions aussi annoncé
qu'un coup terrible l'attendait. Le voici.

En **1969**, deux poids lourds du camp symbolique — **Marvin Minsky**, l'un des pères
de Dartmouth, et son collègue **Seymour Papert** — publient un livre au titre sobre,
*Perceptrons*. Ce n'est pas un pamphlet, mais une analyse mathématique rigoureuse ; et
sa conclusion tombe comme un couperet. Le perceptron, démontrent-ils, est frappé d'une
limite de principe : il est incapable d'apprendre certaines fonctions d'une simplicité
pourtant dérisoire. L'exemple resté emblématique est le **XOR**, le « ou exclusif ».

Le XOR, c'est cette règle : *l'un ou l'autre, mais pas les deux à la fois*. Vous la
connaissez sans le savoir — c'est le principe du **va-et-vient**, ces deux interrupteurs
qui commandent une même lampe au bout d'un couloir. Basculez l'un *ou* l'autre, la
lumière change d'état ; les deux interrupteurs dans la même position, elle est éteinte ;
dans des positions opposées, elle s'allume. Deux entrées, une réponse qui dépend de leur
*désaccord*. Un enfant manie cela tous les jours. Or le perceptron, lui, ne peut pas
l'apprendre : aucun réglage de ses connexions ne lui permet de séparer d'un même trait
les cas « allumé » des cas « éteint ». Une tâche triviale, et pourtant hors de sa portée.

L'effet fut dévastateur. Minsky n'était pas n'importe qui : une autorité immense, et de
surcroît du camp adverse. Son verdict, mathématiquement imparable, fut reçu comme un
arrêt de mort. Les financements de la recherche sur les réseaux de neurones se tarirent
presque du jour au lendemain ; les revues se fermèrent, les étudiants se détournèrent.
Le camp connexionniste entra dans un long sommeil — un **hiver** d'une quinzaine
d'années. Rosenblatt lui-même n'en verrait pas la fin : il mourut en 1971, à
quarante-trois ans, dans un accident de bateau.

Ainsi, le premier hiver de l'IA ne frappa pas la tradition dominante, mais sa
**rivale** — et c'est un homme du camp symbolique qui, de fait, l'y plongea. En écartant
le connexionnisme, *Perceptrons* dégagea la scène : les vingt années suivantes seraient
celles du **règne symbolique** sans partage — la recherche, les systèmes experts, tout
l'âge d'or que nous venons de parcourir. Quand une tradition gèle, l'autre fleurit.

Un détail, pourtant, allait un jour tout changer. La démonstration de Minsky et Papert
ne valait que pour le perceptron le plus simple, fait d'une **seule couche**. On
pressentait qu'en **empilant les couches**, on franchirait l'obstacle du XOR — mais un
mystère restait entier : comment faire *apprendre* un tel empilement ? La réponse ne
viendrait qu'en 1986, et c'est par elle que le dégel commencerait. N'anticipons pas :
pour l'heure, c'est au tour du camp symbolique d'approcher de son propre hiver.

## Le second hiver : l'effondrement du symbolique (fin des années 1980)

L'âge d'or symbolique, on l'a vu, reposait sur une promesse vertigineuse : capturer
l'expertise humaine dans des règles. Mais les fissures de l'épisode 5 — le savoir
tacite qu'on n'extrait pas, la rigidité sans bon sens, les bases ingérables — finirent
par lézarder l'édifice tout entier. À mesure que les systèmes experts livrés
décevaient, l'écart se creusa entre ce qu'on avait *promis* aux investisseurs et ce que
l'IA *tenait*. Et quand un tel écart devient trop visible, l'argent s'en va.

Le symbole de la débâcle fut le **krach des machines Lisp**, vers 1987. Ces ordinateurs
spécialisés, taillés pour l'IA, coûtaient une fortune — et, presque du jour au
lendemain, de simples stations de travail bon marché, puis les ordinateurs personnels,
se mirent à faire aussi bien pour une fraction du prix. Le marché s'effondra ; les
entreprises qui en vivaient disparurent. Au même moment, l'ambitieux projet japonais de
**Cinquième Génération**, lancé en fanfare en 1982, s'acheminait vers une fin discrète,
sans avoir tenu aucune de ses grandes promesses.

Le découragement gagna tout le domaine. Les agences de financement, échaudées,
coupèrent les crédits ; « intelligence artificielle » devint une étiquette presque
honteuse, que les chercheurs évitaient désormais sur leurs demandes de subvention. On
parla, pour cette période, d'un second **hiver de l'IA** — le mot collait maintenant à
la peau du symbolique, comme il avait collé, vingt ans plus tôt, à celle du perceptron.
La leçon, au fond, était la même qu'aux épisodes 4 et 5 : le monde réel, têtu, résiste
à qui prétend l'enfermer dans des règles écrites à la main.

Et pourtant — c'est la grande ironie de notre histoire — pendant que le camp symbolique
sombrait, l'autre, qu'on croyait mort depuis 1969, **respirait de nouveau**. En 1986,
un petit groupe de chercheurs, parmi lesquels un certain **Geoffrey Hinton**, avait
fait paraître une méthode appelée **rétropropagation** : enfin un moyen de faire
*apprendre* les réseaux à **plusieurs couches** — ceux-là mêmes qui, on l'avait
pressenti, pouvaient venir à bout du XOR. Le verrou de *Perceptrons* sautait. Ce dégel
ne ferait pas de bruit tout de suite : il lui faudrait les **données** et la
**puissance de calcul** des années 2010 pour éclater au grand jour. Mais, une fois
encore, les deux traditions échangeaient leurs rôles — à l'hiver de l'une répondait le
printemps de l'autre.

## L'héritage invisible

Deux hivers coup sur coup : on serait tenté de refermer le dossier du GOFAI sur un
constat d'échec. Ce serait manquer l'essentiel. Car il existe, en intelligence
artificielle, un curieux phénomène que les chercheurs ont fini par nommer l'**« effet
IA »** : *dès qu'une technique se met à marcher pour de bon, on cesse de l'appeler
« intelligence artificielle » — elle devient « juste un algorithme ».* La formule la
plus ramassée revient à l'informaticien Larry Tesler, et c'est **Hofstadter** — encore
lui — qui l'a popularisée : *« l'IA, c'est tout ce qui n'a pas encore été fait. »*

Vu ainsi, le GOFAI n'est pas mort : il s'est **dissous** dans l'informatique de tous
les jours. Ses plus belles réussites sont devenues si banales, si fiables, qu'on a
oublié qu'elles sortaient des laboratoires d'IA. Suivons-en quatre à la trace — vous
les côtoyez sans doute chaque jour.

**La recherche dans un arbre** (épisode 3). Les algorithmes d'exploration — minimax,
A\* — qui faisaient gagner les machines aux échecs sont aujourd'hui partout : ce sont
eux qui calculent votre itinéraire **GPS** en une fraction de seconde, qui animent les
personnages des jeux vidéo, qui optimisent les tournées d'un transporteur ou les gestes
d'un robot. Personne, en suivant la flèche bleue sur son téléphone, ne songe qu'il fait
tourner de l'« intelligence artificielle » des années 1960.

**Les moteurs de règles** (épisode 5). Les systèmes experts n'ont pas disparu : ils ont
changé de nom. On les appelle « règles métier », et ils décident en silence de l'octroi
d'un prêt, du repérage d'une transaction frauduleuse, du calcul d'une prime
d'assurance. Les **configurateurs** qui, sur un site marchand, vérifient que les
options de votre voiture ou de votre ordinateur sont compatibles sont les enfants
directs de XCON. Et quand votre logiciel d'**impôts** vous guide de question en
question jusqu'au bon formulaire, il fait, à la lettre, le métier de MYCIN.

**Les idées de Lisp** (épisode 3). C'est peut-être l'héritage le plus profond. Le
langage de McCarthy a fait passer dans la programmation réelle tout un courant, la
**programmation fonctionnelle** : traiter les fonctions comme des valeurs (les
*lambdas*), enchaîner des opérations comme `map`, `filter`, `reduce`, manier des
*closures*. Ouvrez du code Python, JavaScript ou Java d'aujourd'hui : ces tournures,
devenues banales, sont nées dans les labos d'IA. Lisp y a aussi inventé des commodités
qu'on tient pour acquises — le **ramasse-miettes** (la gestion automatique de la
mémoire) et le **REPL**, cette console où l'on essaie son code à la volée. Détail
piquant : l'*autre* grande tradition fonctionnelle, celle des langages typés comme
Haskell, descend du langage **ML**, que Robin Milner avait créé pour faire tourner… un
**assistant de démonstration de théorèmes**. Les deux sources de la programmation
fonctionnelle moderne jaillissent donc, l'une comme l'autre, du raisonnement
symbolique.

**La représentation des connaissances** (épisode 4). Souvenez-vous des réseaux
sémantiques et des frames : on les avait dits promis à une descendance vivante. La
voici. Les **ontologies** et les **knowledge graphs** qui structurent le savoir du web
en sont les héritiers directs : quand Google affiche une fiche toute prête à côté de vos
résultats, quand on interroge Wikidata, c'est cette vieille idée — relier des concepts
par des liens *est-un*, *possède* — qui œuvre sous le capot. Quant aux frames, avec
leurs cases à valeurs par défaut et leurs hiérarchies d'héritage, ce sont les
**cousins**, du côté de l'IA, de l'**objet** de la programmation moderne : non pas son
ancêtre — l'orienté-objet doit plus à la simulation qu'à l'IA —, mais un jumeau né de
la même intuition. Une remarque, en passant, qui prépare le module 4 : tout ce savoir
est **structuré à la main**, patiemment, par des humains — à l'exact opposé de la façon
dont les grands modèles de langage, eux, *absorberont* le leur en avalant des océans de
texte. Deux philosophies du savoir que nous verrons bientôt s'affronter.

Quatre traces, et l'on pourrait en suivre d'autres. Aucune ne porte plus l'étiquette
« IA » : elles sont devenues l'air qu'on respire en informatique. C'est là le sort
secret du GOFAI — non pas une impasse, mais une **diaspora**. Ses idées ont quitté la
maison « intelligence artificielle » pour s'installer, anonymes et indispensables, au
cœur de la programmation ordinaire.

## La bascule

Reprenons le chemin parcouru. Tout est parti, à l'épisode 1, d'un pari de Turing :
*penser, c'est calculer*. De ce pari est née une famille d'idées — manipuler des
symboles selon des règles — qui a porté, trois décennies durant, des réussites
éclatantes : des machines qui démontrent des théorèmes, qui gagnent aux échecs, qui
dialoguent, qui représentent le monde, qui diagnostiquent comme des médecins. Le
programme symbolique fut tout sauf un échec : il a fondé l'informatique du raisonnement,
et nous en vivons encore.

Et pourtant, deux fois, il s'est cogné au même mur. À l'épisode 4, le **sens commun** :
cet océan d'évidences que personne ne pense à formuler, et qu'on ne peut donc pas
écrire. À l'épisode 5, le **goulot d'étranglement** : l'expertise qui se dérobe dès
qu'on veut la mettre en règles, parce qu'une grande part du savoir humain ne se dit pas.
Deux visages d'une seule et même leçon — celle, peut-être, que Hofstadter avait
pressentie le premier : *on n'inscrit pas l'intelligence de l'extérieur, fait après
fait ; le savoir qui compte est trop vaste, trop tacite, trop vivant pour tenir dans une
liste de règles.*

Si l'on ne peut pas *dicter* ce savoir à la machine, alors il faut qu'elle l'**acquière
elle-même**. Or l'idée n'était pas neuve : elle dormait depuis 1958 dans le perceptron
de Rosenblatt — *une machine qui apprend de ses erreurs* — que le camp symbolique avait
cru tuer en 1969. C'est ici que se dénoue le fil rouge tendu depuis l'épisode 2. Les
deux traditions, la symbolique et la connexionniste, ne se sont jamais succédé
proprement : elles ont coexisté en rivales, s'éclipsant tour à tour. L'hiver symbolique
de la fin des années 1980 n'est pas la fin de l'histoire — c'est l'instant où le
balancier, lentement, repart dans l'autre sens.

Une question, dès lors, va tout réorganiser — celle-là même que les déboires du GOFAI
avaient fini par faire surgir : *et si, plutôt que de dicter ses règles à la machine, on
la laissait les découvrir dans les données ?* Ce renversement a un nom :
l'**apprentissage automatique**, et c'est l'objet du **Module 2**. Quant à la vieille
tradition connexionniste, qu'on réveillera avec la rétropropagation et la puissance des
machines modernes, elle le portera, au **Module 3**, jusqu'à des sommets que ni Turing,
ni Rosenblatt, ni Minsky n'avaient osé imaginer. L'âge des règles s'achève ; celui de
l'apprentissage commence.
