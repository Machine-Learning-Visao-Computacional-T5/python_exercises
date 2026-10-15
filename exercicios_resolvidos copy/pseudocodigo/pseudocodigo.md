# Exercícios de Pseudocódigo para Iniciantes

## Sumário

- [Pseudocódigo](#pseudocódigo)
  - [Exercício 1 — Apresentação](#exercício-1--apresentação)
  - [Exercício 2 — Soma de dois números](#exercício-2--soma-de-dois-números)
  - [Exercício 3 — Média das notas](#exercício-3--média-das-notas)
  - [Exercício 4 — Aprovação do aluno](#exercício-4--aprovação-do-aluno)
  - [Exercício 5 — Classificação da nota](#exercício-5--classificação-da-nota)
  - [Exercício 6 — Número par ou ímpar](#exercício-6--número-par-ou-ímpar)
  - [Exercício 7 — Contagem de 1 a 10](#exercício-7--contagem-de-1-a-10)
  - [Exercício 8 — Tabuada](#exercício-8--tabuada)
  - [Exercício 9 — Validação de senha](#exercício-9--validação-de-senha)
  - [Exercício 10 — Soma dos valores de uma lista](#exercício-10--soma-dos-valores-de-uma-lista)
  - [Exercício 11 — Maior valor da lista](#exercício-11--maior-valor-da-lista)
  - [Exercício 12 — Média de uma lista](#exercício-12--média-de-uma-lista)
  - [Exercício 13 — Contagem de aprovados](#exercício-13--contagem-de-aprovados)
  - [Exercício 14 — Classificação de e-mails](#exercício-14--classificação-de-e-mails)
  - [Exercício 15 — Pipeline de Machine Learning (exemplo)](#exercício-15--pipeline-de-machine-learning-exemplo)
- [Resolução em Python](#resolução-em-python)
  - [Exercício 1 — Apresentação](#exercício-1--apresentação-1)
  - [Exercício 2 — Soma de dois números](#exercício-2--soma-de-dois-números-1)
  - [Exercício 3 — Média das notas](#exercício-3--média-das-notas-1)
  - [Exercício 4 — Aprovação do aluno](#exercício-4--aprovação-do-aluno-1)
  - [Exercício 5 — Classificação da nota](#exercício-5--classificação-da-nota-1)
  - [Exercício 6 — Número par ou ímpar](#exercício-6--número-par-ou-ímpar-1)
  - [Exercício 7 — Contagem de 1 a 10](#exercício-7--contagem-de-1-a-10-1)
  - [Exercício 8 — Tabuada](#exercício-8--tabuada-1)
  - [Exercício 9 — Validação de senha](#exercício-9--validação-de-senha-1)
  - [Exercício 10 — Soma dos valores de uma lista](#exercício-10--soma-dos-valores-de-uma-lista-1)
  - [Exercício 11 — Maior valor da lista](#exercício-11--maior-valor-da-lista-1)
  - [Exercício 12 — Média de uma lista](#exercício-12--média-de-uma-lista-1)
  - [Exercício 13 — Contagem de aprovados](#exercício-13--contagem-de-aprovados-1)
  - [Exercício 14 — Classificação de e-mails](#exercício-14--classificação-de-e-mails-1)
  - [Exercício 15 — Pipeline de Machine Learning (só para exemplo)](#exercício-15--pipeline-de-machine-learning-só-para-exemplo)

Material de apoio para aula — enunciados e respostas comentadas em pseudocódigo, seguidas da resolução em Python.

> **Nota:** o exercício 15 é apenas um **exemplo** de como as etapas de um projeto de Machine Learning se traduzem em código. Ele exige a biblioteca scikit-learn (`pip install scikit-learn`).

## Pseudocódigo

### Exercício 1 — Apresentação

**Enunciado:** Crie um algoritmo que solicite o nome do usuário e mostre uma mensagem de boas-vindas.

**Resposta:**

```text
INÍCIO
    LER nome
    MOSTRAR "Olá, " + nome + "! Bem-vindo(a)!"
FIM
```

### Exercício 2 — Soma de dois números

**Enunciado:** Crie um algoritmo que receba dois números, calcule a soma e mostre o resultado.

**Resposta:**

```text
INÍCIO
    LER numero1
    LER numero2
    soma ← numero1 + numero2
    MOSTRAR "Resultado: " + soma
FIM
```

### Exercício 3 — Média das notas

**Enunciado:** Crie um algoritmo que receba três notas de um aluno, calcule a média e mostre o resultado.

**Resposta:**

```text
INÍCIO
    LER nota1
    LER nota2
    LER nota3
    media ← (nota1 + nota2 + nota3) / 3
    MOSTRAR "Média: " + media
FIM
```

### Exercício 4 — Aprovação do aluno

**Enunciado:** Crie um algoritmo que receba a média de um aluno. Se a média for maior ou igual a 7, mostre “Aprovado”. Caso contrário, mostre “Reprovado”.

**Resposta:**

```text
INÍCIO
    LER media
    SE media >= 7 ENTÃO
        MOSTRAR "Aprovado"
    SENÃO
        MOSTRAR "Reprovado"
    FIM_SE
FIM
```

### Exercício 5 — Classificação da nota

**Enunciado:** Receba a nota de um aluno. Mostre “Aprovado” para nota ≥ 7, “Recuperação” para nota entre 5 e 6,9 e “Reprovado” para nota < 5.

**Resposta:**

```text
INÍCIO
    LER nota
    SE nota >= 7 ENTÃO
        MOSTRAR "Aprovado"
    SENÃO SE nota >= 5 ENTÃO
        MOSTRAR "Recuperação"
    SENÃO
        MOSTRAR "Reprovado"
    FIM_SE
FIM
```

### Exercício 6 — Número par ou ímpar

**Enunciado:** Crie um algoritmo que receba um número inteiro e informe se ele é par ou ímpar.

**Resposta:**

```text
INÍCIO
    LER numero
    SE numero MOD 2 = 0 ENTÃO
        MOSTRAR "O número é par"
    SENÃO
        MOSTRAR "O número é ímpar"
    FIM_SE
FIM
```

### Exercício 7 — Contagem de 1 a 10

**Enunciado:** Crie um algoritmo que mostre os números de 1 até 10.

**Resposta:**

```text
INÍCIO
    PARA numero DE 1 ATÉ 10 FAÇA
        MOSTRAR numero
    FIM_PARA
FIM
```

### Exercício 8 — Tabuada

**Enunciado:** Crie um algoritmo que receba um número e mostre sua tabuada de 1 a 10.

**Resposta:**

```text
INÍCIO
    LER numero
    PARA multiplicador DE 1 ATÉ 10 FAÇA
        resultado ← numero * multiplicador
        MOSTRAR numero + " × " + multiplicador + " = " + resultado
    FIM_PARA
FIM
```

### Exercício 9 — Validação de senha

**Enunciado:** Solicite uma senha. Enquanto ela for diferente de 1234, peça uma nova tentativa. Ao acertar, mostre “Acesso permitido”.

**Resposta:**

```text
INÍCIO
    senha_correta ← "1234"
    LER senha
    ENQUANTO senha != senha_correta FAÇA
        MOSTRAR "Senha incorreta. Tente novamente."
        LER senha
    FIM_ENQUANTO
    MOSTRAR "Acesso permitido"
FIM
```

### Exercício 10 — Soma dos valores de uma lista

**Enunciado:** Considere a lista [10, 20, 30, 40]. Percorra a lista, some todos os valores e mostre o resultado.

**Resposta:**

```text
INÍCIO
    numeros ← [10, 20, 30, 40]
    soma ← 0
    PARA CADA numero EM numeros FAÇA
        soma ← soma + numero
    FIM_PARA
    MOSTRAR "Soma: " + soma
FIM
```

### Exercício 11 — Maior valor da lista

**Enunciado:** Considere a lista [12, 35, 8, 42, 17]. Encontre e mostre o maior valor.

**Resposta:**

```text
INÍCIO
    numeros ← [12, 35, 8, 42, 17]
    maior ← numeros[0]
    PARA CADA numero EM numeros FAÇA
        SE numero > maior ENTÃO
            maior ← numero
        FIM_SE
    FIM_PARA
    MOSTRAR "Maior número: " + maior
FIM
```

### Exercício 12 — Média de uma lista

**Enunciado:** Considere as notas [8, 7, 9, 6, 10]. Calcule e mostre a média.

**Resposta:**

```text
INÍCIO
    notas ← [8, 7, 9, 6, 10]
    soma ← 0
    PARA CADA nota EM notas FAÇA
        soma ← soma + nota
    FIM_PARA
    media ← soma / TAMANHO(notas)
    MOSTRAR "Média: " + media
FIM
```

### Exercício 13 — Contagem de aprovados

**Enunciado:** Considere as notas [8, 4, 7, 9, 5]. Conte quantos alunos possuem nota maior ou igual a 7.

**Resposta:**

```text
INÍCIO
    notas ← [8, 4, 7, 9, 5]
    quantidade_aprovados ← 0
    PARA CADA nota EM notas FAÇA
        SE nota >= 7 ENTÃO
            quantidade_aprovados ← quantidade_aprovados + 1
        FIM_SE
    FIM_PARA
    MOSTRAR "Quantidade de aprovados: " + quantidade_aprovados
FIM
```

### Exercício 14 — Classificação de e-mails

**Enunciado:** Receba a quantidade de palavras suspeitas em um e-mail. Se houver três ou mais, classifique-o como “Possível spam”; caso contrário, como “E-mail normal”.

**Resposta:**

```text
INÍCIO
    LER quantidade_palavras_suspeitas
    SE quantidade_palavras_suspeitas >= 3 ENTÃO
        MOSTRAR "Possível spam"
    SENÃO
        MOSTRAR "E-mail normal"
    FIM_SE
FIM
```

### Exercício 15 — Pipeline de Machine Learning (exemplo)

**Enunciado:** Organize as etapas de um projeto de Machine Learning: carregar dados, separar treino e teste, treinar, realizar previsões e avaliar o modelo.

**Resposta:**

```text
INÍCIO
    dataset ← CARREGAR_DADOS()
    dados_treino, dados_teste ← SEPARAR_DADOS(dataset)
    modelo ← TREINAR_MODELO(dados_treino)
    previsoes ← REALIZAR_PREVISOES(modelo, dados_teste)
    resultado ← AVALIAR_MODELO(previsoes, dados_teste)
    MOSTRAR resultado
FIM
```

## Resolução em Python

### Exercício 1 — Apresentação

```python
nome = input("Digite seu nome: ")
print("Olá, " + nome + "! Bem-vindo(a)!")
```

`input()` pausa o programa, mostra o texto entre aspas na tela e espera a pessoa digitar algo — o que ela digitar vira o valor da variável `nome` (sempre como texto/*string*). `print()` mostra algo na tela; aqui estou "colando" pedaços de texto com o `+` (chamado de **concatenação**).

### Exercício 2 — Soma de dois números

```python
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
soma = numero1 + numero2
print("Resultado: " + str(soma))
```

`input()` sempre devolve texto — por isso envolvo com `float(...)`, que converte esse texto para número decimal (senão `"3" + "4"` viraria `"34"`, e não 7). No `print`, faço o caminho inverso com `str(soma)`, convertendo o número de volta para texto, para poder colar com `+`.

### Exercício 3 — Média das notas

```python
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print("Média: " + str(media))
```

Três `input()` guardam cada nota numa variável diferente. A média é só a fórmula matemática mesmo: soma tudo e divide por 3.

### Exercício 4 — Aprovação do aluno

```python
media = float(input("Digite a média do aluno: "))

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
```

O `if` testa a condição `media >= 7`. Se for verdadeira, roda o bloco indentado logo abaixo (`print("Aprovado")`). Se for falsa, pula para o bloco do `else`. Só um dos dois `print` roda, nunca os dois.

### Exercício 5 — Classificação da nota

```python
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

`elif` (abreviação de "else if") permite testar uma segunda condição, só se a primeira for falsa. O Python testa em ordem: primeiro `nota >= 7`; se não for, testa `nota >= 5`; se nenhuma das duas for, cai no `else`.

### Exercício 6 — Número par ou ímpar

```python
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")
```

`int(...)` converte o texto digitado para número inteiro. O `%` é o operador de resto da divisão (**módulo**): `numero % 2` dá o resto de dividir `numero` por 2 — que só pode ser 0 (número par) ou 1 (número ímpar).

### Exercício 7 — Contagem de 1 a 10

```python
for numero in range(1, 11):
    print(numero)
```

`range(1, 11)` gera a sequência de números de 1 até 10 (o segundo número, 11, não entra — é o "até, mas sem incluir"). O `for` pega cada número dessa sequência, um de cada vez, guarda na variável `numero` e roda o bloco indentado (`print`) para cada um.

### Exercício 8 — Tabuada

```python
numero = int(input("Digite um número para ver a tabuada: "))

for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(str(numero) + " × " + str(multiplicador) + " = " + str(resultado))
```

Mesma lógica do `for` anterior, mas agora a cada volta eu calculo `numero * multiplicador` e guardo em `resultado`, para depois montar a linha de texto da tabuada.

### Exercício 9 — Validação de senha

```python
senha_correta = "1234"
senha = input("Digite a senha: ")

while senha != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha = input("Digite a senha: ")

print("Acesso permitido")
```

`while` repete o bloco enquanto a condição for verdadeira — diferente do `for`, que roda um número fixo de vezes, aqui não sei de antemão quantas tentativas a pessoa vai precisar. `!=` significa "diferente de". Repare que dentro do `while` eu peço a senha de novo (`senha = input(...)`) — sem isso, o valor de `senha` nunca mudaria e o laço rodaria para sempre (**laço infinito**).

### Exercício 10 — Soma dos valores de uma lista

```python
numeros = [10, 20, 30, 40]
soma = 0

for numero in numeros:
    soma = soma + numero

print("Soma: " + str(soma))
```

`[10, 20, 30, 40]` é uma **lista** — uma coleção ordenada de valores. Aqui o `for` percorre a lista diretamente (sem precisar de `range`), pegando cada item, um de cada vez. `soma = soma + numero` é o padrão de **acumulador**: começa em 0 e vai somando o valor atual a cada volta do laço.

### Exercício 11 — Maior valor da lista

```python
numeros = [12, 35, 8, 42, 17]
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print("Maior número: " + str(maior))
```

`numeros[0]` acessa o primeiro item da lista (em Python, a contagem começa do zero). Começo assumindo que o primeiro é o maior; a cada volta do `for`, comparo o item atual com `maior` — se for maior, atualizo a variável. No final, `maior` guarda o maior valor de todos.

### Exercício 12 — Média de uma lista

```python
notas = [8, 7, 9, 6, 10]
soma = 0

for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print("Média: " + str(media))
```

Mesmo padrão de acumulador do exercício 10. `len(notas)` conta quantos itens tem na lista (aqui, 5) — uso isso para dividir a soma e achar a média, sem precisar contar na mão.

### Exercício 13 — Contagem de aprovados

```python
notas = [8, 4, 7, 9, 5]
quantidade_aprovados = 0

for nota in notas:
    if nota >= 7:
        quantidade_aprovados = quantidade_aprovados + 1

print("Quantidade de aprovados: " + str(quantidade_aprovados))
```

Combina `for` + `if` + acumulador: percorro a lista, e toda vez que a nota é `>= 7`, incremento o contador em 1 (`+ 1`). No final, `quantidade_aprovados` tem o total de notas que passaram no teste.

### Exercício 14 — Classificação de e-mails

```python
quantidade_palavras_suspeitas = int(input("Quantidade de palavras suspeitas: "))

if quantidade_palavras_suspeitas >= 3:
    print("Possível spam")
else:
    print("E-mail normal")
```

Mesma estrutura do exercício 4 — só um `if`/`else` simples comparando um número digitado com um limite (3).

### Exercício 15 — Pipeline de Machine Learning (só para exemplo)

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

dataset_X, dataset_y = load_iris(return_X_y=True)

dados_treino_X, dados_teste_X, dados_treino_y, dados_teste_y = train_test_split(
    dataset_X, dataset_y, test_size=0.2, random_state=42
)

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(dados_treino_X, dados_treino_y)

previsoes = modelo.predict(dados_teste_X)

resultado = accuracy_score(dados_teste_y, previsoes)
print("Acurácia do modelo: " + str(round(resultado, 2)))
```

Cada `from ... import ...` traz uma ferramenta pronta da biblioteca **scikit-learn**. `load_iris()` carrega um conjunto de dados de exemplo (flores). `train_test_split` separa os dados em duas partes — uma para "estudar" (treino) e outra para "testar de verdade depois" (teste), como no esquema de treino/validação/teste. `modelo.fit(...)` é o treinamento em si: o modelo aprende os padrões dos dados de treino. `modelo.predict(...)` usa o que ele aprendeu para "chutar" as respostas dos dados de teste (que ele nunca viu). E `accuracy_score` compara os chutes com as respostas certas, dizendo a porcentagem de acerto.
