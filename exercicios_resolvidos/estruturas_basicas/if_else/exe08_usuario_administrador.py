"""Exercício 8 — Usuário administrador

Crie uma lista com usuários, incluindo `"admin"`. Mostre uma mensagem especial para o administrador e uma mensagem comum para os demais usuários.
"""

usuarios = ["ana", "bruno", "admin", "carla"]

for usuario in usuarios:
    if usuario == "admin":
        print(
            "Olá, admin! Deseja visualizar o relatório do sistema?"
        )
    else:
        print(f"Olá, {usuario.title()}! Bem-vindo novamente.")
