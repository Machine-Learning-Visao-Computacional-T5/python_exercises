"""Exercício 9 — Lista vazia

Modifique o exercício anterior para verificar se existem usuários antes de percorrer a lista.
"""

usuarios = []

if usuarios:
    for usuario in usuarios:
        if usuario == "admin":
            print("Olá, admin! Deseja visualizar o relatório?")
        else:
            print(f"Olá, {usuario.title()}!")
else:
    print("Precisamos cadastrar usuários.")
