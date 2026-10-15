"""Exercício 5 — Login simples

Crie duas variáveis: `usuario` e `senha`. O acesso será permitido somente quando o usuário for `"admin"` e a senha for `"1234"`.
"""

usuario = "admin"
senha = "1234"

if usuario == "admin" and senha == "1234":
    print("Acesso permitido.")
else:
    print("Usuário ou senha incorretos.")
