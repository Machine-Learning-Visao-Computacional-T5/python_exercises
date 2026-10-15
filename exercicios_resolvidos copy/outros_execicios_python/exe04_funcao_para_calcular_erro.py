"""Exercício 4 — Função para calcular erro

Crie a função calcular_erro, que recebe uma acurácia e retorna 1 menos a acurácia. Teste com 0.82.
"""

def calcular_erro(acuracia):
    return 1 - acuracia

print(round(calcular_erro(0.82), 2))  # 0.18
