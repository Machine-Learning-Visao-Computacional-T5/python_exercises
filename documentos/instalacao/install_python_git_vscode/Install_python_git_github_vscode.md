# Guia: Python, VS Code, Git e GitHub

Vamos criar um programa que lê uma tabela de notas e colocar o projeto no GitHub. O guia serve para **Windows** e **Mac**. Digite cada comando separadamente e pressione **Enter**.

| Ferramenta | O que faz |
| --- | --- |
| **Python** | Executa nosso programa. |
| **VS Code** | Abre a pasta e permite escrever os arquivos. |
| **Git** | Registra versões do projeto no computador. |
| **GitHub** | Guarda o repositório na internet. |

> **Terminal** é a janela para digitar comandos.

---

## Parte 1 — Preparar o computador

### 1. Verificar se já existe Python

No Windows, abra o menu Iniciar, procure **PowerShell** e abra-o. No Mac, procure o aplicativo **Terminal**. Digite somente o comando correspondente ao seu sistema:

**Windows**

```powershell
py --version
```

**Mac**

```bash
python3 --version
```

- Se aparecer `Python 3.x.x`, você já tem Python: vá para o **passo 3**. O número exato da versão pode variar.
- Se aparecer "comando não encontrado" ou "não é reconhecido", siga o **passo 2**.

### 2. Instalar Python (somente se necessário)

1. Acesse [python.org/downloads](https://www.python.org/downloads/).
2. Baixe a versão indicada para seu sistema, Windows ou macOS.
3. Abra o arquivo baixado e siga as instruções. No Windows, se aparecer **Add Python to PATH**, marque essa opção.
4. Feche e abra o PowerShell ou Terminal novamente. Repita o comando do passo 1. Só avance quando aparecer a versão do Python.

### 3. Instalar VS Code (se necessário)

> Caso você já tenha o VS Code, não precisa instalar: siga adiante.

Acesse [code.visualstudio.com/download](https://code.visualstudio.com/download).

- **Windows:** abra o instalador e siga as etapas.
- **Mac:** abra o arquivo `.dmg` e arraste **Visual Studio Code** para **Aplicativos**.

Depois, abra o programa.

### 4. Instalar a extensão Python

No VS Code, clique em **Extensions/Extensões** (ícone de blocos na barra lateral), procure **Python**, selecione a extensão publicada pela **Microsoft** e clique em **Install/Instalar**.

> A extensão ajuda o editor; ela **não** substitui o Python instalado no computador.

### 5. Verificar Git e a conta no GitHub

Abra um terminal e digite:

```bash
git --version
```

Se aparecer um número de versão, o Git está disponível. Se não, instale pelo [site oficial do Git](https://git-scm.com/downloads), reabra o terminal e teste novamente. No Mac, uma janela do sistema também pode oferecer a instalação das ferramentas necessárias; siga as instruções dela.

Crie uma conta em [github.com](https://github.com) se ainda não tiver uma.

> **Git e GitHub são coisas diferentes:** instalar o Git não cria a conta.

---

## Parte 2 — Escolha um caminho

Temos duas possibilidades. Na aula de hoje trabalharemos com o **Caminho A**. O Caminho B será mencionado e poderá ser testado posteriormente.

| Caminho | Descrição |
| --- | --- |
| **A** | Criar no GitHub e depois copiar o projeto para o computador. |
| **B** | Começar com uma pasta no computador e depois publicá-la no GitHub. |

Usaremos o nome `meu_primeiro_projeto`. Nos comandos, troque `SEU_USUARIO` pelo nome da sua conta no GitHub.

---

## Caminho A — Criar primeiro no GitHub

### A1. Criar o repositório

1. Acesse [github.com/new](https://github.com/new).
2. Em **Repository name**, escreva `meu_primeiro_projeto` (ou um nome da sua preferência; nesse caso, substitua-o onde for necessário).
3. Escolha **Public** ou **Private**.
4. Marque **Add a README file**.
5. Clique em **Create repository**.

Agora o GitHub já tem um README e um primeiro commit.

### A2. Copiar para o computador

Na página do repositório, clique em **Code → HTTPS** e copie a URL. Abra o PowerShell (Windows) ou Terminal (Mac) e vá para Documentos:

> A sugestão é usar a pasta Documentos. Se preferir outra, pode usar, desde que saiba onde estão sua pasta e seu projeto.

**Windows (PowerShell)**

```powershell
cd "$HOME\Documents"
```

**Mac**

```bash
cd ~/Documents
```

Se sua pasta Documentos estiver em outro local, navegue até a pasta onde deseja guardar o projeto. Depois execute, com sua URL real:

```bash
git clone https://github.com/SEU_USUARIO/meu_primeiro_projeto.git
cd meu_primeiro_projeto
git status
```

`git clone` cria a pasta `meu_primeiro_projeto` no computador e traz o histórico.

> **Atenção:** não crie manualmente uma pasta de mesmo nome antes. Não use `git init` nesse caminho, pois o clone já configurou o Git e a conexão com o GitHub.

### A3. Criar e testar os arquivos

No VS Code, use **File → Open Folder...** para abrir a pasta criada pelo clone. O `README.md` já existe; abra-o e escreva:

```markdown
# Meu primeiro projeto

Este projeto lê um arquivo CSV e mostra o nome e a nota de cada aluno.
```

Crie o arquivo `dados.csv`:

```csv
nome,nota
Ana,8
Bruno,7
Carla,9
```

Crie o arquivo `analisar.py`:

```python
import csv

with open("dados.csv", encoding="utf-8") as arquivo:
    dados = csv.DictReader(arquivo)
    for aluno in dados:
        print(aluno["nome"], aluno["nota"])
```

Salve tudo. Abra **Terminal → New Terminal** no VS Code e execute:

**Windows**

```powershell
py analisar.py
```

**Mac**

```bash
python3 analisar.py
```

Você deve ver:

```text
Ana 8
Bruno 7
Carla 9
```

### A4. Registrar e enviar as mudanças

No terminal do projeto, execute um comando por vez:

```bash
git status
git add .
git status
git commit -m "Adiciona dados e script de analise"
git push
```

- O primeiro `git status` mostra o que mudou; o segundo mostra o que foi selecionado.
- O `commit` registra a versão no computador; o `push` a envia ao GitHub.

Se o Git pedir nome e e-mail, configure-os e repita o commit:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"
```

Substitua os exemplos pelo nome e e-mail que deseja associar aos commits.

Atualize a página do GitHub. Os três arquivos devem estar lá.

> Terminou o Caminho A. **Não** faça o Caminho B com essa mesma pasta.

---

## Resumo para lembrar

| Ação | Resultado |
| --- | --- |
| Salvar com `Ctrl+S` ou `⌘S` | Grava o arquivo no computador. |
| `git add .` | Seleciona mudanças para o próximo commit. |
| `git commit -m "mensagem"` | Registra uma versão no Git local. |
| `git push` | Envia commits ao GitHub. |
| `git pull` | Traz para o computador mudanças feitas no GitHub. |
| `git status` | Mostra o estado atual do projeto. |

> ⚠️ **Nunca** coloque senhas, chaves de API ou dados pessoais no repositório. Um repositório público pode ser visto por outras pessoas.

---

## Caminho B — Criar primeiro no computador

### B1. Criar e abrir a pasta

1. No Explorador de Arquivos (Windows) ou Finder (Mac), abra Documentos e crie a pasta `meu_primeiro_projeto`. Lembre-se de onde a salvou.
2. No VS Code, use **File → Open Folder...** (Arquivo → Abrir Pasta...) e selecione a pasta inteira.
3. Na barra lateral, passe o mouse pelo nome da pasta e clique em **New File/Novo Arquivo**. Crie estes três arquivos, um de cada vez:

| Arquivo | Para que serve |
| --- | --- |
| `README.md` | Explica o projeto. |
| `dados.csv` | Guarda a tabela de notas. |
| `analisar.py` | Contém o programa Python. |

Em `README.md`, escreva:

```markdown
# Meu primeiro projeto

Este projeto lê um arquivo CSV e mostra o nome e a nota de cada aluno.
```

Em `dados.csv`, escreva:

```csv
nome,nota
Ana,8
Bruno,7
Carla,9
```

A primeira linha traz os nomes das colunas. As outras são os dados.

Em `analisar.py`, escreva (com os espaços no início das linhas):

```python
import csv

with open("dados.csv", encoding="utf-8") as arquivo:
    dados = csv.DictReader(arquivo)
    for aluno in dados:
        print(aluno["nome"], aluno["nota"])
```

O programa abre o CSV, passa por cada aluno e mostra o nome e a nota. Salve os arquivos com `Ctrl+S` (Windows) ou `⌘S` (Mac).

### B2. Testar o programa

No VS Code, clique em **Terminal → New Terminal**. O terminal deve estar dentro de `meu_primeiro_projeto`. Digite `pwd`: o caminho mostrado deve terminar com o nome dessa pasta. Se estiver em outra pasta, abra a pasta certa no VS Code e crie um terminal novo.

Execute:

**Windows**

```powershell
py analisar.py
```

**Mac**

```bash
python3 analisar.py
```

Resultado esperado:

```text
Ana 8
Bruno 7
Carla 9
```

> Se aparecer `FileNotFoundError`, confira se o terminal está na pasta correta e se o arquivo realmente se chama `dados.csv`.

### B3. Iniciar o Git e registrar a primeira versão

No terminal da pasta do projeto, execute um comando por vez:

```bash
git init
git branch -M main
git status
git add .
git status
git commit -m "Cria projeto de analise de notas"
```

- `git init` inicia o histórico no computador.
- `main` é o nome da branch principal.
- `git status` mostra o estado dos arquivos; antes do `git add`, eles aparecem como *untracked*.
- O ponto em `git add .` seleciona os arquivos da pasta.
- `git commit` registra uma versão, mas ainda **não** envia nada à internet.

Se o Git pedir nome e e-mail, configure-os e repita o commit:

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@example.com"
```

Substitua os exemplos pelo nome e e-mail que deseja associar aos commits.

### B4. Criar o repositório no GitHub

1. Acesse [github.com/new](https://github.com/new).
2. Em **Repository name**, escreva `meu_primeiro_projeto`.
3. Escolha **Public** ou **Private**, conforme a orientação da aula.
4. **Não** marque as opções para adicionar README, `.gitignore` ou licença: o projeto já tem arquivos e commit no computador.
5. Clique em **Create repository** e copie a URL HTTPS mostrada na página.

Ela terá a forma `https://github.com/SEU_USUARIO/meu_primeiro_projeto.git`. Copie a URL pura, sem colchetes ou parênteses de Markdown.

### B5. Conectar e enviar

Volte ao terminal do projeto. No primeiro comando, substitua `SEU_USUARIO` pelo seu usuário real:

```bash
git remote add origin https://github.com/SEU_USUARIO/meu_primeiro_projeto.git
git remote -v
git push -u origin main
```

- `origin` é um apelido para o endereço no GitHub.
- `git remote -v` permite conferir o endereço.
- `git push` envia o commit. Se aparecer uma janela para entrar na conta do GitHub, siga as instruções.

Atualize a página do repositório: os três arquivos devem aparecer.

> Terminou o Caminho B. **Não** faça o Caminho A com essa mesma pasta.
