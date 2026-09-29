"""Exercício 2 — Soma de dois números

Crie um algoritmo que receba dois números, calcule a soma e mostre o resultado.

Pseudocódigo:

    INÍCIO
        LER numero1
        LER numero2
        soma ← numero1 + numero2
        MOSTRAR "Resultado: " + soma
    FIM
"""

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
print("Resultado: " + str(soma))
