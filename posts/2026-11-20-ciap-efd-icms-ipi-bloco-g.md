---
titulo: "CIAP no Bloco G da EFD ICMS/IPI: como os registros funcionam e os erros que fazem perder crédito"
resumo: O crédito de ICMS do ativo imobilizado é demonstrado no Bloco G da EFD ICMS/IPI. Veja o papel dos registros 0300, 0305, G110, G125, G126, G130 e G140, um cálculo completo do G110 e os erros mais comuns.
data: 2026-11-20
categoria: Créditos de ICMS
tags: [CIAP, Bloco G, EFD ICMS/IPI, SPED Fiscal, ativo imobilizado, crédito de ICMS]
fontes:
  - Guia Prático da EFD ICMS/IPI (Bloco G e registros 0300 e 0305), portal do SPED | https://www.gov.br/sped/pt-br/assuntos/escrituracoes-digitais/efd-icms-ipi/manuais-e-documentos-tecnicos
  - Lei Complementar nº 87/1996 (Lei Kandir), art. 20, § 5º | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp87.htm
  - RICMS/MG 2023 (Decreto nº 48.589/2023), Parte Geral, art. 31, §§ 1º, 7º e 8º | https://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/ricms_2023_seco/regulamento2023_1.html
checagem:
  - A descrição dos registros segue o Guia Prático da EFD ICMS/IPI versão 3.1.8 (atualização de 31/10/2024); conferir se houve versão posterior com alteração no Bloco G
  - Valores do exemplo são ilustrativos
  - O código de ajuste usado no registro E111 para lançar o crédito do CIAP é definido por cada estado e não foi detalhado
---

O crédito de ICMS na compra de máquinas e equipamentos não entra de uma vez: é apropriado em 48 parcelas mensais, proporcionais às saídas tributadas. Esse controle, o CIAP (Controle de Crédito de ICMS do Ativo Permanente), é escriturado no Bloco G da EFD ICMS/IPI. Quando o Bloco G está mal preenchido, a empresa perde parcelas sem perceber ou se credita de bens que já saíram da fábrica. E o arquivo deixa o erro visível para qualquer cruzamento do fisco.

## A regra por trás do Bloco G

A Lei Complementar nº 87/1996, art. 20, § 5º, define a apropriação:

- 1/48 por mês do ICMS do bem;
- multiplicado pela relação entre as **saídas tributadas** (com as exportações equiparadas) e o **total de saídas** do período;
- com cancelamento do saldo restante ao fim do 48º mês;
- e sem apropriação das frações restantes se o bem for alienado antes desse prazo.

Em Minas Gerais, o RICMS/2023 detalha a regra no art. 31, § 1º, e determina expressamente, no inciso VI, a escrituração do crédito no Bloco G da EFD.

## Os registros, um por um

Segundo o Guia Prático da EFD ICMS/IPI:

| Registro | Função |
|---|---|
| 0300 | Cadastro de cada bem ou componente, com código individual, descrição precisa, conta contábil e número total de parcelas (NR_PARC) |
| 0305 | Utilização do bem: centro de custo, função na atividade e vida útil estimada em meses |
| G001 | Abertura do bloco, indicando se há dados |
| G110 | Resumo do período: saldo inicial, soma das parcelas, saídas tributadas e totais, índice e crédito a apropriar |
| G125 | Movimentação de cada bem no período, com o tipo de movimento e a parcela |
| G126 | Outros créditos do CIAP, de parcelas não escrituradas em períodos anteriores, quando a legislação permitir |
| G130 | Documento fiscal da entrada ou saída do bem |
| G140 | Item do documento fiscal |

### Os tipos de movimentação do G125

| Código | Significado |
|---|---|
| SI | Saldo inicial: bem que já estava no CIAP e ainda tem parcelas |
| IM | Imobilização de bem individual no período |
| IA | Imobilização em andamento: componente de bem construído pela empresa |
| CI | Conclusão de imobilização em andamento: bem resultante |
| MC | Imobilização oriunda do ativo circulante (estoque) |
| BA | Baixa pelo fim do período de apropriação |
| AT | Alienação ou transferência |
| PE | Perecimento, extravio ou deterioração |
| OT | Outras saídas do imobilizado |

Quando um bem sai do CIAP por venda, perda ou outro motivo, o guia prevê dois registros no período: um SI, representando o bem, e um AT, PE ou OT, representando a saída. Na última parcela, um SI com a parcela e um BA.

## Exemplo ilustrativo: o cálculo do G110

Uma indústria tem três bens com parcelas a apropriar no mês (valores ilustrativos):

| Bem | VL_PARC_PASS (parcela antes do índice) |
|---|---|
| Prensa hidráulica | R$ 1.200,00 |
| Compressor | R$ 850,00 |
| Empilhadeira | R$ 425,50 |
| **SOM_PARC** | **R$ 2.475,50** |

As saídas do mês foram:

- tributadas: R$ 1.350.000,00
- exportações: R$ 450.000,00
- isentas: R$ 200.000,00
- total: R$ 2.000.000,00

Campos do G110:

- VL_TRIB_EXP (tributadas + exportações) = R$ 1.800.000,00
- VL_TOTAL = R$ 2.000.000,00
- IND_PER_SAI = 1.800.000 ÷ 2.000.000 = **0,90**
- ICMS_APROP = 2.475,50 × 0,90 = **R$ 2.227,95**

Esse é o crédito do mês. Segundo o guia, ele é levado à apuração do ICMS como ajuste (registro E111), com o código definido pelo estado, salvo se a legislação exigir documento fiscal.

Repare no erro mais comum desse cálculo: deixar as exportações fora do numerador. Se a empresa usasse só as tributadas (1.350.000 ÷ 2.000.000 = 0,675), o crédito cairia para cerca de R$ 1.670,96, perda de R$ 556,99 só naquele mês.

## Erros que fazem perder crédito

1. **Bem fora do CIAP.** A máquina foi lançada no imobilizado, mas nunca entrou no 0300 e no G125. As parcelas não são apropriadas e o prazo de cinco anos para usar o crédito continua correndo.
2. **Exportações fora do índice.** O IND_PER_SAI fica menor do que deveria.
3. **Frete e DIFAL esquecidos.** O G125 tem campos próprios para o ICMS do frete (VL_IMOB_ICMS_FRT) e do diferencial de alíquotas (VL_IMOB_ICMS_DIF). Quando a legislação do estado admite esses créditos e eles não são informados, a parcela fica menor.
4. **Componentes de bem construído tratados como despesa.** Peças e materiais de uma máquina montada na própria fábrica podem ir para o CIAP como IA e CI, conforme a regra do estado.

## Erros que geram crédito indevido

1. **Bem vendido ou sucateado que continua com SI.** Sem o registro AT, PE ou OT, as parcelas seguem sendo apropriadas.
2. **Bem alheio à atividade no CIAP.** Veículo de diretoria, imóvel residencial (veja [bens alheios à atividade](/credito-icms-bens-alheios-atividade/)).
3. **Parcelas além da 48ª.** Falta do registro BA no fim do período.
4. **Função no 0305 incoerente.** Bem descrito como administrativo, com crédito integral, chama atenção num cruzamento.

## E o crédito que não foi escriturado na época?

O registro G126 existe para "outros créditos CIAP", parcelas de períodos anteriores que não foram escrituradas, quando a legislação do estado permitir. Em Minas Gerais, o RICMS/2023, art. 31, § 7º, determina que, na apropriação extemporânea de fração de crédito do ativo no Bloco G, o índice de saídas tributadas seja o do **período em que a fração deveria ter sido apropriada**, e o § 8º trata da contagem do prazo de cinco anos para essas frações. O tema geral está em [crédito extemporâneo de ICMS](/credito-extemporaneo-icms-como-lancar/).

## O que fazer agora

1. Compare a relação de bens do imobilizado adquiridos nos últimos quatro anos com o registro 0300 da EFD.
2. Confira se o IND_PER_SAI de alguns meses inclui as exportações no numerador.
3. Verifique se bens vendidos ou baixados nos últimos anos tiveram o registro de saída correspondente no G125.
4. Confira se o ICMS do frete e do DIFAL dos bens foi considerado, quando o seu estado admite.
5. Se encontrar parcelas não apropriadas, confira a regra do seu estado para o G126 antes de lançar.
