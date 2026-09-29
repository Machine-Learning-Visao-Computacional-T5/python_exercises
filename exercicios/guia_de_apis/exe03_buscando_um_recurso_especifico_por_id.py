"""Exercício 3 — Buscando um recurso específico por ID

Busque o produto de ID 5 em https://dummyjson.com/products/5 e imprima nome, categoria e estoque.
"""

import requests

produto_id = 5
url = f"https://dummyjson.com/products/{produto_id}"

resposta = requests.get(url)
produto = resposta.json()

print("Nome:", produto["title"])
print("Categoria:", produto["category"])
print("Estoque:", produto["stock"])
