"""Exercício 14 — Desafio de decisão

Para 100.000 rótulos e muitas consultas de pertencimento, escolha entre list e set. Explique o custo de construir a estrutura e o custo médio de cada consulta.

Solução: Para muitas consultas, use set. Construí-lo custa O(n) tempo e O(n) memória; cada consulta custa O(1) em média. Consultar diretamente uma lista custa O(n) por consulta. Para q consultas, a lista custa O(qn), enquanto o set custa O(n + q) em média.
"""

import time

rotulos = [f"rotulo_{i}" for i in range(100_000)]
consultas = [f"rotulo_{i}" for i in range(99_000, 100_000)] + ["inexistente"] * 100

# Lista: cada consulta percorre a lista -> O(q * n)
inicio = time.perf_counter()
achados_lista = sum(1 for c in consultas if c in rotulos)
tempo_lista = time.perf_counter() - inicio

# Set: constrói uma vez (O(n)) e cada consulta custa O(1) em média -> O(n + q)
inicio = time.perf_counter()
indice = set(rotulos)
achados_set = sum(1 for c in consultas if c in indice)
tempo_set = time.perf_counter() - inicio

print(f"Lista: {achados_lista} encontrados em {tempo_lista:.4f} s")
print(f"Set:   {achados_set} encontrados em {tempo_set:.4f} s")
