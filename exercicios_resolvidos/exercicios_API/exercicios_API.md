# Exercício com API

## Sumário

- [Exercício 1 — Trazer os itens para o seu ambiente](#exercício-1--trazer-os-itens-para-o-seu-ambiente)
- [Exercício 2 — Acessar o dado do seu ambiente](#exercício-2--acessar-o-dado-do-seu-ambiente)
- [Atividade 3 — Explorando produtos com Python](#atividade-3--explorando-produtos-com-python)
  - [Exercício 3.1 — Acessar a lista de produtos](#exercício-31--acessar-a-lista-de-produtos)
  - [Exercício 3.2 — Mostrar o primeiro produto](#exercício-32--mostrar-o-primeiro-produto)
  - [Exercício 3.3 — Mostrar somente o título](#exercício-33--mostrar-somente-o-título)
  - [Exercício 3.4 — Mostrar título e preço](#exercício-34--mostrar-título-e-preço)
  - [Exercício 3.5 — Alterar um valor](#exercício-35--alterar-um-valor)
  - [Exercício 3.6 — Adicionar uma nova chave](#exercício-36--adicionar-uma-nova-chave)
  - [Exercício 3.7 — Percorrer os produtos](#exercício-37--percorrer-os-produtos)
  - [Exercício 3.8 — Mostrar título e preço de todos](#exercício-38--mostrar-título-e-preço-de-todos)
  - [Exercício 3.9 — Encontrar produtos caros](#exercício-39--encontrar-produtos-caros)
  - [Exercício 3.10 — Calcular o valor do estoque](#exercício-310--calcular-o-valor-do-estoque)
  - [Exercício 3.11 — Acessar um dicionário aninhado](#exercício-311--acessar-um-dicionário-aninhado)
  - [Exercício 3.12 — Percorrer as avaliações](#exercício-312--percorrer-as-avaliações)
  - [Exercício 3.13 — Mostrar avaliador e nota](#exercício-313--mostrar-avaliador-e-nota)
  - [Exercício 3.14 — Calcular a média das avaliações](#exercício-314--calcular-a-média-das-avaliações)
  - [Exercício 3.15 — Tratar uma lista vazia](#exercício-315--tratar-uma-lista-vazia)
  - [Desafio final — Relatório de produtos](#desafio-final--relatório-de-produtos)
- [Gabarito](#gabarito)
  - [3.1](#31)
  - [3.2](#32)
  - [3.3](#33)
  - [3.4](#34)
  - [3.5](#35)
  - [3.6](#36)
  - [3.7](#37)
  - [3.8](#38)
  - [3.9](#39)
  - [3.10](#310)
  - [3.11](#311)
  - [3.12](#312)
  - [3.13](#313)
  - [3.14](#314)
  - [3.15](#315)
  - [Desafio final](#desafio-final)

> **Dica:** para responder esses exercícios, você pode fazer uma cópia do arquivo original (**File → Make a copy**) ou responder onde preferir.

No Colab, crie um notebook chamado `Exercicio_com_API` (ou outro nome da sua preferência).

Nesse exercício vamos trazer os itens da API para o nosso ambiente, simulando a interação com *third parties*. Depois de trazer os dados, executaremos os exercícios usando os conceitos aprendidos até agora.

- API usada na aula: <https://dummyjson.com>
- Enunciado original: [documento da atividade](https://docs.google.com/document/d/1hJWeLGB0hjFJD8gwtDntZU6QG9_XZtTgQrc-9K3TpXQ/edit?tab=t.0)

## Exercício 1 — Trazer os itens para o seu ambiente

**Passo 1** — Salve os dados com o código da API que usamos na aula passada:

```python
import os
import json
import requests

# Criar as pastas
os.makedirs("produtos", exist_ok=True)
os.makedirs("usuarios", exist_ok=True)
os.makedirs("carrinhos", exist_ok=True)

# --- Produtos ---
resposta = requests.get("https://dummyjson.com/products")
dados_produtos = resposta.json()

with open("produtos/produtos.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_produtos, arquivo, ensure_ascii=False, indent=2)

# --- Usuários ---
resposta = requests.get("https://dummyjson.com/users")
dados_usuarios = resposta.json()

with open("usuarios/usuarios.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_usuarios, arquivo, ensure_ascii=False, indent=2)

# --- Carrinhos ---
resposta = requests.get("https://dummyjson.com/carts")
dados_carrinhos = resposta.json()

with open("carrinhos/carrinhos.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados_carrinhos, arquivo, ensure_ascii=False, indent=2)

print("Arquivos salvos!")

for pasta in ["produtos", "usuarios", "carrinhos"]:
    print(f"{pasta}/:", os.listdir(pasta))
```

## Exercício 2 — Acessar o dado do seu ambiente

**Passo 2** — Carregue o arquivo `produtos` em uma variável chamada `dados`:

```python
import json

with open("produtos/produtos.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

display(dados)
```

> `display()` existe no Colab/Jupyter. Fora do notebook, use `print(dados)`.

**Responda:** Qual a vantagem de você trazer os dados para dentro do seu ambiente ao invés de apenas consultar a API?

**Resposta:**

## Atividade 3 — Explorando produtos com Python

Nesta atividade, `dados` é um dicionário que contém uma lista de produtos. Cada produto também é um dicionário, com informações como título, preço, estoque e avaliações.

**Como fazer:**

- **Opção a)** Em cada exercício, leia o objetivo e tente resolver sem olhar a resposta. Depois, compare o código proposto com a sua resolução e responda às perguntas.
- **Opção b)** Caso precise da resposta, olhe o código e responda às perguntas *antes* de executá-lo. Depois, execute, compare o resultado com a sua previsão e corrija sua resposta se necessário.

Os exercícios foram escritos para serem feitos **em ordem**. Nos exercícios 3.5 e 3.6, você vai alterar o primeiro produto; essas alterações continuarão presentes nos exercícios seguintes.

### Exercício 3.1 — Acessar a lista de produtos

**Objetivo:** mostrar todos os produtos armazenados em `dados`.

**Código Python:**

```python
produtos = dados["products"]
print(produtos)
```

**Para pensar:**

1. `dados` é um dicionário. O que representa `"products"`?
2. O valor guardado em `produtos` será uma lista ou um dicionário?
3. Se houver cinco produtos, quantos itens existirão nessa lista?
4. Ao executar `print(produtos)`, você espera ver somente os títulos ou todas as informações dos produtos?

### Exercício 3.2 — Mostrar o primeiro produto

**Objetivo:** acessar e mostrar o primeiro produto da lista.

**Código Python:**

```python
primeiro_produto = dados["products"][0]
print(primeiro_produto)
```

**Para pensar:**

1. Qual parte do código acessa a lista de produtos?
2. O que `[0]` seleciona?
3. Por que usamos `[0]` para o primeiro produto, e não `[1]`?
4. O valor de `primeiro_produto` é uma lista ou um dicionário?

### Exercício 3.3 — Mostrar somente o título

**Objetivo:** mostrar o título do primeiro produto.

**Código Python:**

```python
titulo = dados["products"][0]["title"]
print(titulo)
```

Resultado esperado nos dados deste exercício:

```text
Essence Mascara Lash Princess
```

**Para pensar:**

1. O que cada parte seleciona: `["products"]`, `[0]` e `["title"]`?
2. Por que este código mostra uma informação, enquanto o exercício anterior mostrou o produto inteiro?
3. Como você acessaria o título do segundo produto?
4. O que provavelmente aconteceria se você escrevesse `["titulo"]` no lugar de `["title"]`, sem que essa chave existisse?

### Exercício 3.4 — Mostrar título e preço

**Objetivo:** mostrar duas informações do primeiro produto.

**Código Python:**

```python
produto = dados["products"][0]
print("Produto:", produto["title"])
print("Preço:", produto["price"])
```

**Para pensar:**

1. Por que guardamos o produto na variável `produto`?
2. `"Produto:"` e `"Preço:"` são chaves do dicionário ou textos escritos por nós?
3. Qual parte do código acessa o preço armazenado nos dados?
4. Como você acrescentaria uma terceira linha para mostrar o estoque?

### Exercício 3.5 — Alterar um valor

**Objetivo:** alterar o estoque do primeiro produto para 80.

**Código Python:**

```python
produto = dados["products"][0]
produto["stock"] = 80
print(produto["stock"])
```

**Para pensar:**

1. Antes de executar, qual número você espera que apareça?
2. A linha `produto["stock"] = 80` consulta o estoque ou modifica o estoque?
3. Depois da alteração, o que você espera obter com `dados["products"][0]["stock"]`?
4. Se executar essa célula novamente, o estoque mudará para outro valor?

### Exercício 3.6 — Adicionar uma nova chave

**Objetivo:** registrar que o primeiro produto está em promoção.

**Código Python:**

```python
produto = dados["products"][0]
produto["onSale"] = True
print(produto)
```

**Para pensar:**

1. A chave `"onSale"` precisava existir antes dessa linha?
2. Qual é a diferença entre adicionar `produto["onSale"] = True` e alterar `produto["stock"] = 80`?
3. `True` é um texto, um número ou um valor booleano?
4. Que valor você usaria para indicar que o produto não está em promoção?

### Exercício 3.7 — Percorrer os produtos

**Objetivo:** mostrar o título de todos os produtos.

**Código Python:**

```python
for produto in dados["products"]:
    print(produto["title"])
```

**Para pensar:**

1. O que a variável `produto` representa em cada repetição?
2. Se houver cinco produtos, quantas vezes o `print` será executado?
3. Por que não precisamos escrever `[0]`, `[1]`, `[2]` e assim por diante?
4. O que mudaria se usássemos `print(produto)` em vez de `print(produto["title"])`?

### Exercício 3.8 — Mostrar título e preço de todos

**Objetivo:** mostrar o título e o preço de cada produto.

**Código Python:**

```python
for produto in dados["products"]:
    print("Produto:", produto["title"])
    print("Preço: R$", produto["price"])
    print()
```

**Para pensar:**

1. Quais linhas estão dentro do `for`? Como você identifica isso no código?
2. Para que serve o `print()` sem nenhum argumento?
3. Se houver três produtos, quantas vezes a palavra `"Produto:"` aparecerá?
4. Acrescente mentalmente uma linha para mostrar a marca. Onde ela deveria ficar?

### Exercício 3.9 — Encontrar produtos caros

**Objetivo:** mostrar somente os produtos cujo preço é superior a 15.

**Código Python:**

```python
for produto in dados["products"]:
    if produto["price"] > 15:
        print(produto["title"])
```

**Para pensar:**

1. O `for` percorre todos os produtos ou somente os caros?
2. O que o `if` decide?
3. Um produto que custa exatamente 15 será mostrado? Por quê?
4. Qual operador você usaria para incluir também produtos que custam exatamente 15?
5. Se nenhum produto atender à condição, o que será impresso?

### Exercício 3.10 — Calcular o valor do estoque

**Objetivo:** calcular quanto vale o estoque de cada produto.

**Código Python:**

```python
for produto in dados["products"]:
    valor_estoque = produto["price"] * produto["stock"]
    print(produto["title"])
    print("Valor do estoque: R$", round(valor_estoque, 2))
```

**Para pensar:**

1. Se um produto custa R$ 10 e há 8 unidades em estoque, qual será o valor do estoque?
2. Por que multiplicamos `price` por `stock`?
3. O que acontecerá com `valor_estoque` se `stock` for zero?
4. Para que serve `round(valor_estoque, 2)`?
5. Esse código calcula o valor de cada produto separadamente ou a soma do estoque de todos os produtos?

### Exercício 3.11 — Acessar um dicionário aninhado

**Objetivo:** mostrar a largura do primeiro produto.

**Código Python:**

```python
largura = dados["products"][0]["dimensions"]["width"]
print("Largura:", largura)
```

Caminho percorrido:

```text
dados → products → primeiro produto → dimensions → width
```

**Para pensar:**

1. Qual parte do caminho é uma lista?
2. Qual parte seleciona o primeiro produto?
3. O que você espera encontrar em `["dimensions"]`?
4. Como mudaria o código para mostrar `height`?
5. Se a chave `"width"` não existisse em `"dimensions"`, o código conseguiria mostrar a largura?

### Exercício 3.12 — Percorrer as avaliações

**Objetivo:** mostrar os comentários recebidos pelo primeiro produto.

**Código Python:**

```python
produto = dados["products"][0]
for avaliacao in produto["reviews"]:
    print(avaliacao["comment"])
```

**Para pensar:**

1. O que `produto["reviews"]` contém?
2. O que a variável `avaliacao` representa em cada repetição?
3. Se o produto tiver três avaliações, quantos comentários serão mostrados?
4. Se a lista de avaliações estiver vazia, o `print` será executado alguma vez?

### Exercício 3.13 — Mostrar avaliador e nota

**Objetivo:** mostrar o nome e a nota de cada pessoa que avaliou o primeiro produto.

**Código Python:**

```python
produto = dados["products"][0]
for avaliacao in produto["reviews"]:
    print("Avaliador:", avaliacao["reviewerName"])
    print("Nota:", avaliacao["rating"])
    print()
```

**Para pensar:**

1. `reviewerName` e `rating` pertencem ao produto diretamente ou a cada avaliação?
2. Por que as duas linhas de `print` estão dentro do `for`?
3. Se houver quatro avaliações, quantas vezes `"Nota:"` aparecerá?
4. O que mudaria se o último `print()` estivesse fora do `for`?

### Exercício 3.14 — Calcular a média das avaliações

**Objetivo:** calcular a média das notas do primeiro produto.

> **Atenção:** existe um erro proposital no código. Encontre-o antes de executar.

**Código Python (com erro proposital):**

```python
produto = dados["products"][0"]
soma = 0
for avaliacao in produto["reviews"]:
    soma = soma + avaliacao["rating"]
media = soma / len(produto["reviews"])
print("Média:", media)
```

**Para pensar:**

1. Qual linha impede a execução do código? O que há de errado nela?
2. Depois de corrigir o erro, por que começamos com `soma = 0`?
3. O que acontece com `soma` a cada repetição do `for`?
4. Por que dividimos por `len(produto["reviews"])`?
5. Se as notas fossem 4, 5 e 3, qual seria a média?
6. O que aconteceria se esse produto não tivesse avaliações?

### Exercício 3.15 — Tratar uma lista vazia

**Objetivo:** calcular uma média sem provocar divisão por zero.

Para garantir que todos possam testar esse caso, vamos começar com uma lista de avaliações vazia. Depois, você pode substituir `[]` por `dados["products"][1]["reviews"]` e observar o que acontece com o segundo produto dos seus dados.

**Código Python:**

```python
avaliacoes = []
if len(avaliacoes) > 0:
    soma = 0
    for avaliacao in avaliacoes:
        soma = soma + avaliacao["rating"]
    media = soma / len(avaliacoes)
    print("Média:", media)
else:
    print("Este produto ainda não possui avaliações.")
```

**Para pensar:**

1. Quanto vale `len(avaliacoes)` neste exemplo?
2. A condição `len(avaliacoes) > 0` é verdadeira ou falsa?
3. Qual bloco será executado: `if` ou `else`?
4. Por que o código não tenta calcular a média de uma lista vazia?
5. O que você precisaria mudar para testar o bloco `if`?

### Desafio final — Relatório de produtos

**Objetivo:** mostrar, para cada produto:

- título;
- marca;
- preço;
- estoque;
- valor total do estoque;
- quantidade de avaliações.

**Código Python:**

```python
for produto in dados["products"]:
    valor_estoque = produto["price"] * produto["stock"]
    quantidade_avaliacoes = len(produto["reviews"])

    print("Produto:", produto["title"])
    print("Marca:", produto.get("brand", "Não informada"))
    print("Preço: R$", produto["price"])
    print("Estoque:", produto["stock"])
    print("Valor do estoque: R$", round(valor_estoque, 2))
    print("Quantidade de avaliações:", quantidade_avaliacoes)

    print("------------------------------")
```

> **Atenção:** nos dados atuais da API, os produtos de mercado (a partir do id 16, como Apple e Beef Steak) não possuem a chave `"brand"`. Por isso o código usa `produto.get("brand", "Não informada")` em vez de `produto["brand"]`, que provocaria `KeyError`.

**Para pensar:**

1. Quais informações já estavam armazenadas no produto?
2. Quais informações o código precisou calcular?
3. Por que usamos `len()` para obter a quantidade de avaliações?
4. Se um produto não tiver avaliações, que número aparecerá no relatório?
5. Como o relatório do primeiro produto foi afetado pelas alterações feitas nos exercícios 3.5 e 3.6?

**Modificação:** acrescente ao relatório uma linha que mostre `Em promoção: Sim` quando `onSale` for `True` e `Em promoção: Não` nos demais casos. Lembre-se de que nem todos os produtos possuem a chave `onSale`.

## Gabarito

Os valores exatos impressos dependem dos produtos presentes em `dados`. O gabarito explica o raciocínio; não é necessário que todos tenham a mesma quantidade de produtos ou avaliações.

### 3.1

1. `"products"` é uma chave do dicionário `dados`.
2. `produtos` recebe uma lista.
3. Se houver cinco produtos, haverá cinco itens.
4. `print(produtos)` mostra a representação da lista inteira, incluindo as informações dos produtos.

### 3.2

1. `dados["products"]` acessa a lista.
2. `[0]` seleciona o primeiro item.
3. Em Python, os índices de uma lista começam em zero.
4. `primeiro_produto` é um dicionário.

### 3.3

1. `["products"]` acessa a lista; `[0]` seleciona o primeiro produto; `["title"]` acessa seu título.
2. O exercício anterior imprime o dicionário inteiro. Este imprime apenas o valor da chave `"title"`.
3. O segundo título seria acessado por `dados["products"][1]["title"]`.
4. Se `"titulo"` não existir como chave, ocorrerá um `KeyError`.

### 3.4

1. A variável evita repetir `dados["products"][0]` em cada linha.
2. `"Produto:"` e `"Preço:"` são textos que escolhemos imprimir.
3. `produto["price"]` acessa o preço.
4. Uma possibilidade é:

    ```python
    print("Estoque:", produto["stock"])
    ```

### 3.5

1. O código mostra `80`.
2. A atribuição **modifica** o estoque.
3. `dados["products"][0]["stock"]` também será `80`, pois `produto` se refere ao mesmo dicionário da lista.
4. Não. Executar a atribuição novamente mantém o valor em `80`.

### 3.6

1. Não. A atribuição cria a chave se ela ainda não existir.
2. No 3.5, uma chave existente recebe outro valor; no 3.6, uma nova chave pode ser criada.
3. `True` é um valor booleano.
4. `False`.

### 3.7

1. `produto` representa um item da lista a cada repetição.
2. Cinco vezes, se houver cinco produtos.
3. O `for` acessa os itens da lista um de cada vez.
4. `print(produto)` mostraria todas as informações do produto, e não apenas seu título.

### 3.8

1. As três linhas recuadas estão dentro do `for`. Esse recuo é chamado de **indentação**.
2. `print()` produz uma linha em branco para separar visualmente os produtos.
3. Três vezes.
4. A linha deve ficar dentro do `for`:

    ```python
    print("Marca:", produto["brand"])
    ```

    > **Atenção:** nos dados atuais da API, os produtos de mercado (a partir do id 16, como Apple e Beef Steak) não possuem a chave `"brand"`. Nesses casos, `produto["brand"]` provoca `KeyError`. Use `produto.get("brand", "Não informada")`, como no desafio final.

### 3.9

1. O `for` percorre todos os produtos.
2. O `if` decide se o título do produto atual será mostrado.
3. Não. `15 > 15` é falso.
4. `>=`, formando `produto["price"] >= 15`.
5. Nenhum título será impresso.

### 3.10

1. R$ 80.
2. O valor do estoque é o preço de uma unidade multiplicado pela quantidade disponível.
3. Será zero.
4. `round(valor_estoque, 2)` arredonda o resultado para duas casas decimais.
5. Calcula o valor de cada produto separadamente. Não há uma variável acumulando o total de todos eles.

### 3.11

1. `dados["products"]` é a lista.
2. `[0]` seleciona o primeiro produto.
3. Um dicionário com as dimensões do produto.
4. Assim:

    ```python
    altura = dados["products"][0]["dimensions"]["height"]
    print("Altura:", altura)
    ```
5. Não. O acesso a uma chave inexistente provocaria um `KeyError`.

### 3.12

1. Uma lista de avaliações.
2. Um dicionário correspondente a uma avaliação.
3. Três comentários.
4. Não. Um `for` sobre uma lista vazia não executa seu bloco.

### 3.13

1. Pertencem a cada avaliação.
2. Queremos mostrar o nome e a nota para cada avaliação.
3. Quatro vezes.
4. Apareceria uma única linha em branco depois de todas as avaliações, em vez de uma entre elas.

### 3.14

1. Há uma aspa extra depois do `[0]`. A linha correta é:

    ```python
    produto = dados["products"][0]
    ```
2. `soma = 0` estabelece o valor inicial antes de acumular as notas.
3. Cada nota é adicionada à soma.
4. `len(produto["reviews"])` informa quantas notas entraram na soma. A média é a soma dividida por essa quantidade.
5. (4 + 5 + 3) / 3 = 4.
6. O programa tentaria dividir por zero e produziria `ZeroDivisionError`.

### 3.15

1. `len(avaliacoes)` vale `0`.
2. A condição é falsa.
3. O bloco `else`.
4. O cálculo está dentro do `if`, que só é executado quando há pelo menos uma avaliação.
5. Use uma lista com ao menos uma avaliação, por exemplo:

    ```python
    avaliacoes = [{"rating": 4}, {"rating": 5}]
    ```

    Nesse caso, a média será `4.5`.

### Desafio final

1. `title`, `brand`, `price`, `stock` e `reviews` já estão nos dados.
2. `valor_estoque` e `quantidade_avaliacoes` são calculados.
3. `len(produto["reviews"])` conta quantos itens existem na lista de avaliações.
4. Aparecerá `0`.
5. O estoque do primeiro produto será `80`, porque foi alterado no 3.5. A chave `onSale` também foi adicionada no 3.6, embora não apareça no relatório original.

Uma solução para a modificação é usar `get()`, que permite consultar uma chave mesmo quando ela não está presente em todos os produtos. Acrescente estas linhas dentro do `for`:

```python
if produto.get("onSale", False):
    print("Em promoção: Sim")
else:
    print("Em promoção: Não")
```

Em `produto.get("onSale", False)`, o `False` é o valor usado quando o produto não possui a chave `"onSale"`.
