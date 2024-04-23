import plotly.express as px
import pandas as pd
import numpy as np

def plot_population_density_map_with_plotly(df):
    df_2024 = df[df['Year'] == 2024].dropna(subset=['Population density'])
    df_2024 = df_2024[~df_2024['Code'].str.startswith('OWID')]
    
    df_2024['Log Population Density'] = np.log1p(df_2024['Population density'])
    max_log_density = df_2024['Log Population Density'].max()
    min_log_density = df_2024['Log Population Density'].min()
    df_2024['Normalized Log Density'] = 100 * (df_2024['Log Population Density'] - min_log_density) / (max_log_density - min_log_density)

    # Crear el mapa coroplético con Plotly Express
    fig = px.choropleth(
        df_2024,
        locations="Code",
        color="Normalized Log Density",
        hover_name="Entity",
        hover_data={"Population density": ":.2f", "Normalized Log Density": False},
        color_continuous_scale=['white', 'red'],
        projection="natural earth",
    )

    fig.update_layout(
        title_text='Densidad de población por país en 2024',
        title_x=0.5,
        geo=dict(showframe=False, showcoastlines=False),
        width=1200,
        height=600
    )

    # Configuración manual de la leyenda para usar valores de densidad reales
    max_density = df_2024['Population density'].max()
    step_values = np.exp(np.linspace(np.log1p(min_density_log), np.log1p(max_density), 6)) - 1  # Usamos log-scale para determinar los puntos medios
    step_labels = [f"{v:.2f}" for v in step_values]

    fig.update_coloraxes(colorbar=dict(
        title="Densidad de Población",
        tickvals=np.linspace(0, 100, 6),
        ticktext=step_labels
    ))

    return fig
