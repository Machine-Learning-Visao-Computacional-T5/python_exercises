"""Exercício 10 — Produtos disponíveis

Considere as listas:

produtos_disponiveis = [
    "notebook",
    "mouse",
    "teclado",
    "monitor"
]

produtos_solicitados = [
    "mouse",
    "impressora",
    "monitor"
]

Informe quais produtos podem ser adicionados ao pedido.
"""

produtos_disponiveis = [
    "notebook",
    "mouse",
    "teclado",
    "monitor"
]

produtos_solicitados = [
    "mouse",
    "impressora",
    "monitor"
]

for produto in produtos_solicitados:
    if produto in produtos_disponiveis:
        print(f"{produto.title()} adicionado ao pedido.")
    else:
        print(f"{produto.title()} não está disponível.")

print("Verificação concluída.")
