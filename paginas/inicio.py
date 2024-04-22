# paginas/inicio.py
import streamlit as st
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
from modules.cargar_df import cargar_df

def display():
    # Carga los DataFrames
    df, df_continentes = cargar_df()

    # Verificación de la carga correcta de los datos
    if df_continentes is None:
        st.error("Error al cargar los datos. Por favor, revisa los archivos de datos.")
        return

    # Imagen de cabecera (si decides volver a incluirla)
    # st.image('sources/cabecera.jpg', use_column_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)  # Espacio extra

    # Título de la página
    st.markdown("<h1 style='text-align: center;'>Estudio sobre la densidad de población mundial</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción descriptiva
    st.markdown("""
        <div style='text-align: justify;'>
            Bienvenidos a este proyecto sobre la evolución de la densidad de población humana en los continentes y países 
            a lo largo de los últimos 12,000 años. Este análisis permite observar las tendencias históricas en la 
            densidad de población y entender cómo han cambiado las dinámicas poblacionales a través tiempo. 
            A continuación, presentamos una visualización interactiva que muestra estos cambios a lo largo del tiempo.
        </div>
        """, unsafe_allow_html=True)

    # Crear y mostrar la gráfica de Plotly

    df_continentes['Year_Label'] = df_continentes['Year'].apply(
        lambda x: f"{abs(x)} a.C." if x < 0 else f"{x} d.C."
    )
    
    # Especificar manualmente los ticks que queremos en el eje x
    specified_years = [-10000, -5000, -2000, -1000, -500, -200, 0, 200, 500, 800, 
                       1000, 1200, 1400, 1600, 1800, 1850, 1900, 1950, 2000, 2020, 2050, 2100]
    
    # Asegurarse de que solo se usen los años que existen en el DataFrame
    tickvals = [year for year in specified_years if year in df_continentes['Year'].values]
    ticktext = [df_continentes[df_continentes['Year'] == year]['Year_Label'].iloc[0] for year in tickvals]

    # Crear la figura
    fig = go.Figure()

    # Añadir trazos para cada entidad
    for entity in df_continentes['Entity'].unique():
        df_entity = df_continentes[df_continentes['Entity'] == entity]
        fig.add_trace(go.Scatter(
            x=df_entity['Year_Label'],  # Se mantiene el uso de 'Year_Label' para el eje x
            y=df_entity['Population density'],
            mode='lines',
            name=entity
        ))

    # Actualizar los ticks del eje x
    fig.update_xaxes(tickvals=tickvals, ticktext=ticktext)

    # Configurar el layout de la figura
    fig.update_layout(
        title='Evolución de la densidad de población por zona geográfica',
        xaxis_title='Año',
        yaxis_title='Densidad de población (personas por km²)',
        legend_title='Zona geográfica',
        xaxis=dict(
            tickmode='array',
            type='linear',
            showgrid=True,
        )
    )

    # Mostrar la figura en Streamlit
    st.plotly_chart(fig, use_container_width=True)
