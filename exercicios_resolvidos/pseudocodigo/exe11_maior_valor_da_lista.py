"""Exercício 11 — Maior valor da lista

Considere a lista [12, 35, 8, 42, 17]. Encontre e mostre o maior valor.

Pseudocódigo:

    INÍCIO
        numeros ← [12, 35, 8, 42, 17]
        maior ← numeros[0]
        PARA CADA numero EM numeros FAÇA
            SE numero > maior ENTÃO
                maior ← numero
            FIM_SE
        FIM_PARA
        MOSTRAR "Maior número: " + maior
    FIM
"""

numeros = [12, 35, 8, 42, 17]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("Maior número: " + str(maior))
