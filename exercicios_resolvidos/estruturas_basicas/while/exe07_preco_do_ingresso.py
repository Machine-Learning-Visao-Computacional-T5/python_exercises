"""Exercício 7 — Preço do ingresso

Peça repetidamente a idade dos clientes:

- menos de 3 anos: gratuito;
- de 3 até 12 anos: R$ 10;
- acima de 12 anos: R$ 15.

O usuário pode digitar `"sair"` para encerrar.
"""

while True:
    entrada = input(
        "Digite a idade ou 'sair': "
    )

    if entrada.lower() == "sair":
        break

    idade = int(entrada)

    if idade < 3:
        preco = 0
    elif idade <= 12:
        preco = 10
    else:
        preco = 15

    print(f"Preço do ingresso: R$ {preco:.2f}")
