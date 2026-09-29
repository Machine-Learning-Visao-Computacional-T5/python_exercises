"""Desafio — Desconto em camisetas

Uma loja oferece 10% de desconto na compra de cinco camisetas de R$ 40,00 cada. Calcule:

- valor sem desconto;
- valor do desconto;
- valor final.
"""

produto = "Camiseta"
preco = 40.00
quantidade = 5
percentual_desconto = 10

subtotal = preco * quantidade
desconto = subtotal * percentual_desconto / 100
total = subtotal - desconto

print(f"Produto: {produto}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total:.2f}")
