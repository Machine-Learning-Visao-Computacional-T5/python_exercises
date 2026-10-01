"""Exercício 4 — Remover duplicatas

Remova os valores duplicados. Produza uma solução que preserve a ordem original e outra que não garanta a ordem.
"""

classes = [1, 0, 1, 2, 0, 2, 3]

# Solução A — Set direto
# Complexidade: O(n) tempo médio e O(n) espaço
# Não use quando a ordem original precisa ser garantida.
unicos = list(set(classes))
print("Solução A:", unicos)

# Solução B — Dict preservando ordem
# Complexidade: O(n) tempo médio e O(n) espaço
unicos = list(dict.fromkeys(classes))
print("Solução B:", unicos)

# Solução C — Laço e set
# Complexidade: O(n) tempo médio e O(n) espaço
# Torna explícita a regra de preservação da primeira ocorrência.
vistos = set()
unicos = []
for valor in classes:
    if valor not in vistos:
        vistos.add(valor)
        unicos.append(valor)
print("Solução C:", unicos)
