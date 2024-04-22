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
    df_continentes['Year_Label'] = df_continentes['Year'].apply(lambda x: f"{abs(x)} a.C." if x < 0 else f"{x} d.C.")

    if df_continentes is not None:
        # Configuración de las marcas para el eje X
        x_ticks = {year: f"{abs(year)} a.C." if year < 0 else f"{year} d.C." for year in range(-10000, 2021, 1000)}
        x_ticks.update({year: f"{year} d.C." for year in range(0, 2021, 50)})

        fig = px.line(df_continentes, x='Year_Label', y='Population density', color='Entity', 
                      title='Evolución de la densidad de población por zona geográfica',
                      labels={
                          'Population density': 'Densidad de población (personas por km²)',
                          'Year_Label': 'Año',
                          'Entity': 'Zona geográfica'
                      })

        # Actualizar marcas en el eje X
        fig.update_xaxes(tickvals=list(x_ticks.keys()), ticktext=list(x_ticks.values()))

        # Usar esta función para integrar la gráfica en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
