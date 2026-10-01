# Guia 2: Exercícios de Python, .env e .gitignore

*30 de set. de 2026 · @hellen*

## Sumário

- [Como usar este guia](#como-usar-este-guia)
- [O ciclo de cada exercício](#o-ciclo-de-cada-exercício)
- [Os quatro tipos de exercício](#os-quatro-tipos-de-exercício)
- [Passo a passo completo: o Exercício 1 do início ao fim](#passo-a-passo-completo-o-exercício-1-do-início-ao-fim)
- [Checklist do aluno](#checklist-do-aluno)
- [Parte 1 — Exercícios de Python](#parte-1--exercícios-de-python)
- [Parte 2 — Criar um arquivo `.env`](#parte-2--criar-um-arquivo-env)
- [Parte 3 — `.gitignore`](#parte-3--gitignore)
- [Resumo e problemas comuns](#resumo-e-problemas-comuns)
- [Respostas de todos os exercícios](#respostas-de-todos-os-exercícios)

## Como usar este guia

Cada exercício é uma volta completa no ciclo do Git: **branch, código, teste, commit, push, Pull Request e pull**. Git se aprende pela repetição, então o ciclo é o mesmo em todos os exercícios.

Este guia continua o Guia 1 (Caminho A). Use a mesma pasta `meu_primeiro_projeto`, já clonada e aberta no VS Code. O gabarito está na aba **Gabarito (professor)**.

| Parte | O que você vai praticar |
| --- | --- |
| **1. Exercícios de Python** | Resolver, testar, debugar e escrever programas. |
| **2. Arquivo `.env`** | Guardar configurações e senhas fora do código. |
| **3. `.gitignore`** | Impedir que o `.env` e outros arquivos que não devem ir para o GitHub sejam enviados. |

## O ciclo de cada exercício

No terminal do VS Code, dentro da pasta do projeto, siga sempre esta ordem. Troque `exNN-nome` pelo nome indicado no exercício.

1. Atualize a main: `git switch main` e depois `git pull`.
2. Crie a branch do exercício: `git switch -c feat/exNN-nome`.
3. Crie o arquivo dentro da pasta `exercicios`, escreva o código e salve (`Ctrl+S` ou `⌘S`).
4. Rode o programa: `py arquivo.py` (Windows) ou `python3 arquivo.py` (Mac), com o terminal dentro de `exercicios` (`cd exercicios`). Corrija até funcionar.
5. Registre: `git status`, `git add .` e `git commit -m "mensagem"`.
6. Envie a branch: `git push -u origin feat/exNN-nome`.
7. No GitHub, abra o Pull Request, faça o merge e clique em **Delete branch** (passos C6 a C8 do Guia 1).
8. Volte e limpe: `git switch main`, `git pull` e `git branch -d feat/exNN-nome`.

> **Dica:** se ficar perdido, rode `git status`. Ele sempre diz em qual branch você está e o que mudou.

## Os quatro tipos de exercício

| Tipo | O que você faz |
| --- | --- |
| **Resolver** | Escreve um programa do zero a partir de um enunciado. |
| **Testar** | Ideal: escreve testes com `assert` que conferem se uma função funciona. Por ora, faremos testes manuais. |
| **Debugar** | Recebe um código com erros, encontra e corrige cada um. |
| **Escrever** | Escreve funções e programas com mais partes, juntando o que já aprendeu. |

## Passo a passo completo: o Exercício 1 do início ao fim

Aqui fazemos juntos o Exercício 1, clique por clique: criar a pasta, criar o arquivo, escrever, salvar, rodar, testar, debugar e enviar ao GitHub. Os outros exercícios seguem exatamente os mesmos passos.

### P1. Abrir o projeto no VS Code

1. Abra o VS Code.
2. Clique em **File → Open Folder...** (Arquivo → Abrir Pasta...).
3. Vá até Documentos e selecione a pasta `meu_primeiro_projeto`, criada no Guia 1. Clique em **Abrir** (Windows) ou **Open** (Mac).
4. Se aparecer a pergunta *Do you trust the authors...?*, clique em **Yes, I trust the authors**.
5. Clique no ícone de duas folhas no topo da barra lateral esquerda: é o **Explorer**. O nome da pasta, em maiúsculas, aparece no topo: `MEU_PRIMEIRO_PROJETO`.

> Abra sempre a **pasta**, e não um arquivo solto. Assim o VS Code e o terminal sabem onde o projeto está.

### P2. Abrir o terminal

1. No menu, clique em **Terminal → New Terminal**. Um painel abre na parte de baixo da janela.
2. Digite `pwd` e pressione **Enter**. O caminho mostrado deve terminar em `meu_primeiro_projeto`.
3. Digite `git status`. Deve aparecer `On branch main`.

> Se o caminho estiver errado, feche o terminal (ícone de lixeira no painel), confira o passo P1 e abra um terminal novo.

### P3. Atualizar a main e criar a branch

Digite um comando por vez, pressionando **Enter** depois de cada um:

```bash
git switch main
git pull
git switch -c feat/ex01-media
```

Confira no canto inferior esquerdo da janela: agora aparece `feat/ex01-media` no lugar de `main`.

### P4. Criar a pasta `exercicios`

Todos os exercícios da Parte 1 ficam numa pasta só, para o projeto não virar bagunça.

**Pelo VS Code**

1. No Explorer, passe o mouse sobre `MEU_PRIMEIRO_PROJETO`. Aparecem quatro ícones pequenos à direita.
2. Clique no segundo ícone, **New Folder** (uma pasta com um +).
3. Digite `exercicios` e pressione **Enter**.

**Ou pelo terminal** (funciona no Windows e no Mac):

```bash
mkdir exercicios
```

**Regra para nomes de pastas e arquivos**

| Regra | Certo | Errado |
| --- | --- | --- |
| Sem espaços: use `_` ou `-` | `ex01_media.py` | `ex01 media.py` |
| Sem acentos nem cedilha | `exercicios` | `exercícios` |
| Tudo em minúsculas | `dados.csv` | `Dados.CSV` |

> Se a pasta foi criada dentro de outra por engano, arraste-a no Explorer até o nome `MEU_PRIMEIRO_PROJETO`.

### P5. Criar o arquivo

1. No Explorer, clique uma vez na pasta `exercicios` para selecioná-la.
2. Passe o mouse sobre `MEU_PRIMEIRO_PROJETO` e clique no primeiro ícone, **New File** (uma folha com um +).
3. Digite `ex01_media.py` e pressione **Enter**.
4. Confira: o arquivo aparece dentro de `exercicios` (um pouco mais à direita) e tem o ícone do Python. O arquivo abre vazio no editor.

> **A extensão importa.** O `.py` diz ao VS Code e ao computador que o arquivo é Python. Um arquivo `ex01_media` ou `ex01_media.txt` não roda.

### P6. Escrever o código

Digite o código abaixo. Evite só copiar e colar: digitar ensina onde ficam os dois-pontos e os espaços.

**Objetivo:** dadas 3 notas, calcular a média. Se maior ou igual a 7, então *aprovado*; se maior ou igual a 5 e menor que 7, então *recuperação*; do contrário, *reprovado*. Imprima a média e a situação (aprovado/reprovado/recuperação).

```python
# Exercício 1: média do aluno

# 1. As notas
nota1 = 8
nota2 = 6.5
nota3 = 7

# 2. O cálculo
media = (nota1 + nota2 + nota3) / 3

# 3. A decisão
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# 4. O resultado
print("Média:", round(media, 1))
print("Situação:", situacao)
```

| Parte | O que observar |
| --- | --- |
| `#` | Comentário: o Python ignora a linha. Serve para explicar o código. |
| `nota2 = 6.5` | Números decimais usam ponto, não vírgula. |
| `(nota1 + nota2 + nota3) / 3` | Os parênteses fazem a soma acontecer antes da divisão. |
| `if`, `elif`, `else` | Terminam com dois-pontos (`:`). |
| Linhas abaixo do `if` | Começam com 4 espaços. Pressione `Tab` uma vez: o VS Code coloca os 4 espaços. |
| `"Aprovado"` | Texto fica entre aspas. |

### P7. Salvar

1. Olhe a aba do arquivo, no topo do editor: uma **bolinha branca** ao lado do nome quer dizer *não salvo*.
2. Pressione `Ctrl+S` (Windows) ou `⌘S` (Mac). A bolinha vira um **X**: o arquivo está salvo.

> **Dica:** ative **File → Auto Save** para o VS Code salvar sozinho. O erro mais comum da aula é rodar o programa sem ter salvo: o Python roda a versão antiga.

### P8. Rodar o programa

O terminal ainda está na pasta do projeto. Entre na pasta `exercicios`:

```bash
cd exercicios
```

Agora rode:

**Windows**

```powershell
py ex01_media.py
```

**Mac**

```bash
python3 ex01_media.py
```

Resultado esperado:

```text
Média: 7.2
Situação: Aprovado
```

> **Atalhos úteis no terminal:** a seta para cima repete o último comando. Digite `py ex0` e pressione `Tab`: o terminal completa o nome do arquivo.
>
> **Outra forma de rodar:** o botão ▶ no canto superior direito do editor. Ele sempre usa o arquivo aberto.

| Mensagem | O que fazer |
| --- | --- |
| `can't open file ... No such file or directory` | O terminal está na pasta errada. Rode `pwd`: deve terminar em `exercicios`. Se não, `cd exercicios`. |
| `cd: no such file or directory` | Você já está dentro de `exercicios`, ou a pasta tem outro nome. Rode `pwd` e confira no Explorer. |

### P9. Testar manualmente

Um programa que funciona com um conjunto de notas pode falhar com outro. **Testar** é rodar com vários valores e comparar com o que deveria sair.

Para cada linha da tabela: troque as três notas no código, salve, rode e marque se o resultado bateu.

| Teste | nota1, nota2, nota3 | Média esperada | Situação esperada | Deu certo? |
| --- | --- | --- | --- | --- |
| 1 | 8, 6.5, 7 | 7.2 | Aprovado | |
| 2 | 10, 10, 10 | 10.0 | Aprovado | |
| 3 | 7, 7, 7 | 7.0 | Aprovado | |
| 4 | 5, 5, 5 | 5.0 | Recuperação | |
| 5 | 3, 4, 2 | 3.0 | Reprovado | |

> **Por que o teste 3?** A nota 7 é a **fronteira** onde a regra muda. Se alguém escrever `media > 7` em vez de `media >= 7`, só esse teste mostra o erro. Experimente: troque, salve, rode o teste 3 e veja o resultado errado. Depois desfaça.

No final, volte às notas originais (8, 6.5, 7).

### P10. Debugar

**Debugar** é encontrar e corrigir erros. Há três ferramentas, da mais simples à mais poderosa.

**Ferramenta 1: ler a mensagem de erro.** Vamos provocar um erro de propósito.

1. Apague os dois-pontos do final da linha `if media >= 7:` e salve.
2. Repare: o VS Code sublinha a linha com uma ondinha vermelha. Passe o mouse sobre ela para ler o aviso.
3. Rode o programa. Aparece algo assim:

   ```text
     File ".../exercicios/ex01_media.py", line 12
       if media >= 7
                    ^
   SyntaxError: expected ':'
   ```

4. Leia **de baixo para cima**: a última linha diz o que houve (`expected ':'`, faltam dois-pontos) e `line 12` diz onde. O `^` aponta o lugar exato.
5. Devolva os dois-pontos, salve e rode de novo.

**Ferramenta 2: `print` para espiar.** Quando o programa roda mas o resultado parece estranho, mostre os valores do meio do caminho. Logo abaixo da linha `media = ...`, acrescente:

```python
print("DEBUG soma:", nota1 + nota2 + nota3)
print("DEBUG media sem arredondar:", media)
```

Rode: aparecem `21.5` e `7.166666666666667`. Agora você vê que a média real é 7,1666... e que o `round` só muda como ela aparece.

> Apague as linhas de `DEBUG` e salve antes de seguir: senão os números de linha do próximo passo mudam.

**Ferramenta 3: o depurador do VS Code.** Ele pausa o programa e mostra todas as variáveis.

1. Clique à esquerda do número 12 (a linha do `if`). Aparece uma bolinha vermelha: é o **breakpoint**, onde o programa vai parar.
2. Pressione `F5` (no Mac, pode ser `fn+F5`). Se o VS Code perguntar, escolha **Python Debugger** e depois **Python File**.
3. A linha 12 fica amarela: o programa parou ali, antes de executá-la.
4. Na barra lateral, o painel **Variables → Locals** mostra `nota1`, `nota2`, `nota3` e `media` com seus valores.
5. Pressione `F10` para executar uma linha. Veja qual caminho o programa segue (`if`, `elif` ou `else`) e quando `situacao` aparece no painel.
6. Continue com `F10` até o fim, ou pressione `Shift+F5` para parar.
7. Clique na bolinha vermelha para removê-la.

| Tecla | O que faz |
| --- | --- |
| `F5` | Começa a depurar (ou continua até o próximo breakpoint). |
| `F10` | Executa a linha atual e para na próxima. |
| `Shift+F5` | Para o depurador. |

### P11. Registrar a versão (commit)

No terminal (pode continuar dentro de `exercicios`):

```bash
git status
```

O arquivo aparece em **vermelho** como *Untracked files*: `exercicios/` ou `ex01_media.py`. O Git viu o arquivo, mas ainda não o registra.

```bash
git add .
git status
```

Agora ele aparece em **verde** em *Changes to be committed*: está selecionado.

```bash
git commit -m "Resolve exercicio 1: media"
```

> O Git não guarda pastas vazias. A pasta `exercicios` só aparece no `git status` depois de ter pelo menos um arquivo dentro.

### P12. Enviar e juntar na main

```bash
git push -u origin feat/ex01-media
```

1. Abra o repositório no GitHub e clique em **Compare & pull request**.
2. Confira: base `main` ← compare `feat/ex01-media`. Clique em **Create pull request**.
3. Clique em **Merge pull request**, **Confirm merge** e **Delete branch**.
4. De volta ao terminal:

```bash
git switch main
git pull
git branch -d feat/ex01-media
```

No GitHub, a pasta `exercicios` com o `ex01_media.py` deve aparecer na página do repositório.

## Checklist do aluno

- [ ] Abri a pasta do projeto no VS Code e o terminal mostra o caminho certo.
- [ ] Criei a branch antes de mexer nos arquivos.
- [ ] Criei a pasta `exercicios` e o arquivo `ex01_media.py` dentro dela.
- [ ] Salvei (sem bolinha branca na aba) antes de rodar.
- [ ] Rodei os 5 testes da tabela e todos bateram.
- [ ] Provoquei um erro, li a mensagem e corrigi.
- [ ] Usei o breakpoint e vi as variáveis no depurador.
- [ ] Fiz commit, push, Pull Request, merge e `git pull` na main.

Daqui em diante, faça cada exercício seguindo o **ciclo do início do guia**, sempre com os arquivos dentro de `exercicios`.

## Parte 1 — Exercícios de Python

São 8 exercícios, do mais simples ao que junta tudo. Faça na ordem: cada um usa algo do anterior. Em todos, siga o ciclo da seção anterior.

| Nº | Tipo | Arquivo | Branch |
| --- | --- | --- | --- |
| 1 | Resolver | `ex01_media.py` | `feat/ex01-media` |
| 2 | Resolver | `ex02_tabuada.py` | `feat/ex02-tabuada` |
| 3 | Testar | `ex03_testes.py` | `feat/ex03-testes` |
| 4 | Debugar | `ex04_debug_soma.py` | `feat/ex04-debug-soma` |
| 5 | Debugar | `ex05_debug_media.py` | `feat/ex05-debug-media` |
| 6 | Escrever | `ex06_situacao.py` | `feat/ex06-situacao` |
| 7 | Escrever | `ex07_turma.py` e `dados.csv` | `feat/ex07-turma` |
| 8 | Git | `README.md` (no GitHub) | nenhuma |

### Exercício 1 — Média do aluno (Resolver)

Crie variáveis com três notas: `nota1 = 8`, `nota2 = 6.5` e `nota3 = 7`. O programa deve calcular a média e mostrar a situação:

- média 7 ou mais: **Aprovado**;
- média 5 ou mais (e menor que 7): **Recuperação**;
- média menor que 5: **Reprovado**.

Resultado esperado:

```text
Média: 7.2
Situação: Aprovado
```

**Teste também:** troque as notas para 5, 5, 5 (deve dar *Recuperação*) e para 3, 4, 2 (deve dar *Reprovado*). Um programa só está certo quando funciona em **todos** os casos.

> **Dica:** para mostrar uma casa decimal, use `round(media, 1)`. Para três condições, use `if`, `elif` e `else`.

Commit sugerido: `git commit -m "Resolve exercicio 1: media"`.

### Exercício 2 — Tabuada (Resolver)

O programa pede um número com `input` e mostra a tabuada de 1 a 10. Resultado esperado, digitando 7:

```text
Digite um número: 7
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

> **Dica:** `input` sempre devolve texto. Converta com `int(...)` antes de fazer contas. Para repetir de 1 a 10, use `for i in range(1, 11):`.


### Exercício 3 — Três erros na soma (Debugar)

Este programa deveria somar os números da lista e mostrar `A soma é: 108`. Ele tem **três erros**. Copie exatamente como está:

```python
numeros = [4, 8, 15, 16, 23, 42]

total = 0
for i in range(1, len(numeros))
    total = total + numeros[i]

print("A soma é: " + total)
```

**Como ler uma mensagem de erro:** comece pela **última linha**. Ela diz o tipo do erro (`SyntaxError`, `TypeError`, `NameError`...). Logo acima, `line 4` diz em que linha o Python parou.

1. Rode o programa, leia o erro e corrija **só esse** erro.
2. Faça um commit para essa correção: `git add .` e `git commit -m "Corrige erro de sintaxe"`.
3. Repita até o programa rodar. Atenção: rodar sem erro não quer dizer que está certo. Compare o resultado com 108.
4. No final, rode `git log --oneline`. Você verá um commit para cada correção.

> Um commit por correção é um bom hábito: se algo der errado, dá para ver exatamente o que mudou em cada passo.

### Exercício 4 — O depurador do VS Code (Debugar)

Este programa deveria mostrar `Média da Ana: 8.0`. Ele tem **dois erros**, e um deles não gera mensagem nenhuma:

```python
def media(notas):
    soma = 0
    for nota in notas:
        soma = nota
    return soma / len(notas)


notas_ana = [8, 7, 9]
resultado = media(notas_ana)
print("Média da Ana:", resultdo)
```

O primeiro erro aparece ao rodar. Corrija-o. O segundo exige o **depurador**, que executa o programa linha por linha e mostra o valor de cada variável:

1. Clique à esquerda do número da linha `soma = nota`. Aparece uma bolinha vermelha: é um **breakpoint**, onde o programa vai pausar.
2. Pressione `F5` (no Mac, pode ser `fn+F5`). Se o VS Code perguntar, escolha **Python Debugger** e depois **Python File**.
3. O programa pausa na linha marcada. Na barra lateral, o painel **Variables** mostra `soma`, `nota` e `notas`.
4. Pressione `F10` para avançar uma linha. Observe o valor de `soma` a cada volta do `for`.
5. **Pergunta:** `soma` está acumulando as notas? Descubra o erro, pare o depurador (`Shift+F5`), corrija e rode de novo.

### Exercício 5 — Função `situacao` (Escrever)

Escreva a função `situacao(nota)`. Ela **devolve** (com `return`, sem `print`) o texto `Aprovado`, `Recuperação` ou `Reprovado`, com as mesmas regras do Exercício 1.

Depois, escreva testes com `assert` para estas notas: 10, 7, 6.9, 5, 4.9 e 0.

> **Por que 7 e 6.9?** Os erros costumam aparecer nas **fronteiras**, onde a regra muda. Trocar `>=` por `>` é o erro mais comum: só um teste com a nota 7 exata o encontra.

### Exercício 7 — Relatório da turma (Escrever)

Crie `dados.csv` com este conteúdo:

```csv
nome,nota
Ana,8
Bruno,7
Carla,9
Diego,4.5
Elisa,6
```

Em `ex07_turma.py`, copie a função `situacao` do Exercício 6 e escreva um programa que leia o CSV com o módulo `csv` e mostre:

```text
Ana 8.0 Aprovado
Bruno 7.0 Aprovado
Carla 9.0 Aprovado
Diego 4.5 Reprovado
Elisa 6.0 Recuperação
Média da turma: 6.9
Maior nota: Carla (9.0)
```

> **Dica:** o CSV também devolve texto. Use `float(aluno["nota"])` para converter a nota. Guarde as notas numa lista para calcular a média no final.

Para ler o CSV, use este esqueleto e complete o que está dentro do `for`:

```python
import csv

with open("dados.csv", encoding="utf-8") as arquivo:
    dados = csv.DictReader(arquivo)
    for aluno in dados:
        print(aluno["nome"], aluno["nota"])
```

### Exercício 7 — Mudança feita no GitHub (Git)

Até agora, as mudanças iam do computador para o GitHub. Agora é o contrário.

1. No GitHub, abra o `README.md` do projeto e clique no lápis (**Edit this file**).
2. Acrescente uma lista com os exercícios que você já fez.
3. Clique em **Commit changes...** e confirme na `main`.
4. No computador, abra o `README.md` no VS Code: ele ainda está antigo.
5. No terminal: `git switch main` e `git pull`. Abra o arquivo de novo: agora a mudança chegou.

> **Resumo:** `push` leva do computador para o GitHub; `pull` traz do GitHub para o computador.

## Parte 2 — Criar um arquivo `.env`

O `.env` guarda **configurações e segredos** (senhas, chaves de API) fora do código, num arquivo que nunca vai para o GitHub. É a resposta ao aviso do Guia 1: nada de senhas no repositório.

> **Importante:** faça a Parte 2 e a Parte 3 **na mesma branch** e só faça o commit no final da Parte 3. Se o `.env` entrar num commit antes do `.gitignore` existir, ele vai para o GitHub.

### E1. Criar a branch

O `.env` fica na **raiz do projeto**, e não em `exercicios`. Se o terminal estiver dentro de `exercicios`, volte uma pasta com `cd ..` e confira com `pwd`. Depois:

```bash
git switch main
git pull
git switch -c feat/env-gitignore
```

### E2. Criar o arquivo `.env`

No VS Code, crie um arquivo novo na raiz do projeto (a mesma pasta de `exercicios`) com o nome exato `.env`: começa com ponto e não tem nada antes dele.

```text
# Configurações do projeto
NOME_ESCOLA=Colegio Exemplo
NOTA_MINIMA=7
API_KEY=chave-falsa-123456
```

| Regra | Exemplo |
| --- | --- |
| Uma variável por linha, no formato `NOME=valor`. | `NOTA_MINIMA=7` |
| Sem espaços ao redor do `=`. | `NOTA_MINIMA = 7` está **errado**. |
| Nomes em maiúsculas, com `_` no lugar de espaços. | `NOME_ESCOLA` |
| Linhas com `#` são comentários. | `# Configurações do projeto` |

> A chave acima é **falsa**, só para a aula. Uma chave real nunca deve aparecer em slides, prints ou mensagens.

> No Windows e no Mac, arquivos que começam com ponto podem ficar **ocultos** no Explorador de Arquivos ou no Finder. No VS Code eles aparecem normalmente.

### E3. Instalar a biblioteca `python-dotenv`

O Python não lê o `.env` sozinho. A biblioteca `python-dotenv` faz isso. No terminal:

**Windows**

```powershell
py -m pip install python-dotenv
```

**Mac**

```bash
python3 -m pip install python-dotenv
```

Se aparecer `Successfully installed` ou `Requirement already satisfied`, está pronto.

### E4. Ler o `.env` no Python

Crie `config.py`:

```python
import os

from dotenv import load_dotenv

load_dotenv()  # lê o arquivo .env e carrega as variáveis

escola = os.getenv("NOME_ESCOLA")
nota_minima = float(os.getenv("NOTA_MINIMA", "7"))
chave = os.getenv("API_KEY")

print("Escola:", escola)
print("Nota mínima:", nota_minima)
print("Chave carregada?", chave is not None)
```

Rode com `py config.py` (Windows) ou `python3 config.py` (Mac). Resultado esperado:

```text
Escola: Colegio Exemplo
Nota mínima: 7.0
Chave carregada? True
```

- `os.getenv("NOME")` devolve o valor da variável, ou `None` se ela não existir.
- O segundo valor em `os.getenv("NOTA_MINIMA", "7")` é o **padrão**, usado quando a variável não está no `.env`.
- Todo valor chega como **texto**: por isso o `float(...)`.
- O programa mostra só se a chave **existe**, nunca a chave em si.

**Teste:** mude `NOTA_MINIMA=7` para `NOTA_MINIMA=6` no `.env`, salve e rode de novo. O resultado muda sem mexer no código: essa é a vantagem.

### E5. Criar o `.env.example`

Como o `.env` não vai para o GitHub, quem clonar o projeto não saberá quais variáveis criar. Para isso existe o `.env.example`: a mesma lista de nomes, com valores falsos ou vazios. Esse arquivo **vai** para o GitHub.

Crie `.env.example`:

```text
# Copie este arquivo para .env e preencha os valores
NOME_ESCOLA=
NOTA_MINIMA=7
API_KEY=
```

| Arquivo | Tem valores reais? | Vai para o GitHub? |
| --- | --- | --- |
| `.env` | Sim | **Não** |
| `.env.example` | Não | Sim |

> Ainda **não** faça commit. Siga para a Parte 3.

## Parte 3 — `.gitignore`

O `.gitignore` é uma lista de arquivos que o Git deve fingir que não existem: eles não aparecem no `git status`, não entram no `git add .` e nunca chegam ao GitHub.

O `.env` e a pasta `__pycache__/` ficam no computador; todo o resto sobe com `git push`.

### G1. De onde vem um `.gitignore`

O próprio GitHub mantém modelos prontos de `.gitignore` para cada linguagem, no repositório [github/gitignore](https://github.com/github/gitignore). O de Python é o `Python.gitignore`. Há três jeitos de usar:

| Situação | Como fazer |
| --- | --- |
| Repositório **novo** no GitHub | Em [github.com/new](https://github.com/new), em **Add .gitignore**, escolha **Python**. |
| Repositório que **já existe** (o nosso caso) | Crie o arquivo `.gitignore` no VS Code (passo G2). |
| Quer o modelo **completo** | Abra o `Python.gitignore`, clique em **Raw**, copie tudo e cole no seu `.gitignore`. |

> O modelo completo tem mais de 100 linhas, para ferramentas que ainda não usamos. Para a aula, a versão curta do passo G2 basta.

### G2. Criar o `.gitignore`

Na raiz do projeto, na branch `feat/env-gitignore`, crie o arquivo `.gitignore` (com ponto no início):

```text
# Segredos: nunca vão para o GitHub
.env

# Ambiente virtual do Python
.venv/
venv/

# Arquivos gerados pelo Python
__pycache__/
*.pyc

# Arquivos do sistema
.DS_Store
Thumbs.db
```

| Linha | O que ignora |
| --- | --- |
| `.env` | Exatamente o arquivo `.env`. O `.env.example` **não** é ignorado. |
| `__pycache__/` | A pasta inteira (a `/` no final indica pasta). |
| `*.pyc` | Qualquer arquivo terminado em `.pyc` (o `*` vale "qualquer nome"). |
| `.DS_Store` e `Thumbs.db` | Arquivos que o Mac e o Windows criam sozinhos. |

> **Cuidado:** não escreva `.env*`. Isso também ignoraria o `.env.example`, que precisa ir para o GitHub.

### G3. Conferir antes do commit

Rode:

```bash
git status
```

Devem aparecer como novos: `.gitignore`, `.env.example` e `config.py`. O `.env` **não pode** aparecer. Se aparecer, confira o nome do `.gitignore` (com ponto, sem `.txt` no final) e se ele está na raiz do projeto.

Para confirmar que o `.env` está ignorado:

```bash
git check-ignore -v .env
```

A resposta `.gitignore:2:.env .env` quer dizer: "ignorado pela linha 2 do `.gitignore`".

### G4. Commit, push e Pull Request

```bash
git add .
git status
git commit -m "Adiciona .env.example, .gitignore e config.py"
git push -u origin feat/env-gitignore
```

Abra o Pull Request, faça o merge e volte para a main com `git switch main` e `git pull`, como nos exercícios.

> **Prova final:** abra o repositório no GitHub. Devem estar lá `.gitignore`, `.env.example` e `config.py`. O `.env` **não** pode estar.

### G5. E se o `.env` já foi para o GitHub?

O `.gitignore` só vale para arquivos que o Git **ainda não acompanha**. Se o `.env` entrou num commit antes, faça:

```bash
git rm --cached .env
git commit -m "Remove .env do repositorio"
git push
```

`git rm --cached` tira o arquivo do Git, mas mantém o arquivo no seu computador.

> ⚠️ **Isso não apaga o passado.** O `.env` continua visível nos commits antigos do GitHub. Se havia uma senha ou chave real, **troque-a** (gere uma chave nova e desative a antiga). Considere a antiga como vazada.

## Resumo e problemas comuns

| Comando ou arquivo | Para que serve |
| --- | --- |
| `assert condição` | Para o programa com `AssertionError` se a condição for falsa. |
| Breakpoint + `F5` + `F10` | Pausa o programa e avança linha por linha, mostrando as variáveis. |
| `git log --oneline` | Lista os commits, um por linha. |
| `.env` | Guarda valores reais (senhas, chaves). Fica só no computador. |
| `.env.example` | Lista os nomes das variáveis, sem valores reais. Vai para o GitHub. |
| `load_dotenv()` e `os.getenv("NOME")` | Carregam o `.env` e leem uma variável no Python. |
| `.gitignore` | Lista o que o Git deve ignorar. |
| `git check-ignore -v arquivo` | Mostra qual linha do `.gitignore` ignora aquele arquivo. |
| `git rm --cached arquivo` | Tira do Git um arquivo que não devia estar lá, sem apagá-lo do computador. |

| Mensagem ou situação | O que fazer |
| --- | --- |
| `SyntaxError: expected ':'` | Faltam os dois-pontos no fim de `if`, `for`, `def` ou `else`. |
| `IndentationError` | Os espaços no início da linha estão errados. Use 4 espaços dentro de cada bloco. |
| `TypeError: can only concatenate str (not "int") to str` | Você juntou texto e número com `+`. Use vírgula no `print` ou converta com `str(...)`. |
| `NameError: name '...' is not defined` | Nome de variável escrito errado, ou usada antes de ser criada. |
| `ValueError: invalid literal for int()` | O `input` recebeu algo que não é número inteiro. |
| `ModuleNotFoundError: No module named 'dotenv'` | Falta instalar: repita o passo E3. Se continuar, confira se o VS Code usa o mesmo Python (canto inferior direito). |
| `error: externally-managed-environment` (Mac) | Seu Python não aceita `pip` direto. Crie um ambiente virtual: `python3 -m venv .venv` e `source .venv/bin/activate`, e repita o E3. |
| `os.getenv` devolve `None` | O `.env` não está na raiz do projeto, o nome da variável está diferente ou o arquivo não foi salvo. |
| O `.env` aparece no `git status` | O `.gitignore` não está na raiz, tem outro nome (como `.gitignore.txt`) ou o `.env` já tinha sido commitado (passo G5). |
| O `.env` aparece no GitHub | Passo G5, e troque qualquer senha ou chave real que estava nele. |

## Respostas de todos os exercícios

Todas as soluções foram executadas e produzem exatamente a saída mostrada. Outras soluções também estão certas se derem o mesmo resultado nos mesmos testes. **Tente resolver antes de olhar.**

### Resposta 1 — Média do aluno

```python
nota1 = 8
nota2 = 6.5
nota3 = 7

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("Média:", round(media, 1))
print("Situação:", situacao)
```

```text
Média: 7.2
Situação: Aprovado
```

Com 5, 5, 5: *Recuperação*. Com 3, 4, 2: *Reprovado*.

**Erros comuns:** esquecer os parênteses na soma (a divisão acontece primeiro) e usar três `if` em vez de `if`, `elif` e `else`.

### Resposta 2 — Tabuada

```python
numero = int(input("Digite um número: "))

for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)
```

**Erros comuns:** `range(1, 10)` para no 9. Sem `int(...)`, o número digitado é texto e `"7" * 3` vira `777`.

### Resposta 3 — Testes com `assert`

```python
def eh_par(numero):
    return numero % 2 == 0


def maior(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= c:
        return b
    return c


# Testes de eh_par
assert eh_par(4) == True
assert eh_par(7) == False
assert eh_par(0) == True
assert eh_par(-2) == True
assert eh_par(-3) == False

# Testes de maior: o maior em cada posição, números iguais e negativos
assert maior(9, 2, 5) == 9
assert maior(2, 9, 5) == 9
assert maior(2, 5, 9) == 9
assert maior(3, 3, 3) == 3
assert maior(-1, -5, -3) == -1

print("Todos os testes passaram!")
```

Ao trocar `% 2 == 0` por `% 2 == 1`, o primeiro teste falha com `AssertionError` na linha `assert eh_par(4) == True`.

### Resposta 4 — Três erros na soma

| Ordem | O que aparece | Erro | Correção |
| --- | --- | --- | --- |
| 1 | `SyntaxError: expected ':'` | Faltam os dois-pontos no `for`. | `for i in range(1, len(numeros)):` |
| 2 | `TypeError: can only concatenate str (not "int") to str` | Texto + número com `+`. | `print("A soma é:", total)` |
| 3 | Nenhuma mensagem, mas mostra `A soma é: 104` | O `range` começa em 1 e pula o primeiro número (4). | `range(0, len(numeros))` |

```python
numeros = [4, 8, 15, 16, 23, 42]

total = 0
for i in range(0, len(numeros)):
    total = total + numeros[i]

print("A soma é:", total)
```

```text
A soma é: 108
```

O erro 3 é o mais importante: o programa roda sem reclamar, mas o resultado está **errado**. Só quem compara com o resultado esperado percebe.

### Resposta 5 — O depurador

| Ordem | O que aparece | Erro | Correção |
| --- | --- | --- | --- |
| 1 | `NameError: name 'resultdo' is not defined` | Nome digitado errado. | `resultado` |
| 2 | Nenhuma mensagem, mas mostra `Média da Ana: 3.0` | `soma = nota` troca o valor em vez de somar. | `soma = soma + nota` |

No depurador, `soma` vale 8, depois 7, depois 9: nunca acumula. No final, 9 / 3 = 3.0.

```python
def media(notas):
    soma = 0
    for nota in notas:
        soma = soma + nota
    return soma / len(notas)


notas_ana = [8, 7, 9]
resultado = media(notas_ana)
print("Média da Ana:", resultado)
```

```text
Média da Ana: 8.0
```

### Resposta 6 — Função `situacao`

```python
def situacao(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


assert situacao(10) == "Aprovado"
assert situacao(7) == "Aprovado"
assert situacao(6.9) == "Recuperação"
assert situacao(5) == "Recuperação"
assert situacao(4.9) == "Reprovado"
assert situacao(0) == "Reprovado"

print("Todos os testes passaram!")
```

**Erro comum:** usar `print` dentro da função em vez de `return`. A função mostra o texto, mas devolve `None`, e todos os `assert` falham.

### Resposta 7 — Relatório da turma

O `dados.csv` fica dentro de `exercicios`, junto com o programa.

```python
import csv


def situacao(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


notas = []
melhor_nome = ""
melhor_nota = -1

with open("dados.csv", encoding="utf-8") as arquivo:
    dados = csv.DictReader(arquivo)
    for aluno in dados:
        nome = aluno["nome"]
        nota = float(aluno["nota"])
        notas.append(nota)
        print(nome, nota, situacao(nota))
        if nota > melhor_nota:
            melhor_nota = nota
            melhor_nome = nome

media_turma = sum(notas) / len(notas)
print("Média da turma:", round(media_turma, 1))
print("Maior nota:", melhor_nome, "(" + str(melhor_nota) + ")")
```

```text
Ana 8.0 Aprovado
Bruno 7.0 Aprovado
Carla 9.0 Aprovado
Diego 4.5 Reprovado
Elisa 6.0 Recuperação
Média da turma: 6.9
Maior nota: Carla (9.0)
```

**Erros comuns:** sem `float(...)`, a comparação `"4.5" >= 7` dá `TypeError`. Se aparecer `FileNotFoundError`, o terminal não está dentro de `exercicios`.

### Resposta 8 — Mudança feita no GitHub

Não há código. Está certo quando:

- o commit feito pelo site aparece no `git log --oneline` depois do `git pull`;
- o `README.md` aberto no VS Code mostra a lista nova.

### Resposta das Partes 2 e 3 — `.env` e `.gitignore`

Saída de `config.py`, rodado na raiz do projeto:

```text
Escola: Colegio Exemplo
Nota mínima: 7.0
Chave carregada? True
```

| Verificação | Resultado certo |
| --- | --- |
| `git status` antes do commit | Aparecem `.gitignore`, `.env.example` e `config.py`. O `.env` **não** aparece. |
| `git check-ignore -v .env` | `.gitignore:2:.env .env` |
| `git check-ignore -v .env.example` | Nenhuma resposta: ele não é ignorado, como deve ser. |
| Repositório no GitHub depois do merge | Tem `.gitignore`, `.env.example` e `config.py`. Não tem o `.env`. |
