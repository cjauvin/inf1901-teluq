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
entraînement et test ?), **pertinent** (mesure-t-il ce qui coûte vraiment
quand on se trompe ?) et **valable** (vaut-il pour les données qu'on
rencontrera vraiment ?). Quatre questions, quatre sections. Aucune ne demande de
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
réponse**, ou qu'on ne possédera pas au moment de prédire. L'exemple le plus
célèbre vient du naufrage du *Titanic*, dont la liste des passagers est un
classique des cours d'apprentissage automatique : on y prédit qui a survécu à
partir de la classe, du sexe, de l'âge, du tarif payé. La [version complète de
cette liste](https://hbiostat.org/data/repo/titanic.html), compilée à partir de
l'*Encyclopedia Titanica* et hébergée par l'Université Vanderbilt, comporte
deux colonnes de plus : le numéro du canot de sauvetage et le numéro
d'identification du corps repêché. Donnez-les au modèle, et il devient parfait,
et pour cause : avoir un numéro de canot, *c'est* avoir survécu ; avoir un
numéro de corps, *c'est* être mort. Le modèle n'a rien deviné, il a lu la
réponse, à peine maquillée, dans la question. Nos maisons ont leur version du
même piège : pour prédire le prix, la « taxe foncière » ferait des merveilles,
puisqu'elle est calculée à partir de la valeur de la maison.

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

C'est aussi le cadre naturel pour une opération que nous avons faite plusieurs
fois sans la nommer tout à fait : régler ce qui ne s'apprend pas. Le nombre de
voisins *k*, la sévérité λ de la pénalité, le taux d'apprentissage de la
descente : aucun de ces nombres n'est un paramètre du modèle, aucun ne descend
la pente avec les autres. Ce sont des **hyperparamètres**, des réglages *de la
procédure*, fixés avant l'entraînement. On les choisit en essayant plusieurs
valeurs et en gardant celle qui donne le meilleur score de validation croisée ;
puis, et seulement alors, on ouvre les scellés du jeu de test pour le verdict
final. C'est exactement le rôle de l'ensemble de validation de la page
précédente, en version tournante.

## Compter juste : les métriques

Troisième question : le score mesure-t-il ce qui coûte vraiment ? Jusqu'ici,
pour une catégorie, nous avons compté le **taux de bonnes réponses**, et il a un
défaut que nous connaissons déjà : dans [*Le modèle le plus
bête*](docs/module2/20-modele-le-plus-bete), un filtre qui ne signalait
*jamais* de pourriel obtenait 99 % de bonnes réponses, parce que les pourriels
étaient rares. Un seul nombre ne peut pas dire à la fois combien de pourriels on
attrape et combien de vrais courriels on jette. Il faut compter *séparément*.

Prenons 1000 courriels, dont 50 pourriels, et un filtre qui en jette une
partie. Quatre choses peuvent arriver à chaque courriel, et on les range dans un
tableau, la **matrice de confusion** : un pourriel jeté (**vrai positif**), un
pourriel passé au travers (**faux négatif**), un vrai courriel jeté (**faux
positif**), un vrai courriel gardé (**vrai négatif**). « Positif » veut dire
ici « signalé par le filtre », et n'a rien d'une bonne nouvelle.

Ces deux façons de se tromper n'ont d'ailleurs rien de propre à l'intelligence
artificielle. La statistique les a nommées bien avant, en 1933, sous la plume
de Jerzy Neyman et Egon Pearson : l'**erreur de première espèce**, voir un
effet là où il n'y en a pas (notre faux positif), et l'**erreur de seconde
espèce**, manquer un effet bien réel (notre faux négatif), en anglais [*type I
and type II errors*](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors).
C'est la grammaire de tout test, de l'essai clinique au contrôle de qualité en
usine ; un tribunal qui condamne un innocent ou acquitte un coupable commet
exactement ces deux erreurs-là. L'apprentissage automatique n'a fait qu'en
hériter, avec son vocabulaire à lui.

{{< image src="/images/module2/matrice-confusion.svg" alt="Un tableau à quatre cases croisant la réalité (pourriel ou courriel légitime, en lignes) et la décision du filtre (jeté ou gardé, en colonnes), pour 1000 courriels dont 50 pourriels. Vrais positifs : 40 pourriels jetés. Faux négatifs : 10 pourriels gardés. Faux positifs : 20 courriels légitimes jetés. Vrais négatifs : 930 courriels légitimes gardés. Les deux cases d'erreur sont teintées en rouge ; sous le tableau, le taux de bonnes réponses (97 %), la précision (67 %) et le rappel (80 %)." title="La matrice de confusion : quatre cases au lieu d'un seul score. Les deux cases rouges sont les deux façons de se tromper, et elles ne coûtent pas la même chose." loading="lazy" >}}

Ce filtre affiche 97 % de bonnes réponses ; « jamais un pourriel » en aurait eu
95. Le taux global cache presque tout. Deux questions plus précises se lisent
dans le tableau, et chacune a son nom. La **précision** : parmi ce que le
filtre a jeté, quelle part était vraiment du pourriel ? Ici 40 sur 60, soit
67 % ; le reste, ce sont des courriels légitimes perdus. Le **rappel** : parmi
les vrais pourriels, quelle part le filtre a-t-il attrapée ? Ici 40 sur 50,
soit 80 % ; le reste est passé au travers. Deux nombres au lieu d'un, et ils
tirent en sens contraires.

{{< image src="/images/module2/precision-rappel.svg" alt="À gauche, des courriels figurés par des points, rouges pour les pourriels, bleus pour les légitimes, et un lasso pointillé autour de ce que le filtre a jeté : 40 rouges et 20 bleus à l'intérieur, 10 rouges restés dehors. À droite, deux barres. La barre de la précision représente les 60 courriels jetés, dont 40 rouges : 67 %. La barre du rappel représente les 50 vrais pourriels, dont 40 attrapés : 80 %." title="Précision et rappel, avec les nombres de la matrice : deux questions, deux dénominateurs. La précision se lit à l'intérieur du lasso ; le rappel, parmi les points rouges." loading="lazy" >}}

Ces deux mots ne viennent pas non plus de l'IA, mais de la **recherche
d'information**, la discipline des catalogues de bibliothèque puis des moteurs
de recherche. Devant une requête, un bon système ramène des documents
*pertinents*, sans les noyer dans du bruit (la précision), et n'en oublie pas
en route (le rappel) ; c'est pour départager les systèmes de recherche
documentaire, dès les années 1960, qu'on a fait de ce couple la mesure de
référence, et il l'est resté : [précision et
rappel](https://fr.wikipedia.org/wiki/Précision_et_rappel) sont aujourd'hui le
vocabulaire commun de tout ce qui *trie*. Un filtre anti-pourriel n'est
d'ailleurs qu'une recherche déguisée : retrouver les pourriels parmi les
courriels.

Car ils tirent en sens contraires. Souvenez-vous de la régression logistique de
[*Classer*](docs/module2/60-classer) : elle donne une probabilité, et nous
avons tranché à 0,5. Rien n'y oblige. Placez le seuil à 0,9, et le filtre ne
jette plus que ce dont il est presque sûr : la précision monte, le rappel
s'effondre. Placez-le à 0,1, et il jette au moindre doute : le rappel monte, la
précision s'effondre. Le même modèle, sans rien réentraîner, peut être strict
ou indulgent, et le choix n'appartient pas aux mathématiques mais au problème.
Pour un filtre anti-pourriel, un vrai courriel jeté coûte plus cher qu'un
pourriel qui passe : on privilégie la précision. Pour un test de dépistage, un
malade manqué coûte plus cher qu'une fausse alerte qu'un second examen
dissipera : on privilégie le rappel. C'est cette question, *quelle erreur coûte
le plus ?*, que le [travail noté](docs/module2/99-travail-noté-2) vous posera
sur un vrai filtre.

Pour un nombre, la question se pose aussi, plus simplement. L'erreur
quadratique moyenne d'[*Un modèle qui s'entraîne*](docs/module2/50-entrainer-un-modele)
est faite pour être *minimisée* : ses carrés sont commodes pour la descente,
mais illisibles pour un humain (des dollars au carré). Pour *rendre compte*, on
préfère l'**erreur absolue moyenne** : sur nos vingt maisons, la droite se
trompe de 41 000 \\$ en moyenne, et de 59 000 \\$ au pire. Voilà qui se comprend,
et qui permet de juger si le modèle est bon *pour l'usage qu'on en fera* :
excellent pour un aperçu, insuffisant pour fixer un prix de vente.

Une métrique, en somme, est un choix : elle dit ce qu'on décide de compter
comme réussite. Avant de lire un score, demandez toujours lequel.

## Jamais vu, mais du même monde : la question de la distribution

Dernière question, et la plus facile à oublier : le score vaut-il pour les
données qu'on rencontrera *vraiment* ? Pour la comprendre, faisons un détour
par les sondages. Interroger mille personnes pour connaître l'opinion de
millions d'autres, c'est un pari : on suppose que l'échantillon **ressemble**
à la population, qu'il en est un petit modèle réduit. Quand ce n'est pas le
cas, le sondage se trompe avec une assurance parfaite. L'exemple le plus
célèbre date de 1936 : un grand magazine américain, le [*Literary Digest*](https://en.wikipedia.org/wiki/The_Literary_Digest),
avait recueilli plus de deux millions de réponses et prédisait une large
défaite de Roosevelt ; il fut réélu triomphalement. Les réponses venaient de
listes d'abonnés au téléphone et de propriétaires d'automobiles, en pleine
crise économique : un échantillon immense, mais tiré d'un autre monde que
celui des électeurs. Ce n'est pas la quantité qui garantit un sondage, c'est la
**représentativité**.

Un jeu de données est un sondage. Nos vingt maisons ne sont pas *les*
maisons ; ce sont vingt tirages dans un réservoir bien plus vaste, celui de
toutes les maisons qu'un tel modèle pourrait rencontrer, et les statisticiens
appellent ce réservoir une **distribution**. Le jeu d'entraînement en est un
échantillon, le jeu de test un autre, et toute la méthode de ce chapitre repose
sur une hypothèse muette : les deux viennent du même réservoir, et les
données de demain aussi. On dit alors que le test est **en distribution**.
Généraliser, c'est toujours généraliser *à ce réservoir-là*, jamais au monde
entier.

Que se passe-t-il quand l'hypothèse tombe, quand une donnée est **hors
distribution** ? Trois visages du même problème.

- **L'extrapolation.** Nos maisons vont de 112 à 280 m². Demandez à la droite
  le prix d'un manoir de 600 m² : elle répond, 1 696 000 \\$, avec le même
  aplomb que pour une maison de 180 m². Mais aucune donnée ne soutient plus
  cette réponse ; la droite se prolonge dans le vide, et rien ne dit que les
  manoirs obéissent à la même règle que les bungalows.
- **Le changement de lieu ou de population.** Un modèle entraîné sur les ventes
  de Montréal, appliqué à Vancouver ; un test de dépistage mis au point sur des
  adultes, appliqué à des enfants. Les mêmes caractéristiques, mais un autre
  réservoir : le score obtenu là-bas ne dit rien d'ici.
- **La dérive dans le temps.** Un filtre anti-pourriel entraîné sur les
  pourriels de 2010, face à ceux de 2025 : les mots ont changé, les ruses
  aussi. La distribution a glissé sous le modèle, sans qu'il s'en aperçoive, et
  son score d'hier ne dit plus rien d'aujourd'hui.

{{< image src="/images/module2/hors-distribution.svg" alt="Le nuage des vingt maisons (de 112 à 280 m²) et sa droite, avec la zone couverte par les données ombrée. Loin à droite, un manoir de 600 m² pour lequel la droite, prolongée en pointillé, annonce environ 1 696 000 dollars, accompagné d'un point d'interrogation : le modèle répond avec le même aplomb, mais aucune donnée ne le soutient plus." title="Hors distribution : dans la zone que les données couvrent, le score du test veut dire quelque chose ; au-delà, la droite répond encore, mais plus rien ne la garantit." loading="lazy" >}}

C'est le *Literary Digest* à chaque fois : un échantillon, parfois énorme, mais
tiré d'un autre monde que celui où l'on prédit. La leçon pratique tient en deux
règles. Le jeu de test doit ressembler au **déploiement**, pas seulement à
l'entraînement : si le modèle servira à Vancouver, il faut des maisons de
Vancouver dans le test, et l'on aura vite fait de découvrir qu'il en faut aussi
dans l'entraînement. Et un modèle mis en service doit être **surveillé**, parce
que le monde bouge et que rien, dans le modèle, ne l'avertira que la
distribution a changé.

Rappelez-vous la 1001ᵉ image du début du module : la question était de savoir
si elle faisait partie des 1000. Il y avait une question cachée derrière :
vient-elle seulement *du même monde* que les 1000 ? Une photo prise de nuit,
quand toutes les autres l'ont été de jour, est neuve d'une façon que le modèle
ne sait pas traiter. Et pour les grands modèles de langage de l'encart de
[*Généraliser*](docs/module2/70-generaliser/#un-modèle-se-juge-sur-ce-quil-na-jamais-vu),
la question devient vertigineuse : quand l'entraînement est tout le Web, où
finit « en distribution » ?

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
