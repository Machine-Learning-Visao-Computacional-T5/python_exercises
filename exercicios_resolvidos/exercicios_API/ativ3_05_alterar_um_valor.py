"""Exercício 3.5 — Alterar um valor

Objetivo: alterar o estoque do primeiro produto para 80.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

produto = dados["products"][0]
produto["stock"] = 80
print(produto["stock"])
