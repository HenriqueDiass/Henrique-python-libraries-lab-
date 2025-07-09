import requests
import pandas as pd

def buscar_dados_cor_raca_recife():
    """
    Busca e exibe a população de Recife por Cor ou Raça do Censo 2022,
    com a formatação correta.
    """
    print("--- Tabela: População de Recife por Cor ou Raça (Censo 2022) ---")
    
    codigo_recife = "2611606"
    
    # URL para a Tabela 9605. A ordem dos parâmetros (/v/ antes de /c86/)
    # influencia a ordem das colunas na resposta.
    url = f"https://apisidra.ibge.gov.br/values/t/9605/n6/{codigo_recife}/p/2022/v/93/c86/allxt?formato=json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados_brutos = response.json()
        
        # Pula a primeira linha, que é o cabeçalho
        dados_reais = dados_brutos[1:]
        
        df = pd.DataFrame(dados_reais)
        
        # --- CORREÇÃO PRINCIPAL ---
        # A API retorna as dimensões na ordem em que aparecem na URL.
        # D1N: Município
        # D2N: Ano
        # D3N: Variável ("População residente")
        # D4N: Cor ou Raça (A coluna que queremos!)
        tabela = df[['D4N', 'V']].rename(columns={'D4N': 'Cor ou Raça', 'V': 'População'})
        
        # Converte a coluna População para número
        tabela['População'] = pd.to_numeric(tabela['População'], errors='coerce')
        tabela.dropna(subset=['População'], inplace=True)
        tabela['População'] = tabela['População'].astype(int)
        
        # Deixa a tabela mais bonita antes de imprimir
        tabela = tabela.sort_values(by='População', ascending=False)
        tabela['População'] = tabela['População'].apply(lambda x: f'{x:,.0f}'.replace(',', '.'))

        # Imprime a tabela final formatada
        print(tabela.to_string(index=False))

    except Exception as e:
        print(f"❌ Falha ao buscar dados: {e}")
    finally:
        print("-" * 60)


# --- Execução Principal ---
if __name__ == "__main__":
    buscar_dados_cor_raca_recife()