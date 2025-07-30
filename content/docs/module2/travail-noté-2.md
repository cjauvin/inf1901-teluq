---
title: "Travail noté 2"
weight: 100
---

# Classification naïve bayésienne pour détecter les pourriels

La classification naïve bayésienne est un algorithme d'apprentissage supervisé
qui fonctionne avec les probabilités. Un problème classique qui peut être traité
avec cet algorithme est la classification de courriels. On peut tenter d'estimer
la probabilité qu'un courriel soit en fait un pourriel en prenant en compte les
mots particuliers qu'il contient, l'idée étant que certains mots auront tendance
à être plus souvent utilisés dans des pourriels.

La probabilité qui nous intéresse est en fait une probabilité conditionnelle,
celle du fait qu'un courriel particulier soit ou non un pourriel, étant donné
les mots particuliers qui le composent. Un courriel sera classifié en tant que
pourriel si :

$$\text{Prob(oui c'est un pourriel | mots)} > \text{Prob(non ce n'est pas un | mots)}$$

## Entraînement du modèle

Voyons comment il est possible de calculer ces probabilités en entraînant un
modèle de classification sur une série de courriels particuliers.

Étant donné que nous allons encore une fois utiliser la tableur en ligne [Google
Sheets]({{< relref "docs/google-sheets.md" >}}), assurez-vous que votre version
est correctement configurée.

Copiez tout d'abord ces 10 courriels dans la colonne A d'une nouvelle "feuille"
Google Sheets, un courriel par rangée :

```
voici le colis est arrivé
bonjour voici le lien
offre spéciale colis gratuit
merci pour votre colis
colis livré demain matin
voici votre carte gratuite
réunion demain à midi
voici le code pour carte
livraison spéciale pour vous
merci encore pour votre carte
```

Pour avoir un aperçu de la tâche d’étiquetage des données (qui dans un scénario
réel peut s'avérer très coûteuse et laborieuse), vous êtes invités à tenter tout
d'abord de catégoriser les courriels dans la colonne B, en utilisant la valeur
"oui" si vous considérez qu'il s'agit d'un pourriel, ou "non" (ce n'est pas un
pourriel) sinon.

Si vous n'avez pas envie de vous soumettre à cet exercice à ce stade,
vous pouvez toujours copier ces valeurs (dans la colonne B) :

```
non
non
oui
non
non
oui
non
non
oui
non
```

À ce stade, votre feuille devrait ressembler à ceci :

![](/images/module2/tn2/sheets_cols_a_et_b.png)

Calculons tout d'abord dans la colonne C la probabilité à priori qu'un
courriel quelconque soit un pourriel ou non (sans prendre en
considérations les mots donc, pour le moment) :

```
=MAP(UNIQUE(B1:B10), LAMBDA(x, COUNTIF(B1:B10, x) / COUNTA(B1:B10)))
```

Ces probabilités à priori nous serviront plus loin. Définissez ensuite
la colonne D avec cette formule :

```
=UNIQUE(TRANSPOSE(SPLIT(TEXTJOIN(" ", TRUE, A:A), " ")))
```

La colonne D devrait maintenant contenir le vocabulaire des courriels :

![](/images/module2/tn2/sheets_col_d_voc.png)

La colonne E devrait ensuite correspondre au nombre de fois où les
mots de la colonne D apparaissent dans les courriels valides (qui donc
"non", ne sont pas des pourriels) :

```
=SUMPRODUCT((B$1:B$10="non") * ISNUMBER(SEARCH(D1, A$1:A$10)))
```

et de manière similaire pour la colonne F et la fréquence des mots qui
apparaissent dans les courriels qui "oui", sont des pourriels :

```
=SUMPRODUCT((B$1:B$10="oui") * ISNUMBER(SEARCH(D1, A$1:A$10)))
```

Notez que les colonnes E et F doivent avoir le même nombre d'éléments
que la colonne D (il faut donc utiliser la fonction de remplissage
automatique, pour laquelle le plus simple est de soit glisser (drag)
la première cellule vers le bas, une fois qu'elle a été calculée, ou
encore de double-cliquer sur le petit "+" noir qui apparait en bas à
droite de la première cellule).

![](/images/module2/tn2/sheets_col_e_drag.png)

![](/images/module2/tn2/sheets_cols_e_et_f.png)

À partir de ces fréquences de mots pour chaque classe ("oui" ou
"non"), on peut maintenant calculer la probabilité conditionnelle de
chaque mot du vocabulaire, étant donné le fait qu'un courriel soit
"oui" ou "non" un pourriel. Donc la colonne G correspond à la
probabilité des mots étant donné que "non" il ne s'agit pas d'un
pourriel :

```
=(E1 + 1) / (SUM(E:E) + COUNTA(D:D))
```

et de manière similaire la colonne H est la probabilité des mots quand
on sait que "oui" il s'agit d'un pourriel :

```
=(F1 + 1) / (SUM(F:F) + COUNTA(D:D))
```

Encore une fois les colonnes G et H doivent avoir la même taille que
celle du vocabulaire (colonne D), il faut donc s'assurer d'utiliser le
mécanisme du remplissage automatique décrit précédemment.

![](/images/module2/tn2/sheets_cols_g_et_h.png)

Notre modèle est maintenant entièrement entraîné, et il est donc prêt
pour son utilisation!

## Utilisation du modèle (inférence)

Nous allons maintenant utiliser le modèle pour déterminer si un
nouveau courriel (qui n'a pas servi à l'entraînement) est un pourriel
ou non. Dans la colonne I entrez un courriel à tester :

```
voici votre carte spéciale
```

Faites l'extraction des mots du courriel dans la colonne J :

```
=TRANSPOSE(SPLIT(I1, " "))
```

Nous avons maintenant besoin, dans la colonne K, de la probabilité des
mots de ce courriel de test dans l'hypothèse où "non", ça ne serait
pas un pourriel :

```
=IFERROR(XLOOKUP(J1, D:D, G:G), 1E-5)
```

et de manière similaire pour la colonne L, avec la probabilité des
mots du courriel dans l'hypothèse où "oui" il s'agit d'un pourriel :

```
=IFERROR(XLOOKUP(J1, D:D, H:H), 1E-5)
```

Les colonnes K et L doivent avoir la même taille que la colonne J,
donc assurez-vous d'utiliser le remplissage automatique. Calculons
dans la colonne M la probabilité que "non" le courriel n'est pas un
pourriel :

```
=PRODUCT(K:K) * C1
```

Et dans la colonne N la probabilité que "oui" le courriel est un
pourriel :

```
=PRODUCT(L:L) * C2
```

Notre classification finale sera dans la colonne O :

```
=IF(M1 > N1; "non"; "oui")
```

![](/images/module2/tn2/sheets_toutes_les_cols.png)

## Questions

1. Que se passe-t-il si vous changez le mot "spéciale" par le mot
   "livrée" dans le courriel de test de la cellule I1?

2. Expliquez en vos mots ce qui se passe avec les probabilités
   conditionnelles du mot "livrée", aux cellules K4 et L4. Pourquoi
   a-t-on besoin de faire en sorte que ça fonctionne ainsi?

3. Est-ce que ce modèle est paramétrique ou non? Expliquez pourquoi.

4. S'il s'agit d'un modèle paramétrique, quels sont les paramètres du
   modèle exactement?

5. Quelle est la signification des nombres dans les cellules G11 et
   H11, comment peut-on les interpréter?

6. Quelles sont les différentes probabilités conditionnelles de ce
   modèles?

7. Quelles sont les probabilités non-conditionnelles (à priori)?

8. Est-ce qu'il serait possible d'utiliser seulement ces probabilités
   non-conditionnelles pour faire un modèle? Quelles conséquences ça
   entrainerait?

9. De quelle manière peut-ton dire que ce modèle généralise?

10. Est-ce que l'ordre des mots joue un rôle dans les décisions de ce
    modèle? Expliquez pourquoi c'est ainsi

11. Si l'ordre des mots ne joue pas de rôle, comment pourrait-on
    modifier le modèle de manière à ce qu'il en joue un?

12. Est-ce que certains mots aident particulièrement le modèle? Si oui
    pourquoi?

13. Est-ce que certains mots sont moins utiles? Si oui pourquoi?