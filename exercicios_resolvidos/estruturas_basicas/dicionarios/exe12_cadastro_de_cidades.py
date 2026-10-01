"""Exercício 12 — Cadastro de cidades

Crie um dicionário no qual cada cidade esteja relacionada a outro dicionário com país, população e uma curiosidade.
"""

cidades = {
    "Curitiba": {
        "pais": "Brasil",
        "populacao": 1_770_000,
        "curiosidade": "É a capital do Paraná."
    },
    "Paris": {
        "pais": "França",
        "populacao": 2_100_000,
        "curiosidade": "É conhecida pela Torre Eiffel."
    },
    "Tóquio": {
        "pais": "Japão",
        "populacao": 14_000_000,
        "curiosidade": "É uma das maiores cidades do mundo."
    }
}

for cidade, informacoes in cidades.items():
    print(f"\nCidade: {cidade}")
    print(f"País: {informacoes['pais']}")
    print(f"População: {informacoes['populacao']}")
    print(f"Curiosidade: {informacoes['curiosidade']}")
