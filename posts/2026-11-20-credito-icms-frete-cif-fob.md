---
titulo: "Frete CIF e FOB no ICMS: quem tem direito ao crédito na compra e na venda"
resumo: Na venda CIF o frete entra na base do ICMS da nota; na FOB, quem contrata o transporte é o comprador. Veja quem se credita de quê em cada modalidade, com exemplo e os erros mais comuns.
data: 2026-11-20
categoria: Créditos de ICMS
tags: [ICMS, frete, CIF, FOB, CT-e, crédito de ICMS]
fontes:
  - Lei Complementar nº 87/1996 (Lei Kandir), arts. 13, § 1º, II, b, 19 e 20 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp87.htm
  - Regulamento do ICMS de Minas Gerais (RICMS/MG 2023, Decreto nº 48.589/2023) | https://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/ricms_2023_seco/regulamento2023_1.html
checagem:
  - Alíquotas e valores do exemplo são ilustrativos (18% interna e 12% no transporte foram usados só para o cálculo)
  - Confirmar no RICMS/MG 2023 o dispositivo que condiciona o crédito do frete ao tomador identificado no CT-e (citado de forma geral no texto)
  - O tratamento do ICMS do frete na compra de bem do ativo (entrada no CIAP) e o recolhimento pelo tomador no caso de transportador autônomo variam por estado; o texto trata de forma geral
---

O frete é uma das linhas mais esquecidas na apuração do ICMS. Em muitas empresas, o crédito da nota de compra é lançado direitinho, mas o CT-e do transporte fica na pasta do financeiro e nunca chega ao fiscal. Em outras, acontece o contrário: o comprador se credita de um frete que não contratou. A diferença entre CIF e FOB resolve a maior parte dessas dúvidas.

## O que significam CIF e FOB na prática fiscal

As siglas vêm do comércio internacional, mas no dia a dia fiscal brasileiro indicam **quem contrata e paga o transporte**:

- **CIF (frete por conta do remetente):** o vendedor contrata o transporte e embute o custo no preço ou cobra em separado na nota.
- **FOB (frete por conta do destinatário):** o comprador retira a mercadoria ou contrata a transportadora. O frete não passa pela nota de venda.

Essa informação aparece no campo de modalidade do frete da NF-e e precisa bater com o CT-e (Conhecimento de Transporte Eletrônico) emitido pela transportadora. É a partir dessa combinação que o fisco confere quem tem direito ao crédito.

## O que a Lei Kandir diz

Duas regras da Lei Complementar nº 87/1996 sustentam a análise:

1. **O frete pode compor a base do ICMS da venda.** Pelo art. 13, § 1º, II, b, integra a base de cálculo o valor do frete quando o transporte é feito pelo próprio remetente ou por sua conta e ordem e é cobrado em separado.
2. **O serviço de transporte gera crédito.** O art. 20 assegura o crédito do imposto cobrado nas entradas de mercadorias e no recebimento de serviços de transporte interestadual e intermunicipal, respeitadas as vedações (bens alheios à atividade, operações isentas etc.).

Na prática, o crédito do ICMS destacado no CT-e é de quem **tomou o serviço**, ou seja, de quem contratou e consta como tomador no documento. Em Minas Gerais, o RICMS/MG 2023 condiciona o crédito do frete à identificação do tomador no CT-e. Outros estados têm regras semelhantes.

## Quem se credita de quê

| Modalidade | Vendedor | Comprador |
|---|---|---|
| CIF com transportadora | Debita ICMS sobre mercadoria + frete; credita o ICMS do CT-e (é o tomador) | Credita o ICMS destacado na NF-e, que já inclui o frete na base, se a compra der direito a crédito |
| CIF com veículo próprio do vendedor | Debita ICMS sobre mercadoria + frete cobrado; não há CT-e nem ICMS de transporte a creditar | Credita o ICMS da NF-e, se a compra der direito a crédito |
| FOB com transportadora contratada pelo comprador | Debita ICMS só sobre a mercadoria | Credita o ICMS da NF-e e o ICMS do CT-e (é o tomador), se a compra der direito a crédito |
| FOB com veículo próprio do comprador | Debita ICMS só sobre a mercadoria | Credita o ICMS da NF-e; o custo do transporte próprio não tem ICMS de serviço |

A expressão "se a compra der direito a crédito" não é detalhe. O frete segue o destino da mercadoria transportada: se a compra é de material de uso e consumo, cujo crédito está adiado pela LC 87/1996 até 2033, o ICMS do frete dessa compra também fica sem crédito. Se é insumo de produção ou mercadoria para revenda tributada, o frete acompanha.

## Exemplo ilustrativo

Uma indústria vende R$ 10.000 em produtos para um cliente que vai usá-los como insumo. O transporte custa R$ 500. Alíquotas ilustrativas: 18% na venda e 12% no transporte.

**Venda CIF, com transportadora contratada pelo vendedor:**

| Item | Valor |
|---|---|
| Base do ICMS na NF-e (mercadoria + frete) | R$ 10.500,00 |
| ICMS destacado na NF-e (débito do vendedor, crédito do comprador) | R$ 1.890,00 |
| ICMS do CT-e (crédito do vendedor, que é o tomador) | R$ 60,00 |

**Venda FOB, com transportadora contratada pelo comprador:**

| Item | Valor |
|---|---|
| ICMS destacado na NF-e (só a mercadoria) | R$ 1.800,00 |
| ICMS do CT-e (crédito do comprador, que é o tomador) | R$ 60,00 |
| Crédito total do comprador | R$ 1.860,00 |

Nas duas situações, o comprador acaba se creditando de valores próximos, mas por caminhos diferentes. Na CIF, o crédito do frete vem embutido na nota de venda. Na FOB, ele depende de o CT-e chegar ao fiscal e ser escriturado. É justamente no FOB que o crédito mais se perde.

## Erros que geram perda de crédito ou glosa

- **CT-e não escriturado.** O comprador FOB paga a transportadora, o financeiro lança a despesa e o fiscal nunca recebe o documento. O crédito fica de fora da EFD ICMS/IPI.
- **Crédito tomado por quem não é tomador.** Na venda CIF, o comprador às vezes recebe cópia do CT-e e se credita dele. O crédito é do vendedor. Esse erro aparece fácil no cruzamento de documentos eletrônicos.
- **Modalidade de frete divergente.** NF-e marcada como FOB e CT-e com o vendedor como tomador (ou o inverso) abre espaço para questionamento das duas pontas.
- **Frete de uso e consumo creditado.** O frete de uma compra sem direito a crédito não gera crédito sozinho.
- **Transporte municipal.** O transporte que começa e termina no mesmo município é serviço sujeito ao ISS, não ao ICMS. Não há ICMS a creditar.

Para os detalhes do serviço de transporte em si (subcontratação, redespacho, transportador autônomo, documentos exigidos), veja o post sobre [crédito de ICMS no transporte de insumos](/credito-icms-servico-transporte-insumos/).

## Casos que merecem atenção

**Transportador autônomo.** Quando o transporte é feito por pessoa física sem inscrição, vários estados atribuem ao tomador contribuinte a responsabilidade pelo recolhimento do ICMS do frete. Se esse imposto pode ser creditado, e de que forma, depende da legislação de cada estado.

**Compra de bem do ativo.** O ICMS do frete na compra de uma máquina costuma seguir a lógica do próprio bem, com apropriação no CIAP em 48 meses. Confirme a regra do seu estado antes de lançar o crédito integral no mês.

**Frete na exportação.** O frete até o porto ou aeroporto, quando a operação é de exportação, tem tratamento próprio e pode envolver não incidência. Vale analisar separadamente.

## O que fazer agora

1. Puxe do ambiente nacional dos documentos eletrônicos os CT-e em que a empresa aparece como tomadora nos últimos meses.
2. Compare com os CT-e escriturados na EFD ICMS/IPI. Os que faltam são crédito potencial (dentro do prazo de cinco anos da emissão).
3. Confira se a modalidade de frete das NF-e de compra e venda bate com o tomador indicado nos CT-e.
4. Revise se algum crédito de frete foi tomado em compras de uso e consumo ou em transporte municipal.
5. Combine com o financeiro um fluxo para que todo CT-e pago chegue ao fiscal antes do fechamento da apuração.
