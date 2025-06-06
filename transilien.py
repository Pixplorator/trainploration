import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go

# Fonction pour styliser les figures Plotly
def stylize_figure(fig, title_text):
    fig.update_layout(
        title={
            'text': title_text,
            'font': {
                'size': 24,
                'family': "Arial",
                'color': "black"
            },
            'x': 0.5,
            'xanchor': 'center'
        },
        font=dict(
            family="Arial",
            size=14,
            color="black"
        ),
        xaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=12)
        ),
        yaxis=dict(
            title_font=dict(size=18),
            tickfont=dict(size=12)
        ),
        legend=dict(
            title_font=dict(size=16),
            font=dict(size=14)
        )
    )
    return fig

# Charger les données
df = pd.read_csv("ponctualite-mensuelle-transilien.csv", delimiter=';')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m')
df = df.sort_values("Date")

# Traitement des valeurs manquantes dans "Taux de ponctualité"
# Remplir avec la médiane par date
print(f"Nombre de valeurs manquantes avant traitement: {df['Taux de ponctualité'].isna().sum()}")

# Calculer la médiane par date et remplir les valeurs manquantes
df['Taux de ponctualité'] = df.groupby('Date')['Taux de ponctualité'].transform(
    lambda x: x.fillna(x.median())
)

# Si après ce traitement il reste des valeurs manquantes (toute une date sans données),
# les remplir avec la médiane globale
global_median = df['Taux de ponctualité'].median()
df['Taux de ponctualité'] = df['Taux de ponctualité'].fillna(global_median)

print(f"Nombre de valeurs manquantes après traitement: {df['Taux de ponctualité'].isna().sum()}")
print(f"Médiane globale utilisée si nécessaire: {global_median:.2f}")

# Palette Coolors
coolors_palette = {
    "primary": "#1f271b",
    "secondary": "#19647e",
    "tertiary": "#28afb0",
    "quaternary": "#f4d35e",
    "quinary": "#ee964b"
}

# Analyse globale
max_impact = df["Nombre de voyageurs à l'heure pour un voyageur en retard"].max()
max_ponctualité = df["Taux de ponctualité"].max()

median_evolution = df.groupby("Date")["Taux de ponctualité"].median().reset_index()
median_evolution.columns = ["Date", "Mediane_Ponctualite"]
# Lignes les plus ponctuelles (global)
best_perf = df.groupby("Date")["Taux de ponctualité"].transform(max)
best_perf_df = df[df["Taux de ponctualité"] == best_perf]
counts_best = best_perf_df["Ligne"].value_counts().reset_index()
counts_best.columns = ["Ligne", "Count"]
"""fig = px.bar(counts_best, x="Ligne", y="Count", text="Count", text_auto=True,
             color_discrete_sequence=[coolors_palette["tertiary"]])
fig = stylize_figure(fig, "Lignes les plus ponctuelles au fil des années")
fig.show(renderer="browser")"""

# Lignes les moins ponctuelles (global)
worst_perf = df.groupby("Date")["Taux de ponctualité"].transform(min)
worst_perf_df = df[df["Taux de ponctualité"] == worst_perf]
counts_worst = worst_perf_df["Ligne"].value_counts().reset_index()
counts_worst.columns = ["Ligne", "Count"]
"""fig = px.bar(counts_worst, x="Ligne", y="Count", text="Count", text_auto=True,
             color_discrete_sequence=[coolors_palette["quinary"]])
fig = stylize_figure(fig, "Lignes les moins ponctuelles au fil des années")
fig.show(renderer="browser")"""

# Après 2024
valeur_sup_2024 = df[df["Date"] > "2023-12"] 

# Best depuis 2024
best_perf_2024 = valeur_sup_2024.groupby("Date")["Taux de ponctualité"].transform(max)
best_perf_df_2024 = valeur_sup_2024[valeur_sup_2024["Taux de ponctualité"] == best_perf_2024]
counts_2024 = best_perf_df_2024["Ligne"].value_counts().reset_index()
counts_2024.columns = ["Ligne", "Count"]
"""fig = px.bar(counts_2024, x="Ligne", y="Count", text="Count", text_auto=True,
             color_discrete_sequence=[coolors_palette["quaternary"]])
fig = stylize_figure(fig, "Lignes les plus ponctuelles depuis 2024")
fig.show(renderer="browser")"""

# Worst depuis 2024
worst_perf_2024 = valeur_sup_2024.groupby("Date")["Taux de ponctualité"].transform(min)
worst_perf_df_2024 = valeur_sup_2024[valeur_sup_2024["Taux de ponctualité"] == worst_perf_2024]
counts_worst_2024 = worst_perf_df_2024["Ligne"].value_counts().reset_index()
counts_worst_2024.columns = ["Ligne", "Count"]
"""fig = px.bar(counts_worst_2024, x="Ligne", y="Count", text="Count", text_auto=True,
             color_discrete_sequence=[coolors_palette["secondary"]])
fig = stylize_figure(fig, "Lignes les moins ponctuelles depuis 2024")
fig.show(renderer="browser")"""

# Lignes les plus performantes (H, K)
best_lignes = df[df["Ligne"].isin(["H", "K"])]
fig = px.line(best_lignes, x="Date", y="Taux de ponctualité", color="Ligne",
              hover_data={"Date": True, "Taux de ponctualité": True},
              color_discrete_map={
                  "H": coolors_palette["primary"],
                  "K": coolors_palette["tertiary"]
              })
fig.update_traces(line=dict(width=3, shape='spline'))

# Ajouter la médiane générale
fig.add_trace(go.Scatter(
    x=median_evolution["Date"],
    y=median_evolution["Mediane_Ponctualite"],
    mode='lines',
    name='Médiane générale',
    line=dict(width=2, dash='dash', color=coolors_palette["quinary"]),
    hovertemplate='<b>Médiane générale</b><br>Date: %{x}<br>Ponctualité: %{y:.2f}%<extra></extra>'
))

fig.update_yaxes(range=[30, 100])
fig = stylize_figure(fig, "Évolution du taux de ponctualité des lignes les plus performantes")
fig.show(renderer="browser")

# Lignes les moins performantes (A, B)
worst_lignes = df[df["Ligne"].isin(["A", "B"])]
fig = px.line(worst_lignes, x="Date", y="Taux de ponctualité", color="Ligne",
              hover_data={"Date": True, "Taux de ponctualité": True},
              color_discrete_map={
                  "A": coolors_palette["primary"],
                  "B": coolors_palette["tertiary"]
              })
fig.update_traces(line=dict(width=3, shape='spline'))

# Ajouter la médiane générale
fig.add_trace(go.Scatter(
    x=median_evolution["Date"],
    y=median_evolution["Mediane_Ponctualite"],
    mode='lines',
    name='Médiane générale',
    line=dict(width=2, dash='dash', color=coolors_palette["quinary"]),
    hovertemplate='<b>Médiane générale</b><br>Date: %{x}<br>Ponctualité: %{y:.2f}%<extra></extra>'
))

fig.update_yaxes(range=[0, 100])
fig = stylize_figure(fig, "Évolution du taux de ponctualité des lignes les moins performantes")
fig.show(renderer="browser")

# Lignes sélectionnées (H, K, A, B) avec seuil & annotations
selected_lignes = df[df["Ligne"].isin(["H", "K", "A", "B"])]
ligne_colors = {
    "H": coolors_palette["primary"],
    "K": coolors_palette["tertiary"],
    "A": coolors_palette["quaternary"],
    "B": coolors_palette["quinary"]
}
fig = px.line(selected_lignes, x="Date", y="Taux de ponctualité", color="Ligne",
                 hover_data={"Date": True, "Taux de ponctualité": True},
                 color_discrete_map=ligne_colors)
fig.update_yaxes(range=[40, 100])
fig.update_traces(line=dict(width=3, shape='spline'))

fig = stylize_figure(fig, "Évolution des performances des lignes H, K, A, B")
fig.show(renderer="browser")