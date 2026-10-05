# Python Exercises

Material de estudo e exercícios de Python, do zero até análise de dados com Pandas, APIs, complexidade de algoritmos e noções de engenharia de dados.

O repositório está dividido em quatro áreas:

| Pasta | O que tem |
| --- | --- |
| [documentos/](documentos/) | Guias para preparar o ambiente, organizar o raciocínio e teoria dos tópicos básicos |
| [data_analysis/](data_analysis/) | Demonstrações e exercícios de análise de dados (notebooks com Pandas) |
| [exercicios_resolvidos/](exercicios_resolvidos/) | Soluções para conferir os resultados e estudar os passos |
| [materiais_de_apoio/](materiais_de_apoio/) | Videoaulas e textos de consulta para revisar conteúdos |

Para a rotina de preparação antes das aulas e para trabalhar numa cópia própria (fork), veja o [guia_geral.md](guia_geral.md).

## Como começar

Ainda não tem Python, VS Code ou Git instalados? Siga primeiro os guias de instalação:

- [Guia: Python, VS Code, Git e GitHub](documentos/install_python_git_vscode/Install_python_git_github_vscode.md)
- [Habilitar o Jupyter Notebook no VS Code](documentos/install_python_git_vscode/habilitar_jupyter_notebook.md)
- [Guia básico para trabalhar com o VS Code (PDF)](documentos/guia_basico_trabalhar_com_vscode/guia_basico_vscode.pdf)

Depois, clone este repositório:

```bash
git clone https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises.git
cd python_exercises
```

### Instalando bibliotecas

Alguns tópicos usam bibliotecas externas. Veja o passo a passo em [Como instalar pacotes no Python](documentos/pip_install_bibliotecas/pip_install_bibiotecas.md). Para instalar as principais de uma vez:

```bash
pip install pandas numpy requests scikit-learn
```

| Biblioteca | Usada em |
| --- | --- |
| `pandas` | Notebooks de `data_analysis/` e de datas, funções e regex |
| `numpy` | Ordem de complexidade (exercícios 1 e 2) |
| `requests` | Exercícios com API e Guia de APIs |
| `scikit-learn` | Pseudocódigo (exercício 15, apenas exemplo) |

## Conteúdo

Sugestão de ordem de estudo.

### 1. Documentos

Guias e teoria, em [documentos/](documentos/):

| Tópico | Arquivo |
| --- | --- |
| Como resolver exercícios (fluxograma com Python e Pandas) | [guia_alunos_fluxograma_python_pandas.pdf](documentos/como_resolver_exercicios/guia_alunos_fluxograma_python_pandas.pdf) |
| Variáveis, strings e números | [variaveis.md](documentos/estruturas_basicas/variaveis/variaveis.md) |
| Listas | [listas.md](documentos/estruturas_basicas/listas/listas.md) |
| Listas com `for`, `range`, slices e tuplas | [listas_for_range.md](documentos/estruturas_basicas/listas_for_range/listas_for_range.md) |
| Condicionais (`if`, `elif`, `else`) | [if_else.md](documentos/estruturas_basicas/if_else/if_else.md) |
| Dicionários | [dicionarios.md](documentos/estruturas_basicas/dicionarios/dicionarios.md) |
| Entrada de dados e `while` | [while.md](documentos/estruturas_basicas/while/while.md) |
| Arquivos, exceções e JSON | [arquivos_excecoes_json.md](documentos/estruturas_basicas/arquivos_excecoes_json/arquivos_excecoes_json.md) |
| Python para dados | [python_para_dados.md](documentos/python_para_dados/python_para_dados.md) |
| Guia de APIs REST (verbos, status HTTP, autenticação) | [guia_de_apis.md](documentos/guia_de_apis/guia_de_apis.md) |
| Engenharia de dados (material só de leitura) | [engenharia_de_dados.md](documentos/engenharia_de_dados/engenharia_de_dados.md) |

### 2. Análise de dados

Notebooks em [data_analysis/](data_analysis/), organizados por nível:

| Pasta | O que tem |
| --- | --- |
| [demo1/](data_analysis/demo1/) | Demonstração com uma tabela de alunos |
| [exercicios_nivel_1/](data_analysis/exercicios_nivel_1/) | Pandas básico: academia, loja de roupas e papelaria |
| [exercicios_nivel_2/](data_analysis/exercicios_nivel_2/) | Valores nulos (CSV e Excel) e regex. Leia o `LEIA_PRIMEIRO.txt` antes |
| [exercicios_nivel_4/](data_analysis/exercicios_nivel_4/) | Titanic: tabela completa e `merge` de tabelas |

Mantenha os arquivos de dados nas pastas fornecidas, para que os notebooks os encontrem.

### 3. Exercícios resolvidos

Em [exercicios_resolvidos/](exercicios_resolvidos/). Tente resolver cada exercício sozinho antes de olhar a resolução.

**Estruturas básicas** ([estruturas_basicas/](exercicios_resolvidos/estruturas_basicas/)): um script `.py` por exercício.

| Tópico | Pasta |
| --- | --- |
| Variáveis | [variaveis/](exercicios_resolvidos/estruturas_basicas/variaveis/) |
| Listas | [listas/](exercicios_resolvidos/estruturas_basicas/listas/) |
| Listas com `for` e `range` | [listas_for_range/](exercicios_resolvidos/estruturas_basicas/listas_for_range/) |
| Condicionais | [if_else/](exercicios_resolvidos/estruturas_basicas/if_else/) |
| Dicionários | [dicionarios/](exercicios_resolvidos/estruturas_basicas/dicionarios/) |
| `while` | [while/](exercicios_resolvidos/estruturas_basicas/while/) |
| Arquivos, exceções e JSON | [arquivos_excecoes_json/](exercicios_resolvidos/estruturas_basicas/arquivos_excecoes_json/) |
| Funções | [exercicios_funcoes/](exercicios_resolvidos/estruturas_basicas/exercicios_funcoes/) |
| Datas | [trabalhando_com_datas/](exercicios_resolvidos/estruturas_basicas/trabalhando_com_datas/) |

**Notebooks por tema:**

| Tema | Pasta |
| --- | --- |
| Datas e fusos horários | [dates/](exercicios_resolvidos/dates/) |
| Funções | [funcoes/](exercicios_resolvidos/funcoes/) |
| Regex | [regex/](exercicios_resolvidos/regex/) |
| Pandas, NumPy e regex | [pandas_numpy_regex/](exercicios_resolvidos/pandas_numpy_regex/) |

**Prática e reforço:**

| Tópico | O que é | Pasta |
| --- | --- | --- |
| Pseudocódigo | 15 exercícios de lógica, em pseudocódigo e depois em Python | [pseudocodigo/](exercicios_resolvidos/pseudocodigo/) |
| Outros exercícios de Python | Aquecimento A1 a A7 e 18 exercícios com exemplos de ML | [outros_execicios_python/](exercicios_resolvidos/outros_execicios_python/) |
| Ordem de complexidade | Mesmo problema resolvido de várias formas (laços, `dict`, `set`, NumPy) e comparado em Big O | [ordem_complexidade/](exercicios_resolvidos/ordem_complexidade/) |
| Git e Python | Exercícios de Git junto com Python | [exercicios_git_python/](exercicios_resolvidos/exercicios_git_python/) |

**APIs:**

| Tópico | O que é | Pasta |
| --- | --- | --- |
| Exercícios com API | Baixar dados da [dummyjson.com](https://dummyjson.com) em JSON e explorá-los com dicionários, listas, `for` e `if` | [exercicios_API/](exercicios_resolvidos/exercicios_API/) |
| Guia de APIs | Exercícios com `requests` | [guia_de_apis/](exercicios_resolvidos/guia_de_apis/) |

### 4. Materiais de apoio

Textos e videoaulas de consulta, em [materiais_de_apoio/](materiais_de_apoio/):

- [datas_funcoes_regex.md](materiais_de_apoio/datas_funcoes_regex.md): videoaulas sobre datas e fusos, regex, funções e VS Code.
- [git_github_vscode.md](materiais_de_apoio/git_github_vscode.md): Git, GitHub e VS Code.

## Como usar

1. Leia o documento do tópico, quando houver.
2. Tente resolver o exercício sozinho antes de olhar a resolução.
3. Compare com a solução na pasta [exercicios_resolvidos/](exercicios_resolvidos/).

Os scripts `.py` começam com o enunciado num comentário e trazem a resolução em seguida. Para executar:

```bash
python3 exercicios_resolvidos/estruturas_basicas/variaveis/exe01_mensagem_simples.py
```

No Windows, use `py` no lugar de `python3`. Os notebooks `.ipynb` são abertos no VS Code: selecione o kernel Python e execute as células de cima para baixo.

### Atenção

- Vários scripts usam `input()` e esperam que você digite algo no terminal.
- Alguns scripts leem e gravam arquivos ou dependem de arquivos criados por outro script. Nesses casos, execute-os **de dentro** da própria pasta, pois usam caminhos relativos:
  - `exercicios_resolvidos/estruturas_basicas/arquivos_excecoes_json/`: o `aprendizado.txt` já está nela;
  - `exercicios_resolvidos/guia_de_apis/`: precisa de internet, e o `exe01` deve ser executado antes dos demais.

## Estrutura

```text
.
├── guia_geral.md                    # Preparação para as aulas e uso do repositório
├── documentos/                      # Guias e teoria (.md e .pdf)
│   ├── install_python_git_vscode/   # Instalação de Python, Git, VS Code e Jupyter
│   ├── guia_basico_trabalhar_com_vscode/
│   ├── pip_install_bibliotecas/     # Como instalar pacotes
│   ├── como_resolver_exercicios/    # Fluxograma para resolver exercícios
│   ├── estruturas_basicas/          # Variáveis, listas, if/else, dicionários, while, arquivos
│   ├── python_para_dados/           # Python básico com exemplos de dados e ML
│   ├── guia_de_apis/                # Guia de APIs REST
│   └── engenharia_de_dados/         # Fundamentos de engenharia de dados
├── data_analysis/                   # Notebooks de análise de dados
│   ├── demo1/
│   ├── exercicios_nivel_1/
│   ├── exercicios_nivel_2/
│   └── exercicios_nivel_4/
├── exercicios_resolvidos/           # Soluções dos exercícios
│   ├── estruturas_basicas/
│   ├── dates/
│   ├── funcoes/
│   ├── regex/
│   ├── pandas_numpy_regex/
│   ├── pseudocodigo/
│   ├── outros_execicios_python/
│   ├── ordem_complexidade/
│   ├── exercicios_git_python/
│   ├── exercicios_API/
│   └── guia_de_apis/
└── materiais_de_apoio/              # Videoaulas e textos de consulta
```

## Licença

Distribuído sob a licença descrita em [LICENSE](LICENSE).
