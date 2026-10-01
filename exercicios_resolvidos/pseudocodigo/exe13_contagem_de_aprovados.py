"""Exercício 13 — Contagem de aprovados

Considere as notas [8, 4, 7, 9, 5]. Conte quantos alunos possuem nota maior ou igual a 7.

Pseudocódigo:

    INÍCIO
        notas ← [8, 4, 7, 9, 5]
        quantidade_aprovados ← 0
        PARA CADA nota EM notas FAÇA
            SE nota >= 7 ENTÃO
                quantidade_aprovados ← quantidade_aprovados + 1
            FIM_SE
        FIM_PARA
        MOSTRAR "Quantidade de aprovados: " + quantidade_aprovados
    FIM
"""

notas = [8, 4, 7, 9, 5]
quantidade_aprovados = 0

for nota in notas:
    if nota >= 7:
        quantidade_aprovados = quantidade_aprovados + 1

print("Quantidade de aprovados: " + str(quantidade_aprovados))
