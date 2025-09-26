import streamlit as st
from sqlalchemy.orm import Session
from datetime import datetime
from src.data.db_connection import engine
# from src.services.vendas_services import add_sale
# você poderia também importar uma função que busca clientes do repository

st.warning("🚧 Página em construção! Em breve novidades...")

# st.title("📝 Registrar Nova Venda")

# with st.form("form_venda", clear_on_submit=True):
#     st.subheader("📌 Informações da Venda")

#     # Cliente - aqui ideal seria puxar do banco
#     cliente_id = st.selectbox(
#         "Cliente",
#         options=[1, 2, 3],  # mock (trocar por consulta ao banco)
#         format_func=lambda x: f"Cliente {x}",
#         help="Selecione o cliente que realizou a compra"
#     )

#     valor_total = st.number_input(
#         "Valor Total (R$)",
#         min_value=0.0,
#         step=50.0,
#         format="%.2f",
#         help="Digite o valor total da venda"
#     )

#     forma_pagamento = st.radio(
#         "Forma de Pagamento",
#         ["Pix", "Cartão", "Boleto", "Dinheiro"],
#         help="Selecione como o cliente pagou"
#     )

#     parcelas = st.slider(
#         "Número de Parcelas",
#         min_value=1,
#         max_value=12,
#         value=1,
#         help="Defina em quantas parcelas o pagamento será feito"
#     )

#     data_venda = st.date_input(
#         "Data da Venda",
#         value=datetime.today(),
#         help="Escolha a data da venda"
#     )

#     responsavel = st.text_input(
#         "Responsável pela Venda",
#         placeholder="Nome do consultor",
#         help="Digite quem realizou o fechamento da venda"
#     )

#     # Expander para informações opcionais
#     with st.expander("➕ Detalhes adicionais"):
#         observacoes = st.text_area("Observações", placeholder="Ex: Cliente pediu nota fiscal")

#     submitted = st.form_submit_button("💾 Registrar Venda")

        # if submitted:
        #     if cliente_id and valor_total > 0:
        #         with Session(engine) as session:
        #             venda = add_sale(
        #                 session,
        #                 cliente_id,
        #                 valor_total,
        #                 forma_pagamento,
        #                 parcelas,
        #                 responsavel
        #             )
        #             st.success("✅ Venda registrada com sucesso!")
        #             st.table({
        #                 "ID": [venda.id],
        #                 "Cliente": [cliente_id],
        #                 "Valor": [valor_total],
        #                 "Forma Pagamento": [forma_pagamento],
        #                 "Parcelas": [parcelas],
        #                 "Data": [data_venda],
        #                 "Responsável": [responsavel],
        #                 "Obs": [observacoes or "-"]
        #             })
        #     else:
        #         st.error("⚠️ Preencha todos os campos obrigatórios.")
