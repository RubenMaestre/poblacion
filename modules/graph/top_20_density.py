import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def plot_top_20_density(df):
    # Filtrar el DataFrame para el año deseado y calcular el top 20 en densidad
    df_year = df[df['Year'] == 2024]
    top_20 = df_year.nlargest(20, 'Population density')

    # Crear la figura
    fig = go.Figure()

    # Añadir burbujas para los top 20 países en densidad
    for i, row in top_20.iterrows():
        # Tamaño del círculo en función de la densidad de población
        size = row['Population density']
        fig.add_trace(go.Scatter(
            x=[row['Entity']],  # Nombre del país
            y=[size],           # Usar la densidad como la coordenada y para la dispersión vertical
            marker=dict(
                size=size,      # El tamaño del marcador es proporcional a la densidad
                sizemode='area',  # El tamaño del marcador representa el área (densidad de población)
                sizeref=2.*max(df_year['Population density'])/(40.**2),  # Ajuste para el tamaño de referencia
            ),
            mode='markers',
            name=row['Entity']
        ))

    # Actualizar el layout para mejor visualización
    fig.update_layout(
        title='Top 20 países por densidad de población en 2024',
        xaxis=dict(showticklabels=True),
        yaxis=dict(showticklabels=False),
        showlegend=False
    )

    # Ajustar la configuración de los ejes para mejor visualización
    fig.update_xaxes(tickangle=45)

    # Mostrar la figura en Streamlit
    st.plotly_chart(fig, use_container_width=True)
