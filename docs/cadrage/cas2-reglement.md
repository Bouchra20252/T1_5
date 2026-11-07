# Fiche de cadrage : Questions sur le règlement intérieur

> Remplir chaque rubrique en une à trois phrases. Les rubriques marquées (obligatoire) sont vérifiées par `pytest`.

## Besoin en une phrase (obligatoire)
Automatiser les réponses aux questions fréquentes des employés concernant les articles et les clauses du règlement intérieur de l'entreprise.

## Utilisateur final (obligatoire)
Les collaborateurs et nouveaux arrivants de l'entreprise souhaitant consulter rapidement les consignes et règles internes.

## Approche retenue (obligatoire)

Cocher une seule case :

- [ ] Règles métier
- [ ] Machine learning
- [x] RAG
- [ ] Modèle génératif seul

## Justification (obligatoire, citer au moins deux critères de la grille : (a) données étiquetées, (b) vérifiabilité, (c) coût par requête, (d) conséquence d'une erreur)
L'approche RAG est retenue car elle ne nécessite pas de (a) données étiquetées d'entraînement massives tout en offrant une excellente (b) vérifiabilité grâce à la récupération directe des extraits textuels du document officiel.

## Données nécessaires et leur origine (obligatoire)
Le document PDF officiel du règlement intérieur de l'entreprise fourni par le département des ressources humaines et des affaires juridiques.

## Métrique de succès et seuil d'acceptation (obligatoire)
Atteindre un taux de pertinence des réponses supérieur à 90% évalué sur un ensemble de questions-tests validées par les RH.

## Conséquence d'une erreur et validation humaine prévue (obligatoire)
Une information erronée peut perturber l'employé sur ses droits ou devoirs ; c'est pourquoi chaque réponse affiche la source exacte et un lien de contact vers les RH en cas de doute.

## Risques éthiques ou de confidentialité (obligatoire)
Les questions et documents internes ne doivent pas fuiter en externe ; le système doit être déployé dans un environnement sécurisé et restreint aux salariés.

## Approche écartée et pourquoi (facultatif)
L'utilisation d'un modèle génératif seul a été écartée en raison des risques importants d'hallucination sur des règles juridiques strictes.