"""Exercício 11 — Pessoas e lugares favoritos

Crie um dicionário em que cada pessoa possua uma lista de lugares favoritos.
"""

lugares_favoritos = {
    "Ana": ["Curitiba", "Florianópolis"],
    "Bruno": ["São Paulo"],
    "Carla": ["Recife", "Salvador", "Fortaleza"]
}

for pessoa, lugares in lugares_favoritos.items():
    print(f"\nLugares favoritos de {pessoa}:")

    for lugar in lugares:
        print(f"- {lugar}")
