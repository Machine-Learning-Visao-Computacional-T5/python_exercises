"""Exercício 3.8 — Mostrar título e preço de todos

Objetivo: mostrar o título e o preço de cada produto.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

for produto in dados["products"]:
    print("Produto:", produto["title"])
    print("Preço: R$", produto["price"])
    print()
