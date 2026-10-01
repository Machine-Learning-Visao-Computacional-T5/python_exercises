"""Exercício 9 — Agrupar previsões

Agrupe probabilidades pelo rótulo usando um dicionário cujos valores são listas.
"""

rotulos = ["A", "B", "A", "C", "B"]
probabilidades = [0.91, 0.72, 0.84, 0.66, 0.79]

# Solução A — Dicionário de listas
# Complexidade: O(n) tempo médio e O(n) espaço
grupos = {}
for rotulo, probabilidade in zip(rotulos, probabilidades):
    grupos.setdefault(rotulo, []).append(probabilidade)
print("Solução A:", grupos)
