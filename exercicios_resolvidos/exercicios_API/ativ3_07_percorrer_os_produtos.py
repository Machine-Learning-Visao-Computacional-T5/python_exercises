"""Exercício 3.7 — Percorrer os produtos

Objetivo: mostrar o título de todos os produtos.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

for produto in dados["products"]:
    print(produto["title"])
