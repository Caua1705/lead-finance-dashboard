import streamlit as st


def exibir_filtros_visao_geral(cursos, intervalo_datas, cidades):
    st.sidebar.markdown("## Filtros - Visão Geral")
    
    curso = st.sidebar.selectbox("🎓 Curso", ["Todos"] + cursos)
    
    periodo = st.sidebar.date_input(
        "📅 Período", 
        (intervalo_datas["data_minima"], intervalo_datas["data_maxima"]),
        min_value=intervalo_datas["data_minima"],
        max_value=intervalo_datas["data_maxima"],
        format="DD/MM/YYYY"
    )
    
    cidade = st.sidebar.selectbox("📍 Cidade", ["Todas"] + cidades)

    filtros = {
        "curso": curso,
        "periodo": periodo,
        "cidade": cidade
    }
    
    return filtros


def exibir_filtros_mensagens(cursos, intervalo_datas, etapas_atendimento):
    st.sidebar.markdown("## Filtros - Mensagens")
    
    curso = st.sidebar.selectbox("🎓 Curso", cursos)
    
    periodo = st.sidebar.date_input(
        "📅 Período", 
        (intervalo_datas["data_minima"], intervalo_datas["data_maxima"]),
        min_value=intervalo_datas["data_minima"],
        max_value=intervalo_datas["data_maxima"],
        format="DD/MM/YYYY"
    )
    
    etapa_atendimento = st.sidebar.selectbox("🎯 Etapa de Atendimento", etapas_atendimento)

    filtros = {
        "curso": curso,
        "periodo": periodo,
        "etapa_atendimento": etapa_atendimento
    }
    
    return filtros


def exibir_filtros_financeiro(cursos, intervalo_datas):
    st.sidebar.markdown("## Filtros - Financeiro")
    curso = st.sidebar.selectbox("🎓 Curso", ["Todos"] + cursos)
    periodo = st.sidebar.date_input(
        "📅 Período", 
        (intervalo_datas["data_minima"], intervalo_datas["data_maxima"]),
        min_value=intervalo_datas["data_minima"],
        max_value=intervalo_datas["data_maxima"],
        format="DD/MM/YYYY"
    )
    filtros = {
        "curso": curso,
        "periodo": periodo
    }
    return filtros