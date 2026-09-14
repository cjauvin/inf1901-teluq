---
title: "Bien évaluer un modèle"
weight: 75
slug: bien-evaluer
---

# Bien évaluer un modèle

La page précédente a posé la règle d'or : on juge un modèle sur des exemples
qu'il n'a jamais vus. C'est nécessaire, mais ce n'est pas suffisant. Un score
sur le jeu de test n'a de valeur que s'il est **honnête** (le modèle n'a-t-il
vraiment rien vu du test ?), **fiable** (tient-il au hasard de la coupe entre
entraînement et test ?) et **pertinent** (mesure-t-il ce qui coûte vraiment
quand on se trompe ?). Trois questions, trois sections. Aucune ne demande de
nouveau modèle ; toutes demandent de la méthode, et c'est là, bien plus que dans
le choix d'un algorithme, que se joue la différence entre un modèle qui marche
et un modèle qui a l'air de marcher.

## Le score trop beau pour être vrai : la fuite de données

Commençons par le piège le plus courant, et le plus sournois. Un modèle affiche
99 % de bonnes réponses sur le jeu de test ; on le déploie ; il s'effondre. Que
s'est-il passé ? Le plus souvent, une **fuite de données** : une information qui
n'aurait pas dû être disponible s'est glissée dans l'entraînement, et le test
n'était plus vraiment neuf.

La fuite prend deux formes. La première est la **contamination** : le jeu de
test contient, sous un déguisement, des exemples que le modèle a déjà vus. La
même maison, vendue deux fois en trois ans, une fois dans chaque paquet ; la
même photo, en deux résolutions ; le même courriel, transféré à trois personnes.
Le modèle ne généralise pas, il *reconnaît*, et le score le récompense pour sa
mémoire. À grande échelle, c'est exactement le problème des grands modèles de
langage évoqué dans [l'encart de la page précédente](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu) :
quand les données d'entraînement sont tout le Web, on ne sait plus ce qui a
fui.

La seconde forme est plus subtile : **une caractéristique qui contient la
réponse**, ou qu'on ne possédera pas au moment de prédire. Reprenons nos
maisons. Pour prédire si une maison partira vite, quelqu'un ajoute au registre
le « nombre de visites reçues » : le modèle devient excellent, forcément, une
maison très visitée est une maison qui se vend. Mais ce nombre, on ne le
connaît qu'*après* la mise en vente, précisément quand la prédiction ne sert
plus à rien. Pour prédire le prix, la « taxe foncière » ferait des merveilles :
elle est calculée à partir de la valeur de la maison. Dans les deux cas, le
modèle n'a rien appris de l'avenir ; il a lu la réponse, à peine maquillée, dans
la question.

{{< image src="/images/module2/fuite-de-donnees.svg" alt="Le même découpage entraînement / test que dans la page précédente, mais deux exemples du bloc de test ont un jumeau dans le bloc d'entraînement, reliés par un trait pointillé rouge : les mêmes exemples, sous un déguisement. Le modèle les reconnaît au lieu de généraliser, et le score du test ment." title="Une fuite par contamination : deux exemples du test ont un jumeau dans l'entraînement. Le modèle les reconnaît, et le score le récompense pour sa mémoire." loading="lazy" >}}

Il n'existe pas de détecteur automatique de fuites ; il existe une discipline.
D'abord, la méfiance : un score exceptionnel est un symptôme avant d'être une
bonne nouvelle, et la première question à poser est « qu'est-ce qui pourrait
avoir fui ? ». Ensuite, une règle mécanique : **tout ce qu'on calcule à partir
des données se calcule sur l'ensemble d'entraînement seul**, moyennes, écarts,
choix des caractéristiques, réglages ; le jeu de test ne sert qu'une fois, à la
toute fin, comme un examen qu'on ne corrige pas en cours de route.

{{% hint info %}}
**Une unité n'est pas l'autre : mettre à l'échelle.** Cette règle a un cas
d'application très concret, que nous avons contourné sans le dire. Dans le plan
des maisons, kNN mesure une distance entre une différence de kilomètres et une
différence d'années ; or rien ne dit qu'un kilomètre « vaut » une année. Si
l'on avait mis la superficie en mètres carrés à côté du nombre de chambres, un
écart de 50 m² aurait écrasé un écart d'une chambre, et la distance n'aurait
plus mesuré grand-chose. On corrige en **mettant à l'échelle** chaque
caractéristique, par exemple en la ramenant entre 0 et 1, ou en soustrayant sa
moyenne et en divisant par son écart-type. La descente de gradient y gagne
aussi, car une cuvette étirée dans une direction se descend mal. Et la règle
s'applique : les moyennes et les écarts servant à la mise à l'échelle se
calculent sur l'entraînement, puis s'appliquent tels quels au test.
{{% /hint %}}

## Quand les données sont rares : la validation croisée

Deuxième question : le score est-il *fiable* ? Revenons à nos vingt maisons.
Suivre la règle d'or, c'est en mettre quatre sous scellés et n'apprendre que sur
seize. Deux ennuis, aussitôt. Seize maisons, c'est peu pour apprendre, et l'on
aimerait bien se servir des vingt. Surtout, le score dépend beaucoup
*desquelles* quatre on a écartées : tombez sur les deux exceptions du nuage
coloré, et le modèle paraîtra mauvais ; tombez sur quatre maisons bien typiques,
et il paraîtra excellent. Le hasard d'une seule coupe pèse trop lourd.

La parade est élégante : plutôt que de couper une fois, on **tourne**. On
partage les vingt maisons en cinq paquets de quatre. Au premier tour, le premier
paquet sert de test et les seize autres maisons servent à apprendre ; au
deuxième tour, c'est le deuxième paquet qui est mis à l'épreuve, et ainsi de
suite. Cinq tours, cinq scores, et l'on prend leur moyenne. Chaque maison a
servi de test exactement une fois, et toutes ont servi à l'entraînement quatre
fois sur cinq. C'est la **validation croisée**, et le nombre de paquets se règle
à volonté : cinq ou dix le plus souvent, jusqu'à *n* paquets d'un seul exemple
quand les données sont vraiment rares.

{{< image src="/images/module2/validation-croisee.svg" alt="Cinq rangées de vingt points, une par tour. Dans chaque rangée, seize points en vert-bleu forment l'ensemble d'entraînement et quatre points en brun, encadrés, l'ensemble de test ; le bloc de test se déplace de quatre places d'une rangée à l'autre, si bien que chaque maison sert de test exactement une fois. À droite de chaque rangée, un score ; en bas, leur moyenne." title="La validation croisée sur nos vingt maisons : cinq tours, chaque maison testée une fois, et le score final est la moyenne des cinq." loading="lazy" >}}

La validation croisée coûte cinq entraînements au lieu d'un, ce qui n'est rien
pour une droite et beaucoup pour un réseau de neurones géant ; c'est pourquoi
on la voit partout sur de petits jeux de données et presque jamais sur les très
grands, où un seul jeu de test suffit, parce qu'il est lui-même énorme.

C'est aussi le cadre naturel pour un geste que nous avons fait plusieurs fois
sans le nommer tout à fait : régler ce qui ne s'apprend pas. Le nombre de
voisins *k*, la sévérité λ de la pénalité, le taux d'apprentissage de la
descente : aucun de ces nombres n'est un paramètre du modèle, aucun ne descend
la pente avec les autres. Ce sont des **hyperparamètres**, des réglages *de la
procédure*, fixés avant l'entraînement. On les choisit en essayant plusieurs
valeurs et en gardant celle qui donne le meilleur score de validation croisée ;
puis, et seulement alors, on ouvre les scellés du jeu de test pour le verdict
final. C'est exactement le rôle de l'ensemble de validation de la page
précédente, en version tournante.

## Tout cela portait un nom : l'apprentissage supervisé

Prenons un peu de recul. Depuis la première page de ce module, une chose n'a
jamais changé, si discrète qu'on l'a à peine remarquée : **la bonne réponse était
toujours là.** Chaque maison venait avec son prix ; chaque courriel, avec son
étiquette pourriel ou non ; chaque point, avec sa couleur. Le modèle n'avait qu'à
apprendre le chemin de la question vers une réponse *qu'on lui fournissait
d'avance*.

Cette situation porte un nom, que nous pouvons enfin prononcer, maintenant que
nous l'avons vécue de bout en bout : l'**apprentissage supervisé**. « Supervisé »,
comme un élève qu'un professeur corrige, parce qu'il connaît, lui, la réponse
attendue. Régression ou classification, droite ou Bayes, paramétrique ou non :
tout ce que nous avons construit relève de cette grande famille, celle où l'on
apprend à partir d'exemples **étiquetés**.

Mais cette réponse toute prête, d'où vient-elle ? Quelqu'un a dû, quelque part,
étiqueter ces milliers d'exemples un à un, travail souvent long, coûteux,
parfois impossible. Il est si central qu'il est devenu une **industrie à part
entière**, celle de l'*étiquetage de données*. Des entreprises comme Scale AI
(dans laquelle Meta a investi une quinzaine de milliards de dollars en 2025),
Appen, Sama ou Labelbox, ou des plateformes comme le Mechanical Turk d'Amazon,
emploient ou mobilisent des centaines de milliers de personnes pour tracer des
contours sur des images, transcrire des enregistrements, classer des textes, et,
depuis les grands modèles de langage, comparer et noter des réponses générées.
Ce travail, souvent invisible et mal payé, réalisé en bonne partie au Kenya, aux
Philippines ou au Venezuela, est l'envers discret de l'apprentissage
supervisé : derrière chaque « bonne réponse » fournie au modèle, il y a eu un
humain. Et le monde déborde de données *sans* étiquette : des
millions de photos que personne n'a triées, des historiques d'achats sans
catégories, des textes en vrac. Peut-on apprendre quelque chose de données
brutes, livrées sans la moindre bonne réponse ? Et à l'inverse, quand un robot
apprend à marcher, nul ne lui souffle le « bon » mouvement à chaque instant : il
ne reçoit qu'un encouragement ou une chute, bien plus tard. Est-ce encore de
l'apprentissage ?

Oui — mais d'une autre sorte. Ce qui distingue ces situations, c'est la nature du
**signal** dont le modèle apprend : une réponse donnée, une structure à découvrir
sans guide, ou une récompense différée. C'est cette typologie, et les nouveaux
mondes qu'elle ouvre, que nous explorons au chapitre suivant.
