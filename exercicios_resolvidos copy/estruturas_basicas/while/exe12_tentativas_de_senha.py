"""Exercício 12 — Tentativas de senha

Defina uma senha correta e permita no máximo três tentativas. Encerre o laço quando a senha estiver correta ou quando as tentativas terminarem.
"""

senha_correta = "python123"
tentativas = 0
limite = 3

while tentativas < limite:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Acesso permitido.")
        break

    tentativas_restantes = limite - tentativas

    if tentativas_restantes > 0:
        print(
            f"Senha incorreta. "
            f"Restam {tentativas_restantes} tentativa(s)."
        )
    else:
        print("Acesso bloqueado.")
