"""Exercício 4 — Aprovação do aluno

Crie um algoritmo que receba a média de um aluno. Se a média for maior ou igual a 7, mostre “Aprovado”. Caso contrário, mostre “Reprovado”.

Pseudocódigo:

    INÍCIO
        LER media
        SE media >= 7 ENTÃO
            MOSTRAR "Aprovado"
        SENÃO
            MOSTRAR "Reprovado"
        FIM_SE
    FIM
"""

media = float(input("Digite a média do aluno: "))

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
