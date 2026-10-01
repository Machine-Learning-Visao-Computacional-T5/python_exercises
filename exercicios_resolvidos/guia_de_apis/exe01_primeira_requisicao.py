"""Exercício 1 — Primeira requisição

Faça uma requisição GET para https://dummyjson.com/products, imprima o código de status da resposta e o total de produtos (campo "total" do JSON).
"""

import requests

url = "https://dummyjson.com/products"

resposta = requests.get(url)
print("Status:", resposta.status_code)

dados = resposta.json()
print("Total de produtos:", dados["total"])
