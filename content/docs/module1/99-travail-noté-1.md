---
title: "Travail noté 1"
weight: 99
slug: travail-noté-1
---

# Vous êtes le moteur d'inférence : un système expert (travail noté 1)

Au Module 1, nous avons vu qu'avant l'apprentissage automatique (que nous commencerons à étudier sérieusement au module 2), la grande idée de
l'IA « classique » (le GOFAI) était de **capturer la connaissance dans des règles
explicites**. Les **[systèmes experts](docs/module1/50-systemes-experts)** en sont l'aboutissement : une
**base de règles** `si… alors…`, une **base de faits** (le cas qu'on traite), et un
**moteur d'inférence** qui confronte les deux, déclenche les règles applicables, et
en tire de nouvelles conclusions — jusqu'au diagnostic final.

Dans ce travail, vous allez incarner ce moteur d'inférence sur un petit système
expert qui **identifie des animaux** à partir de leurs caractéristiques. Vous le
ferez *tourner*, vous le mettrez *en échec*, puis vous tenterez de l'*améliorer* — et
vous éprouverez, de l'intérieur, ce qu'on a appelé le **[goulot d'étranglement de la
connaissance](docs/module1/50-systemes-experts)**.

Une règle a la forme suivante :

```
SI  (mammifère)  ET  (mange de la viande)   ALORS  (carnivore)
```

Les conditions d'une règle sont **toujours reliées par des ET, jamais par des OU** :
une règle ne se déclenche que si **toutes** ses conditions sont vraies *en même
temps*. Dans l'exemple ci-dessus, il faut que `mammifère` **et** `mange de la viande`
soient tous deux vrais pour conclure `carnivore` ; l'un des deux seul ne suffit pas.
(Pour exprimer un « OU » — par exemple `a du poil` **ou** `allaite ses petits` →
`mammifère` —, on écrit tout simplement **deux règles séparées**, ce que fait
justement la base avec R1 et R2.)

Le « savoir » du système n'est rien d'autre qu'une pile de telles règles ; son
« raisonnement », un simple mécanisme qui regarde *quelles règles ont toutes leurs
conditions réunies*. Toute l'intelligence du système tient, comme nous le verrons,
dans une seule formule.

## Consignes

1. Ouvrez le [fichier Google Sheets fourni pour ce travail](https://docs.google.com/spreadsheets/d/1R6-yobTFy5XE9eUPg_XhnjEZ3efEQU0V76uQSBtPwIc/edit?usp=sharing)
   et **faites-en une copie** (*Fichier ▸ Créer une copie*) : vous ferez tout votre
   travail à partir de **votre copie**.

2. Une fois vos manipulations terminées, [partagez votre fichier](docs/50-google-sheets/#fonction-de-partage-anonyme-dun-fichier) et copiez le lien vers celui-ci dans un document PDF (**Attention&nbsp;: aucun autre format que PDF ne sera accepté**).

3. Répondez aux questions d'interprétation de la dernière section dans le même
   fichier PDF, en fournissant des réponses claires et précises.

## Le système

Le classeur ne comporte que **deux onglets** — il *est* le système expert réduit à
l'essentiel : une base de faits et une base de règles, rien de plus.

- **Faits** — la liste de toutes les caractéristiques possibles (les *attributs
  observables* comme `a du poil`, mais aussi les *catégories* déduites comme
  `mammifère` et les *espèces*). Chaque fait a une case **Vrai ?** à cocher.
- **Base de règles** — les 11 règles `si… alors…`, sous forme de conditions et d'une
  conclusion.

Le cœur du système est la colonne **« Activable ? »** de la *Base de règles*. Pour
chaque règle, cette unique formule vérifie que **toutes ses conditions sont vraies**
dans l'onglet *Faits*, et que sa conclusion n'a pas déjà été établie :

```
=IF($F2="","",AND(
   IF($B2="",TRUE,VLOOKUP($B2,Faits!$A:$B,2,FALSE)),
   IF($C2="",TRUE,VLOOKUP($C2,Faits!$A:$B,2,FALSE)),
   IF($D2="",TRUE,VLOOKUP($D2,Faits!$A:$B,2,FALSE)),
   IF($E2="",TRUE,VLOOKUP($E2,Faits!$A:$B,2,FALSE)),
   NOT(VLOOKUP($F2,Faits!$A:$B,2,FALSE))))
```

Quand une règle est activable, sa ligne se **surligne en vert** : elle est « prête à
se déclencher ». C'est *vous* qui jouez le moteur : vous choisissez une règle verte
et vous **cochez sa conclusion** dans l'onglet *Faits* — ce qui rend de nouvelles
règles vertes, et ainsi de suite.

Dans un vrai système expert, ce travail est entièrement **automatique** : un
programme — le *moteur d'inférence* — parcourt sans relâche la base de règles,
repère celles dont toutes les conditions sont réunies, les déclenche, ajoute leurs
conclusions à la base de faits, puis recommence, jusqu'à ce que plus aucune règle
ne s'applique. L'humain n'intervient pas. Ici, **pour des raisons pédagogiques, c'est
vous qui tenez ce rôle** : vous exécutez « à la main » l'algorithme que la machine
ferait tourner toute seule. Le but est précisément de vous faire *sentir*, de
l'intérieur, à quel point ce raisonnement est mécanique — une simple boucle qui
applique des règles, sans la moindre compréhension de ce qu'est un guépard ou un
manchot.

<!-- CAPTURE À AJOUTER : onglet Base de règles avec une règle surlignée en vert -->

## Manipulation 1 — Tracer le raisonnement

Voici le **Cas 1** : cochez `a du poil`, `mange de la viande`, `robe fauve` et
`taches sombres` dans l'onglet *Faits* (laissez tout le reste à FAUX).

Une seule règle devient verte : **R1**. Déclenchez-la (cochez sa conclusion,
`mammifère`, dans l'onglet *Faits*). Une nouvelle règle s'active ; déclenchez-la à
son tour ; et continuez jusqu'à ce qu'une **espèce** passe à VRAI.

Au fur et à mesure, **tenez la trace** de votre raisonnement directement dans votre
document PDF, sous la forme d'un petit tableau — une ligne par règle déclenchée :

| Étape | Règle déclenchée | Nouveau fait établi | Pourquoi (conditions réunies) |
|-------|------------------|---------------------|-------------------------------|
| 1     | R1               | `mammifère`         | `a du poil` est vrai          |
| 2     | …                | …                   | …                             |

Recommencez ensuite avec le **Cas 2** — le manchot (`a des plumes`,
`incapable de voler`, `nage`, `plumage noir et blanc`) — après avoir remis tous les
faits à FAUX.

## Manipulation 2 — Casser le système

Remettez tous les faits à FAUX, puis chargez le **Cas 3** : `a du poil`,
`a des sabots`, `rumine`.

Faites tourner le moteur. Vous obtenez `mammifère`… puis **plus rien** : aucune
règle d'espèce ne devient verte. Le système est **bloqué** — il ne sait pas
identifier cet animal (il s'agit, par exemple, d'une **antilope**).

## Manipulation 3 — Étendre la base de règles

À vous d'ajouter le savoir manquant. Sur la première ligne vide de la *Base de
règles*, écrivez une nouvelle règle qui conclut `antilope`. Servez-vous des **menus
déroulants** pour les conditions (et ajoutez l'espèce `antilope` à l'onglet *Faits*
si elle n'y est pas, en n'oubliant pas d'ajouter une case à cocher correspondante, ainsi que tout nouvel attribut dont vous auriez besoin).

Vérifiez que votre règle identifie bien le Cas 3. Puis **testez sa solidité** :
chargez un autre animal (par exemple le **zèbre** : `a du poil`, `a des sabots`,
`rayures noires`). Votre nouvelle règle se déclenche-t-elle *aussi*, par erreur&nbsp;?
Ajustez-la s'il le faut.

<!-- CAPTURE À AJOUTER : la nouvelle règle ajoutée dans la Base de règles -->

## Questions d'interprétation

1. Pour le Cas 1, combien de règles se sont déclenchées, et dans quel ordre&nbsp;?
   Décrivez la **cascade** : en quoi la conclusion d'une règle sert-elle de condition
   à une autre&nbsp;?

2. Dans ce système, le « savoir » (la base de règles) et le « raisonnement » (le
   moteur) sont **séparés**. Si l'on remplaçait entièrement la base de règles par des
   règles de diagnostic automobile, qu'est-ce qui changerait, et qu'est-ce qui
   resterait identique&nbsp;?

3. Le système peut **expliquer** sa conclusion (le tableau de trace que vous avez
   rempli en est la preuve). En quoi est-ce une force&nbsp;? Comparez avec ce que vous
   anticipez d'un réseau de neurones (Module 3).

4. Vous avez fait tourner le moteur « vers l'avant » (des faits vers la conclusion) :
   c'est le **chaînage avant**. Comment auriez-vous procédé pour vérifier une
   hypothèse précise (« et si c'était un tigre&nbsp;? ») sans tout cocher d'avance —
   c'est-à-dire en **chaînage arrière**&nbsp;?

5. Au Cas 3, pourquoi exactement le système s'est-il bloqué&nbsp;? Qu'est-ce que cela
   révèle sur sa capacité à gérer un cas **imprévu**&nbsp;?

6. La règle que vous avez ajoutée risquait-elle de **mal classer** d'autres
   animaux&nbsp;? Racontez ce que vous avez observé en la testant sur le zèbre, et ce
   que cela dit de la difficulté de maintenir une grosse base de règles.

7. Imaginez qu'on veuille étendre ce système pour identifier **tous les animaux du
   monde**. Décrivez concrètement ce qui se passerait pour la base de règles. Quel
   concept des chapitres « [Capturer l'expertise](docs/module1/50-systemes-experts) »
   et « [Les hivers et la bascule](docs/module1/60-hivers) » cela illustre-t-il&nbsp;?

8. Un zoologiste reconnaît souvent un animal « d'un coup d'œil », sans pouvoir
   énoncer la règle exacte qu'il applique. Quel nom donne-t-on à ce type de savoir,
   et pourquoi pose-t-il problème à un système expert&nbsp;?

9. Ce système **apprend-il** de son expérience&nbsp;? Si on lui présentait mille
   animaux, ses règles s'amélioreraient-elles toutes seules&nbsp;? Quelle conséquence
   cela a-t-il, et vers quel changement de paradigme (Module 2) cela pointe-t-il&nbsp;?

10. Toute « l'intelligence » du moteur tient dans la formule de la colonne
    *Activable ?*. Diriez-vous que ce système *pense*&nbsp;? Reliez votre réponse au
    [test de Turing](docs/module1/10-turing) et à l'[« effet IA »](docs/module1/60-hivers).

11. Les systèmes experts ont presque disparu sous ce nom — mais leur mécanisme
    survit (voir « [Les hivers et la bascule](docs/module1/60-hivers) »). Donnez un
    exemple, tiré de la vie courante, d'un endroit où
    une base de règles `si… alors…` décide encore quelque chose à votre sujet.
