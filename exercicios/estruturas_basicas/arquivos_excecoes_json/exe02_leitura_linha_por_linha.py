"""Exercício 2 — Leitura linha por linha

Leia o mesmo arquivo e mostre as linhas utilizando `for`.
"""

from pathlib import Path

caminho = Path("aprendizado.txt")

conteudo = caminho.read_text(
    encoding="utf-8"
)

for linha in conteudo.splitlines():
    print(linha)
