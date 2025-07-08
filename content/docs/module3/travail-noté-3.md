---
title: "Travail noté 3"
weight: 100
---

# Apprivoisez un réseau de neurones

## Instructions et questions

1. En vous assurant tout d'abord que le "type de problème" (menu déroulant à
   droite) est la "classification", considérez les 4 problèmes proposés.

2. Expliquez tout d'abord ce que veut dire "résoudre" ces problèmes.

3. Quel problème vous apparait ensuite le plus facile à résoudre, pour un
   algorithme d'apprentissage machine (pas seulement un réseau de neurones)?
   Expliquez pourquoi.

4. Considérez maintenant le problème avec lequel deux petits groupes de points
   sont disposés en diagonale, l'un par rapport à l'autre.

   <p style="text-align: center;">
     <img src="/images/module3/tn3/prob1.png" alt="My image" style="width: 50%;">
   </p>

   Assurez-vous de n'avoir aucune couche cachée, et seulement les caractérisques
   $X_1$ et $X_2$ activées. Quelles sont, avant tout entrainement, les erreurs
   d'entrainement et de test? Appuyez plusieurs fois sur le bouton de
   rafraichissement, et constatez les variations au niveau de ces mêmes erreurs
   initiales (avant tout entrainement):

   <p style="text-align: center;">
     <img src="/images/module3/tn3/refresh_button.png" alt="My image" style="width: 50%;">
   </p>

   Que signifient ces erreurs et ces variations, et de quelle manière peut-on
   les constater visuellement?

5. Ajustez la valeur de "bruit" à 25, et appuyez sur le bouton "régénérez" à
   quelques reprises. Est-ce que ceci rend le problème plus facile ou plus
   difficile pour un problème d'apprentissage? Expliquez pourquoi.

6. Considérez maintenant ce problème :

   <p style="text-align: center;">
     <img src="/images/module3/tn3/prob2.png" alt="My image" style="width: 50%;">
   </p>

   À priori, est-ce qu'il vous apparait possible qu'un modèle ayant servi à
   résoudre le premier problème puisse servir à résoudre celui-ci? Expliquez
   pourquoi. Tentez l'expérience, que se passe-t-il?

7. Ajoutez maintenant une couche cachée avec trois neurones, quel est l'effet
   sur l'entrainement? N'oubliez pas que la fonction d'entrainement est démarrée
   en appuyant sur ce bouton :

   <p style="text-align: center;">
     <img src="/images/module3/tn3/train_button.png" alt="My image" style="width: 50%;">
   </p>

8. Ajoutez maintenant une couche deuxième couche cachée avec deux neurones.
   Effectuez quelques entrainements, en n'oubliant pas d'utiliser la fonction de
   rafraichissement entre les entrainements (pour faire en sorte que les
   paramètres départ puissent varier). Qu'observez-vous, et que pouvez-vous en
   conclure?

9. Une fois qu'un entrainement a atteint un certain niveau d'erreur (assez bas,
   probablement, si l'entrainement a bien fonctionné), est-ce que le fait de
   laisser l'entrainement continuer pendant une longue période (et donc
   d'atteindre un très grand nombre d'époques) fait une différence? Comment
   expliquez-vous cela? Quel mot pourrait-on utiliser pour illustrer ce
   phénomène particulier?

10. Comment expliquez-vous le fait que l'entrainement ne converge pas toujours
    vers la même solution, et par extension, la même valeur pour les erreurs?

11. Considérez maintenant ce troisième problème :

    <p style="text-align: center;">
      <img src="/images/module3/tn3/prob3.png" alt="My image" style="width: 50%;">
    </p>

    En ayant aucune cachée (et toujours les mêmes deux seules caractéristiques
    $X_1$ et $X_2$ activées), est-ce qu'il est possible de résoudre ce problème?

12. Est-ce que la situation change en remplaçant les caractériques $X_1$ et
    $X_2$ par les caractéristiques $X_1^2$ et $X_2^2$? Comment peut-on expliquer
    cela?

13. En remettant seulement les caractéristiques $X_1$ et $X_2$, est-ce qu'il est
    possible de résoudre le problème à l'aide de couches cachées?
