"""Exercício 10 — Mini cadastro de produto

Crie variáveis para armazenar:

- nome do produto;
- preço unitário;
- quantidade;
- disponibilidade.

Calcule o valor total do estoque e mostre uma ficha organizada.
"""

produto = "Teclado"
preco = 120.00
quantidade = 8
disponivel = True

valor_estoque = preco * quantidade

print("DADOS DO PRODUTO")
print(f"\tProduto: {produto}")
print(f"\tPreço: R$ {preco:.2f}")
print(f"\tQuantidade: {quantidade}")
print(f"\tDisponível: {disponivel}")
print(f"\tValor do estoque: R$ {valor_estoque:.2f}")
