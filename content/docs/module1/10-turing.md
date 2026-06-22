---
title: "Épisode 1 — Turing et la question fondatrice (1950)"
weight: 10
slug: turing
---

# Épisode 1 — Turing et la question fondatrice (1950)

## Le moment

Nous sommes en 1950. La Seconde Guerre mondiale vient de s'achever, et le
mathématicien britannique **Alan Turing** publie un article au titre d'apparence
anodine : *Computing Machinery and Intelligence*. Il s'ouvre sur une question qui
allait hanter tout un domaine pour les décennies à venir :

> *« Les machines peuvent-elles penser ? »*

Turing n'est pas un inconnu. Pendant la guerre, il a joué un rôle décisif dans le
décryptage des communications de la machine **Enigma** des armées allemandes, en
concevant des dispositifs électromécaniques capables d'explorer mécaniquement des
millions de combinaisons — un effort longtemps resté secret, dont les historiens
estiment qu'il a pu écourter le conflit de plusieurs années. Turing sait donc,
mieux que quiconque à son époque, qu'une machine peut accomplir des tâches qu'on
croyait réservées à l'esprit humain. Mais une machine qui *déchiffre* est-elle
une machine qui *pense* ? C'est tout l'objet de son article.

## Le jeu de l'imitation

Turing comprend tout de suite que sa question — « les machines peuvent-elles
penser ? » — est un piège : elle dépend entièrement de ce qu'on accepte d'appeler
« penser », un mot qu'on n'arrive même pas à définir clairement pour les humains.
Plutôt que de s'enliser dans ce débat, il fait un coup de génie : il **remplace
la question par une autre**, qu'on peut réellement trancher.

À la place de « une machine peut-elle penser ? », il propose une épreuve
concrète, le **jeu de l'imitation** — ce qu'on appelle aujourd'hui le **test de
Turing**. Imaginez un juge humain qui dialogue par écrit avec deux interlocuteurs
cachés : un être humain et une machine. Les messages passent par clavier, pour
qu'aucune voix ni aucun visage ne trahisse qui est qui. Le juge peut poser
n'importe quelle question — sur la météo, la poésie, l'arithmétique, ses
souvenirs d'enfance. Sa tâche : deviner lequel des deux est la machine. Si, au
fil de nombreuses parties, la machine parvient à se faire passer pour un humain
aussi souvent qu'un humain lui-même y parvient, alors, dit Turing, il n'y aura
plus de raison sérieuse de lui refuser le qualificatif de « pensante ».

L'astuce est autant philosophique que technique : Turing **déplace la question de
l'intériorité vers le comportement**. Peu importe ce qui se passe « à l'intérieur »
de la machine, ou si elle « ressent » quoi que ce soit ; ce qui compte, c'est ce
qu'elle est capable de *faire*. C'est précisément ce déplacement qui soulève une
question de fond, que les philosophes débattent encore aujourd'hui :

{{% details "Au fond, qu'est-ce qui ferait qu'une machine « pense » vraiment ?" %}}
La proposition de Turing s'inscrit dans l'air du temps de 1950, dominé par le
**behaviorisme** : ce courant de la psychologie soutenait qu'on ne fait pas de
science avec ce qui se passe « dans la tête » — invisible et invérifiable — mais
seulement avec le **comportement observable**. Juger la machine sur ses réponses
plutôt que sur sa vie intérieure, c'est tout à fait dans cet esprit. Mais une
thèse plus précise allait bientôt donner au rêve de l'IA sa véritable assise
philosophique : le **fonctionnalisme**. Son idée : un état mental n'est pas
défini par la *matière* qui le produit, mais par le *rôle* qu'il joue — ses
causes et ses effets. La douleur, par exemple, c'est « ce qui est causé par une
blessure et qui cause le retrait et la plainte », peu importe que ce soit réalisé
par des neurones humains, le système nerveux d'un poulpe... ou les circuits d'un
ordinateur. Vu sous cet angle, la frontière entre l'esprit et la machine devient
poreuse dans les deux sens : non seulement un ordinateur pourrait penser, mais
**notre propre cerveau peut être vu comme une sorte d'« ordinateur biologique »**
— un support de chair qui réalise, lui aussi, une certaine organisation. Si
l'esprit est une *organisation* et non une *substance*, alors rien n'interdit
qu'il tourne sur du silicium comme il tourne sur des neurones : c'est exactement
le permis qui autorise à prendre l'IA au sérieux. Nous retrouverons cette idée —
et sa contestation la plus célèbre, la *Chambre chinoise* du philosophe John
Searle — au Module 5.
{{% /details %}}

{{% hint warning %}}
Le test de Turing est souvent mal compris. Ce n'est **pas** un test de
conscience, ni une définition de l'intelligence au sens large. C'est une
proposition *pragmatique* : *si* on ne peut plus distinguer la machine de
l'humain en conversation, *alors* s'acharner à savoir si elle « pense vraiment »
devient un débat sans issue. C'est une façon de contourner une question
insoluble, pas de la résoudre.
{{% /hint %}}

## La pensée comme calcul

Derrière le test se cache une intuition beaucoup plus profonde, et c'est elle le
véritable héritage de Turing pour l'IA. Dès 1936, bien avant son article sur le
jeu de l'imitation, Turing avait inventé un objet mathématique qu'on appelle
aujourd'hui la **machine de Turing** : un dispositif imaginaire, d'une simplicité
presque dérisoire, qui se contente de lire et d'écrire des symboles sur un ruban
en suivant un jeu de règles fixes.

Son résultat est stupéfiant : ce mécanisme élémentaire peut, en principe,
**calculer tout ce qui est calculable**. En fait, la machine de Turing donne une
définition précise à une notion qu'on emploie tous les jours sans jamais la
définir : celle d'**algorithme**. Un algorithme, c'est une recette finie d'étapes
sans ambiguïté ; et l'on admet que tout ce qu'un algorithme peut accomplir, une
machine de Turing peut l'accomplir aussi — et réciproquement. « Algorithme »,
« machine de Turing » et « ce qui est calculable » désignent ainsi, au fond, une
seule et même chose. Mieux encore : il existe une *machine universelle*, capable
d'imiter n'importe quelle autre machine, simplement en recevant sa description en
entrée. C'est exactement le principe de l'ordinateur moderne : un seul appareil
physique qui, selon le programme qu'on lui fournit, devient traitement de texte,
jeu vidéo ou calculatrice. Votre téléphone est, à ce titre, une machine
universelle de Turing.

On tient là le **pari implicite** que Turing lègue aux fondateurs de l'IA : *si*
penser n'est qu'une forme de calcul — manipuler des symboles selon des règles —
*et si* une machine peut tout calculer, *alors* une machine devrait pouvoir
penser. Tout le programme de recherche des décennies suivantes, que nous allons
suivre dans ce module, découle de ce raisonnement. Reste une question que Turing
laisse ouverte, et qui fera tout le drame de la suite : *est-il vraiment vrai que
penser se réduit à calculer ?*

{{% details "Pour aller plus loin : qu'est-ce qu'une machine de Turing, concrètement ?" %}}
Imaginez un ruban de papier infini divisé en cases, une tête qui se déplace le
long du ruban en lisant et en écrivant un symbole à la fois, et une petite table
de règles du genre : « si je suis dans l'état A et que je lis un `0`, alors
j'écris un `1`, je me déplace d'une case vers la droite et je passe à l'état B ».
C'est tout. Aucune mémoire géante, aucune intelligence cachée : juste des
symboles, des règles et un état courant. Ce qui est vertigineux, c'est que ce
mécanisme minimaliste suffit à exprimer n'importe quel calcul réalisable par
n'importe quel ordinateur, aussi puissant soit-il. La machine de Turing ne sert
pas à calculer *vite* ; elle sert à définir, une fois pour toutes, *ce que
« calculer » veut dire*. L'idée que tout procédé de calcul imaginable se ramène à
une machine de Turing porte d'ailleurs un nom : la **thèse de Church-Turing**.
{{% /details %}}

## L'ombre de Gödel

Ce rêve — *penser, c'est calculer* — portait pourtant en lui une **ombre**,
projetée presque au même moment. Cinq ans avant la machine de Turing, en **1931**,
un jeune logicien autrichien, **Kurt Gödel**, avait démontré un théorème qui
allait ébranler les mathématiques elles-mêmes : son **théorème d'incomplétude**.

Le résultat est aussi simple à énoncer que vertigineux. Tout système de règles
formelles assez puissant pour faire de l'arithmétique contient des énoncés qui
sont **vrais**, mais que le système est **incapable de prouver**. La *vérité*
déborde toujours la *démonstration* : aucun jeu de règles, si complet soit-il, ne
pourra jamais tout capturer. Et le ressort de la preuve est une idée qui va
devenir centrale pour nous — l'**auto-référence**. Gödel construit, à l'intérieur
du système, un énoncé qui parle de lui-même et affirme en substance : *« Cet
énoncé n'est pas démontrable. »* Si le système le démontrait, il prouverait
quelque chose de faux ; il ne peut donc pas le démontrer — et c'est justement ce
qui le rend vrai. Une boucle qui se mord la queue, et dont le système ne peut pas
sortir.

Turing, du reste, n'a pas échappé à cette ombre : il l'a lui-même prolongée. Sa
machine de 1936 servait aussi à établir qu'il existe des questions qu'**aucun
algorithme ne pourra jamais trancher** (la plus célèbre étant de savoir si un
programme donné finira par s'arrêter ou tournera à l'infini). Le père de l'idée
« penser = calculer » a donc, du même geste, tracé les **frontières** du calcul.
Le pari de l'IA naît ainsi avec, inscrite en lui, la trace de ses propres limites.

Que conclure, pour notre question — une machine peut-elle penser ? Étonnamment, on
a tiré de Gödel **deux leçons radicalement opposées**, et toutes deux nous
accompagneront jusqu'au bout du cours.

**Première lecture : le théorème est un mur.** Le physicien **Roger Penrose** en a
tiré l'argument anti-IA le plus célèbre : *nous*, humains, sommes capables de
*voir* qu'un tel énoncé est vrai, là où la machine reste bloquée. Si notre esprit
saisit une vérité qu'aucun système formel ne peut prouver, c'est donc qu'il ne se
réduit **pas** à un système formel — que penser ne se ramène pas à du calcul. Nous
reviendrons longuement sur cette thèse au **Module 5**, aux côtés d'un autre
adversaire célèbre de l'IA, le philosophe John Searle.

**Seconde lecture : le théorème est un moteur.** Pour le penseur américain
**Douglas Hofstadter**, la boucle auto-référentielle de Gödel n'est pas une
infirmité, mais le secret même de l'esprit. Un système assez riche pour se
**représenter lui-même** engendre une « **boucle étrange** » — et c'est de ce
repli sur soi qu'émergeraient, selon lui, le sentiment d'un « je », le sens, la
conscience. Loin d'interdire la pensée à la machine, l'auto-référence en serait la
**source**. Nous recroiserons Hofstadter et ses idées à plusieurs reprises dans ce
module.

Un même théorème, donc, et deux conclusions inverses : l'auto-référence comme
*limite* infranchissable, ou comme *origine* de l'esprit. Le désaccord n'est
toujours pas tranché. Retenez surtout l'essentiel : dès sa naissance, le rêve
d'une pensée mécanique avance avec une ombre attachée à ses pas.

{{% details "Pour aller plus loin : ce que dit — et ne dit pas — le théorème de Gödel" %}}
Le théorème vaut pour tout système formel **cohérent** (sans contradiction) et
assez riche pour exprimer l'arithmétique. Gödel établit en fait deux résultats : un
tel système ne peut pas prouver tous les énoncés arithmétiques vrais (**premier
théorème**), et il ne peut pas non plus prouver sa **propre cohérence** (**second
théorème**). Le tour de force technique est le *codage de Gödel* : numéroter chaque
énoncé pour que le système puisse, en parlant de nombres, **parler de lui-même** —
et fabriquer ainsi la phrase « je ne suis pas démontrable ».

Attention aux contresens : le théorème ne dit **pas** que « les mathématiques sont
fausses », ni que la vérité serait une affaire d'opinion. C'est une limite
**précise** sur ce qu'une démonstration *formelle, à l'intérieur d'un système
donné*, peut atteindre. On peut toujours prouver l'énoncé récalcitrant dans un
système **plus puissant** — qui aura alors, à son tour, son propre angle mort.
Quant à l'argument de Penrose, il reste **contesté** : ses critiques objectent que
rien ne garantit qu'un humain puisse réellement « voir » la vérité en question sans
déjà supposer, gratuitement, la cohérence du système.
{{% /details %}}

## Une fin tragique, et une porte qui s'ouvre

L'histoire personnelle de Turing, elle, se termine mal. En 1952, il est poursuivi
par la justice britannique en raison de son homosexualité, alors illégale, et
condamné à subir un traitement hormonal — une castration chimique. Mis au ban,
privé de son habilitation de sécurité, il meurt en 1954, à seulement 41 ans, par
empoisonnement au cyanure, dans des circonstances que l'on a longtemps tenues
pour un suicide. Il ne verra jamais les machines pensantes qu'il avait
pressenties. Il faudra attendre **2009** pour que le gouvernement britannique
présente des excuses officielles, et **2013** pour une grâce royale posthume.

Turing a posé la question et dégagé l'horizon — *la pensée comme calcul* — mais
il n'a pas dit *comment* s'y prendre concrètement pour construire une machine
intelligente. Cette tâche revient à la génération suivante. Et, dès le départ,
celle-ci va se diviser : non pas une, mais **deux réponses rivales** vont naître
presque en même temps, chacune pariant sur une idée radicalement différente de ce
qu'est l'intelligence. C'est le sujet du prochain épisode.
