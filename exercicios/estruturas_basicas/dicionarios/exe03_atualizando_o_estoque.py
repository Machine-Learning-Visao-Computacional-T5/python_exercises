"""Exercício 3 — Atualizando o estoque

O dicionário abaixo representa um produto:

produto = {
    "nome": "Mouse",
    "estoque": 15
}

Considere que três unidades foram vendidas. Atualize o estoque.
"""

produto = {
    "nome": "Mouse",
    "estoque": 15
}

produto["estoque"] -= 3

print(f"Estoque atual: {produto['estoque']}")
