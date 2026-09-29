"""Exercício 3 — Busca de um rótulo

Verifique se spam está presente. Resolva percorrendo uma lista e utilizando set. Compare o custo de uma busca e de muitas buscas.
"""

rotulos = ["normal", "normal", "spam", "normal"]

# Solução A — Lista
# Complexidade: O(n) por busca no pior caso
encontrou = "spam" in rotulos
print("Solução A:", encontrou)

# Solução B — Conjunto
# Complexidade: O(n) para construir e O(1) médio por busca
# Para uma única consulta, construir o set pode não compensar; para muitas consultas, tende a compensar.
indice = set(rotulos)
encontrou = "spam" in indice
print("Solução B:", encontrou)
