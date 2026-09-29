"""Exercício 3.6 — Adicionar uma nova chave

Objetivo: registrar que o primeiro produto está em promoção.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

produto = dados["products"][0]
produto["onSale"] = True
print(produto)
