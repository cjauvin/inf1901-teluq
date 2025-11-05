---
title: "AA versus X"
weight: 20
---

## En quoi l'apprentissage automatique diffère de la programmation au sens traditionnel?

Bien que l'apprentissage automatique requiert de la programmation, il s'agit
d'un paradigme entièrement différent de celui de la programmation.

Un programme traditionnel spécifie une série d'instructions que l'ordinateur
exécute pour résoudre un problème. Normalement, ce programme fait son travail en
relation avec des données fournies par l'utilisateur. Le programme dans ce cas
est une série d'instructions symboliques dans un langage de programmation.

Un modèle d'AA (déjà entraîné) va prendre en entrée des données fournies par
l'utilisateur, et va offrir une réponse appropriée après avoir effectué une
série d'opérations mathématiques (plus spécifiquement, des calculs souvent
reliés à l'algèbre linéaire ou aux probabilités). Si on veut absolument parler
de "programme" dans ce cas, on peut parler des opérations mathématiques (pas
nécessairement symboliques) qui sont effectuées sur les données, pour les
transformer en réponse. Il est important de comprendre que même si un modèle
d'AA est avant tout un objet mathématique (un modèle avec ses paramètres), son
implémentation concrète se fait quand même toujours avec un langage de
programmation.

Ce sujet est traité plus en profondeur dans le [prochain chapitre]({{< relref
"docs/module2/les-données/" >}}), qui parle des données et de leur
représentation.

![](/images/module2/abeille.png)

Voici une bande dessinée fameuse de l'artiste web [XKCD](https://xkcd.com/) qui illustre la même idée :

<p style="text-align: center;">
    <a href="https://xkcd.com/1425/"><img src="/images/xkcd1425.png" alt="My image" style="width: 50%;"></a>
</p>

{{% hint info %}}

Traduction : <br />
&#8208; "Quand un usager prend une photo, l'application devrait vérifier s'il est dans un parc national..."<br />
&#8208; "Pas de problème, un simple appel [SIG](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27information_g%C3%A9ographique), donne-moi quelques heures."<br />
&#8208; "... et vérifier si la photo est celle d'un oiseau."<br />
&#8208; "Je vais avoir besoin d'une équipe de recherche et de 5 ans."<br />
En informatique, il peut être difficile d'expliquer la différence entre ce qui est facile et ce qui est presque impossible.

{{% /hint %}}

{{% hint warning %}}

Cette bande dessinée a plus de 10 ans maintenant, et ce qu'elle dit n'est plus
vrai (car identifier un oiseau dans une photo est devenu facile), mais il reste
que l'idée de base, que certaines tâches sont plus difficiles que d'autres,
reste valide.

{{% /hint %}}

## En quoi l'apprentissage automatique diffère de l'IA?

L'intelligence artificielle est le domaine plus vaste, qui englobe
l'apprentissage automatique et l'intelligence artificielle classique (plus
ancienne) et dite symbolique (en anglais on utilise parfois le terme GOFAI,
"good old fashioned artificial intelligence"). Il est important de comprendre
que ces deux disciplines sont distinctes et ont des méthodes profondément
différentes, et l'histoire de leur développement est entièrement différente.
Dans un certain sens, l'AA est une forme plus spécialisée et un peu plus récente
d'IA, plus mathématique, moins symbolique, et clairement celle qui domine la
période actuelle. Les mathématiques qui sont le plus souvent associées à
l'apprentissage machine sont l'algèbre linéaire et les probabilités, qui
elles-mêmes entretiennent des liens étroits.

## En quoi l'apprentissage automatique diffère des statistiques?

L'apprentissage automatique, conceptuellement, est pratiquement un synonyme de
statistiques. Les deux domaines entretiennent des relations très étroites, et la
distinction est parfois assez difficile. Dans les deux cas on parle de modèles,
d'entraînement (ou recherche des paramètres), d'inférence, etc. Toutefois l'AA
est plus axée sur les problèmes dont la modélisation se fait en très haute
dimension, comme l'analyse d'images ou le traitement du langage. De plus,
l'accent en AA est davantage mis sur les aspects computationnels, par opposition
aux mathématiques (bien que l'AA demeure très mathématique en substance). En
résumé, les statistiques ont une saveur mathématique et scientifique, tandis que
l'AA a une saveur plus mathématique et informatique (ou computationnelle).
