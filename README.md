# Python Exercises

Material de estudo e exercícios de Python, do zero até APIs, complexidade de algoritmos e noções de engenharia de dados. Cada tópico tem um **documento** com a teoria e os exercícios resolvidos, e uma pasta com um **script `.py` por exercício**.

## Como começar

Ainda não tem Python, VS Code ou Git instalados? Siga primeiro o guia de instalação:

- [Guia: Python, VS Code, Git e GitHub](documentos/instalacao/install_python_git_vscode/Install_python_git_github_vscode.md)

Depois, clone este repositório:

```bash
git clone https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises.git
cd python_exercises
```

Alguns tópicos usam bibliotecas externas. Para instalar todas de uma vez:

```bash
pip install requests numpy scikit-learn
```

| Biblioteca | Usada em |
| --- | --- |
| `requests` | Exercícios com API e Guia de APIs |
| `numpy` | Ordem de complexidade (exercícios 1 e 2) |
| `scikit-learn` | Pseudocódigo (exercício 15, apenas exemplo) |

## Conteúdo

Sugestão de ordem de estudo. Cada tópico tem a teoria (em `documentos/`) e os scripts (em `exercicios/`).

### 1. Estruturas básicas de Python

Fundamentos da linguagem, em sequência:

| # | Tópico | Teoria | Exercícios |
| --- | --- | --- | --- |
| 1 | Variáveis, strings e números | [variaveis.md](documentos/estruturas_basicas/variaveis/variaveis.md) | [variaveis/](exercicios/estruturas_basicas/variaveis/) |
| 2 | Listas | [listas.md](documentos/estruturas_basicas/listas/listas.md) | [listas/](exercicios/estruturas_basicas/listas/) |
| 3 | Listas com `for`, `range`, slices e tuplas | [listas_for_range.md](documentos/estruturas_basicas/listas_for_range/listas_for_range.md) | [listas_for_range/](exercicios/estruturas_basicas/listas_for_range/) |
| 4 | Condicionais (`if`, `elif`, `else`) | [if_else.md](documentos/estruturas_basicas/if_else/if_else.md) | [if_else/](exercicios/estruturas_basicas/if_else/) |
| 5 | Dicionários | [dicionarios.md](documentos/estruturas_basicas/dicionarios/dicionarios.md) | [dicionarios/](exercicios/estruturas_basicas/dicionarios/) |
| 6 | Entrada de dados e `while` | [while.md](documentos/estruturas_basicas/while/while.md) | [while/](exercicios/estruturas_basicas/while/) |
| 7 | Arquivos, exceções e JSON | [arquivos_excecoes_json.md](documentos/estruturas_basicas/arquivos_excecoes_json/arquivos_excecoes_json.md) | [arquivos_excecoes_json/](exercicios/estruturas_basicas/arquivos_excecoes_json/) |

### 2. Prática e reforço

| Tópico | O que é | Teoria | Exercícios |
| --- | --- | --- | --- |
| Pseudocódigo | 15 exercícios de lógica, em pseudocódigo e depois em Python com explicações | [pseudocodigo.md](documentos/pseudocodigo/pseudocodigo.md) | [pseudocodigo/](exercicios/pseudocodigo/) |
| Python para dados | Sintaxe, decisões, repetições e coleções aplicadas a exemplos de ML (aquecimento A1 a A7 e 18 exercícios) | [python_para_dados.md](documentos/python_para_dados/python_para_dados.md) | [python_para_dados/](exercicios/python_para_dados/) |
| Ordem de complexidade | Mesmo problema resolvido de várias formas (laços, `dict`, `set`, NumPy) e comparado em Big O | [ordem_complexidade.md](documentos/ordem_complexidade/ordem_complexidade.md) | [ordem_complexidade/](exercicios/ordem_complexidade/) |

### 3. APIs

| Tópico | O que é | Teoria | Exercícios |
| --- | --- | --- | --- |
| Exercícios com API | Baixar dados da [dummyjson.com](https://dummyjson.com) em JSON e explorá-los com dicionários, listas, `for` e `if` | [exercicios_API.md](documentos/exercicios_API/exercicios_API.md) | [exercicios_API/](exercicios/exercicios_API/) |
| Guia de APIs | Conceitos de APIs REST (verbos, status HTTP, autenticação), perguntas de entrevista e exercícios com `requests` | [guia_de_apis.md](documentos/guia_de_apis/guia_de_apis.md) | [guia_de_apis/](exercicios/guia_de_apis/) |

### 4. Engenharia de dados

Material só de leitura, sem exercícios: fontes de dados, formatos (JSON, CSV, Parquet), modelos de dados, OLTP e OLAP, ETL e ELT, batch e streaming.

- [engenharia_de_dados.md](documentos/engenharia_de_dados/engenharia_de_dados.md)

### 5. Materiais de apoio

Textos de consulta que complementam os tópicos acima, na pasta [materiais_de_apoio/](materiais_de_apoio/):

- [git_github_vscode.md](materiais_de_apoio/git_github_vscode.md): Git, GitHub e VS Code.

## Como usar

1. Leia o documento do tópico. Ele tem um sumário no início.
2. Tente resolver cada exercício sozinho antes de olhar a resolução.
3. Compare com o script correspondente na pasta de exercícios.

Cada script começa com o enunciado num comentário e traz a resolução em seguida. Para executar:

```bash
python3 exercicios/estruturas_basicas/variaveis/exe01_mensagem_simples.py
```

No Windows, use `py` no lugar de `python3`.

### Atenção

- Vários scripts usam `input()` e esperam que você digite algo no terminal.
- Alguns scripts leem e gravam arquivos ou dependem de arquivos criados por outro script. Nesses casos, execute-os **de dentro** da própria pasta, pois usam caminhos relativos:
  - `exercicios/estruturas_basicas/arquivos_excecoes_json/`: o `aprendizado.txt` já está nela;
  - `exercicios/exercicios_API/`: comece pelo `exe01`, que cria os arquivos JSON usados pelos demais (precisa de internet);
  - `exercicios/guia_de_apis/`: também precisa de internet.

## Estrutura

```text
.
├── documentos/                      # Teoria e exercícios resolvidos (.md)
│   ├── instalacao/                  # Guia de instalação
│   ├── estruturas_basicas/          # Variáveis, listas, if/else, dicionários, while, arquivos
│   ├── pseudocodigo/                # Pseudocódigo e resolução em Python
│   ├── python_para_dados/           # Python básico com exemplos de dados e ML
│   ├── ordem_complexidade/          # Vetores, hash e Big O
│   ├── exercicios_API/              # Exercícios com a API dummyjson
│   ├── guia_de_apis/                # Guia de APIs + exercícios com requests
│   └── engenharia_de_dados/         # Fundamentos de engenharia de dados
├── materiais_de_apoio/              # Textos de consulta (Git, GitHub e VS Code)
└── exercicios/                      # Um script .py por exercício
    ├── estruturas_basicas/
    ├── pseudocodigo/
    ├── python_para_dados/
    ├── ordem_complexidade/
    ├── exercicios_API/
    └── guia_de_apis/
```

## Licença

Distribuído sob a licença descrita em [LICENSE](LICENSE).
