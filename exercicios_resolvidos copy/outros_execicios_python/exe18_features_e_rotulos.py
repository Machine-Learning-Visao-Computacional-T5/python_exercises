"""Exercício 18 — Features e rótulos

Crie X com idade e renda e y com o rótulo comprou.
"""

dataset = [
    {"idade": 22, "renda": 2500, "comprou": 0},
    {"idade": 35, "renda": 5200, "comprou": 1},
    {"idade": 47, "renda": 6800, "comprou": 1},
    {"idade": 29, "renda": 3100, "comprou": 0}
]

X = []
y = []
for registro in dataset:
    X.append([registro["idade"], registro["renda"]])
    y.append(registro["comprou"])
print(X)
print(y)
