"""Exercício 8 — Mostrando somente números ímpares

Utilize `while` e `continue` para mostrar os números ímpares de 1 até 20.
"""

numero = 0

while numero < 20:
    numero += 1

    if numero % 2 == 0:
        continue

    print(numero)
