"""Exercício 8 — Tipo de tarefa de ML

Para tipo_alvo igual a categoria, apresente Problema de classificação. Para numero, apresente Problema de regressão. Para outro valor, apresente Tipo de problema desconhecido.
"""

tipo_alvo = "categoria"

if tipo_alvo == "categoria":
    print("Problema de classificação")
elif tipo_alvo == "numero":
    print("Problema de regressão")
else:
    print("Tipo de problema desconhecido")
