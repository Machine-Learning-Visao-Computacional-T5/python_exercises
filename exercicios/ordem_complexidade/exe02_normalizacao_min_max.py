"""Exercício 2 — Normalização min-max

Normalize os valores para o intervalo de 0 a 1 usando (x - mínimo) / (máximo - mínimo). Resolva com laço e com NumPy.
"""

valores = [10, 20, 30, 40]

# Solução A — Laço
# Complexidade: O(n) tempo e O(n) espaço
minimo = min(valores)
maximo = max(valores)
normalizados = []
for x in valores:
    normalizados.append((x - minimo) / (maximo - minimo))
print("Solução A:", normalizados)

# Solução B — NumPy
# Complexidade: O(n) tempo e O(n) espaço
import numpy as np
v = np.array(valores, dtype=float)
normalizados = (v - v.min()) / (v.max() - v.min())
print("Solução B:", normalizados)
