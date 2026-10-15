"""Exercício 9 — Trabalhando com recortes

Considere a lista:

linguagens = [
    "Python",
    "Java",
    "JavaScript",
    "C",
    "C++",
    "Ruby"
]

Mostre:

- as três primeiras linguagens;
- três linguagens do meio;
- as três últimas linguagens.
"""

linguagens = [
    "Python",
    "Java",
    "JavaScript",
    "C",
    "C++",
    "Ruby"
]

print("Primeiras três:")
print(linguagens[:3])

print("Três do meio:")
print(linguagens[1:4])

print("Últimas três:")
print(linguagens[-3:])
