"""Desafio — Lista de espera

Uma turma começa com os seguintes estudantes:

estudantes = ["Ana", "Bruno", "Carla"]

Faça o programa:

1. adicionar `"Daniel"` ao final;
2. inserir `"Eduarda"` no início;
3. substituir `"Bruno"` por `"Bianca"`;
4. remover o último estudante e guardar seu nome;
5. mostrar quem foi removido;
6. ordenar a lista;
7. mostrar a lista final e a quantidade de estudantes.
"""

estudantes = ["Ana", "Bruno", "Carla"]

estudantes.append("Daniel")
estudantes.insert(0, "Eduarda")
estudantes[2] = "Bianca"

estudante_removido = estudantes.pop()

estudantes.sort()

print(f"Estudante removido: {estudante_removido}")
print(f"Lista final: {estudantes}")
print(f"Quantidade de estudantes: {len(estudantes)}")
