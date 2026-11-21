---
titulo: "EFD-Contribuições: os erros de escrituração que fazem a empresa perder crédito de PIS e COFINS"
resumo: Muito crédito de PIS e COFINS se perde na escrituração, e não na interpretação da lei. Veja os erros mais comuns na EFD-Contribuições, em quais registros eles aparecem e como conferir.
data: 2026-11-20
categoria: PIS e COFINS
tags: [EFD-Contribuições, SPED, PIS, COFINS, CST, créditos]
fontes:
  - Guia Prático da EFD-Contribuições, versão 1.35 (Receita Federal, SPED) | http://sped.rfb.gov.br/estatico/AD/06A0F5C4E4CC8CA16035EB891A3AE31EA79708/Guia_Pratico_EFD_Contribuicoes_Versao_1_35%20-%2018_06_2021.pdf
  - Lei nº 10.833/2003, art. 3º (créditos e vedações) | https://www.planalto.gov.br/ccivil_03/leis/2003/l10.833.htm
  - Receita Federal, substituição da DCTF pela DCTFWeb a partir de 2025 | https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2024/dezembro/receita-federal-divulga-esclarecimentos-iniciais-sobre-a-substituicao-da-dctf-a-partir-de-janeiro-de-2025
  - Receita Federal, regras para uso de créditos de PIS/Cofins na transição para a CBS (junho de 2026) | https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/junho/receita-federal-esclarece-as-regras-para-uso-de-creditos-de-pis-cofins-na-transicao-para-a-cbs
checagem:
  - Os valores do exemplo são ilustrativos
  - O Guia Prático citado é a versão 1.35 (junho de 2021); conferir no portal do SPED se há versão posterior com mudança nas regras de retificação ou nos registros citados
---

Quando se fala em crédito de PIS e COFINS, a discussão costuma girar em torno do conceito de insumo. Mas uma parte grande do crédito perdido nas empresas do Lucro Real não tem nada de polêmico: é energia elétrica, aluguel, depreciação e frete que a lei garante e que simplesmente não chegaram à EFD-Contribuições, ou chegaram com o código errado.

## Onde o crédito nasce na escrituração

Na EFD-Contribuições, o crédito é formado a partir dos documentos e operações informados nos blocos A, C, D e F, e consolidado no bloco M:

| Tipo de gasto | Onde costuma ser escriturado |
|---|---|
| Notas de serviço tomado (insumo) | A100 |
| Notas de mercadorias e insumos | Bloco C (C100 e filhos) |
| Conta de energia elétrica | C500 |
| Fretes contratados (CT-e) | D100 |
| Aluguéis e demais operações | F100 |
| Depreciação de máquinas e edificações | F120 |
| Crédito sobre o valor de aquisição do imobilizado | F130 |
| Consolidação do crédito do mês | M100 (PIS) e M500 (COFINS) |
| Controle de saldos de meses anteriores | 1100 (PIS) e 1500 (COFINS) |

Se um gasto não aparece em nenhum desses registros, para a Receita ele não gerou crédito.

## Erro 1: CST sem direito a crédito

Cada item de entrada leva um Código de Situação Tributária (CST) de PIS e de COFINS. Os códigos 50 a 56 indicam operação com direito a crédito. Um insumo escriturado com CST de "operação sem direito a crédito" (como 70 ou 98) sai do cálculo. Esse erro costuma vir do cadastro do produto ou da regra fiscal do ERP, e se repete em todas as notas daquele item.

## Erro 2: código de base de cálculo do crédito inadequado

O campo NAT_BC_CRED classifica a natureza do crédito: 02 para bens usados como insumo, 03 para serviços usados como insumo, 04 para energia, 05 e 06 para aluguéis de prédios e de máquinas, 07 para armazenagem e frete na venda, 09 e 10 para o imobilizado, 13 para outras operações, entre outros. Código errado não elimina o crédito automaticamente, mas cria inconsistência que aparece em qualquer auditoria e dificulta a defesa.

## Erro 3: os gastos "fora da nota de mercadoria"

Os créditos de energia, aluguel e depreciação dependem de registros que nem sempre são alimentados pelo ERP de forma automática:

- **Energia (C500):** a conta da distribuidora às vezes é lançada só na contabilidade.
- **Aluguel pago a pessoa jurídica (F100):** o contrato existe, a despesa está no razão, mas a operação nunca foi informada.
- **Depreciação (F120):** exige o controle do imobilizado com a parcela de cada mês. Sem um cadastro patrimonial organizado, a empresa costuma desistir do crédito. O tema conversa com o [inventário do ativo imobilizado](/inventario-ativo-imobilizado-conciliacao-ciap/).

## Erro 4: rateio de créditos comuns mal configurado

Empresa com receitas tributadas e não tributadas (exportação, alíquota zero, regime cumulativo) precisa ratear os créditos comuns. O registro 0110 indica o método (apropriação direta ou rateio proporcional pela receita bruta), e o 0111 traz a receita do mês para o rateio. Um 0110 preenchido com o método errado, ou um 0111 com receita incompleta, distorce o crédito do mês inteiro.

## Erro 5: ICMS dentro da base do crédito

O ICMS que incidiu na aquisição não gera crédito de PIS e COFINS (art. 3º, § 2º, III, da Lei nº 10.833/2003 e da Lei nº 10.637/2002). Escrituração que mantém o ICMS na base infla o crédito e cria risco de glosa. É um erro no sentido contrário, mas também aparece em revisões.

## Erro 6: saldo de crédito que some de um mês para o outro

O crédito não usado num mês pode ser aproveitado nos seguintes (art. 3º, § 4º, da Lei nº 10.833/2003). Esse saldo é controlado nos registros 1100 e 1500. Quando a empresa troca de sistema ou de escritório e o saldo inicial não é informado, o crédito acumulado simplesmente desaparece da escrituração. A Receita informou, em junho de 2026, que identificou divergências nesses saldos em milhares de empresas e que o PER/DCOMP Web vai buscar os saldos informados na EFD-Contribuições de dezembro de 2026 para a transição para a CBS. Saldo errado em dezembro de 2026 é crédito com problema em 2027.

## Erro 7: retificar sem olhar o resto

Segundo o Guia Prático, a retificação pode ser feita em até cinco anos contados do primeiro dia do exercício seguinte ao da escrituração, mas não produz efeitos em certas situações, como créditos que já estejam em exame em procedimento fiscal ou em pedido de ressarcimento ou compensação. E, se a retificação alterar valores declarados, a declaração de débitos também precisa ser retificada: a DCTF para períodos até 2024 e a DCTFWeb para fatos geradores a partir de janeiro de 2025. A ordem dos passos está no post sobre [a ordem certa das retificações](/retificacao-sped-recuperacao-creditos/).

## Exemplo ilustrativo

Uma indústria escriturou por um ano um grupo de insumos (embalagens secundárias e materiais de laboratório usados na produção) com CST 70, por erro na regra fiscal do ERP. Esses itens somam R$ 80.000 por mês, já sem o ICMS.

| Cálculo | Valor |
|---|---|
| Base mensal | R$ 80.000,00 |
| Crédito de PIS e COFINS (9,25%) | R$ 7.400,00 |
| Em 12 meses | R$ 88.800,00 |

O crédito sempre existiu. O que faltou foi o código certo.

## O que fazer agora

1. Gere um relatório das entradas dos últimos 12 meses agrupado por CST e por NCM ou código de serviço.
2. Procure itens de produção escriturados com CST sem direito a crédito.
3. Confira se C500, D100, F100 e F120 estão sendo alimentados todos os meses.
4. Verifique o método de rateio no 0110 e a receita informada no 0111.
5. Compare o saldo final dos registros 1100 e 1500 de um mês com o saldo inicial do mês seguinte, especialmente antes de dezembro de 2026.
