"""Exercício 10 — Ordenar modelos

Ordene os modelos da maior para a menor acurácia. Compare ordenar toda a lista com localizar apenas o maior valor.
"""

resultados = [
    {"modelo": "Árvore", "acuracia": 0.82},
    {"modelo": "KNN", "acuracia": 0.78},
    {"modelo": "Random Forest", "acuracia": 0.89}
]

# Solução A — Ordenação completa
# Complexidade: O(n log n) tempo
# Necessária quando queremos o ranking completo.
ordenados = sorted(
    resultados,
    key=lambda item: item["acuracia"],
    reverse=True
)
print("Solução A:", ordenados)

# Solução B — Somente o melhor
# Complexidade: O(n) tempo e O(1) espaço adicional
# Preferível quando queremos apenas o máximo.
melhor = max(resultados, key=lambda item: item["acuracia"])
print("Solução B:", melhor)
