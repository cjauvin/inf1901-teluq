---
title: "Épisode 4 — Représenter le monde"
weight: 40
slug: representer-le-monde
---

# Épisode 4 — Représenter le monde

## Le sens, angle mort de la machine

Faisons le bilan des épisodes précédents. Le Logic Theorist démontrait des
théorèmes, Deep Blue gagnait aux échecs, ELIZA tenait la conversation — mais
tous, au fond, faisaient *la même chose* : **manipuler des symboles d'après leur
forme**, selon des règles. ELIZA repérait le mot « mère » sans avoir la moindre
idée de ce qu'est une mère. C'est ce qu'on appelle le niveau de la **syntaxe** :
agencer des symboles correctement, sans toucher à leur sens.

Or comprendre le monde demande bien davantage. Les spécialistes du langage
distinguent trois niveaux, qu'un seul petit exemple suffit à éclairer. Imaginez
qu'à table, quelqu'un vous dise : **« Pouvez-vous me passer le sel ? »**

- La **syntaxe**, c'est la *forme* : la phrase est une question grammaticalement
  bien construite. Une machine peut vérifier ça sans rien comprendre.
- La **sémantique**, c'est le *sens littéral* : la phrase interroge votre
  *capacité* à passer le sel. Pour y accéder, il faut savoir ce que veulent dire
  « sel », « passer », « pouvoir ».
- La **pragmatique**, c'est l'*intention réelle en contexte* : tout le monde
  comprend qu'il ne s'agit pas d'une question sur vos aptitudes, mais d'une
  **demande** polie — « passez-moi le sel ». Saisir cela exige du contexte et une
  montagne de sous-entendus que nous partageons tous.

Voilà le drame de l'IA symbolique résumé en une phrase : elle excellait au niveau
de la **syntaxe**, peinait à atteindre la **sémantique**, et se fracassait sur la
**pragmatique**. Car pour passer de la forme au sens, une machine a besoin de
quelque chose dont Deep Blue et ELIZA étaient totalement dépourvus : des
**connaissances** sur le monde. C'est le grand chantier de cet épisode — et, on
le verra, sa grande déconvenue. Reste la question vertigineuse par laquelle tout
commence : comment loger dans une machine *ce que tout le monde sait* ?
