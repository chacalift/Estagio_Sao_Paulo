'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
import json

# Função para ler o arquivo JSON e extrair os dados
def ler_dados_json(arquivo):
    with open(arquivo, 'r') as file:
        dados = json.load(file)
    return dados["faturamento_diario"]

# Função para calcular o menor valor de faturamento
def menor_valor(faturamento):
    valores = [item['valor'] for item in faturamento if item['valor'] > 0]
    return min(valores) if valores else None

# Função para calcular o maior valor de faturamento
def maior_valor(faturamento):
    valores = [item['valor'] for item in faturamento if item['valor'] > 0]
    return max(valores) if valores else None

# Função para calcular o número de dias com faturamento acima da média
def dias_acima_media(faturamento):
    valores = [item['valor'] for item in faturamento if item['valor'] > 0]
    if not valores:
        return 0
    
    media = sum(valores) / len(valores)
    dias_acima = sum(1 for item in faturamento if item['valor'] > media)
    
    return dias_acima

# Função principal para processamento dos dados
def processar_faturamento(arquivo):
    faturamento = ler_dados_json(arquivo)
    
    menor = menor_valor(faturamento)
    maior = maior_valor(faturamento)
    dias_acima = dias_acima_media(faturamento)
    
    return {
        "menor_valor": menor,
        "maior_valor": maior,
        "dias_acima_media": dias_acima
    }

# Exemplo de uso
resultado = processar_faturamento('faturamento.json')
print("Menor valor de faturamento:", resultado["menor_valor"])
print("Maior valor de faturamento:", resultado["maior_valor"])
print("Número de dias com faturamento acima da média mensal:", resultado["dias_acima_media"])
