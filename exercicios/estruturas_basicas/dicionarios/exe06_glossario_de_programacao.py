"""Exercício 6 — Glossário de programação

Crie um dicionário com cinco termos de programação e seus significados. Utilize um `for` para mostrar todos os termos.
"""

glossario = {
    "variável": "Nome que referencia um valor.",
    "lista": "Coleção ordenada de elementos.",
    "dicionário": "Coleção de pares de chave e valor.",
    "condição": "Expressão avaliada como verdadeira ou falsa.",
    "laço": "Estrutura que repete instruções."
}

for termo, significado in glossario.items():
    print(f"{termo.title()}:")
    print(f"  {significado}\n")
