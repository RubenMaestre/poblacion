#modules/graph/grafica_inicio.py
import plotly.graph_objects as go
import streamlit as st
from modules.cargar_df import cargar_df

# Cargar datos
df, df_continentes, df_ingresos = cargar_df()

def grafica_simple(df_continentes):
    if not df_continentes.empty:
        # Convertir los años en etiquetas de texto
        df_continentes['Year_Label'] = df_continentes['Year'].apply(
            lambda x: f"{abs(x)} a.C." if x < 0 else f"{x} d.C."
        )

        # Ordenar el DataFrame por 'Year' para asegurarse de que la gráfica se renderice correctamente
        df_continentes.sort_values(by='Year', inplace=True)
        
        # Crear la figura
        fig = go.Figure()

        # Añadir trazos para cada entidad
        for entity in df_continentes['Entity'].unique():
            df_entity = df_continentes[df_continentes['Entity'] == entity]
            if not df_entity.empty:
                fig.add_trace(go.Scatter(
                    x=df_entity['Year_Label'],  # Se mantiene el uso de 'Year_Label' para el eje x
                    y=df_entity['Population density'],
                    mode='lines',
                    name=entity
                ))

        # Configurar el layout de la figura
        fig.update_layout(
            title='Evolución de la densidad de población por zona geográfica',
            xaxis_title='Año',
            yaxis_title='Densidad de población (personas por km²)',
            legend_title='Zona geográfica',
            xaxis=dict(
                type='linear',  # Configuración básica del eje X
                showgrid=True,
            )
        )

        # Mostrar la figura en Streamlit
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No hay datos disponibles para mostrar.")