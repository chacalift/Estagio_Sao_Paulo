# Dados de faturamento por estado
faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Função para calcular o total de faturamento
def calcular_total_faturamento(faturamento):
    return sum(faturamento.values())

# Função para calcular a porcentagem do faturamento de cada estado
def calcular_porcentagens(faturamento, total):
    porcentagens = {}
    for estado, valor in faturamento.items():
        porcentagem = (valor / total) * 100
        porcentagens[estado] = porcentagem
    return porcentagens

# Função para identificar o estado com maior e menor faturamento
def identificar_extremos(faturamento):
    estado_max = max(faturamento, key=faturamento.get)
    estado_min = min(faturamento, key=faturamento.get)
    return estado_max, estado_min

# Função principal para processamento dos dados
def processar_faturamento(faturamento):
    total = calcular_total_faturamento(faturamento)
    porcentagens = calcular_porcentagens(faturamento, total)
    estado_max, estado_min = identificar_extremos(faturamento)
    
    return {
        "total_faturamento": total,
        "porcentagens": porcentagens,
        "estado_maior_faturamento": estado_max,
        "estado_menor_faturamento": estado_min
    }

# Exemplo de uso
resultado = processar_faturamento(faturamento_estados)
print(f"Total de faturamento: R${resultado['total_faturamento']:.2f}")

for estado, porcentagem in resultado["porcentagens"].items():
    print(f"{estado}: {porcentagem:.2f}% do total")

print(f"Estado com maior faturamento: {resultado['estado_maior_faturamento']}")
print(f"Estado com menor faturamento: {resultado['estado_menor_faturamento']}")
