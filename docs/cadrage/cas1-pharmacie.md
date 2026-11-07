# Fiche de cadrage : Ordonnances incomplètes en pharmacie

## Besoin en une phrase (obligatoire)

Aider le pharmacien à repérer les informations manquantes ou incomplètes sur une ordonnance avant son traitement.

## Utilisateur final (obligatoire)

Le pharmacien ou le préparateur en pharmacie qui vérifie les ordonnances reçues.

## Approche retenue (obligatoire)

Cocher une seule case :

- [x] Règles métier
- [ ] Machine learning
- [ ] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)

Les règles métier sont adaptées car (b) chaque contrôle peut être vérifié à partir de critères explicites et compréhensibles. De plus, (d) une erreur peut avoir des conséquences sur la sécurité du patient, donc le résultat doit rester vérifiable par un professionnel de santé. Il n'est pas nécessaire de disposer d'un grand jeu de données étiquetées.

## Données nécessaires et leur origine (obligatoire)

Les informations présentes sur l'ordonnance : identité du patient, date, identification du prescripteur, médicaments prescrits, posologie et durée du traitement. Elles proviennent des ordonnances et des règles de vérification validées par la pharmacie.

## Métrique de succès et seuil d'acceptation (obligatoire)

Atteindre au moins 95 % de détection des champs obligatoires manquants sur un jeu de test préparé et vérifié par des pharmaciens.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)

Une information manquante non détectée peut entraîner une erreur de délivrance ou retarder le traitement. Le pharmacien doit toujours vérifier l'ordonnance et prendre la décision finale.

## Risques éthiques ou de confidentialité (obligatoire)

Les ordonnances contiennent des données personnelles et médicales sensibles. Leur accès doit être limité et leur stockage sécurisé, conformément aux règles de confidentialité.

## Approche écartée et pourquoi (facultatif)

Le modèle génératif seul est écarté car il peut produire des informations incorrectes et ses décisions sont moins facilement vérifiables qu'une liste de règles explicites.