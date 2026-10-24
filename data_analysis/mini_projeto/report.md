# Relatório — Festa em Cena

A análise do arquivo identificou 1.500 linhas e 1.500 pedidos distintos. Cada linha representa um pedido de um produto, que pode incluir várias unidades. A base é fictícia e cobre agosto a novembro de 2024 e 2025. As contagens incluem Concluído, Cancelado e Devolvido e representam pedidos registrados, não receita nem vendas concluídas.

Na limpeza, 18 categorias vazias foram preenchidas com "sem categoria". As outras 1.482 categorias foram alteradas pela padronização para minúsculas, remoção de espaços nas extremidades e, quando necessário, retirada de pontuação com expressão regular. Esse total inclui mudanças apenas de maiúsculas para minúsculas; não significa que todas essas categorias tinham pontuação indevida.

Foram encontrados 7 pedidos com quantidade inválida e 12 com preço inválido. A união desses grupos contém 19 pedidos; nesta base não há sobreposição. Outros 4 pedidos apresentam data de venda inválida ou vazia, totalizando 23 pedidos com pelo menos um problema numérico ou temporal. Os valores originais foram preservados e os problemas sinalizados, sem imputação de números ou datas.

A hipótese de que todo pedido sem data de entrega é cancelado foi refutada: 109 pedidos sem entrega estão cancelados, mas 34 possuem outros status. Os pedidos 1170, 990 e 740, por exemplo, estão como Concluído e não têm data de entrega. A ausência desse campo não comprova cancelamento nem permite afirmar que a entrega não ocorreu; recomenda-se investigar o preenchimento antes de usar esse campo como indicador operacional.

Por canal, a Web registra 666 pedidos (44,4%), a Loja física 551 (36,7%) e o Mercado 283 (18,9%). Todos os canais foram reconhecidos, sem exclusões. A Web concentra a maior parcela dos registros e merece atenção no planejamento operacional. Entretanto, sem avaliar valores, unidades e status separadamente, não se pode concluir que ela gere maior faturamento ou mais vendas efetivas.

Por período, outubro lidera nos dois anos: 393 pedidos em 2024 e 410 em 2025, aumento de 17 registros (4,3%). Somados, os dois outubros representam 803 dos 1.496 pedidos com data válida (53,7%). O padrão é compatível com a concentração de procura próxima ao Halloween e pode orientar o planejamento de estoque. A análise exclui 4 datas inválidas e inclui todos os status. Dois anos de dados fictícios não permitem comprovar sazonalidade no mercado real nem atribuir causalidade ao evento.

A qualidade dos dados é uma etapa anterior à modelagem. A limpeza melhora a consistência, mas não garante representatividade ou elimina overfitting e underfitting, que também dependem do modelo e de sua avaliação.
