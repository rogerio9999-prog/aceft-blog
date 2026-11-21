---
titulo: "Vida útil contábil x taxa de depreciação fiscal: por que os dois números são diferentes e como controlar no e-Lalur"
resumo: A contabilidade deprecia pela vida útil real do bem; o IRPJ aceita as taxas da Receita. Veja por que os dois convivem, como a diferença é excluída e depois adicionada no e-Lalur, com exemplo de uma máquina ao longo de 15 anos.
data: 2026-11-20
categoria: Ativo Imobilizado
tags: [depreciação, vida útil, IN RFB 1.700/2017, e-Lalur, CPC 27, Lucro Real]
fontes:
  - CPC 27: Ativo Imobilizado (vida útil, valor residual e revisão anual) | https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=58
  - Instrução Normativa RFB nº 1.700/2017, Anexo III (taxas de depreciação) | http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?idAto=81268
  - Lei nº 4.506/1964, art. 57, §§ 15 e 16, incluídos pela Lei nº 12.973/2014 (exclusão e posterior adição da diferença) | https://www.planalto.gov.br/ccivil_03/leis/l4506.htm
  - Decreto nº 9.580/2018 (Regulamento do Imposto de Renda), art. 320 (vida útil admissível) | https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/decreto/d9580.htm
checagem:
  - Os valores do exemplo são ilustrativos
  - "As taxas citadas (10% ao ano para máquinas em geral e 4% para edificações) são as usuais do Anexo III da IN RFB nº 1.700/2017; a taxa de cada bem depende da sua classificação no anexo e deve ser conferida caso a caso"
  - "Aplicação da exclusão dos §§ 15 e 16 do art. 57 da Lei nº 4.506/1964 à base da CSLL: o texto fala do lucro real e recomenda conferir o tratamento da CSLL na IN RFB nº 1.700/2017"
  - Confirmar o link da Lei nº 4.506/1964 no Planalto (detalhe menor)
  - Confirmar no art. 320 do RIR/2018 a forma de prova exigida para usar taxa diferente da fixada pela Receita (o texto fala em laudo de entidade oficial de pesquisa, de forma geral)
---

O auditor pede para revisar a vida útil das máquinas. A equipe fiscal responde que a vida útil "é a da Receita": 10 anos para máquinas, 25 para prédios, 5 para veículos. Essa confusão é antiga e ainda comum. Ela faz a contabilidade depreciar por uma tabela fiscal que não reflete o uso real dos bens, ou faz o fiscal perder a dedução mais rápida que a lei permite. Os dois números existem por razões diferentes e devem ser controlados separadamente.

## Dois objetivos, duas regras

**Na contabilidade**, o CPC 27 exige que a depreciação reflita o padrão de consumo dos benefícios do bem. A empresa estima a **vida útil** (quanto tempo, ou quantas unidades de produção, ela espera usar o bem) e o **valor residual** (quanto espera obter ao final), e revisa as duas estimativas pelo menos ao fim de cada exercício. Uma máquina usada em três turnos numa mineração pode durar bem menos que a mesma máquina num turno numa indústria leve.

**No imposto de renda**, a depreciação dedutível segue as taxas publicadas pela Receita Federal. Hoje elas estão no Anexo III da Instrução Normativa RFB nº 1.700/2017, organizadas pela classificação do bem. O Regulamento do Imposto de Renda (art. 320) prevê que a empresa pode usar taxa diferente se provar sua adequação, na forma que o regulamento exige (em regra, por laudo de entidade oficial de pesquisa).

| Aspecto | Contabilidade (CPC 27) | Imposto de renda |
|---|---|---|
| Base da taxa | Vida útil estimada pela empresa | Taxas do Anexo III da IN RFB 1.700/2017 |
| Valor residual | Considerado | Não reduz a base da taxa fiscal |
| Revisão | Pelo menos anual | Taxa fixa, salvo prova de outra |
| Onde aparece | Balanço e resultado | e-Lalur e ECF |

## Como a diferença é tratada

Desde a Lei nº 12.973/2014, a regra é clara. O art. 57 da Lei nº 4.506/1964 passou a prever que, se a depreciação registrada na contabilidade for **menor** que a calculada pelas taxas fiscais, a diferença **pode ser excluída** do lucro líquido na apuração do lucro real (§ 15). Quando o total depreciado para fins fiscais atinge o custo do bem, a depreciação que continuar sendo registrada na contabilidade passa a ser **adicionada** (§ 16).

Ou seja: a empresa pode deduzir no ritmo fiscal, mesmo depreciando mais devagar na contabilidade. Mas o total deduzido ao longo da vida do bem nunca passa do custo de aquisição.

Se a depreciação contábil for **maior** que a fiscal, o excesso é adicionado no e-Lalur e excluído depois, à medida que a depreciação fiscal alcança o valor.

## Exemplo ilustrativo

Uma indústria compra uma máquina por R$ 600.000. A engenharia estima vida útil de 15 anos e valor residual de R$ 60.000. A taxa fiscal do bem é de 10% ao ano.

| Item | Contabilidade | Fiscal |
|---|---|---|
| Base depreciável | R$ 540.000 (custo menos residual) | R$ 600.000 (custo) |
| Prazo | 15 anos | 10 anos |
| Depreciação anual | R$ 36.000 | R$ 60.000 |

O efeito no e-Lalur ao longo do tempo:

| Período | Depreciação contábil anual | Depreciação fiscal anual | Ajuste no e-Lalur por ano |
|---|---|---|---|
| Anos 1 a 10 | R$ 36.000 | R$ 60.000 | Exclusão de R$ 24.000 |
| Anos 11 a 15 | R$ 36.000 | R$ 0 | Adição de R$ 36.000 |
| **Acumulado** | **R$ 540.000** | **R$ 600.000** | Exclusões de R$ 240.000, adições de R$ 180.000 |

Sobram R$ 60.000 de diferença, que é exatamente o valor residual. Esse valor continua no balanço (valor contábil de R$ 60.000) mas já foi todo deduzido no fiscal (valor fiscal zero). Quando a máquina for vendida, o ganho de capital fiscal será maior que o contábil nesse mesmo valor. A conta fecha.

O benefício é financeiro: a empresa antecipa R$ 24.000 por ano de dedução nos primeiros dez anos e devolve depois. Para quem paga IRPJ e CSLL a 34%, é capital de giro.

## Erros comuns

- **Usar a taxa fiscal na contabilidade.** O balanço passa a refletir uma tabela, não a realidade. Bens totalmente depreciados continuam operando por anos, e o imobilizado some do balanço.
- **Não fazer a exclusão.** A empresa adota vida útil longa na contabilidade e deixa de excluir a diferença fiscal. Perde a antecipação da dedução.
- **Fazer a exclusão sem controle por bem.** O e-Lalur exige controle na parte B. Sem saber, bem a bem, quanto já foi excluído, a empresa não sabe quando começar a adicionar.
- **Esquecer a baixa.** Na venda ou sucata, o saldo de exclusões do bem precisa ser revertido no cálculo do ganho ou perda de capital. Veja [baixa do ativo imobilizado](/baixa-ativo-imobilizado-venda-sucata/).

## A revisão da vida útil

Revisar a vida útil não é formalidade. Se a revisão concluir que as máquinas duram mais do que se estimava, a depreciação contábil anual cai e o lucro contábil sobe, sem efeito no imposto, desde que o controle fiscal esteja em dia. Se concluir que duram menos, a depreciação contábil sobe, e o excesso sobre a fiscal é adicionado. A revisão é contábil; a dedução fiscal segue a sua própria regra.

Para bens usados em mais de um turno, a legislação fiscal admite coeficientes de aceleração, tema de [depreciação acelerada](/depreciacao-acelerada-incentivada/).

## O que fazer agora

1. Compare a política de vida útil da contabilidade com as taxas do Anexo III para as principais classes de bens.
2. Se as duas forem idênticas, avalie se a contabilidade está usando a tabela fiscal sem estudo de vida útil.
3. Verifique se as diferenças estão registradas na parte B do e-Lalur, bem a bem.
4. Identifique bens que já atingiram o custo no fiscal e confira se a depreciação contábil está sendo adicionada.
5. Documente a revisão anual de vida útil e valor residual, com participação da engenharia ou da manutenção.
