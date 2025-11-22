import streamlit as st

def render_home():
    st.markdown("""
    <div style="text-align: center; padding: 100px 20px;">
        <h1 style="font-size: 80px; color: #1e1e1e; letter-spacing: -3px; margin-bottom: 0px; line-height:1;">ANALYTIC.</h1>
        <p style="font-size: 20px; color: #888;">Plataforma Profesional de Datos.</p>
        <br>
        <div style="background: #1e1e1e; color: white; display: inline-block; padding: 12px 30px; border-radius: 30px; font-size: 14px; font-weight: 600;">
            Versión Final 4.0
        </div>
    </div>
    """, unsafe_allow_html=True)