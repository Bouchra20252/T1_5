# Semaine 3 : l'API, notes du binôme

> Deux questions, quelques phrases chacune. Répondez avec ce que vous avez observé, pas avec le cours.

## 1. Pourquoi l'API refuse-t-elle de démarrer sans `models/sentiment.joblib`, plutôt que de démarrer et de répondre 503 ?

Parce que le modèle est indispensable au fonctionnement de l’API. Il est chargé au démarrage pour éviter de lancer une application incapable de faire des prédictions.

## 2. Un texte vide est refusé deux fois : par Pydantic, puis par `predict()`. Est-ce redondant ?
 Parce que le modèle est indispensable au fonctionnement de l’API. Il est chargé au démarrage pour éviter de lancer une application incapable de faire des prédictions.
