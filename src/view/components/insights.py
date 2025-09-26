import streamlit as st

def exibir_insight(icon, bg, border, texto):
    st.markdown(f"""
    <div style="
        background-color:{bg};
        border:1px solid {border};
        padding:16px 18px; border-radius:10px;
        font-size:15px; font-weight:500; color:#1F2937;">
        <span style="margin-right:8px; font-size:1.1em;">{icon}</span>
        {texto}
    </div>
    """, unsafe_allow_html=True)