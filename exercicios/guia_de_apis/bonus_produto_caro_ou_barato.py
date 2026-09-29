"""Bônus — Produto caro ou barato

Busque o produto de ID 1. Se o preço for maior que 10, imprima "Produto caro"; caso contrário, "Produto barato".
"""

import requests

produto_id = 1
url = f"https://dummyjson.com/products/{produto_id}"

resposta = requests.get(url)
produto = resposta.json()

if produto["price"] > 10:
    print("Produto caro")
else:
    print("Produto barato")
