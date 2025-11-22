import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from src.services.data_loader import load_dataset
from src.utils.constants import PLOT_HEIGHT, TEMPLATE

def render_dashboard():
    st.title("Panel de Control")
    
    uploaded = st.file_uploader("Subir CSV", type="csv", label_visibility="collapsed")
    if uploaded:
        try:
            st.session_state.df = load_dataset(uploaded)
        except Exception as e: st.error(f"Error: {e}")

    if st.session_state.df is not None:
        df = st.session_state.df
        nums = df.select_dtypes(include=np.number).columns.tolist()
        cats = df.select_dtypes(include='object').columns.tolist()
        
        eje_x = cats[0] if cats else df.columns[0]
        eje_y = nums[0] if nums else None
        
        if not eje_y:
            st.warning("Faltan datos numéricos.")
            return

        st.markdown("---")
        t1, t2, t3 = st.tabs(["⚡ KPIs", "📄 Datos", "🔥 Mapa de Calor"])
        
        with t1:
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Filas", f"{df.shape[0]:,}")
            c2.metric(f"Total {eje_y}", f"{df[eje_y].sum():,.0f}")
            c3.metric(f"Promedio", f"{df[eje_y].mean():,.0f}")
            c4.metric("Calidad", "Limpieza OK")
        
        with t2:
            st.dataframe(df.head(10), use_container_width=True)
            
        with t3:
            if len(nums) > 1:
                fig_corr, ax = plt.subplots(figsize=(8, 3))
                sns.heatmap(df[nums].corr(), annot=True, cmap="Greys", ax=ax, fmt=".1f")
                st.pyplot(fig_corr)
            else: st.info("Se requieren +2 columnas numéricas.")

        st.markdown("---")
        
        # Gráficos
        df_agg = df.groupby(eje_x, as_index=False)[eje_y].sum().sort_values(by=eje_y, ascending=False).head(8)
        layout = dict(height=PLOT_HEIGHT, margin=dict(l=20,r=20,t=40,b=20), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='#333'))

        c1, c2 = st.columns(2)
        with c1:
            with st.container():
                st.caption(f"Comparativa: {eje_x}")
                fig = px.bar(df_agg, x=eje_x, y=eje_y, template=TEMPLATE, color_discrete_sequence=['#1e1e1e'])
                fig.update_layout(**layout)
                st.plotly_chart(fig, use_container_width=True)
        with c2:
            with st.container():
                st.caption("Tendencia")
                fig = px.area(df.head(50), x=eje_x, y=eje_y, template=TEMPLATE)
                fig.update_traces(line_color="#1e1e1e", fillcolor="rgba(0,0,0,0.1)")
                fig.update_layout(**layout)
                st.plotly_chart(fig, use_container_width=True)
        
        c3, c4 = st.columns(2)
        with c3:
            with st.container():
                st.caption("Distribución")
                fig = px.pie(df_agg, names=eje_x, values=eje_y, hole=0.6, template=TEMPLATE, color_discrete_sequence=px.colors.sequential.Greys)
                fig.update_layout(**layout)
                st.plotly_chart(fig, use_container_width=True)
        with c4:
            with st.container():
                st.caption("Boxplot")
                fig = px.box(df, x=eje_x, y=eje_y, template=TEMPLATE, color_discrete_sequence=['#1e1e1e'])
                fig.update_layout(**layout)
                st.plotly_chart(fig, use_container_width=True)