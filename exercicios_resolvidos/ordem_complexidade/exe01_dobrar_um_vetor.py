"""Exercício 1 — Dobrar um vetor

Dado o vetor abaixo, produza outro vetor com cada valor multiplicado por 2. Resolva com for, compreensão de lista e NumPy.
"""

valores = [2, 5, 8, 11]

# Solução A — Laço
# Complexidade: O(n) tempo e O(n) espaço
dobrados = []
for valor in valores:
    dobrados.append(valor * 2)
print("Solução A:", dobrados)

# Solução B — Compreensão
# Complexidade: O(n) tempo e O(n) espaço
# Mesma ordem, escrita mais compacta.
dobrados = [valor * 2 for valor in valores]
print("Solução B:", dobrados)

# Solução C — NumPy
# Complexidade: O(n) tempo e O(n) espaço para o resultado
# A vetorização reduz o custo interpretado pelo Python, mas não transforma a operação em O(1).
import numpy as np
dobrados = np.array(valores) * 2
print("Solução C:", dobrados)
