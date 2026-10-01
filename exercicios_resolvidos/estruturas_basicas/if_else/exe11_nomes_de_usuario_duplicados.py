"""Exercício 11 — Nomes de usuário duplicados

Crie uma lista de usuários existentes e outra com novos usuários. Verifique se cada novo nome já está em uso, ignorando diferenças entre letras maiúsculas e minúsculas.
"""

usuarios_atuais = [
    "Ana",
    "Bruno",
    "Carlos",
    "Mariana"
]

novos_usuarios = [
    "PEDRO",
    "ana",
    "Laura",
    "CARLOS"
]

usuarios_minusculos = []

for usuario in usuarios_atuais:
    usuarios_minusculos.append(usuario.lower())

for novo_usuario in novos_usuarios:
    if novo_usuario.lower() in usuarios_minusculos:
        print(
            f"O nome {novo_usuario} já está em uso. "
            "Escolha outro nome."
        )
    else:
        print(f"O nome {novo_usuario} está disponível.")
