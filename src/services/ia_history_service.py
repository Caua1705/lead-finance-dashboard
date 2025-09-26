from src.data.repositories.ia_history_repository import HistoricoIARepository

class HistoricoIAService():
    def __init__(self, repo: HistoricoIARepository):
        self.repo = repo

    def obter_historico_mensagens(self, id_cliente):
        return self.repo.get_historico_mensagens(id_cliente)
