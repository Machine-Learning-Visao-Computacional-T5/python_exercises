"""Exercício 5 — Livro de convidados

Solicite nomes até o usuário digitar `"sair"`. Depois, grave todos os nomes em `convidados.txt`, um por linha.
"""

from pathlib import Path

nomes = []

while True:
    nome = input(
        "Digite um nome ou 'sair': "
    )

    if nome.lower() == "sair":
        break

    nomes.append(nome)

conteudo = ""

for nome in nomes:
    conteudo += f"{nome}\n"

caminho = Path("convidados.txt")
caminho.write_text(
    conteudo,
    encoding="utf-8"
)

print("Lista de convidados salva.")
