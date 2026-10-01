"""Exercício 3 — Substituindo palavras

Leia `aprendizado.txt` e substitua `"Python"` por `"Java"` somente na saída. O arquivo original não deve ser modificado.
"""

from pathlib import Path

caminho = Path("aprendizado.txt")

conteudo = caminho.read_text(
    encoding="utf-8"
)

conteudo_modificado = conteudo.replace(
    "Python",
    "Java"
)

print(conteudo_modificado)
