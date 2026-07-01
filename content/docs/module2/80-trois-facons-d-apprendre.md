---
title: "Trois façons d'apprendre"
weight: 80
slug: trois-facons-d-apprendre
---

# Trois façons d'apprendre

Nous avons refermé le chapitre précédent sur une prise de conscience : tout ce
que nous avons construit dans ce module — régression, classification, la droite,
Bayes — appartenait à une seule et même famille, l'**apprentissage supervisé**,
celle où chaque exemple arrive accompagné de sa bonne réponse. Mais nous avons
aussi entrevu que ce n'était pas la seule façon d'apprendre.

Ce qui distingue les grandes familles de l'apprentissage automatique, c'est la
nature du **signal** dont le modèle se nourrit — ce qui, dans les données, lui
tient lieu de guide. Et il n'en existe, au fond, que trois grands types :

- une **réponse fournie** pour chaque exemple : c'est l'apprentissage
  **supervisé**, notre terrain depuis le début ;
- **aucune réponse**, juste des données brutes dans lesquelles il faut débusquer
  une structure : l'apprentissage **non supervisé** ;
- ni réponse ni structure donnée, mais une **récompense** qui arrive après coup,
  au fil de l'action : l'apprentissage par **renforcement**.

{{< image src="/images/module2/trois-paradigmes.svg" alt="Trois panneaux. « Supervisé » : des points étiquetés en bleu et rouge — la réponse est donnée. « Non supervisé » : les mêmes points, tous gris et sans étiquette, que l'algorithme regroupe en cercles pointillés — on découvre des groupes. « Renforcement » : une boucle entre un agent et son environnement, reliés par une flèche « action » et une flèche « récompense »." title="Les trois grandes familles, par la nature de leur signal : réponse donnée (supervisé), structure à découvrir (non supervisé), récompense au fil de l'action (renforcement)." loading="lazy" >}}

Trois signaux, trois façons d'apprendre. Nous avons passé tout le module dans la
première ; ce dernier chapitre part à la rencontre des deux autres — moins pour
les maîtriser que pour situer ce que nous avons appris dans un paysage plus vaste,
et apercevoir les routes qui mènent aux modules suivants.
