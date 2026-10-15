"""Exercício 3 — Reserva de restaurante

Pergunte quantas pessoas fazem parte de um grupo. Se houver mais de oito pessoas, informe que será necessário aguardar. Caso contrário, informe que a mesa está pronta.
"""

quantidade = int(
    input("Quantas pessoas estão no grupo? ")
)

if quantidade > 8:
    print("Será necessário aguardar uma mesa.")
else:
    print("A mesa está pronta.")
