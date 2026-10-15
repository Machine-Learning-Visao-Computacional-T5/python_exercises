"""Exercício 7 — Tratando entrada inválida

Peça dois números inteiros, some-os e trate o `ValueError` caso o usuário informe texto.
"""

try:
    numero_1 = int(
        input("Digite o primeiro número: ")
    )

    numero_2 = int(
        input("Digite o segundo número: ")
    )
except ValueError:
    print("Informe somente números inteiros.")
else:
    soma = numero_1 + numero_2
    print(f"Resultado: {soma}")
