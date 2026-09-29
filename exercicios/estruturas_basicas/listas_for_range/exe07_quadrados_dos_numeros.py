"""Exercício 7 — Quadrados dos números

Crie uma lista contendo o quadrado dos números de 1 até 10.
"""

quadrados = []

for numero in range(1, 11):
    quadrado = numero ** 2
    quadrados.append(quadrado)

print(quadrados)
