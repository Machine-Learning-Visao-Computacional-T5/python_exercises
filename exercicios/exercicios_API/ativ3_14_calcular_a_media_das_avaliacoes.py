"""Exercício 3.14 — Calcular a média das avaliações

Objetivo: calcular a média das notas do primeiro produto.

Atenção: existe um erro proposital no código. Encontre-o antes de executar.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

produto = dados["products"][0]
soma = 0
for avaliacao in produto["reviews"]:
    soma = soma + avaliacao["rating"]
media = soma / len(produto["reviews"])
print("Média:", media)
