import pandas as pd
import streamlit as st

@st.cache_data
def load_dataset(file):
    """Carga resiliente de datos (Detecta separadores y limpia números)."""
    try:
        df = pd.read_csv(file)
        if len(df.columns) < 2:
            file.seek(0)
            df = pd.read_csv(file, sep=';')
    except:
        file.seek(0)
        df = pd.read_csv(file, sep=';')
    
    df = df.drop_duplicates()
    
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                clean = df[col].astype(str).str.replace('$', '', regex=False).str.replace('.', '', regex=False).str.replace(',', '.', regex=False).str.strip()
                df[col] = pd.to_numeric(clean)
            except: pass
    return df