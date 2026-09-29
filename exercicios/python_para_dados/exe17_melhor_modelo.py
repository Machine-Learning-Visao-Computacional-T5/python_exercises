"""Exercício 17 — Melhor modelo

Utilizando a estrutura do exercício anterior, encontre o modelo com maior acurácia sem ordenar a lista.
"""

resultados = [
    {"modelo": "Regressão Logística", "acuracia": 0.81},
    {"modelo": "Árvore de Decisão", "acuracia": 0.76},
    {"modelo": "Random Forest", "acuracia": 0.89}
]

melhor = resultados[0]
for resultado in resultados:
    if resultado["acuracia"] > melhor["acuracia"]:
        melhor = resultado
print("Melhor modelo:", melhor["modelo"])
print("Acurácia:", melhor["acuracia"])
