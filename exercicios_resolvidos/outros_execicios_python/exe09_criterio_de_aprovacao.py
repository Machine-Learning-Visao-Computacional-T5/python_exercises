"""Exercício 9 — Critério de aprovação

Um modelo é aprovado quando a acurácia de teste é pelo menos 0.80 e a diferença entre treino e teste não ultrapassa 0.10. Implemente a regra.
"""

acuracia_treino = 0.87
acuracia_teste = 0.82

diferenca = acuracia_treino - acuracia_teste
if acuracia_teste >= 0.80 and diferenca <= 0.10:
    print("Modelo aprovado")
else:
    print("Modelo não aprovado")
