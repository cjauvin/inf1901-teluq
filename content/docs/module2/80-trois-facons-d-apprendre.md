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

## Apprendre avec un professeur : le supervisé

Commençons par ce que nous connaissons déjà par cœur. En apprentissage supervisé,
le signal est une **réponse toute prête**, attachée à chaque exemple : le prix de
cette maison, l'étiquette *pourriel* de ce courriel, la couleur de ce point. Le
modèle n'a qu'un but — apprendre à relier l'entrée à cette réponse —, et une fois
entraîné, il l'applique à des cas neufs. C'est l'image même du professeur qui
corrige : il connaît la bonne réponse, et c'est en s'y comparant que l'élève
progresse.

Nous en avons rencontré les deux visages : la **régression**, quand la réponse
est un nombre (un prix), et la **classification**, quand c'est une catégorie
(pourriel ou non). Malgré leurs différences, tous deux carburent au même
signal — une cible fournie d'avance — et à la même mécanique : régler des
paramètres pour minimiser l'écart à cette cible.

Cette dépendance à des réponses toutes prêtes est la grande force du supervisé…
et son talon d'Achille. Car ces étiquettes, il faut bien que *quelqu'un* les
fournisse — souvent à la main, un exemple à la fois.

{{% hint info %}}
**Étiqueter les données : une industrie à part entière**

Derrière chaque modèle supervisé se cache une montagne de travail humain.
Quelqu'un a dû regarder des centaines de milliers d'images pour dire « ceci est
un chat », transcrire des heures d'audio, ou trancher « ce message est haineux,
celui-là non ». Cette tâche — l'**étiquetage** (ou *annotation*) des données —
est devenue un véritable secteur économique mondial : des plateformes comme
Amazon Mechanical Turk, ou des entreprises spécialisées telles Scale AI,
emploient des centaines de milliers de personnes, souvent dans des pays à bas
salaires, pour produire ces étiquettes une par une.

Ce travail est le plus souvent invisible, peu rémunéré, et parfois éprouvant —
pensez à la modération de contenus violents. Même les assistants les plus récents
en dépendent : une part de l'entraînement de ChatGPT repose sur des humains qui
notent et corrigent ses réponses (nous y reviendrons au Module 4). L'« intelligence »
de ces systèmes s'appuie ainsi sur un socle très humain — et soulève des questions
que nous retrouverons au Module 5.
{{% /hint %}}

Que faire, alors, quand personne n'a fourni ces réponses ?
