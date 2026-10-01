"""Exercício 13 — Lista de features

Adicione numero_compras, remova tempo_cliente, apresente a primeira feature e a quantidade final de features.
"""

features = ["idade", "renda", "tempo_cliente"]

features.append("numero_compras")
features.remove("tempo_cliente")
print(features[0])
print(len(features))
