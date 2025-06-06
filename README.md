# trainploration : Analyse Exploratoire de la Ponctualité des Trains Transilien

🎯 Objectif

Ce projet vise à analyser l’évolution de la ponctualité des lignes Transilien (Ile-de-France) depuis le début des mesures disponibles, en identifiant les lignes les plus et les moins ponctuelles, à la fois sur l'ensemble de la période et spécifiquement depuis janvier 2024.
🧩 Données

    Source : Fichier ponctualite-mensuelle-transilien.csv

    Période : De janvier 2013 à avril 2025

    Colonnes clés :

        Date : Mois de la mesure

        Ligne : Code de la ligne Transilien

        Taux de ponctualité : Pourcentage de trains à l’heure

        Nombre de voyageurs à l'heure pour un voyageur en retard : Mesure complémentaire d’impact

⚙️ Méthodologie

    Préparation

        Conversion de la colonne Date en format datetime

        Tri chronologique

        Filtrage des données depuis janvier 2024 pour certaines analyses

    Identification des performances extrêmes

        Pour chaque mois, identification de la ligne avec :

            La meilleure ponctualité

            La pire ponctualité

        Comptage du nombre d’occurrences par ligne (meilleure / pire performance)

    Mesures de dispersion

        Calcul de l’écart-type (volatilité) du taux de ponctualité par ligne

    Visualisations interactives

        Graphiques en barres : fréquence des lignes les plus ou moins ponctuelles

        Graphiques en ligne : évolution du taux de ponctualité des lignes les plus emblématiques

🏆 Lignes les plus ponctuelles
📅 Sur toute la période

    La ligne H est apparue comme la plus ponctuelle le plus grand nombre de fois.

    D'autres lignes comme K montrent également de très bons résultats.

📆 Depuis janvier 2024

    La ligne K domine clairement avec de nombreuses apparitions en tête de classement.

👉 Visualisation :
Visuel montrant les lignes avec les meilleures ponctualités depuis janvier 2013
![best_over_time](https://github.com/user-attachments/assets/4eb2ec7a-d70f-4003-b934-b2819463b3c7)

Et depuis 2024 
![best_since_2024](https://github.com/user-attachments/assets/27ae069f-92a8-4380-a61f-3ea9fc63f2bf)

🚨 Lignes les moins ponctuelles
📅 Sur toute la période

    La ligne A est régulièrement la moins ponctuelle.

📆 Depuis janvier 2024

    La ligne B se distingue par des résultats particulièrement bas.

👉 Visualisation :
Visuel montrant les lignes avec les moins bonnes ponctualités depuis janvier 2013
![worst_over_time](https://github.com/user-attachments/assets/420581de-c001-4c75-b8f2-ab00ad99ff16)

Et depuis 2024
![worst_since_2024](https://github.com/user-attachments/assets/d9bd4034-d521-4408-97fd-69a16a47bc9d)

📈 Évolution temporelle
Comparaison des meilleures lignes

    Lignes analysées : H (historique), K (2024)

    La ligne H montre une performance globalement stable avec des pics de performance.

    La ligne K affiche une nette amélioration en 2024.

Comparaison des pires lignes

    Lignes analysées : A (historique), B (2024)

    Les performances de la ligne A sont constamment faibles.

    La ligne B présente une grande variabilité et des pics de très faible ponctualité en 2024.

👉 Visualisations :

    Lignes de temps interactives avec couleurs personnalisées

📊 Analyse comparative – Focus sur 4 lignes

Un graphique final illustre l’évolution des lignes :

    Performantes : H (historique), K (depuis 2024)

    Défaillantes : A (historique), B (depuis 2024)

Ce graphique comprend :

    Courbes de tendance

    Ligne de seuil de performance à 80%

    Annotations des valeurs extrêmes (meilleurs et pires mois)

📌 Enseignements clés

    Certaines lignes comme H et K se distinguent par leur constance ou leur progression récente.

    D’autres, comme A et B, montrent des difficultés structurelles de ponctualité.

    L’écart-type par ligne confirme que certaines souffrent d’une ponctualité instable.

🛠️ Compétences mobilisées

    Python : pandas, matplotlib, seaborn, plotly

    Traitement et nettoyage de séries temporelles

    Agrégation, groupby et statistiques descriptives

    Visualisations interactives (Plotly)

    Ajout d’annotations dynamiques et interprétables

🔮 Perspectives

    Intégration d'autres variables (trafic, météo, incidents)

    Modélisation prédictive de la ponctualité

    Création d’un dashboard interactif (ex. Streamlit ou Dash)
