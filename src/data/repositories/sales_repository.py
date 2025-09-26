from sqlalchemy.orm import Session
from sqlalchemy import select, func
from src.model.sales_model import Vendas
from src.model.courses_model import Cursos
from src.data.db_connection import engine

class SalesRepository():
    def __init__(self, db:Session):
        self.db = db

    def get_intervalo_datas(self):
        intervalo_datas = self.db.execute(
            select(
                func.min(Vendas.data_venda).label("data_minima"),
                func.max(Vendas.data_venda).label("data_maxima"),
            )
        ).mappings().one()
        return dict(intervalo_datas)
    
    def get_vendas_filtradas(self, curso, data_inicial, data_final):
        query = select(
            Vendas.valor_total,
            Vendas.forma_pagamento,
            Vendas.data_venda,
            Vendas.responsavel_venda
        ).where(
            Vendas.data_venda.between(data_inicial, data_final)
        )

        if curso != "Todos":
            query = (
                query.add_columns(Cursos.nome.label("curso_nome"))
                .join(Cursos, Cursos.id == Vendas.curso_id)
                .where(Cursos.nome == curso)
            )
            
        vendas_filtradas = self.db.execute(query).mappings().all()
        return vendas_filtradas