# cargar_df_pob.py
import pandas as pd

def cargar_df_pob():
    """Carga los DataFrames desde archivos Parquet y los devuelve."""
    try:
        df_paises_pob = pd.read_parquet('data/df_paises_pob.parquet')
        df_continentes_pob = pd.read_parquet('data/df_continentes_pob.parquet')
        df_sociedad_pob = pd.read_parquet('data/df_sociedad_pob.parquet')
        df_mundo_pob = pd.read_parquet('data/df_mundo_pob.parquet')
        return df_paises_pob, df_continentes_pob, df_sociedad_pob, df_mundo_pob
    except Exception as e:
        print(f"Error al cargar los DataFrames: {e}")
        return None, None, None, None
