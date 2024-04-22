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

    # Definir ticks para el eje x que sean uniformes a lo largo de la escala de tiempo
    # Desde el año más antiguo hasta el más reciente, en intervalos de 100 años
    tickvals = np.arange(df_continentes['Year'].min(), df_continentes['Year'].max() + 1, 100)
    ticktext = [f"{abs(year)} a.C." if year < 0 else f"{year} d.C." for year in tickvals]

    # Crear la figura
    fig = go.Figure()

    # Añadir trazos para cada entidad
    for entity in df_continentes['Entity'].unique():
        df_entity = df_continentes[df_continentes['Entity'] == entity]
        fig.add_trace(go.Scatter(
            x=df_entity['Year'],  # Usar la columna 'Year' directamente para un mapeo correcto en el eje x
            y=df_entity['Population density'],
            mode='lines',
            name=entity
        ))

    # Actualizar los ticks del eje X para mostrar cada 100 años y asegurar que se extienden a lo largo de todo el eje
    fig.update_xaxes(tickvals=tickvals, ticktext=ticktext)

    # Configurar el layout de la figura para que incluya todos los años
    fig.update_layout(
        title='Evolución de la densidad de población por zona geográfica',
        xaxis_title='Año',
        yaxis_title='Densidad de población (personas por km²)',
        legend_title='Zona geográfica',
        xaxis=dict(
            tickmode='array',
            type='linear',
            showgrid=True,  # Puede activar o desactivar la cuadrícula para mayor claridad
        )
    )

    # Mostrar la figura en Streamlit
    st.plotly_chart(fig, use_container_width=True)