"""Exercício 5 — Carrinhos

Busque o carrinho de ID 1 em https://dummyjson.com/carts/1 e imprima quantos produtos diferentes ele tem (len da lista "products") e o valor total ("total").
"""

import requests

url = "https://dummyjson.com/carts/1"
resposta = requests.get(url)
carrinho = resposta.json()

qtd_produtos = len(carrinho["products"])
print("Quantidade de produtos diferentes:", qtd_produtos)
print("Valor total:", carrinho["total"])
