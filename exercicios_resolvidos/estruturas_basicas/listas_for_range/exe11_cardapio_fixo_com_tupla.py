"""Exercício 11 — Cardápio fixo com tupla

Um restaurante oferece cinco pratos fixos. Armazene-os em uma tupla e mostre cada prato.

Depois, crie uma nova versão do cardápio, substituindo dois pratos.
"""

cardapio = (
    "arroz",
    "feijão",
    "macarrão",
    "salada",
    "frango"
)

print("Cardápio original:")

for prato in cardapio:
    print(prato)

cardapio = (
    "arroz",
    "feijão",
    "purê de batata",
    "legumes",
    "frango"
)

print("\nNovo cardápio:")

for prato in cardapio:
    print(prato)
