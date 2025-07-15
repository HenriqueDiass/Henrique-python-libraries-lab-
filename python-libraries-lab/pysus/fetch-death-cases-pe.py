from pysus.online_data import SIM

# Baixar os dados do SIM para Pernambuco em 2018
arquivos = SIM.download(groups=["cid10"], states="PE", years=2018)

# Converter os dados para DataFrame
df = arquivos.to_dataframe()

# Mostrar resumo
print(df.shape)
print(df.head())

# Salvar em JSON (1 linha por registro, ideal para arquivos grandes)
df.to_json("obitos_pe_2018.json", orient="records", lines=True)
