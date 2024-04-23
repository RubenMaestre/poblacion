import folium
import pandas as pd
import numpy as np
import branca.colormap as cm

def plot_population_density_map_with_folium(df, width=1200, height=500):
    df_2023 = df[df['Year'] == 2023].dropna(subset=['Population density'])
    df_2023 = df_2023[~df_2023['Code'].str.startswith('OWID')]
    
    # Utiliza los valores reales de densidad de población
    min_density = df_2023['Population density'].min()
    max_density = df_2023['Population density'].max()

    # Define el número de pasos en la escala de colores
    steps = 100

    # Crea una escala de colores lineal
    colormap = cm.linear.YlOrRd_09.scale(min_density, max_density).to_step(steps)
    colormap.caption = 'Population Density'

    # Crea un mapa base
    m = folium.Map(location=[20, 0], tiles='cartodbpositron', zoom_start=2, width=width, height=height)

    # Crea y añade el mapa coroplético al mapa base
    folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json',
        data=df_2023,
        columns=['Code', 'Population density'],
        key_on='feature.id',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        threshold_scale=colormap.colors,  # Usa la escala de colores creada
        reset=True
    ).add_to(m)

    # Añade la escala de colores al mapa
    m.add_child(colormap)

    # Añade el control de capas al mapa
    folium.LayerControl().add_to(m)

    return m

