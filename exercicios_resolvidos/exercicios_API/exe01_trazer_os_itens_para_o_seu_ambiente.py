"""Exercício 1 — Trazer os itens para o seu ambiente

Objetivo: salvar em arquivos JSON os dados de produtos, usuários e carrinhos da API https://dummyjson.com.
"""

import os
import json
import requests

# Criar as pastas
os.makedirs("produtos", exist_ok=True)
os.makedirs("usuarios", exist_ok=True)
os.makedirs("carrinhos", exist_ok=True)

# --- Produtos ---
resposta = requests.get("https://dummyjson.com/products")
dados_produtos = resposta.json()

with open("produtos/produtos.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_produtos, arquivo, ensure_ascii=False, indent=2)

# --- Usuários ---
resposta = requests.get("https://dummyjson.com/users")
dados_usuarios = resposta.json()

with open("usuarios/usuarios.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_usuarios, arquivo, ensure_ascii=False, indent=2)

# --- Carrinhos ---
resposta = requests.get("https://dummyjson.com/carts")
dados_carrinhos = resposta.json()

with open("carrinhos/carrinhos.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_carrinhos, arquivo, ensure_ascii=False, indent=2)

print("Arquivos salvos!")

for pasta in ["produtos", "usuarios", "carrinhos"]:
    print(f"{pasta}/:", os.listdir(pasta))
