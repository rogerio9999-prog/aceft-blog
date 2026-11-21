---
titulo: "Como identificar produtos monofásicos de PIS e COFINS pela NCM, sem depender de listas prontas"
resumo: Listas de produtos monofásicos circulam pela internet, mas envelhecem e erram exceções. Veja o método para conferir cada NCM direto na lei, com exemplos de posições e das exceções que mais confundem.
data: 2026-11-20
categoria: PIS e COFINS
tags: [monofásico, NCM, PIS, COFINS, TIPI, cadastro de produtos]
fontes:
  - Lei nº 10.637/2002, art. 2º, § 1º (leis com alíquotas concentradas) | https://www.planalto.gov.br/ccivil_03/leis/2002/l10637.htm
  - Lei nº 10.147/2000, art. 1º (farmacêuticos, perfumaria, toucador e higiene pessoal) | https://www.planalto.gov.br/ccivil_03/leis/l10147.htm
  - Lei nº 10.485/2002, arts. 1º e 3º e Anexos I e II (máquinas, veículos e autopeças) | https://www.planalto.gov.br/ccivil_03/leis/2002/l10485.htm
  - Receita Federal, Tabela de Incidência do IPI (TIPI) | https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/legislacao/documentos-e-arquivos/tipi.pdf
checagem:
  - Os códigos citados como exemplo foram conferidos no texto compilado da Lei nº 10.147/2000 e da Lei nº 10.485/2002 no Planalto; confirmar se não houve alteração posterior
  - Detalhe menor, confirmar se o endereço do arquivo da TIPI no site da Receita continua o mesmo
  - Os percentuais do exemplo são ilustrativos
---

"Esse produto é monofásico?" A pergunta aparece toda semana no fiscal de distribuidoras, farmácias e lojas de autopeças. A resposta mais comum é buscar uma lista na internet. O problema é que essas listas não dizem de qual data são, ignoram exceções dentro de uma mesma posição e, às vezes, misturam o monofásico de PIS e COFINS com a substituição tributária do ICMS. A única fonte segura é a lei, lida a partir da NCM correta.

## Primeiro passo: a NCM precisa estar certa

Todas as leis do monofásico identificam os produtos pelo código da NCM (Nomenclatura Comum do Mercosul), que é a mesma base da TIPI, a tabela do IPI. Se o cadastro do produto no ERP tem a NCM errada, qualquer conferência posterior sai errada.

Vale lembrar a estrutura do código de oito dígitos:

| Dígitos | Nível | Exemplo de leitura |
|---|---|---|
| 2 primeiros | Capítulo | 30 (produtos farmacêuticos) |
| 4 primeiros | Posição | 30.04 |
| 6 primeiros | Subposição | 3004.90 |
| 7 primeiros | Item | 3004.90.4 |
| 8 dígitos | Subitem | 3004.90.46 |

Quando a lei cita uma **posição** (quatro dígitos), alcança todos os códigos abaixo dela, salvo exceção expressa. Quando cita um **código** completo, alcança só aquele. A diferença parece detalhe, mas decide o enquadramento.

## Segundo passo: ir à lei certa

A Lei nº 10.637/2002, no art. 2º, § 1º, relaciona as leis que fixam alíquotas concentradas para fabricantes e importadores. As principais são:

- **Lei nº 9.718/1998:** gasolinas, diesel, GLP, querosene e álcool.
- **Lei nº 10.147/2000:** produtos farmacêuticos, de perfumaria, de toucador e de higiene pessoal.
- **Lei nº 10.485/2002:** máquinas e veículos (art. 1º), autopeças (Anexos I e II) e pneus e câmaras de ar.
- **Lei nº 10.560/2002:** querosene de aviação.
- As leis que tratam de bebidas frias, também citadas no mesmo parágrafo.

Use sempre o **texto compilado** do Planalto, que mostra as redações sucessivas. Muitas dessas leis foram alteradas várias vezes, e a redação vigente costuma ser a última de cada dispositivo.

## Terceiro passo: ler as exceções

As exceções são onde as listas prontas mais erram. Dois exemplos do texto da Lei nº 10.147/2000:

- a lei alcança as posições 30.03 e 30.04 (medicamentos), **exceto** os códigos 3003.90.56 e 3004.90.46;
- alcança as posições 33.03 a 33.07 (perfumaria e toucador), **exceto** a posição 33.06 (preparações para higiene bucal ou dentária);
- alcança o código 3401.11.90 (sabões de toucador), **exceto** o "Ex 01" desse código.

Um creme dental, portanto, não entra no monofásico da Lei nº 10.147/2000 só por estar "perto" dos cosméticos na tabela. E um "Ex" da TIPI (um destaque criado dentro de um código) pode tirar um produto específico da regra.

Na Lei nº 10.485/2002, o art. 1º alcança veículos e máquinas de posições como 84.29 e 87.01 a 87.06, entre outras, e as autopeças estão nos Anexos I e II, que listam códigos um a um, alguns com a condição de serem destinados a determinados veículos.

## Quarto passo: conferir a versão da TIPI

As leis citam códigos da TIPI vigente na época em que foram escritas. Quando a NCM muda (o que acontece a cada atualização do Sistema Harmonizado), o código do produto pode mudar sem que a lei seja reescrita. Nesse caso, é preciso fazer a correlação entre a tabela antiga e a atual. Esse é um dos motivos pelos quais um cadastro antigo, nunca revisado, gera erros. O tema de saneamento de cadastro está no post sobre [saneamento do cadastro de produtos no ERP](/saneamento-cadastro-produtos-erp-ncm/).

## Quinto passo: refletir no sistema

Identificado o produto, o cadastro precisa trazer:

- a NCM correta;
- o CST de PIS e COFINS adequado para a saída de revenda monofásica;
- no Lucro Real, a indicação de que a compra do item para revenda não gera crédito;
- no Simples Nacional, a marcação que permite segregar a receita no PGDAS-D.

## Exemplo ilustrativo

Uma distribuidora de cosméticos tem 2.000 itens ativos. Na conferência, o fiscal encontra:

| Situação | Itens | Participação na receita (ilustrativa) |
|---|---|---|
| NCM em posição monofásica, sem exceção aplicável | 1.200 | 65% |
| NCM na posição 33.06 (higiene bucal), fora do monofásico | 150 | 8% |
| NCM fora das leis do monofásico | 650 | 27% |

Se o sistema tratava todos os itens do capítulo 33 como monofásicos, a empresa deixava de pagar PIS e COFINS sobre os 8% de receita de higiene bucal, o que gera passivo. Se não tratava nenhum, pagava sobre 65% da receita sem necessidade, o que gera crédito a recuperar. A mesma conferência pode apontar as duas coisas ao mesmo tempo.

## Erros que se repetem

- Confundir monofásico de PIS e COFINS com substituição tributária de ICMS. São listas diferentes, com regras diferentes.
- Usar a descrição comercial do produto em vez da NCM.
- Aplicar a posição inteira quando a lei cita apenas um código.
- Ignorar que, a partir de 2027, PIS e COFINS dão lugar à CBS, com regras próprias. A conferência continua útil para revisar os cinco anos anteriores.

Para entender a lógica do regime, veja [o que é a tributação monofásica](/pis-cofins-monofasico-o-que-e/).

## O que fazer agora

1. Exporte o cadastro de produtos com NCM, descrição e CST de PIS e COFINS.
2. Agrupe por posição (quatro primeiros dígitos) para reduzir o trabalho de conferência.
3. Abra o texto compilado de cada lei do monofásico e marque as posições, os códigos e as exceções.
4. Confira as NCMs duvidosas na TIPI vigente, inclusive os "Ex".
5. Corrija o cadastro e só então calcule eventuais diferenças do passado.
