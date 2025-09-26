from src.data.db_connection import engine, Base
from src.model.clients_model import Clientes
from src.model.sales_model import Vendas
from src.model.courses_model import Cursos
from src.model.messages_model import Mensagens
from src.model.ia_history_model import HistoricoIA

def criar_tabelas():
    Base.metadata.create_all(engine)
