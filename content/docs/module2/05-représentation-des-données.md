---
title: "Que sont les données?"
weight: 5
---

# Que sont les données, et comment les représenter?

Il y a une tension fondamentale en informatique entre les différentes manières
de représenter les données, et ce qu'elles peuvent signifier. Quand on ajoute
l'apprentissage automatique, la situation devient encore plus complexe. Tentons
de clarifier le tout.

## Niveau des bits, physiques et mathématiques

Au niveau le plus fondamental, l'ordinateur, physiquement et logiquement, ne
peut traiter qu'un seul type de donnée : le bit, qui est à la fois un concept
mathématique (un symbole dont la valeur ne peut être que `0` ou `1` généralement, ou
`vrai` ou `faux` plus spécifiquement en logique) et physique, au niveau de
l'implémentation, soit en terme électrique (mémoire RAM, CPU, disque SSD), de
magnétisme (disque dur) ou de caractéristiques optiques (CD). Les bits
*représentent* les nombres via la convention de l'encodage binaire.

![](/images/module2/binary_enc.png)

## Niveau de l'ordinateur et de son langage

Au niveau suivant, on trouve l'ordinateur lui-même, dont le mécanisme central
est le microprocesseur (CPU). Un CPU traite les bits sous leur forme physique,
et il interprète des "paquets" (ou *mots*) de bits de taille déterminée (souvent
32, 64 ou 128 bits) de deux manière fondamentalement différentes :

1. En tant que *nombre* (ou plus généralement *valeur*)
2. En tant qu'*instruction*

Le flot de bits auquel est exposé le CPU (soit via sa mémoire physique, ou via
un autre médium physique comme un disque) constitue un *programme*, et le CPU
*exécute* ce programme, de manière séquentielle et dynamique. Un programme dans
un "langage machine" (le langage du CPU) fictif pourrait être par exemple :

```
MOV 1000
ADD 0001
STR 2000
```

Les symboles `MOV`, `ADD` et `STR` sont des instructions, qui correspondent en fait
elles-mêmes à des nombres (donc des séries de bits). En réalité, le CPU verrait peut-être
la séquence suivante :

```
1000 1000
1001 0001
1002 2000
```

si `MOV`, `ADD` et `STR` correspondaient par convention aux valeurs 1000, 1001
et 1002. La signification de ce programme pourrait être la suivante :

```
- Prendre la valeur à l'adresse mémoire 1000 et la mettre dans un registre
- Ajouter 1 à cette valeur dans le registre
- Prendre le contenu du registre et l'enregistrer à l'adresse mémoire 2000
```

Comment le CPU peut-il distinguer entre 1000 en tant qu'instruction `MOV`, ou
1000 en tant que valeur? Une manière simple serait de simplement respecter la
convention selon laquelle les "paquets de bits" (de taille fixe) aux positions
paires (dans la séquence du programme) sont des instructions, tandis que ceux
aux positions impaires sont des valeurs (dans la réalité c'est un peu plus
complexe, mais l'idée est semblable, il s'agit de conventions préétablies). Et
qu'est-ce que le CPU doit "faire" pour exécuter une instruction particulière? Il
s'agit en fait d'un mini-programme (pour cette instruction particulière) qui est
implémenté directement dans les circuits du CPU. C'est l'endroit où la logique
et la matière se touchent !

Vous pouvez exécuter vous-même pas à pas une version interactive de ce
mini-programme :

<style>
    /* --- instructions --- */
    ul.instructions {list-style: none; padding: 0; margin-bottom: 1rem;}
    ul.instructions li            {padding: .3rem .6rem; border: 1px solid #ccc; border-radius: 4px; margin-bottom: .3rem;}
    ul.instructions li.current{
    background-color: rgba(33, 150, 243, 0.20); /* bleu + opacité 20 % */
    border-color:     #2196f3;
    color:            inherit;                  /* conserve la couleur de texte courante */
    }

    /* --- mémoire & registre --- */
    .row            {display: flex; align-items: center; margin-bottom: .5rem;}
    .row label      {width: 130px; font-weight: bold;}
    .row span       {display: inline-block; width: 90px; text-align: right;
                        padding: .3rem .5rem; border: 1px solid #888; border-radius: 4px;}

    /* --- boutons --- */
    .buttons        {margin-top: 1rem;}
    button          {padding: .5rem 1.2rem; margin-right: .5rem;}
    button:disabled {opacity: .5; cursor: not-allowed;}
</style>

<ul class="instructions">
  <li data-op="MOV" data-arg="1000">MOV 1000</li>
  <li data-op="ADD" data-arg="1">ADD 0001</li>
  <li data-op="STR" data-arg="2000">STR 2000</li>
</ul>

<!-- ordre demandé : Registre, puis mémoire 1000 et 2000 -->
<div class="row">
  <label>Registre&nbsp;:</label><span id="reg"></span>
</div>
<div class="row">
  <label>Adresse 1000&nbsp;:</label><span id="mem1000"></span>
</div>
<div class="row">
  <label>Adresse 2000&nbsp;:</label><span id="mem2000"></span>
</div>

<div class="buttons">
  <button id="execBtn">Exécuter</button>
  <button id="resetBtn">Réinitialiser</button>
</div>

<script>
(function () {
  /* --- éléments du DOM --- */
  const instrElems = [...document.querySelectorAll('.instructions li')];
  const mem1000   = document.getElementById('mem1000');
  const mem2000   = document.getElementById('mem2000');
  const reg       = document.getElementById('reg');
  const execBtn   = document.getElementById('execBtn');
  const resetBtn  = document.getElementById('resetBtn');

  let pc = 0; // program counter

  /* --- fonctions utilitaires --- */
  function highlight() {
    instrElems.forEach((li, i) => li.classList.toggle('current', i === pc));
  }
  function updateBtnState() {
    execBtn.disabled = pc >= instrElems.length;
  }

  /* --- réinitialisation --- */
  function reset() {
    mem1000.textContent = Math.floor(Math.random() * 256); // valeur aléatoire 0-255
    reg.textContent     = '_';
    mem2000.textContent = '_';
    pc = 0;
    highlight();
    updateBtnState();
  }

  /* --- exécution pas à pas --- */
  function step() {
    if (pc >= instrElems.length) return;

    const li  = instrElems[pc];
    const op  = li.dataset.op;
    const arg = parseInt(li.dataset.arg, 10);

    switch (op) {
      case 'MOV': // MOV 1000
        reg.textContent = mem1000.textContent || '0';
        break;
      case 'ADD': // ADD 0001
        reg.textContent = (parseInt(reg.textContent || '0', 10) + arg);
        break;
      case 'STR': // STR 2000
        mem2000.textContent = reg.textContent;
        break;
    }
    pc++;
    highlight();
    updateBtnState();
  }

  /* --- événements --- */
  execBtn.addEventListener('click', step);
  resetBtn.addEventListener('click', reset);

  /* --- état initial --- */
  reset();
})();
</script>

## Niveau de la programmation symbolique

Le prochain niveau est implémenté en terme du langage du niveau précédent : tout
comme il est possible d'écrire un jeu, un système d'exploitation ou tout autre
type de programme dans le langage natif du CPU (le langage machine), il est
également possible d'écrire.. un autre langage ! Cet autre langage sera en
général plus *abstrait* (plus éloigné donc de la réalité physique de
l'ordinateur), ce qui permettra au programmeur d'exprimer des idées
computationnelles plus complexes, d'une manière plus naturelle et expressive
(C++, Python ou JavaScript sont des exemples de langage de cette catégorie).
Pour mieux comprendre la notion d'un langage en tant que *programme*, on peut
imaginer qu'il s'agit d'une sorte "d'ordinateur virtuel", implémenté en terme
d'un langage moins abstrait (le langage machine). Ce langage de "plus haut
niveau" (plus abstrait) doit encore une fois traiter avec des instructions et
des valeurs (toujours, ultimement, représentées en termes de bits), mais cette
fois on voit apparaître des représentations plus complexes, pouvant encoder des
structures plus riches et diverses :

- des nombres entiers
- des nombres réels (beaucoup plus complexe à représenter!)
- des chaînes de caractères (strings)
- des listes de nombres
- des listes de mots
- des listes de listes de mots
- des images
- des sons
- etc!

## Niveau de l'apprentissage automatique et des mathématiques

L'aspect "algorithmique" d'un algorithme d'apprentissage automatique réfère au
fait qu'on effectue en général une procédure, une séquence d'opérations (ou de
transformations) sur des données qui sont essentiellement de nature numérique.
Cette procédure est généralement écrite dans un langage du niveau précédent, par
exemple Python. L'aspect mathématique des algorithmes d'apprentissage
automatique exige des structures des données et des représentations plus
sophistiquées et performantes. L'outil conceptuel le plus souvent utilisé pour
les données d'AA est l'espace vectoriel, souvent de très haute dimensionnalité
(bien au-delà des trois dimensions dans lesquelles nous vivons quotidiennement).

Prenons l'exemple de l'image d'une maison. Il est raisonnable à priori de
considérer qu'une image est représentée dans un espace à deux dimensions, la
grille 2D de ses pixels :

![](/images/module2/2d_house.png)

Pourtant, s'il s'agissait d'une maison dans un jeu vidéo, elle pourrait être
représentée par un modèle vectoriel en trois dimensions (ce qui permettrait de
rendre l'environnement dynamique, avec une caméra, à l'aide d'algèbre linéaire)
:


![](/images/module2/3d_house.png)

Mais dans le contexte de l'apprentissage automatique, nous allons en fait
considérer un espace beaucoup plus difficile à imaginer et représenter, un
espace multi-dimensionnel avec lequel il y a autant de dimensions que de pixels
:

![](/images/module2/nd_house.png)

Si notre image a 1000 X 2000 pixels par exemple, il s'agira donc d'un espace à
6,000,000 dimensions (1000 x 2000 x 3 couleurs de base pour chaque pixel :
rouge, bleu et vert). Il s'agit d'un espace absolument énorme, qu'il n'est pas
possible de se représenter visuellement. Un "point" dans cet espace représente
une image entière et particulière, correspondant aux valeurs de sa position
relative à chacune des 6,000,000 dimensions. Si on ne modifie qu'un seul pixel
de cette image, il s'agira en fait d'un autre point (donc une autre image),
proche, mais tout de même différent du premier.

Les images ne sont utilisées qu'avec certains types d'algorithmes
d'apprentissage, mais l'idée générale de l'espace vectoriel à plusieurs
dimensions, pour représenter des objets ou des concepts, est très importante et
répandue. On pourrait utiliser un tel espace pour représenter les
caractéristiques quantitatives (features) d'une maison :

![](/images/module2/nf_house.png)

### Les GPUs

Il serait possible d'implémenter un espace vectoriel entièrement avec les
primitives offertes au niveau précédent (langage de programmation symbolique)
mais il est maintenant établi que l'utilisation de GPUs est plus performante.
Les GPUs sont des puces spéciales qui sont spécialisées dans le calcul numérique
parallèle. Cette technologie a été introduite tout d'abord dans le contexte des
jeux vidéos, pour le calcul 3D, mais a trouvé rapidement un usage dans les
applications numériques d'apprentissage automatique. Les environnements de
programmation spécialisés en AA (PyTorch et TensorFlow en sont de bons exemples)
permettent à un programme écrit dans un langage symbolique (par exemple Python)
de communiquer directement avec ce matériel spécialisé. Le même calcul,
implémenté sur un CPU au lieu d'un GPU, serait beaucoup moins performant.

### Retour vers les symboles

On comprend mieux maintenant la distinction mentionnée souvent entre l'IA au
sens classique, qui manipule des symboles, et l'apprentissage automatique, qui
manipule plutôt des valeurs numériques, et dont on dit parfois qu'il est
sub-symbolique. Dans un certain sens les deux manipulent des données qui sont
ultimement des valeurs numériques (et même au final des entités physiques, les
bits), mais il y a tout de même un sens clair à distinguer les deux types de
mathématiques sur lesquels sont fondés l'IA classique et l'AA.

Il se trouve que la distinction peut apparaître moins claire, selon le type
d'algorithme d'apprentissage dont on parle. Avec les grands modèles de langage
(GML), les données de base sont les mots (ou souvent des morceaux de mots, les
"tokens") qui sont au départ des données de nature résolument symbolique (un mot
est un symbole par excellence, après tout). Un GML fonctionne pourtant en fait à
partir d'une représentation vectorielle des mots. Chaque mot est associé à un
vecteur arbitraire dans un espace de grande dimensionnalité (par exemple 512
dimensions), et ce sont ces vecteurs qui sont manipulés, transformés et
*appris*, à l'interne, par un GML. Il n'est pas nécessairement clair à priori ce
que représente chaque dimension de cet espace particulier. Mais il se trouve
qu'après la phase d'apprentissage d'un GML, les mots se trouvant près les uns
des autres, dans cet espace, auront tendance à être sémantiquement rapprochés.
Les mots "chien" et "chat" seront donc probablement relativement proches (en
terme de distance euclidienne), dans cet espace à 512 dimensions. Le
fonctionnement du GML fait donc en sorte de reproduire, dans son fonctionnement
et sa représentation interne (c-à-d ses paramètres) son propre système
symbolique, dans un format qui peut être particulièrement opaque pour un
interprète humain.

![](/images/module2/schema_repr_donnees.png)

