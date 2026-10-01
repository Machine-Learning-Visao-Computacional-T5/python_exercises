"""Desafio — Sistema de pedidos

Crie um programa que:

1. solicite produtos até o usuário digitar `"finalizar"`;
2. peça a quantidade de cada produto;
3. armazene os produtos e quantidades em um dicionário;
4. ao final, mostre o resumo do pedido.
"""

pedido = {}

while True:
    produto = input(
        "Digite o produto ou 'finalizar': "
    )

    if produto.lower() == "finalizar":
        break

    quantidade = int(
        input("Digite a quantidade: ")
    )

    if produto in pedido:
        pedido[produto] += quantidade
    else:
        pedido[produto] = quantidade

print("\nResumo do pedido:")

if pedido:
    for produto, quantidade in pedido.items():
        print(
            f"{produto.title()}: {quantidade} unidade(s)"
        )
else:
    print("Nenhum produto foi adicionado.")
