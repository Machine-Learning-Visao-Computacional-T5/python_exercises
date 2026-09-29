"""Exercício 2 — Acessar o dado do seu ambiente

Objetivo: carregar o arquivo produtos.json em uma variável chamada dados.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print(dados)
