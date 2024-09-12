import json

# Exemplo de JSON com dados fictícios
dados_faturamento = '''
{
    "faturamento_diario": [0, 1500, 2300, 3000, 0, 2000, 3400, 2500, 0, 0, 1000, 4500, 1500, 0, 0, 2000, 2700, 0, 4000, 3000, 2900, 1500, 5000, 0, 0, 2100, 3200, 0, 0, 1800, 3700]
}
'''

dados = json.loads(dados_faturamento)
faturamento = [f for f in dados["faturamento_diario"] if f > 0]

menor_valor = min(faturamento)
maior_valor = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_media = len([f for f in faturamento if f > media_mensal])

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_media}")
