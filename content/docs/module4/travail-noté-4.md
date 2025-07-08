---
title: "Travail noté 4"
weight: 100
---

# Un mini ChatGPT dans Google Sheets

Un modèle de langage est un outil mathématique qui permet d'établir la
distribution statistique des mots : en présence (ou dans le contexte) de
certains mots, quel mot a tendance à suivre, et dans quelle proportion des cas
(c'est-à-dire avec quelle probabilité). Un modèle de langage n'est pas un objet
abstrait qui décrit une réalité théorique : il s'agit d'un modèle statistique
entraîné sur des données particulières. De la même manière qu'un modèle de
prédiction de la température pour la ville de Montréal est différent d'un modèle
pour la ville de Québec, un modèle de langage créé par exemple à partir des
données de 100 livres écrits au 19ième siècle, et un autre à partir de 100
livres écrits au 20ième siècles, seront deux modèles distincts, et auront des
propriétés statistiques très différentes.

Tout comme le modèle de classification du travail noté #2, il est encore ici
question de probabilité conditionnelle. Étant donné que nous allons construire
un modèle bigramme, il s'agit donc de la probabilité d'un mot, étant donné le
mot qui le précède (la barre verticale dans l'équation signifie "étant donné",
ou "en présence de", ou "dans le contexte de") :

$$\text{Prob(mot à prédire | mot qui précède)}$$

La tâche de notre modèle de classification pour les courriels était de
discriminer (répondre oui ou non à la question : est-ce un pourriel?) tandis que
la tâche de notre modèle bigramme sera ici de générer du nouveau texte, une fois
le modèle entraîné, en faisant de l'échantillonnage. La génération de nouveau
texte à l'aide de l'échantillonnage est précisément ce qui permet à ChatGPT de
répondre à une question, ou de composer un poème.

## Entraînement du modèle

Voyons maintenant comment il est possible de calculer ces probabilités en
entraînant un modèle bigramme génératif sur un texte très simple.

Nous allons encore une fois utiliser le tableur
[[https://sheets.google.com][Google Sheets]] au lieu de Excel, car Google Sheets
est plus accessible, et le langage de ses formules est plus facile à gérer
(celui d'Excel dépend de la langue et des paramètres régionaux de votre système
d'exploitation). Pour éviter la confusion dans le contexte de ce travail, nous
devons tout d'abord nous assurer que la langue des fonctions et des paramètres
régionaux est l'anglais :

![](/images/module4/tn4/sheets_params_langue.png)

Assurez-vous ensuite que la "barre de formules" soit bien visible :

![](/images/module4/tn4/sheets_visu_barre_formule.png)

Copiez tout d'abord les mots de ce texte dans la colonne `A` d'une nouvelle
"feuille" Google Sheets, un mot par rangée :

```
le
chat
dort
le
chien
mange
le
chat
mange
une
souris
le
chien
dort
la
souris
court
la
souris
mange
le
fromage
le
chat
court
le
chien
voit
le
chat
le
chat
voit
la
souris
le
chien
court
```

Notez tout d'abord que la colonne `A` (son contenu) est très souvent nommée le
"corpus d'entraînement". Il s'agit du texte brut à partir duquel nous allons
calculer les paramètres du modèle. Pour les vrais modèles de langage, ce texte
peut être extrêmement volumineux ! (Il peut comprendre des millions de livres,
par exemple).

Dans la première cellule de la colonne `B` (donc `B1`), entrez maintenant cette
formule :

```
=A2
```

La colonne `B` devrait être étendue jusqu'à la cellule `B37`, en double-cliquant
sur le petit "+" qui apparaît quand votre curseur est placé au-dessus du coin
inférieur droit de la cellule `B1` (il est possible que Google Sheets offre de
le faire pour vous, automatiquement).

Dans la cellule `C1`, entrez maintenant cette formule :

```
=A1 & " " & B1
```

Encore une fois, la colonne `C` doit s'étendre jusqu'à la cellule `C37`. À ce stade,
votre feuille devrait ressembler à ceci :

![](/images/module4/tn4/sheets_3_first_cols.png)

À ce stade, il devrait être clair pour vous que la colonne `C` contient tous les
bigrammes extraits du texte de la colonne `A` (la colonne `B` n'est qu'un
mécanisme intermédiaire pour les obtenir facilement).

Nous allons maintenant compter, dans la colonne `D`, le nombre de fois où un
bigramme particulier (une séquence particulière de deux mots) apparaît dans le
corpus d'entraînement de la colonne `A` (la colonne `D` doit être étendue pour
avoir le même nombre d'éléments que la colonne `C`) :

```
=COUNTIF(C:C, C1)
```

On constate par exemple que le bigramme "le chien" apparaît 4 fois, tandis que
le bigramme "fromage le", apparaît seulement une fois.

Dans la colonne `E`, nous allons maintenant calculer les paramètres de notre
modèle, soit la probabilité d'un mot, étant donné le mot qui le précède :

$$\text{Prob(mot de la col B | mot de la col A)} =
\frac{
  \#(\text{mots A et B})
}{
  \#(\text{mot A})
}
$$

Pour ce faire, entrez dans la cellule `E1` (la formule est un peu complexifiée par
le fait qu'on veut considérer tous les mots de la colonne A sauf le dernier, car
sa présence fausserait légèrement les probabilités) :

```
=D1 / COUNTIF(A$1:INDEX(A:A, COUNTA(A:A)-1), A1)
```

La probabilité d'un mot étant donné le mot qui le précède est donc simplement le
nombre de fois où ce bigramme particulier apparaît dans le texte, divisée par le
nombre de fois où le premier mot du bigramme apparaît (le dénominateur est
nécessairement plus grand ou égal que le numérateur, prenez un moment pour vous
en convaincre). Étant donné que cette valeur est une probabilité, elle doit
nécessairement être contenue entre 0 et 1.

Dans la colonne `F` nous allons filtrer la colonne `C` (tous les bigrammes, qui
comprennent donc des bigrammes répétés) pour ne retenir que les bigrammes
uniques :

```
=SORT(UNIQUE(C:C))
```

Nous devons ensuite séparer les mots des bigrammes uniques, les
premiers mots dans la colonne `G` :

```
=INDEX(SPLIT(F1, " "), 1)
```

suivis des deuxièmes mots (des bigrammes uniques de la colonne `F`) dans la
colonne `H` :

```
=INDEX(SPLIT(F1, " "), 2)
```

Et dans la colonne `I` nous allons ajouter les probabilités
correspondantes (provenant de la colonne `E`):

```
=INDEX(E:E, MATCH(F1, C:C, 0))
```

On peut maintenant constater que le mot "souris" suit nécessairement (avec
certitude, soit une probabilité de 1) le mot "la", tandis que le mot "le" peut
être suivi des mots "chat", "chien" et "fromage" avec des probabilités de 0.5,
0.4 et 0.1, respectivement.

À ce stade, votre feuille devrait ressembler à ceci :

![](/images/module4/tn4/sheets_model_complete.png)

## Utilisation du modèle (inférence)

Maintenant que notre modèle de langage est "entraîné" (c'est-à-dire que les
probabilités pour les différents bigrammes, les paramètres donc, sont
calculées), on peut l'utiliser pour générer un nouveau texte, différent du
corpus d'entraînement.

Pour démarrer le mécanisme de génération, on peut entrer un premier mot dans la
cellule `J1`, par exemple le mot "le" (ce mot doit faire partie du vocabulaire du
modèle).

Ensuite, la génération peut être effectuée de manière itérative avec cette
formule plus complexe, à partir de la cellule `K1` si vous désirez que les mots
soient générés à la verticale, ou `J2` si vous désirez qu'ils le soient à
l'horizontale (attention étant donné que cette formule contient plusieurs lignes
elle doit être entrée dans l'espace de la formule, en haut des colonnes) :

```
=LET(
  next_word_mask, ARRAYFORMULA($G:$G = J1),
  next_words, FILTER($H:$H, next_word_mask),
  probs, FILTER($I:$I, next_word_mask),
  probs_cumul, SCAN(0, probs, LAMBDA(a, b, a + b)),
  sampled_word_idx, MATCH(RAND(), {0; probs_cumul}, 1),
  INDEX(next_words, sampled_word_idx)
)
```

![](/images/module4/tn4/sheets_generate.png)

Cette formule détermine tout d'abord quels sont les prochains mots possibles
(suivant le mot "le", dans ce cas particulier), ainsi que leur probabilité
associée. Elle détermine ensuite le mot suivant en choisissant un nombre
aléatoire qui est utilisé en tant qu'index dans la liste des probabilités
cumulatives (cette procédure est appelée échantillonnage).

Si votre deuxième mot généré se trouve dans la cellule `K2`, vous pouvez
continuer la génération en glissant la cellule vers la droite. Si votre deuxième
mot se trouve plutôt dans la cellule `J2`, vous pouvez poursuivre la génération
en glissant la cellule `J2` vers le bas.

## Questions

1. Quels sont les paramètres du modèle (quelles colonnes exactement)?

2. Expliquez en vos mots comment ces paramètres sont calculés.

3. En quoi la colonne `B` de ce modèle diffère de la colonne `B` du modèle de
   classification des courriels du [travail noté #2]({{< relref
   "docs/module2/travail-noté-2.md" >}})?

4. Expliquez en quoi le modèle de classification du travail #2 était un modèle
   discriminatif, alors que ce modèle de langage est un modèle génératif?

5. Quelle est la conséquence du fait que le bigramme "le chat" apparaisse 5 fois
   dans le corpus d'entraînement (colonne `A`)?

6. Quelle est la conséquence du fait que le bigramme "la souris" apparaisse 3
   fois, et en quoi cela diffère du bigramme de la question (4)?

7. Est-ce que la présence de certains bigrammes fait en sorte qu'il est possible
   de générer des séquences moins grammaticales? Lesquels en particulier?

8. Est-ce que la présence de certains bigrammes fait en sorte qu'il est possible
   de générer des séquences sémantiquement plus étranges? Lesquels en
   particulier?

9. De quel type d'apprentissage s'agit-il ici : supervisé, non-supervisé ou
   semi-supervisé? Expliquez en quoi ça l'est.

10. Si on utilisait un modèle trigramme au lieu d'un bigramme, qu'est-ce qui
    changerait? Quelles seraient les contraintes entraînées par l'utilisation
    d'un modèle trigramme au lieu d'un modèle bigramme?

11. Supposons que le modèle ait généré le mot "voit", expliquez la conséquence
    que le choix du prochain mot (celui suivant immédiatement "voit") va avoir
    sur la suite de la phrase générée.

12. Est-ce qu'il y a une limite à la longueur de la phrase pouvant être générée
    par le modèle?

13. Est-ce qu'il est possible que le modèle génère un bigramme qui ne fait pas
    partie des exemples qui ont servis à son entraînement?

14. Expliquez quelles sont les limites au niveau de la capacité de
    généralisation de ce modèle. À quoi sont dues ces limites?

15. Expliquez comment on pourrait faire en sorte que le modèle puisse modéliser
    et générer des phrases complètes (avec une majuscule et un point final).
