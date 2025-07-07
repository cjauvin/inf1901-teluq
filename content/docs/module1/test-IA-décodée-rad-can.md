---
title: "Test sur l'intelligence artificielle décodée"
weight: 6
draft: true
---

## Test sur l'intelligence artificielle décodée

Ce test vise à évaluer votre compréhension des grands enjeux liés à l'IA abordés dans le documentaire L'intelligence artificielle décodée que vous avez visionné à l'activité 1 du module 1. Il permet de revenir sur les acteurs engagés dans le domaine, sur leur point de vue sur les aspects de l'IA traité dans le documentaire et et sur les enjeux éthique de l'IA tels qu'ils se posent aujourd'hui.

<link rel="stylesheet" href="/css/quiz.css">

<div id="ia-decodee-quiz"></div>

<script src="/js/quiz.js"></script>
<script>
// Quiz data for this specific page
const questionsData = [
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
            "Mark Zuckerberg et Jeff Bezos",
            "Tim Cook et Satya Nadella",
            "Joëlle Pineau, Yosua Bengio, Yann LeCun, Valérie Pisano",
            "Elon Musk et Sundar Pichai"
        ],
        correct: 2
    },
    {
        question: "Quelles sont les applications médicales de l'IA, discutées le documentaire ?",
        answers: [
            "L'IA remplaçant entièrement le personnel médical",
            "Diagnostic assisté, médecine personnalisée et le suivi à distance",
            "L'IA supprimant le besoin de laboratoires médicaux",
            "L'IA rendant obsolète les hôpitaux traditionnels"
        ],
        correct: 1
    },
    {
        question: "Quelle divergence de point de vue a été mise en évidence entre Yoshua Bewngio et Yann LeCun lors de l'émission.",
        answers: [
            "Leur conflit sur la propriété intellectuelle des algorithmes d'IA",
            "Leur opposition concernant les applications militaires de l'IA",
            "Leur divergence sur les risques et les bénéfices futurs de l'IA",
            "Leur désaccord sur l'existence de l'intelligence artificielle"
        ],
        correct: 2
    },
    {
        question: "Quel rôle l'intelligence artificielle a-t-elle joué dans la production de l'émission ?",
        answers: [
            "Elle a été utilisée pour créer certains éléments de design et de contenu",
            "Elle a servi de présentatrice virtuelle de l'émission",
            "Elle a généré, en temps réel, les réponses des expertes ou experts invités",
            "Elle a entièrement remplacé l'équipe de production humaine"
        ],
        correct: 0
    },
    {
        question: "Quel est l'un des grands défis soulevés par les experts concernant l'utilisation de l'IA dans la société ?",
        answers: [
            "L'absence totale d'impact sur l'emploi",
            "Le risque de biais et d'injustices dans les décisions automatisées",
            "L'interdiction complète de l'IA par les gouvernements",
            "Le remplacement des ordinateurs par des machines à vapeur"
        ],
        correct: 1
    },
    {
        question: "Selon les discussions de l'émission, quel est un des avantages potentiels de l'IA en éducation ?",
        answers: [
            "Supprimer tous les enseignements humains",
            "Personnaliser les parcours d'apprentissage au profil de chaque apprenante et apprenante",
            "Remplacer les écoles physiques par des centres commerciaux",
            "Uniformiser l'enseignement sans prendre en compte les besoins individuels"
        ],
        correct: 1
    },
    {
        question: "Quelle inquiétude concernant l'A a été exprimée par Yoshua Bengio lors de l'émission ?",
        answers: [
            "La lenteur de l'innovation technologique",
            "L'impossibilité d'utiliser l'IA dans les pays du Sud",
            "L'absence de garde-fous suffisants pour encadrer le développement de l'IA",
            "Le coût trop élevé des applications d'IA dans l'industrie musicale"
        ],
        correct: 2
    }
];

// Initialize the quiz
document.addEventListener('DOMContentLoaded', function() {
    new Quiz('ia-decodee-quiz', questionsData);
});
</script>