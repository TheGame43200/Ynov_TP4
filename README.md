# Notes de Conception : TP Pipeline CI/CD

Ce document résume les étapes clés pour la mise en place d'une pipeline de CI/CD pour une application Python simple, en utilisant GitHub Actions.

## 1. Mise en place du Repository Git

*   Initialiser un repository Git local.
*   Créer un repository correspondant sur GitHub (manuellement, si nécessaire).
*   Lier le repository local au distant.

## 2. Développement de l'Application Python

*   Créer `simple_math.py` avec une fonction d'addition.
*   Développer `test_simple_math.py` pour inclure un test unitaire pour l'addition.

## 3. Premier Push et Workflow de Tests

*   Pousser le code initial sur GitHub.
*   Mettre en place un workflow GitHub Actions (`.github/workflows/python-app.yml`) pour exécuter automatiquement les tests unitaires lors des pushes et pull requests.

## 4. Évolution de l'Application

*   Ajouter une fonction de soustraction à `simple_math.py`.
*   Ajouter le test unitaire correspondant à `test_simple_math.py`.

## 5. Validation Automatique des Modifications

*   Pousser les modifications sur GitHub. Le workflow CI/CD se déclenchera pour valider la nouvelle fonctionnalité via les tests.

## 6. Intégration du Linting

*   Ajouter une étape de linting (`pylint`) au workflow GitHub Actions pour assurer la qualité et la conformité du code.

## 7. Conteneurisation avec Docker

*   Créer un `Dockerfile` pour construire une image Docker de l'application. La commande de démarrage du conteneur exécutera les tests unitaires.
*   Intégrer une étape de build Docker au workflow GitHub Actions.

## 8. Finalisation et Vérification

*   Pousser le `Dockerfile` et les dernières modifications du workflow.
*   Vérifier l'exécution complète de la pipeline (tests, lint, build Docker) dans l'onglet "Actions" de GitHub.

## Conclusion

Ce TP a permis de couvrir les aspects fondamentaux d'une pipeline CI/CD, de la gestion de version à la conteneurisation, en passant par les tests et l'analyse de code.
