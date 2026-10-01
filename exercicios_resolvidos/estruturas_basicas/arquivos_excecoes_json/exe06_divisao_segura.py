"""Exercício 6 — Divisão segura

Peça dois números e realize uma divisão. Trate a tentativa de divisão por zero.
"""

numero_1 = float(
    input("Digite o primeiro número: ")
)

numero_2 = float(
    input("Digite o segundo número: ")
)

try:
    resultado = numero_1 / numero_2
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
else:
    print(f"Resultado: {resultado}")
