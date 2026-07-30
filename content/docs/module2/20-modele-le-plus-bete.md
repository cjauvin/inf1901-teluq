---
title: "Le modèle le plus bête"
weight: 20
slug: modele-le-plus-bete
---

# Le modèle le plus bête

À la fin de la page précédente, nous nous sommes posé une question presque
absurde : quelle est la prédiction la plus bête qu'on puisse imaginer ?
Prenons-la au sérieux — car la pire réponse possible a, paradoxalement, beaucoup
à nous apprendre. Et, chemin faisant, elle va nous obliger à dire ce qu'est, au
juste, un *modèle*.

## Toujours prédire la moyenne

Voici donc le pire « prédicteur » concevable : pour *n'importe quelle* maison, on
ignore tout d'elle — sa superficie, son âge, son nombre de chambres — et on
annonce toujours le **même** prix : le **prix moyen** de toutes les maisons de
notre liste.

Dans notre exemple, ce prix moyen tourne autour de **500 000 \\$**. La prédiction
ne dépend alors plus de rien : un minuscule studio ? 500 000 \\$. Un vaste manoir ?
500 000 \\$ aussi. C'est manifestement ridicule.

Et pourtant — c'est parfaitement défini, ça ne « plante » jamais, et ça donne
toujours une réponse. Sur le nuage de points de la page précédente, ce
prédicteur se réduit à une simple **ligne horizontale** : la même hauteur
(500 000 \\$) quelle que soit la superficie. Elle traverse le nuage en son milieu,
au-dessus des maisons bon marché, en dessous des plus chères.

{{< image src="/images/module2/maisons-baseline.svg" alt="Le nuage de maisons traversé par une droite horizontale à 500 000 $ : un modèle qui prédit toujours le prix moyen, sans tenir compte de la superficie." title="Le modèle le plus bête : une droite plate à 500 000 $, qui ignore complètement la superficie." loading="lazy" >}}

## La même bêtise, pour l'autre question

Et si l'on nous posait plutôt la **seconde question** du chapitre précédent —
*cette maison partira-t-elle vite ?* Le prédicteur le plus bête existe là aussi,
et il obéit à la même logique : ignorer superbement la maison qu'on lui présente,
et répondre toujours la même chose.

Mais répondre quoi ? Pas la moyenne, cette fois : on ne peut pas faire la moyenne
de « oui » et de « non ». La bêtise équivalente consiste à donner **la réponse la
plus fréquente**, celle qui revient le plus souvent dans nos registres. Si, parmi
les maisons déjà vendues, 60 % ont trouvé preneur en moins de trente jours, notre
prédicteur bête répondra « oui » — toujours, pour un studio comme pour un manoir.

Deux questions de nature très différente, et pourtant la **même ossature** : une
entrée qu'on ignore, une sortie constante, et une réponse tirée des seules
données. C'est la première fois que nous voyons cette parenté ; ce ne sera pas la
dernière.

## Qu'est-ce qu'un modèle, au juste ?

Nous venons d'appeler ce prédicteur un « modèle ». Profitons-en pour fixer le
sens de ce mot, car il sera au cœur de tout le module.

> Un **modèle**, c'est une recette qui transforme une description (l'entrée) en
> une prédiction (la sortie).

C'est tout. Notre prédicteur bête y entre de plein droit : on lui donne une
maison en entrée, il renvoie un prix en sortie. Qu'il ignore superbement cette
entrée ne le disqualifie pas — ça en fait juste un *très mauvais* modèle, pas un
non-modèle.

Remarquez de quoi ce modèle est fait : **un seul nombre**, le prix moyen
(500 000 \\$). Ce nombre, c'est ce que le modèle a « retenu » des données ; on
l'appelle son **paramètre**. Et le calculer — faire la moyenne des prix observés
— c'est déjà une forme rudimentaire d'*apprentissage* : le modèle a tiré son
unique connaissance des exemples qu'on lui a montrés. Son jumeau ne fonctionne
pas autrement : son unique paramètre, à lui, est la réponse majoritaire (« oui »),
obtenue en comptant plutôt qu'en moyennant.

Tout le reste du module ne fera qu'enrichir cette image. Les modèles que nous
construirons auront davantage de paramètres — un, puis deux, puis des milliers,
puis des milliards — et toute la difficulté consistera à trouver les *bonnes
valeurs* pour ces paramètres, celles qui collent le mieux aux données. Mais
l'ossature, elle, ne changera jamais : une entrée, une recette réglée par des
paramètres, une sortie.

## Pourquoi un modèle aussi bête est utile

Si ce modèle est si mauvais, pourquoi s'y attarder ? Parce qu'il nous offre un
**étalon** — un point de comparaison contre lequel juger tous les modèles à
venir.

« Bon » et « mauvais » ne veulent en effet rien dire dans l'absolu. Pour savoir
si un modèle vaut quelque chose, il faut une référence ; et la plus honnête qui
soit, c'est : *fait-il mieux que de ne rien regarder du tout ?* Un modèle, si
sophistiqué soit-il, incapable de battre « toujours 500 000 \\$ » n'aurait,
littéralement, rien appris d'utile.

On peut rendre cette comparaison concrète sans la moindre formule : il suffit de
mesurer **de combien un modèle se trompe, en moyenne**. Pour le prédicteur bête,
l'écart entre le prix annoncé (toujours 500 000 \\$) et le vrai prix peut atteindre
des centaines de milliers de dollars aux extrêmes. C'est exactement cette
« distance à la vérité » qu'un meilleur modèle cherchera à réduire. Nous lui
donnerons plus loin un nom et une définition précise — la *fonction d'erreur* —,
mais l'intuition suffit ici : un bon modèle, c'est un modèle qui se trompe moins.

{{< image src="/images/module2/maisons-erreurs.svg" alt="Le nuage de maisons et la droite plate à 500 000 $, avec un segment vertical rouge reliant chaque maison à la droite : c'est l'erreur du modèle sur cette maison, longue aux extrêmes et courte près du centre." title="L'erreur du modèle, maison par maison : l'écart vertical entre le vrai prix et la prédiction." loading="lazy" >}}

C'est ce rôle d'étalon qui, en pratique, évite bien des illusions. Un chiffre de
performance ne signifie rien tout seul : la première question à poser devant un
modèle est toujours *« fait-il vraiment mieux que de prédire bêtement la
moyenne ? »*. Étonnamment souvent, la réponse est non — et c'est précisément
l'étalon qui le révèle.

Pour la question en oui/non, le principe est identique ; seule la façon de
compter change. Plutôt qu'un écart en dollars, on regarde tout simplement **quelle
proportion des réponses le modèle obtient justes**. Notre prédicteur jumeau, qui
répond « oui » à tout, aura donc raison dans 60 % des cas : voilà l'étalon à
battre.

{{< image src="/images/module2/maisons-erreurs-oui-non.svg" alt="Exactement le nuage coloré de la page précédente — les mêmes maisons, aux mêmes places, la superficie en abscisse et l'année de construction en ordonnée. Mais toutes sont maintenant bleues : le modèle répond « oui » — vendue en moins de 30 jours — pour chacune, sans jamais les regarder. Un ✗ rouge barre celles qui avaient en réalité traîné, c'est-à-dire précisément celles qui étaient rouges sur la figure d'origine : ce sont ses erreurs." title="Le prédicteur jumeau à l'œuvre. Il peint toutes les maisons en « oui » ; les ✗ marquent celles où il se trompe. On ne mesure plus un écart en dollars — on compte les réponses justes." loading="lazy" >}}

C'est le nuage coloré de la page précédente, à l'identique : les **mêmes
maisons**, aux mêmes places. Seule leur couleur a changé — le modèle répondant
« oui » partout, il les peint toutes en bleu, et les ✗ signalent celles qui
étaient rouges. Remarquez que les ✗ se groupent en bas du dessin, du côté des
maisons anciennes : c'est là que le prédicteur bête se trompe, et c'est bien
normal, puisqu'il répond « oui » sans jamais regarder l'année.

Comparez maintenant avec le graphique des écarts de prix, quelques lignes plus
haut. Les axes ne sont pas les mêmes — ils ne peuvent pas l'être, les deux
questions ne se lisant pas dans le même plan —, mais ce n'est pas là qu'est le
contraste. Là, chaque maison portait un segment plus ou moins long, et l'erreur
se **mesurait** ; ici, chaque maison est simplement juste ou fausse, et l'erreur
se **compte**.

{{% hint warning %}}
Cet étalon-là réserve une surprise, et elle est instructive. Imaginez une question
bien plus déséquilibrée : *ce courriel est-il un pourriel ?*, dans une boîte où
99 % des messages sont légitimes. Le prédicteur le plus bête — « ce n'est jamais
un pourriel » — obtient d'emblée **99 % de bonnes réponses**… tout en étant
parfaitement inutile, puisqu'il ne détecte aucun pourriel. Un chiffre flatteur
peut donc masquer un modèle sans la moindre valeur. Nous y reviendrons : *bien*
mesurer la qualité d'un modèle est autrement plus subtil qu'il n'y paraît.
{{% /hint %}}

## Son défaut, et ce qu'il révèle

Le défaut de notre modèle saute aux yeux : il accorde le **même** prix à un
studio et à un manoir. Il n'a, à aucun moment, *regardé* la maison qu'on lui
présente. Toute l'information utile — la superficie, l'âge, le nombre de chambres
— est là, sous ses yeux, et il la jette.

C'est précisément là que se loge la marge de progression. Si le prix moyen est
notre meilleur point de départ *tant qu'on ignore tout* d'une maison, alors la
seule façon de faire mieux est de **cesser de l'ignorer** : tenir compte de ses
caractéristiques. Une grande maison devrait tirer la prédiction vers le haut ;
une vieille bicoque, vers le bas. Un bon modèle, ce sera un modèle qui *écoute*
l'entrée.

Mais avant de pouvoir s'en servir, encore faut-il savoir ce qu'« écouter
l'entrée » signifie concrètement. Qu'est-ce, au juste, qu'une « donnée » pour une
machine ? Comment une maison — ou une image, ou un courriel — se transforme-t-elle
en quelque chose qu'un modèle peut manipuler ? C'est l'objet de la [page
suivante](docs/module2/30-les-donnees).
