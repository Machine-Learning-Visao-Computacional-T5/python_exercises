"""Exercício 3 — Média das notas

Crie um algoritmo que receba três notas de um aluno, calcule a média e mostre o resultado.

Pseudocódigo:

    INÍCIO
        LER nota1
        LER nota2
        LER nota3
        media ← (nota1 + nota2 + nota3) / 3
        MOSTRAR "Média: " + media
    FIM
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print("Média: " + str(media))
