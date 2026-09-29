"""Exercício 3.1 — Acessar a lista de produtos

Objetivo: mostrar todos os produtos armazenados em dados.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

produtos = dados["products"]
print(produtos)
