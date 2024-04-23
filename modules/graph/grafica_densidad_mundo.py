import plotly.express as px
import pandas as pd
import numpy as np

def plot_population_density_map_with_plotly(df):
    df_2024 = df[df['Year'] == 2024].dropna(subset=['Population density'])
    df_2024 = df_2024[~df_2024['Code'].str.startswith('OWID')]
    
    # Agregar una nueva columna con el logaritmo de la densidad de población
    df_2024['Log Population Density'] = np.log1p(df_2024['Population density'])  # log1p para manejar el logaritmo de 0
    
    # Normalizar la densidad logarítmica de 0 a 100
    max_log_density = df_2024['Log Population Density'].max()
    min_log_density = df_2024['Log Population Density'].min()
    df_2024['Normalized Log Density'] = 100 * (df_2024['Log Population Density'] - min_log_density) / (max_log_density - min_log_density)

    # Crear el mapa coroplético con Plotly Express
    fig = px.choropleth(
        df_2024,
        locations="Code",  # Columna con los códigos de país ISO
        color="Normalized Log Density",  # Columna que define el color de la choropleth
        hover_name="Entity",  # Asumiendo que 'Entity' es la columna con los nombres de los países
        hover_data={"Population density": ":.2f",  # Mostrar la densidad real con 2 decimales
                    "Normalized Log Density": False},  # Ocultar la densidad logarítmica normalizada en el tooltip
        color_continuous_scale=['white', 'red'],  # Escala de color de blanco a rojo
        projection="natural earth",  # Proyección del mapa
    )

    fig.update_layout(
        title_text='Densidad de población por país en 2024',
        title_x=0.5,  # Centrar el título
        geo=dict(
            showframe=False,  # Ocultar el marco del mapa
            showcoastlines=False,  # Ocultar las líneas costeras
        ),
        width=1200,  # Ancho del mapa
        height=600   # Altura del mapa
    )

    # Ajustar la leyenda para que muestre "Índice de Densidad de Población"
    fig.update_coloraxes(colorbar_title="Índice de densidad de población")

    return fig

