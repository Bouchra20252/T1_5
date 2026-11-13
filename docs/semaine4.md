## 1. Couverture

- Avant (étape A) : 91 %.
- Certaines branches de `api/main.py` n'étaient pas couvertes : validation des entrées, gestion des erreurs et comportement lorsque le modèle n'est pas disponible.
- Après les tests d'intégration (étape D) : 97,44 %.
- Couverture finale : 97,75 %, soit au-dessus de l'objectif de 95 %.

## 2. Défauts trouvés

| Symptôme | Test qui l'a révélé | Correction |
| --- | --- | --- |
| Les textes contenant uniquement des espaces étaient acceptés. | Tests de limites et tests Hypothesis | Ajout d'un validateur rejetant les textes vides ou composés uniquement d'espaces. |
| Les erreurs internes pouvaient être confondues avec des erreurs de validation. | Tests d'intégration | Gestion des exceptions internes avec une réponse HTTP 500. |
| Le modèle pouvait être chargé avec des classes inattendues. | Test d'intégration du chargement du modèle | Vérification des classes attendues au démarrage. |
| Le contrat de réponse de l'API n'était pas suffisamment précis. | Mypy et tests de l'API | Ajout de types explicites avec TypedDict et Literal. |

## 3. Seuil d'abstention

- Seuil retenu : 0.60 ; 72 % des avis traités automatiquement et 28 % envoyés à un humain.
- À ce seuil, exactitude de 95.2 % sur les avis traités automatiquement (42 avis).
- Justification : réduire les erreurs en confiant les prédictions peu fiables à un humain.

## 4. Jeu d'or

- Bilan : 7 prédictions justes, 9 abstentions et 4 erreurs franches déclarées.
- Les 4 erreurs connues sont documentées avec xfail(strict=True) dans les tests.
- Ces chiffres montrent que le modèle sait s'abstenir, mais reste limité sur les formulations complexes, la négation et l'ironie.

## 5. Outils statiques

- Au départ, Ruff signalait 11 problèmes de qualité du code.
- Mypy ne signalait aucune erreur sur les 4 fichiers vérifiés.
- Après correction, Ruff ne signale plus aucune erreur.
- Les vérifications Mypy et les hooks pre-commit passent également.
- Conclusion : les outils statiques détectent des problèmes de style, d'organisation et de typage, mais ne remplacent pas les tests fonctionnels et d'intégration.