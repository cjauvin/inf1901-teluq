---
title: "Regarder les données"
weight: 30
slug: les-donnees
---

# Regarder les données

La page précédente s'est close sur une exigence : pour faire mieux que la
moyenne, un modèle doit *tenir compte* des caractéristiques d'une maison — sa
superficie, son âge, son nombre de chambres. Encore faut-il les lui présenter
sous une forme qu'il puisse manipuler.

Car une machine ne « voit » ni une maison, ni une photo, ni un courriel : elle
ne manipule que des **nombres**. Toute la question — étonnamment profonde — est
donc celle-ci : comment transformer un objet du monde réel en nombres, sans en
perdre l'essentiel ? C'est l'affaire de cette page, et un préalable à *tout* ce
qui suivra.

## Une maison, c'est une liste de nombres

Reprenons notre table de maisons. Chaque ligne décrit une maison par quelques
**caractéristiques** (en anglais *features*) — des grandeurs mesurables :

| Superficie (m²) | Année | Chambres | Salles de bain | Prix |
|---|---|---|---|---|
| 180 | 1995 | 4 | 2 | 420 000 \\$ |
| 150 | 1980 | 3 | 1 | 350 000 \\$ |
| 220 | 2010 | 5 | 3 | 580 000 \\$ |
| 130 | 1972 | 3 | 1 | 310 000 \\$ |

Pour une machine, décrire la première maison, c'est simplement aligner ses
caractéristiques :

$$\text{maison} \rightarrow (180,\ 1995,\ 4,\ 2)$$

Cette liste ordonnée de nombres porte un nom : un **vecteur**. Peu importe
l'objet — une maison, un client, un patient, un courriel — du moment qu'on sait
le décrire par une poignée de grandeurs, il devient un vecteur de nombres, et
c'est *cela* qu'un modèle reçoit en entrée.

Une précision de vocabulaire, utile pour toute la suite : le **prix**, lui, ne
fait pas partie de cette description — c'est justement la valeur qu'on cherche à
*prédire*. On l'appelle la **cible**. On a donc, d'un côté, les caractéristiques
(l'entrée du modèle), et de l'autre, la cible (sa sortie attendue).

{{< image src="/images/module2/modele-entree-sortie.svg" alt="Schéma : à gauche les caractéristiques d'une maison (superficie, année, chambres, salles de bain) ; une flèche vers une boîte « modèle » ; une flèche en sortie vers le prix (420 000 $)." title="Un modèle : les caractéristiques entrent, le prix sort." loading="lazy" >}}

### Et quand la cible est une catégorie ?

Le prix est un nombre : il se prête sans difficulté à cette mise en forme. Mais
souvenez-vous de notre seconde question — *cette maison va-t-elle partir vite ?*
Sa réponse, elle, est un **oui** ou un **non**. Or nous venons de le dire : une
machine ne manipule que des nombres. Comment lui faire avaler un « oui » ?

De la façon la plus simple qui soit : en décidant que **oui vaut 1 et non vaut
0**. Le choix est arbitraire — on aurait pu prendre l'inverse, ou n'importe quel
autre couple de valeurs — mais il a l'immense avantage de faire de la cible une
grandeur comme une autre. Une fois cette convention posée, une catégorie n'est
plus qu'un nombre, et tout ce qui suit s'applique sans changement.

Cela permet aussi d'éclairer, rétrospectivement, un détail du premier chapitre.
Nous y avions dessiné les mêmes maisons en coloriant chaque point selon qu'elle
s'était vendue vite ou non — faute de place pour un troisième axe. Maintenant que
nous savons que la cible est un nombre, nous pouvons lui **donner cet axe** :

{{< image src="/images/module2/troisieme-dimension.svg" alt="Vue en perspective des mêmes maisons. Le plan horizontal porte deux caractéristiques, la superficie et le prix. La cible occupe un troisième axe, vertical, qui ne comporte que deux niveaux : 0 (non) en bas et 1 (oui) en haut. Chaque maison se pose donc sur l'un ou l'autre de deux plans superposés — les maisons vendues vite sur le plan du haut, celles qui ont traîné sur celui du bas." title="La cible a bel et bien son propre axe : simplement, quand elle est une catégorie, cet axe ne compte que deux barreaux, 0 et 1." loading="lazy" >}}

Les maisons ne flottent plus à n'importe quelle hauteur : elles se posent sur
l'un ou l'autre de **deux plans**. Et l'on passe d'un dessin à l'autre sans rien
perdre — regardez ce relief *d'en haut*, à la verticale, et vous retrouverez
trait pour trait le nuage colorié du premier chapitre. Cette couleur, c'était
l'ombre portée de ce troisième axe.

Attention toutefois à ne pas confondre : cet axe-là n'est pas de même nature que
les autres. La superficie et le prix sont des **caractéristiques**, elles
*décrivent* la maison et forment l'espace où elle vit ; la cible, elle, est ce
qu'on **cherche**. Dans tout ce qui suit, quand nous parlerons des *dimensions*
d'un objet, il s'agira toujours des caractéristiques.

Nous tenons maintenant de quoi nommer ces deux familles de problèmes, car chacune
porte un nom que vous rencontrerez partout :

- prédire un **nombre** — un prix, une température, une durée — s'appelle une
  **régression** ;
- prédire une **catégorie** — vendue vite ou non, pourriel ou courriel, chat ou
  chien — s'appelle une **classification**.

Rien de plus : la seule chose qui les distingue est la **nature de la cible**.
C'est pourtant l'une des partitions les plus utiles du domaine, car presque tout
problème d'apprentissage à partir d'exemples étiquetés tombe dans l'une ou dans
l'autre. Nous les retrouverons constamment — et nous verrons que certains
algorithmes savent faire les deux, quand d'autres se spécialisent.

## Un vecteur, c'est un point dans un espace

Représenter une maison par un vecteur de nombres ne fait pas que ranger ses
caractéristiques : ça lui donne une **place dans l'espace**.

Prenons deux caractéristiques, la superficie et le nombre de chambres. On peut
alors placer chaque maison comme un **point** sur un graphe : la superficie en
horizontale, le nombre de chambres en verticale. Une maison se résume à un
endroit du plan — exactement comme, sur le nuage des pages précédentes, chaque
maison était déjà devenue un point. Un vecteur à deux composantes, c'est donc une
position dans un plan.

Et rien n'oblige à s'arrêter à deux. Ajoutez l'année de construction : la maison
devient un point dans un espace à **trois** dimensions, comme une mouche
immobile quelque part dans une pièce. Une quatrième caractéristique ? Un point
dans un espace à quatre dimensions. La règle ne change jamais : **autant de
nombres pour décrire un objet, autant de dimensions dans l'espace où il vit.**

{{< image src="/images/module2/nf_house.png" alt="Diagramme à plusieurs axes, un par caractéristique : superficie, année de construction, nombre de chambres, … nombre de salles de bain. Deux maisons y sont placées comme des points, chacune accompagnée de son vecteur : {180, 1995, 4, … 2} en bleu et {220, 2010, 5, … 3} en rouge — deux maisons de la table, dans le même espace à n dimensions." title="Chaque caractéristique devient un axe : une maison est un point dans un espace à autant de dimensions qu'elle a de caractéristiques." loading="lazy" >}}

Cette image géométrique est étonnamment puissante. Deux maisons aux
caractéristiques semblables seront deux points *proches* ; deux maisons très
différentes, deux points *éloignés*. La ressemblance entre objets devient une
**distance** entre points — une idée dont le prochain chapitre fera son miel.

## Quand il y a trop de dimensions pour les voir

Nos maisons se contentaient de trois ou quatre caractéristiques — on pouvait
presque les imaginer comme des points dans une pièce. Mais beaucoup d'objets du
monde réel se décrivent par *bien* plus de nombres.

Prenez une image. Pour une machine, une photo n'est qu'une **grille de pixels**,
et chaque pixel est un nombre (ou trois : ses doses de rouge, de vert et de
bleu).

{{< image src="/images/module2/2d_house.png" alt="Une photo de maison posée sur des axes x et y : pour une machine, une image est une grille de pixels." title="Une image, pour une machine : une grille de pixels, chacun un nombre." loading="lazy" >}}

On pourrait, bien sûr, la représenter autrement — par exemple, s'il s'agissait
d'une maison de jeu vidéo, par un modèle en trois dimensions, avec ses axes x, y
et z :

{{< image src="/images/module2/3d_house.png" alt="Une maison en fil de fer sur des axes x, y et z : un modèle tridimensionnel, comme dans un jeu vidéo." title="Autre représentation : un modèle 3D, repéré par des axes x, y, z." loading="lazy" >}}

Mais en apprentissage automatique, on fait quelque chose de plus radical : on
traite l'image **entière** comme un seul point, dans un espace où *chaque pixel
est une dimension*. Une vignette de 100 × 100 pixels ? Un point dans un espace à
10 000 dimensions. Une photo ordinaire ? Des **millions** de dimensions.

{{< image src="/images/module2/nd_house.png" alt="Une photo de maison placée comme un point dans un espace à de nombreux axes (x1…xn), avec un second exemplaire plus pâle : une image est un point dans un espace de très haute dimension, et deux images semblables sont deux points voisins." title="En haute dimension : l'image entière devient un seul point ; deux images semblables, deux points voisins." loading="lazy" >}}

Impossible de se représenter un tel espace — nous, créatures à trois dimensions,
en sommes bien incapables. Et pourtant, l'essentiel survit : **la distance
continue d'avoir un sens.** Deux photos presque identiques sont deux points
*voisins* ; deux images sans rapport, deux points très *éloignés*. Exactement
comme pour nos maisons.

C'est là toute la force de l'idée. Maison, image, courriel : du moment qu'on sait
décrire un objet par des nombres, il devient un point dans un espace, et leur
ressemblance se mesure par leur proximité. C'est précisément ce dont le prochain
chapitre va se servir pour **prédire par ressemblance**.

{{% details "Sous le capot : des vecteurs aux bits (optionnel)" %}}

Nous venons de dire qu'une machine « ne manipule que des nombres ». Mais
qu'est-ce qu'un nombre, *physiquement*, pour un ordinateur ? Voici la descente —
du vecteur jusqu'au fil électrique. Elle n'est pas indispensable à la suite du
module, mais elle éclaire ce qui se passe sous le capot.

**Niveau des bits**

Au niveau le plus fondamental, l'ordinateur ne peut traiter qu'un seul type de
donnée : le **bit**, qui est à la fois un concept mathématique (un symbole dont
la valeur ne peut être que `0` ou `1`, ou `vrai`/`faux` en logique) et physique,
au niveau de l'implémentation : électrique (RAM, CPU, SSD), magnétique (disque
dur) ou optique (CD). Les bits *représentent* les nombres via la convention de
l'encodage binaire.

![](/images/module2/binary_enc.png)

**Niveau du processeur (le CPU)**

Au niveau suivant, on trouve l'ordinateur lui-même, dont le mécanisme central est
le microprocesseur (CPU). Un CPU traite les bits sous leur forme physique, et il
interprète des « paquets » (ou *mots*) de bits de taille déterminée (souvent 32,
64 ou 128 bits) de deux manières fondamentalement différentes :

1. en tant que *nombre* (ou plus généralement *valeur*) ;
2. en tant qu'*instruction*.

Le flot de bits auquel est exposé le CPU constitue un *programme*, que le CPU
*exécute* séquentiellement. Un programme dans un « langage machine » fictif
pourrait être :

```
MOV 1000
ADD 0001
STR 2000
```

Les symboles `MOV`, `ADD` et `STR` sont des instructions, qui correspondent
elles-mêmes à des nombres. Le CPU verrait peut-être la séquence :

```
1000 1000
1001 0001
1002 2000
```

si `MOV`, `ADD` et `STR` correspondaient par convention aux valeurs 1000, 1001 et
1002. La signification du programme pourrait être :

```
- Prendre la valeur à l'adresse mémoire 1000 et la mettre dans un registre
- Ajouter 1 à cette valeur dans le registre
- Enregistrer le contenu du registre à l'adresse mémoire 2000
```

Comment le CPU distingue-t-il `1000` *instruction* de `1000` *valeur* ? Par des
conventions préétablies (par exemple : positions paires = instructions, impaires
= valeurs ; la réalité est un peu plus subtile, mais l'idée est là). Et
qu'exécute le CPU pour réaliser une instruction ? Un mini-programme, câblé
directement dans ses circuits. C'est l'endroit où la logique et la matière se
touchent !

Vous pouvez exécuter vous-même, pas à pas, une version interactive de ce
mini-programme :

{{< applet src="/html/applets/cpu-simulator.html" >}}

**Niveau des langages de programmation**

Le niveau suivant est implémenté dans le langage du précédent : tout comme on
peut écrire un jeu ou un système d'exploitation en langage machine, on peut y
écrire… un autre langage ! Plus *abstrait*, plus éloigné de la réalité physique,
il permet d'exprimer des idées plus complexes de façon plus naturelle (C++,
Python, JavaScript). On peut le voir comme un « ordinateur virtuel » implémenté
en termes d'un langage moins abstrait. À ce niveau apparaissent des
représentations bien plus riches :

- des nombres entiers ;
- des nombres réels (bien plus complexes à représenter !) ;
- des chaînes de caractères ;
- des listes de nombres, de mots, de listes… ;
- des images, des sons ;
- etc.

C'est à ce niveau que sont écrits, justement, les algorithmes d'apprentissage
automatique — et que vivent les *vecteurs* dont parle cette page.

**Retour vers les symboles**

On comprend mieux, maintenant, la distinction souvent évoquée entre l'IA
classique, qui manipule des **symboles**, et l'apprentissage automatique, qui
manipule des **valeurs numériques** — et dont on dit parfois qu'il est
*sub-symbolique*. Au fond, les deux manipulent des données qui sont *ultimement*
des valeurs numériques (et même des bits physiques) ; mais il reste un sens clair
à distinguer les deux types de mathématiques sur lesquels ils se fondent.

![](/images/module2/schema_repr_donnees.png)

{{% /details %}}
