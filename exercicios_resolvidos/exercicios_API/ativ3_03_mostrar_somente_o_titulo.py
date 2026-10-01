"""Exercício 3.3 — Mostrar somente o título

Objetivo: mostrar o título do primeiro produto.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

titulo = dados["products"][0]["title"]
print(titulo)
