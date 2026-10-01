"""Exercício 9 — Validação de senha

Solicite uma senha. Enquanto ela for diferente de 1234, peça uma nova tentativa. Ao acertar, mostre “Acesso permitido”.

Pseudocódigo:

    INÍCIO
        senha_correta ← "1234"
        LER senha
        ENQUANTO senha != senha_correta FAÇA
            MOSTRAR "Senha incorreta. Tente novamente."
            LER senha
        FIM_ENQUANTO
        MOSTRAR "Acesso permitido"
    FIM
"""

senha_correta = "1234"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")

print("Acesso permitido")
