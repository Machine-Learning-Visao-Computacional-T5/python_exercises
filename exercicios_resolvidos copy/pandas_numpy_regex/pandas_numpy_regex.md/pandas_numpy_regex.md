# Lista de Exercícios — Python para Dados

*30 de set. de 2026 · @hellen*

## Sumário

- [Como usar esta lista](#como-usar-esta-lista)
- [Bloco 1 — Manipulação básica de dados](#bloco-1--manipulação-básica-de-dados)
- [Bloco 2 — Funções e modularização](#bloco-2--funções-e-modularização)
- [Bloco 3 — DataFrames com Pandas](#bloco-3--dataframes-com-pandas)
- [Bloco 4 — NumPy para operações numéricas](#bloco-4--numpy-para-operações-numéricas)
- [Bloco 5 — Dataset real do Kaggle: e-commerce da Olist](#bloco-5--dataset-real-do-kaggle-e-commerce-da-olist)
- [Bloco 6 — De JSON de API para tabela](#bloco-6--de-json-de-api-para-tabela)
- [Projeto integrador — Relatório mensal de vendas](#projeto-integrador--relatório-mensal-de-vendas)
- [Gabarito comentado](#gabarito-comentado)
- [Referências para estudo](#referências-para-estudo)

## Como usar esta lista

São **67 exercícios em 6 blocos**, do mais simples ao mais aplicado, mais um projeto integrador. Os Blocos 1 a 4 usam um CSV pequeno; o Bloco 5 usa um dataset real do Kaggle e o Bloco 6, JSON de uma API pública.

Cada exercício tem um nível:

- **[Básico]** aplica um conceito isolado;
- **[Intermediário]** combina dois ou mais conceitos;
- **[Desafio]** problema aberto, parecido com o dia a dia.

**Pré-requisitos:** Python 3.10+, `pandas`, `numpy` e `openpyxl` (para Excel). O Bloco 6 usa também `requests`. Páginas no PyPI:

- pandas: <https://pypi.org/project/pandas/>
- numpy: <https://pypi.org/project/numpy/>
- openpyxl: <https://pypi.org/project/openpyxl/>
- requests: <https://pypi.org/project/requests/>

Instale com:

```bash
pip install pandas numpy openpyxl requests
```

### Dados de exemplo

Vários exercícios usam este arquivo. Salve como `vendas.csv` na mesma pasta dos scripts:

```csv
id_venda,data,cliente,produto,categoria,quantidade,preco_unit,vendedor
1,2026-01-05,Ana Souza,Notebook,Eletrônicos,1,4500.00,Carlos
2,2026-01-07,Bruno Lima,Mouse,Acessórios,3,89.90,Marina
3,2026-01-12,Carla Dias,Monitor,Eletrônicos,2,1200.00,Carlos
4,2026-02-02,Ana Souza,Teclado,Acessórios,1,250.00,Marina
5,2026-02-15,Diego Rocha,Notebook,Eletrônicos,2,4300.00,Paula
6,2026-02-20,Bruno Lima,Cadeira,Móveis,1,980.00,Paula
7,2026-03-03,Elisa Mota,Mesa,Móveis,1,1500.00,Carlos
8,2026-03-10,Carla Dias,Mouse,Acessórios,5,79.90,Marina
9,2026-03-18,Diego Rocha,Monitor,Eletrônicos,1,1150.00,Paula
10,2026-03-25,Elisa Mota,Teclado,Acessórios,2,230.00,Carlos
```

> **Dica:** tente resolver sem olhar o gabarito; ele está no fim, comentado exercício a exercício.

## Bloco 1 — Manipulação básica de dados

### Leitura e escrita de arquivos

#### 1.1 · Lendo um CSV sem pandas · *Básico*

Use o módulo `csv` ([documentação](https://docs.python.org/pt-br/3/library/csv.html)) para ler `vendas.csv` e imprimir quantas linhas de dados existem (sem contar o cabeçalho) e os nomes das colunas.

#### 1.2 · Calculando o total de cada venda · *Básico*

Leia `vendas.csv` com `csv.DictReader` e gere um novo arquivo `vendas_total.csv` com uma coluna extra `total = quantidade * preco_unit`.

#### 1.3 · CSV para JSON · *Intermediário*

Converta `vendas.csv` em `vendas.json`, uma lista de dicionários. Números devem ser salvos como números (não strings) e o arquivo deve ser legível (`indent=2`, `ensure_ascii=False` para manter os acentos).

#### 1.4 · JSON aninhado · *Intermediário*

Leia `vendas.json` e monte um novo JSON agrupado por vendedor, no formato `{"Carlos": {"qtd_vendas": 4, "faturamento": 8860.0}, ...}`. Salve como `resumo_vendedores.json`.

#### 1.5 · Excel com várias abas · *Intermediário*

Com pandas + openpyxl, salve `vendas.csv` num arquivo `vendas.xlsx` com uma aba por categoria (Eletrônicos, Acessórios, Móveis). Depois leia de volta só a aba **Móveis**.

### Datas com `datetime`

#### 1.6 · Convertendo strings em datas · *Básico*

Converta a coluna `data` de `vendas.csv` para `datetime` e imprima cada data no formato brasileiro `dd/mm/aaaa` e o dia da semana em português (monte uma lista com os nomes dos dias).

#### 1.7 · Diferença entre datas · *Intermediário*

Para cada cliente, calcule quantos dias se passaram entre a primeira e a última compra. Clientes com uma só compra devem aparecer com 0.

#### 1.8 · Prazo de entrega em dias úteis · *Intermediário*

Escreva código que, dada uma data de venda, calcule a data de entrega somando **5 dias úteis** (pule sábados e domingos). Teste com `2026-03-25`: a resposta deve ser `2026-04-01`.

### Expressões regulares para limpeza

#### 1.9 · Limpando telefones · *Básico*

Dada a lista abaixo, use `re` ([documentação](https://docs.python.org/pt-br/3/library/re.html)) para manter só os dígitos e depois formate todos como `(41) 99999-8888`:

```python
telefones = ["(41) 99876-5432", "41998765432", "41 9 9876 5432", "+55 41 99876-5432", "(41)99876.5432"]
```

#### 1.10 · Padronizando um cadastro sujo · *Desafio*

Dada a lista de registros abaixo, extraia com regex: **e-mail** (validado de forma simples), **CPF** no formato `000.000.000-00` e **valor em reais** convertido para `float`. Registros sem e-mail válido devem ser listados à parte.

```python
registros = [
    "Ana Souza | ana.souza@gmail.com | cpf 123.456.789-00 | R$ 1.250,50",
    "BRUNO LIMA | bruno@empresa | CPF: 98765432100 | r$ 89,9",
    "carla dias|carla_dias@yahoo.com.br|cpf=111.222.333-44|R$3.000",
    "Diego Rocha | diego.rocha@outlook.com | 55566677788 | R$ 12,00",
]
```

## Bloco 2 — Funções e modularização

### Definição, parâmetros e retorno

#### 2.1 · Primeira função · *Básico*

Crie `calcular_total(quantidade, preco_unit)` que retorna o total da venda. Teste com `calcular_total(3, 89.90)` (esperado: `269.7`).

#### 2.2 · Parâmetro com valor padrão · *Básico*

Crie `aplicar_desconto(valor, percentual=10)` que retorna o valor com desconto. Teste chamando com e sem o segundo argumento, e também com argumento nomeado (`percentual=25`).

#### 2.3 · Retornando vários valores · *Intermediário*

Crie `estatisticas(valores)` que recebe uma lista de números e retorna uma tupla `(minimo, maximo, media)`. Use desempacotamento para receber o resultado: `mn, mx, md = estatisticas([...])`. O que deve acontecer se a lista estiver vazia? Trate esse caso.

#### 2.4 · `*args` e `**kwargs` · *Intermediário*

Crie `montar_relatorio(titulo, *linhas, **opcoes)` que imprime o título, cada linha numerada, e aceita opções como `maiusculas=True` e `separador="-"`.

#### 2.5 · Validação dentro da função · *Intermediário*

Crie `converter_valor_br(texto)` que transforma `"R$ 1.250,50"` em `1250.5`. Se o texto não for um valor válido, levante `ValueError` com uma mensagem clara. Reaproveite a regex do exercício 1.10.

### Funções `lambda`

#### 2.6 · Ordenando com `lambda` · *Básico*

Dada a lista de tuplas `(produto, preco)` abaixo, ordene por preço decrescente usando `sorted` com `key=lambda ...`:

```python
produtos = [("Mouse", 89.9), ("Notebook", 4500), ("Teclado", 250), ("Monitor", 1200)]
```

#### 2.7 · `map`, `filter` e `lambda` · *Intermediário*

Usando a mesma lista: **(a)** com `filter`, mantenha só produtos acima de R$ 200; **(b)** com `map`, aplique 15% de desconto em todos. Depois reescreva (a) e (b) com *list comprehension* e compare a legibilidade.

#### 2.8 · Função que retorna função · *Intermediário*

Crie `criar_desconto(percentual)` que retorna uma `lambda` que aplica aquele desconto. Exemplo: `black_friday = criar_desconto(30)` e `black_friday(100)` retorna `70.0`.

### Módulos e importação

#### 2.9 · Seu primeiro módulo · *Intermediário*

Crie o arquivo `utils_dados.py` com as funções dos exercícios 2.1, 2.2 e 2.5. Em outro arquivo `main.py`, importe de três formas diferentes e explique a diferença: `import utils_dados`, `from utils_dados import calcular_total` e `import utils_dados as ud`.

#### 2.10 · Pacote com `__name__` · *Desafio*

Organize a estrutura abaixo, adicione um bloco `if __name__ == "__main__":` em `limpeza.py` com testes rápidos e explique por que esses testes **não rodam** quando o módulo é importado por `main.py`:

```text
projeto/
├── main.py
└── meu_pacote/
    ├── __init__.py
    ├── arquivos.py   # funções de leitura/escrita (Bloco 1)
    └── limpeza.py    # funções de regex e conversão
```

## Bloco 3 — DataFrames com Pandas

### Series e DataFrames

#### 3.1 · Criando uma Series · *Básico*

Crie uma Series com o faturamento mensal `[12500, 9800, 15300]` e índice `['jan', 'fev', 'mar']`. Mostre o valor de fevereiro, o mês de maior faturamento (`idxmax`) e a variação percentual mês a mês (`pct_change`).

#### 3.2 · DataFrame a partir de dicionário · *Básico*

Crie um DataFrame de clientes com as colunas `cliente`, `cidade` e `segmento`:

```python
clientes = {
    "cliente": ["Ana Souza", "Bruno Lima", "Carla Dias", "Diego Rocha", "Elisa Mota"],
    "cidade": ["Curitiba", "São Paulo", "Curitiba", "Porto Alegre", "São Paulo"],
    "segmento": ["PF", "PJ", "PF", "PJ", "PF"],
}
```

Explore com `.shape`, `.dtypes`, `.info()`, `.head()` e `.describe(include="all")`.

### Leitura de diferentes fontes

#### 3.3 · Lendo CSV com os tipos certos · *Básico*

Leia `vendas.csv` com `pd.read_csv`, já convertendo `data` para `datetime` (`parse_dates`). Crie a coluna `total`.

#### 3.4 · Três fontes, um DataFrame · *Intermediário*

Leia o mesmo conjunto de dados de `vendas.json` (exercício 1.3) e da aba **Móveis** de `vendas.xlsx` (exercício 1.5). Confirme com `.equals()` ou comparando formas e tipos que os dados batem com o CSV.

#### 3.5 · CSV "brasileiro" · *Intermediário*

Crie à mão um arquivo com separador `;`, decimal `,` e encoding `latin-1` e leia corretamente usando os parâmetros `sep`, `decimal` e `encoding` do `read_csv`.

### Filtros e seleções

#### 3.6 · `loc` e `iloc` · *Básico*

No DataFrame de vendas: **(a)** selecione as 3 primeiras linhas e as colunas `cliente` e `total` com `iloc`; **(b)** faça o mesmo com `loc`; **(c)** explique a diferença.

#### 3.7 · Filtros combinados · *Intermediário*

Selecione: **(a)** vendas de Eletrônicos acima de R$ 2.000; **(b)** vendas de Carlos ou Paula em março; **(c)** produtos que contêm a letra "o" no nome, com `.str.contains`; **(d)** vendedores em `["Marina", "Paula"]` com `.isin`.

### `groupby`, `merge` e `pivot`

#### 3.8 · `groupby` com várias agregações · *Intermediário*

Por categoria, calcule: faturamento total, ticket médio, número de vendas e quantidade de itens vendidos. Use `.agg()` com nomes de colunas legíveis e ordene pelo faturamento.

#### 3.9 · `merge` · *Intermediário*

Junte `vendas` com o DataFrame `clientes` (exercício 3.2) pela coluna `cliente`. Depois responda: qual cidade gerou mais faturamento? Teste também `how="left"` com um cliente que não existe em `clientes` e veja o que acontece.

#### 3.10 · `pivot_table` · *Desafio*

Monte uma tabela com vendedores nas linhas, meses nas colunas e faturamento nos valores (`fill_value=0`, `margins=True`). Qual vendedor foi o melhor em cada mês?

## Bloco 4 — NumPy para operações numéricas

### Arrays

#### 4.1 · Criando arrays · *Básico*

Crie: **(a)** um array com os números de 1 a 20 (`arange`); **(b)** 5 números igualmente espaçados entre 0 e 1 (`linspace`); **(c)** uma matriz 3×4 de zeros; **(d)** uma matriz identidade 3×3. Para cada um, imprima `shape`, `ndim` e `dtype`.

#### 4.2 · Indexação e fatiamento · *Básico*

Com `m = np.arange(1, 13).reshape(3, 4)`, obtenha: a segunda linha, a última coluna, o elemento da linha 0 coluna 2 e a submatriz das 2 primeiras linhas × 2 últimas colunas.

#### 4.3 · Máscaras booleanas · *Intermediário*

Gere 1.000 notas aleatórias entre 0 e 10 com `np.random.default_rng(42).uniform(0, 10, 1000)`. Conte quantas são ≥ 7, calcule a média só das notas abaixo de 5 e substitua por 0 todas as notas abaixo de 2 (**sem laço `for`**).

### Operações vetorizadas

#### 4.4 · Sem laço `for` · *Básico*

Dados `quantidades = np.array([1, 3, 2, 1, 2])` e `precos = np.array([4500, 89.9, 1200, 250, 4300])`, calcule o total de cada venda, o faturamento total e o preço médio ponderado pela quantidade.

#### 4.5 · Comparando desempenho · *Intermediário*

Some os quadrados de 1 a 1.000.000 de duas formas: com laço `for` em Python e com NumPy. Meça o tempo de cada uma com `time.perf_counter()` e compare. (Cuidado com o *overflow*: use `dtype=np.int64`.)

#### 4.6 · Funções universais e agregações por eixo · *Intermediário*

Numa matriz 4×3 de vendas (4 lojas × 3 meses), calcule: total por loja (`axis=1`), total por mês (`axis=0`), a loja com maior total (`argmax`) e a raiz quadrada e o log de todos os valores.

### Broadcasting

#### 4.7 · Escalar e array · *Básico*

Aplique um reajuste de 8% em todos os preços de `precos` (exercício 4.4) e converta para dólar dividindo por 5,40, numa única expressão.

#### 4.8 · Linha × matriz · *Intermediário*

Numa matriz 4×3 de quantidades vendidas (4 lojas × 3 produtos), multiplique pelo vetor de preços `[89.9, 250, 1200]` para obter o faturamento por loja e produto. Explique por que o formato `(4, 3)` combina com `(3,)`.

#### 4.9 · Normalização por coluna · *Intermediário*

Padronize cada coluna de uma matriz 100×3 de dados aleatórios usando *z-score*: `(x - media) / desvio`, com média e desvio calculados **por coluna**. Confirme que cada coluna ficou com média ≈ 0 e desvio ≈ 1.

#### 4.10 · Matriz de distâncias · *Desafio*

Dados 5 pontos 2D `pts = np.random.default_rng(0).random((5, 2))`, calcule a matriz 5×5 de distâncias euclidianas entre todos os pares **sem laços**, usando broadcasting com `pts[:, None, :] - pts[None, :, :]`. Qual par de pontos está mais próximo?

## Bloco 5 — Dataset real do Kaggle: e-commerce da Olist

O [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) tem cerca de 100 mil pedidos feitos entre 2016 e 2018, distribuídos em vários CSVs ligados por chaves. É um dataset bom para praticar `merge`, datas e limpeza de texto em português.

**Como baixar:** entre em <https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce>, clique em **Download** (precisa de conta) e descompacte numa pasta `dados/`. Outra opção é usar a linha de comando:

```bash
kaggle datasets download -d olistbr/brazilian-ecommerce --unzip -p dados
```

| Arquivo | Uma linha é | Chaves |
| --- | --- | --- |
| `olist_orders_dataset.csv` | um pedido | `order_id`, `customer_id` |
| `olist_order_items_dataset.csv` | um item de um pedido | `order_id`, `product_id`, `seller_id` |
| `olist_customers_dataset.csv` | um cliente por pedido | `customer_id`, `customer_unique_id` |
| `olist_products_dataset.csv` | um produto | `product_id` |
| `olist_order_payments_dataset.csv` | um pagamento | `order_id` |
| `olist_order_reviews_dataset.csv` | uma avaliação | `review_id`, `order_id` |
| `olist_sellers_dataset.csv` | um vendedor | `seller_id` |
| `product_category_name_translation.csv` | uma categoria PT → EN | `product_category_name` |

### A. Leitura e inspeção

#### 5.1 · Carregando tudo de uma vez · *Básico*

Escreva `carregar_olist(pasta)` que lê todos os CSVs da pasta com `pathlib.Path.glob` e retorna um dicionário `{nome: DataFrame}`. Use regex para tirar o prefixo `olist_` e o sufixo `_dataset` dos nomes (ex.: `orders`, `order_items`). Imprima o `shape` de cada tabela.

#### 5.2 · Raio-X das tabelas · *Básico*

Crie `raio_x(df)` que retorna um DataFrame com tipo, número de nulos, % de nulos e valores únicos por coluna. Rode em `orders` e `products`. Você vai achar colunas com o erro de digitação `lenght`: renomeie-as para `length` usando `rename(columns=lambda c: ...)`.

#### 5.3 · Exportando recortes · *Intermediário*

Salve uma amostra de 1.000 pedidos (`sample`, `random_state=42`) em JSON (`orient="records"`) e em Excel, com uma aba por `order_status`.

### B. Datas

#### 5.4 · Convertendo todas as datas · *Básico*

Escreva `converter_datas(df)` que encontra, via regex, as colunas terminadas em `_timestamp`, `_date` ou `_at` e converte todas com `pd.to_datetime(errors="coerce")`.

#### 5.5 · Prazo e atraso · *Intermediário*

Nos pedidos com status `delivered`, calcule os dias entre compra e entrega e os dias de atraso em relação à data estimada. Qual a % de pedidos atrasados? Qual estado (`customer_state`) tem a maior taxa de atraso?

#### 5.6 · Quando as pessoas compram? · *Intermediário*

Conte pedidos por dia da semana (em português, na ordem seg→dom), por hora do dia e por mês (`dt.to_period("M")`). Em que horário e em que mês houve mais pedidos?

### C. Limpeza e regex

#### 5.7 · Limpando os comentários · *Intermediário*

Escreva `limpar_texto(txt)` para `review_comment_message`: minúsculas, sem acentos (`unicodedata`), sem pontuação e sem espaços repetidos. Trate valores nulos.

#### 5.8 · Extraindo informação do texto · *Intermediário*

**(a)** Com `.str.extract`, capture o número de dias citado em frases como "chegou em 3 dias". **(b)** Com `.str.contains` e uma regex com `\b` e alternância (`|`), marque comentários com reclamações ("não recebi", "defeito", "péssimo", "devolver"...). A nota média de quem reclama é menor?

#### 5.9 · CEP e cidades · *Intermediário*

O `customer_zip_code_prefix` é lido como número e perde o zero à esquerda (`01037` vira `1037`). Corrija de duas formas: com `dtype=` no `read_csv` e com `.astype(str).str.zfill(5)`. Depois compare `customer_city` e `seller_city`: padronize os nomes (espaços, maiúsculas, acentos) e conte quantas cidades "diferentes" eram, na verdade, a mesma.

#### 5.10 · Lambda para categorizar · *Básico*

Crie a coluna `sentimento` a partir de `review_score` (1–2 negativo, 3 neutro, 4–5 positivo) usando `.apply(lambda ...)`. Refaça com `pd.cut` e compare.

### D. Modularização

#### 5.11 · Pacote `olist/` · *Intermediário*

Mova as funções dos exercícios anteriores para `olist/carregar.py`, `olist/limpeza.py` e `olist/metricas.py`. Em `metricas.py`, crie `taxa_atraso(df, por=None)` que retorna a taxa geral ou agrupada pela coluna informada.

### E. Pandas

#### 5.12 · Tabela analítica · *Intermediário*

Junte `orders` + `customers` + `order_items` + `products` + tradução de categorias. Compare o número de linhas antes e depois de cada `merge` e explique por que ele aumenta: qual é a **granularidade** da tabela final?

#### 5.13 · `groupby` · *Intermediário*

Calcule receita (`price + freight_value`), número de pedidos distintos (`nunique`) e de itens por categoria em inglês; mostre o top 10. Depois calcule o ticket médio por pedido em cada estado (cuidado: some os itens do pedido antes de tirar a média).

#### 5.14 · `pivot_table` · *Intermediário*

Monte estado × tipo de pagamento com o valor total pago. Converta para % da linha: em que estados o boleto pesa mais?

#### 5.15 · Clientes recorrentes · *Desafio*

Cada pedido gera um `customer_id` novo; o cliente real é o `customer_unique_id`. Quantos clientes compraram mais de uma vez? Que % isso representa?

### F. NumPy

#### 5.16 · Peso cubado · *Intermediário*

Transportadoras cobram pelo maior valor entre peso real e peso cubado (`C × A × L / 6000`, em kg). Calcule os dois para todos os produtos com arrays NumPy, o peso taxado com `np.maximum`, e a % de produtos em que o cubado vence.

#### 5.17 · Outliers por broadcasting · *Intermediário*

Monte uma matriz `(n, 2)` com `price` e `freight_value`, padronize as duas colunas de uma vez (z-score) e conte os itens com `|z| > 3` em qualquer coluna. **Bônus:** z-score do frete dentro de cada estado com `groupby().transform`.

#### 5.18 · Atraso × nota · *Desafio*

Calcule a correlação entre dias de entrega e `review_score` com `np.corrcoef`. Depois crie faixas com `np.select` ("no prazo", "até 7 dias", "mais de 7 dias" de atraso) e compare a nota média de cada faixa.

## Bloco 6 — De JSON de API para tabela

APIs costumam devolver JSON aninhado: dicionários dentro de dicionários e listas dentro de registros. O objetivo aqui é transformar esse JSON em **tabelas limpas**, uma para cada "nível" do dado, ligadas por chave.

Os exemplos usam a [DummyJSON](https://dummyjson.com) ([documentação de produtos](https://dummyjson.com/docs/products)), uma API pública e gratuita de produtos. Se vocês usam outra API, os mesmos passos valem: basta trocar a URL e os nomes dos campos. Cada produto vem assim (resumido):

```json
{
  "products": [
    {
      "id": 1, "title": "Essence Mascara Lash Princess", "category": "beauty",
      "price": 9.99, "discountPercentage": 10.48, "stock": 99, "brand": "Essence",
      "tags": ["beauty", "mascara"],
      "dimensions": {"width": 15.14, "height": 13.08, "depth": 22.99},
      "warrantyInformation": "1 week warranty",
      "shippingInformation": "Ships in 3-5 business days",
      "reviews": [
        {"rating": 3, "comment": "Would not recommend!", "date": "2025-04-30T09:41:02.053Z",
         "reviewerName": "Eleanor Collins", "reviewerEmail": "eleanor.collins@x.dummyjson.com"}
      ],
      "meta": {"createdAt": "2025-10-09T14:47:01.588Z", "updatedAt": "2026-05-23T11:27:41.868Z", "barcode": "5784719087687"},
      "images": ["https://cdn.dummyjson.com/.../1.webp"]
    }
  ],
  "total": 194, "skip": 0, "limit": 30
}
```

Repare nos **três tipos de aninhamento**:

| Tipo | Exemplo | Vira |
| --- | --- | --- |
| Dicionário | `dimensions`, `meta` | colunas |
| Lista de valores | `tags`, `images` | linhas |
| Lista de dicionários | `reviews` | uma tabela própria |

### A. Buscando os dados

#### 6.1 · Primeira requisição · *Básico*

Com `requests`, busque <https://dummyjson.com/products>. Verifique o `status_code`, use `raise_for_status()`, liste as chaves do JSON e salve a resposta bruta em `produtos_raw.json`. (Boa prática: guardar o bruto antes de transformar.)

#### 6.2 · Paginação · *Intermediário*

A API devolve 30 produtos por vez e informa `total`, `skip` e `limit`. Escreva `buscar_todos(url, limite=50)` que percorre as páginas com `?limit=...&skip=...` até juntar todos os produtos. Adicione `timeout` e trate erro de conexão com `try/except`.

### B. Achatando

#### 6.3 · O problema · *Básico*

Crie `pd.DataFrame(produtos)` e veja o que acontece com `dimensions`, `reviews` e `tags`. Escreva uma linha de código que liste as colunas cujos valores são `dict` ou `list`.

#### 6.4 · `json_normalize` para dicionários · *Básico*

Use `pd.json_normalize(produtos, sep="_")` e confira as novas colunas (`dimensions_width`, `meta_createdAt`...). Teste também `max_level=0`. Depois calcule, de forma vetorizada, o volume (`width × height × depth`) e o preço final com desconto.

#### 6.5 · Lista de dicionários → tabela filha · *Intermediário*

Gere a tabela de avaliações com `json_normalize(produtos, record_path="reviews", meta=["id", "title", "category"], record_prefix="review_")`. Renomeie `id` para `product_id`. Quantas avaliações e qual a nota média por produto?

#### 6.6 · Lista de valores → linhas · *Intermediário*

Use `.explode("tags")` para criar a tabela `(product_id, tag)`. Atenção: `explode` repete o índice e gera `NaN` para listas vazias. Resolva com `ignore_index=True` e `dropna()`. Depois monte `pd.crosstab` de categoria × tag. Faça o mesmo para `images` e conte as imagens por produto.

### C. Limpando o que veio da API

#### 6.7 · Textos que escondem números · *Intermediário*

**(a)** Converta `warrantyInformation` (`"1 week warranty"`, `"3 months warranty"`, `"2 year warranty"`, `"No warranty"`, `"Lifetime warranty"`) em dias com regex. **(b)** Extraia de `shippingInformation` (`"Ships in 3-5 business days"`, `"Ships in 2 weeks"`, `"Ships overnight"`) o prazo mínimo e máximo em dias com `.str.extract` e grupos nomeados `(?P<min>...)`. **(c)** Converta as datas ISO com `pd.to_datetime(utc=True)`. **(d)** Preencha `brand` ausente com `"Sem marca"`. **(e)** Extraia o domínio do e-mail dos avaliadores.

### D. Resultado final

#### 6.8 · Modelo relacional · *Intermediário*

Monte quatro tabelas: `produtos` (sem colunas de lista), `reviews`, `tags` e `imagens`, todas com `product_id`. Salve num Excel com uma aba por tabela. **Dica:** o Excel não aceita datas com fuso horário, então use `.dt.tz_localize(None)` antes de salvar. Valide: a soma de avaliações por produto bate com o total de `reviews` no JSON?

#### 6.9 · Função genérica · *Desafio*

Escreva `achatar(registros, chave="id")` que funcione para **qualquer** lista de JSONs: normaliza os dicionários, detecta sozinha as colunas de lista e devolve `(tabela_pai, {nome: tabela_filha})`. Listas de dicionários devem virar colunas; listas simples, uma coluna só. Teste com outro endpoint, como <https://dummyjson.com/users> ou <https://dummyjson.com/carts>.

## Projeto integrador — Relatório mensal de vendas

O objetivo é juntar os quatro blocos num pipeline pequeno, organizado em módulos, que lê dados sujos e gera um relatório.

1. **Dados sujos.** Crie `vendas_sujas.csv` a partir de `vendas.csv`, estragando de propósito: datas em formatos misturados (`05/01/2026`, `2026-01-07`), preços como `"R$ 1.200,00"`, nomes de clientes com espaços extras e letras maiúsculas/minúsculas misturadas.
2. **Módulo `limpeza.py`.** Funções para padronizar datas (`datetime`), converter valores (regex) e normalizar nomes (`.strip().title()`). Cada função com *docstring* e um teste no bloco `if __name__ == "__main__":`.
3. **Módulo `analise.py`.** Com pandas: faturamento por mês e por categoria (`groupby`), junção com clientes (`merge`) e tabela vendedor × mês (`pivot_table`).
4. **NumPy.** Calcule, com operações vetorizadas, o crescimento percentual mês a mês e marque as vendas acima de 2 desvios-padrão da média como "atípicas".
5. **Saída.** Salve o resultado em `relatorio.xlsx` (uma aba por análise) e um `resumo.json` com os números principais: faturamento total, melhor vendedor, melhor categoria e mês com maior crescimento.
6. **`main.py`.** Orquestra tudo com poucas linhas, só importando e chamando funções dos módulos.

**Critérios de avaliação:**

- [ ] o código roda do zero com `python main.py`;
- [ ] nenhuma função tem mais de ~20 linhas;
- [ ] nenhum laço `for` onde uma operação vetorizada resolveria;
- [ ] os números do `resumo.json` batem com uma conferência manual.

## Gabarito comentado

Todas as soluções abaixo foram executadas com o `vendas.csv` de exemplo; os resultados esperados estão nos comentários. Há outras formas corretas de resolver.

### Gabarito do Bloco 1

```python
import csv, json, re
from datetime import datetime, timedelta
import pandas as pd

# 1.1 — next() consome o cabeçalho
with open("vendas.csv", encoding="utf-8") as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)
    linhas = list(leitor)
print(len(linhas), cabecalho)  # 10 linhas

# 1.2 — DictReader/DictWriter; newline="" evita linhas em branco no Windows
with open("vendas.csv", encoding="utf-8") as f, \
     open("vendas_total.csv", "w", newline="", encoding="utf-8") as out:
    leitor = csv.DictReader(f)
    escritor = csv.DictWriter(out, fieldnames=leitor.fieldnames + ["total"])
    escritor.writeheader()
    for linha in leitor:
        linha["total"] = round(int(linha["quantidade"]) * float(linha["preco_unit"]), 2)
        escritor.writerow(linha)

# 1.3 — o csv lê tudo como string; converta os números antes de salvar
with open("vendas.csv", encoding="utf-8") as f:
    dados = [{**l, "id_venda": int(l["id_venda"]), "quantidade": int(l["quantidade"]),
              "preco_unit": float(l["preco_unit"])} for l in csv.DictReader(f)]
with open("vendas.json", "w", encoding="utf-8") as f:
    json.dump(dados, f, indent=2, ensure_ascii=False)

# 1.4 — setdefault cria a chave na primeira vez
resumo = {}
for v in dados:
    r = resumo.setdefault(v["vendedor"], {"qtd_vendas": 0, "faturamento": 0.0})
    r["qtd_vendas"] += 1
    r["faturamento"] = round(r["faturamento"] + v["quantidade"] * v["preco_unit"], 2)
with open("resumo_vendedores.json", "w", encoding="utf-8") as f:
    json.dump(resumo, f, indent=2, ensure_ascii=False)
# Carlos: 4 vendas / 8860.0 · Marina: 3 / 919.2 · Paula: 3 / 10730.0

# 1.5 — ExcelWriter permite várias abas no mesmo arquivo
df = pd.read_csv("vendas.csv")
with pd.ExcelWriter("vendas.xlsx") as w:
    for categoria, grupo in df.groupby("categoria"):
        grupo.to_excel(w, sheet_name=categoria, index=False)
moveis = pd.read_excel("vendas.xlsx", sheet_name="Móveis")  # 2 linhas

# 1.6 — strptime lê, strftime escreve; weekday(): 0 = segunda
DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
for v in dados:
    d = datetime.strptime(v["data"], "%Y-%m-%d")
    print(d.strftime("%d/%m/%Y"), DIAS[d.weekday()])  # 05/01/2026 segunda ...

# 1.7 — subtrair datas gera um timedelta
compras = {}
for v in dados:
    compras.setdefault(v["cliente"], []).append(datetime.strptime(v["data"], "%Y-%m-%d"))
print({c: (max(ds) - min(ds)).days for c, ds in compras.items()})
# Ana 28, Bruno 44, Carla 57, Diego 31, Elisa 22

# 1.8
def data_entrega(data, dias_uteis=5):
    while dias_uteis:
        data += timedelta(days=1)
        if data.weekday() < 5:  # segunda a sexta
            dias_uteis -= 1
    return data
print(data_entrega(datetime(2026, 3, 25)).date())  # 2026-04-01

# 1.9 — \D = "qualquer coisa que não é dígito"; [-11:] descarta o +55
def formatar_tel(t):
    d = re.sub(r"\D", "", t)[-11:]
    return f"({d[:2]}) {d[2:7]}-{d[7:]}"
# todos viram "(41) 99876-5432"

# 1.10 — ? torna pontuação opcional; re.I ignora maiúsculas
RE_EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
RE_CPF = re.compile(r"(\d{3})\.?(\d{3})\.?(\d{3})-?(\d{2})")
RE_VALOR = re.compile(r"R\$\s*([\d.]+(?:,\d{1,2})?)", re.I)
validos, sem_email = [], []
for reg in registros:
    email, cpf, valor = RE_EMAIL.search(reg), RE_CPF.search(reg), RE_VALOR.search(reg)
    item = {
        "email": email.group() if email else None,
        "cpf": "{}.{}.{}-{}".format(*cpf.groups()) if cpf else None,
        "valor": float(valor.group(1).replace(".", "").replace(",", ".")) if valor else None,
    }
    (validos if email else sem_email).append(item)
# sem_email: Bruno (bruno@empresa não tem domínio com ponto)
# valores: 1250.5, 89.9, 3000.0, 12.0
```

### Gabarito do Bloco 2

```python
# 2.1
def calcular_total(quantidade, preco_unit):
    return round(quantidade * preco_unit, 2)
calcular_total(3, 89.90)  # 269.7

# 2.2
def aplicar_desconto(valor, percentual=10):
    return valor * (1 - percentual / 100)
aplicar_desconto(100)                 # 90.0
aplicar_desconto(100, 20)             # 80.0
aplicar_desconto(100, percentual=25)  # 75.0

# 2.3 — retornar vários valores = retornar uma tupla
def estatisticas(valores):
    if not valores:
        raise ValueError("A lista não pode estar vazia")
    return min(valores), max(valores), sum(valores) / len(valores)
mn, mx, md = estatisticas([10, 20, 30])  # 10, 30, 20.0

# 2.4 — *linhas vira tupla, **opcoes vira dicionário
def montar_relatorio(titulo, *linhas, **opcoes):
    maiusc = opcoes.get("maiusculas", False)
    sep = opcoes.get("separador", "-")
    print(titulo.upper() if maiusc else titulo)
    print(sep * len(titulo))
    for i, linha in enumerate(linhas, start=1):
        print(f"{i}. {linha.upper() if maiusc else linha}")
montar_relatorio("Vendas", "Notebook", "Mouse", maiusculas=True, separador="=")

# 2.5 — fullmatch exige que o texto INTEIRO siga o padrão
def converter_valor_br(texto):
    m = re.fullmatch(r"\s*R\$\s*(\d{1,3}(?:\.\d{3})*|\d+)(?:,(\d{1,2}))?\s*", texto, re.I)
    if not m:
        raise ValueError(f"Valor inválido: {texto!r}")
    return float(m.group(1).replace(".", "") + "." + (m.group(2) or "0"))
converter_valor_br("R$ 1.250,50")  # 1250.5

# 2.6
sorted(produtos, key=lambda p: p[1], reverse=True)
# Notebook, Monitor, Teclado, Mouse

# 2.7
list(filter(lambda p: p[1] > 200, produtos))
list(map(lambda p: (p[0], round(p[1] * 0.85, 2)), produtos))
[p for p in produtos if p[1] > 200]                 # mesma coisa, mais legível
[(nome, round(preco * 0.85, 2)) for nome, preco in produtos]

# 2.8 — closure: a lambda "lembra" o percentual
def criar_desconto(percentual):
    return lambda valor: valor * (1 - percentual / 100)
black_friday = criar_desconto(30)
black_friday(100)  # 70.0
```

**2.9 —** `import utils_dados` exige o prefixo (`utils_dados.calcular_total(...)`) e deixa claro de onde vem cada função; `from ... import` traz o nome direto para o seu código (mais curto, mas pode colidir com outros nomes); `as ud` cria um apelido, como em `import pandas as pd`.

**2.10 —** Quando um arquivo é executado diretamente, `__name__` vale `"__main__"`; quando é importado, vale o nome do módulo (`"meu_pacote.limpeza"`). Por isso o bloco de testes só roda com `python meu_pacote/limpeza.py`. O `__init__.py` marca a pasta como pacote e pode reexportar funções: `from .limpeza import converter_valor_br`. Em `main.py`: `from meu_pacote.limpeza import converter_valor_br`.

### Gabarito do Bloco 3

```python
import pandas as pd

# 3.1
fat = pd.Series([12500, 9800, 15300], index=["jan", "fev", "mar"])
fat["fev"]         # 9800
fat.idxmax()       # 'mar'
fat.pct_change()   # NaN, -21,6%, +56,1%

# 3.2 — clientes = pd.DataFrame(clientes)

# 3.3
vendas = pd.read_csv("vendas.csv", parse_dates=["data"])
vendas["total"] = vendas["quantidade"] * vendas["preco_unit"]

# 3.4
vj = pd.read_json("vendas.json")
vx = pd.read_excel("vendas.xlsx", sheet_name="Móveis")
print(vj.shape, vj.dtypes)  # (10, 8); atenção: 'data' pode vir como texto ou datetime

# 3.5
df = pd.DataFrame({"produto": ["Café", "Pão"], "preco": [12.5, 0.8]})
df.to_csv("br.csv", sep=";", decimal=",", index=False, encoding="latin-1")
pd.read_csv("br.csv", sep=";", decimal=",", encoding="latin-1")  # preco como float

# 3.6 — iloc usa POSIÇÃO (fim exclusivo); loc usa RÓTULO (fim inclusivo)
vendas.iloc[:3, [2, 8]]                 # colunas 2 = cliente, 8 = total
vendas.loc[:2, ["cliente", "total"]]    # rótulos 0, 1 e 2

# 3.7 — use & e | com parênteses em cada condição
vendas[(vendas["categoria"] == "Eletrônicos") & (vendas["total"] > 2000)]  # ids 1, 3, 5
vendas[vendas["vendedor"].isin(["Carlos", "Paula"]) & (vendas["data"].dt.month == 3)]  # ids 7, 9, 10
vendas[vendas["produto"].str.contains("o")]  # Notebook, Mouse, Monitor, Teclado
vendas[vendas["vendedor"].isin(["Marina", "Paula"])]

# 3.8 — agregação nomeada
resumo = (vendas.groupby("categoria")
          .agg(faturamento=("total", "sum"), ticket_medio=("total", "mean"),
               n_vendas=("id_venda", "count"), itens=("quantidade", "sum"))
          .sort_values("faturamento", ascending=False))
# Eletrônicos 16650.0 | 4162.5 | 4 | 6
# Móveis       2480.0 | 1240.0 | 2 | 2
# Acessórios   1379.2 |  344.8 | 4 | 11

# 3.9 — how="left" mantém todas as vendas; cliente sem cadastro fica com NaN
m = vendas.merge(clientes, on="cliente", how="left")
m.groupby("cidade")["total"].sum().sort_values(ascending=False)
# Porto Alegre 9750.0 · Curitiba 7549.5 · São Paulo 3209.7

# 3.10
vendas["mes"] = vendas["data"].dt.to_period("M").astype(str)
pv = vendas.pivot_table(index="vendedor", columns="mes", values="total",
                        aggfunc="sum", fill_value=0, margins=True)
pv.drop(index="All", columns="All").idxmax()
# jan: Carlos (6900) · fev: Paula (9580) · mar: Carlos (1960) · total geral: 20509.2
```

### Gabarito do Bloco 4

```python
import numpy as np, time

# 4.1
a = np.arange(1, 21); b = np.linspace(0, 1, 5); c = np.zeros((3, 4)); d = np.eye(3)
for x in (a, b, c, d):
    print(x.shape, x.ndim, x.dtype)

# 4.2
m = np.arange(1, 13).reshape(3, 4)
m[1]; m[:, -1]; m[0, 2]; m[:2, -2:]   # [5 6 7 8], [4 8 12], 3, [[3 4] [7 8]]

# 4.3 — máscara = array de True/False usado como filtro
notas = np.random.default_rng(42).uniform(0, 10, 1000)
(notas >= 7).sum()            # 304 (True conta como 1)
notas[notas < 5].mean()       # ≈ 2.453
notas = np.where(notas < 2, 0, notas)

# 4.4
q = np.array([1, 3, 2, 1, 2]); p = np.array([4500, 89.9, 1200, 250, 4300])
totais = q * p                # [4500. 269.7 2400. 250. 8600.]
totais.sum()                  # 16019.7
totais.sum() / q.sum()        # ≈ 1779.97 (ou np.average(p, weights=q))

# 4.5 — NumPy costuma ser 10 a 50× mais rápido
t0 = time.perf_counter(); s = sum(k * k for k in range(1, 1_000_001)); t1 = time.perf_counter()
v = np.arange(1, 1_000_001, dtype=np.int64); s2 = (v * v).sum(); t2 = time.perf_counter()
print(s == s2, t1 - t0, t2 - t1)   # True · soma = 333333833333500000

# 4.6
lojas = np.array([[100, 120, 90], [80, 95, 110], [150, 130, 160], [60, 70, 65]])
lojas.sum(axis=1)             # por loja (soma ao longo das colunas)
lojas.sum(axis=0)             # por mês
lojas.sum(axis=1).argmax()    # 2 (terceira loja)
np.sqrt(lojas); np.log(lojas)

# 4.7
np.round(p * 1.08 / 5.40, 2)  # [900. 17.98 240. 50. 860.]

# 4.8 — as formas são comparadas da direita: (4, 3) e (3,) → o 3 bate, o vetor é "esticado" nas 4 linhas
qtd = np.array([[2, 1, 0], [5, 2, 1], [0, 3, 2], [1, 1, 1]])
precos = np.array([89.9, 250, 1200])
fat = qtd * precos            # (4, 3)

# 4.9 — media e desvio têm forma (3,), aplicados a cada linha
x = np.random.default_rng(1).normal(50, 10, (100, 3))
z = (x - x.mean(axis=0)) / x.std(axis=0)
z.mean(axis=0).round(6), z.std(axis=0)   # ≈ [0 0 0], [1 1 1]

# 4.10 — (5,1,2) - (1,5,2) → (5,5,2): todas as diferenças entre pares
pts = np.random.default_rng(0).random((5, 2))
dist = np.sqrt(((pts[:, None, :] - pts[None, :, :]) ** 2).sum(axis=-1))
aux = dist.copy(); np.fill_diagonal(aux, np.inf)   # ignora distância de um ponto a ele mesmo
i, j = np.unravel_index(aux.argmin(), aux.shape)   # pontos 3 e 4, distância ≈ 0.215
```

### Gabarito do Bloco 5 (Olist)

> As soluções foram testadas numa amostra com o mesmo esquema do dataset; os números do dataset real serão diferentes, por isso não há resultados esperados aqui.

```python
from pathlib import Path
import re, unicodedata
import numpy as np
import pandas as pd

# 5.1 — Path.stem = nome do arquivo sem extensão
def carregar_olist(pasta="dados"):
    tabelas = {}
    for arq in sorted(Path(pasta).glob("*.csv")):
        nome = re.sub(r"^olist_|_dataset$", "", arq.stem)
        tabelas[nome] = pd.read_csv(arq)
    return tabelas
t = carregar_olist()
for nome, df in t.items():
    print(f"{nome:40} {df.shape}")

# 5.2
def raio_x(df):
    return pd.DataFrame({
        "tipo": df.dtypes, "nulos": df.isna().sum(),
        "pct_nulos": (df.isna().mean() * 100).round(1), "unicos": df.nunique(),
    })
raio_x(t["orders"])
t["products"] = t["products"].rename(columns=lambda c: c.replace("lenght", "length"))

# 5.3 — sheet_name=None lê todas as abas num dicionário
amostra = t["orders"].sample(1000, random_state=42)
amostra.to_json("amostra_pedidos.json", orient="records", indent=2, force_ascii=False)
with pd.ExcelWriter("pedidos_por_status.xlsx") as w:
    for status, g in amostra.groupby("order_status"):
        g.to_excel(w, sheet_name=status, index=False)

# 5.4 — errors="coerce" transforma vazios/inválidos em NaT
def converter_datas(df):
    cols = [c for c in df.columns if re.search(r"(_timestamp|_date|_at)$", c)]
    df = df.copy()
    df[cols] = df[cols].apply(pd.to_datetime, errors="coerce")
    return df
orders = converter_datas(t["orders"])

# 5.5 — subtrair colunas datetime gera timedelta; .dt.days extrai os dias
ent = orders[orders["order_status"] == "delivered"].copy()
ent["dias_entrega"] = (ent["order_delivered_customer_date"] - ent["order_purchase_timestamp"]).dt.days
ent["dias_atraso"] = (ent["order_delivered_customer_date"] - ent["order_estimated_delivery_date"]).dt.days
ent["atrasado"] = ent["dias_atraso"] > 0
print(f"{ent['atrasado'].mean():.1%} atrasados")   # média de booleanos = proporção
(ent.merge(t["customers"], on="customer_id")
    .groupby("customer_state")["atrasado"].mean().sort_values(ascending=False))

# 5.6
ts = orders["order_purchase_timestamp"]
DIAS = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
ts.dt.dayofweek.map(dict(enumerate(DIAS))).value_counts().reindex(DIAS)
ts.dt.hour.value_counts().idxmax()
ts.dt.to_period("M").value_counts().idxmax()

# 5.7 — NFKD separa a letra do acento; encode("ascii", "ignore") descarta o acento
def limpar_texto(txt):
    if pd.isna(txt):
        return ""
    txt = unicodedata.normalize("NFKD", txt.lower()).encode("ascii", "ignore").decode()
    txt = re.sub(r"[^\w\s]", " ", txt)      # pontuação vira espaço
    return re.sub(r"\s+", " ", txt).strip()  # espaços repetidos viram um
rev = t["order_reviews"].copy()
rev["msg_limpa"] = rev["review_comment_message"].apply(limpar_texto)

# 5.8 — o texto já está sem acento, então a regex também fica sem acento
rev["dias_citados"] = rev["msg_limpa"].str.extract(r"(\d+)\s*dias?")[0].astype(float)
RECLAMACAO = r"\b(?:nao recebi|defeito|pessim\w*|devolv\w*|quebrad\w*)\b"
rev["reclamacao"] = rev["msg_limpa"].str.contains(RECLAMACAO, regex=True)
rev.groupby("reclamacao")["review_score"].mean()

# 5.9
cust = pd.read_csv("dados/olist_customers_dataset.csv", dtype={"customer_zip_code_prefix": str})
# ou: t["customers"]["customer_zip_code_prefix"].astype(str).str.zfill(5)
antes = t["sellers"]["seller_city"].nunique()
depois = t["sellers"]["seller_city"].map(limpar_texto).nunique()
print(antes - depois, "nomes eram variações da mesma cidade")

# 5.10 — pd.cut é vetorizado e mais rápido que apply em bases grandes
rev["sentimento"] = rev["review_score"].apply(
    lambda n: "negativo" if n <= 2 else "neutro" if n == 3 else "positivo")
rev["sentimento2"] = pd.cut(rev["review_score"], bins=[0, 2, 3, 5],
                            labels=["negativo", "neutro", "positivo"])

# 5.11 — olist/metricas.py
def taxa_atraso(df, por=None):
    if por is None:
        return df["atrasado"].mean()
    return df.groupby(por)["atrasado"].mean().sort_values(ascending=False)

# 5.12 — depois de order_items, cada linha é um ITEM de pedido, não um pedido
base = (orders
    .merge(t["customers"], on="customer_id", how="left")
    .merge(t["order_items"], on="order_id", how="inner")
    .merge(t["products"][["product_id", "product_category_name"]], on="product_id", how="left")
    .merge(t["product_category_name_translation"], on="product_category_name", how="left"))
print(len(orders), len(base), base["order_id"].nunique())

# 5.13 — dropna=False mantém produtos sem categoria no resultado
base["receita"] = base["price"] + base["freight_value"]
(base.groupby("product_category_name_english", dropna=False)
     .agg(receita=("receita", "sum"), pedidos=("order_id", "nunique"), itens=("order_item_id", "count"))
     .sort_values("receita", ascending=False).head(10))
por_pedido = base.groupby(["order_id", "customer_state"], as_index=False)["receita"].sum()
por_pedido.groupby("customer_state")["receita"].mean().sort_values(ascending=False)

# 5.14 — div(..., axis=0) divide cada linha pelo total da linha
pag = (t["order_payments"]
       .merge(t["orders"][["order_id", "customer_id"]], on="order_id")
       .merge(t["customers"][["customer_id", "customer_state"]], on="customer_id"))
pv = pag.pivot_table(index="customer_state", columns="payment_type", values="payment_value",
                     aggfunc="sum", fill_value=0)
pct = pv.div(pv.sum(axis=1), axis=0) * 100
pct.sort_values("boleto", ascending=False)

# 5.15
compras = (t["orders"].merge(t["customers"], on="customer_id")
           .groupby("customer_unique_id")["order_id"].nunique())
print((compras > 1).sum(), f"{(compras > 1).mean():.1%}")

# 5.16
p = t["products"].dropna(subset=["product_weight_g", "product_length_cm"])
C, A, L = (p[c].to_numpy() for c in ["product_length_cm", "product_height_cm", "product_width_cm"])
peso_real = p["product_weight_g"].to_numpy() / 1000
peso_cubado = C * A * L / 6000
peso_taxado = np.maximum(peso_real, peso_cubado)   # elemento a elemento
(peso_cubado > peso_real).mean()

# 5.17 — x.mean(axis=0) tem forma (2,) e é "esticado" nas n linhas
x = base[["price", "freight_value"]].to_numpy()
z = (x - x.mean(axis=0)) / x.std(axis=0)
(np.abs(z) > 3).any(axis=1).sum()
base["z_frete_uf"] = (base.groupby("customer_state")["freight_value"]
                      .transform(lambda s: (s - s.mean()) / s.std()))

# 5.18
er = ent.merge(t["order_reviews"][["order_id", "review_score"]], on="order_id")
np.corrcoef(er["dias_entrega"], er["review_score"])[0, 1]
faixa = np.select([er["dias_atraso"] <= 0, er["dias_atraso"] <= 7],
                  ["no prazo", "até 7 dias"], default="mais de 7 dias")
er.groupby(faixa)["review_score"].mean()
```

### Gabarito do Bloco 6 (JSON de API)

```python
import json, re
import numpy as np
import pandas as pd
import requests

URL = "https://dummyjson.com/products"

# 6.1
resp = requests.get(URL, timeout=10)
resp.raise_for_status()          # levanta erro se status for 4xx/5xx
bruto = resp.json()
print(resp.status_code, bruto.keys())   # products, total, skip, limit
with open("produtos_raw.json", "w", encoding="utf-8") as f:
    json.dump(bruto, f, indent=2, ensure_ascii=False)

# 6.2
def buscar_todos(url, limite=50):
    itens, skip = [], 0
    while True:
        try:
            r = requests.get(url, params={"limit": limite, "skip": skip}, timeout=10)
            r.raise_for_status()
        except requests.RequestException as erro:
            print("Falha na página", skip, erro)
            break
        pagina = r.json()
        itens.extend(pagina["products"])
        skip += limite
        if skip >= pagina["total"]:
            break
    return itens
produtos = buscar_todos(URL)

# 6.3
ingenuo = pd.DataFrame(produtos)
[c for c in ingenuo.columns if ingenuo[c].map(lambda v: isinstance(v, (dict, list))).any()]
# ['tags', 'dimensions', 'reviews', 'meta', 'images']

# 6.4 — dicionários viram colunas "pai_filho"; listas continuam como listas
df = pd.json_normalize(produtos, sep="_")
df["volume_cm3"] = df["dimensions_width"] * df["dimensions_height"] * df["dimensions_depth"]
df["preco_final"] = (df["price"] * (1 - df["discountPercentage"] / 100)).round(2)
pd.json_normalize(produtos, max_level=0)   # não achata nada: igual ao DataFrame ingênuo

# 6.5 — record_path = a lista que vira linhas; meta = campos do pai copiados em cada linha
reviews = pd.json_normalize(produtos, record_path="reviews",
                            meta=["id", "title", "category"], record_prefix="review_")
reviews = reviews.rename(columns={"id": "product_id"})
reviews.groupby("product_id")["review_rating"].agg(["count", "mean"])

# 6.6 — sem ignore_index, o índice se repete e o crosstab falha com
#        "cannot reindex on an axis with duplicate labels"
tags = (df[["id", "tags"]].explode("tags", ignore_index=True).dropna()
        .rename(columns={"id": "product_id", "tags": "tag"}))
ex = df[["category", "tags"]].explode("tags", ignore_index=True)
pd.crosstab(ex["category"], ex["tags"])
imagens = (df[["id", "images"]].explode("images", ignore_index=True).dropna()
           .rename(columns={"id": "product_id", "images": "url"}))
imagens.groupby("product_id").size()

# 6.7a — grupo 1 = quantidade, grupo 2 = unidade; o s? aceita singular e plural
DIAS_POR = {"day": 1, "week": 7, "month": 30, "year": 365}
def garantia_em_dias(txt):
    m = re.search(r"(\d+)\s*(day|week|month|year)s?", txt, re.I)
    if m:
        return int(m.group(1)) * DIAS_POR[m.group(2).lower()]
    if re.search(r"lifetime", txt, re.I):
        return np.inf
    return 0   # "No warranty"
df["garantia_dias"] = df["warrantyInformation"].apply(garantia_em_dias)
# "1 week" → 7 · "3 months" → 90 · "2 year" → 730 · "No warranty" → 0

# 6.7b — grupos nomeados viram nomes de coluna; (?:-...)? torna o máximo opcional
prazo = df["shippingInformation"].str.extract(
    r"(?P<min>\d+)(?:-(?P<max>\d+))?\s*(?P<unid>business day|day|week|month)", flags=re.I)
fator = prazo["unid"].str.lower().map({"business day": 1, "day": 1, "week": 7, "month": 30})
df["envio_min_dias"] = prazo["min"].astype(float) * fator
df["envio_max_dias"] = prazo["max"].fillna(prazo["min"]).astype(float) * fator
df.loc[df["shippingInformation"].str.contains("overnight", case=False),
       ["envio_min_dias", "envio_max_dias"]] = 1
# "3-5 business days" → 3 e 5 · "2 weeks" → 14 e 14 · "overnight" → 1 e 1

# 6.7c, d, e
for c in ["meta_createdAt", "meta_updatedAt"]:
    df[c] = pd.to_datetime(df[c], utc=True)
df["brand"] = df["brand"].fillna("Sem marca")
reviews["review_date"] = pd.to_datetime(reviews["review_date"], utc=True)
reviews["dominio_email"] = reviews["review_reviewerEmail"].str.extract(r"@([\w.-]+)$")

# 6.8
produtos_tab = df.drop(columns=["tags", "images", "reviews"]).rename(columns={"id": "product_id"})
tabelas = {"produtos": produtos_tab, "reviews": reviews, "tags": tags, "imagens": imagens}
with pd.ExcelWriter("produtos_tabular.xlsx") as w:
    for nome, tab in tabelas.items():
        tab = tab.copy()
        for c in tab.select_dtypes("datetimetz").columns:
            tab[c] = tab[c].dt.tz_localize(None)   # Excel não aceita fuso
        tab.to_excel(w, sheet_name=nome, index=False)
assert len(reviews) == sum(len(p["reviews"]) for p in produtos)

# 6.9
def achatar(registros, chave="id"):
    base = pd.json_normalize(registros, sep="_")
    cols_lista = [c for c in base.columns
                  if base[c].map(lambda v: isinstance(v, list)).any()]
    filhas = {}
    for c in cols_lista:
        ex = base[[chave, c]].explode(c).dropna(subset=[c])
        if ex[c].map(lambda v: isinstance(v, dict)).all():   # lista de dicionários
            filhas[c] = pd.concat([ex[[chave]].reset_index(drop=True),
                                   pd.json_normalize(ex[c].tolist(), sep="_")], axis=1)
        else:                                                  # lista simples
            filhas[c] = ex.reset_index(drop=True)
    return base.drop(columns=cols_lista), filhas

pai, filhas = achatar(produtos)
print(pai.shape, {nome: t.shape for nome, t in filhas.items()})
```

## Referências para estudo

Material para consultar durante os exercícios ou indicar para a turma. Todos são gratuitos.

| Recurso | Tipo | Para que serve |
| --- | --- | --- |
| [pandas — Working with text data](https://pandas.pydata.org/docs/user_guide/text.html) | Documentação | Todos os métodos `.str` (`extract`, `contains`, `replace` com regex) |
| [pandas — Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) | Documentação | `isna`, `fillna`, `dropna`, tipos de nulo |
| [pandas.json_normalize](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html) | Documentação | `record_path`, `meta`, `sep`, `max_level` (Bloco 6) |
| [DataFrame.explode](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html) | Documentação | Listas em linhas (Bloco 6) |
| [Python — Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html) | Tutorial oficial | Base de regex: grupos, `\b`, `?`, *lookahead* |
| [regex101](https://regex101.com) | Ferramenta | Testar regex e ver a explicação de cada parte (escolha o sabor Python) |
| [RegexOne](https://regexone.com) | Exercícios interativos | Aprender regex do zero, passo a passo |
| [Kaggle Learn — Data Cleaning](https://www.kaggle.com/learn/data-cleaning) | Curso curto com notebooks | Nulos, escala, datas, encoding, entradas inconsistentes |
| [Kaggle Learn — Pandas](https://www.kaggle.com/learn/pandas) | Curso curto com notebooks | Seleção, `groupby`, tipos, renomear e combinar |
| [Real Python — Pythonic Data Cleaning With pandas and NumPy](https://realpython.com/python-data-cleaning-numpy-pandas/) | Tutorial | Limpeza passo a passo com `.str` e regex num dataset real |
| [guipsamora/pandas_exercises](https://github.com/guipsamora/pandas_exercises) | Lista de exercícios (GitHub) | 11 temas (filtros, `groupby`, `merge`, `apply`, séries temporais) com soluções comentadas |
| [Python for Data Analysis, 3ª ed.](https://wesmckinney.com/book/) | Livro online (inglês) | Referência completa do criador do pandas; cap. 7 trata de limpeza e regex |

> **Sugestão de uso:** a turma resolve os Blocos 1 e 5.7–5.9 consultando a documentação de texto do pandas e o regex101 aberto ao lado; a lista do GitHub serve como treino extra de `groupby` e `merge`.

### Todos os links (para copiar)

**Dados e APIs**

- Olist no Kaggle: <https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce>
- DummyJSON: <https://dummyjson.com>
- DummyJSON produtos: <https://dummyjson.com/docs/products>
- DummyJSON users: <https://dummyjson.com/users>
- DummyJSON carts: <https://dummyjson.com/carts>

**Bibliotecas (PyPI)**

- pandas: <https://pypi.org/project/pandas/>
- numpy: <https://pypi.org/project/numpy/>
- openpyxl: <https://pypi.org/project/openpyxl/>
- requests: <https://pypi.org/project/requests/>

**Documentação do Python**

- csv: <https://docs.python.org/pt-br/3/library/csv.html>
- re: <https://docs.python.org/pt-br/3/library/re.html>
- Regex HOWTO: <https://docs.python.org/3/howto/regex.html>

**Documentação do pandas**

- Text data: <https://pandas.pydata.org/docs/user_guide/text.html>
- Missing data: <https://pandas.pydata.org/docs/user_guide/missing_data.html>
- json_normalize: <https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html>
- explode: <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html>

**Estudo e prática**

- regex101: <https://regex101.com>
- RegexOne: <https://regexone.com>
- Kaggle Data Cleaning: <https://www.kaggle.com/learn/data-cleaning>
- Kaggle Pandas: <https://www.kaggle.com/learn/pandas>
- Real Python: <https://realpython.com/python-data-cleaning-numpy-pandas/>
- pandas_exercises: <https://github.com/guipsamora/pandas_exercises>
- Python for Data Analysis: <https://wesmckinney.com/book/>
