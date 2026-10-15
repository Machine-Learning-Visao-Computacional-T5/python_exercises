"""Exercício 1.1 — Salvando os dados em pastas

**Objetivo:** criar pastas e salvar os dados da API em arquivos .json, cada tipo de dado na sua própria pasta (produtos/, usuarios/, carrinhos/).

**Novos conceitos:**

- import os para trabalhar com pastas;
- os.makedirs("pasta", exist_ok=True) cria uma pasta sem dar erro se ela já existir;
- import json e json.dump(dados, arquivo) escrevem um dicionário/lista Python como JSON dentro de um arquivo aberto.
"""

import requests

import os
import json

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
