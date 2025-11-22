import streamlit as st
from src.ui.styles import apply_custom_styles
from src.ui.views.home import render_home
from src.ui.views.dashboard import render_dashboard
from src.ui.views.prediction import render_prediction

# 1. Config
st.set_page_config(page_title="ANALYTIC", layout="wide", initial_sidebar_state="expanded")

# 2. Estilos
apply_custom_styles()

# 3. Estado Global
if 'df' not in st.session_state: st.session_state.df = None
if 'model' not in st.session_state: st.session_state.model = None
if 'metrics' not in st.session_state: st.session_state.metrics = None

# 4. Menú Lateral
with st.sidebar:
    st.markdown("<h3 style='margin-left:10px; font-weight:800;'>ANALYTIC.</h3>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="display:flex; align-items:center; padding:10px; background:#f9f9f9; border-radius:10px; margin-bottom:20px;">
        <div style="width:35px; height:35px; background:#1e1e1e; border-radius:50%; color:white; display:flex; align-items:center; justify-content:center; margin-right:10px; font-size:14px;">
            <i class="fa-solid fa-user-graduate"></i>
        </div>
        <div>
            <div style="font-size:13px; font-weight:bold;">Admin</div>
            <div style="font-size:10px; color:#888;">Pro Workspace</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    opcion = st.radio("Nav", ["INICIO", "DASHBOARD", "PREDICCIÓN"], label_visibility="collapsed")
    
    st.markdown("<div style='flex-grow:1'></div>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("Salir"): st.toast("Cerrando...")

# 5. Router
if opcion == "INICIO": render_home()
elif opcion == "DASHBOARD": render_dashboard()
elif opcion == "PREDICCIÓN": render_prediction()