**Preparação para as aulas e materiais de estudo**

Pessoal, antes de cada aula, reservem alguns minutos para preparar o ambiente:

1. Fechem abas, programas e arquivos que não serão necessários.
2. Abram o VS Code e a **pasta do projeto**, pelo menu **Arquivo → Abrir Pasta**.
3. Sigam o guia de preparação disponível em:
   `documentos/guia_basico_trabalhar_com_vscode/guia_basico_vscode.pdf` ou nesse link https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises/blob/main/documentos/guia_basico_trabalhar_com_vscode/guia_basico_vscode.pdf

4. Abram o notebook/código da atividade, selecionem o kernel Python e executem uma célula para conferir se está funcionando.

5. Caso ainda não tenham feito o set up do Jupyter notebook para usarem notebook no VS Code, aqui tem como fazer -> https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises/blob/main/documentos/install_python_git_vscode/habilitar_jupyter_notebook.md

**Onde encontrar os materiais**

As demonstrações, os exercícios e os materiais de estudo ficarão no GitHub da turma:

https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises

O repositório está organizado em pastas:

- **`data_analysis`**: demonstrações e exercícios de análise de dados.
- **`documentos`**: guias para preparar o ambiente e organizar o raciocínio ao resolver exercícios.
- **`exercicios_resolvidos`**: soluções para conferir os resultados e estudar os passos.
- **`materiais_de_apoio`**: explicações e links para revisar os conteúdos e esclarecer dúvidas.

Mantenham os arquivos de dados nas pastas fornecidas para que os notebooks consigam encontrá-los. Tentem resolver as atividades antes de consultar as soluções.

**Como trabalhar em uma cópia própria — fork**

Se preferirem, podem criar um **fork**, que é uma cópia do repositório na sua conta do GitHub:

1. Acessem o repositório da turma.
2. Cliquem em **Fork**, no canto superior direito.
3. Escolham sua conta e cliquem em **Create fork**.
4. No seu fork, cliquem em **Code** e copiem o endereço HTTPS.
5. No VS Code, abram a Paleta de Comandos, procurem **Git: Clone**, colem o endereço e escolham onde salvar o projeto.
6. Quando terminar, abram a pasta clonada.

Quando novos materiais forem publicados:

1. Abram **seu fork no GitHub**.
2. Cliquem em **Sync fork → Update branch**.
3. No computador, salvem e registrem suas alterações com um commit.
4. No VS Code, usem **Git: Pull** para trazer as atualizações.

**Sync fork atualiza sua cópia no GitHub; Pull traz essas atualizações para o computador.** Se aparecer conflito, peçam ajuda antes de continuar.

Guia de sincronização:
https://docs.github.com/en/pull-requests/how-tos/work-with-forks/syncing-a-fork

**Se ainda não configuraram o Jupyter**

1. Instalem as extensões **Python** e **Jupyter**, ambas da Microsoft.
2. Abram um arquivo `.ipynb`.
3. Cliquem em **Select Kernel / Selecionar Kernel**, no canto superior direito.
4. Escolham o ambiente Python da atividade.
5. Se o VS Code solicitar a instalação de `ipykernel`, sigam a orientação apresentada.

Guia oficial:
https://code.visualstudio.com/docs/datascience/jupyter-notebooks

**Para quem tem dificuldade com funções**

Assistam à demonstração sobre reutilizar uma tarefa sem repetir todo o código:

https://www.youtube.com/watch?v=XbvSBegg09s

Para entender melhor a diferença entre `print` e `return`:

https://www.youtube.com/watch?v=elxVw67ayug

Depois, tentem responder: **quais dados minha função recebe, o que ela faz e o que devolve?**

**Para quem tem dificuldade em começar os exercícios**

Consultem:
`documentos/como_resolver_exercicios/guia_alunos_fluxograma_python_pandas.pdf` ou no link https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises/blob/main/documentos/como_resolver_exercicios/guia_alunos_fluxograma_python_pandas.pdf

Antes de escrever código, respondam:

- Quais dados tenho?
- O que o enunciado pede?
- Qual resultado espero?
- Quais passos preciso seguir em português?

Resolvam um exemplo pequeno à mão e depois transformem os passos em Python.

**Para quem tem dificuldade com GitHub**

Comecem pelo material:
`materiais_de_apoio/git_github_vscode.md`
ou no link https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises/blob/main/documentos/install_python_git_vscode/Install_python_git_github_vscode.md a partir do A3.

Pratiquem uma etapa por vez: encontrar o repositório, trazer os arquivos para o computador, abrir o projeto e atualizar os materiais.

**Para quem tem dificuldade com o terminal no VS Code**

Consultem o guia em `documentos/guia_basico_trabalhar_com_vscode` link https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises/blob/main/documentos/guia_basico_trabalhar_com_vscode/guia_basico_vscode.pdf e esta videoaula:

https://www.youtube.com/watch?v=mOtSc3SbavY

Para abrir o terminal integrado, usem **Terminal → Novo Terminal**.

**Durante a prática**

Executem as células em ordem e consultem os materiais de apoio conforme a dificuldade encontrada. Se travarem, anotem **o que tentaram, qual resultado esperavam e qual mensagem de erro apareceu**. Isso ajuda a identificar o problema e pedir ajuda.

**Para instalar bibliotecas e/ou problemas com pip**

Por favor, sigam os passos desse documento:
https://github.com/Machine-Learning-Visao-Computacional-T5/python_exercises/blob/main/documentos/pip_install_bibliotecas/pip_install_bibiotecas.md