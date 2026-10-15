"""Exercício 12 — Identificando um erro lógico

Observe:

alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(f"Bem-vindo, {aluno}!")
    print("Todos os alunos foram recebidos.")

Por que a segunda mensagem aparece três vezes? Como corrigir?
"""

alunos = ["Ana", "Bruno", "Carla"]

for aluno in alunos:
    print(f"Bem-vindo, {aluno}!")

print("Todos os alunos foram recebidos.")
