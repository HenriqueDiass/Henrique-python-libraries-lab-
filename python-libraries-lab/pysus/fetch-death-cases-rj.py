from pysus.online_data import SIM

# Baixa os arquivos para o estado do Rio de Janeiro, ano de 2018
arquivos = SIM.download(groups=["cid10"], states="RJ", years=2018)

# Converte todos os arquivos baixados em um DataFrame
df = arquivos.to_dataframe()

# Visualiza as dimensões e as 5 primeiras linhas
print(df.shape)
print(df.head())