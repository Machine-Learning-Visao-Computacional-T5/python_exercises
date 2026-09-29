# Exercícios de Python — Vetores, tabelas hash e ordem de complexidade

## Sumário

- [Conceitos essenciais](#conceitos-essenciais)
  - [Vetores e arrays](#vetores-e-arrays)
  - [Tabela hash](#tabela-hash)
  - [Ordens de crescimento](#ordens-de-crescimento)
- [Exercícios](#exercícios)
  - [Exercício 1 — Dobrar um vetor](#exercício-1--dobrar-um-vetor)
  - [Exercício 2 — Normalização min-max](#exercício-2--normalização-min-max)
  - [Exercício 3 — Busca de um rótulo](#exercício-3--busca-de-um-rótulo)
  - [Exercício 4 — Remover duplicatas](#exercício-4--remover-duplicatas)
  - [Exercício 5 — Contar frequências](#exercício-5--contar-frequências)
  - [Exercício 6 — Primeiro elemento repetido](#exercício-6--primeiro-elemento-repetido)
  - [Exercício 7 — Interseção de features](#exercício-7--interseção-de-features)
  - [Exercício 8 — Soma de duas features](#exercício-8--soma-de-duas-features)
  - [Exercício 9 — Agrupar previsões](#exercício-9--agrupar-previsões)
  - [Exercício 10 — Ordenar modelos](#exercício-10--ordenar-modelos)
  - [Exercício 11 — Busca em dados ordenados](#exercício-11--busca-em-dados-ordenados)
  - [Exercício 12 — Matriz de distâncias](#exercício-12--matriz-de-distâncias)
  - [Exercício 13 — Valores ausentes por coluna](#exercício-13--valores-ausentes-por-coluna)
  - [Exercício 14 — Desafio de decisão](#exercício-14--desafio-de-decisão)
- [Soluções e comparações](#soluções-e-comparações)
  - [Exercício 1 — Dobrar um vetor](#exercício-1--dobrar-um-vetor-1)
  - [Exercício 2 — Normalização min-max](#exercício-2--normalização-min-max-1)
  - [Exercício 3 — Busca de um rótulo](#exercício-3--busca-de-um-rótulo-1)
  - [Exercício 4 — Remover duplicatas](#exercício-4--remover-duplicatas-1)
  - [Exercício 5 — Contar frequências](#exercício-5--contar-frequências-1)
  - [Exercício 6 — Primeiro elemento repetido](#exercício-6--primeiro-elemento-repetido-1)
  - [Exercício 7 — Interseção de features](#exercício-7--interseção-de-features-1)
  - [Exercício 8 — Soma de duas features](#exercício-8--soma-de-duas-features-1)
  - [Exercício 9 — Agrupar previsões](#exercício-9--agrupar-previsões-1)
  - [Exercício 10 — Ordenar modelos](#exercício-10--ordenar-modelos-1)
  - [Exercício 11 — Busca em dados ordenados](#exercício-11--busca-em-dados-ordenados-1)
  - [Exercício 12 — Matriz de distâncias](#exercício-12--matriz-de-distâncias-1)
  - [Exercício 13 — Valores ausentes por coluna](#exercício-13--valores-ausentes-por-coluna-1)
  - [Exercício 14 — Desafio de decisão](#exercício-14--desafio-de-decisão-1)
- [Resumo das escolhas](#resumo-das-escolhas)

**Vetores, tabelas hash e comparação de soluções por ordem de complexidade**

> **Objetivo.** Resolver o mesmo problema de diferentes maneiras e comparar clareza, tempo e memória. A escolha de uma estrutura de dados pode transformar uma solução quadrática em uma solução linear.

## Como utilizar

1. Resolva cada problema antes de consultar as soluções.
2. Identifique primeiro a solução mais simples, mesmo que ela não seja a mais eficiente.
3. Compare as alternativas usando a **ordem de crescimento**, e não apenas o tempo observado em uma execução pequena.
4. Considere que operações com `dict` e `set` têm custo médio O(1), mas podem chegar a O(n) no pior caso.

## Conceitos essenciais

### Vetores e arrays

Neste material, *vetor* significa uma coleção unidimensional de valores. Uma **lista** Python é flexível e pode conter tipos diferentes. Um **array NumPy** normalmente armazena valores do mesmo tipo e permite operações vetorizadas.

```python
valores = [10, 20, 30]          # lista Python

import numpy as np
vetor = np.array([10, 20, 30])  # array NumPy
print(vetor * 2)                # [20 40 60]
```

### Tabela hash

Uma tabela hash transforma uma chave em uma posição interna por meio de uma função hash. Em Python, `dict` associa chaves a valores e `set` armazena elementos únicos. Isso permite inserção, consulta e remoção em tempo médio O(1).

```python
metricas = {"acuracia": 0.87, "recall": 0.81}
print(metricas["recall"])

classes = {"spam", "normal"}
print("spam" in classes)
```

As chaves precisam ser *hashable*: valores imutáveis como números, strings e tuplas geralmente podem ser chaves; listas não podem. Hash não significa criptografia neste contexto.

### Ordens de crescimento

| Ordem | Exemplo | Para n = 1.000 | Interpretação |
| --- | --- | --- | --- |
| O(1) | Acesso por chave | 1 | Custo constante médio |
| O(log n) | Busca binária | aprox. 10 | Reduz o espaço de busca |
| O(n) | Um laço | 1.000 | Percorre os dados uma vez |
| O(n log n) | Ordenação | aprox. 10.000 | Mais caro que linear |
| O(n²) | Dois laços | 1.000.000 | Crescimento quadrático |

Os números são aproximações didáticas. Big O descreve a tendência dominante e omite constantes e termos menores.

## Exercícios

### Exercício 1 — Dobrar um vetor

Dado o vetor abaixo, produza outro vetor com cada valor multiplicado por 2. Resolva com `for`, compreensão de lista e NumPy.

```python
valores = [2, 5, 8, 11]
```

### Exercício 2 — Normalização min-max

Normalize os valores para o intervalo de 0 a 1 usando `(x - mínimo) / (máximo - mínimo)`. Resolva com laço e com NumPy.

```python
valores = [10, 20, 30, 40]
```

### Exercício 3 — Busca de um rótulo

Verifique se `spam` está presente. Resolva percorrendo uma lista e utilizando `set`. Compare o custo de uma busca e de muitas buscas.

```python
rotulos = ["normal", "normal", "spam", "normal"]
```

### Exercício 4 — Remover duplicatas

Remova os valores duplicados. Produza uma solução que preserve a ordem original e outra que não garanta a ordem.

```python
classes = [1, 0, 1, 2, 0, 2, 3]
```

### Exercício 5 — Contar frequências

Conte quantas vezes cada classe aparece. Resolva com dois laços, com `dict` e com `Counter`.

```python
rotulos = [0, 1, 1, 0, 2, 1, 2, 2]
```

### Exercício 6 — Primeiro elemento repetido

Encontre o primeiro valor que aparece pela segunda vez durante a leitura da esquerda para a direita. Compare uma solução sem `set` e outra com `set`.

```python
valores = [4, 2, 7, 5, 2, 4]
```

### Exercício 7 — Interseção de features

Encontre as features presentes nas duas listas. Resolva com dois laços e com conjuntos.

```python
features_a = ["idade", "renda", "cidade", "compras"]
features_b = ["renda", "compras", "score"]
```

### Exercício 8 — Soma de duas features

Encontre dois valores cuja soma seja 10. Resolva testando todos os pares e utilizando um conjunto de valores já observados.

```python
valores = [3, 4, 6, 8, 2]
```

### Exercício 9 — Agrupar previsões

Agrupe probabilidades pelo rótulo usando um dicionário cujos valores são listas.

```python
rotulos = ["A", "B", "A", "C", "B"]
probabilidades = [0.91, 0.72, 0.84, 0.66, 0.79]
```

### Exercício 10 — Ordenar modelos

Ordene os modelos da maior para a menor acurácia. Compare ordenar toda a lista com localizar apenas o maior valor.

```python
resultados = [
    {"modelo": "Árvore", "acuracia": 0.82},
    {"modelo": "KNN", "acuracia": 0.78},
    {"modelo": "Random Forest", "acuracia": 0.89}
]
```

### Exercício 11 — Busca em dados ordenados

Localize o valor 42 usando busca linear e busca binária. Explique quando o custo de ordenar os dados precisa ser incluído.

```python
valores = [3, 8, 12, 19, 27, 31, 42, 58]
```

### Exercício 12 — Matriz de distâncias

Calcule a distância absoluta entre todos os pares. Qual é a ordem em relação ao número de amostras? É possível evitar cálculos repetidos quando a distância é simétrica?

```python
valores = [2, 5, 9, 12]
```

### Exercício 13 — Valores ausentes por coluna

Conte valores `None` em cada feature usando um dicionário.

```python
dataset = [
    {"idade": 20, "renda": None},
    {"idade": None, "renda": 3000},
    {"idade": 35, "renda": None}
]
```

### Exercício 14 — Desafio de decisão

Para 100.000 rótulos e muitas consultas de pertencimento, escolha entre `list` e `set`. Explique o custo de construir a estrutura e o custo médio de cada consulta.

## Soluções e comparações

As alternativas abaixo produzem resultados equivalentes, mas têm custos e propriedades diferentes. A melhor solução depende do volume de dados, da frequência da operação, da memória disponível e da necessidade de preservar a ordem.

### Exercício 1 — Dobrar um vetor

**Solução A — Laço**

*Complexidade:* O(n) tempo e O(n) espaço.

```python
dobrados = []
for valor in valores:
    dobrados.append(valor * 2)
```

**Solução B — Compreensão**

*Complexidade:* O(n) tempo e O(n) espaço. Mesma ordem, escrita mais compacta.

```python
dobrados = [valor * 2 for valor in valores]
```

**Solução C — NumPy**

*Complexidade:* O(n) tempo e O(n) espaço para o resultado. A vetorização reduz o custo interpretado pelo Python, mas não transforma a operação em O(1).

```python
import numpy as np
dobrados = np.array(valores) * 2
```

### Exercício 2 — Normalização min-max

**Solução A — Laço**

*Complexidade:* O(n) tempo e O(n) espaço.

```python
minimo = min(valores)
maximo = max(valores)
normalizados = []
for x in valores:
    normalizados.append((x - minimo) / (maximo - minimo))
```

**Solução B — NumPy**

*Complexidade:* O(n) tempo e O(n) espaço.

```python
import numpy as np
v = np.array(valores, dtype=float)
normalizados = (v - v.min()) / (v.max() - v.min())
```

### Exercício 3 — Busca de um rótulo

**Solução A — Lista**

*Complexidade:* O(n) por busca no pior caso.

```python
encontrou = "spam" in rotulos
```

**Solução B — Conjunto**

*Complexidade:* O(n) para construir e O(1) médio por busca. Para uma única consulta, construir o `set` pode não compensar; para muitas consultas, tende a compensar.

```python
indice = set(rotulos)
encontrou = "spam" in indice
```

### Exercício 4 — Remover duplicatas

**Solução A — Set direto**

*Complexidade:* O(n) tempo médio e O(n) espaço. Não use quando a ordem original precisa ser garantida.

```python
unicos = list(set(classes))
```

**Solução B — Dict preservando ordem**

*Complexidade:* O(n) tempo médio e O(n) espaço.

```python
unicos = list(dict.fromkeys(classes))
```

**Solução C — Laço e set**

*Complexidade:* O(n) tempo médio e O(n) espaço. Torna explícita a regra de preservação da primeira ocorrência.

```python
vistos = set()
unicos = []
for valor in classes:
    if valor not in vistos:
        vistos.add(valor)
        unicos.append(valor)
```

### Exercício 5 — Contar frequências

**Solução A — Dois laços**

*Complexidade:* O(n²) tempo e O(k) espaço.

```python
frequencias = {}
for rotulo in rotulos:
    contagem = 0
    for outro in rotulos:
        if outro == rotulo:
            contagem += 1
    frequencias[rotulo] = contagem
```

**Solução B — Dicionário**

*Complexidade:* O(n) tempo médio e O(k) espaço.

```python
frequencias = {}
for rotulo in rotulos:
    frequencias[rotulo] = frequencias.get(rotulo, 0) + 1
```

**Solução C — Counter**

*Complexidade:* O(n) tempo médio e O(k) espaço.

```python
from collections import Counter
frequencias = Counter(rotulos)
```

### Exercício 6 — Primeiro elemento repetido

**Solução A — Lista de vistos**

*Complexidade:* O(n²) no pior caso.

```python
vistos = []
repetido = None
for valor in valores:
    if valor in vistos:
        repetido = valor
        break
    vistos.append(valor)
```

**Solução B — Set de vistos**

*Complexidade:* O(n) tempo médio e O(n) espaço.

```python
vistos = set()
repetido = None
for valor in valores:
    if valor in vistos:
        repetido = valor
        break
    vistos.add(valor)
```

### Exercício 7 — Interseção de features

**Solução A — Dois laços**

*Complexidade:* O(n × m) tempo.

```python
comuns = []
for a in features_a:
    for b in features_b:
        if a == b:
            comuns.append(a)
```

**Solução B — Conjuntos**

*Complexidade:* O(n + m) tempo médio e O(n + m) espaço.

```python
comuns = set(features_a) & set(features_b)
```

### Exercício 8 — Soma de duas features

**Solução A — Todos os pares**

*Complexidade:* O(n²) tempo e O(1) espaço adicional.

```python
par = None
for i in range(len(valores)):
    for j in range(i + 1, len(valores)):
        if valores[i] + valores[j] == 10:
            par = (valores[i], valores[j])
            break
    if par:
        break
```

**Solução B — Hash set**

*Complexidade:* O(n) tempo médio e O(n) espaço.

```python
vistos = set()
par = None
for valor in valores:
    complemento = 10 - valor
    if complemento in vistos:
        par = (complemento, valor)
        break
    vistos.add(valor)
```

### Exercício 9 — Agrupar previsões

**Solução — Dicionário de listas**

*Complexidade:* O(n) tempo médio e O(n) espaço.

```python
grupos = {}
for rotulo, probabilidade in zip(rotulos, probabilidades):
    grupos.setdefault(rotulo, []).append(probabilidade)
```

### Exercício 10 — Ordenar modelos

**Solução A — Ordenação completa**

*Complexidade:* O(n log n) tempo. Necessária quando queremos o ranking completo.

```python
ordenados = sorted(
    resultados,
    key=lambda item: item["acuracia"],
    reverse=True
)
```

**Solução B — Somente o melhor**

*Complexidade:* O(n) tempo e O(1) espaço adicional. Preferível quando queremos apenas o máximo.

```python
melhor = max(resultados, key=lambda item: item["acuracia"])
```

### Exercício 11 — Busca em dados ordenados

**Solução A — Busca linear**

*Complexidade:* O(n) tempo.

```python
indice = -1
for i, valor in enumerate(valores):
    if valor == 42:
        indice = i
        break
```

**Solução B — Busca binária**

*Complexidade:* O(log n) tempo com dados ordenados. Se os dados não estiverem ordenados, ordenar primeiro custa O(n log n).

```python
from bisect import bisect_left
i = bisect_left(valores, 42)
indice = i if i < len(valores) and valores[i] == 42 else -1
```

### Exercício 12 — Matriz de distâncias

**Solução A — Todos os pares**

*Complexidade:* O(n²) tempo e O(n²) espaço.

```python
matriz = []
for a in valores:
    linha = []
    for b in valores:
        linha.append(abs(a - b))
    matriz.append(linha)
```

**Solução B — Somente triângulo superior**

*Complexidade:* O(n²) tempo e aproximadamente metade dos cálculos. A ordem continua O(n²), embora a constante seja menor.

```python
distancias = {}
for i in range(len(valores)):
    for j in range(i + 1, len(valores)):
        distancias[(i, j)] = abs(valores[i] - valores[j])
```

### Exercício 13 — Valores ausentes por coluna

**Solução — Contagem por chave**

*Complexidade:* O(n × f) tempo e O(f) espaço. `f` representa a quantidade de features por registro.

```python
ausentes = {}
for registro in dataset:
    for feature, valor in registro.items():
        if valor is None:
            ausentes[feature] = ausentes.get(feature, 0) + 1
        else:
            ausentes.setdefault(feature, 0)
```

### Exercício 14 — Desafio de decisão

Para muitas consultas, use `set`. Construí-lo custa O(n) tempo e O(n) memória; cada consulta custa O(1) em média. Consultar diretamente uma lista custa O(n) por consulta. Para `q` consultas, a lista custa O(qn), enquanto o `set` custa O(n + q) em média.

## Resumo das escolhas

- Use **lista** quando a ordem e as posições importam e o conjunto é pequeno ou pouco consultado.
- Use **set** para unicidade, pertencimento e operações de conjuntos.
- Use **dict** para associar chaves a valores, contar ocorrências e agrupar registros.
- Use **NumPy** para operações numéricas vetorizadas, sem confundir vetorização com mudança automática da ordem Big O.
- Não ordene em O(n log n) quando uma única passagem O(n) resolve o objetivo.
- Uma otimização pode reduzir constantes sem alterar a ordem, como calcular apenas metade de uma matriz simétrica.
