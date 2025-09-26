from sqlalchemy.orm import Session
from src.model.messages_model import Mensagens
from src.model.courses_model import Cursos
from src.model.clients_model import Clientes
from sqlalchemy import select

class MessagesRepository():
    def __init__(self, db:Session):
        self.db = db

    def get_mensagens(self, curso, data_inicial, data_final, cidade):
        query = select(
            Mensagens.data_envio
        ).where(
            Mensagens.data_envio.between(data_inicial, data_final)
        )

        if curso != "Todos":
            query = (
                query.add_columns(Cursos.nome.label("curso_nome"))
                .join(Cursos, Mensagens.curso_id == Cursos.id)
                .where(Cursos.nome == curso)
            )

        if cidade != "Todas":
            query = (
                query.add_columns(Clientes.cidade)
                .join(Clientes, Mensagens.cliente_id == Clientes.id)
                .where(Clientes.cidade == cidade)
            )

        return self.db.execute(query).mappings().all()

    def get_all_mensagens(self, curso, data_inicial, data_final, etapa_atendimento):
        query = (
            select(
                Mensagens.id,
                Mensagens.conteudo,
                Mensagens.data_envio,
                Clientes.id.label("cliente_id"),
                Clientes.nome.label("cliente_nome"),
                Clientes.telefone.label("cliente_telefone"),
                Clientes.forma_pagamento_preferida.label("forma_pagamento"),
                Clientes.tipo_inscricao.label("tipo_inscricao"),
                Clientes.perfil_cliente.label("perfil_cliente"),
                Clientes.status_qualificacao.label("status_qualificacao"),
                Clientes.cidade,
                Clientes.etapa_atendimento,
                Cursos.nome.label("curso_nome")
            )
            .join(Clientes, Mensagens.cliente_id == Clientes.id)
            .join(Cursos, Mensagens.curso_id == Cursos.id)
            .where(Mensagens.data_envio.between(data_inicial, data_final))
            .where(Cursos.nome == curso)
            .where(Clientes.etapa_atendimento == etapa_atendimento)
        )

        return self.db.execute(query).mappings().all()
