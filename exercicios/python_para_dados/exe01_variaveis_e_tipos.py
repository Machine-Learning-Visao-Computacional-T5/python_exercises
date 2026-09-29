"""Exercício 1 — Variáveis e tipos

Identifique o tipo de cada variável e escreva uma frase que apresente o modelo e sua acurácia.
"""

modelo = "Random Forest"
acuracia = 0.87
numero_amostras = 1500
modelo_treinado = True

# modelo é str; acuracia é float; numero_amostras é int; modelo_treinado é bool.
print(type(modelo), type(acuracia), type(numero_amostras), type(modelo_treinado))
print(f"O modelo {modelo} obteve acurácia de {acuracia}.")
