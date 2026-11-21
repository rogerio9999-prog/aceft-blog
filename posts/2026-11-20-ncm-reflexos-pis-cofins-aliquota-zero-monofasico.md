---
titulo: "NCM e PIS/COFINS: como o código do produto define monofásico, alíquota zero e direito a crédito"
resumo: Monofásico, alíquota zero e vedação de crédito no PIS e na COFINS são definidos, em muitos casos, pelo código NCM. Veja as leis que usam a NCM, os erros mais comuns e um exemplo ilustrativo de receita tributada sem necessidade.
data: 2026-11-20
categoria: Classificação Fiscal
tags: [PIS/COFINS, NCM, monofásico, alíquota zero, crédito de PIS e COFINS]
fontes:
  - Lei nº 10.147/2000 (medicamentos e produtos de perfumaria e higiene) | https://www.planalto.gov.br/ccivil_03/leis/l10147.htm
  - Lei nº 10.485/2002 (máquinas, veículos e autopeças) | https://www.planalto.gov.br/ccivil_03/leis/2002/l10485.htm
  - Lei nº 10.925/2004, art. 1º (alíquota zero de insumos agropecuários e outros) | https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2004/lei/l10.925.htm
  - Lei nº 10.833/2003, art. 3º (créditos e vedações da COFINS não cumulativa) | https://www.planalto.gov.br/ccivil_03/leis/2003/l10.833.htm
  - Lei Complementar nº 214/2025, art. 381 (crédito presumido de CBS sobre estoque) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm
checagem:
  - Valores e alíquotas do exemplo são ilustrativos (alíquotas gerais de 1,65% e 7,6% do regime não cumulativo)
  - As listas de códigos das Leis nº 10.147/2000 e 10.485/2002 foram alteradas várias vezes; o texto não reproduz as listas e orienta a conferir a redação vigente
  - Regras de segregação no Simples Nacional não foram detalhadas neste post
---

Um distribuidor no Lucro Real revisa a apuração e descobre que, há anos, tributa pela alíquota cheia de PIS e COFINS a revenda de produtos que têm alíquota zero na revenda. Outro, no sentido oposto, trata como monofásico um item que só parece com os da lista, mas tem outra NCM, e deixa de recolher o que devia. Nos dois casos a causa está no cadastro: a tributação do PIS e da COFINS foi parametrizada a partir de um código errado, ou de um código certo lido sem a lei ao lado.

## Por que a NCM pesa tanto no PIS e na COFINS

O PIS e a COFINS incidem sobre a receita, não sobre o produto. Mas várias leis criam tratamentos diferentes para determinados produtos, e a forma de identificar esses produtos é o código da TIPI, que é a NCM. Os principais casos:

| Regime | Lei | Como a NCM entra |
|---|---|---|
| Monofásico de medicamentos e perfumaria, toucador e higiene | Lei nº 10.147/2000 | Lista posições e códigos dos Capítulos 30, 33 e outros; o industrial ou importador recolhe com alíquota concentrada e o revendedor tem alíquota zero (art. 2º) |
| Monofásico de máquinas, veículos e autopeças | Lei nº 10.485/2002 | Arts. 1º e 3º citam códigos dos Capítulos 84 e 87 e os Anexos I e II de autopeças |
| Alíquota zero de insumos agropecuários e outros | Lei nº 10.925/2004, art. 1º | Adubos do Capítulo 31, defensivos da posição 38.08, corretivos de solo do Capítulo 25 e outros códigos |
| Combustíveis e bebidas frias | Legislação própria de cada segmento | Também identificados por código |

As listas dessas leis mudaram muitas vezes ao longo dos anos, com inclusões, exclusões e "exceto" em códigos específicos. A conferência deve ser feita na redação vigente de cada lei, código a código, e não por listas prontas de terceiros. O post sobre [como identificar produtos monofásicos pela NCM](/produtos-monofasicos-como-identificar-ncm/) mostra o método.

## O detalhe que mais derruba: posição, código e "exceto"

As leis usam níveis diferentes da NCM. Algumas citam a **posição** inteira (quatro dígitos), outras um **código** de oito dígitos, outras uma posição com exceções. A Lei nº 10.147/2000, por exemplo, cita posições do Capítulo 30 com a exclusão expressa de códigos específicos. Quem lê só os quatro primeiros dígitos inclui produtos que a lei excluiu.

Também é comum a lei condicionar o tratamento à destinação. Na Lei nº 10.485/2002, as autopeças têm alíquotas diferentes conforme sejam vendidas para fabricante de veículos ou para o varejo. A NCM é condição necessária, mas não suficiente.

## O outro lado: o crédito de quem compra

Para empresas no regime não cumulativo, a NCM também afeta o crédito. A Lei nº 10.833/2003 (art. 3º) e a Lei nº 10.637/2002 vedam, em regra:

- o crédito na aquisição, para revenda, de produtos sujeitos à incidência monofásica;
- o crédito na aquisição de bens ou serviços não sujeitos ao pagamento da contribuição (art. 3º, § 2º, II), com as ressalvas que a própria lei faz.

Assim, um insumo comprado com alíquota zero, em regra, não dá crédito. Se o fornecedor classificou o insumo errado e tributou, o comprador pode ter tomado crédito sobre algo que não devia ter sido tributado. Se o fornecedor deixou de tributar o que devia, o comprador perde crédito. A conferência da NCM das compras relevantes faz parte da revisão de PIS e COFINS, junto com o [conceito de insumo](/conceito-de-insumo-pis-cofins-essencialidade-relevancia/).

## Exemplo ilustrativo

Um atacadista no Lucro Real revende, por mês, R$ 200.000,00 de produtos que estão na lista monofásica da Lei nº 10.147/2000 e, portanto, têm alíquota zero na revenda. Por erro de parametrização, o ERP tributa essa receita pelas alíquotas gerais do regime não cumulativo.

| Item | Cálculo | Valor |
|---|---|---|
| PIS indevido no mês | R$ 200.000,00 × 1,65% | R$ 3.300,00 |
| COFINS indevida no mês | R$ 200.000,00 × 7,6% | R$ 15.200,00 |
| Total indevido no mês | | R$ 18.500,00 |
| Total indevido em 12 meses | | R$ 222.000,00 |

O valor pago a maior pode ser recuperado dentro do prazo de cinco anos, por retificação da EFD-Contribuições e das declarações e pedido de restituição ou compensação. Mas a revisão precisa olhar também os créditos: se a empresa se creditou na compra desses mesmos produtos, esse crédito era vedado e o ajuste reduz o valor a recuperar. O resultado líquido só aparece com a apuração refeita.

## NCM e a transição para a CBS

A Lei Complementar nº 214/2025 trata expressamente dos produtos monofásicos na transição. O art. 381 permite ao contribuinte do regime regular da CBS apropriar crédito presumido sobre o estoque existente em 1º de janeiro de 2027 de bens que foram adquiridos sob incidência monofásica (entre outros, os da Lei nº 10.147/2000 e da Lei nº 10.485/2002), observadas as condições da lei e o ato do Poder Executivo sobre o inventário. Para usar esse crédito, a empresa precisa identificar, pelo código, quais itens do estoque se enquadram. Cadastro de NCM errado em 2026 vira crédito perdido ou glosado em 2027.

Para o IBS e a CBS, a NCM continua decisiva: as reduções de alíquota da LC 214/2025 (cesta básica, insumos agropecuários, dispositivos médicos, medicamentos) são definidas por códigos NCM/SH nos anexos da lei.

## O que fazer agora

1. Liste os produtos parametrizados no ERP como monofásicos, alíquota zero ou suspensão de PIS/COFINS.
2. Confira cada código na redação vigente da lei correspondente, inclusive exceções e condições de destinação.
3. Faça o caminho inverso: procure, entre os itens tributados normalmente, NCMs que aparecem nas listas.
4. Cruze com as compras: créditos tomados sobre itens monofásicos ou com alíquota zero.
5. Quantifique o efeito dos últimos cinco anos e prepare o inventário dos itens monofásicos que estarão em estoque em 1º de janeiro de 2027.
