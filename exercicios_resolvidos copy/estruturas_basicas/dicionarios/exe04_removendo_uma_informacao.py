"""Exercício 4 — Removendo uma informação

Remova a chave `"senha"` do dicionário antes de exibi-lo.
"""

usuario = {
    "nome": "Ana",
    "email": "ana@email.com",
    "senha": "123456"
}

del usuario["senha"]

print(usuario)
