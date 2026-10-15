"""Exercício 10 — Aluno com várias notas

Crie um dicionário que contenha o nome de um aluno e uma lista de notas. Calcule a média.
"""

aluno = {
    "nome": "Mariana",
    "notas": [8.0, 7.5, 9.0, 8.5]
}

media = sum(aluno["notas"]) / len(aluno["notas"])

print(f"Aluno: {aluno['nome']}")
print(f"Notas: {aluno['notas']}")
print(f"Média: {media:.2f}")
