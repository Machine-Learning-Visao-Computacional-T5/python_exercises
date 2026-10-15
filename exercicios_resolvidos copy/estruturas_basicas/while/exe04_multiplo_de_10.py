"""Exercício 4 — Múltiplo de 10

Peça um número e informe se ele é múltiplo de 10.
"""

numero = int(input("Digite um número: "))

if numero % 10 == 0:
    print(f"{numero} é múltiplo de 10.")
else:
    print(f"{numero} não é múltiplo de 10.")
