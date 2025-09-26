import streamlit as st

from src.data.db_connection import Sessionlocal
from src.data.db_init import criar_tabelas

from src.data.repositories.sales_repository import SalesRepository
from src.data.repositories.courses_repository import CoursesRepository

from src.services.courses_service import CoursesServices
from src.services.sales_services import SalesServices

from src.utils.date_utils import formatar_periodo

from src.view.components.filters_sidebar import exibir_filtros_financeiro
from src.view.components.kpi_cards import montar_dict_kpis_financeiro
from src.view.components.layout import exibir_pagina_financeiro


st.set_page_config(page_title="Gestão de Leads", page_icon="👥", layout="wide")


def inicializar_repositories(db):
    sales_repo = SalesRepository(db)
    courses_repo = CoursesRepository(db)
    return sales_repo, courses_repo


def inicializar_services(sales_repo, courses_repo):
    sales_service = SalesServices(sales_repo)
    courses_service = CoursesServices(courses_repo)
    return sales_service, courses_service


def carregar_entradas_filtros(
    sales_service: SalesServices,
    courses_service: CoursesServices
):
    cursos = courses_service.obter_cursos_unicos()
    intervalo_datas = sales_service.obter_intervalo_datas_vendas()
    return cursos, intervalo_datas


def aplicar_filtros(curso, intervalo_datas):
    saidas_filtros = exibir_filtros_financeiro(
        curso,
        intervalo_datas,
    )
    data_inicial, data_final = formatar_periodo(saidas_filtros["periodo"])
    return saidas_filtros["curso"], data_inicial, data_final


def main():
    criar_tabelas()
    with Sessionlocal() as db:
        sales_repo, courses_repo = inicializar_repositories(db)
        sales_service, courses_service = inicializar_services(
            sales_repo,
            courses_repo
        )
        curso, intervalo_datas = carregar_entradas_filtros(
            sales_service,
            courses_service
        )
        curso, data_inicial, data_final = aplicar_filtros(
            curso,
            intervalo_datas
        )

        df_vendas_filtrado = sales_service.obter_vendas_filtradas(
            curso,
            data_inicial,
            data_final
        )

        kpis = sales_service.calcular_kpis(df_vendas_filtrado)

        df_evolucao_diaria = sales_service.obter_evolucao_diaria(
            df_vendas_filtrado,
            data_inicial,
            data_final,
            "data_venda",
            limite=15
        )
        df_pagamentos = sales_service.obter_distribuicao(
            df_vendas_filtrado,
            "forma_pagamento"
        )
        df_consultores = sales_service.obter_distribuicao(
            df_vendas_filtrado,
            "responsavel_venda"
        )

    dict_kpis = montar_dict_kpis_financeiro(kpis)
    exibir_pagina_financeiro(
        df_evolucao_diaria,
        df_pagamentos,
        df_consultores,
        curso,
        dict_kpis
    )


if __name__ == "__main__":
    main()
