"""Desafio — Sistema de descontos

Uma loja utiliza as seguintes regras:

- compras abaixo de R$ 100 não recebem desconto;
- compras de R$ 100 até menos de R$ 300 recebem 10%;
- compras de R$ 300 até menos de R$ 500 recebem 15%;
- compras a partir de R$ 500 recebem 20%;
- clientes VIP recebem mais 5% de desconto.

Calcule o valor do desconto e o total final.
"""

valor_compra = 450.00
cliente_vip = True

if valor_compra < 100:
    percentual_desconto = 0
elif valor_compra < 300:
    percentual_desconto = 10
elif valor_compra < 500:
    percentual_desconto = 15
else:
    percentual_desconto = 20

if cliente_vip:
    percentual_desconto += 5

valor_desconto = (
    valor_compra * percentual_desconto / 100
)

valor_final = valor_compra - valor_desconto

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Desconto: {percentual_desconto}%")
print(f"Valor descontado: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")
