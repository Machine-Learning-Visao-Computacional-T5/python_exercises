"""Exercício 13 — Valores ausentes por coluna

Conte valores None em cada feature usando um dicionário.
"""

dataset = [
    {"idade": 20, "renda": None},
    {"idade": None, "renda": 3000},
    {"idade": 35, "renda": None}
]

# Solução A — Contagem por chave
# Complexidade: O(n × f) tempo e O(f) espaço
# f representa a quantidade de features por registro.
ausentes = {}
for registro in dataset:
    for feature, valor in registro.items():
        if valor is None:
            ausentes[feature] = ausentes.get(feature, 0) + 1
        else:
            ausentes.setdefault(feature, 0)
print("Solução A:", ausentes)
