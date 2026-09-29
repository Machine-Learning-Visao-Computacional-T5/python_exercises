# Python Exercises

Material de estudo e exercícios de Python, do zero até arquivos, exceções e JSON. Cada tópico tem um **documento** com a teoria e os exercícios resolvidos, e uma pasta com um **script `.py` por exercício**.

## Como começar

Ainda não tem Python, VS Code ou Git instalados? Siga primeiro o guia de instalação:

- [Guia: Python, VS Code, Git e GitHub](documentos/instalacao/install_python_git_vscode/Install_python_git_github_vscode.md)

Depois, clone este repositório:

```bash
git clone https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises.git
cd python_exercises
```

## Conteúdo

Sugestão de ordem de estudo:

| # | Tópico | Teoria | Exercícios |
| --- | --- | --- | --- |
| 1 | Variáveis, strings e números | [variaveis.md](documentos/estruturas_basicas/variaveis/variaveis.md) | [variaveis/](exercicios/estruturas_basicas/variaveis/) |
| 2 | Listas | [listas.md](documentos/estruturas_basicas/listas/listas.md) | [listas/](exercicios/estruturas_basicas/listas/) |
| 3 | Listas com `for`, `range`, slices e tuplas | [listas_for_range.md](documentos/estruturas_basicas/listas_for_range/listas_for_range.md) | [listas_for_range/](exercicios/estruturas_basicas/listas_for_range/) |
| 4 | Condicionais (`if`, `elif`, `else`) | [if_else.md](documentos/estruturas_basicas/if_else/if_else.md) | [if_else/](exercicios/estruturas_basicas/if_else/) |
| 5 | Dicionários | [dicionarios.md](documentos/estruturas_basicas/dicionarios/dicionarios.md) | [dicionarios/](exercicios/estruturas_basicas/dicionarios/) |
| 6 | Entrada de dados e `while` | [while.md](documentos/estruturas_basicas/while/while.md) | [while/](exercicios/estruturas_basicas/while/) |
| 7 | Arquivos, exceções e JSON | [arquivos_excecoes_json.md](documentos/estruturas_basicas/arquivos_excecoes_json/arquivos_excecoes_json.md) | [arquivos_excecoes_json/](exercicios/estruturas_basicas/arquivos_excecoes_json/) |

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
- Os scripts do tópico 7 leem e gravam arquivos no caminho relativo à pasta atual. Execute-os **de dentro** da pasta `exercicios/estruturas_basicas/arquivos_excecoes_json/`; por exemplo, `aprendizado.txt` está nela.

## Estrutura

```text
.
├── documentos/
│   ├── instalacao/                 # Guia de instalação
│   └── estruturas_basicas/         # Teoria + exercícios resolvidos (.md)
└── exercicios/
    └── estruturas_basicas/         # Um script .py por exercício
```

## Licença

Distribuído sob a licença descrita em [LICENSE](LICENSE).
