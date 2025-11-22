import streamlit as st
import pandas as pd
from src.services.ai_model import train_linear_model

def render_prediction():
    st.title("Predicción (ML)")
    
    if st.session_state.df is None:
        st.warning("Carga datos primero.")
        return
    
    df = st.session_state.df
    nums = df.select_dtypes(include=['number']).columns.tolist()
    
    if len(nums) < 2:
        st.error("Insuficientes columnas numéricas.")
        return

    c_conf, c_res = st.columns([1, 2])

    with c_conf:
        with st.container():
            st.subheader("Configuración")
            target = st.selectbox("Objetivo (Y)", nums)
            feats = st.multiselect("Variables (X)", [c for c in df.columns if c != target], default=[c for c in nums if c!=target][0])
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("🧠 Entrenar"):
                if feats:
                    try:
                        model, metrics = train_linear_model(df, target, feats)
                        st.session_state.model = model
                        st.session_state.metrics = metrics
                        st.success("Listo.")
                    except Exception as e: st.error(f"Error: {e}")

    with c_res:
        if st.session_state.model:
            with st.container():
                m = st.session_state.metrics
                c1, c2 = st.columns(2)
                c1.metric("Precisión (R²)", f"{m['r2']:.2%}")
                c2.metric("Error (MSE)", f"{m['mse']:.2f}")
                
                st.markdown("---")
                st.subheader("Simulador")
                inputs = {}
                cc = st.columns(2)
                for i, f in enumerate(feats):
                    with cc[i%2]:
                        if f in df.select_dtypes(include=['number']).columns:
                            inputs[f] = st.number_input(f, value=float(df[f].mean()))
                        else:
                            inputs[f] = st.selectbox(f, df[f].unique())
                
                st.markdown("<br>", unsafe_allow_html=True)
                if st.button("🔮 Predecir"):
                    res = st.session_state.model.predict(pd.DataFrame([inputs]))
                    st.markdown(f"<h1 style='text-align:center; font-size:50px;'>{res[0]:,.2f}</h1>", unsafe_allow_html=True)