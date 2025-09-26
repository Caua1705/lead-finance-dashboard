import pandas as pd

def calcular_distribuicao(df, coluna):
    return df[coluna].value_counts().reset_index()


def calcular_insights(df, coluna):
    df = calcular_distribuicao(df, coluna)
    nome_maior_ocorrencia = df[coluna].iloc[0]
    numero_maior_ocorrencia = df["count"].iloc[0]
    soma_ocorrencias = df["count"].sum()
    porcentagem = (numero_maior_ocorrencia * 100) / soma_ocorrencias
    return {
    "Nome": nome_maior_ocorrencia,
    "Porcentagem": porcentagem
}


def calcular_evolucao_diaria(df, data_inicial, data_final, coluna_data, limite):
    datas_intervalo_completo = pd.DataFrame({coluna_data:pd.date_range(data_inicial, data_final)})
    datas_reais = df[coluna_data].dt.normalize().value_counts().reset_index()
    df_concatenado = pd.merge(
        datas_intervalo_completo, 
        datas_reais, 
        on=coluna_data, 
        how="left"
        ).fillna(0)
    df_concatenado = df_concatenado.sort_values(by=coluna_data)
    df_concatenado = df_concatenado.iloc[0:limite]
    return df_concatenado