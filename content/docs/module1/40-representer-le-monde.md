---
title: "Représenter le monde"
weight: 40
slug: representer-le-monde
---

# Représenter le monde

## Le sens, angle mort de la machine

Faisons le bilan des chapitres précédents. Le Logic Theorist démontrait des
théorèmes, Deep Blue gagnait aux échecs, ELIZA tenait la conversation — mais
tous, au fond, faisaient *la même chose* : **manipuler des symboles d'après leur
forme**, selon des règles. ELIZA repérait le mot « mère » sans avoir la moindre
idée de ce qu'est une mère. C'est ce qu'on appelle le niveau de la **syntaxe** :
agencer des symboles correctement, sans toucher à leur sens.

Or comprendre le monde demande bien davantage. Les spécialistes du langage
distinguent trois niveaux, qu'un seul petit exemple suffit à éclairer. Imaginez
qu'à table, quelqu'un vous dise : **« Pouvez-vous me passer le sel ? »**

- La **syntaxe**, c'est la *forme* : la phrase est une question grammaticalement
  bien construite. Une machine peut vérifier ça sans rien comprendre.
- La **sémantique**, c'est le *sens littéral* : la phrase interroge votre
  *capacité* à passer le sel. Pour y accéder, il faut savoir ce que veulent dire
  « sel », « passer », « pouvoir ».
- La **pragmatique**, c'est l'*intention réelle en contexte* : tout le monde
  comprend qu'il ne s'agit pas d'une question sur vos aptitudes, mais d'une
  **demande** polie — « passez-moi le sel ». Saisir cela exige du contexte et une
  montagne de sous-entendus que nous partageons tous.

Voilà le drame de l'IA symbolique résumé en une phrase : elle excellait au niveau
de la **syntaxe**, peinait à atteindre la **sémantique**, et se fracassait sur la
**pragmatique**. Car pour passer de la forme au sens, une machine a besoin de
quelque chose dont Deep Blue et ELIZA étaient totalement dépourvus : des
**connaissances** sur le monde. C'est le grand chantier de ce chapitre — et, on
le verra, sa grande déconvenue. Reste la question vertigineuse par laquelle tout
commence : comment loger dans une machine *ce que tout le monde sait* ?

## Donner un savoir à la machine

Si l'intelligence exige des connaissances, il faut trouver le moyen de les
**inscrire dans la machine** sous une forme qu'elle puisse exploiter. Entre la fin
des années 1960 et les années 1970, trois grandes idées s'imposent — trois façons
de structurer le savoir.

**Les réseaux sémantiques** (Ross Quillian). L'idée : représenter les
connaissances comme un **réseau de concepts reliés** par des relations. « Canari »
est relié à « oiseau » par un lien *est-un*, lui-même relié à « animal » ;
« oiseau » est relié à « ailes » par un lien *possède*. L'intérêt est que la
machine peut alors **déduire** ce qu'on ne lui a jamais dit explicitement : un
canari a-t-il des ailes ? Il suffit de suivre les flèches — *canari est-un
oiseau*, *oiseau possède ailes* — pour conclure que oui. (Notez que ces réseaux
portent le mot **sémantique** dans leur nom : c'est tout l'enjeu, passer de la
forme au *sens*.)

**Les frames, ou « cadres »** (Marvin Minsky, 1974). Plutôt que des concepts
isolés, Minsky propose de regrouper le savoir en **situations types** munies de
« cases » à remplir, avec des valeurs par défaut. Le cadre « chambre d'hôtel »
comporte des cases pour le lit, la porte, la salle de bain — et, par défaut, on
s'attend à y trouver un lit. Quand vous entrez dans une chambre d'hôtel inconnue,
vous n'analysez pas la scène de zéro : vous chargez ce cadre tout prêt, et vous ne
corrigez que ce qui détonne. C'est une manière de capturer nos **attentes**.

**Les scripts** (Roger Schank et Robert Abelson). Même idée, mais appliquée aux
**enchaînements d'actions**. Le « script du restaurant » décrit la séquence
attendue : entrer, s'asseoir, consulter le menu, commander, manger, payer, partir.
Grâce à lui, une machine peut **combler les trous** d'un récit : si on lui dit
« Jean est allé au restaurant et a commandé un steak », elle infère qu'il s'est
assis, qu'il a mangé, puis payé — bien que rien de tout cela n'ait été dit.

Le point commun de ces trois approches est ce qui faisait défaut à Deep Blue et à
ELIZA : la capacité à **inférer l'implicite**, à mobiliser un savoir de fond pour
aller au-delà de ce qui est littéralement énoncé. C'est un pas réel en direction
de la *sémantique*.

Ces représentations partagent d'ailleurs un ancêtre plus rigoureux : la **logique
formelle**, qui rêvait depuis Boole et Frege de réduire le raisonnement à un
*calcul* sur des symboles — « Socrate est un homme ; tous les hommes sont mortels ;
donc Socrate est mortel ». Le syllogisme a beau sembler relever du sens, il
s'obtient par pure mécanique sur la *forme* des énoncés. Et c'est là le fond du
problème : qu'on enchaîne des règles logiques ou qu'on suive des flèches dans un
réseau, on manipule toujours la **forme** des symboles. Reste à savoir si la forme
suffit à capturer le **sens** — ce pas vers la sémantique, on va le voir, traîne
avec lui une fragilité redoutable.

{{% hint info %}}
Ces façons de structurer le savoir — réseaux de concepts, cases à remplir,
hiérarchies *est-un* — pourraient sembler s'être éteintes avec le GOFAI. Il n'en est
rien : elles ont essaimé. Les **ontologies** et les **knowledge graphs** qui font
tourner la recherche de Google ou Wikidata en descendent en droite ligne, et les
*cases héritées* des frames ne sont pas sans rappeler les **objets** de la
programmation moderne. Nous y reviendrons dans « [Les hivers et la
bascule](docs/module1/60-hivers) », pour mesurer ce que le GOFAI a *vraiment* légué.
{{% /hint %}}

<!-- FIGURE À CRÉER (M1, ép. 4) : petit schéma du réseau sémantique canari→oiseau→animal + ailes/chanter. Repère laissé volontairement. -->

## SHRDLU, ou le sommet de l'ambition

C'est dans ce climat d'optimisme qu'un jeune chercheur du MIT, **Terry Winograd**,
réalise vers **1970** ce qui passe encore pour le sommet de l'IA symbolique :
**SHRDLU**. Le programme dialogue *en anglais ordinaire* avec un humain, à propos
d'un petit monde de **blocs colorés** — cubes, pyramides, boîtes posés sur une
table — qu'il peut déplacer à l'aide d'un bras robotique virtuel. Et la
conversation est, pour l'époque, stupéfiante :

> — *Prends un gros bloc rouge.*
> — D'accord.
> — *Saisis la pyramide.*
> — Je ne sais pas de **quelle** pyramide vous parlez.
> — *Trouve un bloc plus haut que celui que tu tiens et place-le dans la boîte.*
> — Par « **le** », je suppose que vous parlez du bloc plus haut que celui que je
>   tiens.

Regardez ce que SHRDLU réussit là. Il **lève une ambiguïté** (« quelle
pyramide ? »), il **résout un pronom** (à quoi renvoie « le » ?), il **agit** sur
le monde et il **se souvient** de ce qu'il vient de faire. Mieux : on peut lui
demander *« Pourquoi as-tu fait ça ? »* et il **explique** son raisonnement.

Comment fait-il ? Parce que, derrière le dialogue, SHRDLU entretient un **modèle du
monde** (*world model*) : une représentation interne de sa petite scène — quel bloc
repose sur quel autre, lequel est rouge, lequel est libre, ce que le bras tient à
l'instant. À chaque action, il **met ce modèle à jour** ; à chaque question, il le
**consulte**. C'est cette maquette intérieure qui lui permet de résoudre « le », de
se rappeler son geste passé, de justifier ce qu'il a fait. SHRDLU ne fait pas que
*parler* des blocs : il en tient, au-dedans de lui, une carte fidèle. Retenez bien
cette idée — **un modèle du monde est une représentation interne de la réalité, sur
laquelle on peut raisonner** ; nous la retrouverons, beaucoup plus loin dans le
cours, au cœur d'un grand débat sur les IA d'aujourd'hui.

Sauf que ce tour de force cache un **tour de passe-passe**. Si le modèle du monde de
SHRDLU est si fidèle, c'est qu'il n'a presque rien à représenter : une poignée de
blocs, une table, une boîte, quelques formes et couleurs. Dans cet univers de poche,
on *peut* tout dire à la machine — la liste complète des objets, des propriétés, des
actions possibles. Le « monde » de SHRDLU tient tout entier dans une représentation
**codée à la main**. Winograd l'avait d'ailleurs baptisé un **micro-monde** (*blocks
world*) — et le mot *micro* dit tout.

Que se passe-t-il si l'on sort de la table à blocs ? Rien. Le modèle du monde de
SHRDLU ne sait rien de la pluie, d'un mensonge ou d'un escalier ; il ne peut pas
*grandir* vers le monde réel, parce qu'il faudrait alors y faire entrer… tout. C'est
le sort commun de toutes les approches de ce chapitre : elles brillent tant qu'on
reste dans un domaine assez petit pour être entièrement décrit, et s'effondrent dès
qu'affleure l'immensité de ce que nous, humains, tenons pour évident. Cette immensité
a un nom, et c'est le mur sur lequel le GOFAI tout entier va se briser.

<!-- FIGURE À CRÉER (M1, ép. 4) : illustration du micro-monde de blocs de SHRDLU (cubes/pyramides/boîte sur une table). Candidat applet/interactif possible. -->

## Le mur du sens commun

Ce mur a un nom : le **sens commun**. C'est l'immense réservoir de choses si
évidentes que personne ne prend jamais la peine de les dire. Que l'eau mouille.
Qu'un objet lâché tombe. Qu'on ne peut pas pousser une corde. Que votre mère est
plus âgée que vous. Que si Jean entre dans un restaurant, il y entre par la porte
et non par le plafond. Nous mobilisons à chaque instant des millions de ces
certitudes muettes — et c'est précisément parce qu'elles vont **sans dire** que
personne ne les a jamais écrites nulle part.

Or toute l'IA symbolique repose sur un pari : pour qu'une machine sache, il faut
lui **inscrire** son savoir. Réseaux sémantiques, frames, scripts, SHRDLU — tous
fonctionnent tant que ce savoir tient dans un domaine assez petit pour être décrit
à la main. La machine ne sait que ce qu'on lui a explicitement fourni ; et le sens
commun, lui, **n'a pas de bord**. Pour le donner à une machine, il faudrait lui
fournir… le monde entier.

Un homme a pris ce défi au mot. En **1984**, **Douglas Lenat** lance **CYC** (de
l'anglais *encyclopedia*), une entreprise d'une ambition vertigineuse : **encoder à
la main**, fait après fait, règle après règle, la totalité du sens commun humain.
Des équipes ont passé des **décennies** et des dizaines de millions de dollars à
saisir patiemment des millions d'assertions — « un café chaud refroidit si on le
laisse », « on ne peut pas être à deux endroits à la fois »… Le projet le plus
héroïque, et le plus fou, de toute l'histoire du GOFAI.

Et il n'a jamais atteint son but. Non par manque d'argent ou de talent, mais parce
que la tâche est **sans fond** : pour chaque évidence saisie, dix autres surgissent,
et chacune en présuppose cent. On ne *remplit* pas le sens commun à la cuillère ; il
se dérobe à mesure qu'on l'écrit. CYC a buté, comme tout le reste de ce chapitre,
sur la même vérité — **le savoir implicite d'un humain ordinaire est trop vaste pour
être énuméré**.

C'est ici que le GOFAI plafonne. On avait cru qu'il suffisait de *donner* des
connaissances à la machine ; or les connaissances qui comptent vraiment sont
justement celles que personne ne formule. Et pourtant, à l'écart du courant
dominant, un trublion soutenait depuis longtemps qu'on s'y prenait à l'envers — qu'on
cherchait le sens là où il ne pouvait pas se trouver. Avant de quitter l'âge d'or
symbolique, il faut écouter cette voix dissidente.

## L'objection de Hofstadter

Cette voix, nous l'avons déjà entendue. Le trublion, c'est **Douglas Hofstadter** —
l'homme de la *boucle étrange*, croisé dès « [Turing et la question
fondatrice](docs/module1/10-turing) » à propos de Gödel.
Tandis que ses collègues bâtissaient des moteurs d'échecs et des bases de règles,
lui n'a cessé de répéter que l'IA dominante courait après la mauvaise proie. Battre
Kasparov par force brute, aligner des millions d'assertions à la manière de CYC :
pour Hofstadter, rien de tout cela ne touche au cœur de la pensée.

Ce cœur, selon lui, c'est l'**analogie**. Penser, ce n'est pas dérouler des règles :
c'est *percevoir des ressemblances*, plier des **concepts fluides** à des situations
neuves, comprendre l'inconnu à travers le déjà-connu. Quand vous parlez du *pied*
d'une montagne, des *jambes* d'une table ou de la *bouche* d'un fleuve, vous faites —
sans y penser — de l'analogie : l'opération la plus banale et la plus profonde de
l'esprit. Or une analogie ne se *liste* pas dans une base de connaissances ; elle se
*fabrique* à la volée, selon le contexte. C'est exactement ce que le rêve de CYC ne
pouvait pas capturer.

Pour le démontrer, Hofstadter et sa collaboratrice **Melanie Mitchell** ont conçu un
programme, **Copycat**, qui vit lui aussi dans un micro-monde — mais d'un genre tout
différent de celui de SHRDLU. Son univers : de simples **chaînes de lettres**. On lui
pose des énigmes d'analogie : *« si `abc` se change en `abd`, que devient `ijk` ? »*
La réponse naturelle est `ijl` — on a remplacé la dernière lettre par la suivante
dans l'alphabet. Facile. Mais Copycat n'applique pas une règle figée : il *perçoit*
une structure, et il peut en percevoir plusieurs. Demandez-lui ce que devient
**`xyz`** selon la même analogie, et tout se complique : le `z` n'a pas de lettre
suivante. Il n'y a plus de réponse unique — on peut défendre `xyd`, ou `wyz`, ou
repartir de l'autre bout de l'alphabet… Le « bon » résultat dépend de la *manière*
dont on voit la situation. Et c'est là tout le propos : l'intelligence n'est pas
l'exécution d'une règle, mais une **perception fluide, sensible au contexte**.

Voilà le renversement. SHRDLU, lui aussi, vivait dans un micro-monde — mais il
l'avait rapetissé pour **tricher** : un univers assez petit pour qu'on puisse tout y
énumérer d'avance. Hofstadter rapetisse le sien pour la raison **inverse** : écarter
tout le bric-à-brac du savoir encyclopédique afin d'**isoler l'essence**, l'acte
d'analogie à l'état pur. Deux micro-mondes, deux idées opposées de ce qu'est, au
fond, l'intelligence.

Reste la question qui hante tout ce chapitre : *comment du sens peut-il naître de
simples symboles ?* La réponse de Hofstadter prolonge sa **boucle étrange**. Le sens,
dit-il, ne s'**injecte** pas de l'extérieur, fait après fait, comme CYC l'espérait :
il **émerge** — d'un système assez riche pour se replier sur lui-même, percevoir ses
propres structures, faire analogie entre ses propres états. On ne *remplit* pas un
esprit de significations ; on met en place une mécanique d'où la signification
*jaillit*. C'est l'exact contraire de la démarche GOFAI, qui voulait tout écrire à la
main.

Hofstadter avait-il raison ? Oui et non. Sa **vision** a vu juste : on le verra,
c'est bien du côté de l'émergence — et non de l'inscription — que l'IA finira par
décoller. Mais sa **solution** n'a jamais atteint l'ampleur de son ambition : Copycat
est resté un petit programme de laboratoire, magnifique et confiné. Hofstadter
n'était pas non plus un homme des réseaux de neurones. Il a montré la bonne direction
sans construire le véhicule qui y mènerait.

Car ce véhicule existait déjà — en sommeil. Depuis « [Deux paris
rivaux](docs/module1/20-deux-paris) », une **autre
tradition** attend dans l'ombre : celle qui ne prétend pas *dire* le monde à la
machine, mais la laisse l'**apprendre** d'elle-même, à partir d'exemples. Le GOFAI
vient de se cogner à son plafond ; le sens commun lui a résisté ; et l'idée
d'émergence, soufflée par sa propre voix dissidente, pointe déjà vers la sortie. *Et
si, plutôt que de tout dire à la machine, on la laissait apprendre ?* Cette
question-là couve encore en silence ; il faudra un long hiver avant qu'elle ne
s'impose. Car l'âge d'or symbolique, lui, n'a pas dit son dernier mot : avant de
s'effondrer, il connaîtra son heure de gloire la plus éclatante.

{{% details "Pour aller plus loin : comment « pense » Copycat" %}}
Copycat ne contient aucune règle du genre « remplace la dernière lettre ». Il explore
en parallèle une multitude de petits rapprochements possibles — *cette lettre est-elle
un début ? une fin ? le successeur d'une autre ?* — qui se renforcent ou s'inhibent
mutuellement. Une mesure interne, que ses auteurs appellent la **« température »**,
indique à quel point une interprétation cohérente a émergé : tant que tout reste flou,
la température est haute et le programme continue d'explorer presque au hasard ; quand
une structure d'ensemble se cristallise, la température baisse et la réponse se fige.
Le sens n'y est donc pas *calculé* d'un trait, mais **gagné** peu à peu, par une
compétition de perceptions partielles — une image, à petite échelle, de ce que
Hofstadter tient pour le propre de la cognition.
{{% /details %}}

<!-- FIGURE/APPLET À CRÉER (M1, ép. 4) : énigme d'analogie de Copycat (abc→abd, ijk→? puis le cas xyz). Candidat applet interactif. -->

