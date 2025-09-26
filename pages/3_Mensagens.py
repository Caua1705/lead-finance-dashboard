import streamlit as st

from src.data.db_connection import Sessionlocal
from src.data.db_init import criar_tabelas

from src.data.repositories.clients_repository import ClientsRepository
from src.data.repositories.courses_repository import CoursesRepository
from src.data.repositories.messages_repository import MessagesRepository
from src.data.repositories.ia_history_repository import HistoricoIARepository

from src.services.clients_service import ClientsServices
from src.services.courses_service import CoursesServices
from src.services.messages_service import MessageService
from src.services.ia_history_service import HistoricoIAService

from src.utils.date_utils import formatar_periodo

from src.view.components.filters_sidebar import exibir_filtros_mensagens


st.set_page_config(page_title="Gestão de Leads", page_icon="👥", layout="wide")


def inicializar_repositories(db):
    clients_repo = ClientsRepository(db)
    courses_repo = CoursesRepository(db)
    message_repo = MessagesRepository(db)
    history_ia_repo = HistoricoIARepository(db)
    return clients_repo, courses_repo, message_repo, history_ia_repo


def inicializar_services(clients_repo, courses_repo, message_repo, history_ia_repo):
    clients_service = ClientsServices(clients_repo)
    courses_service = CoursesServices(courses_repo)
    message_service = MessageService(message_repo)
    history_ia_service = HistoricoIAService(history_ia_repo)
    return clients_service, courses_service, message_service, history_ia_service


def carregar_entradas_filtros(
    clients_service: ClientsServices,
    courses_service: CoursesServices
):
    cursos = courses_service.obter_cursos_unicos()
    intervalo_datas = clients_service.obter_intervalo_datas_clientes()
    etapas_atendimento = clients_service.obter_etapas_atendimento()
    return cursos, intervalo_datas, etapas_atendimento

def aplicar_filtros(cursos, intervalo_datas, etapas_atendimento):
    saidas_filtros = exibir_filtros_mensagens(cursos, intervalo_datas, etapas_atendimento)
    data_inicial, data_final = formatar_periodo(saidas_filtros["periodo"])
    return (
        saidas_filtros["curso"],
        data_inicial,
        data_final,
        saidas_filtros["etapa_atendimento"]
    )


def main():
    criar_tabelas()
    with Sessionlocal() as db:
        clients_repo, courses_repo, message_repo, history_ia_repo = inicializar_repositories(db)
        clients_service, courses_service, message_service, history_ia_service = inicializar_services(
            clients_repo,
            courses_repo,
            message_repo,
            history_ia_repo
        )

        cursos, intervalo_datas, etapas_atendimento = carregar_entradas_filtros(
            clients_service,
            courses_service
        )
        curso, data_inicial, data_final, etapa_atendimento = aplicar_filtros(
            cursos,
            intervalo_datas,
            etapas_atendimento
        )

        df_mensagens = message_service.obter_todas_mensagens(
            curso,
            data_inicial,
            data_final,
            etapa_atendimento
        )

        df_mensagens_filtrado = df_mensagens.loc[df_mensagens["status_qualificacao"] == "qualificado"]
        mensagens_agrupadas = df_mensagens_filtrado.sort_values("data_envio").groupby("cliente_id").last().reset_index()


        st.title(f"💬 Mensagens por Cliente - Etapa: {etapa_atendimento}")

        st.divider()

        # Layout em 2 colunas para organizar melhor
        cols = st.columns(2)

        for i, row in mensagens_agrupadas.iterrows():
            col = cols[i % 2]
            with col.container(border=True):
                nome = row["cliente_nome"] 
                curso = row['curso_nome']
                cidade = row['cidade']
                ultima_mensagem = row["conteudo"]
                telefone = row["cliente_telefone"]
                etapa_atendimento = row["etapa_atendimento"]
                perfil_cliente = row["perfil_cliente"]
                forma_pagamento = row["forma_pagamento"]
                tipo_inscricao = row["tipo_inscricao"]
                id_cliente = row["cliente_id"]
                data_envio = row["data_envio"]

                st.subheader(nome)

                # Info formatada
                if etapa_atendimento == "IA":
                    st.caption(f"📚 {curso} | 📍 {cidade} | 👤 {perfil_cliente}")
                else:
                    st.caption(f"📚 {curso} | 📍 {cidade} | 👤 {perfil_cliente} | 📌 {tipo_inscricao} | 💳 {forma_pagamento}")

                # Última mensagem
                st.write(f"💬 Última mensagem: *{ultima_mensagem[:80]}...*")

                # Data formatada
                from datetime import datetime
                data_formatada = data_envio.strftime("%d/%m/%Y %H:%M") if isinstance(data_envio, datetime) else data_envio
                st.write(f"📅 **Última interação:** {data_formatada}")

                # Link WhatsApp
                if telefone:
                    st.markdown(
                        f"📞 [Abrir no WhatsApp](https://wa.me/55{telefone})",
                        unsafe_allow_html=True
                    )

                # Expander para histórico
                with st.expander("📜 Ver Conversa"):
                    historico_mensagens = history_ia_service.obter_historico_mensagens(id_cliente)
                    for h in historico_mensagens:
                        msg = h["message"]
                        autor = msg.get("type")
                        conteudo = msg.get("content", "")

                        if autor == "human":
                            with st.chat_message("user", avatar="src/view/assets/LOGO-HUMANO.png"):
                                st.markdown(f"{conteudo[:80]}...")
                        else:
                            with st.chat_message("assistant", avatar="src/view/assets/LOGO-2K.png"):
                                st.markdown(f"{conteudo[:80]}...")
if __name__ == "__main__":
    main()