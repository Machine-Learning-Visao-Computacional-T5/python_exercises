"""Exercício 3.4 — Mostrar título e preço

Objetivo: mostrar duas informações do primeiro produto.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

produto = dados["products"][0]
print("Produto:", produto["title"])
print("Preço:", produto["price"])
