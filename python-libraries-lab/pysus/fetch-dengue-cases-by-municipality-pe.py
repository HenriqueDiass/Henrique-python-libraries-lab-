from pysus.online_data import SINAN

# Baixar dados dengue 2018
arquivos = SINAN.download(diseases=['DENG'], years=[2018])
df = arquivos.to_dataframe()

print(df.columns.tolist())  # Só para conferir, pode remover depois

# Filtrar Pernambuco pelo código do município de residência
df_pe = df[df['ID_MN_RESI'].astype(str).str.startswith('26')]

# Agrupar por município (pelo código de residência)
casos_por_municipio = df_pe.groupby('ID_MN_RESI').size().reset_index(name='total_casos')

# Se quiser, renomear coluna para algo mais amigável
casos_por_municipio = casos_por_municipio.rename(columns={'ID_MN_RESI': 'COD_MUN_RES'})

# Salvar JSON
casos_por_municipio.to_json("dengue_por_municipio_pe_2018.json", orient="records", indent=2)

print(casos_por_municipio.head())
