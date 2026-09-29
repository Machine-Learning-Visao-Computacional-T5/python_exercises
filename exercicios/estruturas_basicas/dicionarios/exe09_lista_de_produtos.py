"""Exercício 9 — Lista de produtos

Crie três dicionários representando produtos. Armazene-os em uma lista e mostre as informações utilizando `for`.
"""

produtos = [
    {
        "nome": "Notebook",
        "preco": 3500.00,
        "estoque": 5
    },
    {
        "nome": "Mouse",
        "preco": 80.00,
        "estoque": 20
    },
    {
        "nome": "Teclado",
        "preco": 150.00,
        "estoque": 12
    }
]

for produto in produtos:
    print(f"Produto: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Estoque: {produto['estoque']}\n")
