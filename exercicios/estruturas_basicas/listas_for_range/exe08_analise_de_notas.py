"""Exercício 8 — Análise de notas

Considere as notas:

notas = [7.5, 8.0, 6.5, 9.5, 8.5]

Mostre:

- menor nota;
- maior nota;
- soma das notas;
- média;
- quantidade de notas.
"""

notas = [7.5, 8.0, 6.5, 9.5, 8.5]

menor_nota = min(notas)
maior_nota = max(notas)
soma_notas = sum(notas)
quantidade = len(notas)
media = soma_notas / quantidade

print(f"Menor nota: {menor_nota}")
print(f"Maior nota: {maior_nota}")
print(f"Soma das notas: {soma_notas}")
print(f"Média: {media:.2f}")
print(f"Quantidade de notas: {quantidade}")
