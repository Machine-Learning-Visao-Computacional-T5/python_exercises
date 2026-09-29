"""Exercício 3.10 — Calcular o valor do estoque

Objetivo: calcular quanto vale o estoque de cada produto.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

for produto in dados["products"]:
    valor_estoque = produto["price"] * produto["stock"]
    print(produto["title"])
    print("Valor do estoque: R$", round(valor_estoque, 2))
