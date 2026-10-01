"""Exercício 10 — Soma dos valores de uma lista

Considere a lista [10, 20, 30, 40]. Percorra a lista, some todos os valores e mostre o resultado.

Pseudocódigo:

    INÍCIO
        numeros ← [10, 20, 30, 40]
        soma ← 0
        PARA CADA numero EM numeros FAÇA
            soma ← soma + numero
        FIM_PARA
        MOSTRAR "Soma: " + soma
    FIM
"""

numeros = [10, 20, 30, 40]
soma = 0

for numero in numeros:
    soma = soma + numero

print("Soma: " + str(soma))
