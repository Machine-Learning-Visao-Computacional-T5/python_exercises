"""Exercício 5 — Leitura e interpretação

Informe a saída do código. Depois explique o que uma diferença elevada entre treino e teste pode sugerir.
"""

modelo = "Regressão Logística"
acuracia_treino = 0.92
acuracia_teste = 0.78
diferenca = acuracia_treino - acuracia_teste
print(modelo)
print(round(diferenca, 2))

# Saída: "Regressão Logística" e 0.14.
# Uma diferença elevada pode sugerir overfitting, mas a conclusão depende
# dos dados, da métrica e do procedimento de avaliação.
print(modelo)
print(round(diferenca, 2))
