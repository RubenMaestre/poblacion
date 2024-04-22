# paginas/inicio.py
import streamlit as st
import plotly.express as px
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
    st.markdown("<h1 style='text-align: center;'>Estudio sobre la población mundial</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    # Introducción descriptiva
    st.markdown("""
        <div style='text-align: justify;'>
            Bienvenidos a la página dedicada al estudio de la evolución de la población humana en los continentes y países 
            a lo largo de los últimos 12,000 años. Este análisis permite observar las tendencias históricas en la 
            densidad de población y entender cómo han cambiado las dinámicas poblacionales a través de las eras. 
            A continuación, presentamos una visualización interactiva que muestra estos cambios a lo largo del tiempo.
        </div>
        """, unsafe_allow_html=True)

    # Crear y mostrar la gráfica de Plotly
    if df_continentes is not None:
        fig = px.line(df_continentes, x='Year', y='Population density', color='Entity', 
                      title='Evolución de la Densidad de Población por Zona Geográfica',
                      labels={'Population density': 'Densidad de Población (personas por km²)', 'Year': 'Año'})
        st.plotly_chart(fig, use_container_width=True)  # Usar esta función para integrar la gráfica en Streamlit

    st.markdown("<br><br>", unsafe_allow_html=True)  # Espacio al final de la página
