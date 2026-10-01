"""Exercício 5 — Classificação da nota

Receba a nota de um aluno. Mostre “Aprovado” para nota ≥ 7, “Recuperação” para nota entre 5 e 6,9 e “Reprovado” para nota < 5.

Pseudocódigo:

    INÍCIO
        LER nota
        SE nota >= 7 ENTÃO
            MOSTRAR "Aprovado"
        SENÃO SE nota >= 5 ENTÃO
            MOSTRAR "Recuperação"
        SENÃO
            MOSTRAR "Reprovado"
        FIM_SE
    FIM
"""

nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
