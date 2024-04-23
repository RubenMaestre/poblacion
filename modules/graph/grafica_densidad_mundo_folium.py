import folium
import pandas as pd
import numpy as np
import branca.colormap as cm

def plot_population_density_map_with_folium(df):
    df_2023 = df[df['Year'] == 2023].dropna(subset=['Population density'])
    df_2023 = df_2023[~df_2023['Code'].str.startswith('OWID')]
    
    # Calcula el logaritmo de la densidad de población para reducir el impacto de valores extremadamente altos
    df_2023['Log Population Density'] = np.log1p(df_2023['Population density'])

    # Define los límites de la escala de colores en función de los datos logarítmicos
    min_density_log = df_2023['Log Population Density'].min()
    max_density_log = df_2023['Log Population Density'].max()
    
    # Define una escala de colores con muchos pasos
    steps = 100  # Define el número de colores/pasos en la escala
    colormap = cm.linear.YlOrRd_09.scale(min_density_log, max_density_log).to_step(steps)
    colormap.caption = 'Log of Population Density'

    # Crea un mapa base
    m = folium.Map(location=[20, 0], tiles='cartodbpositron', zoom_start=2)
    
    # Añade la escala de colores al mapa
    m.add_child(colormap)

    # Añade un mapa coroplético al mapa base usando los datos logarítmicos
    folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json',
        name='choropleth',
        data=df_2023,
        columns=['Code', 'Log Population Density'],
        key_on='feature.id',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Log of Population Density',
        threshold_scale=colormap.colors,  # Usa la escala de colores con los pasos definidos
        reset=True
    ).add_to(m)

    # Añade la leyenda al mapa
    folium.LayerControl().add_to(m)

    return m

