from sqlalchemy.orm import Session
from src.model.ia_history_model import HistoricoIA
from src.model.clients_model import Clientes
from sqlalchemy import select

class HistoricoIARepository():
    def __init__(self, db:Session):
        self.db = db

    def get_historico_mensagens(self, id_cliente):
        query = select(
            HistoricoIA.message
        ).where(
            HistoricoIA.cliente_id == id_cliente
        ).order_by(
            HistoricoIA.id
        )

        return self.db.execute(query).mappings().all()

