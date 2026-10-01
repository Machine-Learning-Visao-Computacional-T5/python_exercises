"""Exercício 4 — Classificação da nota

Classifique a nota utilizando as seguintes regras:

- de 9 até 10: excelente;
- de 7 até menos de 9: aprovado;
- de 5 até menos de 7: recuperação;
- abaixo de 5: reprovado.
"""

nota = 6.5

if nota >= 9:
    resultado = "Excelente"
elif nota >= 7:
    resultado = "Aprovado"
elif nota >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

print(f"Resultado: {resultado}")
