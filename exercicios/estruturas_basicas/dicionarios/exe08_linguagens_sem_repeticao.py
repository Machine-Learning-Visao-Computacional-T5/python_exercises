"""Exercício 8 — Linguagens sem repetição

Considere a pesquisa:

linguagens = {
    "Ana": "Python",
    "Bruno": "Java",
    "Carla": "Python",
    "Daniel": "C",
    "Eduarda": "Java"
}

Mostre todas as linguagens mencionadas sem repetições.
"""

linguagens = {
    "Ana": "Python",
    "Bruno": "Java",
    "Carla": "Python",
    "Daniel": "C",
    "Eduarda": "Java"
}

print("Linguagens mencionadas:")

for linguagem in set(linguagens.values()):
    print(linguagem)
