"""Exercício 4 — Salvando o nome de um usuário

Peça o nome do usuário e salve-o em `convidado.txt`.
"""

from pathlib import Path

nome = input("Digite seu nome: ")

caminho = Path("convidado.txt")
caminho.write_text(
    nome,
    encoding="utf-8"
)

print("Nome salvo com sucesso.")
