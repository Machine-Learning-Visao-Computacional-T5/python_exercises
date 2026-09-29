"""Exercício 5 — Evitando um KeyError

O dicionário não possui a chave `"telefone"`. Mostre uma mensagem adequada sem produzir erro.
"""

cliente = {
    "nome": "Carlos",
    "email": "carlos@email.com"
}

telefone = cliente.get(
    "telefone",
    "Telefone não informado"
)

print(telefone)
