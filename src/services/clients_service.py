from datetime import date
import pandas as pd
from src.utils.analytics_utils import calcular_insights
from src.utils.analytics_utils import calcular_evolucao_diaria, calcular_distribuicao
import streamlit as st

from src.data.repositories.clients_repository import ClientsRepository

class ClientsServices():
    def __init__(self, repo: ClientsRepository):
        self.repo = repo

    def obter_intervalo_datas_clientes(self):
        intervalo = self.repo.get_intervalo_datas()

        data_minima = intervalo["data_minima"]
        data_maxima = intervalo["data_maxima"]

        if not data_minima or not data_maxima:
            hoje = date.today()
            return {"data_minima": hoje, "data_maxima": hoje}
        
        return intervalo
    
    def obter_cidades_unicas(self):
        return self.repo.get_cidades()
    
    def obter_df_clientes_filtrado(self, curso, data_inicial, data_final, cidade):
        clientes_filtrado = self.repo.get_clientes_filtrados(curso, data_inicial, data_final, cidade)
        return pd.DataFrame(clientes_filtrado)
    
    def calcular_kpis(self, df):
        if df.empty:
            return {
                "total": 0,
                "qualificados": 0,
                "atendimento_ia": 0,
                "atendimento_consultor": 0
            }
        return {
            "total": len(df),
            "qualificados": len(df.loc[df["status_qualificacao"] == "qualificado"]),
            "atendimento_ia": len(df.loc[df["etapa_atendimento"] == "IA"]),
            "atendimento_consultor": len(df.loc[df["etapa_atendimento"] == "Consultor"])
        }
    
    def obter_insight(self, df, coluna):
        if df.empty or df[coluna].dropna().empty:
            return {"Nome": "-", "Porcentagem": 0.0}
        return calcular_insights(df, coluna)
    
    def obter_evolucao_diaria(self, df, data_inicial, data_final, coluna, limite):
        if df.empty:
            return pd.DataFrame({ coluna: [], "count": [] })
        return calcular_evolucao_diaria(df, data_inicial, data_final, coluna, limite)

    def obter_distribuicao_por_perfil(self, df, coluna):
        if df.empty:
            return pd.DataFrame({
                coluna: ["Sem dados"],
                "count": [1]
            })
        return calcular_distribuicao(df, coluna)
    
    def obter_etapas_atendimento(self):
        return self.repo.get_etapas_atendimento()