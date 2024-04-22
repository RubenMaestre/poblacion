#modules/graph/grafica_inicio.py
import plotly.express as px
import numpy as np
import streamlit as st
from modules.cargar_df import cargar_df

# Cargar datos
df, df_continentes, df_ingresos = cargar_df()

def grafica_rango_years(df_continentes):
    if not df_continentes.empty:
        # Crear la figura utilizando Plotly Express
        fig = px.line(
            df_continentes,
            x='Year',  # Usa la columna 'Year' directamente para el eje x
            y='Population density',
            color='Entity',
            title='Evolución de la densidad de población por zona geográfica',
            labels={'Population density': 'Densidad de población (personas por km²)', 'Year': 'Año', 'Entity': 'Zona geográfica'}
        )
        def custom_format_tickvals(tickval):
                if tickval < 0:
                    return f"{abs(tickval)} a.C."
                else:
                    return f"{tickval} d.C."

                # Aplicar la función a los tickvals actuales del eje x
        tickvals = np.arange(df_continentes['Year'].min(), df_continentes['Year'].max() + 1, 1000)
        ticktext = [f"{abs(year)} a.C." if year < 0 else f"{year} d.C." for year in tickvals]

        # Actualizar los ticks del eje X para mostrar cada 1000 años con la inclinación deseada
        fig.update_xaxes(tickvals=tickvals, ticktext=ticktext, tickangle=45)

                # Mostrar la figura en Streamlit
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.write("No hay datos disponibles para mostrar.")