---
titulo: "Teste de recuperabilidade do imobilizado (impairment, CPC 01): quando fazer, como calcular e o efeito no IRPJ"
resumo: Quando uma linha de produção vale menos do que mostra o balanço, o CPC 01 exige reconhecer a perda. Veja os indícios que obrigam o teste, o cálculo do valor recuperável com exemplo e por que a perda não é dedutível de imediato.
data: 2026-11-20
categoria: Ativo Imobilizado
tags: [impairment, CPC 01, valor recuperável, valor em uso, ativo imobilizado, Lei 12.973/2014]
fontes:
  - CPC 01: Redução ao Valor Recuperável de Ativos | https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=2
  - Lei nº 6.404/1976, art. 183, § 3º (análise periódica da recuperação do imobilizado) | https://www.planalto.gov.br/ccivil_03/leis/l6404consol.htm
  - Lei nº 12.973/2014, art. 32 (perda por redução ao valor recuperável) | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2014/lei/l12973.htm
checagem:
  - Os fluxos de caixa, a taxa de desconto e os demais valores do exemplo são ilustrativos
  - "O texto descreve a regra fiscal de forma geral: a perda é adicionada no e-Lalur quando reconhecida e computada na realização do bem (depreciação, alienação ou baixa); conferir os detalhes de controle na IN RFB nº 1.700/2017"
---

Uma mineradora tem uma planta de beneficiamento registrada por R$ 2 milhões. O preço do minério caiu, a jazida que abastece a planta está perto do fim e a produção prevista para os próximos anos é bem menor do que a projetada na compra. O balanço continua mostrando os R$ 2 milhões. Esse número não se sustenta, e o auditor vai perguntar se a empresa fez o teste de recuperabilidade.

## O que o CPC 01 exige

O princípio é simples: **nenhum ativo pode ficar no balanço por valor maior do que aquele que a empresa consegue recuperar com ele**, seja usando, seja vendendo. A Lei nº 6.404/1976 (art. 183, § 3º) também manda a companhia analisar periodicamente a recuperação dos valores registrados no imobilizado.

O CPC 01 define:

- **Valor contábil:** custo menos depreciação acumulada e perdas já reconhecidas.
- **Valor justo líquido de despesas de venda:** quanto se obteria vendendo o ativo numa transação normal, menos os custos de venda.
- **Valor em uso:** o valor presente dos fluxos de caixa futuros que o ativo deve gerar.
- **Valor recuperável:** o **maior** entre o valor justo líquido e o valor em uso.

Se o valor contábil for maior que o recuperável, a diferença é uma **perda por redução ao valor recuperável**, reconhecida no resultado.

## Quando o teste é obrigatório

Para o imobilizado, o teste não precisa ser feito todo ano de forma completa. Ele é obrigatório quando houver **indicação** de que o ativo pode ter perdido valor. Os indícios mais comuns:

| Fontes externas | Fontes internas |
|---|---|
| Queda relevante do preço de mercado do bem ou do produto | Obsolescência ou dano físico |
| Mudanças adversas no mercado, na tecnologia ou na regulação | Planos de descontinuar ou reestruturar a operação |
| Aumento das taxas de juros que afeta a taxa de desconto | Desempenho econômico pior que o esperado |
| Valor de mercado da empresa abaixo do patrimônio líquido | Bem ocioso ou com previsão de venda antecipada |

A empresa precisa avaliar, em cada data de balanço, se algum desses indícios existe, e documentar a avaliação, mesmo quando conclui que não há.

## Unidade geradora de caixa

Raramente uma máquina isolada gera caixa sozinha. Por isso o CPC 01 trabalha com a **unidade geradora de caixa**: o menor grupo de ativos que gera entradas de caixa em grande parte independentes. Uma linha de produção inteira, uma planta ou uma mina costumam ser a unidade. O teste compara o valor contábil do grupo com o valor recuperável do grupo.

## Exemplo ilustrativo

A planta de beneficiamento do início tem valor contábil de R$ 2.000.000. A empresa estima:

- valor justo líquido de despesas de venda (venda dos equipamentos no mercado): R$ 1.400.000;
- fluxo de caixa líquido de R$ 400.000 por ano, por cinco anos, até o esgotamento da jazida;
- taxa de desconto de 10% ao ano.

**Cálculo do valor em uso:**

| Ano | Fluxo de caixa | Fator de desconto (10%) | Valor presente |
|---|---|---|---|
| 1 | R$ 400.000 | 0,9091 | R$ 363.636,36 |
| 2 | R$ 400.000 | 0,8264 | R$ 330.578,51 |
| 3 | R$ 400.000 | 0,7513 | R$ 300.525,92 |
| 4 | R$ 400.000 | 0,6830 | R$ 273.205,38 |
| 5 | R$ 400.000 | 0,6209 | R$ 248.368,53 |
| **Total** | | | **R$ 1.516.314,71** |

O total foi calculado sem arredondar as parcelas; a soma das linhas arredondadas difere em um centavo.

**Teste:**

| Item | Valor |
|---|---|
| Valor justo líquido de despesas de venda | R$ 1.400.000,00 |
| Valor em uso | R$ 1.516.314,71 |
| Valor recuperável (o maior dos dois) | R$ 1.516.314,71 |
| Valor contábil | R$ 2.000.000,00 |
| **Perda a reconhecer** | **R$ 483.685,29** |

A partir daí, a depreciação passa a ser calculada sobre o novo valor contábil, de R$ 1.516.314,71, pela vida útil remanescente.

## O efeito fiscal: perda reconhecida não é perda dedutível

Para o IRPJ e a CSLL, a regra está na Lei nº 12.973/2014 (art. 32). A perda por redução ao valor recuperável **não é dedutível quando reconhecida**. Ela é adicionada no e-Lalur no período do reconhecimento e controlada na parte B. A dedução acontece quando o bem é realizado: à medida que é depreciado, ou quando é vendido ou baixado.

No exemplo, a empresa adiciona R$ 483.685,29 no ano da perda. Nos anos seguintes, a depreciação contábil fica menor do que seria sem a perda, e a diferença volta via exclusão, até que o controle seja zerado. Se a planta for vendida ou sucateada, o saldo remanescente é considerado no cálculo do ganho ou perda de capital.

## Reversão

Se, em período posterior, os indícios desaparecerem (o preço do minério voltou, por exemplo), o CPC 01 permite reverter a perda do imobilizado, limitada ao valor contábil que o bem teria se a perda nunca tivesse sido reconhecida. A reversão também tem tratamento próprio no e-Lalur, coerente com a adição feita antes.

## Relação com o inventário

O teste parte de uma base patrimonial confiável. Se o imobilizado tem bens fantasmas ou agrupamentos genéricos, o valor contábil da unidade está errado antes mesmo do cálculo. Por isso o teste costuma vir depois de um [inventário e conciliação do imobilizado](/inventario-ativo-imobilizado-conciliacao-ciap/).

## O que fazer agora

1. Faça e documente, no fechamento do exercício, a análise de indícios de perda para cada unidade geradora de caixa.
2. Se houver indício, defina a unidade e reúna as projeções de fluxo de caixa aprovadas pela administração.
3. Calcule o valor em uso e o valor justo líquido e compare com o valor contábil.
4. Se houver perda, registre a adição no e-Lalur e abra o controle na parte B.
5. Ajuste a depreciação dos períodos seguintes ao novo valor contábil.
