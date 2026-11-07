# Fiche de cadrage : Priorisation des avis négatifs

## Besoin en une phrase (obligatoire)

Identifier et classer automatiquement les avis clients négatifs afin d'aider l'équipe support à traiter en priorité les réclamations les plus importantes.

## Utilisateur final (obligatoire)

Les responsables du service client et les agents du support chargés du traitement des réclamations.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [x] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

Le machine learning est adapté car (a) les anciens avis peuvent être étiquetés selon leur sentiment et leur niveau de priorité afin d'entraîner un modèle de classification. De plus, (c) un modèle entraîné peut analyser rapidement un grand nombre d'avis avec un coût limité par requête.

## Données nécessaires et leur origine (obligatoire)

Les avis clients, leur contenu textuel, leur date et leurs étiquettes de sentiment ou de priorité. Ces données proviennent des plateformes d'avis, des enquêtes de satisfaction et de l'historique du service client.

## Métrique de succès et seuil d'acceptation (obligatoire)

Atteindre au moins 85 % de précision dans la détection des avis négatifs sur un jeu de test indépendant, avec un rappel suffisant pour ne pas manquer les réclamations importantes.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Un avis urgent mal classé peut retarder le traitement d'une réclamation importante. Les agents du support doivent pouvoir vérifier les résultats et modifier manuellement les priorités.

## Risques éthiques ou de confidentialité (obligatoire)

Les avis peuvent contenir des données personnelles ou des informations sensibles. Il faut limiter leur collecte, anonymiser les informations identifiantes et surveiller les biais du modèle.

## Approche écartée et pourquoi (facultatif)

Les règles métier seules sont écartées car elles détectent difficilement les nuances du langage, le sarcasme et les différentes manières d'exprimer une insatisfaction.