# Plan — Refonte v2 du cours INF1901 (TELUQ)

> **Note de démarrage** — Ce document est le livrable d'une séance de brainstorm de conception. Il est conçu pour être **autosuffisant** : la rédaction de la v2 démarrera en **contexte neuf, avec ce plan comme seule entrée**. Les *pourquoi* et les alternatives écartées sont consignés exprès pour survivre sans le transcript.
> **Emplacement cible** : à déplacer à la **racine du dépôt sous `PLAN-v2.md`** dès la sortie du plan mode (versionné par git, voyage avec le cours).
> **Première cible de rédaction** : le **Module 1** (le plus défini et le plus vide actuellement).

---

## 1. Contexte

Refonte de la v2 du cours INF1901 (Hugo + thème hugo-book-teluq, contenu markdown sous `content/docs/moduleN/`). Quatre axes définis par Christian :

1. **Module 1** : refonte complète → IA classique (GOFAI), mélange d'histoire et d'idées algorithmiques/mathématiques, pour faire comprendre ce qui a précédé le ML.
2. **Modules 2-3-4** : compléter et uniformiser (très inégaux en v1 : M2 ≈ 17 000 mots, M3 ≈ 8 300, M4 ≈ 3 700).
3. **Module 5** : le rendre plus mordant, plus connecté à l'actualité récente.
4. **Travaux notés 1 et 5** : leur donner une forme *hands-on* comme les TN2-3-4.

## 2. Fondations

- **Structure macro inchangée** : M1 GOFAI → M2 ML → M3 réseaux/deep → M4 GenAI/LLM → M5 société/philo.
- **Public (inchangé vs v1)** : étudiants à distance de premier cycle, **non-informaticiens**. Cours de *littératie en IA* : comprendre ce qu'il y a sous le capot sans devenir praticien, pour finir capable de juger (M5). **Pas de programmation, pas de formalisme math lourd** ; vulgarisation appuyée (vidéos, outils interactifs, exemples à la main).
- **Retrait des deux livres** : la v2 élimine les deux ouvrages obligatoires de la v1 — *La plus belle histoire de l'intelligence* (Dehaene et al.) et *Quand la machine apprend* (Le Cun). Cours désormais **autonome**, sans achat obligatoire.
  - Supprimer `content/docs/30-livres.md` et les lectures/quiz du M1 actuel (`content/docs/module1/10-activités.md`) qui en dépendent.
  - **Détachement complet** côté Dehaene : sa substance M1 (nature de l'intelligence, limites du symbolique, sens commun) est déjà couverte par notre contenu original.
  - **Récupérer la matière Le Cun** (CNN, reconnaissance de chiffres/chèques, révolution du deep learning), actuellement mal placée au M1 → la **replacer au M3**.

## 3. Idées d'unification (le tissu conjonctif de la v2)

Ce qui donnera sa cohérence à la v2 — à exploiter activement comme liens entre modules.

- **Motif récurrent « semé → fleurit »** : un mécanisme est *introduit* dans un module, puis *fleurit* dans le suivant.
  - **Perceptron** : semé M1 → fleurit M3.
  - **RL** : semé M2 → fleurit M3 (deep RL) → réemployé M4 (RLHF).
  - **Transformer** : introduit M3 (architecture) → fleurit M4 (LLM).
- **Fil rouge des deux traditions** : GOFAI (symbolique) et ML (connexionnisme) n'ont **pas** évolué séquentiellement ; ils ont **co-évolué dans des univers parallèles** depuis les années 1950, s'éclipsant à tour de rôle. Posé au M1, dénoué au M3.
- **Fil transversal cerveau ↔ IA** (fond au M3) :
  - **M1 (origine)** : inspiration biologique fondatrice (McCulloch & Pitts 1943, cybernétique de Wiener, perceptron). Recoupe « l'esprit comme logique » (symbolique) vs « l'esprit comme cerveau » (connexionnisme). Touche légère.
  - **M3 (cœur — le piège technique)** : là où la métaphore est la plus séduisante et trompeuse. Encadré « la carte n'est pas le territoire » : le neurone artificiel est une caricature (pas de spikes, pas de neuromodulation, le cerveau ne fait pas de rétropropagation). Démystifiage à haute valeur, au moment de la tentation.
  - **M5 (la question profonde)** : reproduire le cerveau donnerait-il un esprit ? conscience, paradoxe de Moravec. Touche légère / terreau.
- **Principe d'interactivité** : *quand le sujet est un mécanisme, laisser l'étudiant le faire tourner* (vaut M1-M4). Constat clé : ce qui distingue les modules « riches » des « pauvres » n'est pas le volume de texte mais la **densité d'expériences manipulables**. Le M5 (philo) a un levier différent : engagement par le **débat et l'actualité**.

## 4. Gabarit de module (à appliquer uniformément)

Le squelette commun existe déjà en v1 ; il est **à appliquer partout**, pas à inventer.

1. **`_index.md`** — mise en contexte, objectifs (3-5), durée, aperçu de l'évaluation. (`bookCollapseSection: true`)
2. **Page « 10 »** — *premier contact concret* avant la théorie (ex. scénario d'assemblage de téléviseurs au M2).
3. **Pages « 20-90 »** — un concept par page, du simple au complexe. Éléments récurrents : applets `{{< applet src=… >}}`, vidéos `{{< youtube id=… >}}` (3Blue1Brown), encadrés `{{% hint %}}`, sections repliables `{{% details %}}` pour l'optionnel, LaTeX (`$$…$$`, `\(…\)`).
4. **Page « 99 »** — le travail noté.

Front matter : `title`, `weight` (ordonne le menu), `slug` optionnel. Fichiers nommés `NN-titre.md`. Pas d'accents dans les URLs.

---

## 5. Module 1 — GOFAI (refonte complète)

- **Format** : sections « épisode historique → idée technique » (**6 épisodes**). L'étudiant comprend l'*idée* et le *drame historique*, **pas** la technique fine (réservée aux M2-3-4).
- **Fil rouge** : les deux traditions parallèles (voir §3). Le M1 plante la tension fondatrice ; le M3 est le dénouement.

### Ossature (6 épisodes, à raffiner à la rédaction)
1. **Turing, la question fondatrice (1950)** — mécaniser la pensée ? Test de Turing, machine universelle. Idée : la pensée comme calcul.
2. **1956-58, deux paris rivaux** — Dartmouth / IA symbolique (règles, symboles) **vs** perceptron de Rosenblatt (apprendre d'exemples). Les deux grandes hypothèses sur l'intelligence, nées quasi simultanément.
3. **L'âge d'or symbolique : chercher et raisonner** — espaces d'états, minimax, explosion combinatoire (jusqu'à Deep Blue 1997). Idée : résoudre = explorer un arbre. **Y loger : ELIZA** (Weizenbaum 1966 — appariement de motifs, « effet ELIZA », rappel du test de Turing ép. 1, sème M4/M5) ; **Lisp** (McCarthy 1958 — la langue maternelle du GOFAI, *list processing* = manipulation de symboles ; résonne à l'ép. 6 avec le krach des machines Lisp).
4. **Représenter le monde** — réseaux sémantiques (Quillian), frames (Minsky 1974), scripts (Schank & Abelson), dépendance conceptuelle → mène au **problème du sens commun** (CYC de Lenat). Explique *pourquoi* le GOFAI a plafonné ; résonne avec ce que les LLM font « gratuitement » (contraste M4). **Y loger : SHRDLU** (Winograd 1970 — le sommet de l'ambition symbolique dans un « micro-monde de blocs », mais qui ne marche *que* là → bute pile sur le sens commun).
5. **Capturer l'expertise : les systèmes experts (70-80)** — l'intelligence comme règles d'experts (MYCIN), grandeur et fragilité (goulot d'étranglement de la connaissance). Idée : connaissance = règles explicites.
6. **Les hivers et la bascule** — Minsky & Papert tuent le perceptron (1969, 1er hiver) ; limites du symbolique (2e hiver). Le monde réel résiste aux règles → porte d'entrée du M2 (« et si on laissait les données parler ? »).

- Le perceptron apparaît 2× : **promesse** (ép. 2) et **victime** (ép. 6) — boucle le drame du M1 et arme le retour du M3. Traiter seulement l'*idée* (machine qui apprend de ses erreurs) et le *drame* (XOR, Minsky), pas la technique.
- **Arbres de décision (ID3, CART)** : placés au M1 comme **figure de transition** (règles lisibles mais *apprises* → illustre le pont GOFAI/ML).
- **Interactivité M1** : fortement candidat (minimax, A*, système expert qui déroule ses règles, perceptron qui ajuste ses poids). Nourrit directement le TN1.

### Catalogue de phares GOFAI (à trier par épisode — au moment de rédiger)
- **Recherche / résolution de problèmes** : espaces d'états, minimax, élagage alpha-bêta, A*, analyse moyens-fins (GPS, Newell & Simon), Deep Blue (1997)
- **Logique** : logique formelle (Boole, Frege), résolution et unification (Robinson), Prolog / programmation logique
- **Planification** : STRIPS, SHRDLU (Winograd, monde des blocs)
- **Contraintes** : satisfaction de contraintes (CSP)
- **Règles / expertise** : systèmes de production, algorithme RETE, systèmes experts (MYCIN), goulot d'étranglement de la connaissance
- **Représentation des connaissances** : réseaux sémantiques (Quillian), frames (Minsky), scripts (Schank), dépendance conceptuelle, CYC (Lenat), problème du sens commun
- **Langage / dialogue (illusion de compréhension)** : ELIZA (Weizenbaum 1966, « effet ELIZA » → ép. 3), PARRY (pendant paranoïaque), STUDENT (problèmes d'algèbre en mots), SHRDLU (Winograd, monde des blocs → ép. 4)
- **Outils / substrat** : Lisp (McCarthy 1958, langage du GOFAI → ép. 3) ; machines Lisp et leur krach (~1987, déclencheur du 2e hiver → ép. 6) ; Samuel's Checkers (1959, machine qui apprend aux dames — petite graine RL)
- **Zone-pont GOFAI ↔ ML** : arbres de décision ID3 (Quinlan) / CART (Breiman) [→ M1], réseaux bayésiens (Pearl 1988)
- **Fondations** : Turing (test, machine universelle), Dartmouth (1956), perceptron (Rosenblatt 1958), Minsky & Papert (1969), hivers de l'IA

## 6. Module 2 — Apprentissage automatique (refonte de fond)

### Diagnostic v1
Le plus riche (≈17 000 mots, 7 applets), bon fil narratif, mais : (1) **page monstre** `60-apprentissage-supervisé.md` (5509 mots = ⅓ du module) ; (2) **déséquilibre supervisé (5500) / non-supervisé (800)** ; (3) pages préparatoires dispersées ; (4) ordre discutable ; (5) **aucun foyer pour généralisation/surapprentissage/évaluation** alors que le `_index` en fait le cœur.

### Décision : refonte complète, colonne = **le flux de travail ML**
Principe organisateur : **données → modèle → entraînement par minimisation d'une erreur → vérification de la généralisation**. Enseigne un *modèle mental transférable* qui démystifie le ML en entier (mieux qu'une taxonomie « par paradigmes », un « zoo » d'algos, ou un narratif pur). Les algorithmes deviennent des *illustrations* dans ce squelette. Supervisé/non-supervisé = une **bifurcation** (la cible est présente ou absente), pas la colonne. Le contenu v1 = carrière d'idées à réassembler (refonte radicale assumée).

### Structure : **fil continu « construire en butant sur des obstacles »**
Pas de pages « préparatoires » abstraites : chaque concept **naît quand un obstacle le rend nécessaire**. Le module devient une seule démonstration qui se construit.
1. **Le problème** (scénario d'ouverture conservé) — on veut prédire qqch.
2. **Le modèle le plus bête** — prédire la moyenne/majorité ; c'est *déjà* un modèle. Obstacle : ignore l'entrée.
3. **Regarder les données** — attributs, vecteurs (la notion « données » émerge par besoin).
4. **Prédire par ressemblance** — similarité + kNN (apprendre presque sans modèle). Obstacle : lourd, pas d'« apprentissage ».
5. **Un vrai modèle qui s'entraîne** — régression linéaire, fonction d'erreur, descente de gradient (cœur du flux). Obstacle : et pour une catégorie ?
6. **Classer** — régression logistique, Bayes naïf → TN2. Obstacle : marche-t-il sur du neuf ?
7. **Généraliser** — train/test, surapprentissage (cœur conceptuel, **nouveau**).
8. **De quel signal apprend-on ?** — bifurcation à 3 branches : supervisé (cible étiquetée) / non-supervisé (clustering, k-means) / **renforcement** (récompense, essai-erreur).
9. **TN2**

- La page monstre est absorbée par cette structure (régression linéaire → étape 5 ; logistique + Bayes → étape 6).
- **Graine RL** (étape 8) : l'idée seulement (agent, action, récompense, essai-erreur, exploration), exemple simple **non-profond** (souris dans un labyrinthe / gridworld), tease AlphaGo. Pas d'algos (Q-learning, etc.). Fleurit au M3.

## 7. Module 3 — Réseaux de neurones et apprentissage profond

### Diagnostic v1
Contenu : `10-réseaux-de-neurones.md` (2872, **cœur solide** : neurone = généralisation de la régression logistique → pont M2, rétropropagation, deep learning, décomposition hiérarchique, GPU ; applet + hints), `20-3blue1brown.md` (vidéo), `30-architectures-avancées.md` (3610, **fourre-tout monolithe** : CNN, RNN, autoencodeurs, GNN, NTM), `40-aa-adverse.md` (628, mince), `99-travail-noté-3.md` (TF Playground). Problèmes : (1) **aucun Transformer/attention** ; (2) architectures déséquilibrées (exotique traité, essentiel manquant) ; (3) ne porte pas le deep RL ni la floraison du perceptron ; (4) adverse sous-développé.

### Décisions
- **Éclater** `30-architectures-avancées` en pages séparées (CNN | RNN | autoencodeurs | …). Élagage de l'exotique (GNN/NTM) à décider page par page.
- **Transformers : pont au M3, fond au M4.** M3 = *comment la machine est bâtie* : le Transformer en point d'orgue de la séquence **CNN → RNN → Transformer** (la limite du RNN motive l'attention : « regarder toute la séquence en parallèle »), traité **comme architecture**, pas comme chatbot. (Le fond LLM est au M4 ; le M4 ne ré-enseigne pas la mécanique de l'attention.)
- **Intégrer le deep RL** (AlphaGo, DQN/Atari) = floraison de la graine RL du M2.
- **Floraison du perceptron** : la revanche connexionniste (pas seulement « généralisation de la régression logistique », mais le retour de la tradition semée au M1).
- **Récupérer la matière Le Cun** (CNN, deep learning) rapatriée depuis le M1.
- **Étoffer l'apprentissage adverse** (exemples adverses, duper un classifieur d'images).
- **Cœur du fil cerveau ↔ IA** (voir §3) : l'encadré « la carte n'est pas le territoire ».

## 8. Module 4 — IA générative et LLM

### Diagnostic v1
**Promet plus qu'il ne livre.** `10-IA-générative.md` (288, survol), `20-grands-modèles-de-langage.md` (1020, narration n-grammes → word2vec → RNN/LSTM → Transformers → RLHF, mais 100 % texte, dense), `30-3blue1brown.md` (4 vidéos), `99-travail-noté-4.md` (mini-LLM bigramme en Sheets — déjà hands-on). Trous : (1) versant *génératif-média* (GANs, diffusion, image/vidéo) en un paragraphe ; (2) zéro interactivité ; (3) déséquilibre interne ; (4) possible obsolescence (écrit à l'ère ChatGPT 2022).

### Orientation retenue
- **Intro conceptuelle forte** : l'IA générative comme **paradigme qui transcende les LLM**. Idée unificatrice : au lieu de *discriminer* (classer, comme aux M2/M3), on **modélise la distribution des données pour en échantillonner de nouvelles** (« imiter la source, puis produire du neuf »). Couvre texte, image, vidéo, audio, code. L'image/vidéo (diffusion, GANs) = *illustration de l'ampleur du paradigme*, pas un bloc co-vedette.
- **Cœur = les LLM**, développés au maximum (dominent l'actualité, enchaînent vers le M5).
- **Profondeur LLM = trois aspects équilibrés** : (a) **mécanisme interne** (tokens, embeddings, attention, prédiction du mot suivant ; 3b1b en appui), (b) **du modèle à l'assistant** (pré-entraînement, fine-tuning, RLHF, alignement → pont M5), (c) **usages et phénomènes** (prompting, hallucinations, capacités émergentes, fenêtre de contexte, multimodal, agents — la face « vécue » en 2026).

### Ossature cible
1. `_index` — contexte.
2. **Page 10 — « L'IA générative, un paradigme »** : modéliser/échantillonner une distribution ; tour d'horizon des modalités (texte, image/diffusion, vidéo).
3. **Pages 20-50 — les LLM en profondeur** : éclater la page monolithique (mécanisme / entraînement-alignement / usages), aérer avec visuels + **au moins une expérience manipulable**.
4. **Page 99 — TN** (mini-LLM en Sheets, déjà hands-on).

## 9. Module 5 — IA et société (plus mordant)

### Diagnostic v1
Riche philosophiquement mais pas assez « mordant ». `_index.md` (194), `10-attitudes.md` (1119 — quatre attitudes : libérale / défaitiste-doomer / accélérationniste / transhumaniste), `20-conversation.md` (4521 — bâti autour de la **conversation vidéo de 2h** Lemire & Jauvin, minutée, + 9 sections thématiques), `99-travail-noté-5.md` (528, essai). Problèmes : (1) trop ancré sur un artefact fixe et passif (vidéo 2h) qui **vieillit** ; (2) attitudes intemporelles, pas branchées sur des controverses vives ; (3) engagement passif.

### Pivot retenu : **controverses = colonne, attitudes = lentilles**
Les quatre attitudes ne sont plus le *contenu* mais une **boîte à outils d'analyse** (quatre façons de *lire* un débat). Le contenu devient une série de **dossiers chauds** — points de friction où l'IA percute le réel *maintenant*.
- **Confronter des controverses vives** → les dossiers eux-mêmes.
- **Relief / provocation** → chaque dossier s'ouvre sur une question dérangeante + **prise de position assumée des profs** (fini la neutralité encyclopédique).
- **Actualité non-périssable** → le texte cadre la *tension durable*, l'**étudiant apporte l'instance récente** (veille). Rejoint le TN5.

### Dossiers chauds retenus (cœur du M5)
- **IA, vérité et démocratie** : deepfakes, désinformation, élections, confiance épistémique.
- **IA et travail** : automatisation, emplois, économie, gagnants/perdants.
- **IA, création et propriété** : art génératif, droit d'auteur, devenir de la créativité humaine.
- **Risque, pouvoir et alignement** : risque existentiel, concentration Big Tech, surveillance, sécurité.
- **IA et éducation** : méta/auto-référentiel (des étudiants TELUQ qui utilisent l'IA dans ce cours même : intégrité académique, apprendre avec/malgré l'IA, devenir de l'évaluation). Le seul dossier où l'étudiant est personnellement impliqué → particulièrement mordant.

### Conversation de 2h
Ne pas la jeter (riche, personnelle). La **repositionner** : découpée en segments thématiques branchés sur les dossiers (le minutage existant le permet), comme *une voix parmi d'autres*, pas la pièce maîtresse passive.

## 10. Travaux notés 1 et 5

**Esprit recherché** : la signature des TN2-3-4 est que l'étudiant *manipule le mécanisme lui-même* (calcule, triture, construit), au lieu de « produire un document ». **Forme commune réutilisée** : un « quelque chose » interactif + des **questions interprétatives**.

### TN1 — Système expert en Google Sheets
Substrat : **Google Sheets** (façon TN2/TN4). Mécanisme : **un système expert qu'on trace, casse et étend**.
- On fournit une base de règles `si… alors…` (p. ex. identifier un animal / diagnostiquer une panne).
- L'étudiant **joue le moteur d'inférence** sur des cas : quelles règles se déclenchent, dans quel ordre, jusqu'à la conclusion.
- Puis : **trouver un cas que le système rate** et **ajouter une règle pour le corriger** → fait vivre le *goulot d'étranglement de la connaissance* (porte le récit des épisodes 5-6 du M1).
- Le plus *purement* GOFAI **et** porteur de sa fragilité. (Alternatives écartées : minimax-Sheets, A*-applet.)

### TN5 — Expérience sur une IA réelle
Le M5 n'a **pas de mécanisme** → le « quelque chose » est **une vraie IA de pointe** (ChatGPT, Claude…) manipulée comme objet d'étude. Hands-on, maximalement actuel, non-périssable, méta.
- **Forme** : l'étudiant mène une **petite expérience sur une IA réelle, branchée sur un dossier chaud de son choix**, documente (transcription = artefact), puis **analyse via les lentilles des 4 attitudes** + questions interprétatives.
- Pistes : vérité/démocratie (désinformation, garde-fous) ; création/propriété (« à la manière de », originalité/droit d'auteur) ; éducation (lui faire « faire » un travail, critiquer la fiabilité). (Alternatives écartées : analyser une news ; débat dialectique.)

---

## 11. Démarrage de la rédaction (prochaines séances)

- **Approche** : contexte neuf à chaque séance, ce plan comme entrée. Rédiger **module par module**, en commençant par le **M1**.
- **Premiers gestes concrets pour le M1** : (1) supprimer `30-livres.md` et l'ancien `module1/10-activités.md` ; (2) trier le catalogue de phares (§5) dans les 6 épisodes ; (3) rédiger épisode par épisode selon le gabarit (§4) ; (4) concevoir le gabarit Sheets du TN1.
- **Points laissés ouverts volontairement** : tri fin du catalogue M1 ; élagage de l'exotique au M3 (GNN/NTM) ; choix précis des applets/expériences manipulables à créer (M1, M4).
