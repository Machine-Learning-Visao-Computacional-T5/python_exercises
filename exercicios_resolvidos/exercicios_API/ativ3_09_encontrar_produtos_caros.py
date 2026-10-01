"""Exercício 3.9 — Encontrar produtos caros

Objetivo: mostrar somente os produtos cujo preço é superior a 15.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

for produto in dados["products"]:
    if produto["price"] > 15:
        print(produto["title"])
