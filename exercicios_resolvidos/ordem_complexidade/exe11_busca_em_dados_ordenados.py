"""Exercício 11 — Busca em dados ordenados

Localize o valor 42 usando busca linear e busca binária. Explique quando o custo de ordenar os dados precisa ser incluído.
"""

valores = [3, 8, 12, 19, 27, 31, 42, 58]

# Solução A — Busca linear
# Complexidade: O(n) tempo
indice = -1
for i, valor in enumerate(valores):
    if valor == 42:
        indice = i
        break
print("Solução A:", indice)

# Solução B — Busca binária
# Complexidade: O(log n) tempo com dados ordenados
# Se os dados não estiverem ordenados, ordenar primeiro custa O(n log n).
from bisect import bisect_left
i = bisect_left(valores, 42)
indice = i if i < len(valores) and valores[i] == 42 else -1
print("Solução B:", indice)
