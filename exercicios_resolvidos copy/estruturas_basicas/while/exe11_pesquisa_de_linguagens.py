"""Exercício 11 — Pesquisa de linguagens

Faça uma pesquisa perguntando o nome e a linguagem de programação favorita de cada pessoa. Armazene as respostas em um dicionário.
"""

respostas = {}
pesquisa_ativa = True

while pesquisa_ativa:
    nome = input("\nDigite seu nome: ")
    linguagem = input(
        "Qual é sua linguagem favorita? "
    )

    respostas[nome] = linguagem

    continuar = input(
        "Outra pessoa responderá? (sim/não): "
    )

    if continuar.lower() == "não":
        pesquisa_ativa = False

print("\nResultados da pesquisa:")

for nome, linguagem in respostas.items():
    print(
        f"{nome} escolheu {linguagem}."
    )
