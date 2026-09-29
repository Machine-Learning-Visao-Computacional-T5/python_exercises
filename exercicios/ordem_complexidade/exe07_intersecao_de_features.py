"""Exercício 7 — Interseção de features

Encontre as features presentes nas duas listas. Resolva com dois laços e com conjuntos.
"""

features_a = ["idade", "renda", "cidade", "compras"]
features_b = ["renda", "compras", "score"]

# Solução A — Dois laços
# Complexidade: O(n × m) tempo
comuns = []
for a in features_a:
    for b in features_b:
        if a == b:
            comuns.append(a)
print("Solução A:", comuns)

# Solução B — Conjuntos
# Complexidade: O(n + m) tempo médio e O(n + m) espaço
comuns = set(features_a) & set(features_b)
print("Solução B:", comuns)
