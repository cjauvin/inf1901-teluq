---
title: "Test sur l'intelligence artificielle décodée"
weight: 6
---

## Test sur l'intelligence artificielle décodée

Ce test vise à évaluer votre compréhension des grands enjeux liés à l'IA abordés dans le documentaire L'intelligence artificielle décodée que vous avez visionné à l'activité 1 du module 1. Il permet de revenir sur les acteurs engagés dans le domaine, sur leur point de vue sur les aspects de l'IA traité dans le documentaire et et sur les enjeux éthique de l'IA tels qu'ils se posent aujourd'hui.

<style>
.quiz-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
}

.question-container {
    background: #f5f5f5;
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
    overflow: hidden;
}

.question-text {
    font-size: 18px;
    font-weight: bold;
    margin-bottom: 15px;
    color: #333;
}

.question-counter {
    font-size: 14px;
    color: #666;
    margin-bottom: 10px;
}

.answer-option {
    margin: 10px 0;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    background-color: #fff;
    border: 1px solid #ddd;
    display: flex;
    align-items: center;
}

.answer-option:hover {
    background-color: #f8f9fa;
}

.answer-option.selected {
    background-color: #e3f2fd;
    border: 2px solid #2196f3;
}

.answer-option input[type="radio"] {
    margin-right: 10px;
    margin-left: 0;
}

.answer-option label {
    color: #333;
    font-weight: normal;
    cursor: pointer;
    display: inline;
    width: auto;
    flex: 1;
}

.answer-option.correct {
    background-color: #d4edda;
    border: 2px solid #28a745;
}

.answer-option.correct label {
    color: #155724;
    font-weight: bold;
}

.answer-option.incorrect {
    background-color: #f8d7da;
    border: 2px solid #dc3545;
}

.answer-option.incorrect label {
    color: #721c24;
    font-weight: bold;
}

.quiz-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 12px 24px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 20px;
    float: right;
}

.quiz-button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}

.quiz-button:hover:not(:disabled) {
    background-color: #0056b3;
}

.results-container {
    text-align: center;
    padding: 20px;
}

.score-display {
    font-size: 24px;
    font-weight: bold;
    color: #007bff;
    margin-bottom: 20px;
}

.recap-section {
    text-align: left;
    margin-top: 30px;
}

.recap-question {
    background: #f8f9fa;
    padding: 15px;
    margin-bottom: 15px;
    border-radius: 5px;
    border-left: 4px solid #007bff;
}

.recap-question.correct {
    border-left-color: #28a745;
}

.recap-question.incorrect {
    border-left-color: #dc3545;
}

.recap-question-text {
    font-weight: bold;
    margin-bottom: 15px;
    color: #333;
    font-size: 16px;
}

.recap-answer {
    margin: 5px 0;
    padding: 8px;
    border-radius: 5px;
    color: #333;
    font-size: 14px;
    background-color: #fff;
    border: 1px solid #ddd;
}

.recap-answer.correct-answer {
    background-color: #d4edda;
    border: 2px solid #28a745;
    color: #155724;
    font-weight: bold;
}

.recap-answer.user-incorrect {
    background-color: #f8d7da;
    border: 2px solid #dc3545;
    color: #721c24;
    text-decoration: line-through;
    font-weight: bold;
}

.hidden {
    display: none !important;
}

#results-section {
    display: none;
}
</style>

{{< html >}}
<div class="quiz-container">
    <div id="quiz-section">
        <div class="question-counter">
            Question <span id="current-question">1</span> sur 10
        </div>
        <div class="question-container">
            <div class="question-text" id="question-text"></div>
            <div id="answers-container"></div>
            <button class="quiz-button" id="action-button" disabled>Répondre</button>
        </div>
    </div>

    <div id="results-section" class="results-container hidden" style="display: none;">
        <div class="score-display">
            Votre score: <span id="final-score"></span>/10
        </div>
        <div class="recap-section">
            <h3>Récapitulatif des questions</h3>
            <div id="recap-container"></div>
        </div>
    </div>
</div>
{{< /html >}}

<script>
const questions = [
    {
        question: "Selon vous, quel est l'objectif principal de l'émission spéciale « l'intelligence artificielle décodée » animée par Patrice Roy ?",
        answers: [
            "Former le public à la programmation en intelligence artificielle.",
            "Analyser les enjeux et les impacts de l'intelligence artificielle sur la société.",
            "Présenter les dernières innovations en robotique humanoïde.",
            "Promouvoir les produits technologiques de Meta."
        ],
        correct: 1
    },
    {
        question: "Quel exemple concret a été donné dans le documentaire pour illustrer les avancées de l'IA dans la médecine ?",
        answers: [
            "L'amélioration du diagnostic du cancer grâce à l'analyse d'images médicales par l'IA.",
            "L'usage de robots pour remplacer les patients.",
            "L'utilisation de l'IA pour abolir les hôpitaux.",
            "La suppression totale de la chirurgie manuelle."
        ],
        correct: 0
    },
    {
        question: "Quels sont les quatre axes principaux abordés dans l'émission ?",
        answers: [
            "IA et santé, IA et éducation, IA et économie, IA et culture.",
            "Développement de l'IA, régulation gouvernementale, éducation en IA, IA et environnement.",
            "Ce qui nous a menés jusqu'ici, où en sommes-nous, un futur lumineux, un futur sombre",
            "Historique de l'IA, applications militaires, éthique de l'IA, avenir de l'IA."
        ],
        correct: 2
    },
    {
        question: "Quelles expertes ou quels experts en intelligence artificielle ont participé à l'émission ?",
        answers: [
            "Mark zuckerberg et Jeff BezoZ",
            "Tim Cook et Satya Nadella.",
            "Joëlle Pineau, Yosua Bengio, Yann LeCun, Valérie Pisano.",
            "Elon Musk et Sundar Pichai."
        ],
        correct: 2
    },
    {
        question: "Quelles sont les applications médicales de l'IA, discutées le documentaire ?",
        answers: [
            "L'IA remplaçant entièrement le personnel médical.",
            "Diagnostic assisté, médecine personnalisée et le suivi à distance.",
            "L'IA supprimant le besoin de laboratoires médicaux.",
            "L'IA rendant obsolète les hôpitaux traditionnels"
        ],
        correct: 1
    },
    {
        question: "Quelle divergence de point de vue a été mise en évidence entre Yoshua Bewngio et Yann LeCun lors de l'émission.",
        answers: [
            "Leur conflit sur la propriété intellectuelle des algorithmes d'IA.",
            "Leur opposition concernant les applications militaires de l'IAA",
            "Leur divergence sur les risques et les bénéfices futurs de l'IA",
            "Leur désaccord sur l'existence de l'intelligence artificielle."
        ],
        correct: 2
    },
    {
        question: "Quel rôle l'intelligence artificielle a-t-elle joué dans la production de l'émission ?",
        answers: [
            "Elle a été utilisée pour créer certains éléments de design et de contenu.",
            "Elle a servi de présentatrice virtuelle de l'émission",
            "Elle a généré, en temps réel, les réponses des expertes ou experts invités.",
            "Elle a entièrement remplacé l'équipe de production humaine."
        ],
        correct: 0
    },
    {
        question: "Quel est l'un des grands défis soulevés par les experts concernant l'utilisation de l'IA dans la société ?",
        answers: [
            "L'absence totale d'impact sur l'emploi.",
            "Le risque de biais et d'injustices dans les décisions automatisées.",
            "L'interdiction complète de l'IA par les gouvernements.",
            "Le remplacement des ordinateurs par des machines à vapeur."
        ],
        correct: 1
    },
    {
        question: "Selon les discussions de l'émission, quel est un des avantages potentiels de l'IA en éducation ?",
        answers: [
            "Supprimer tous les enseignements humains.",
            "Personnaliser les parcours d'apprentissage au profil de chaque apprenante et apprenante.",
            "Remplacer les écoles physiques par des centres commerciaux.",
            "Uniformiser l'enseignement sans prendre en compte les besoins individuels."
        ],
        correct: 1
    },
    {
        question: "Quelles inquiétudes concernant l'A a été exprimée par Yoshua Bengio lors de l'émission ?",
        answers: [
            "La lenteur de l'innovation technologique.",
            "L'impossibilité d'utiliser l'IA dans les pays du Sud.",
            "L'absence de garde-fous suffisants pour encadrer le développement de l'IA",
            "Le coût trop élevé des applications d'IA dans l'industrie musicale."
        ],
        correct: 2
    }
];

let currentQuestion = 0;
let userAnswers = [];
let score = 0;
let answered = false;

function displayQuestion() {
    const questionData = questions[currentQuestion];
    document.getElementById('current-question').textContent = currentQuestion + 1;
    document.getElementById('question-text').textContent = questionData.question;

    const answersContainer = document.getElementById('answers-container');
    answersContainer.innerHTML = '';

    questionData.answers.forEach((answer, index) => {
        const answerDiv = document.createElement('div');
        answerDiv.className = 'answer-option';
        answerDiv.innerHTML = `
            <input type="radio" name="answer" value="${index}" id="answer-${index}">
            <label for="answer-${index}">${String.fromCharCode(97 + index)}. ${answer}</label>
        `;
        answersContainer.appendChild(answerDiv);

        answerDiv.addEventListener('click', () => {
            document.getElementById(`answer-${index}`).checked = true;

            // Remove selected class from all options
            document.querySelectorAll('.answer-option').forEach(opt => {
                opt.classList.remove('selected');
            });

            // Add selected class to clicked option
            answerDiv.classList.add('selected');

            enableActionButton();
        });
    });

    document.getElementById('action-button').disabled = true;
    document.getElementById('action-button').textContent = 'Répondre';
    answered = false;
}

function enableActionButton() {
    document.getElementById('action-button').disabled = false;
}

function handleAnswer() {
    if (!answered) {
        const selectedAnswer = document.querySelector('input[name="answer"]:checked');
        if (selectedAnswer) {
            const userAnswer = parseInt(selectedAnswer.value);
            const correctAnswer = questions[currentQuestion].correct;

            userAnswers.push(userAnswer);

            if (userAnswer === correctAnswer) {
                score++;
            }

            document.querySelectorAll('.answer-option').forEach((option, index) => {
                if (index === correctAnswer) {
                    option.classList.add('correct');
                } else if (index === userAnswer && userAnswer !== correctAnswer) {
                    option.classList.add('incorrect');
                }
            });

            document.getElementById('action-button').textContent = 'Question suivante';
            answered = true;

            if (currentQuestion === questions.length - 1) {
                document.getElementById('action-button').textContent = 'Voir les résultats';
            }
        }
    } else {
        if (currentQuestion < questions.length - 1) {
            currentQuestion++;
            displayQuestion();
        } else {
            showResults();
        }
    }
}

function showResults() {
    document.getElementById('quiz-section').classList.add('hidden');
    document.getElementById('results-section').style.display = 'block';
    document.getElementById('results-section').classList.remove('hidden');
    document.getElementById('final-score').textContent = score;

    const recapContainer = document.getElementById('recap-container');
    recapContainer.innerHTML = '';

    questions.forEach((question, index) => {
        const userAnswer = userAnswers[index];
        const correctAnswer = question.correct;
        const isCorrect = userAnswer === correctAnswer;

        const recapDiv = document.createElement('div');
        recapDiv.className = `recap-question ${isCorrect ? 'correct' : 'incorrect'}`;

        let answersHtml = '';
        question.answers.forEach((answer, answerIndex) => {
            let answerClass = '';
            if (answerIndex === correctAnswer) {
                answerClass = 'correct-answer';
            } else if (answerIndex === userAnswer && !isCorrect) {
                answerClass = 'user-incorrect';
            }

            answersHtml += `<div class="recap-answer ${answerClass}">${String.fromCharCode(97 + answerIndex)}. ${answer}</div>`;
        });

        recapDiv.innerHTML = `
            <div class="recap-question-text">Question ${index + 1}: ${question.question}</div>
            ${answersHtml}
        `;

        recapContainer.appendChild(recapDiv);
    });
}

document.getElementById('action-button').addEventListener('click', handleAnswer);

// Initialize the quiz
displayQuestion();

// Debug: Add test data for showResults
// userAnswers = [2, 0, 2, 2, 1, 2, 0, 1, 1, 2]; // Some test answers
// score = 7; // Test score

// showResults();

// Ensure results section is hidden on load (commented out for debugging)
// document.getElementById('results-section').classList.add('hidden');
</script>