from sqlalchemy.orm import Session
from src.model.clients_model import Clientes
from src.model.courses_model import Cursos
from sqlalchemy import select, func

class ClientsRepository():
    def __init__(self, db:Session):
        self.db = db

    def get_intervalo_datas(self):
        intervalo_datas = self.db.execute(
            select(
            func.min(Clientes.data_criacao).label("data_minima"),
            func.max(Clientes.data_criacao).label("data_maxima")
            )
        ).mappings().one()
        return dict(intervalo_datas)
    
    def get_cidades(self):
        cidade = self.db.execute(
            select(Clientes.cidade)
            .distinct()
            .order_by(Clientes.cidade)
            ).scalars().all()
        return cidade
    
    def get_etapas_atendimento(self):
        etapas_atendimento = self.db.execute(
            select(Clientes.etapa_atendimento)
            .distinct()
            .order_by(Clientes.etapa_atendimento)
            ).scalars().all()
        return etapas_atendimento

    def get_clientes_filtrados(self, curso, data_inicial, data_final, cidade):
        query = select(
            Clientes.perfil_cliente,
            Clientes.cidade,
            Clientes.etapa_atendimento,
            Clientes.status_qualificacao,
            Clientes.data_criacao
        ).where(
            Clientes.data_criacao.between(data_inicial, data_final)
        )

        if curso != "Todos":
            query = (
                query.add_columns(Cursos.nome.label("curso_nome"))
                .join(Cursos, Clientes.curso_id == Cursos.id)
                .where(Cursos.nome == curso)
            )

        if cidade != "Todas":
            query = query.where(Clientes.cidade == cidade)

        clientes_filtrados = self.db.execute(query).mappings().all()
        return clientes_filtrados
    