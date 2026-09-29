"""Exercício 12 — Média de uma lista

Considere as notas [8, 7, 9, 6, 10]. Calcule e mostre a média.

Pseudocódigo:

    INÍCIO
        notas ← [8, 7, 9, 6, 10]
        soma ← 0
        PARA CADA nota EM notas FAÇA
            soma ← soma + nota
        FIM_PARA
        media ← soma / TAMANHO(notas)
        MOSTRAR "Média: " + media
    FIM
"""

notas = [8, 7, 9, 6, 10]
soma = 0

for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print("Média: " + str(media))
