"""Exercício 12 — Matriz de distâncias

Calcule a distância absoluta entre todos os pares. Qual é a ordem em relação ao número de amostras? É possível evitar cálculos repetidos quando a distância é simétrica?
"""

valores = [2, 5, 9, 12]

# Solução A — Todos os pares
# Complexidade: O(n²) tempo e O(n²) espaço
matriz = []
for a in valores:
    linha = []
    for b in valores:
        linha.append(abs(a - b))
    matriz.append(linha)
print("Solução A:", matriz)

# Solução B — Somente triângulo superior
# Complexidade: O(n²) tempo e aproximadamente metade dos cálculos
# A ordem continua O(n²), embora a constante seja menor.
distancias = {}
for i in range(len(valores)):
    for j in range(i + 1, len(valores)):
        distancias[(i, j)] = abs(valores[i] - valores[j])
print("Solução B:", distancias)
