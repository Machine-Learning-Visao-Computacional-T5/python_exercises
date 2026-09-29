"""Exercício 10 — Removendo produtos indisponíveis

Remova todas as ocorrências de `"indisponível"`:

produtos = [
    "notebook",
    "indisponível",
    "mouse",
    "indisponível",
    "teclado"
]
"""

produtos = [
    "notebook",
    "indisponível",
    "mouse",
    "indisponível",
    "teclado"
]

while "indisponível" in produtos:
    produtos.remove("indisponível")

print(produtos)
