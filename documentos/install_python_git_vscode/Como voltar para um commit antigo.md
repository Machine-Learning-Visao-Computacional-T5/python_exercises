# Como voltar para um commit antigo

## Resumo

Ache o hash do commit e escolha como voltar. Na dúvida, use `git restore` + commit, que não reescreve o histórico.

| Situação | O que usar |
| --- | --- |
| Só quero olhar uma versão antiga | `git checkout <hash>` |
| Quero o código igual a uma versão antiga | `git restore --source=<hash>` + commit |
| Preciso desfazer um commit específico | `git revert <hash>` |
| A branch é só minha e quero apagar commits | `git reset --hard` + `push --force-with-lease` |

## Voltar versão no Git

Primeiro ache o hash do commit de destino, depois escolha a opção. Na dúvida, use a opção B.

**Achar o commit**

```bash
git log --oneline
```

No GitHub, o hash também aparece na aba Commits do repositório.

**A. Só olhar a versão antiga**

```bash
git checkout a1b2c3d   # o projeto fica como naquele commit
git switch -           # volta ao estado atual
```

**B. Voltar mantendo o histórico (recomendado)**

O código fica igual ao do commit antigo, e isso vira um commit novo, que dá pra desfazer.

```bash
git restore --source=a1b2c3d --staged --worktree .
git commit -m "Volta para a versão a1b2c3d"
git push
```

Pra desfazer só um commit específico, use `git revert <hash>` e depois `git push`.

**C. Apagar os commits depois daquele**

```bash
git branch backup-antes-do-reset
git reset --hard a1b2c3d
git push --force-with-lease
```

Os commits mais novos somem da branch, e quem já baixou vai ter conflito. Use só numa branch que é só sua.

**Pelo site do GitHub:** não há botão pra voltar a uma versão. Dá pra ver o código antigo em Browse files, num commit, ou desfazer um PR já mergeado com o botão Revert.
