"""Exercício 6 — Classificação de desempenho

Use if, elif e else para classificar a acurácia: Excelente para valor maior ou igual a 0.90; Bom para 0.80 ou mais; Regular para 0.70 ou mais; Precisa melhorar nos demais casos. Teste com 0.84.
"""

acuracia = 0.84
if acuracia >= 0.90:
    print("Excelente")
elif acuracia >= 0.80:
    print("Bom")
elif acuracia >= 0.70:
    print("Regular")
else:
    print("Precisa melhorar")
