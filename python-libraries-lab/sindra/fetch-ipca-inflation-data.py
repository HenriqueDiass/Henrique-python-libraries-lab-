import requests
import pandas as pd
import matplotlib.pyplot as plt
import json

# URL para os últimos 12 meses do IPCA
url_ipca = "https://apisidra.ibge.gov.br/values/t/1737/p/last 12/v/63/n1/1"

print("--- BUSCANDO DADOS DO IPCA COM O MÉTODO CORRETO ---")
print(f"Acessando: {url_ipca}")

try:
    response = requests.get(url_ipca)
    response.raise_for_status()

    dados_brutos = response.json()
    dados_reais = dados_brutos[1:] # Remove a linha de cabeçalho

    # Cria um DataFrame do Pandas
    df = pd.DataFrame(dados_reais)

    # --- LINHAS CORRIGIDAS ---
    # Seleciona as colunas que vamos usar pelos seus nomes originais (D1C, V)
    # e já renomeia para nomes mais fáceis.
    df = df[['D1C', 'V']].rename(columns={'D1C': 'MesCodigo', 'V': 'Variacao'})

    # Converte a variação para número
    df['Variacao'] = pd.to_numeric(df['Variacao'])

    # AGORA USAMOS A COLUNA 'MesCodigo' (ex: "202406") PARA CONVERTER A DATA
    df['NomeMesFormatado'] = pd.to_datetime(df['MesCodigo'], format='%Y%m').dt.strftime('%b/%y')
    
    print("\n✅ Dados do IPCA recebidos e processados com sucesso!")

    # --- GERAÇÃO DO GRÁFICO ---
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(12, 7))
    
    # Usa a nova coluna com o nome formatado para o eixo X
    bars = plt.bar(df['NomeMesFormatado'], df['Variacao'], color='#007acc')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}%',
                 va='bottom' if yval >=0 else 'top', ha='center', fontsize=10)

    plt.title('Variação Mensal do IPCA no Brasil - Últimos 12 Meses', fontsize=16)
    plt.ylabel('Variação (%)', fontsize=12)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


except requests.exceptions.RequestException as e:
    print(f"❌ Ocorreu um erro de conexão: {e}")
except Exception as e:
    print(f"❌ Ocorreu um erro ao processar os dados: {e}")