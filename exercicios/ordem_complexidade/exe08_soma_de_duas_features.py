"""Exercício 8 — Soma de duas features

Encontre dois valores cuja soma seja 10. Resolva testando todos os pares e utilizando um conjunto de valores já observados.
"""

valores = [3, 4, 6, 8, 2]

# Solução A — Todos os pares
# Complexidade: O(n²) tempo e O(1) espaço adicional
par = None
for i in range(len(valores)):
    for j in range(i + 1, len(valores)):
        if valores[i] + valores[j] == 10:
            par = (valores[i], valores[j])
            break
    if par:
        break
print("Solução A:", par)

# Solução B — Hash set
# Complexidade: O(n) tempo médio e O(n) espaço
vistos = set()
par = None
for valor in valores:
    complemento = 10 - valor
    if complemento in vistos:
        par = (complemento, valor)
        break
    vistos.add(valor)
print("Solução B:", par)
