"""Exercício 10 — Cópia independente

Crie uma lista de comidas favoritas e faça uma cópia para um amigo. Adicione um alimento diferente em cada lista e mostre os resultados.
"""

minhas_comidas = ["pizza", "lasanha", "sushi"]

comidas_amigo = minhas_comidas[:]

minhas_comidas.append("hambúrguer")
comidas_amigo.append("sorvete")

print("Minhas comidas:")
for comida in minhas_comidas:
    print(comida)

print("\nComidas do meu amigo:")
for comida in comidas_amigo:
    print(comida)
