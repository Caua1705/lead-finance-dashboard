from datetime import date
from src.utils.analytics_utils import calcular_distribuicao, calcular_evolucao_diaria
from src.data.repositories.sales_repository import SalesRepository
import pandas as pd

class SalesServices():
    def __init__(self, repo:SalesRepository):
        self.repo = repo

    def obter_intervalo_datas_vendas(self):
        intervalo = self.repo.get_intervalo_datas()

        data_minima = intervalo["data_minima"]
        data_maxima = intervalo["data_maxima"]

        if not data_minima or not data_maxima:
            hoje = date.today()
            return {"data_minima": hoje, "data_maxima": hoje}
        return intervalo
    
    def obter_vendas_filtradas(self, curso, data_inicial, data_final):
        df_vendas_filtradas = self.repo.get_vendas_filtradas(curso, data_inicial, data_final)
        return pd.DataFrame(df_vendas_filtradas)
    
    def calcular_kpis(self, df):
        if df.empty:
            return {
                "faturamento_total": 0,
                "numero_vendas": 0,
                "ticket_medio": 0,
                "porcentagem_a_vista": 0
            }
        faturamento_total = df["valor_total"].sum()
        numero_vendas = len(df)
        ticket_medio = faturamento_total / numero_vendas
        faturamento_a_vista = df.loc[df["forma_pagamento"].isin(["Pix","Dinheiro"]),"valor_total"].sum()
        porcentagem_a_vista = (faturamento_a_vista / faturamento_total) * 100
        return {
            "faturamento_total": faturamento_total,
            "numero_vendas": numero_vendas,
            "ticket_medio": ticket_medio,
            "porcentagem_a_vista": porcentagem_a_vista
        }
    
    def obter_evolucao_diaria(self, df, data_inicial, data_final, coluna, limite):
        if df.empty:
            return pd.DataFrame({ coluna: [], "count": [] })
        return calcular_evolucao_diaria(df, data_inicial, data_final, coluna, limite)
    
    def obter_distribuicao(self, df, coluna):
        if df.empty:
            return pd.DataFrame({
                coluna: ["Sem dados"],
                "count": [1]
            })
        return calcular_distribuicao(df, coluna)