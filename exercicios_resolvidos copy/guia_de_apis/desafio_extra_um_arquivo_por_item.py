"""Desafio extra — Um arquivo por item

Em vez de salvar um arquivo só com a lista inteira, salve um arquivo para cada item dentro da pasta (ex.: produto_1.json, produto_2.json...).
"""

import requests

import os
import json

os.makedirs("produtos", exist_ok=True)

resposta = requests.get("https://dummyjson.com/products")
dados_produtos = resposta.json()

for produto in dados_produtos["products"]:
    nome_arquivo = f"produtos/produto_{produto['id']}.json"
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(produto, arquivo, ensure_ascii=False, indent=2)

print("Um arquivo por produto salvo em produtos/")
