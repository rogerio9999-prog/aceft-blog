---
titulo: "NCM, CEST e substituição tributária: como saber se o produto está na ST do ICMS"
resumo: A NCM sozinha não decide se o produto está na substituição tributária do ICMS. A descrição do item, o segmento e o CEST também contam, e a regra varia por estado. Veja como conferir, com exemplo.
data: 2026-11-20
categoria: Classificação Fiscal
tags: [CEST, NCM, substituição tributária, ICMS-ST, Convênio ICMS 142/2018]
fontes:
  - Convênio ICMS nº 142/2018 (regras gerais da substituição tributária, segmentos e CEST) | https://www.confaz.fazenda.gov.br/legislacao/convenios/2018/CV142_18
  - Regulamento do ICMS de Minas Gerais (RICMS/MG 2023), Anexo VII (substituição tributária) | https://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/ricms_2023_seco/sumario2023seco.html
checagem:
  - MVA, alíquotas e valores do exemplo são ilustrativos; cada estado define MVA e alíquotas
  - Confirmar a regra atual de obrigatoriedade de informar o CEST na NF-e (convênio e leiaute da NF-e)
  - Confirmar se o Anexo VII do RICMS/MG 2023 continua concentrando as regras de ST em Minas Gerais na data da publicação
---

A distribuidora compra um item de um fabricante de outro estado, a nota vem sem ICMS-ST retido, e três meses depois a fiscalização entende que o produto estava na substituição tributária. Agora o ICMS-ST é cobrado do destinatário, com multa. Ou o contrário: a empresa recolhe ST sobre um produto que, pela descrição do convênio, nunca esteve no regime, e paga imposto antecipado que não devia. Nos dois casos a origem costuma ser a mesma: alguém olhou só a NCM.

## A NCM é o ponto de partida, não a resposta

A substituição tributária do ICMS (ICMS-ST) concentra numa empresa da cadeia, em geral o fabricante ou o importador, o recolhimento do imposto das operações seguintes. Quais mercadorias entram no regime é decisão de cada estado, por lei própria e por convênios e protocolos firmados no CONFAZ.

O Convênio ICMS nº 142/2018 organiza as regras gerais. Pela cláusula sétima, os bens passíveis de ST são os identificados nos Anexos II a XXVI do convênio, agrupados por segmento, cada item com **descrição, NCM e CEST**. E há três regras que mudam a forma de ler a tabela:

- **A descrição prevalece.** Quando a descrição do item não reproduz a descrição do código NCM, a ST se aplica somente aos bens que correspondam à descrição do convênio (§ 1º).
- **Reclassificação não inclui nem exclui.** Mudanças de código na NCM não colocam nem tiram produto da ST; a empresa informa o código novo e mantém o tratamento anterior (§§ 2º e 3º).
- **O segmento importa.** O regime alcança somente os itens vinculados aos segmentos em que estão inseridos (§ 7º).

Ou seja: um produto pode ter uma NCM que aparece no anexo e mesmo assim não estar na ST, porque a descrição do item é mais restrita. E dois produtos com a mesma NCM podem ter tratamentos diferentes.

## O que é o CEST

O Código Especificador da Substituição Tributária (CEST) tem sete dígitos, segundo o próprio convênio:

| Dígitos | Significado |
|---|---|
| 1º e 2º | Segmento do bem ou mercadoria |
| 3º ao 5º | Item dentro do segmento |
| 6º e 7º | Especificação do item |

O CEST existe para identificar, de forma uniforme entre os estados, as mercadorias passíveis de ST. O convênio exige que convênios, protocolos e leis estaduais que instituírem a ST reproduzam o CEST, a NCM e a descrição constantes dos anexos. O CEST é informado na NF-e, e o seu preenchimento correto depende de a empresa ter identificado o item certo do segmento certo.

Alguns segmentos têm regras em convênios específicos, fora do Convênio 142/2018: energia elétrica, combustíveis e lubrificantes, venda porta a porta e veículos vendidos por faturamento direto ao consumidor (cláusula quinta).

## O estado de destino manda

O sujeito passivo por substituição segue a legislação da unidade federada de destino da mercadoria (cláusula quarta do convênio). Na prática, a pergunta "este produto está na ST?" tem uma resposta para cada estado. Em operações internas de Minas Gerais, a referência é o Anexo VII do RICMS/MG 2023. Em vendas interestaduais, a empresa precisa conferir se há convênio ou protocolo entre o estado de origem e o de destino para aquele item e, se houver, quem é o responsável pela retenção.

## Exemplo ilustrativo do efeito de um enquadramento errado

Uma indústria vende uma mercadoria por R$ 1.000,00 para um revendedor de outro estado. Suponha (valores ilustrativos) alíquota interestadual de 12%, alíquota interna no destino de 18% e Margem de Valor Agregado (MVA) de 40%.

| Item | Cálculo | Valor |
|---|---|---|
| ICMS próprio | R$ 1.000,00 × 12% | R$ 120,00 |
| Base de cálculo da ST | R$ 1.000,00 × 1,40 | R$ 1.400,00 |
| ICMS total da cadeia | R$ 1.400,00 × 18% | R$ 252,00 |
| ICMS-ST a reter | R$ 252,00 menos R$ 120,00 | R$ 132,00 |

Se a mercadoria estiver na ST e a indústria não reter, a diferença de R$ 132,00 por unidade fica em aberto. Dependendo do estado, a cobrança pode recair sobre o remetente, sobre o destinatário ou sobre ambos. Se ela não estiver na ST e a indústria reter, o cliente paga imposto antecipado indevido, que depois precisa ser recuperado pelo rito do estado.

## Erros comuns

- **Usar só os quatro primeiros dígitos da NCM** para concluir que o produto está na ST, sem ler a descrição do item.
- **Escolher o CEST "mais parecido"** sem conferir o segmento. O mesmo tipo de produto pode aparecer em segmentos diferentes, com tratamentos diferentes.
- **Copiar o CEST do fornecedor** sem conferir, quando a empresa é a responsável pela retenção.
- **Esquecer a alteração da legislação estadual.** Estados incluem e excluem itens da ST com frequência.
- **Não revisar o cadastro depois de uma reclassificação da NCM**, aplicando um tratamento diferente do que o convênio manda manter.

O post sobre [riscos da NCM errada](/erro-classificacao-ncm-riscos/) mostra como esse erro se combina com IPI e PIS/COFINS.

## E com a Reforma Tributária?

O ICMS será extinto a partir de 2033, depois de uma redução gradual das alíquotas entre 2029 e 2032. Até lá a ST continua valendo, com as regras de cada estado. A Lei Complementar nº 227/2026 já prevê um procedimento para o ICMS retido por substituição relativo às mercadorias em estoque em 31 de dezembro de 2032, que exigirá inventário desse estoque. Cadastro de NCM e CEST bem feito agora facilita esse levantamento.

## O que fazer agora

1. Extraia do ERP os produtos com CEST preenchido e os produtos sem CEST cuja NCM aparece nos anexos do Convênio 142/2018.
2. Para cada item, compare a descrição do produto com a descrição exata do item no anexo do segmento.
3. Confira, para os principais estados de destino, se há regra de ST e quem é o responsável pela retenção.
4. Em Minas Gerais, confronte o cadastro com o Anexo VII do RICMS/MG 2023.
5. Corrija o cadastro e quantifique eventuais diferenças de ICMS-ST nos últimos cinco anos, a pagar e a recuperar.
