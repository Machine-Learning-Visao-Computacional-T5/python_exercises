"""Exercício 6 — Primeiro elemento repetido

Encontre o primeiro valor que aparece pela segunda vez durante a leitura da esquerda para a direita. Compare uma solução sem set e outra com set.
"""

valores = [4, 2, 7, 5, 2, 4]

# Solução A — Lista de vistos
# Complexidade: O(n²) no pior caso
vistos = []
repetido = None
for valor in valores:
    if valor in vistos:
        repetido = valor
        break
    vistos.append(valor)
print("Solução A:", repetido)

# Solução B — Set de vistos
# Complexidade: O(n) tempo médio e O(n) espaço
vistos = set()
repetido = None
for valor in valores:
    if valor in vistos:
        repetido = valor
        break
    vistos.add(valor)
print("Solução B:", repetido)
