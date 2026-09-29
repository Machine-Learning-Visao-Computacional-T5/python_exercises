"""Exercício 7 — Organizando cidades

Crie uma lista com cinco cidades fora da ordem alfabética. Mostre:

- a lista original;
- a lista temporariamente ordenada;
- a lista original novamente;
- a lista permanentemente ordenada.
"""

cidades = [
    "Curitiba",
    "Salvador",
    "Manaus",
    "Brasília",
    "Recife"
]

print("Original:")
print(cidades)

print("Temporariamente ordenada:")
print(sorted(cidades))

print("Original novamente:")
print(cidades)

cidades.sort()

print("Permanentemente ordenada:")
print(cidades)
