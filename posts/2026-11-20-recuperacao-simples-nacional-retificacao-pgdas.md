---
titulo: "Recuperação de tributos no Simples Nacional: como a retificação do PGDAS-D destrava o valor pago a maior"
resumo: No Simples, quase todo valor pago a maior nasce de uma receita segregada de forma errada no PGDAS-D. Veja o caminho certo: retificar, separar o que é federal do que é ICMS e ISS, e pedir restituição ou compensação.
data: 2026-11-20
categoria: Recuperação de Créditos
tags: [Simples Nacional, PGDAS-D, restituição, compensação, ICMS-ST, monofásico]
fontes:
  - Lei Complementar nº 123/2006 (Estatuto da Microempresa), art. 21 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm
  - Receita Federal, Manual do Pedido Eletrônico de Restituição do Simples Nacional | https://www8.receita.fazenda.gov.br/SimplesNacional/Arquivos/manual/MANUAL_RESTITUICAO.pdf
  - Portal do Simples Nacional (Resolução CGSN nº 140/2018 e serviços de restituição e compensação) | https://www8.receita.fazenda.gov.br/SimplesNacional/
  - Código Tributário Nacional, arts. 165 e 168 | https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm
checagem:
  - Alíquota efetiva e percentuais de repartição do exemplo são ilustrativos; os percentuais reais dependem do anexo e da faixa de receita
  - Confirmar na Resolução CGSN nº 140/2018 os artigos atuais sobre retificação, restituição e compensação (a numeração foi citada de forma geral, sem artigo específico)
  - O procedimento de restituição do ICMS pago no DAS varia por estado; o texto não descreve o rito de nenhum estado específico
  - Confirmar se a compensação no próprio aplicativo do Simples continua restrita a débitos do mesmo regime (o texto trata a regra de forma geral)
  - Confirmar na Resolução CGSN nº 140/2018 a regra de atualização pela Selic dos valores federais restituídos ou compensados no Simples
---

A empresa do Simples Nacional paga um único boleto, o DAS (Documento de Arrecadação do Simples Nacional), e por isso muita gente acha que não existe "crédito" a recuperar. Existe. Ele nasce quase sempre de uma informação errada no PGDAS-D (Programa Gerador do DAS Declaratório): receita de produto com ICMS já recolhido por substituição tributária lançada como receita normal, produto monofásico tributado de novo, venda para o exterior sem marcação de exportação. O DAS sai maior do que deveria, todo mês, e ninguém percebe porque o valor "parece normal".

A boa notícia é que o caminho para corrigir está dentro do próprio sistema do Simples. A má notícia é que muita empresa pula etapas e trava o pedido.

## Por que tudo começa no PGDAS-D

No Simples, o valor devido não é calculado pela Receita a partir das notas. É o próprio contribuinte que informa a receita do mês no PGDAS-D e diz como ela se divide: revenda, industrialização, serviço, com ou sem substituição tributária, com ou sem tributação monofásica, mercado interno ou exportação. A partir dessa segregação, o sistema aplica a alíquota efetiva e retira do cálculo os tributos que não deveriam incidir naquela parcela.

A declaração tem natureza de confissão de dívida. Enquanto ela disser que o tributo era devido, não há pagamento indevido para restituir. Por isso a ordem é sempre esta:

1. Identificar o erro de segregação, mês a mês.
2. **Retificar o PGDAS-D** do período, informando a receita do jeito certo.
3. Só então usar o saldo que aparece, por restituição ou compensação.

Pedir restituição sem retificar antes não funciona: o sistema não enxerga valor pago a maior.

## Os erros de segregação mais comuns

| Situação | O que acontece no DAS | Tributo afetado |
|---|---|---|
| Revenda de mercadoria com ICMS-ST já retido pelo fornecedor, informada sem substituição | O DAS cobra de novo a parcela do ICMS | ICMS (estadual) |
| Revenda de produto monofásico de PIS/COFINS informada como tributada | O DAS cobra PIS e COFINS que já foram pagos na indústria | PIS e COFINS (federais) |
| Venda ao exterior informada como mercado interno | O DAS cobra tributos sobre receita que tem tratamento próprio na exportação | Vários |
| ISS retido pelo tomador informado como não retido | O DAS cobra o ISS de novo | ISS (municipal) |
| Atividade enquadrada no anexo errado | Alíquota efetiva diferente da correta | Vários |

O caso do monofásico tem regras e um método de identificação próprios, que explicamos em [recuperação do monofásico no Simples Nacional](/pis-cofins-monofasico-simples-nacional-recuperacao/). Aqui o foco é o procedimento que vale para qualquer erro de segregação.

## Federal de um lado, ICMS e ISS do outro

Este é o ponto que mais confunde. O DAS reúne tributos de três entes, mas a devolução não é única. Pelo manual do Pedido Eletrônico de Restituição da Receita Federal, o aplicativo do Simples restitui os tributos federais apurados no regime (IRPJ, CSLL, contribuição previdenciária, PIS, COFINS e IPI). A restituição do ICMS e do ISS só pode ser pedida ao estado ou ao município.

Na prática:

- **Erro que reduz PIS e COFINS** (monofásico, por exemplo): depois da retificação, o saldo federal pode ser objeto de pedido de restituição no e-CAC ou de compensação com DAS futuros, nos serviços do Portal do Simples.
- **Erro que reduz ICMS** (substituição tributária, por exemplo): a retificação mostra o ICMS pago a maior, mas o pedido segue o rito da Secretaria de Fazenda do estado. Cada estado tem formulário, documentos e prazo de análise próprios.
- **Erro que reduz ISS**: o pedido é feito ao município.

Uma empresa de Minas Gerais que errou na substituição tributária, por exemplo, precisa seguir o procedimento da SEF-MG para o ICMS, mesmo que o restante do crédito seja tratado no e-CAC.

## Exemplo ilustrativo

Um comércio do Simples tem receita mensal de R$ 200.000. Suponha uma alíquota efetiva de 8%, com a parcela do ICMS representando 34% do DAS e a de PIS e COFINS somando 15,5% (percentuais ilustrativos; os reais dependem do anexo e da faixa). Na revisão, descobre-se que R$ 50.000 por mês eram de produtos com ICMS-ST já retido e R$ 30.000 de produtos monofásicos, todos informados como receita comum.

| Item | Cálculo | Valor mensal |
|---|---|---|
| DAS pago | R$ 200.000 × 8% | R$ 16.000,00 |
| ICMS pago a maior (parcela ST) | R$ 50.000 × 8% × 34% | R$ 1.360,00 |
| PIS e COFINS pagos a maior (monofásicos) | R$ 30.000 × 8% × 15,5% | R$ 372,00 |
| **Total pago a maior no mês** | | **R$ 1.732,00** |
| Em 12 meses | | R$ 20.784,00 |

Repare que, desses R$ 1.732 mensais, R$ 1.360 são ICMS e seguem para o estado. Só R$ 372 entram no pedido federal. Quem não separa os dois montantes cria uma expectativa errada sobre prazo e forma de devolução.

## Prazo de cinco anos

O direito de pedir restituição de tributo pago indevidamente se extingue em cinco anos contados do pagamento (CTN, arts. 165 e 168). Cada mês tem o seu prazo correndo de forma independente. Uma revisão feita hoje alcança, em regra, os pagamentos dos últimos 60 meses, e a cada mês que passa o mais antigo sai da janela. Detalhamos esse prazo em [prazo para recuperar tributos pagos a maior](/prazo-recuperar-tributos-pagos-a-maior/).

## Cuidados antes de retificar

- **Prova da segregação.** Para cada mês retificado, guarde a relação de notas que sustenta a nova divisão da receita: NCM do produto, CST ou CSOSN, valor do ICMS-ST retido pelo fornecedor. Se a fiscalização questionar, é isso que vai ser pedido.
- **Cadastro de produtos.** Na maioria dos casos o erro vem do cadastro do ERP, que não marca o produto como ST ou monofásico. Retificar o passado sem corrigir o cadastro faz o erro continuar no mês seguinte.
- **Coerência com o estado.** A retificação do PGDAS-D altera as informações que o estado recebe. Se a empresa entrega declarações estaduais complementares, elas também precisam estar coerentes.
- **Débitos em aberto.** Restituição de tributo federal pode ser usada pela Receita para quitar débitos pendentes da empresa antes do pagamento. Confira a situação fiscal antes do pedido.
- **Pedido certo para cada DAS.** O manual da Receita orienta um pedido de restituição por documento de arrecadação. Em uma revisão de 60 meses, isso exige organização.

## Restituição ou compensação?

A restituição devolve o dinheiro em conta, depois da análise. A compensação usa o saldo para abater DAS futuros, o que costuma ser mais rápido para quem tem DAS mensal relevante. A escolha depende do caixa da empresa e do tamanho do saldo de cada tributo. Em ambos os casos, o valor federal é corrigido pela Selic, conforme a legislação do regime.

## O que fazer agora

1. Puxe os PGDAS-D dos últimos 60 meses e veja como a receita foi segregada em cada um.
2. Cruze com as notas de entrada: quais produtos vieram com ICMS-ST retido e quais têm NCM de tributação monofásica.
3. Monte uma planilha mês a mês separando o valor pago a maior por tributo e por ente (federal, estado, município).
4. Corrija o cadastro de produtos no ERP antes de retificar o passado.
5. Retifique o PGDAS-D, faça os pedidos federais no e-CAC e siga o rito da Secretaria de Fazenda do seu estado para o ICMS.
