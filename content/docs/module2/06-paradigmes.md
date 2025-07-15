---
title: "Paradigmes de l'AA"
weight: 6
---

<style>
canvas {
    display: block;
    margin: auto;
   /*  background: #f0f0f0; */
}
.graph-area {
    background: white;
    border: 1px solid #aaa;
}
h2, #info, #info2 {
    text-align: center;
}
#info, #info2 {
    margin-top: 20px;
}
</style>

# Les différents paradigmes de l'apprentissage automatique

Il existe plusieurs manières de catégoriser les algorithmes
d'apprentissage automatique, selon leur structure même, mais aussi selon
la nature et la structure des problèmes qu'ils tentent de résoudre.
Nous allons considérer deux schémas de classement fondamentaux :

- L'apprentissage supervisé versus non-supervisé
- L'apprentissage paramétrique versus non-paramétrique

## Apprentissage supervisé (classification, regression)

L'apprentissage supervisé fonctionne à partir de données pour
lesquelles la "bonne réponse" (i.e. celle qu'on aimerait que
l'algorithme fournisse systématiquement, une fois entrainé) est
fournie, en tant que donnée d'entrainement.

### Régression

Une régression est une famille d'algorithmes d'apprentissage supervisé
(ou plus classiquement, de modélisation statistique) dont le but est
de découvrir une fonction numérique continue, au sens classique
mathématique (dans sa forme la plus simple, une fonction associe une
valeur numérique du domaine X vers l'image Y).

- Régression linéaire (ex. à partir du nombre de pièces et l'année de construction, on aimerait prédire le prix d'une maison)
- Réseau de neurones

### Classification

Une autre famille d'algorithmes d'apprentissage supervisé tente plutôt
de découvrir une fonction de classification, qui associe une série de
caractéristiques à une catégorie particulière (dont le nombre est fini
et connu d'avance).

- Régression logistique (ex1: à partir du nombre d'heures étudiées et du nombre de cours, prédire si un étudiant a gradué ou non, ex2: à partir des caractéristques des passagers du Titanic, prédire s'ils ont survévu ou non)
- k-NN
- Arbres de décision
- Naive Bayes
- Réseau de neurones

#### Régression logistique

Vous pouvez développer une meilleure intuition du mécanisme de la régression
logistique à l'aide de cette petite application interactive :

<div style="text-align: center; margin-bottom: 10px;">
  <label for="pointSlider">Nombre de points : </label>
  <input type="range" id="pointSlider" min="2" max="50" value="12" style="width: 200px;">
  <span id="pointCount">10</span>
</div>
<canvas id="canvas"></canvas>
<div id="info">y = mx + b</div>

#### Régression linéaire

Voici un autre exemple interactif pour explorer la régression linéaire. Les points bleus suivent une droite cachée avec du bruit, et vous pouvez ajuster votre ligne pour minimiser l'erreur quadratique moyenne :

<div style="text-align: center; margin-bottom: 10px;">
  <label for="pointSlider2">Nombre de points : </label>
  <input type="range" id="pointSlider2" min="2" max="50" value="25" style="width: 200px;">
  <span id="pointCount2">25</span>
</div>
<canvas id="canvas2"></canvas>
<div id="info2">Erreur quadratique moyenne</div>

## Apprentissage non-supervisé

Nous avons vu qu'une caractéristique essentielle de l'apprentissage
supervisé est que la "bonne réponse" (qu'il s'agisse du prix réel
d'une maison, ou la variable binaire oui/non correspondant au fait
qu'un étudiant ait échoué ou non) est fournie avec les données
d'entrainement. Un algorithme d'apprentissage supervisé (nous avons vu
qu'il y en avait plusieurs) utilise cette "bonne réponse" comme une
cible cruciale qu'il doit s'efforcer d'atteindre, de modéliser donc.
En contraste, un algorithme non-supervisé n'a pas cette "bonne
réponse", il n'a que des données non-étiquettées. Les algorithmes de
cette famille ont donc une tâche entièrement différente que celle de
l'apprentissage supervisé. Il doivent découvrir la structure inhérente
aux données, de manière autonome, tout en étant guidé possible par des
hypothèses. Par exemple, si les données sont des mesures décrivant un
ensemble de fleurs de différentes espèces, il est possible que je
sache à priori combien d'espèces l'ensemble d'entrainement contient.
Dans ce cas, supposons que je sache qu'il y a trois espèces, alors
l'algorithme n'aura qu'à découvrir ces trois groupes, et associer
chaque exemple à un groupe en particulier. Il pourrait être également
possible que le nombre d'espèces soit à priori inconnu, ce qui rendrait
la tâche de l'algorithme de classification encore plus difficile.

### Partitionnement (clustering)

Avec un algorithme de partitionnement, on peut découvrir des
"agrégats", ou des groupes naturels dans les données.

- k-Means
- DBScan
- Hierarchical clustering
*** Réduction de la dimensionnalité
En tentant de réduire la dimensionnalité des données, on peut
découvrir sa structure inhérente, ce qui est souvent utile en
visualisation (par exemple, une donnée exprimée en très haute
dimension peut être plus facile à comprendre ou visualiser en 2d ou
3d).

- PCA

## Apprentissage paramétrique versus non-paramétrique

Il existe une autre manière, complètement différente, de classifier
les algorithmes d'apprentissage : si l'algorithme est implémenté à
l'aide d'une fonction mathématique essentiellement définie par des
paramètres, qui sont indépendants des données qui seront traitées par
l'algorithme, on parle d'apprentissage paramétrique. Avec l'apprentissage non-paramétrique, en contraste, la fonction de décision est définie à partir des données d'entraînement. Les données elles-mêmes constituent l'algorithme.

Exemples d'algorithmes paramétriques :

- Régression linéaire (apprentissage supervisé)
- Régression logistique (supervisé)
- Réseau de neurones

Exemples d'algorithmes non-paramétriques :

- Arbres de décision
- k-NN

Pour certains algorithmes, la frontière entre ces deux classes est un peu plus floue.

## Apprentissage inductif versus transductif

TODO

## Apprentissage par renforcement (RL)

L'apprentissage par renforcement (APR) est un autre paradigme
d'apprentissage automatique, très différent des précédents dont nous avons
parlés. On peut généraliser les apprentissages supervisé et
non-supervisé en considérant qu'ils sont une forme de "reconnaissance
de motifs" (en anglais "pattern recognition"). Les mécanismes de ce
genre sont souvent associés aux fonctions cognitives de la perception,
chez les humains. Par exemple, mes yeux perçoivent une information
visuelle qu'on m'a appris à classifier en tant que "balle", alors
quand je vois une balle, la classification appropriée est effectuée
par mon esprit (exemple d'apprentissage supervisé). D'une manière
apparentée mais un peu différente, il se peut que mes yeux détectent,
lors d'une promenade en forêt, une forme ou des couleurs
particulières, que je ne parviens pas à identifier, mais qui vont tout
de même attirer mon attention (exemple d'apprentissage non-supervisé).
En contraste de cette reconnaissance de motifs, l'apprentissage par
renforcement est plutôt une modélisation du comportement, plutôt que
de la perception (quelle action devrait être posée dans ce contexte
particulier). L'APR est souvent utilisé dans les jeux et la robotique.

<script>
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
const info = document.getElementById("info");
const pointSlider = document.getElementById("pointSlider");
const pointCount = document.getElementById("pointCount");

// Set canvas dimensions based on parent element
let width, height, graphWidth, graphOffsetX;
window.addEventListener('load', () => {
  const parentWidth = canvas.parentElement.getBoundingClientRect().width;
  width = parentWidth;
  height = Math.round(parentWidth * (500 / 780)); // Maintain proportional ratio

  canvas.width = width;
  canvas.height = height;

  // Calculate graph width as percentage of canvas width, leaving space for error bar
  graphWidth = Math.min(width - 80, width * 0.85); // Reserve 80px for error bar or use 85% of width
  
  // Set graph offset for positioning
  graphOffsetX = 35; // Left offset for error bar positioning

  // Update anchor position to be within graph area
  anchor = { x: graphWidth / 2, y: height / 2 };

  // Initialize after sizing
  generateRandomPoints(12);
  draw();
});

let points = [];

function generateRandomPoints(numPoints) {
  points = [];
  const margin = 20; // Small margin from graph edges

  for (let i = 0; i < numPoints; i++) {
    const label = i < Math.floor(numPoints / 2) ? 0 : 1;
    const x = Math.random() * (graphWidth - 2 * margin) + margin; // Keep within dynamic graph width
    const y = Math.random() * (height - 2 * margin) + margin; // Keep within graph height
    points.push({ x, y, label });
  }
}

// Initialization moved to load event handler

let anchor = { x: 300, y: 200 }; // Will be updated in load handler
let angle = Math.PI / 4;

const anchorRadius = 10;
const innerRadius = 7;
const outerRadius = 11;
let dragging = false;
let dragMode = null;
let draggedPointIndex = -1;
let mouseDownPos = null;
let hasMoved = false;

function drawGrid(spacing = 25, offsetX = 0) {
  ctx.strokeStyle = "#eee";
  ctx.lineWidth = 1;
  for (let x = 0; x <= graphWidth; x += spacing) {
    ctx.beginPath();
    ctx.moveTo(offsetX + x, 0);
    ctx.lineTo(offsetX + x, height);
    ctx.stroke();
  }
  for (let y = 0; y <= height; y += spacing) {
    ctx.beginPath();
    ctx.moveTo(offsetX, y);
    ctx.lineTo(offsetX + graphWidth, y);
    ctx.stroke();
  }
}

function draw() {
  ctx.clearRect(0, 0, width, height);

  const graphX = (width - graphWidth) / 2 - graphOffsetX; // Center with slight left offset for error bar

  // Draw white background for graph area
  ctx.fillStyle = 'white';
  ctx.fillRect(graphX, 0, graphWidth, height);

  // Draw border around graph area
  ctx.strokeStyle = '#aaa';
  ctx.lineWidth = 1;
  ctx.strokeRect(graphX, 0, graphWidth, height);

  drawGrid(25, graphX);

  const dx = Math.cos(angle);
  const dy = Math.sin(angle);
  const lineLength = 1000;
  const x1 = anchor.x - dx * lineLength;
  const y1 = anchor.y - dy * lineLength;
  const x2 = anchor.x + dx * lineLength;
  const y2 = anchor.y + dy * lineLength;

  // Draw decision line (clipped to graph area)
  ctx.save();
  ctx.beginPath();
  ctx.rect(graphX, 0, graphWidth, height);
  ctx.clip();

  ctx.beginPath();
  ctx.moveTo(x1 + graphX, y1);
  ctx.lineTo(x2 + graphX, y2);
  ctx.strokeStyle = 'black';
  ctx.lineWidth = 2;
  ctx.setLineDash([5, 5]);
  ctx.stroke();
  ctx.setLineDash([]);

  ctx.restore();

  // Draw anchor
  ctx.fillStyle = '#000';
  ctx.beginPath();
  ctx.arc(anchor.x + graphX, anchor.y, anchorRadius, 0, Math.PI * 2);
  ctx.fill();
  
  ctx.fillStyle = '#fff';
  ctx.beginPath();
  ctx.arc(anchor.x + graphX, anchor.y, innerRadius, 0, Math.PI * 2);
  ctx.fill();

  // Update slope/intercept
  let m = (x2 - x1) === 0 ? Infinity : (y2 - y1) / (x2 - x1);
  let b = anchor.y - m * anchor.x;
  const mText = isFinite(m) ? m.toFixed(2) : '∞';
  const bText = isFinite(b) ? b.toFixed(2) : '∞';
  info.textContent = `f(x) <= ${mText}x + ${bText}`;

  // Calculate classification error
  let errorCount = 0;
  let classifications = [];

  // First pass: calculate all classifications
  for (let p of points) {
    const dxp = p.x - anchor.x;
    const dyp = p.y - anchor.y;
    const cross = dx * dyp - dy * dxp;
    let predicted = cross > 0 ? 1 : 0;
    const correct = predicted === p.label;

    classifications.push({ predicted, correct });
    if (!correct) errorCount++;
  }

  // If error > 50%, flip all classifications
  const shouldFlip = errorCount > points.length / 2;
  if (shouldFlip) {
    errorCount = points.length - errorCount;
    classifications = classifications.map(c => ({
      predicted: 1 - c.predicted,
      correct: !c.correct
    }));
  }

  // Draw all points
  for (let i = 0; i < points.length; i++) {
    const p = points[i];
    const correct = classifications[i].correct;

    const trueColor = p.label === 0 ? 'red' : 'blue';

    // Draw point in true color
    ctx.beginPath();
    ctx.arc(p.x + graphX, p.y, outerRadius, 0, Math.PI * 2);
    ctx.fillStyle = trueColor;
    ctx.fill();

    // ❌ Draw X if wrong
    if (!correct) {
      ctx.strokeStyle = 'grey';
      ctx.lineWidth = 2;
      const size = outerRadius + 2;
      ctx.beginPath();
      ctx.moveTo(p.x + graphX - size, p.y - size);
      ctx.lineTo(p.x + graphX + size, p.y + size);
      ctx.moveTo(p.x + graphX + size, p.y - size);
      ctx.lineTo(p.x + graphX - size, p.y + size);
      ctx.stroke();
    }
  }

  // Draw error bar
  const errorPercentage = points.length > 0 ? (errorCount / points.length) * 100 : 0;
  const barX = graphX + graphWidth + 20; // 20px space from graph
  const barY = 50;
  const barHeight = height - 100;
  const barWidth = 20;

  // Draw bar background
  ctx.fillStyle = '#f0f0f0';
  ctx.fillRect(barX, barY, barWidth, barHeight);
  ctx.strokeStyle = '#aaa';
  ctx.lineWidth = 1;
  ctx.strokeRect(barX, barY, barWidth, barHeight);

  // Draw error level
  const errorHeight = (errorPercentage / 100) * barHeight;
  ctx.fillStyle = '#ff6b6b';
  ctx.fillRect(barX, barY + barHeight - errorHeight, barWidth, errorHeight);

  // Draw labels
  ctx.fillStyle = getComputedStyle(document.body).getPropertyValue('--body-font-color') || '#333';
  ctx.font = '12px sans-serif';
  ctx.textAlign = 'left';
  ctx.fillText('100%', barX + barWidth + 5, barY + 5);
  ctx.fillText('0%', barX + barWidth + 5, barY + barHeight + 5);
  ctx.fillText(`${errorPercentage.toFixed(1)}%`, barX + barWidth + 5, barY + barHeight - errorHeight + 5);

  // Draw "Error" label
  ctx.font = '14px sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText('Erreur', barX + barWidth / 2, barY - 10);
}

function distance(p1, p2) {
  return Math.hypot(p1.x - p2.x, p1.y - p2.y);
}

canvas.addEventListener('mousedown', (e) => {
  e.preventDefault(); // Prevent context menu on right click
  const rect = canvas.getBoundingClientRect();
  const mouse = { x: e.clientX - rect.left, y: e.clientY - rect.top };
  const graphX = (width - graphWidth) / 2 - graphOffsetX;

  // Store initial mouse position and reset movement flag
  mouseDownPos = { x: mouse.x, y: mouse.y };
  hasMoved = false;

  // Check if mouse is within graph area
  if (mouse.x < graphX || mouse.x > graphX + graphWidth) return;

  // Adjust mouse coordinates to graph space
  const graphMouse = { x: mouse.x - graphX, y: mouse.y };

  // Only handle dragging on left click
  if (e.button === 0) {
    if (distance(graphMouse, anchor) <= anchorRadius) {
      dragging = true;
      dragMode = 'translate';
      return;
    }

    const dx = Math.cos(angle);
    const dy = Math.sin(angle);
    const px = graphMouse.x - anchor.x;
    const py = graphMouse.y - anchor.y;
    const distToLine = Math.abs(dy * px - dx * py);
    if (distToLine < 10) {
      dragging = true;
      dragMode = 'rotate';
      return;
    }
  }

  // Check for point interaction
  for (let i = 0; i < points.length; i++) {
    if (distance(graphMouse, points[i]) < outerRadius) {
      if (e.button === 0) {
        // Left click: prepare for potential drag
        dragging = true;
        dragMode = 'point';
        draggedPointIndex = i;
        return;
      } else if (e.button === 2) {
        // Right click: delete the point immediately
        points.splice(i, 1);
        draw();
        return;
      }
    }
  }

  // Add new points based on click type
  const constrainedX = Math.max(15, Math.min(graphWidth - 15, graphMouse.x));
  const constrainedY = Math.max(15, Math.min(height - 15, graphMouse.y));

  if (e.button === 0) {
    // Left click: add red point (label 0)
    points.push({ x: constrainedX, y: constrainedY, label: 0 });
  } else if (e.button === 2) {
    // Right click: add blue point (label 1)
    points.push({ x: constrainedX, y: constrainedY, label: 1 });
  }

  draw();
});

canvas.addEventListener('mousemove', (e) => {
  const rect = canvas.getBoundingClientRect();
  const mouse = { x: e.clientX - rect.left, y: e.clientY - rect.top };
  const graphX = (width - graphWidth) / 2 - graphOffsetX;
  const graphMouse = { x: mouse.x - graphX, y: mouse.y };

  // Check if mouse has moved significantly
  if (mouseDownPos && distance(mouse, mouseDownPos) > 3) {
    hasMoved = true;
  }

  if (dragging) {
    if (dragMode === 'translate') {
      // Constrain anchor to graph boundaries
      anchor.x = Math.max(15, Math.min(585, graphMouse.x));
      anchor.y = Math.max(15, Math.min(height - 15, graphMouse.y));
    } else if (dragMode === 'rotate') {
      const dx = graphMouse.x - anchor.x;
      const dy = graphMouse.y - anchor.y;
      angle = Math.atan2(dy, dx);
    } else if (dragMode === 'point' && draggedPointIndex >= 0) {
      // Constrain point to graph boundaries
      points[draggedPointIndex].x = Math.max(15, Math.min(585, graphMouse.x));
      points[draggedPointIndex].y = Math.max(15, Math.min(height - 15, graphMouse.y));
    }
    draw();
  } else {
    // Update cursor based on what's under the mouse
    if (mouse.x < graphX || mouse.x > graphX + graphWidth) {
      canvas.style.cursor = 'default';
      return;
    }

    // Check if over anchor point
    if (distance(graphMouse, anchor) <= anchorRadius) {
      canvas.style.cursor = 'grab';
      return;
    }

    // Check if over decision line
    const dx = Math.cos(angle);
    const dy = Math.sin(angle);
    const px = graphMouse.x - anchor.x;
    const py = graphMouse.y - anchor.y;
    const distToLine = Math.abs(dy * px - dx * py);
    if (distToLine < 10) {
      canvas.style.cursor = 'grab';
      return;
    }

    // Check if over a point
    for (let p of points) {
      if (distance(graphMouse, p) < outerRadius) {
        canvas.style.cursor = 'grab';
        return;
      }
    }

    // Default cursor
    canvas.style.cursor = 'default';
  }
});

canvas.addEventListener('mouseup', () => {
  // If we were dragging a point but didn't move, delete it
  if (dragMode === 'point' && draggedPointIndex >= 0 && !hasMoved) {
    points.splice(draggedPointIndex, 1);
    draw();
  }

  dragging = false;
  dragMode = null;
  draggedPointIndex = -1;
  mouseDownPos = null;
  hasMoved = false;
});

canvas.addEventListener('mouseleave', () => {
  dragging = false;
  dragMode = null;
  draggedPointIndex = -1;
  mouseDownPos = null;
  hasMoved = false;
});

// Disable context menu on canvas
canvas.addEventListener('contextmenu', (e) => {
  e.preventDefault();
});

// Helper function to get touch coordinates
function getTouchCoordinates(e) {
  const rect = canvas.getBoundingClientRect();
  const touch = e.touches[0] || e.changedTouches[0];
  return { x: touch.clientX - rect.left, y: touch.clientY - rect.top };
}

// Touch event handlers
let touchStartTime = 0;
let touchHoldTimer = null;
let touchHoldTriggered = false;

canvas.addEventListener('touchstart', (e) => {
  e.preventDefault();
  const touch = getTouchCoordinates(e);
  const graphX = (width - graphWidth) / 2 - graphOffsetX;

  touchStartTime = Date.now();
  touchHoldTriggered = false;

  // Store initial touch position and reset movement flag
  mouseDownPos = { x: touch.x, y: touch.y };
  hasMoved = false;

  // Check if touch is within graph area
  if (touch.x < graphX || touch.x > graphX + graphWidth) return;

  // Adjust touch coordinates to graph space
  const graphTouch = { x: touch.x - graphX, y: touch.y };

  // Set up touch hold timer for right-click equivalent (500ms)
  touchHoldTimer = setTimeout(() => {
    touchHoldTriggered = true;
    // Handle touch hold as right-click
    for (let i = 0; i < points.length; i++) {
      if (distance(graphTouch, points[i]) < outerRadius) {
        // Delete the point
        points.splice(i, 1);
        draw();
        return;
      }
    }
    // Add blue point (label 1) if not over existing point
    const constrainedX = Math.max(15, Math.min(graphWidth - 15, graphTouch.x));
    const constrainedY = Math.max(15, Math.min(height - 15, graphTouch.y));
    points.push({ x: constrainedX, y: constrainedY, label: 1 });
    draw();
  }, 500);

  // Handle anchor dragging
  if (distance(graphTouch, anchor) <= anchorRadius) {
    dragging = true;
    dragMode = 'translate';
    return;
  }

  // Handle line rotation
  const dx = Math.cos(angle);
  const dy = Math.sin(angle);
  const px = graphTouch.x - anchor.x;
  const py = graphTouch.y - anchor.y;
  const distToLine = Math.abs(dy * px - dx * py);
  if (distToLine < 10) {
    dragging = true;
    dragMode = 'rotate';
    return;
  }

  // Check for point interaction
  for (let i = 0; i < points.length; i++) {
    if (distance(graphTouch, points[i]) < outerRadius) {
      // Prepare for potential drag
      dragging = true;
      dragMode = 'point';
      draggedPointIndex = i;
      return;
    }
  }
});

canvas.addEventListener('touchmove', (e) => {
  e.preventDefault();
  const touch = getTouchCoordinates(e);
  const graphX = (width - graphWidth) / 2 - graphOffsetX;
  const graphTouch = { x: touch.x - graphX, y: touch.y };

  // Clear touch hold timer on movement
  if (touchHoldTimer) {
    clearTimeout(touchHoldTimer);
    touchHoldTimer = null;
  }

  // Check if touch has moved significantly
  if (mouseDownPos && distance(touch, mouseDownPos) > 3) {
    hasMoved = true;
  }

  if (dragging && !touchHoldTriggered) {
    if (dragMode === 'translate') {
      // Constrain anchor to graph boundaries
      anchor.x = Math.max(15, Math.min(585, graphTouch.x));
      anchor.y = Math.max(15, Math.min(height - 15, graphTouch.y));
    } else if (dragMode === 'rotate') {
      const dx = graphTouch.x - anchor.x;
      const dy = graphTouch.y - anchor.y;
      angle = Math.atan2(dy, dx);
    } else if (dragMode === 'point' && draggedPointIndex >= 0) {
      // Constrain point to graph boundaries
      points[draggedPointIndex].x = Math.max(15, Math.min(graphWidth - 15, graphTouch.x));
      points[draggedPointIndex].y = Math.max(15, Math.min(height - 15, graphTouch.y));
    }
    draw();
  }
});

canvas.addEventListener('touchend', (e) => {
  e.preventDefault();

  // Clear touch hold timer
  if (touchHoldTimer) {
    clearTimeout(touchHoldTimer);
    touchHoldTimer = null;
  }

  // If touch hold was triggered, don't process as normal touch end
  if (touchHoldTriggered) {
    dragging = false;
    dragMode = null;
    draggedPointIndex = -1;
    mouseDownPos = null;
    hasMoved = false;
    return;
  }

  // Handle tap (short touch without movement)
  if (!hasMoved && Date.now() - touchStartTime < 300) {
    const touch = getTouchCoordinates(e);
    const graphX = (width - graphWidth) / 2 - graphOffsetX;

    if (touch.x >= graphX && touch.x <= graphX + graphWidth) {
      const graphTouch = { x: touch.x - graphX, y: touch.y };

      // Check if tapping existing point to delete it
      for (let i = 0; i < points.length; i++) {
        if (distance(graphTouch, points[i]) < outerRadius) {
          points.splice(i, 1);
          draw();
          dragging = false;
          dragMode = null;
          draggedPointIndex = -1;
          mouseDownPos = null;
          hasMoved = false;
          return;
        }
      }

      // Add red point (label 0) if not over existing point
      const constrainedX = Math.max(15, Math.min(graphWidth - 15, graphTouch.x));
      const constrainedY = Math.max(15, Math.min(height - 15, graphTouch.y));
      points.push({ x: constrainedX, y: constrainedY, label: 0 });
      draw();
    }
  }

  // Reset dragging state
  dragging = false;
  dragMode = null;
  draggedPointIndex = -1;
  mouseDownPos = null;
  hasMoved = false;
});

canvas.addEventListener('touchcancel', (e) => {
  e.preventDefault();

  // Clear touch hold timer
  if (touchHoldTimer) {
    clearTimeout(touchHoldTimer);
    touchHoldTimer = null;
  }

  // Reset all touch state
  dragging = false;
  dragMode = null;
  draggedPointIndex = -1;
  mouseDownPos = null;
  hasMoved = false;
  touchHoldTriggered = false;
});

// Handle slider input
pointSlider.addEventListener('input', (e) => {
  const numPoints = parseInt(e.target.value);
  pointCount.textContent = numPoints;
  generateRandomPoints(numPoints);
  draw();
});

// Initial draw call moved to load event handler

// =====================================
// SECOND WIDGET - LINEAR REGRESSION
// =====================================

// Second widget elements
const canvas2 = document.getElementById("canvas2");
const ctx2 = canvas2.getContext("2d");
const info2 = document.getElementById("info2");
const pointSlider2 = document.getElementById("pointSlider2");
const pointCount2 = document.getElementById("pointCount2");

// Second widget dimensions and variables
let width2, height2, graphWidth2, graphOffsetX2;
let points2 = [];
let anchor2 = { x: 300, y: 200 };
let angle2 = 0;
let hiddenSlope, hiddenIntercept; // Hidden line parameters

// Second widget drag state
let dragging2 = false;
let dragMode2 = null;
let draggedPointIndex2 = -1;
let mouseDownPos2 = null;
let hasMoved2 = false;

// Touch handling for second widget
let touchStartTime2 = 0;
let touchHoldTimer2 = null;
let touchHoldTriggered2 = false;

// Constants for second widget
const anchorRadius2 = 10;
const innerRadius2 = 7;
const outerRadius2 = 11;

// Initialize second widget
window.addEventListener('load', () => {
  const parentWidth2 = canvas2.parentElement.getBoundingClientRect().width;
  width2 = parentWidth2;
  height2 = Math.round(parentWidth2 * (500 / 780));
  
  canvas2.width = width2;
  canvas2.height = height2;
  
  graphWidth2 = Math.min(width2 - 80, width2 * 0.85);
  graphOffsetX2 = 35;
  
  // Generate hidden line parameters
  hiddenSlope = (Math.random() - 0.5) * 1.5; // Random slope between -0.75 and 0.75
  hiddenIntercept = height2 * 0.3 + Math.random() * height2 * 0.4; // Random intercept in middle range
  
  anchor2 = { x: graphWidth2 / 2, y: height2 / 2 };
  
  generateRandomPoints2(25);
  draw2();
});

function generateRandomPoints2(numPoints) {
  points2 = [];
  const margin = 20;
  const noiseAmount = 80; // Noise level
  
  // Calculate safe bounds for the hidden line to ensure all points stay within graph
  const xMin = margin;
  const xMax = graphWidth2 - margin;
  const yMin = margin + noiseAmount / 2;
  const yMax = height2 - margin - noiseAmount / 2;
  
  // Generate hidden line parameters that ensure points stay within bounds
  // Calculate slope limits based on the safe y range
  const maxSlope = (yMax - yMin) / (xMax - xMin);
  const minSlope = -(yMax - yMin) / (xMax - xMin);
  
  hiddenSlope = minSlope + Math.random() * (maxSlope - minSlope);
  
  // Calculate intercept range that works with this slope
  const interceptAtXMin = yMin - hiddenSlope * xMin;
  const interceptAtXMax = yMax - hiddenSlope * xMax;
  const minIntercept = Math.max(interceptAtXMin, interceptAtXMax);
  const maxIntercept = Math.min(yMax - hiddenSlope * xMin, yMin - hiddenSlope * xMax);
  
  hiddenIntercept = minIntercept + Math.random() * (maxIntercept - minIntercept);
  
  for (let i = 0; i < numPoints; i++) {
    // Sample x uniformly across the graph width
    const x = Math.random() * (graphWidth2 - 2 * margin) + margin;
    
    // Calculate ideal y based on hidden line: y = slope * x + intercept
    const idealY = hiddenSlope * x + hiddenIntercept;
    
    // Add noise that keeps points within bounds
    const noise = (Math.random() - 0.5) * noiseAmount;
    const y = idealY + noise;
    
    points2.push({ x, y, label: 1 }); // All points are blue (label 1)
  }
}

function drawGrid2(spacing = 25, offsetX = 0) {
  ctx2.strokeStyle = "#eee";
  ctx2.lineWidth = 1;
  for (let x = 0; x <= graphWidth2; x += spacing) {
    ctx2.beginPath();
    ctx2.moveTo(offsetX + x, 0);
    ctx2.lineTo(offsetX + x, height2);
    ctx2.stroke();
  }
  for (let y = 0; y <= height2; y += spacing) {
    ctx2.beginPath();
    ctx2.moveTo(offsetX, y);
    ctx2.lineTo(offsetX + graphWidth2, y);
    ctx2.stroke();
  }
}

function draw2() {
  ctx2.clearRect(0, 0, width2, height2);
  
  const graphX2 = (width2 - graphWidth2) / 2 - graphOffsetX2;
  
  // Draw white background for graph area
  ctx2.fillStyle = 'white';
  ctx2.fillRect(graphX2, 0, graphWidth2, height2);
  
  // Draw border around graph area
  ctx2.strokeStyle = '#aaa';
  ctx2.lineWidth = 1;
  ctx2.strokeRect(graphX2, 0, graphWidth2, height2);
  
  drawGrid2(25, graphX2);
  
  // Draw user's line (dashed)
  const dx = Math.cos(angle2);
  const dy = Math.sin(angle2);
  const lineLength = Math.max(width2, height2);
  const x1 = anchor2.x - dx * lineLength;
  const y1 = anchor2.y - dy * lineLength;
  const x2 = anchor2.x + dx * lineLength;
  const y2 = anchor2.y + dy * lineLength;
  
  ctx2.save();
  ctx2.rect(graphX2, 0, graphWidth2, height2);
  ctx2.clip();
  
  ctx2.strokeStyle = '#000';
  ctx2.lineWidth = 2;
  ctx2.setLineDash([5, 5]);
  ctx2.beginPath();
  ctx2.moveTo(x1 + graphX2, y1);
  ctx2.lineTo(x2 + graphX2, y2);
  ctx2.stroke();
  ctx2.setLineDash([]);
  
  ctx2.restore();
  
  // Draw points (all blue)
  points2.forEach(point => {
    ctx2.fillStyle = '#4285f4'; // Blue color
    ctx2.beginPath();
    ctx2.arc(point.x + graphX2, point.y, outerRadius2, 0, 2 * Math.PI);
    ctx2.fill();
    
    // Draw border
    ctx2.strokeStyle = '#333';
    ctx2.lineWidth = 1;
    ctx2.stroke();
  });
  
  // Draw anchor point
  ctx2.fillStyle = '#000';
  ctx2.beginPath();
  ctx2.arc(anchor2.x + graphX2, anchor2.y, anchorRadius2, 0, 2 * Math.PI);
  ctx2.fill();
  
  ctx2.fillStyle = '#fff';
  ctx2.beginPath();
  ctx2.arc(anchor2.x + graphX2, anchor2.y, innerRadius2, 0, 2 * Math.PI);
  ctx2.fill();
  
  // Calculate and draw mean squared error
  let totalError = 0;
  points2.forEach(point => {
    const lineY = anchor2.y + (point.x - anchor2.x) * Math.tan(angle2);
    const error = Math.pow(point.y - lineY, 2);
    totalError += error;
  });
  
  const mse = points2.length > 0 ? totalError / points2.length : 0;
  const maxError = 10000; // Reasonable maximum for visualization
  const errorPercentage = Math.min(100, (mse / maxError) * 100);
  
  // Draw error bar
  const barX2 = graphX2 + graphWidth2 + 20;
  const barY2 = 50;
  const barHeight2 = height2 - 100;
  const barWidth2 = 20;
  
  ctx2.fillStyle = '#f0f0f0';
  ctx2.fillRect(barX2, barY2, barWidth2, barHeight2);
  ctx2.strokeStyle = '#666';
  ctx2.lineWidth = 1;
  ctx2.strokeRect(barX2, barY2, barWidth2, barHeight2);
  
  // Draw error level
  const errorHeight2 = (errorPercentage / 100) * barHeight2;
  ctx2.fillStyle = '#ff6b6b';
  ctx2.fillRect(barX2, barY2 + barHeight2 - errorHeight2, barWidth2, errorHeight2);
  
  // Draw labels
  ctx2.fillStyle = getComputedStyle(document.body).getPropertyValue('--body-font-color') || '#333';
  ctx2.font = '12px sans-serif';
  ctx2.textAlign = 'left';
  ctx2.fillText('Max', barX2 + barWidth2 + 5, barY2 + 5);
  ctx2.fillText('0', barX2 + barWidth2 + 5, barY2 + barHeight2 + 5);
  
  // Position MSE value to avoid overlap with "Max" label
  const mseY = barY2 + barHeight2 - errorHeight2 + 5;
  const minMseY = barY2 + 20; // Minimum position to avoid overlap with "Max"
  const finalMseY = Math.max(mseY, minMseY);
  ctx2.fillText(`${mse.toFixed(1)}`, barX2 + barWidth2 + 5, finalMseY);
  
  // Draw "Erreur" label
  ctx2.font = '14px sans-serif';
  ctx2.textAlign = 'center';
  ctx2.fillText('Erreur', barX2 + barWidth2 / 2, barY2 - 10);
  
  // Update info display
  const slope = Math.tan(angle2);
  const intercept = anchor2.y - slope * anchor2.x;
  const mText = isFinite(slope) ? slope.toFixed(2) : '∞';
  const bText = isFinite(intercept) ? intercept.toFixed(2) : '∞';
  info2.textContent = `f(x) = ${mText}x + ${bText}`;
}

// Handle slider input for second widget
pointSlider2.addEventListener('input', (e) => {
  const numPoints = parseInt(e.target.value);
  pointCount2.textContent = numPoints;
  generateRandomPoints2(numPoints);
  draw2();
});

// Helper function for distance calculation (second widget)
function distance2(p1, p2) {
  return Math.hypot(p1.x - p2.x, p1.y - p2.y);
}

// Mouse event handlers for second widget
canvas2.addEventListener('mousedown', (e) => {
  e.preventDefault();
  const rect = canvas2.getBoundingClientRect();
  const mouse = { x: e.clientX - rect.left, y: e.clientY - rect.top };
  const graphX2 = (width2 - graphWidth2) / 2 - graphOffsetX2;
  
  mouseDownPos2 = { x: mouse.x, y: mouse.y };
  hasMoved2 = false;
  
  if (mouse.x < graphX2 || mouse.x > graphX2 + graphWidth2) return;
  
  const graphMouse = { x: mouse.x - graphX2, y: mouse.y };
  
  if (e.button === 0) {
    if (distance2(graphMouse, anchor2) <= anchorRadius2) {
      dragging2 = true;
      dragMode2 = 'translate';
      return;
    }
    
    // Check if clicking on the line for rotation
    const dx = Math.cos(angle2);
    const dy = Math.sin(angle2);
    const px = graphMouse.x - anchor2.x;
    const py = graphMouse.y - anchor2.y;
    const distToLine = Math.abs(dy * px - dx * py);
    if (distToLine < 10) {
      dragging2 = true;
      dragMode2 = 'rotate';
      return;
    }
    
    // Check if clicking on existing point
    for (let i = 0; i < points2.length; i++) {
      if (distance2(graphMouse, points2[i]) < outerRadius2) {
        // Set up for potential drag (will be removed if no movement detected)
        dragging2 = true;
        dragMode2 = 'point';
        draggedPointIndex2 = i;
        return;
      }
    }
    
    // Add new blue point
    const constrainedX = Math.max(15, Math.min(graphWidth2 - 15, graphMouse.x));
    const constrainedY = Math.max(15, Math.min(height2 - 15, graphMouse.y));
    points2.push({ x: constrainedX, y: constrainedY, label: 1 });
  } else if (e.button === 2) {
    // Right click: add blue point
    const constrainedX = Math.max(15, Math.min(graphWidth2 - 15, graphMouse.x));
    const constrainedY = Math.max(15, Math.min(height2 - 15, graphMouse.y));
    points2.push({ x: constrainedX, y: constrainedY, label: 1 });
  }
  
  draw2();
});

canvas2.addEventListener('mousemove', (e) => {
  const rect = canvas2.getBoundingClientRect();
  const mouse = { x: e.clientX - rect.left, y: e.clientY - rect.top };
  const graphX2 = (width2 - graphWidth2) / 2 - graphOffsetX2;
  const graphMouse = { x: mouse.x - graphX2, y: mouse.y };
  
  if (mouseDownPos2 && distance2(mouse, mouseDownPos2) > 3) {
    hasMoved2 = true;
  }
  
  if (dragging2) {
    if (dragMode2 === 'translate') {
      // Constrain anchor to graph boundaries
      anchor2.x = Math.max(15, Math.min(graphWidth2 - 15, graphMouse.x));
      anchor2.y = Math.max(15, Math.min(height2 - 15, graphMouse.y));
    } else if (dragMode2 === 'rotate') {
      const dx = graphMouse.x - anchor2.x;
      const dy = graphMouse.y - anchor2.y;
      angle2 = Math.atan2(dy, dx);
    } else if (dragMode2 === 'point' && draggedPointIndex2 >= 0) {
      points2[draggedPointIndex2].x = Math.max(15, Math.min(graphWidth2 - 15, graphMouse.x));
      points2[draggedPointIndex2].y = Math.max(15, Math.min(height2 - 15, graphMouse.y));
    }
    draw2();
  } else {
    // Update cursor based on what's under the mouse
    if (mouse.x < graphX2 || mouse.x > graphX2 + graphWidth2) {
      canvas2.style.cursor = 'default';
      return;
    }
    
    // Check if over anchor point
    if (distance2(graphMouse, anchor2) <= anchorRadius2) {
      canvas2.style.cursor = 'grab';
      return;
    }
    
    // Check if over decision line
    const dx = Math.cos(angle2);
    const dy = Math.sin(angle2);
    const px = graphMouse.x - anchor2.x;
    const py = graphMouse.y - anchor2.y;
    const distToLine = Math.abs(dy * px - dx * py);
    if (distToLine < 10) {
      canvas2.style.cursor = 'grab';
      return;
    }
    
    // Check if over a point
    for (let p of points2) {
      if (distance2(graphMouse, p) < outerRadius2) {
        canvas2.style.cursor = 'grab';
        return;
      }
    }
    
    // Default cursor for empty space
    canvas2.style.cursor = 'default';
  }
});

canvas2.addEventListener('mouseup', (e) => {
  // Check if it was a click (no movement) on a point to remove it
  if (dragMode2 === 'point' && draggedPointIndex2 >= 0 && !hasMoved2) {
    points2.splice(draggedPointIndex2, 1);
    draw2();
  }
  
  dragging2 = false;
  dragMode2 = null;
  draggedPointIndex2 = -1;
  mouseDownPos2 = null;
  hasMoved2 = false;
});

canvas2.addEventListener('contextmenu', (e) => {
  e.preventDefault();
});

// Touch event handlers for second widget
function getTouchCoordinates2(e) {
  const rect = canvas2.getBoundingClientRect();
  const touch = e.touches[0] || e.changedTouches[0];
  return { x: touch.clientX - rect.left, y: touch.clientY - rect.top };
}

canvas2.addEventListener('touchstart', (e) => {
  e.preventDefault();
  const touch = getTouchCoordinates2(e);
  const graphX2 = (width2 - graphWidth2) / 2 - graphOffsetX2;
  
  touchStartTime2 = Date.now();
  touchHoldTriggered2 = false;
  
  mouseDownPos2 = { x: touch.x, y: touch.y };
  hasMoved2 = false;
  
  if (touch.x < graphX2 || touch.x > graphX2 + graphWidth2) return;
  
  const graphTouch = { x: touch.x - graphX2, y: touch.y };
  
  touchHoldTimer2 = setTimeout(() => {
    touchHoldTriggered2 = true;
    for (let i = 0; i < points2.length; i++) {
      if (distance2(graphTouch, points2[i]) < outerRadius2) {
        points2.splice(i, 1);
        draw2();
        return;
      }
    }
    const constrainedX = Math.max(15, Math.min(graphWidth2 - 15, graphTouch.x));
    const constrainedY = Math.max(15, Math.min(height2 - 15, graphTouch.y));
    points2.push({ x: constrainedX, y: constrainedY, label: 1 });
    draw2();
  }, 500);
  
  if (distance2(graphTouch, anchor2) <= anchorRadius2) {
    dragging2 = true;
    dragMode2 = 'translate';
    return;
  }
  
  // Check if touching on the line for rotation
  const dx = Math.cos(angle2);
  const dy = Math.sin(angle2);
  const px = graphTouch.x - anchor2.x;
  const py = graphTouch.y - anchor2.y;
  const distToLine = Math.abs(dy * px - dx * py);
  if (distToLine < 10) {
    dragging2 = true;
    dragMode2 = 'rotate';
    return;
  }
  
  for (let i = 0; i < points2.length; i++) {
    if (distance2(graphTouch, points2[i]) < outerRadius2) {
      dragging2 = true;
      dragMode2 = 'point';
      draggedPointIndex2 = i;
      return;
    }
  }
});

canvas2.addEventListener('touchmove', (e) => {
  e.preventDefault();
  const touch = getTouchCoordinates2(e);
  const graphX2 = (width2 - graphWidth2) / 2 - graphOffsetX2;
  const graphTouch = { x: touch.x - graphX2, y: touch.y };
  
  if (touchHoldTimer2) {
    clearTimeout(touchHoldTimer2);
    touchHoldTimer2 = null;
  }
  
  if (mouseDownPos2 && distance2(touch, mouseDownPos2) > 3) {
    hasMoved2 = true;
  }
  
  if (dragging2) {
    if (dragMode2 === 'translate') {
      // Constrain anchor to graph boundaries
      anchor2.x = Math.max(15, Math.min(graphWidth2 - 15, graphTouch.x));
      anchor2.y = Math.max(15, Math.min(height2 - 15, graphTouch.y));
    } else if (dragMode2 === 'rotate') {
      const dx = graphTouch.x - anchor2.x;
      const dy = graphTouch.y - anchor2.y;
      angle2 = Math.atan2(dy, dx);
    } else if (dragMode2 === 'point' && draggedPointIndex2 >= 0) {
      points2[draggedPointIndex2].x = Math.max(15, Math.min(graphWidth2 - 15, graphTouch.x));
      points2[draggedPointIndex2].y = Math.max(15, Math.min(height2 - 15, graphTouch.y));
    }
    draw2();
  }
});

canvas2.addEventListener('touchend', (e) => {
  e.preventDefault();
  
  if (touchHoldTimer2) {
    clearTimeout(touchHoldTimer2);
    touchHoldTimer2 = null;
  }
  
  if (touchHoldTriggered2) {
    dragging2 = false;
    dragMode2 = null;
    draggedPointIndex2 = -1;
    mouseDownPos2 = null;
    hasMoved2 = false;
    return;
  }
  
  if (!hasMoved2 && Date.now() - touchStartTime2 < 300) {
    const touch = getTouchCoordinates2(e);
    const graphX2 = (width2 - graphWidth2) / 2 - graphOffsetX2;
    
    if (touch.x >= graphX2 && touch.x <= graphX2 + graphWidth2) {
      const graphTouch = { x: touch.x - graphX2, y: touch.y };
      
      for (let i = 0; i < points2.length; i++) {
        if (distance2(graphTouch, points2[i]) < outerRadius2) {
          points2.splice(i, 1);
          draw2();
          dragging2 = false;
          dragMode2 = null;
          draggedPointIndex2 = -1;
          mouseDownPos2 = null;
          hasMoved2 = false;
          return;
        }
      }
      
      const constrainedX = Math.max(15, Math.min(graphWidth2 - 15, graphTouch.x));
      const constrainedY = Math.max(15, Math.min(height2 - 15, graphTouch.y));
      points2.push({ x: constrainedX, y: constrainedY, label: 1 });
      draw2();
    }
  }
  
  dragging2 = false;
  dragMode2 = null;
  draggedPointIndex2 = -1;
  mouseDownPos2 = null;
  hasMoved2 = false;
});

</script>
