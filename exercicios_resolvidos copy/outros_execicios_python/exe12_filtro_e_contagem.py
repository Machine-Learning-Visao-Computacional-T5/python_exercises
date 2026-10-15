"""Exercício 12 — Filtro e contagem

Apresente somente as acurácias maiores ou iguais a 0.80 e conte quantos modelos atendem ao critério.
"""

acuracias = [0.65, 0.82, 0.91, 0.73, 0.88]

contador = 0
for acuracia in acuracias:
    if acuracia >= 0.80:
        print(acuracia)
        contador += 1
print("Quantidade:", contador)  # 3
