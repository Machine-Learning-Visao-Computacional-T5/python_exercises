"""Exercício 3.15 — Tratar uma lista vazia

Objetivo: calcular uma média sem provocar divisão por zero.

Para garantir que todos possam testar esse caso, vamos começar com uma lista de avaliações vazia. Depois, você pode substituir [] por dados["products"][1]["reviews"] e observar o que acontece com o segundo produto dos seus dados.
"""

import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

avaliacoes = []
if len(avaliacoes) > 0:
    soma = 0
    for avaliacao in avaliacoes:
        soma = soma + avaliacao["rating"]
    media = soma / len(avaliacoes)
    print("Média:", media)
else:
    print("Este produto ainda não possui avaliações.")
