"""Exercício 1 — Leitura completa

Crie um arquivo chamado `aprendizado.txt` com três frases sobre Python. Depois, crie um programa que leia e mostre todo o conteúdo.

Conteúdo de `aprendizado.txt`:

Python permite criar variáveis.
Python permite trabalhar com listas.
Python permite automatizar tarefas.
"""

from pathlib import Path

caminho = Path("aprendizado.txt")

conteudo = caminho.read_text(
    encoding="utf-8"
).rstrip()

print(conteudo)
