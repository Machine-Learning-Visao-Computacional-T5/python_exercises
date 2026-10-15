"""Exercício 2 — Listando campos específicos

Percorra a lista de produtos (campo "products") e imprima o título e o preço de cada um.
"""

import requests

url = "https://dummyjson.com/products"
resposta = requests.get(url)
dados = resposta.json()

for produto in dados["products"]:
    print(f'{produto["title"]} - ${produto["price"]}')
