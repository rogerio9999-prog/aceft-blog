---
titulo: "NCM errada no cadastro de produtos: o efeito em IPI, ICMS e PIS/COFINS e como revisar"
resumo: Um código NCM incorreto muda a alíquota de IPI, o regime de ICMS e o tratamento de PIS e COFINS. Veja como revisar o cadastro de produtos e por que isso importa para a Reforma Tributária.
data: 2026-11-21
categoria: Classificação Fiscal
tags: [NCM, classificação fiscal, IPI, ICMS, PIS, COFINS, Reforma Tributária, cadastro de produtos]
fontes:
  - Receita Federal, classificação fiscal de mercadorias | https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/classificacao-fiscal-de-mercadorias
  - Lei Complementar nº 214/2025 (IBS, CBS e Imposto Seletivo) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm
checagem:
  - Confirmar que a página da Receita Federal citada abre e trata de classificação fiscal (os sites oficiais não puderam ser abertos durante a redação)
  - Confirmar que a LC 214/2025 usa a classificação da NCM para definir o tratamento de bens no IBS e na CBS, e se houve alteração posterior (por exemplo, pela LC 227/2026), sem citar artigos
  - Conferir a TIPI em vigor para as alíquotas de IPI do produto real; as alíquotas do exemplo (5% e 0%) são ilustrativas
  - Conferir no regulamento de ICMS do estado se o código NCM define substituição tributária ou benefício fiscal (o texto trata do assunto de forma geral)
---

A NCM do produto está no cadastro desde que o sistema foi implantado, e ninguém mais olha para ela. Só que ela decide a alíquota de IPI, define se o produto entra na substituição tributária do ICMS, pode determinar o tratamento de PIS e COFINS (monofásico, alíquota zero) e, com a Reforma Tributária, vai alimentar a classificação para IBS e CBS. Um código errado repete o erro em cada nota fiscal.

## O que é a NCM

A Nomenclatura Comum do Mercosul tem 8 dígitos. Os seis primeiros vêm do Sistema Harmonizado, adotado internacionalmente. Os dois últimos são específicos do Mercosul. A classificação segue as Regras Gerais de Interpretação do Sistema Harmonizado e as notas explicativas, não o nome comercial do produto nem o código usado pelo concorrente.

Isso explica por que dois produtos parecidos podem cair em códigos diferentes: o que conta é a composição, a forma de apresentação e a função.

## Onde o erro aparece

| Tributo | Como a NCM influencia |
|---|---|
| IPI | A alíquota está na tabela de incidência (TIPI), por código. |
| ICMS | Em cada estado, a NCM pode definir se o produto está na substituição tributária, na pauta ou em benefício fiscal. A regra é estadual. |
| PIS e COFINS | Há tratamentos específicos por código, como o regime monofásico e a alíquota zero. |
| Comércio exterior | Define tributos de importação e controles administrativos. |
| IBS e CBS | A classificação do produto vai determinar o tratamento na Reforma Tributária. |

O erro pode ser contra a empresa (paga imposto a mais) ou a favor (paga a menos e fica exposta). Os dois merecem revisão.

## Exemplo ilustrativo

Os números são inventados. Um fabricante vende R$ 2.000.000,00 por mês de um produto. Ele está classificado num código com alíquota de IPI de 5% (ilustrativa). Na revisão, a análise técnica mostra que o produto correto fica num código com alíquota de 0% (também ilustrativa).

| Item | Valor |
|---|---|
| Base de vendas mensais | R$ 2.000.000,00 |
| IPI com a classificação antiga (5%) | R$ 100.000,00 |
| IPI com a classificação correta (0%) | R$ 0,00 |
| Diferença por mês | R$ 100.000,00 |

O exemplo mostra a escala do efeito, não promete valor. Para saber se existe pagamento a maior, é preciso conferir a descrição técnica do produto, a TIPI vigente e o histórico das notas. Em sentido contrário, se a classificação correta tivesse alíquota maior, a diferença seria um passivo, e a empresa deveria avaliar a regularização antes de uma fiscalização.

## Como revisar o cadastro

1. **Extraia a lista de NCMs usadas** nas notas dos últimos cinco anos e ordene por faturamento.
2. **Comece pelos produtos de maior valor** e por aqueles com mais de um código no período.
3. **Reúna a ficha técnica**: composição, medidas, finalidade, processo de fabricação, embalagem.
4. **Classifique com base nas Regras Gerais e nas notas explicativas.** Em caso de dúvida real, a Receita Federal possui um procedimento de consulta sobre classificação fiscal.
5. **Compare com os fornecedores e com o concorrente**, mas não use isso como prova. Código igual ao do mercado não garante que está certo.
6. **Cheque os reflexos**: IPI, ST, benefícios de ICMS, PIS e COFINS. Cada um pode mudar.
7. **Documente a decisão**, com a ficha técnica e a fundamentação, para o caso de questionamento.

## Por que isso importa para a Reforma Tributária

A adequação à Reforma Tributária pede cadastro de produto limpo. A Lei Complementar nº 214/2025 define o tratamento de IBS e CBS por tipo de bem e serviço, e os documentos fiscais eletrônicos terão de trazer a classificação tributária de cada item. Um cadastro com NCM duvidosa carrega o erro para o novo sistema. Corrigir agora é mais barato do que corrigir quando o ERP já estiver parametrizado.

## O que fazer agora

1. Peça ao TI a lista de NCMs ativas e o faturamento por código.
2. Separe os 20 produtos de maior receita para a primeira rodada.
3. Reúna fichas técnicas e, se necessário, laudos do produto.
4. Compare o código atual com a TIPI e com a legislação de ICMS do seu estado.
5. Registre as mudanças e avalie, com a consultoria, se há pagamento a maior ou a menor nos últimos cinco anos.
