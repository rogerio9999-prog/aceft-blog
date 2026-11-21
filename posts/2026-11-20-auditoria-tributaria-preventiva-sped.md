---
titulo: "Auditoria preventiva dos arquivos SPED: o que cruzar antes que o fisco cruze"
resumo: O fisco recebe EFD ICMS/IPI, EFD-Contribuições, ECD e ECF e cruza tudo automaticamente. Veja quais confrontos fazer antes, como priorizar as divergências e um exemplo de quanto uma diferença de receita pode custar.
data: 2026-11-20
categoria: Recuperação de Créditos
tags: [SPED, auditoria preventiva, EFD ICMS/IPI, EFD-Contribuições, ECD, ECF]
fontes:
  - Decreto nº 6.022/2007 (institui o Sistema Público de Escrituração Digital) | https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/decreto/d6022.htm
  - Portal do SPED, Receita Federal | http://sped.rfb.gov.br/
  - Lei nº 10.637/2002 e Lei nº 10.833/2003 (alíquotas do PIS e da COFINS não cumulativos) | https://www.planalto.gov.br/ccivil_03/leis/2003/l10.833.htm
checagem:
  - Os valores do exemplo são ilustrativos
  - O texto não cita percentuais de multa por erro ou omissão em arquivos digitais; se o revisor quiser incluí-los, conferir a legislação federal e a do estado
  - Os cruzamentos listados são práticas de revisão; o texto não afirma quais cruzamentos o fisco faz em cada estado
---

Até a década passada, uma inconsistência entre o livro fiscal e a contabilidade só aparecia se um fiscal resolvesse olhar. Hoje a empresa entrega ao fisco, todo mês ou todo ano, os mesmos números em arquivos diferentes: a EFD ICMS/IPI para o estado e para a Receita, a EFD-Contribuições para o PIS e a COFINS, a ECD (Escrituração Contábil Digital) com a contabilidade e a ECF (Escrituração Contábil Fiscal) com a apuração do IRPJ e da CSLL. Se eles não conversam entre si, o cruzamento é feito por sistema, sem ninguém pedir.

A auditoria preventiva faz esse cruzamento antes, do lado da empresa. Ela tem dois resultados possíveis, e os dois interessam: encontrar risco (débito que precisa ser corrigido por iniciativa própria) e encontrar crédito (imposto pago a mais que pode ser recuperado).

## A lógica: o mesmo fato aparece em vários arquivos

O SPED, instituído pelo Decreto nº 6.022/2007, unificou a entrega de livros e escriturações em formato digital. Uma venda de mercadoria, por exemplo, aparece:

- na nota fiscal eletrônica emitida;
- na EFD ICMS/IPI, com o débito de ICMS e de IPI;
- na EFD-Contribuições, como receita tributada ou não pelo PIS e pela COFINS;
- na ECD, como receita contábil;
- na ECF, compondo o lucro.

Se o valor ou a natureza dessa venda muda de um arquivo para outro, existe um problema em algum deles. A auditoria parte dessa ideia simples e procura onde a cadeia se rompe.

## Os cruzamentos que mais encontram problema

| Confronto | O que pode aparecer |
|---|---|
| XML das notas emitidas × EFD ICMS/IPI | Nota emitida e não escriturada, nota cancelada escriturada, CFOP diferente |
| XML das notas recebidas × EFD ICMS/IPI | Crédito de ICMS não aproveitado, ou aproveitado em nota que não deveria gerar crédito |
| EFD ICMS/IPI × EFD-Contribuições | Receita diferente entre os dois arquivos; CST de PIS e COFINS incoerente com a operação |
| EFD-Contribuições × ECD | Base de crédito sem lastro contábil; despesas que geram crédito e não foram informadas |
| ECD × ECF | Saldos que não batem, adições e exclusões sem conta de origem |
| Bloco G (CIAP) × imobilizado contábil | Bem creditado que já foi baixado, bem do ativo sem crédito |
| Inventário (Bloco H) × estoque contábil | Diferenças de estoque que o fisco pode tratar como omissão |

Nem todo confronto se aplica a toda empresa. Uma indústria do Lucro Real usa todos; um comércio do Lucro Presumido trabalha com menos arquivos e menos créditos.

## Exemplo ilustrativo

Uma indústria do Lucro Real tem, num ano, R$ 1.250.000 de receita de vendas tributadas informada na EFD ICMS/IPI e R$ 1.180.000 na EFD-Contribuições. A diferença de R$ 70.000 pode ter várias explicações: devoluções tratadas de forma diferente nos dois arquivos, notas complementares, uma filial que ficou de fora. Mas, se for receita não oferecida ao PIS e à COFINS, o cálculo do risco é direto:

| Item | Valor |
|---|---|
| Diferença de receita | R$ 70.000,00 |
| PIS (1,65%) | R$ 1.155,00 |
| COFINS (7,6%) | R$ 5.320,00 |
| **Contribuições em risco** | **R$ 6.475,00** |

A esse valor somam-se multa e juros se a diferença for encontrada pelo fisco. Corrigida antes, por iniciativa própria, a situação é bem diferente. Pode acontecer também o contrário: a diferença ser receita que não deveria ter sido tributada e foi. Aí o achado é crédito.

## Onde a auditoria costuma achar crédito

Quem faz auditoria preventiva pensando só em risco perde metade do valor do trabalho. Os achados a favor da empresa são frequentes:

- **Notas de entrada com ICMS destacado e não creditado**, em especial de materiais classificados como uso e consumo que, analisados, são insumos ou material intermediário.
- **Bens do imobilizado fora do CIAP**, que deixam de gerar o crédito de 1/48 por mês. Veja [como o CIAP é escriturado no Bloco G](/ciap-efd-icms-ipi-bloco-g/).
- **Despesas que geram crédito de PIS e COFINS** e nunca foram informadas na EFD-Contribuições, como manutenção, fretes e serviços ligados à produção.
- **CST de PIS e COFINS errado nas saídas**, tributando produto que tem alíquota zero ou tributação monofásica.

Cada achado desses entra numa revisão estruturada, nos moldes do que descrevemos em [revisão fiscal dos últimos 5 anos](/revisao-fiscal-5-anos-como-funciona/).

## Como priorizar as divergências

Uma auditoria bem feita gera uma lista longa. Nem tudo merece o mesmo esforço. Uma forma prática de ordenar:

1. **Valor e recorrência.** Uma divergência pequena que se repete todo mês por cinco anos pode ser maior que uma grande e isolada.
2. **Prazo.** Períodos próximos de completar cinco anos têm prioridade, tanto para corrigir débito (antes que o fisco o faça) quanto para recuperar crédito (antes que o prazo acabe).
3. **Natureza.** Débito não declarado tem tratamento diferente de crédito não aproveitado. O primeiro pede correção rápida; o segundo pede documentação antes de qualquer retificação.
4. **Causa.** Se a origem é um parâmetro do ERP (CFOP, CST, cadastro de produto), corrigir a causa vale mais que corrigir os meses passados.

## Com que frequência fazer

Uma auditoria completa dos cinco anos faz sentido uma vez, para limpar o passado. Depois disso, o modelo mais eficiente é a rotina: conferir os principais cruzamentos todo mês, antes da entrega dos arquivos, e fazer um fechamento anual mais profundo antes da ECF. Mudança de ERP, de contador ou de regime tributário são momentos em que a auditoria deve ser antecipada, porque é quando os parâmetros costumam se perder.

## O que fazer agora

1. Reúna os XML de notas emitidas e recebidas e os arquivos SPED (EFD ICMS/IPI, EFD-Contribuições, ECD e ECF) dos últimos cinco anos.
2. Comece pelo confronto mais simples: receita de vendas na EFD ICMS/IPI contra a da EFD-Contribuições, mês a mês.
3. Confira se todo bem do imobilizado com ICMS creditado está no Bloco G e se os baixados saíram dele.
4. Separe as divergências em risco e crédito, e ordene cada lista por valor e prazo.
5. Antes de retificar qualquer arquivo, identifique a causa no ERP e documente a correção.
