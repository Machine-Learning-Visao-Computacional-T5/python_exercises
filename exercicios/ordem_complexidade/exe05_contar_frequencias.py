"""Exercício 5 — Contar frequências

Conte quantas vezes cada classe aparece. Resolva com dois laços, com dict e com Counter.
"""

rotulos = [0, 1, 1, 0, 2, 1, 2, 2]

# Solução A — Dois laços
# Complexidade: O(n²) tempo e O(k) espaço
frequencias = {}
for rotulo in rotulos:
    contagem = 0
    for outro in rotulos:
        if outro == rotulo:
            contagem += 1
    frequencias[rotulo] = contagem
print("Solução A:", frequencias)

# Solução B — Dicionário
# Complexidade: O(n) tempo médio e O(k) espaço
frequencias = {}
for rotulo in rotulos:
    frequencias[rotulo] = frequencias.get(rotulo, 0) + 1
print("Solução B:", frequencias)

# Solução C — Counter
# Complexidade: O(n) tempo médio e O(k) espaço
from collections import Counter
frequencias = Counter(rotulos)
print("Solução C:", frequencias)
