import streamlit as st

from src.data.db_connection import Sessionlocal
from src.data.db_init import criar_tabelas

from src.data.repositories.clients_repository import ClientsRepository
from src.data.repositories.courses_repository import CoursesRepository
from src.data.repositories.messages_repository import MessagesRepository

from src.services.clients_service import ClientsServices
from src.services.courses_service import CoursesServices
from src.services.messages_service import MessageService

from src.utils.date_utils import formatar_periodo

from src.view.components.filters_sidebar import exibir_filtros_visao_geral
from src.view.components.kpi_cards import montar_dict_kpis_visao_geral
from src.view.components.layout import exibir_pagina_visao_geral


st.set_page_config(page_title="Gestão de Leads", page_icon="👥", layout="wide")


def inicializar_repositories(db):
    clients_repo = ClientsRepository(db)
    courses_repo = CoursesRepository(db)
    message_repo = MessagesRepository(db)
    return clients_repo, courses_repo, message_repo


def inicializar_services(clients_repo, courses_repo, message_repo):
    clients_service = ClientsServices(clients_repo)
    courses_service = CoursesServices(courses_repo)
    message_service = MessageService(message_repo)
    return clients_service, courses_service, message_service


def carregar_entradas_filtros(
    clients_service: ClientsServices,
    courses_service: CoursesServices
):
    cursos = courses_service.obter_cursos_unicos()
    intervalo_datas = clients_service.obter_intervalo_datas_clientes()
    cidade = clients_service.obter_cidades_unicas()
    return cursos, intervalo_datas, cidade


def aplicar_filtros(cursos, intervalo_datas, cidade):
    saidas_filtros = exibir_filtros_visao_geral(
        cursos,
        intervalo_datas,
        cidade
    )
    data_inicial, data_final = formatar_periodo(saidas_filtros["periodo"])
    return (
        saidas_filtros["curso"],
        data_inicial,
        data_final,
        saidas_filtros["cidade"]
    )


def main():
    criar_tabelas()
    with Sessionlocal() as db:
        clients_repo, courses_repo, message_repo = inicializar_repositories(db)
        clients_service, courses_service, message_service = inicializar_services(
            clients_repo,
            courses_repo,
            message_repo
        )

        curso, intervalo_datas, cidade = carregar_entradas_filtros(
            clients_service,
            courses_service
        )
        curso, data_inicial, data_final, cidade = aplicar_filtros(
            curso,
            intervalo_datas,
            cidade
        )

        df_clientes_filtrado = clients_service.obter_df_clientes_filtrado(
            curso,
            data_inicial,
            data_final,
            cidade
        )

        kpis = clients_service.calcular_kpis(df_clientes_filtrado)

        insight_perfil = clients_service.obter_insight(
            df_clientes_filtrado,
            "perfil_cliente"
        )
        insight_horario = message_service.obter_insight(
            curso,
            data_inicial,
            data_final,
            cidade,
            "Hora_cheia"
        )

        df_evolucao_diaria = clients_service.obter_evolucao_diaria(
            df_clientes_filtrado,
            data_inicial,
            data_final,
            "data_criacao",
            limite=15
        )
        df_distribuicao_perfil = clients_service.obter_distribuicao_por_perfil(
            df_clientes_filtrado,
            "perfil_cliente"
        )

    dict_kpis = montar_dict_kpis_visao_geral(kpis)
    exibir_pagina_visao_geral(
        df_evolucao_diaria,
        df_distribuicao_perfil,
        curso,
        dict_kpis,
        insight_perfil,
        insight_horario
    )


if __name__ == "__main__":
    main()