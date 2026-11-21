---
titulo: "Retificação do SPED na recuperação de créditos: a ordem certa entre EFD, DCTFWeb, ECF e PER/DCOMP"
resumo: Recuperar crédito exige retificar várias obrigações, e a ordem importa. Veja a sequência que mantém os arquivos coerentes entre si, os limites para retificar e os erros que derrubam a compensação.
data: 2026-11-20
categoria: Recuperação de Créditos
tags: [retificação, SPED, EFD-Contribuições, DCTFWeb, ECF, PER/DCOMP]
fontes:
  - Guia Prático da EFD-Contribuições, versão 1.35, Seção 9 (retificação) | http://sped.rfb.gov.br/estatico/AD/06A0F5C4E4CC8CA16035EB891A3AE31EA79708/Guia_Pratico_EFD_Contribuicoes_Versao_1_35%20-%2018_06_2021.pdf
  - Receita Federal, DCTF substituída pela DCTFWeb para fatos geradores a partir de 2025 | https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2024/dezembro/publicada-instrucao-normativa-que-institui-o-modulo-de-inclusao-de-tributos-2013-mit-na-dctfweb-e-substitui-a-dctf
  - Lei nº 9.430/1996, art. 74 (compensação) | https://www.planalto.gov.br/ccivil_03/leis/l9430.htm
  - CONFAZ, Ajuste SINIEF nº 2/2009 (EFD ICMS/IPI) | https://www.confaz.fazenda.gov.br/legislacao/ajustes/2009/aj_002_09
checagem:
  - As regras de retificação da EFD ICMS/IPI fora do prazo (autorização da Secretaria de Fazenda) foram descritas de forma geral, sem citar cláusula nem prazo; conferir o Ajuste SINIEF nº 2/2009 e a regra do estado
  - Não foram citados prazos de retificação da ECD e da ECF; conferir os manuais vigentes
  - O valor e a alíquota de IRPJ e CSLL do exemplo são ilustrativos
---

Uma revisão encontrou crédito de PIS e COFINS dos últimos três anos. A equipe transmite os PER/DCOMP na semana seguinte. Meses depois, as compensações começam a ser não homologadas com a justificativa de "crédito não confirmado". O crédito existia. O problema é que as obrigações acessórias ainda contavam outra história.

## Por que a ordem importa

A Receita cruza as informações das declarações de forma automática. Uma compensação é analisada à luz do que a empresa declarou na escrituração, na declaração de débitos e na contabilidade. Se o crédito aparece no PER/DCOMP mas não aparece na EFD-Contribuições, ou se o pagamento usado como crédito ainda está vinculado a um débito na DCTFWeb, o sistema aponta inconsistência.

Retificar na ordem certa faz com que, no momento da compensação, todas as fontes de dados da Receita já mostrem o mesmo número.

## A sequência recomendada

| Ordem | Obrigação | O que muda |
|---|---|---|
| 1 | Documentos e cadastros | Corrige NCM, CST e regras fiscais no ERP para o erro não continuar |
| 2 | EFD ICMS/IPI | Quando o achado afeta ICMS ou IPI, ou quando a base de PIS e COFINS depende dele |
| 3 | EFD-Contribuições | Inclui créditos, corrige bases e saldos (registros 1100 e 1500) |
| 4 | DCTF (até 2024) ou DCTFWeb (a partir de 2025) | Ajusta o débito declarado e libera o pagamento como crédito |
| 5 | ECD, se a contabilidade mudar | Registra o crédito e o efeito no resultado |
| 6 | ECF | Reflete o efeito no IRPJ e na CSLL |
| 7 | PER/DCOMP | Pede restituição, ressarcimento ou compensa |

Nem todo caso passa por todas as etapas. Um crédito de insumo de PIS e COFINS não escriturado, por exemplo, exige a EFD-Contribuições e, se reduzir o valor a pagar daquele mês, a declaração de débitos. Um pagamento indevido de IRPJ exige a ECF e a declaração de débitos.

## Os limites da retificação

O Guia Prático da EFD-Contribuições registra que a retificação pode ser feita em até **cinco anos** contados do primeiro dia do exercício seguinte ao da escrituração, mas **não produz efeitos** quando tem por objeto, entre outros casos:

- reduzir débitos já enviados à PGFN para inscrição em dívida ativa;
- alterar débitos em relação aos quais a empresa já foi intimada do início de procedimento fiscal;
- alterar créditos que estejam em exame em fiscalização ou em pedido de ressarcimento ou declaração de compensação.

O mesmo guia diz que, se a EFD-Contribuições retificadora alterar valores informados na declaração de débitos, a declaração também deve ser retificada.

Na EFD ICMS/IPI, a retificação segue o Ajuste SINIEF nº 2/2009 e as regras de cada estado. Fora de certos prazos, ela depende de autorização da Secretaria de Fazenda. Em Minas Gerais, como em outros estados, vale conferir o procedimento antes de transmitir.

## Créditos extemporâneos de PIS e COFINS

O Guia Prático orienta que, desde os períodos de agosto de 2013, o crédito de um período anterior seja lançado pela **retificação do próprio período** a que se refere, e não mais em registros de crédito extemporâneo. O saldo dos meses seguintes é ajustado nos registros 1100 e 1500. Em uma revisão de cinco anos, isso significa retificar em cadeia, mês a mês, para que o saldo de crédito transportado faça sentido.

## Exemplo ilustrativo

Uma indústria do Lucro Real descobre R$ 100.000 de crédito de PIS e COFINS não aproveitado em março de 2024. Naquele mês, ela havia pago R$ 150.000 das contribuições.

1. Retifica a EFD-Contribuições de março de 2024, incluindo o crédito. O valor devido cai para R$ 50.000.
2. Retifica a DCTF de março de 2024 (período anterior a 2025), reduzindo o débito para R$ 50.000. O DARF de R$ 150.000 passa a ter R$ 100.000 de pagamento a maior.
3. Avalia o efeito no IRPJ e na CSLL: o crédito reduz o custo daquele ano. Com alíquota combinada ilustrativa de 34%, o lucro tributável aumenta e há R$ 34.000 de IRPJ e CSLL a ajustar na ECF, conforme o regime de reconhecimento adotado. O tema está em [tributação do crédito recuperado](/tributacao-credito-recuperado-irpj-csll/).
4. Só então transmite o PER/DCOMP com o crédito do pagamento a maior.

Se a empresa inverter os passos 2 e 4, a compensação nasce com um crédito que, para os sistemas da Receita, não existe.

## Erros que derrubam a compensação

- Transmitir PER/DCOMP antes de retificar a declaração de débitos.
- Retificar só o mês do crédito e esquecer de ajustar o saldo transportado nos meses seguintes.
- Retificar depois de receber intimação de início de fiscalização, quando a retificação já não produz efeitos.
- Ignorar o efeito no IRPJ e na CSLL.

Para o passo final, veja [PER/DCOMP passo a passo](/per-dcomp-compensacao-passo-a-passo/).

## O que fazer agora

1. Monte um cronograma por período: quais obrigações cada achado exige retificar.
2. Verifique se há fiscalização em curso ou débito inscrito em dívida ativa nos períodos envolvidos.
3. Confira, no seu estado, a regra para retificar a EFD ICMS/IPI fora do prazo.
4. Retifique em cadeia os saldos de crédito da EFD-Contribuições, do mês do achado até o mês atual.
5. Só transmita o PER/DCOMP depois de conferir que a declaração de débitos já reflete o pagamento a maior.
