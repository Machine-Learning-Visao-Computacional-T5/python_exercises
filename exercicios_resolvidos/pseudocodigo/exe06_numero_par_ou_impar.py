"""Exercício 6 — Número par ou ímpar

Crie um algoritmo que receba um número inteiro e informe se ele é par ou ímpar.

Pseudocódigo:

    INÍCIO
        LER numero
        SE numero MOD 2 = 0 ENTÃO
            MOSTRAR "O número é par"
        SENÃO
            MOSTRAR "O número é ímpar"
        FIM_SE
    FIM
"""

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
