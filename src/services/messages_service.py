import pandas as pd
from src.data.repositories.messages_repository import MessagesRepository
from src.utils.analytics_utils import calcular_insights

class MessageService():
    def __init__(self, repo: MessagesRepository):
        self.repo = repo

    def obter_mensagens_por_horario(self, curso, data_inicial, data_final, cidade):
        mensagens_por_hora = self.repo.get_mensagens(curso, data_inicial, data_final, cidade)
        return pd.DataFrame(mensagens_por_hora)

    def obter_insight(self, curso, data_inicial, data_final, cidade, coluna):
        df_mensagens = self.obter_mensagens_por_horario(curso, data_inicial, data_final, cidade)

        if df_mensagens.empty:
            return {"Nome": "-", "Porcentagem": 0.0}

        df_mensagens[coluna] = df_mensagens["data_envio"].dt.hour

        if df_mensagens[coluna].dropna().empty:
            return {"Nome": "-", "Porcentagem": 0.0}

        return calcular_insights(df_mensagens, coluna)
    
    def obter_todas_mensagens(self, curso, data_inicial, data_final, etapa_atendimento):
        mensagens = self.repo.get_all_mensagens(curso, data_inicial, data_final, etapa_atendimento)
        return pd.DataFrame(mensagens)