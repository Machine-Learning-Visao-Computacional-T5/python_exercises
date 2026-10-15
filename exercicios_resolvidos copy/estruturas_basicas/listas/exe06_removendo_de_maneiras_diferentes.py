"""Exercício 6 — Removendo de maneiras diferentes

Considere a lista:

animais = ["gato", "cachorro", "coelho", "papagaio"]

Faça as seguintes operações:

1. Remova `"cachorro"` pelo valor.
2. Remova o primeiro elemento com `pop()` e guarde-o em uma variável.
3. Remova o último elemento usando `del`.
"""

animais = ["gato", "cachorro", "coelho", "papagaio"]

animais.remove("cachorro")

animal_removido = animais.pop(0)

del animais[-1]

print(f"Animal retirado com pop: {animal_removido}")
print(f"Lista final: {animais}")
