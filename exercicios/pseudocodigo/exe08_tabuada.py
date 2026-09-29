"""Exercício 8 — Tabuada

Crie um algoritmo que receba um número e mostre sua tabuada de 1 a 10.

Pseudocódigo:

    INÍCIO
        LER numero
        PARA multiplicador DE 1 ATÉ 10 FAÇA
            resultado ← numero * multiplicador
            MOSTRAR numero + " × " + multiplicador + " = " + resultado
        FIM_PARA
    FIM
"""

numero = int(input("Digite um número para ver a tabuada: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(str(numero) + " × " + str(multiplicador) + " = " + str(resultado))
