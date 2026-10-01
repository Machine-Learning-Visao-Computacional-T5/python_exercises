"""Exercício 10 — Lista de compras

Crie uma lista com três produtos. Depois:

1. adicione um produto no final;
2. insira um produto no início;
3. substitua o terceiro produto;
4. remova um produto pelo valor;
5. mostre a lista em ordem alfabética;
6. mostre a quantidade final de produtos.
"""

compras = ["arroz", "feijão", "leite"]

compras.append("café")
compras.insert(0, "pão")
compras[2] = "macarrão"
compras.remove("leite")

compras.sort()

print("Lista de compras:")
print(compras)

print(f"Quantidade de produtos: {len(compras)}")
