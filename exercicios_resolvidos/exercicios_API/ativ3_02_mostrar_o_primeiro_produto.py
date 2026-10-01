"""Exercício 3.2 — Mostrar o primeiro produto

Objetivo: acessar e mostrar o primeiro produto da lista.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

primeiro_produto = dados["products"][0]
print(primeiro_produto)
