import streamlit as st
from src.view.components.kpi_cards import aplicar_estilo_metricas, exibir_kpis
from src.view.components.insights import exibir_insight
from src.view.components.graphs import grafico_distribuicao_pizza, grafico_distribuicao_barra, grafico_evolucao_diaria
from src.utils.formatting import formatar_porcentagem
from src.utils.style import linha_divisoria,espaco_extra
from src.config.ui_config import PAGINAS

def exibir_header_pagina(titulo, curso, dict_kpis, dict_cores_kpis, financeiro):
    aplicar_estilo_metricas(dict_cores_kpis)
    st.title(f"{titulo} - {curso}")
    exibir_kpis(dict_kpis)
    if financeiro==False:
        linha_divisoria()
        espaco_extra()


def exibir_pagina_visao_geral(
    df_evolucao_diaria, df_por_perfil,curso, 
    dict_kpis, insight_perfil, insight_horario
):
    config = PAGINAS["visao_geral"]

    exibir_header_pagina(config["titulo"], curso, dict_kpis, config["cores_metricas"], financeiro=False)

    col1, col2 = st.columns(2)
    with col1:
        conf_horario = config["insights"]["horario"]

        exibir_insight(
            conf_horario["icone"],
            conf_horario["bg"],
            conf_horario["border"],
            f"O <b>pico de mensagens</b> ocorre por volta das "
            f"<b>{insight_horario["Nome"]}h</b>, "
            f"concentrando <b>{formatar_porcentagem(insight_horario["Porcentagem"])}</b> do total."
        )
        
        st.markdown(config["graficos"]["evolucao"]["titulo"])
        grafico_evolucao_diaria(
            df_evolucao_diaria,
            "data_criacao",
            "count",
            config["graficos"]["evolucao"]["cor_linha"],
            config["graficos"]["evolucao"]["titulo_grafico"],
            config["graficos"]["evolucao"]["titulo_x"],
            config["graficos"]["evolucao"]["titulo_y"],
        )

    with col2:
        conf_perfil = config["insights"]["perfil"]

        exibir_insight(
            conf_perfil["icone"],
            conf_perfil["bg"],
            conf_perfil["border"],
            f"O <b>perfil predominante</b> é "
            f"<b>{insight_perfil["Nome"]}</b>, "
            f"representando <b>{formatar_porcentagem(insight_perfil["Porcentagem"])}</b> dos leads."
        )

        st.markdown(config["graficos"]["distribuicao"]["titulo"])
        grafico_distribuicao_pizza(df_por_perfil, 
                            "perfil_cliente", 
                            "count", 
                            config["graficos"]["distribuicao"]["titulo_grafico"],
                            config["graficos"]["distribuicao"]["cores"]
                            )

def exibir_pagina_financeiro(df_evolucao_diaria, df_pagamento, df_consultores, curso, dict_kpis):
    config = PAGINAS["financeiro"]

    exibir_header_pagina(config["titulo"], curso, dict_kpis, config["cores_metricas"], financeiro=True)

    aba1, aba2, aba3 = st.tabs(["📈 Evolução", "💳 Pagamentos", "👨‍💼 Consultores"])

    with aba1:
        st.markdown(config["graficos"]["evolucao"]["titulo"])
        grafico_evolucao_diaria(
            df_evolucao_diaria,
            "data_venda",
            "count",
            config["graficos"]["evolucao"]["cor_linha"],
            config["graficos"]["evolucao"]["titulo_grafico"],
            config["graficos"]["evolucao"]["titulo_x"],
            config["graficos"]["evolucao"]["titulo_y"],
        )

    with aba2:
        st.markdown(config["graficos"]["pagamentos"]["titulo"])
        grafico_distribuicao_pizza(df_pagamento, 
                            "forma_pagamento", 
                            "count", 
                            config["graficos"]["pagamentos"]["titulo_grafico"],
                            config["graficos"]["pagamentos"]["cores"]
                            )

    with aba3:
        st.markdown(config["graficos"]["consultores"]["titulo"])
        grafico_distribuicao_barra(df_consultores, 
                            "responsavel_venda", 
                            "count", 
                            config["graficos"]["consultores"]["titulo_grafico"], 
                            config["graficos"]["consultores"]["titulo_x"], 
                            config["graficos"]["consultores"]["titulo_y"], 
                            config["graficos"]["consultores"]["cor"]
                            )
