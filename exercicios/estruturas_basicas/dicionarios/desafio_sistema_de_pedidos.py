"""Desafio — Sistema de pedidos

Crie um pedido contendo:

- número do pedido;
- nome do cliente;
- lista de produtos;
- situação do pedido.

Depois:

1. mostre os dados do pedido;
2. percorra e mostre os produtos;
3. altere a situação para `"enviado"`;
4. tente acessar uma chave opcional chamada `"cupom"` usando `get()`.
"""

pedido = {
    "numero": 1001,
    "cliente": "Ana",
    "produtos": [
        {
            "nome": "Notebook",
            "preco": 3500.00,
            "quantidade": 1
        },
        {
            "nome": "Mouse",
            "preco": 80.00,
            "quantidade": 2
        }
    ],
    "situacao": "em preparação"
}

print(f"Pedido: {pedido['numero']}")
print(f"Cliente: {pedido['cliente']}")
print(f"Situação: {pedido['situacao']}")

total = 0

print("\nProdutos:")

for produto in pedido["produtos"]:
    subtotal = produto["preco"] * produto["quantidade"]
    total += subtotal

    print(f"- {produto['nome']}")
    print(f"  Quantidade: {produto['quantidade']}")
    print(f"  Subtotal: R$ {subtotal:.2f}")

pedido["situacao"] = "enviado"

cupom = pedido.get("cupom", "Nenhum cupom utilizado")

print(f"\nTotal: R$ {total:.2f}")
print(f"Nova situação: {pedido['situacao']}")
print(f"Cupom: {cupom}")
