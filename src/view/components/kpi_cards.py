import streamlit as st
from src.config.ui_config import PAGINAS
from src.utils.formatting import formatar_unidade, formatar_moeda, formatar_porcentagem

def aplicar_estilo_metricas(cores):
    st.markdown(f"""
    <style>
        .stMetric {{
            background-color: #ffffff;
            border-radius: 10px;
            padding: 12px;
            box-shadow: 0 0 5px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            color: #111827;
        }}

        .stMetric:hover {{
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}

        [data-testid="stColumn"]:nth-of-type(1) .stMetric {{
            border-left: 6px solid {cores.get("col1", "#000")};
        }}
        [data-testid="stColumn"]:nth-of-type(2) .stMetric {{
            border-left: 6px solid {cores.get("col2", "#000")};
        }}
        [data-testid="stColumn"]:nth-of-type(3) .stMetric {{
            border-left: 6px solid {cores.get("col3", "#000")};
        }}
        [data-testid="stColumn"]:nth-of-type(4) .stMetric {{
            border-left: 6px solid {cores.get("col4", "#000")};
        }}
    </style>
    """, unsafe_allow_html=True)


def exibir_kpis(dict_kpis):
    cols = st.columns(len(dict_kpis))
    for col, (label, valor) in zip(cols, dict_kpis.items()):
        with col:
            st.metric(label, valor)



def montar_dict_kpis_visao_geral(kpis):
    return {
        PAGINAS["visao_geral"]["labels_kpis"]["total"]: formatar_unidade(kpis["total"]),
        PAGINAS["visao_geral"]["labels_kpis"]["qualificados"]: formatar_unidade(kpis["qualificados"]),
        PAGINAS["visao_geral"]["labels_kpis"]["atendimento_ia"]: formatar_unidade(kpis["atendimento_ia"]),
        PAGINAS["visao_geral"]["labels_kpis"]["atendimento_consultor"]: formatar_unidade(kpis["atendimento_consultor"])
    }


def montar_dict_kpis_financeiro(kpis):
    return {
        PAGINAS["financeiro"]["labels_kpis"]["faturamento_total"]: formatar_moeda(kpis["faturamento_total"]),
        PAGINAS["financeiro"]["labels_kpis"]["ticket_medio"]: formatar_moeda(kpis["ticket_medio"]),
        PAGINAS["financeiro"]["labels_kpis"]["numero_vendas"]: formatar_unidade(kpis["numero_vendas"]),
        PAGINAS["financeiro"]["labels_kpis"]["porcentagem_a_vista"]: formatar_porcentagem(kpis["porcentagem_a_vista"])
    }