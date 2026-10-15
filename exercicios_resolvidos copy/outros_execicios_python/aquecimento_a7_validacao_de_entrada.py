"""Exercício A7 — Validação de entrada

Solicite uma acurácia. Enquanto o valor estiver fora do intervalo de 0 a 1, informe que ele é inválido e solicite-o novamente.
"""

acuracia = float(input("Digite uma acurácia entre 0 e 1: "))
while acuracia < 0 or acuracia > 1:
    print("Valor inválido")
    acuracia = float(input("Digite novamente: "))
print("Acurácia registrada:", acuracia)
