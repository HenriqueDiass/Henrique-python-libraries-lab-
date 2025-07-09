import sidrapy
import pandas as pd
import locale

# Buscar dados do SIDRA
data = sidrapy.get_table(
    table_code='4709',
    territorial_level="6",
    ibge_territorial_code="all",
    variable='93'
)

# Substituir o cabeçalho pelas colunas da primeira linha e remover a linha extra
data.columns = data.iloc[0]
data = data.iloc[1:]

# Criar uma cópia do slice necessário para evitar o warning
df = data.iloc[:, [6, 4, 10]].copy()

# Renomear colunas
df.columns = ['municipio_UF', 'populacao', 'ano']

# Separar município e UF usando .loc
df[['municipio', 'UF']] = df['municipio_UF'].str.split('- ', expand=True)

# Formatar população
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
df.loc[:, 'populacao'] = df['populacao'].astype(float)
df.loc[:, 'populacao_formatada'] = [locale.format_string('%.0f', pop, grouping=True) for pop in df['populacao']]

# Reorganizar colunas
df = df[['municipio', 'UF', 'ano', 'populacao', 'populacao_formatada']]

# Visualizar
print(df.head())
