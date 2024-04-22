# paginas/inicio.py
import streamlit as st
import plotly.express as px
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
    
    # Define los ticks personalizados basándose en los años disponibles en el DataFrame
    custom_x_ticks = [-10000, -5000, -2000, -1000, -500, -100, 0, 100, 300, 500, 800, 1000, 1200, 
                      1400, 1600, 1800, 1900, 1950, 1980, 2000, 2010, 2020, 2050, 2100]
    custom_x_labels = [f"{abs(year)} a.C." if year < 0 else f"{year} d.C." for year in custom_x_ticks]
    
    # Inicializar la figura de Plotly con objeto Graph
    fig = go.Figure()

    # Añadir trazas para cada entidad
    for entity in df_continentes['Entity'].unique():
        df_entity = df_continentes[df_continentes['Entity'] == entity]
        fig.add_trace(go.Scatter(x=df_entity['Year_Label'], y=df_entity['Population density'],
                                 mode='lines', name=entity))

    # Actualizar los ticks del eje x para que se correspondan con los años personalizados
    fig.update_xaxes(tickvals=custom_x_ticks, ticktext=custom_x_labels)

    # Actualizar título y etiquetas
    fig.update_layout(
        title='Evolución de la densidad de población por zona geográfica',
        xaxis_title='Año',
        yaxis_title='Densidad de población (personas por km²)',
        legend_title='Zona geográfica'
    )
    
    # Integrar la gráfica en Streamlit
    st.plotly_chart(fig, use_container_width=True)