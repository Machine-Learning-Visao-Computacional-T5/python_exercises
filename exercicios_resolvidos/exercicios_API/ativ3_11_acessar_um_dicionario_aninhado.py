"""Exercício 3.11 — Acessar um dicionário aninhado

Objetivo: mostrar a largura do primeiro produto.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

largura = dados["products"][0]["dimensions"]["width"]
print("Largura:", largura)
