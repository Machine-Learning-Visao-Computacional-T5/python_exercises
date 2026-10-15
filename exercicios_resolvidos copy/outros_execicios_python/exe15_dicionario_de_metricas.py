"""Exercício 15 — Dicionário de métricas

Crie um dicionário com acurácia 0.88, precisão 0.84 e recall 0.79. Mostre o recall, adicione F1 igual a 0.81 e percorra todos os itens.
"""

metricas = {"acuracia": 0.88, "precisao": 0.84, "recall": 0.79}
print(metricas["recall"])
metricas["f1"] = 0.81
for nome, valor in metricas.items():
    print(nome, valor)
