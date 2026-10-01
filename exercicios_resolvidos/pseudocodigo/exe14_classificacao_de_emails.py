"""Exercício 14 — Classificação de e-mails

Receba a quantidade de palavras suspeitas em um e-mail. Se houver três ou mais, classifique-o como “Possível spam”; caso contrário, como “E-mail normal”.

Pseudocódigo:

    INÍCIO
        LER quantidade_palavras_suspeitas
        SE quantidade_palavras_suspeitas >= 3 ENTÃO
            MOSTRAR "Possível spam"
        SENÃO
            MOSTRAR "E-mail normal"
        FIM_SE
    FIM
"""

quantidade_palavras_suspeitas = int(input("Quantidade de palavras suspeitas: "))

if quantidade_palavras_suspeitas >= 3:
    print("Possível spam")
else:
    print("E-mail normal")
