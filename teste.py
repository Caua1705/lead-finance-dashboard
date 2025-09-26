import pandas as pd

# Arquivos
arquivo_dentistas = "contatos_dentistas_formatado.csv"
arquivo_tpd = "contatos_tpd_formatado.csv"

# Carregar
df_dentistas = pd.read_csv(arquivo_dentistas)
df_tpd = pd.read_csv(arquivo_tpd)

# Normalizar colunas
def normalizar_colunas(df):
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
    )
    return df

df_dentistas = normalizar_colunas(df_dentistas)
df_tpd = normalizar_colunas(df_tpd)

# Renomear "categoria" -> "perfil_cliente"
if "categoria" in df_dentistas.columns:
    df_dentistas = df_dentistas.rename(columns={"categoria": "perfil_cliente"})
if "categoria" in df_tpd.columns:
    df_tpd = df_tpd.rename(columns={"categoria": "perfil_cliente"})

# Concatenar
df_unificado = pd.concat([df_dentistas, df_tpd], ignore_index=True)

# Salvar
df_unificado.to_csv("contatos_unificado.csv", index=False)

print("✅ Arquivo unificado salvo como contatos_unificado.csv")
print("Colunas finais:", df_unificado.columns.tolist())
