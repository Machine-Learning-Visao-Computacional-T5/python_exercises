"""Exercício 9 — Transferência de pedidos

Considere uma lista de pedidos pendentes. Mova cada pedido para uma lista de pedidos concluídos.
"""

pedidos_pendentes = [
    "pedido_101",
    "pedido_102",
    "pedido_103"
]

pedidos_concluidos = []

while pedidos_pendentes:
    pedido = pedidos_pendentes.pop(0)

    print(f"Processando {pedido}.")
    pedidos_concluidos.append(pedido)

print("\nPedidos concluídos:")

for pedido in pedidos_concluidos:
    print(pedido)
