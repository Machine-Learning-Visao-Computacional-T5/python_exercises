# Exercícios — Funções

*1 de out. de 2026 · @hellen*

---

## Como usar

São **15 exercícios em 2 partes**, do mais simples ao desafio final que junta tudo.

**Níveis:**

| Nível | Significado |
|---|---|
| **[Básico]** | aplica um conceito |
| **[Intermediário]** | combina conceitos |
| **[Desafio]** | problema aberto |

**Confira a sua resposta.** Cada exercício traz exemplos no formato `chamada → resultado esperado`. Rode a chamada com `print` e compare com o resultado esperado:

```python
def dobro(x):
    return x * 2

print(dobro(4))    # esperado: 8
print(dobro(0))    # esperado: 0
```

> **Regras do jogo:** use `return` (não `print`) para devolver o resultado, dê nomes que digam o que a função faz e escreva uma docstring curta em cada função.

> **Resolução:** cada exercício traz a resolução logo abaixo. Tente resolver antes de olhar; depois compare com a sua e leia os comentários do código.

---

## Parte 1 — Definição de funções

### 1.1 `[Básico]` Saudação

Crie `saudacao(nome)` que devolve uma frase de boas-vindas.

- `saudacao("Ana")` → `'Olá, Ana!'`

<details>
<summary><strong>Resolução</strong></summary>

```python
def saudacao(nome):
    """Devolve uma frase de boas-vindas."""
    return f"Olá, {nome}!"

print(saudacao("Ana"))   # Olá, Ana!
```

</details>

### 1.2 `[Básico]` Área do retângulo

Crie `area_retangulo(base, altura)`.

- `area_retangulo(3, 4)` → `12`

<details>
<summary><strong>Resolução</strong></summary>

```python
def area_retangulo(base, altura):
    """Devolve a área de um retângulo."""
    return base * altura

print(area_retangulo(3, 4))   # 12
```

</details>

### 1.3 `[Básico]` Par ou ímpar

Crie `eh_par(n)` que devolve `True` se o número for par e `False` se for ímpar.

> **Dica:** o operador `%` dá o resto da divisão.

- `eh_par(10)` → `True`
- `eh_par(7)` → `False`

<details>
<summary><strong>Resolução</strong></summary>

```python
def eh_par(n):
    """True se n for par, False se for ímpar."""
    return n % 2 == 0     # a comparação já é True ou False: não precisa de if

print(eh_par(10))   # True
print(eh_par(7))    # False
```

</details>

### 1.4 `[Intermediário]` Temperatura

Crie `celsius_para_fahrenheit(c)`. A fórmula é `F = C × 9 / 5 + 32`.

- `celsius_para_fahrenheit(100)` → `212.0`
- `celsius_para_fahrenheit(0)` → `32.0`
- `celsius_para_fahrenheit(-40)` → `-40.0` *(curiosidade: as duas escalas se encontram aqui)*

<details>
<summary><strong>Resolução</strong></summary>

```python
def celsius_para_fahrenheit(c):
    """Converte Celsius para Fahrenheit."""
    return c * 9 / 5 + 32

print(celsius_para_fahrenheit(100))   # 212.0
print(celsius_para_fahrenheit(0))     # 32.0
print(celsius_para_fahrenheit(-40))   # -40.0
```

</details>

### 1.5 `[Intermediário]` Situação do aluno

Crie `classificar_nota(nota)` com docstring. Devolva `"Aprovado"` para nota a partir de 7, `"Recuperação"` de 5 até menos de 7 e `"Reprovado"` abaixo de 5.

- `classificar_nota(8.5)` → `'Aprovado'`
- `classificar_nota(5)` → `'Recuperação'`
- `classificar_nota(4.9)` → `'Reprovado'`

<details>
<summary><strong>Resolução</strong></summary>

```python
def classificar_nota(nota):
    """Aprovado (>= 7), Recuperação (>= 5) ou Reprovado."""
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    return "Reprovado"    # o return encerra a função: não precisa de else

print(classificar_nota(8.5))   # Aprovado
print(classificar_nota(5))     # Recuperação
print(classificar_nota(4.9))   # Reprovado
```

</details>

### 1.6 `[Intermediário]` Contar vogais

Crie `contar_vogais(texto)`, que conta quantas vogais o texto tem, incluindo as acentuadas.

> **Dica:** percorra o texto com `for` e use `.lower()`.

- `contar_vogais("Python para dados")` → `5`
- `contar_vogais("Ação")` → `3`
- `contar_vogais("xyz")` → `0`

<details>
<summary><strong>Resolução</strong></summary>

```python
def contar_vogais(texto):
    """Conta as vogais do texto, com ou sem acento."""
    total = 0
    for letra in texto.lower():
        if letra in "aeiouáéíóúâêôãõ":
            total += 1
    return total          # o return fica FORA do for, depois de contar tudo

print(contar_vogais("Python para dados"))   # 5
print(contar_vogais("Ação"))                # 3
print(contar_vogais("xyz"))                 # 0
```

</details>

### 1.7 `[Intermediário]` O maior de três

Crie `maior_de_tres(a, b, c)` sem usar `max`.

- `maior_de_tres(3, 9, 5)` → `9`
- `maior_de_tres(7, 2, 7)` → `7`
- `maior_de_tres(-1, -5, -3)` → `-1`

<details>
<summary><strong>Resolução</strong></summary>

```python
def maior_de_tres(a, b, c):
    """Devolve o maior entre três números."""
    maior = a             # começa supondo que o primeiro é o maior
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior

print(maior_de_tres(3, 9, 5))     # 9
print(maior_de_tres(7, 2, 7))     # 7
print(maior_de_tres(-1, -5, -3))  # -1
```

</details>

---

## Parte 2 — Parâmetros e retorno

### 2.1 `[Básico]` IMC

Crie `calcular_imc(peso, altura)` que devolve o IMC (peso ÷ altura²) arredondado em 1 casa com `round`.

- `calcular_imc(70, 1.75)` → `22.9`
- `calcular_imc(55, 1.60)` → `21.5`

<details>
<summary><strong>Resolução</strong></summary>

```python
def calcular_imc(peso, altura):
    """Devolve o IMC com 1 casa decimal."""
    return round(peso / altura ** 2, 1)    # ** 2 = ao quadrado

print(calcular_imc(70, 1.75))   # 22.9
print(calcular_imc(55, 1.60))   # 21.5
```

</details>

### 2.2 `[Básico]` Valor padrão

Crie `potencia(base, expoente=2)`. Se o expoente não for informado, eleva ao quadrado.

- `potencia(3)` → `9`
- `potencia(2, 10)` → `1024`
- `potencia(expoente=3, base=2)` → `8` *(argumentos nomeados, em outra ordem)*

<details>
<summary><strong>Resolução</strong></summary>

```python
def potencia(base, expoente=2):     # o parâmetro com valor padrão vem por último
    """Eleva a base ao expoente (padrão: ao quadrado)."""
    return base ** expoente

print(potencia(3))                    # 9
print(potencia(2, 10))                # 1024
print(potencia(expoente=3, base=2))   # 8
```

</details>

### 2.3 `[Intermediário]` Preço final

Crie `preco_final(preco, desconto=0, frete=0)`, com o desconto em %. Primeiro aplica o desconto, depois soma o frete.

- `preco_final(100)` → `100.0`
- `preco_final(100, desconto=10)` → `90.0`
- `preco_final(100, frete=15, desconto=10)` → `105.0`

<details>
<summary><strong>Resolução</strong></summary>

```python
def preco_final(preco, desconto=0, frete=0):
    """Aplica o desconto (%) e depois soma o frete."""
    return preco * (1 - desconto / 100) + frete

print(preco_final(100))                          # 100.0
print(preco_final(100, desconto=10))             # 90.0
print(preco_final(100, frete=15, desconto=10))   # 105.0
```

</details>

### 2.4 `[Intermediário]` Vários retornos

Crie `estatisticas(numeros)` que recebe uma lista e devolve o menor, o maior e a média de uma vez. Use desempacotamento para receber os três valores.

- `estatisticas([7, 9, 8])` → `(7, 9, 8.0)`
- `mn, mx, md = estatisticas([3, 10, 5])` → `mn` vale `3`, `mx` vale `10`, `md` vale `6.0`

<details>
<summary><strong>Resolução</strong></summary>

```python
def estatisticas(numeros):
    """Devolve (menor, maior, média) de uma lista."""
    return min(numeros), max(numeros), sum(numeros) / len(numeros)   # volta uma tupla

print(estatisticas([7, 9, 8]))        # (7, 9, 8.0)
mn, mx, md = estatisticas([3, 10, 5])  # desempacotamento: um valor para cada variável
print(mn, mx, md)                      # 3 10 6.0
```

</details>

### 2.5 `[Intermediário]` Quantidade livre de notas

Crie `media(*notas)` que aceita qualquer quantidade de notas e devolve a média arredondada em 2 casas. Se nenhuma nota for passada, devolve `0`.

- `media(7, 8, 9)` → `8.0`
- `media(10)` → `10.0`
- `media()` → `0`

<details>
<summary><strong>Resolução</strong></summary>

```python
def media(*notas):             # *notas junta todos os valores numa tupla
    """Média de qualquer quantidade de notas; 0 se não houver nenhuma."""
    if not notas:              # tupla vazia conta como False
        return 0
    return round(sum(notas) / len(notas), 2)

print(media(7, 8, 9))   # 8.0
print(media(10))        # 10.0
print(media())          # 0
```

</details>

### 2.6 `[Intermediário]` Cadastro flexível

Crie `cadastro(nome, **info)` que monta um texto com o nome e todas as informações extras, separadas por `" | "`.

- `cadastro("Ana", idade=21, cidade="Curitiba")` → `'Ana | idade: 21 | cidade: Curitiba'`
- `cadastro("Bruno")` → `'Bruno'`

<details>
<summary><strong>Resolução</strong></summary>

```python
def cadastro(nome, **info):    # **info junta os argumentos nomeados num dicionário
    """Monta um texto com o nome e as informações extras."""
    partes = [nome]
    for chave, valor in info.items():
        partes.append(f"{chave}: {valor}")
    return " | ".join(partes)

print(cadastro("Ana", idade=21, cidade="Curitiba"))   # Ana | idade: 21 | cidade: Curitiba
print(cadastro("Bruno"))                              # Bruno
```

</details>

### 2.7 `[Desafio]` Conversor com validação

Crie `converter_temperatura(valor, de="C", para="F")`, que converte entre C, F e K e arredonda em 2 casas. Se uma unidade for inválida, levante `ValueError("Unidade inválida: use C, F ou K")`.

> **Dica:** converta tudo primeiro para Celsius.

- `converter_temperatura(100)` → `212.0`
- `converter_temperatura(32, de="F", para="C")` → `0.0`
- `converter_temperatura(10, para="K")` → `283.15`
- `converter_temperatura(300, "K", "C")` → `26.85`
- `converter_temperatura(1, "X")` → `ValueError: Unidade inválida: use C, F ou K`

<details>
<summary><strong>Resolução</strong></summary>

```python
def converter_temperatura(valor, de="C", para="F"):
    """Converte entre C, F e K, com 2 casas decimais."""
    if de not in ("C", "F", "K") or para not in ("C", "F", "K"):
        raise ValueError("Unidade inválida: use C, F ou K")

    # 1) leva tudo para Celsius
    if de == "F":
        c = (valor - 32) * 5 / 9
    elif de == "K":
        c = valor - 273.15
    else:
        c = valor

    # 2) de Celsius para a unidade pedida
    if para == "F":
        return round(c * 9 / 5 + 32, 2)
    if para == "K":
        return round(c + 273.15, 2)
    return round(c, 2)

print(converter_temperatura(100))                  # 212.0
print(converter_temperatura(32, de="F", para="C")) # 0.0
print(converter_temperatura(10, para="K"))         # 283.15
print(converter_temperatura(300, "K", "C"))        # 26.85
converter_temperatura(1, "X")   # ValueError: Unidade inválida: use C, F ou K
```

</details>

---

## Desafio final — Boletim

### 2.8 `[Desafio]` Juntando funções

Crie `boletim(nome, *notas)`, que usa a `media` do exercício 2.5 e a `classificar_nota` do 1.5 e devolve um texto no formato `"Nome: média - situação"`. Depois use um `for` para imprimir o boletim de todos os alunos do dicionário abaixo.

```python
alunos = {"Ana": [8, 9, 7], "Bruno": [5, 6, 4], "Carla": [10, 9, 9.5], "Diego": [6, 7, 5.5]}
```

- `boletim("Ana", 8, 9, 7)` → `'Ana: 8.0 - Aprovado'`
- `boletim("Bruno", 3, 4)` → `'Bruno: 3.5 - Reprovado'`

**Saída esperada do `for`:**

```text
Ana: 8.0 - Aprovado
Bruno: 5.0 - Recuperação
Carla: 9.5 - Aprovado
Diego: 6.17 - Recuperação
```

<details>
<summary><strong>Resolução</strong></summary>

```python
def boletim(nome, *notas):
    """Devolve 'Nome: média - situação'."""
    m = media(*notas)              # reaproveita a função do 2.5
    situacao = classificar_nota(m) # reaproveita a função do 1.5
    return f"{nome}: {m} - {situacao}"

alunos = {"Ana": [8, 9, 7], "Bruno": [5, 6, 4], "Carla": [10, 9, 9.5], "Diego": [6, 7, 5.5]}
for nome, notas in alunos.items():
    print(boletim(nome, *notas))   # o * abre a lista [8, 9, 7] em três argumentos
```

</details>

> **O ponto-chave é reaproveitar:** `boletim` não recalcula nada, só chama funções que já existem. Se a regra de aprovação mudar, basta alterar `classificar_nota`.
