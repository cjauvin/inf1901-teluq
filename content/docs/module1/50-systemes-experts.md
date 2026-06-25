---
title: "Capturer l'expertise : les systèmes experts"
weight: 50
slug: systemes-experts
---

# Capturer l'expertise : les systèmes experts

## Rétrécir et codifier le monde pour réussir

Le chapitre « [Représenter le monde](docs/module1/40-representer-le-monde) » s'est
achevé sur un constat sévère : on ne peut pas *écrire* le sens commun, parce qu'il
n'a pas de fond. Faut-il pour autant renoncer ? Les
chercheurs des années 1970 tirent du mur une leçon plus rusée que désespérée. Si le
savoir général est hors d'atteinte, c'est peut-être qu'on visait trop large. Alors :
visons **étroit**.

L'idée est d'une simplicité presque provocante. Renonçons à l'intelligence générale ;
choisissons **un seul domaine**, bien délimité — diagnostiquer une infection,
configurer un ordinateur, prospecter un gisement minier — et tâchons d'y reproduire
la compétence d'**un seul expert**. Car dans un domaine pointu, le savoir-faire d'un
spécialiste ressemble souvent à un vaste répertoire de règles du type *si telles
conditions, alors telle conclusion*. Le médecin qui raisonne « *si* le patient a de
la fièvre **et** telle bactérie dans le sang, *alors* prescrire tel antibiotique »
applique, au fond, une règle. Recueillons assez de ces règles, inscrivons-les dans la
machine, et celle-ci devrait, dans ce périmètre, *raisonner comme l'expert*. C'est le
pari des **systèmes experts**, et le mot d'ordre de tout ce chapitre : **connaissance =
règles explicites**.

On reconnaît là une vieille ruse. SHRDLU ne « comprenait » son monde de blocs que
parce que ce monde était minuscule ; les systèmes experts reprennent exactement la
même tactique — **réussir en rétrécissant le monde** —, mais en la braquant cette
fois non sur un jouet de laboratoire, mais sur des domaines réels et lucratifs. Et le
pari, pour une fois, va *payer* : l'IA symbolique va sortir des universités, gagner de
l'argent, et faire dire au monde des affaires que l'intelligence artificielle, enfin,
« marche ». Reste à voir *comment*, concrètement, une machine peut raisonner avec des
règles — c'est l'affaire de la section suivante.

## L'anatomie d'un système expert

Un système expert tient en **trois pièces**. D'abord une **base de règles** : la
connaissance du domaine, traduite en énoncés *si… alors…*. Ensuite une **base de
faits** (ou « mémoire de travail ») : ce qu'on sait du cas précis qu'on traite — les
symptômes du patient, l'état de la voiture devant soi. Enfin, un **moteur
d'inférence** : un mécanisme général qui confronte les faits aux règles, déclenche
celles qui s'appliquent, et en tire de nouveaux faits, jusqu'à une conclusion.

La trouvaille est dans cette **séparation**. Le moteur d'inférence ne sait *rien* de
médecine, d'automobile ou de minéralogie : c'est une machine à enchaîner des règles,
point. Toute la compétence loge dans la base de règles — qu'on peut changer comme une
cartouche. Remplacez les règles, et le même moteur devient tour à tour médecin,
mécanicien ou géologue. Le savoir d'un côté, le raisonnement de l'autre : pour la
première fois, on peut bâtir des « experts » à la chaîne, sans tout reprogrammer.

Voyons-le à l'œuvre sur un cas que tout le monde connaît : **une voiture qui refuse
de démarrer**. Donnons à notre système une poignée de règles —

> **R1** — *si* le moteur ne se lance pas du tout **et** les phares sont faibles,
> *alors* la batterie est déchargée.
> **R2** — *si* la batterie est déchargée, *alors* recharger ou remplacer la batterie.
> **R3** — *si* le moteur se lance normalement mais ne démarre pas **et** le réservoir
> est vide, *alors* refaire le plein.
> **R4** — *si* le moteur se lance normalement **et** le réservoir n'est pas vide,
> *alors* faire vérifier l'allumage.

— et deux faits observés au départ : *le moteur ne se lance pas* et *les phares sont
faibles*. Mettez-vous à la place du moteur d'inférence. Vous parcourez les règles :
**R1** voit ses deux conditions satisfaites — elle se **déclenche** et inscrit un fait
nouveau, *la batterie est déchargée*. Ce fait satisfait à son tour la condition de
**R2**, qui se déclenche et livre la conclusion : *recharger ou remplacer la
batterie*. R3 et R4, dont les conditions ne sont pas remplies, restent muettes. En
deux pas, parti de simples symptômes, le système a « diagnostiqué » la panne — et,
détail précieux, il peut **retracer son raisonnement** : *pourquoi* la batterie ? à
cause de R1, à cause des phares faibles.

Ce que vous venez de faire — partir des faits et avancer jusqu'à la conclusion — porte
un nom : le **chaînage avant**. C'est le raisonnement du curieux, qui observe d'abord
et regarde ensuite où cela le mène. Très efficace quand on dispose déjà de beaucoup de
faits et qu'on se demande *ce qui en découle*.

Mais on peut prendre le problème par l'autre bout. Supposez que vous ayez une
intuition — *« et si c'était la batterie ? »* — et que vous vouliez la vérifier. Le
moteur d'inférence part alors de cette **hypothèse**, comme d'un but à atteindre, et
remonte les règles à reculons. Pour affirmer « recharger la batterie » (R2), il
faudrait que *la batterie soit déchargée* ; et pour cela (R1), il faudrait que *le
moteur ne se lance pas* **et** que *les phares soient faibles*. Or ces deux derniers
points, aucune règle ne les produit : ce sont des choses à **observer**. Le système
vous les demande donc — *« les phares sont-ils faibles ? »* — et n'examine *que* ce
qui sert l'hypothèse poursuivie. C'est le **chaînage arrière**.

Deux directions, donc, pour une même base de règles : **en avant**, poussé par les
faits ; **en arrière**, tiré par un but. Le second a un avantage décisif pour le
diagnostic : plutôt que de tout mesurer d'avance, il ne pose que les questions
*utiles* à la piste qu'il suit. C'est exactement pour cette raison que l'employait le
plus célèbre des systèmes experts, un diagnostiqueur médical nommé **MYCIN** — qui
nous attend dans la section suivante.

<!-- FIGURE/APPLET À CRÉER (M1, ép. 5) : moteur d'inférence interactif sur le cas
« voiture qui ne démarre pas » — l'étudiant fixe les faits observés et voit les règles
se déclencher en cascade jusqu'au diagnostic. -->

## L'âge d'or : MYCIN, XCON et le boom

L'aventure commence dès 1965, à Stanford, avec **DENDRAL** — souvent tenu pour le
tout premier système expert : un programme capable d'identifier des **molécules** à
partir de données de spectrométrie, à la manière d'un chimiste chevronné. Mais c'est
son cadet, **MYCIN**, conçu au début des années 1970 par **Edward Shortliffe**, qui
deviendra la vedette du genre. Sa spécialité : diagnostiquer les **infections
bactériennes du sang** et recommander le bon antibiotique, à la bonne dose. Sous le
capot, quelque **600 règles** et le **chaînage arrière** que nous venons de décrire :
MYCIN part d'une hypothèse de germe et interroge le médecin, question après question,
jusqu'à sa conclusion. Et — vertu du même mécanisme — il peut à tout moment
**justifier** sa démarche : demandez-lui *pourquoi* il pose telle question, il vous
montre la règle qu'il cherche à satisfaire.

Une difficulté, pourtant : en médecine, rien n'est sûr à 100 %. Tel symptôme
*suggère* un germe sans le garantir. MYCIN introduit donc des **facteurs de
certitude** — un nombre accolé à chaque règle, indiquant à quel point sa conclusion
est fiable — qu'il combine au fil du raisonnement. Bricolage avant l'heure : des
années plus tard, une théorie autrement plus rigoureuse de l'incertitude, les
**réseaux bayésiens**, viendra prendre le relais (nous la croiserons au Module 2).
Mais l'intuition est déjà là : un système qui *raisonne* doit aussi savoir *douter*.

Et MYCIN était bon. Lors d'une évaluation restée célèbre, en 1979, on soumit ses
recommandations à un jury d'experts qui les compara à celles de médecins humains —
sans savoir lesquelles venaient de la machine. Verdict : MYCIN faisait **jeu égal,
voire mieux**, que les spécialistes. Un programme venait, sur son terrain, d'égaler
les meilleurs cliniciens. Et pourtant — c'est tout le paradoxe — **MYCIN ne fut
jamais utilisé auprès d'un seul vrai patient.** Les obstacles n'étaient pas
scientifiques, mais humains et pratiques : qui serait **responsable** si la machine se
trompait — le médecin, l'hôpital, le programmeur ? Comment l'**intégrer** au travail
réel, à une époque sans ordinateur au chevet du malade, où il fallait tout saisir à la
main sur un terminal ? Et quel médecin accepterait de **déléguer** son jugement à une
boîte ? MYCIN réussissait tout, sauf à exister dans le monde. Premier signe, discret,
que la fragilité des systèmes experts ne serait pas que technique.

Là où la médecine résistait, l'industrie, elle, ouvrit grand les bras. À la fin des
années 1970, le constructeur informatique **DEC** se débattait avec un casse-tête :
chacune de ses commandes d'ordinateurs **VAX** devait être configurée sur mesure — des
centaines de composants à assortir sans erreur ni oubli. On confia la tâche à un
système expert, **XCON**. Ce fut un triomphe : XCON configurait les commandes plus
vite et plus sûrement que les humains, et fit **économiser des dizaines de millions de
dollars par an** à DEC. Le message porta : les systèmes experts n'étaient pas qu'une
curiosité de laboratoire — *ça marchait, et ça rapportait*. (Un détail qu'on n'écouta
guère sur le moment : XCON enflait sans cesse, jusqu'à des milliers de règles qu'il
fallait sans relâche réajuster les unes aux autres. Nous y reviendrons.)

Le succès de XCON déclencha une ruée. Au début des années 1980, l'« IA » devint, pour
la première fois, une véritable **industrie**. On vendit des **coquilles** (*shells*)
— des moteurs d'inférence vides, prêts à recevoir la base de règles de n'importe quel
métier ; un nouveau métier apparut, l'**ingénieur de la connaissance**, chargé
d'extraire le savoir des experts ; des entreprises se montèrent, des capitaux
affluèrent. On construisit même des ordinateurs spécialisés, les **machines Lisp**,
taillés pour ces programmes ; et le Japon lança un projet national pharaonique, la
**Cinquième Génération**, pour prendre la tête de cette informatique du raisonnement.
Jamais l'IA symbolique n'avait semblé si près de tenir ses promesses. Mais le sommet
est aussi l'endroit d'où l'on commence à redescendre — et, déjà, des fissures
couraient sous l'édifice.

## Le goulot d'étranglement

Reprenons les fissures une à une. La première, et la plus profonde, tient à une
question d'apparence innocente : *d'où viennent les règles ?* Quelqu'un doit les
écrire — l'**ingénieur de la connaissance** —, en interrogeant longuement un expert
pour traduire son savoir en *si… alors…*. Or ce travail s'est révélé d'une lenteur
désespérante. Pire : une grande part de l'expertise se laisse mal mettre en mots. Le
médecin chevronné qui « sent » un diagnostic au premier coup d'œil, le mécanicien qui
devine la panne à l'oreille, ne savent pas toujours *dire* ce qu'ils savent — leur
compétence est un **savoir tacite**, fait d'intuition et d'expérience, et non une
liste de règles dormant dans un tiroir. On ne codifie pas ce qui n'a jamais été
formulé. Ce blocage a reçu un nom resté célèbre : le **goulot d'étranglement de
l'acquisition des connaissances**.

Deuxième fissure, déjà rencontrée dans « [Représenter le
monde](docs/module1/40-representer-le-monde) » : la **rigidité**. Un système expert
ne connaît que ses règles, et rien autour. Tant qu'on reste pile dans son domaine, il
brille ; qu'on en sorte d'un pas, et il ne *fléchit* pas — il s'effondre, sans le
moindre signe d'embarras. MYCIN diagnostiquait les infections du sang ; si on lui
avait décrit une jambe cassée, il aurait cherché un microbe, car il n'avait aucune
idée de ce qu'il ignorait. Et faute du moindre **bon sens**, rien ne l'empêchait
d'avaler une absurdité — un patient âgé de moins de zéro an, une dose mille fois trop
forte — qu'un étudiant de première année aurait flairée aussitôt. Le mur du sens
commun, qu'on croyait avoir contourné en rétrécissant le monde, était simplement
revenu par la fenêtre.

Troisième fissure : l'**ingérabilité**. Tant qu'un système compte quelques dizaines de
règles, tout va bien. Mais XCON en accumula des milliers — et l'on découvrit qu'au-delà
d'un certain seuil, les règles **interagissent** de façon imprévisible. En ajouter une
pour corriger un cas pouvait en dérégler trois autres, ailleurs, sans qu'on le voie
venir. Maintenir une grosse base devenait un cauchemar : on passait plus de temps à
rattraper les effets de bord qu'à enrichir le savoir. La connaissance explicite,
écrite à la main, ne **passait pas à l'échelle**.

Mais la fissure la plus décisive est la plus discrète. Un système expert n'**apprend
rien**. Chaque règle a été déposée là par une main humaine ; le programme peut tourner
mille fois sur mille cas, il n'en tirera pas une règle nouvelle, ne corrigera pas de
lui-même celles qui se trompent. Toute son intelligence lui vient du dehors, figée le
jour de sa programmation. Et c'est en butant sur cette limite-là que les chercheurs
commencèrent, peu à peu, à retourner la question. Puisque le coûteux, l'impossible,
c'est d'*extraire* les règles des experts et de les tenir à jour à la main… *et si
l'on confiait ce travail à la machine elle-même ? Et si, au lieu de lui dicter ses
règles, on la laissait les découvrir dans les données ?*

Mais cette question-là devra attendre. Car les promesses des systèmes experts étaient
devenues trop grandes pour des livraisons si minces : à la fin des années 1980, les
capitaux fuient, les entreprises ferment, les fameuses machines Lisp finissent au
rebut. Avant que la machine n'apprenne, l'IA devra d'abord traverser un long
**hiver** — celui de « [Les hivers et la bascule](docs/module1/60-hivers) ».
