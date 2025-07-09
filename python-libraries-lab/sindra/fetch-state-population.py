import sidrapy
import pandas as pd
import locale

# Configurar locale para formatação brasileira
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Buscar dados da tabela 4709 - população residente
data = sidrapy.get_table(
    table_code='4709',
    territorial_level="3",  # 3 = UF
    ibge_territorial_code="all",
    variable='93'
)

# Ajustar colunas
data.columns = data.iloc[0]
data = data.iloc[1:]

# Selecionar colunas: UF, população, ano
df = data.iloc[:, [6, 4, 10]].copy()
df.columns = ['UF', 'populacao', 'ano']

# Formatar população
df['populacao'] = df['populacao'].astype(float)
df['populacao_formatada'] = [
    locale.format_string('%.0f', pop, grouping=True) for pop in df['populacao']
]

# Reorganizar colunas
df = df[['UF', 'ano', 'populacao', 'populacao_formatada']]

# Exibir
print(df)
