---
titulo: "PER/DCOMP passo a passo: como compensar crédito de tributo federal sem cair em glosa"
resumo: A compensação de tributos federais é feita pelo PER/DCOMP e extingue o débito sob condição de homologação em até 5 anos. Veja a sequência correta, os débitos que não podem ser compensados e um exemplo com Selic.
data: 2026-11-20
categoria: Recuperação de Créditos
tags: [PER/DCOMP, compensação, Receita Federal, Selic, créditos tributários]
fontes:
  - Lei nº 9.430/1996, art. 74 (compensação por declaração) | https://www.planalto.gov.br/ccivil_03/leis/l9430.htm
  - Lei nº 9.250/1995, art. 39, § 4º (juros Selic na compensação e na restituição) | https://www.planalto.gov.br/ccivil_03/leis/l9250.htm
  - Lei nº 10.833/2003, art. 18, § 4º (multa isolada na compensação não declarada) | https://www.planalto.gov.br/ccivil_03/leis/2003/l10.833.htm
  - Instrução Normativa RFB nº 2.055/2021 (restituição, compensação, ressarcimento e reembolso) | https://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=122002
  - Receita Federal, como solicitar ou compensar crédito de pagamento | https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/restituicao-ressarcimento-reembolso-e-compensacao/creditos/pagamento/darf/como-solicitar-ou-compensar-o-credito
checagem:
  - A taxa Selic acumulada do exemplo é ilustrativa
  - Os nomes de menus do PER/DCOMP Web podem mudar; o texto descreve a sequência lógica, não telas específicas
  - A IN RFB nº 2.055/2021 teve alterações recentes (por exemplo, IN RFB nº 2.288/2025 e IN RFB nº 2.314/2026, citadas em fontes secundárias); conferir a redação consolidada antes de aplicar a casos específicos
---

A empresa encontrou um crédito: um pagamento de COFINS feito a maior, um saldo negativo de IRPJ, um saldo de PIS e COFINS acumulado com exportações. O próximo passo é usar esse crédito para pagar outros tributos federais. A ferramenta é o PER/DCOMP, e a forma como ele é preenchido decide se o crédito vira economia ou cobrança com multa e juros.

## O que a lei permite

O art. 74 da Lei nº 9.430/1996 autoriza o contribuinte a usar créditos de tributos administrados pela Receita Federal, passíveis de restituição ou ressarcimento, para compensar débitos próprios de tributos administrados pelo mesmo órgão. Os pontos-chave do artigo:

- a compensação é feita por **declaração** do contribuinte (§ 1º), a Declaração de Compensação, transmitida pelo PER/DCOMP;
- a declaração **extingue o débito sob condição resolutória** (§ 2º): ele está quitado, mas a Receita pode rever;
- a Receita tem **5 anos, contados da entrega**, para homologar (§ 5º); sem manifestação nesse prazo, a compensação é homologada tacitamente;
- a declaração é **confissão de dívida** (§ 6º): se não homologada, o débito pode ser cobrado diretamente.

## Débitos que não podem ser compensados

O § 3º do art. 74 lista hipóteses em que a compensação por declaração não é permitida. Entre elas:

- débitos já encaminhados à PGFN para inscrição em dívida ativa;
- débitos consolidados em parcelamento;
- débitos que já foram objeto de compensação não homologada;
- créditos de pedido de restituição ou ressarcimento já indeferido;
- estimativas mensais de IRPJ e CSLL;
- crédito judicial acima do limite mensal do art. 74-A.

Uma declaração com essas hipóteses é considerada **não declarada** (§ 12, I), sem o rito de defesa da compensação comum. O inciso II do mesmo parágrafo traz outras hipóteses de compensação não declarada, ligadas à natureza do crédito (crédito de terceiros, decisão judicial não transitada em julgado, crédito de PIS ou COFINS sem relação com a atividade, entre outras), e nelas o art. 18, § 4º, da Lei nº 10.833/2003 prevê multa isolada.

## A sequência correta

**1. Confirmar o crédito e o prazo.** Identifique o tipo de crédito (pagamento indevido, saldo negativo, ressarcimento de PIS e COFINS ou de IPI, crédito judicial) e confira se ainda está dentro do prazo de cinco anos.

**2. Retificar antes de compensar.** Um pagamento só fica "disponível" como crédito quando a declaração de débitos mostra que ele foi maior que o devido. Se o débito declarado na DCTF (até 2024) ou na DCTFWeb (fatos geradores a partir de 2025) ainda está no valor antigo, o sistema vai entender que o pagamento foi usado. A escrituração (EFD-Contribuições, EFD ICMS/IPI, ECF) também deve ser retificada antes, para manter coerência. A ordem está em [retificação do SPED na recuperação de créditos](/retificacao-sped-recuperacao-creditos/).

**3. Habilitar, se for crédito judicial.** Crédito reconhecido em ação transitada em julgado precisa ser habilitado na Receita antes da primeira compensação. Veja [habilitação de crédito judicial](/habilitacao-credito-judicial-receita-federal/).

**4. Preencher o PER/DCOMP.** No e-CAC, a empresa informa o crédito (com os dados do pagamento, do período de apuração ou do processo) e os débitos que deseja compensar. O sistema calcula a atualização do crédito.

**5. Ajustar a declaração de débitos.** Os débitos compensados continuam declarados normalmente na DCTFWeb; o PER/DCOMP é que informa a forma de quitação.

**6. Acompanhar.** Despachos decisórios chegam pela caixa postal do e-CAC. O prazo para contestar uma não homologação conta da ciência, e a ciência pode ocorrer por decurso de prazo na caixa postal.

## Atualização do crédito

Os créditos de pagamento indevido e de saldo negativo são atualizados pela **Selic** acumulada desde o mês seguinte ao do pagamento até o mês anterior ao da compensação, mais 1% no mês da compensação (Lei nº 9.250/1995, art. 39, § 4º). O ressarcimento de créditos escriturais de PIS e COFINS tem regra diferente: o STJ (Tema 1003) entendeu que a correção só começa depois de 360 dias do protocolo do pedido, quando a Receita não o analisa nesse prazo.

## Exemplo ilustrativo

Uma indústria pagou R$ 120.000 de COFINS a maior em um DARF. Retificou a escrituração e a DCTFWeb do período e, meses depois, compensou o crédito com IRPJ.

| Item | Valor |
|---|---|
| Valor original do crédito | R$ 120.000,00 |
| Selic acumulada no período (ilustrativa) | 18% |
| Acréscimo de 1% no mês da compensação | 1% |
| **Crédito atualizado (120.000 × 1,19)** | **R$ 142.800,00** |

Se o débito de IRPJ do mês for de R$ 100.000, a empresa compensa esse valor e mantém saldo de crédito para uma próxima declaração.

## Erros comuns

- Compensar antes de retificar a declaração de débitos do período de origem.
- Informar como crédito um pagamento já usado em outra compensação.
- Compensar estimativas de IRPJ e CSLL.
- Deixar de acompanhar a caixa postal e perder o prazo de defesa. As consequências estão em compensação não homologada.

## O que fazer agora

1. Monte um quadro com cada crédito, sua origem, período, valor e data-limite de uso.
2. Confira se as obrigações de origem já foram retificadas e se os sistemas da Receita refletem o crédito.
3. Verifique se algum débito que se pretende compensar está nas vedações do § 3º.
4. Defina quem acompanha a caixa postal do e-CAC e com que frequência.
5. Guarde a memória de cálculo e os documentos de cada crédito por, no mínimo, cinco anos após a entrega da declaração.
