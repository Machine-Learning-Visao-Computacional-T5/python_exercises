"""Exercício 3.13 — Mostrar avaliador e nota

Objetivo: mostrar o nome e a nota de cada pessoa que avaliou o primeiro produto.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

produto = dados["products"][0]
for avaliacao in produto["reviews"]:
    print("Avaliador:", avaliacao["reviewerName"])
    print("Nota:", avaliacao["rating"])
    print()
