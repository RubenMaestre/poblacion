import plotly.express as px
import pandas as pd

def plot_population_density_map_with_plotly(df):
    df_2024 = df[df['Year'] == 2024].dropna(subset=['Population density'])
    df_2024 = df_2024[~df_2024['Code'].str.startswith('OWID')]
    
    # Crear el mapa coroplético con Plotly Express
    fig = px.choropleth(
        df_2024,
        locations="Code",  # Columna con los códigos de país ISO
        color="Population density",  # Usamos la columna de densidad de población real
        hover_name="Entity",  # Asumiendo que 'Entity' es la columna con los nombres de los países
        hover_data={"Population density": ":.2f"},  # Mostrar la densidad real con 2 decimales
        color_continuous_scale=['white', 'red'],  # Escala de color de blanco a rojo
        projection="natural earth",  # Proyección del mapa
        range_color=[0, 10],  # Rango de colores para la leyenda de 0 a 10
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

    # Ajustar la leyenda para que muestre "Índice de densidad de población"
    fig.update_coloraxes(colorbar_title="Índice de densidad de población")

    return fig
