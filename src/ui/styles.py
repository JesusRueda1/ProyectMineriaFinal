import streamlit as st

def apply_custom_styles():
    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@300;500;700;800&display=swap');

    /* --- RESET GLOBAL --- */
    html, body, [class*="css"] {
        font-family: 'Manrope', sans-serif;
        background-color: #fcfcfc;
        color: #1e1e1e;
    }
    .stApp { background-color: #fcfcfc; }

    /* --- SIDEBAR --- */
    [data-testid="stSidebar"] {
        background-color: #ffffff; 
        border-right: 1px solid #e5e5e5;
    }

    /* --- CARDS / TARJETAS --- */
    div.stContainer {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #f0f0f0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.02);
    }

    /* --- BOTONES UNIFICADOS --- */
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        background-color: #1e1e1e;
        color: white;
        border: none;
        height: 45px;
        transition: 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton > button:hover {
        background-color: #333;
        transform: translateY(-2px);
    }

    /* --- MENÚ LATERAL (Hack para ocultar radio buttons) --- */
    [data-testid="stRadio"] > div[role="radiogroup"] > label > div:first-child { display: none; }
    
    [data-testid="stRadio"] > div[role="radiogroup"] > label {
        padding: 12px 15px;
        border-radius: 8px;
        color: #555 !important;
        transition: all 0.2s;
        cursor: pointer;
        display: flex;
        align-items: center;
    }
    [data-testid="stRadio"] > div[role="radiogroup"] > label:hover {
        background-color: #f3f4f6;
        color: #000 !important;
    }

    /* --- ICONOS DEL MENÚ (CSS PURO) --- */
    /* 1. INICIO */
    [data-testid="stRadio"] label:nth-child(1)::before { 
        content: "\\f015"; 
        font-family: "Font Awesome 6 Free"; 
        font-weight: 900;
        margin-right: 12px; 
        width: 20px; 
        text-align: center; 
    }
    
    /* 2. DASHBOARD */
    [data-testid="stRadio"] label:nth-child(2)::before { 
        content: "\\f201"; 
        font-family: "Font Awesome 6 Free"; 
        font-weight: 900;
        margin-right: 12px; 
        width: 20px; 
        text-align: center; 
    }
    
    /* 3. PREDICCIÓN */
    [data-testid="stRadio"] label:nth-child(3)::before { 
        content: "\\f0eb"; 
        font-family: "Font Awesome 6 Free"; 
        font-weight: 900;
        margin-right: 12px; 
        width: 20px; 
        text-align: center; 
    }

    /* Ocultar pie de página default */
    footer {visibility: hidden;}
    
    </style>
    """, unsafe_allow_html=True)