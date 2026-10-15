"""Exercício 6 — Ingredientes de uma pizza

Peça ingredientes até que o usuário digite `"sair"`. Para cada ingrediente, mostre uma confirmação.
"""

while True:
    ingrediente = input(
        "Digite um ingrediente ou 'sair': "
    )

    if ingrediente.lower() == "sair":
        break

    print(
        f"{ingrediente.title()} será adicionado à pizza."
    )

print("Pedido finalizado.")
