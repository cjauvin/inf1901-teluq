---
title: "Deux paris rivaux (1956-1958)"
weight: 20
slug: deux-paris
---

# Deux paris rivaux (1956-1958)

## Le moment : l'été 1956 à Dartmouth

À l'été 1956, une poignée de chercheurs se réunissent pendant deux mois sur le
campus du **Dartmouth College**, dans le New Hampshire, pour un atelier qui
restera comme l'**acte de naissance** de la discipline. C'est dans la proposition
de financement de cet atelier, rédigée l'année précédente par le jeune
mathématicien **John McCarthy**, qu'apparaît pour la première fois l'expression
**« intelligence artificielle »**. Le mot est choisi en partie pour marquer une
rupture, et se démarquer des étiquettes existantes comme la cybernétique.

{{< image src="/images/module1/dartmouth-hall.jpg" alt="Dartmouth Hall, un grand bâtiment géorgien en briques peintes en blanc, orné d'un fronton portant la date « 1784 » et surmonté d'un clocheton, sur le campus du Dartmouth College." title="Dartmouth Hall, sur le campus du Dartmouth College où se tint l'atelier de 1956." loading="lazy" >}}

<p class="image-credit">Dartmouth Hall (Dartmouth College). Photo : Kenneth C. Zirkel, <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>, via Wikimedia Commons.</p>

L'ambition affichée donne le vertige. La proposition postule que *« tout aspect
de l'apprentissage, ou de toute autre caractéristique de l'intelligence, peut en
principe être décrit avec une telle précision qu'une machine peut être construite
pour le simuler »* (en version originale : *« every aspect of learning or any
other feature of intelligence can in principle be so precisely described that a
machine can be made to simulate it »*). Les organisateurs — McCarthy, mais aussi
**Marvin Minsky**, **Claude Shannon** (le père de la théorie de l'information) et
**Nathaniel Rochester** (d'IBM) — pensent sincèrement qu'un groupe d'une dizaine
de personnes peut faire des progrès significatifs sur ce programme... en un seul
été.

On connaît la suite : ce qu'ils prenaient pour l'affaire de quelques étés
occupera des générations entières, et n'est toujours pas achevé. Mais
l'enthousiasme de Dartmouth lance véritablement le domaine. Et très vite, deux
familles d'idées sur *comment* fabriquer cette intelligence vont s'y dessiner.

## Le premier pari : l'esprit comme logique

La première famille d'idées prolonge directement l'intuition de Turing. Si
penser, c'est calculer, alors **l'intelligence consiste à manipuler des symboles
selon des règles logiques**. Un symbole, ici, c'est un jeton qui *tient lieu* de
quelque chose — un mot, un objet, une idée — et raisonner, c'est combiner ces
jetons d'après des règles précises, exactement comme un mathématicien enchaîne
les étapes d'une démonstration. Dans cette vision, peu importe que la machine
ressemble ou non à un cerveau : ce qui compte, c'est qu'elle possède les bons
symboles et les bonnes règles. On parle d'approche **descendante** (*top-down*),
car on programme le raisonnement « par le haut », explicitement.

Cette approche n'est pas restée abstraite. Dès 1956, présenté à Dartmouth même,
un programme nommé le **Logic Theorist**, conçu par **Allen Newell** et **Herbert
Simon**, parvient à démontrer des théorèmes de logique mathématique tirés d'un
ouvrage de référence, les *Principia Mathematica* de Russell et Whitehead. Pour
l'une de ces démonstrations, il trouve même une solution plus élégante que celle
des auteurs humains. C'est souvent considéré comme le **tout premier programme
d'intelligence artificielle** : une machine qui ne calcule pas des nombres, mais
qui *raisonne*, du moins en apparence.

L'enthousiasme est à son comble. Newell et Simon iront jusqu'à formuler une
hypothèse audacieuse : un système qui manipule des symboles de la bonne manière
posséderait *tout ce qu'il faut* pour être intelligent — ni plus, ni moins.
Pendant les décennies suivantes, c'est cette voie, **symbolique**, qui dominera
la recherche et récoltera les financements. Ce sera le cœur des chapitres suivants :
la [recherche](docs/module1/30-chercher-raisonner), la [représentation des
connaissances](docs/module1/40-representer-le-monde), les [systèmes
experts](docs/module1/50-systemes-experts).

## Le second pari : l'esprit comme cerveau

À l'autre bout du spectre, une intuition radicalement différente germe au même
moment. Et si, plutôt que de *programmer* le raisonnement d'en haut, on
construisait une machine qui **apprend toute seule, à partir d'exemples**, en
s'inspirant de l'organe qui réussit déjà le mieux à être intelligent : le
**cerveau** ?

L'idée a une racine précise. Dès 1943, deux chercheurs, **Warren McCulloch** et
**Walter Pitts**, proposent un modèle mathématique extrêmement simplifié du
neurone : une petite unité qui reçoit des signaux, les combine, et « s'allume »
ou non selon que la somme dépasse un certain seuil. Ils montrent qu'en reliant
ces unités élémentaires en réseau, on peut en principe réaliser des opérations
logiques. C'est le premier pont jeté entre la matière du cerveau et le calcul.

{{< image src="/images/module1/neurone-formel.svg" alt="Schéma d'un neurone formel : trois signaux d'entrée convergent vers un corps cellulaire qui les additionne (Σ) et compare la somme à un seuil ; en sortie, le neurone s'allume (1) si le seuil est dépassé, ou reste éteint (0)." title="Le neurone formel : combiner des signaux, puis s'activer si leur somme dépasse un seuil." loading="lazy" >}}

Restait à expliquer comment un tel réseau pourrait *apprendre*. En 1949, le
psychologue **Donald Hebb** avance une idée appelée à devenir célèbre : lorsque
deux neurones s'activent ensemble de façon répétée, le lien qui les unit se
renforce — « *neurons that fire together, wire together* ». L'apprentissage, dans
cette optique, ne consiste pas à réécrire des règles, mais à **ajuster la force
des connexions**. C'est précisément ce levier que Rosenblatt va donner à sa
machine.

{{< image src="/images/module1/regle-de-hebb.svg" alt="Schéma de la règle de Hebb : à gauche, deux neurones A et B au repos reliés par un lien fin ; à droite, lorsqu'ils s'activent ensemble, ils s'allument et le lien qui les unit s'épaissit, illustrant son renforcement." title="La règle de Hebb : deux neurones qui s'activent ensemble voient leur lien se renforcer." loading="lazy" >}}

En 1958, le psychologue **Frank Rosenblatt** transforme cette idée en une machine
bien réelle : le **perceptron**. Le principe est d'une élégance frappante. Au
lieu de lui dicter une règle, on *montre* au perceptron des exemples — par exemple
des images étiquetées « cercle » ou « carré ». À chaque essai, s'il se trompe, il
**ajuste légèrement ses réglages internes** pour se rapprocher de la bonne
réponse. Petit à petit, exemple après exemple, il s'améliore — sans que personne
ne lui ait jamais formulé *ce qui distingue* un cercle d'un carré. Il a *appris*.
C'est l'approche **ascendante** (*bottom-up*) : on n'écrit pas le savoir, on le
laisse émerger des données.

La promesse soulève un enthousiasme délirant. En 1958, le *New York Times*,
rapportant les propos de Rosenblatt, annonce que la marine américaine a dévoilé
l'embryon d'une machine électronique qui « sera capable de marcher, parler, voir,
écrire, se reproduire et avoir conscience de son existence ». On est évidemment
très loin du compte. Mais l'idée maîtresse — *une machine qui apprend de ses
erreurs* — est, elle, promise à un avenir immense. C'est la graine de tout ce que
nous étudierons aux modules 2, 3 et 4.

En un sens très concret, le perceptron est l'**ancêtre direct des réseaux de
neurones** d'aujourd'hui : l'apprentissage profond qui fait la une n'est, pour
l'essentiel, qu'un empilement de perceptrons perfectionnés, par millions et sur
de nombreuses couches. La ligne de descendance est directe — nous la remonterons
au **module 3**.

## Deux univers parallèles

On serait tenté de croire que ces deux paris se sont succédé — d'abord l'un, puis
l'autre. C'est faux, et c'est l'un des fils rouges les plus importants de ce
cours : ils sont nés **presque en même temps**, et ils ont **coexisté en
rivaux** pendant plus d'un demi-siècle, chacun dans son camp, avec ses
chercheurs, ses revues, ses financements.

Au fond, ce sont **deux idées de ce qu'est l'esprit** qui s'affrontent. Pour le
camp symbolique, l'esprit est essentiellement de la **logique** : des symboles et
des règles, indépendamment du support qui les réalise. Pour le camp
connexionniste, l'esprit est avant tout un **cerveau** : un réseau qui s'ajuste à
l'expérience. La même question — qu'est-ce que penser ? — reçoit deux réponses
presque opposées.

Ces deux univers ne vont pas avancer côte à côte dans une paisible indifférence :
ils vont **s'éclipser à tour de rôle**. Dès la fin des années 1960, comme nous le
verrons dans « [Les hivers et la bascule](docs/module1/60-hivers) », le camp
symbolique portera au perceptron un coup si rude
qu'il manquera de le tuer — et l'approche symbolique régnera presque sans partage
sur les vingt années suivantes. Il faudra attendre les années 2010, et le module
3 de ce cours, pour assister au spectaculaire retour de la tradition
connexionniste, sous le nom d'*apprentissage profond*.

{{% hint info %}}
La métaphore du cerveau est puissante — et c'est justement pour cela qu'il faut
s'en méfier. Le « neurone » de McCulloch, Pitts et Rosenblatt est une caricature
extrême du vrai neurone biologique. Nous y reviendrons en détail au module 3, au
moment où la tentation de confondre les deux sera la plus forte.
{{% /hint %}}

Pour l'instant, laissons le perceptron à sa promesse, et suivons le camp qui va
prendre les devants. Car c'est la voie symbolique qui, la première, va connaître
son âge d'or — celui des machines qui *cherchent* et qui *raisonnent*. C'est
l'objet de « [Chercher et raisonner](docs/module1/30-chercher-raisonner) ».
