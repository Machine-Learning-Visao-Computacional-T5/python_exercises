"""Exercício 3.12 — Percorrer as avaliações

Objetivo: mostrar os comentários recebidos pelo primeiro produto.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

produto = dados["products"][0]
for avaliacao in produto["reviews"]:
    print(avaliacao["comment"])
