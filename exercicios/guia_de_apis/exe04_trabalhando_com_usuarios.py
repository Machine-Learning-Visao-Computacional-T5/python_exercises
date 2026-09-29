"""Exercício 4 — Trabalhando com usuários

Busque o usuário de ID 10 em https://dummyjson.com/users/10, junte firstName e lastName, e imprima o nome completo e o email.
"""

import requests

url = "https://dummyjson.com/users/10"
resposta = requests.get(url)
usuario = resposta.json()

nome_completo = f'{usuario["firstName"]} {usuario["lastName"]}'
print("Nome completo:", nome_completo)
print("Email:", usuario["email"])
