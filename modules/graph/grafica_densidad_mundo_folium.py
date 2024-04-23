import folium
import pandas as pd
import numpy as np
import branca.colormap as cm

def plot_population_density_map_with_folium(df, width=1200, height=500):
    df_2023 = df[df['Year'] == 2023].dropna(subset=['Population density'])
    df_2023 = df_2023[~df_2023['Code'].str.startswith('OWID')]
    df_2023['Log Population Density'] = np.log1p(df_2023['Population density'])

    min_density_log = df_2023['Log Population Density'].min()
    max_density_log = df_2023['Log Population Density'].max()

    steps = 100
    threshold_scale = np.linspace(min_density_log, max_density_log, steps).tolist()

    # Crea una escala de colores lineal
    colormap = cm.linear.YlOrRd_09.scale(min_density_log, max_density_log).to_step(steps)
    colormap.caption = 'Log of Population Density'  # Título de la escala de colores

    # Crea un mapa base
    m = folium.Map(location=[20, 0], tiles='cartodbpositron', zoom_start=2, width=width, height=height)
    
    # Crea y añade el mapa coroplético al mapa base
    choropleth = folium.Choropleth(
        geo_data='https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json',
        data=df_2023,
        columns=['Code', 'Log Population Density'],
        key_on='feature.id',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        threshold_scale=threshold_scale,  # Usa la escala de umbrales creada
        reset=True
    ).add_to(m)
    
    # Agrega la escala de colores personalizada al mapa
    m.add_child(colormap)

    # Añade el control de capas al mapa
    folium.LayerControl().add_to(m)

    return m

