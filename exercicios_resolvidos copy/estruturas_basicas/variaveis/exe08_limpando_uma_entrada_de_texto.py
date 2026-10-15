"""Exercício 8 — Limpando uma entrada de texto

A variável a seguir contém espaços extras:

linguagem = "   Python   "

Mostre:

- o valor original;
- o valor sem espaços à esquerda;
- o valor sem espaços à direita;
- o valor sem espaços nos dois lados.
"""

linguagem = "   Python   "

print(f"Original: '{linguagem}'")
print(f"Sem espaços à esquerda: '{linguagem.lstrip()}'")
print(f"Sem espaços à direita: '{linguagem.rstrip()}'")
print(f"Sem espaços nos dois lados: '{linguagem.strip()}'")
