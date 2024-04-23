import plotly.express as px
import pandas as pd

def plot_population_density_map_with_plotly(df):
    df_2023 = df[df['Year'] == 2023].dropna(subset=['Population density'])
    df_2023 = df_2023[~df_2023['Code'].str.startswith('OWID')]

    # Crear el mapa coroplético con Plotly Express
    fig = px.choropleth(
        df_2023,
        locations="Code",  # Columna con los códigos de país ISO
        color="Population density",  # Columna que define el color de la choropleth
        hover_name="Code",  # Columna para mostrar en el tooltip
        color_continuous_scale=px.colors.sequential.Plasma,  # Escala de color
        projection="natural earth",  # Proyección del mapa
    )

    fig.update_coloraxes(colorscale="Plasma", colorbar_title="Log Density",
                         type='log')  # Aplicar escala logarítmica

    fig.update_layout(
        title_text='Densidad de Población por País en 2023',
        title_x=0.5,  # Centrar el título
        geo=dict(
            showframe=False,  # Ocultar el marco del mapa
            showcoastlines=False,  # Ocultar las líneas costeras
        )
    )

    return fig
