"""Exercício 16 — Estrutura composta

Apresente somente os modelos com acurácia maior ou igual a 0.80.
"""

resultados = [
    {"modelo": "Regressão Logística", "acuracia": 0.81},
    {"modelo": "Árvore de Decisão", "acuracia": 0.76},
    {"modelo": "Random Forest", "acuracia": 0.89}
]

for resultado in resultados:
    if resultado["acuracia"] >= 0.80:
        print(resultado["modelo"])
