"""Desafio final — Relatório de produtos

Objetivo: mostrar, para cada produto: título, marca, preço, estoque, valor total do estoque, quantidade de avaliações e se está em promoção.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# Alterações feitas nos exercícios 3.5 e 3.6 (no notebook elas persistem;
# aqui precisamos repeti-las, pois cada script começa do zero).
dados["products"][0]["stock"] = 80
dados["products"][0]["onSale"] = True

for produto in dados["products"]:
    valor_estoque = produto["price"] * produto["stock"]
    quantidade_avaliacoes = len(produto["reviews"])

    print("Produto:", produto["title"])
    print("Marca:", produto.get("brand", "Não informada"))
    print("Preço: R$", produto["price"])
    print("Estoque:", produto["stock"])
    print("Valor do estoque: R$", round(valor_estoque, 2))
    print("Quantidade de avaliações:", quantidade_avaliacoes)

    if produto.get("onSale", False):
        print("Em promoção: Sim")
    else:
        print("Em promoção: Não")

    print("------------------------------")
