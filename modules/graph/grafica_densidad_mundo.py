import plotly.express as px
import pandas as pd
import numpy as np

def plot_population_density_map_with_plotly(df):
    df_2023 = df[df['Year'] == 2023].dropna(subset=['Population density'])
    df_2023 = df_2023[~df_2023['Code'].str.startswith('OWID')]

    # Usaremos los valores reales de densidad de población para el color
    # Creamos una escala de colores que va de blanco (menor densidad) a rojo (mayor densidad)
    color_scale = [(0, 'white'), (1, 'red')]

    # Crear el mapa coroplético con Plotly Express
    fig = px.choropleth(
        df_2023,
        locations="Code",  # Columna con los códigos de país ISO
        color="Population density",  # Usamos la columna de densidad de población original
        hover_name="Code",  # Columna para mostrar en el tooltip
        color_continuous_scale=color_scale,  # Escala de color de blanco a rojo
        projection="natural earth",  # Proyección del mapa
    )

    # Actualiza el layout para establecer un tamaño específico del mapa
    fig.update_layout(
        title_text='Densidad de Población por País en 2023',
        title_x=0.5,  # Centrar el título
        geo=dict(
            showframe=False,  # Ocultar el marco del mapa
            showcoastlines=False,  # Ocultar las líneas costeras
        ),
        # Aquí establecemos el ancho (width) y alto (height) del mapa
        width=1200,  # Ajusta según tus necesidades
        height=600   # Ajusta según tus necesidades
    )

    return fig
