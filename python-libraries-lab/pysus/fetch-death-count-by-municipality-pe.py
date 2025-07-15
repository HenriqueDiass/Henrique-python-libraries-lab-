from pysus.online_data import SIM

# 1. Baixar os dados de óbitos de Pernambuco (PE) em 2018
arquivos = SIM.download(groups=["cid10"], states="PE", years=2018)

# 2. Converter para DataFrame
df = arquivos.to_dataframe()

# 3. Verifica as colunas disponíveis (opcional)
print(df.columns.tolist())

# 4. Agrupar apenas pelo código do município
obitos_por_municipio = df.groupby('CODMUNRES').size().reset_index(name='total_obitos')

# 5. Ordenar do maior para o menor
obitos_por_municipio = obitos_por_municipio.sort_values(by='total_obitos', ascending=False)

# 6. Salvar como JSON
obitos_por_municipio.to_json("obitos_por_municipio_pe_2018.json", orient="records", indent=2)

# 7. Exibir os 5 primeiros para conferir
print(obitos_por_municipio.head())
