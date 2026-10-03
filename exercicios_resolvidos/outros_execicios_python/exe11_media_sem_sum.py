"""Exercício 11 — Média sem sum

Calcule a média usando uma estrutura de repetição, sem utilizar sum().
"""

acuracias = [0.78, 0.84, 0.91, 0.87]

total = 0
for acuracia in acuracias:
    total += acuracia
media = total / len(acuracias)
print(media)  # 0.85
