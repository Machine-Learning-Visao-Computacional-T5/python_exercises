"""Exercício 7 — Números favoritos

Crie um dicionário que relacione cinco pessoas aos seus números favoritos. Mostre uma mensagem para cada pessoa.
"""

numeros_favoritos = {
    "Ana": 7,
    "Bruno": 10,
    "Carla": 3,
    "Daniel": 21,
    "Eduarda": 8
}

for pessoa, numero in numeros_favoritos.items():
    print(
        f"O número favorito de {pessoa} é {numero}."
    )
