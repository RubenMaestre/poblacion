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

    # Define el número de pasos en la escala de colores
    steps = 100

    # Crea una escala de colores lineal
    colormap = cm.linear.YlOrRd_09.scale(min_density_log, max_density_log)
    
    # Crea una lista de umbrales utilizando el número de pasos definido
    threshold_scale = np.linspace(min_density_log, max_density_log, steps).tolist()

    # Crea un mapa base
    m = folium.Map(location=[20, 0], tiles='cartodbpositron', zoom_start=2)
    
    # Añade la escala de colores al mapa
    colormap.add_to(m)

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
        threshold_scale=threshold_scale,  # Usa la escala de umbrales creada
        reset=True
    ).add_to(m)

    # Añade la leyenda al mapa
    folium.LayerControl().add_to(m)

    return m

