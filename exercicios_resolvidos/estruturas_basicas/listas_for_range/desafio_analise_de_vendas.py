"""Desafio — Análise de vendas

Uma loja registrou as vendas dos últimos sete dias:

vendas = [1200, 950, 1430, 870, 1600, 1100, 1350]

Crie um programa que:

1. mostre cada venda;
2. apresente a maior e a menor venda;
3. calcule o total;
4. calcule a média;
5. mostre as vendas dos três primeiros dias;
6. crie uma cópia da lista;
7. adicione uma nova venda somente à cópia.
"""

vendas = [1200, 950, 1430, 870, 1600, 1100, 1350]

print("Vendas registradas:")

for venda in vendas:
    print(f"R$ {venda:.2f}")

maior_venda = max(vendas)
menor_venda = min(vendas)
total_vendas = sum(vendas)
media_vendas = total_vendas / len(vendas)

print(f"\nMaior venda: R$ {maior_venda:.2f}")
print(f"Menor venda: R$ {menor_venda:.2f}")
print(f"Total vendido: R$ {total_vendas:.2f}")
print(f"Média de vendas: R$ {media_vendas:.2f}")

print("\nVendas dos três primeiros dias:")
print(vendas[:3])

copia_vendas = vendas[:]
copia_vendas.append(1700)

print("\nLista original:")
print(vendas)

print("Cópia atualizada:")
print(copia_vendas)
