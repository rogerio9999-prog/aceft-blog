---
titulo: "Como contabilizar o crédito tributário recuperado: quando reconhecer, em que conta e como separar principal e Selic"
resumo: O crédito recuperado só entra no balanço quando a entrada do recurso é praticamente certa. Veja o momento do reconhecimento, a separação entre principal e juros, os lançamentos e o controle das compensações.
data: 2026-11-20
categoria: Recuperação de Créditos
tags: [contabilização, crédito tributário, CPC 25, Selic, compensação, recuperação de créditos]
fontes:
  - CPC 25: Provisões, Passivos Contingentes e Ativos Contingentes | https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=56
  - CPC 23: Políticas Contábeis, Mudança de Estimativa e Retificação de Erro | https://www.cpc.org.br/CPC/Documentos-Emitidos/Pronunciamentos/Pronunciamento?Id=54
  - Lei nº 6.404/1976 (Lei das S.A.), arts. 177 e 187 | https://www.planalto.gov.br/ccivil_03/leis/l6404consol.htm
  - Lei nº 9.250/1995, art. 39, § 4º (Selic na compensação e na restituição) | https://www.planalto.gov.br/ccivil_03/leis/l9250.htm
checagem:
  - Os valores do exemplo e os nomes de contas são ilustrativos; cada plano de contas tem a sua estrutura
  - A escolha entre reconhecer o crédito como mudança de estimativa (resultado do período) ou como retificação de erro (CPC 23) depende da causa; o texto trata isso de forma geral
  - O tratamento tributário do valor reconhecido está no post sobre IRPJ e CSLL e não foi detalhado aqui
---

A empresa terminou uma revisão fiscal, retificou as declarações e tem um crédito de PIS e COFINS a compensar. A pergunta seguinte, que costuma chegar ao contador só no fechamento do mês, é: quando e como esse valor entra no balanço? Lançar cedo demais infla o resultado com um crédito que ainda pode ser glosado. Lançar tarde demais, ou fora do lugar, distorce a margem e confunde a apuração do IRPJ e da CSLL.

## O momento do reconhecimento

O ponto de partida é o CPC 25, que trata dos ativos contingentes. A regra é conservadora: um ativo que depende de evento futuro incerto **não é reconhecido** no balanço; ele só é divulgado em nota explicativa quando a entrada de benefícios é provável. Quando a realização do ganho é **praticamente certa**, o ativo deixa de ser contingente e passa a ser reconhecido.

Aplicado à recuperação de créditos, isso leva a situações diferentes:

| Situação do crédito | Tratamento contábil usual |
|---|---|
| Tese em discussão judicial, sem decisão definitiva | Não reconhece; avalia divulgação em nota |
| Decisão judicial transitada em julgado, com valor ainda a apurar | Reconhece quando o valor puder ser mensurado com confiabilidade |
| Crédito administrativo apurado em revisão, documentado e escriturado (EFD retificada) | Em geral reconhece, se a documentação sustenta o direito |
| Crédito com pedido de ressarcimento em análise e risco relevante de glosa | Avaliar com cuidado; reconhecer só a parcela com sustentação sólida |

O critério é o grau de certeza, não a vontade de mostrar resultado. Uma revisão de insumos bem documentada é diferente de uma tese que depende de interpretação ainda contestada.

## Separar principal e atualização

O valor recuperado tem duas naturezas, que devem ir para contas diferentes:

- **Principal:** é o tributo pago a mais ou o crédito não aproveitado. Representa a recuperação de um custo ou de uma despesa que já passou pelo resultado.
- **Atualização pela Selic:** é a remuneração do dinheiro no tempo. Para tributos federais compensados ou restituídos, a Lei nº 9.250/1995 (art. 39, § 4º) prevê juros equivalentes à Selic acumulada, contados do pagamento indevido. Contabilmente, é receita financeira.

Misturar os dois numa única linha de "outras receitas" é o erro mais comum. Ele atrapalha a análise da margem e, principalmente, a apuração dos tributos, porque principal e Selic têm tratamentos fiscais diferentes. O tratamento tributário de cada parcela está em [tributação do crédito recuperado no IRPJ e na CSLL](/tributacao-credito-recuperado-irpj-csll/).

## Para onde vai o principal

O principal deve ir, sempre que possível, para a mesma linha onde o tributo foi originalmente registrado:

- Se o PIS e a COFINS pagos a mais foram lançados como dedução da receita bruta, a recuperação reduz essa dedução.
- Se o crédito não aproveitado era de insumo e o valor ficou no custo do produto vendido, a recuperação reduz o custo.
- Se o tributo foi registrado como despesa operacional, a recuperação reduz essa despesa.

Quando o valor é relevante e se refere a vários exercícios, muitas empresas preferem uma conta própria de "recuperação de tributos" dentro do mesmo grupo, para dar transparência. O que não se recomenda é jogar tudo em receita não operacional, como se fosse ganho eventual desligado da operação.

Se a origem for um erro contábil de exercício anterior, e não uma mudança de estimativa ou um fato novo, o CPC 23 trata da retificação de erro, com ajuste nos saldos de abertura. A diferença entre uma coisa e outra precisa ser decidida com o auditor, caso a empresa tenha um.

## Exemplo ilustrativo

Uma indústria conclui a revisão de tributos federais pagos a maior com R$ 300.000 de PIS e COFINS a recuperar e R$ 45.000 de atualização pela Selic, ambos com documentação suficiente para o reconhecimento. Os valores pagos a maior tinham sido registrados como dedução da receita bruta.

**No reconhecimento:**

| Conta | Débito | Crédito |
|---|---|---|
| PIS e COFINS a recuperar (ativo circulante) | R$ 345.000,00 | |
| Recuperação de PIS e COFINS (redutora das deduções da receita) | | R$ 300.000,00 |
| Receita financeira: atualização Selic | | R$ 45.000,00 |

**No uso de R$ 120.000 para abater PIS e COFINS a recolher no mês seguinte:**

| Conta | Débito | Crédito |
|---|---|---|
| PIS e COFINS a recolher (passivo) | R$ 120.000,00 | |
| PIS e COFINS a recuperar (ativo) | | R$ 120.000,00 |

O saldo de R$ 225.000 continua no ativo até ser usado. A forma de uso (desconto na própria apuração, compensação com outros tributos federais ou ressarcimento) depende da origem do crédito e das regras de cada tipo; nem todo crédito escritural de PIS e COFINS pode ser compensado com outros tributos. Se a compensação for feita depois de alguns meses, a Selic adicional do período também é reconhecida como receita financeira quando apurada.

## Controle das compensações

O ativo "tributos a recuperar" precisa de um controle auxiliar que feche com o balanço. Para cada crédito:

- origem (tese, período, tributo);
- número do PER/DCOMP ou do pedido;
- valores compensados por mês;
- situação da análise (pendente, homologado, não homologado).

Se uma compensação não for homologada, o débito compensado volta a ser exigido. Contabilmente, o crédito sai do ativo e o débito volta ao passivo, com multa e juros conforme o caso. Os riscos dessa situação estão em [compensação não homologada](/compensacao-nao-homologada-riscos/).

## Classificação no balanço

A parcela que a empresa espera compensar ou receber nos próximos 12 meses fica no ativo circulante. O restante vai para o realizável a longo prazo. Em créditos grandes, com débitos mensais pequenos para compensar, essa separação faz diferença nos índices de liquidez.

## O que fazer agora

1. Classifique cada crédito em levantamento pelo grau de certeza: judicial em andamento, judicial definitivo ou administrativo documentado.
2. Separe, para cada um, o valor principal e a atualização pela Selic.
3. Identifique em que linha do resultado o tributo original foi registrado e use a mesma linha para a recuperação.
4. Monte o controle auxiliar das compensações, com número de PER/DCOMP e situação de cada pedido.
5. Revise a nota explicativa sobre ativos contingentes no próximo fechamento.
