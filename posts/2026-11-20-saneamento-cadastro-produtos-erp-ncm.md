---
titulo: "Saneamento do cadastro de produtos no ERP: como revisar NCM e dados fiscais sem parar a empresa"
resumo: O cadastro de produtos alimenta todas as notas fiscais. Veja um método em etapas para revisar NCM, CEST, origem e campos de IBS e CBS no ERP, com amostragem, priorização e controle de mudanças.
data: 2026-11-20
categoria: Classificação Fiscal
tags: [cadastro de produtos, ERP, NCM, saneamento fiscal, Reforma Tributária]
fontes:
  - Receita Federal, NCM (estrutura e consulta pelo Sistema Classif) | https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/classificacao-fiscal-de-mercadorias/ncm
  - Receita Federal, Download e histórico da NCM | https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/classificacao-fiscal-de-mercadorias/download-ncm-nomenclatura-comum-do-mercosul
  - Portal da Conformidade Fácil (tabelas de classificação tributária do IBS e da CBS) | https://dfe-portal.svrs.rs.gov.br/CFF
  - Convênio ICMS nº 142/2018 (CEST) | https://www.confaz.fazenda.gov.br/legislacao/convenios/2018/CV142_18
checagem:
  - Os números do exemplo de amostragem são ilustrativos
  - Confirmar se o endereço da página de download da NCM no site da Receita continua ativo
---

O cadastro de produtos é a peça mais subestimada do fiscal. Cada nota emitida copia dali a NCM, o CEST, a origem da mercadoria, a unidade e, a partir da Reforma, os códigos de situação e de classificação tributária do IBS e da CBS. Um erro no cadastro não fica parado: ele se repete automaticamente, todo dia, em todas as filiais. E quase sempre o cadastro foi montado aos poucos, por pessoas diferentes, copiando notas de fornecedores e itens parecidos.

Revisar tudo de uma vez costuma parar na primeira semana. O que funciona é um projeto em etapas, com prioridade e controle.

## Etapa 1: extrair e entender a base

Exporte do ERP todos os produtos ativos com, no mínimo:

- código interno, descrição e unidade;
- NCM, CEST, código de origem;
- tratamento de IPI, ICMS (incluindo ST) e PIS/COFINS parametrizado;
- volume de vendas e de compras dos últimos 12 meses;
- data de criação e de última alteração do cadastro.

Só essa extração já revela problemas: produtos sem NCM, NCM com menos de oito dígitos, códigos que deixaram de existir, descrições genéricas ("peça", "material diverso"), o mesmo produto cadastrado duas vezes com códigos diferentes.

## Etapa 2: testes automáticos

Antes de olhar item a item, rode testes que não exigem conhecimento do produto:

| Teste | O que revela |
|---|---|
| NCM existe na tabela vigente | Códigos extintos ou digitados errado |
| NCM de entrada x NCM de saída do mesmo item revendido | Divergência com o fornecedor |
| Mesma descrição com NCMs diferentes | Inconsistência de cadastro |
| NCM listada nos anexos de ST sem CEST, ou CEST sem NCM correspondente | Enquadramento de ST a revisar |
| NCM de regime monofásico ou alíquota zero de PIS/COFINS x parametrização do item | Tributação de PIS/COFINS incoerente |
| Alíquota de IPI parametrizada x TIPI | IPI destacado errado |

A tabela da NCM pode ser baixada no site da Receita Federal, e a TIPI atualizada também. O Convênio ICMS nº 142/2018 traz NCM e CEST dos segmentos de substituição tributária.

## Etapa 3: priorizar pelo risco

Nem todo item merece a mesma atenção. Uma matriz simples ajuda:

- **Prioridade 1**: itens fabricados ou revendidos de maior faturamento; itens com IPI diferente de zero; itens em ST; itens monofásicos ou com alíquota zero.
- **Prioridade 2**: insumos relevantes da produção, porque definem crédito.
- **Prioridade 3**: materiais de uso e consumo e itens de baixo giro.

## Etapa 4: amostragem para dimensionar

Antes de mobilizar equipe, uma amostra mostra o tamanho do problema.

### Exemplo ilustrativo

Uma empresa tem 5.000 itens ativos. Uma amostra de 200 itens, revisados tecnicamente, encontra 30 com NCM incorreta.

| Item | Valor |
|---|---|
| Taxa de erro na amostra | 30 ÷ 200 = 15% |
| Estimativa de itens com erro na base | 5.000 × 15% = 750 itens |

Esse número não substitui a revisão, mas ajuda a definir prazo, equipe e se vale começar pelos itens de prioridade 1. Se a amostra for feita só com itens de alto giro, a taxa não vale para a base inteira. Separe amostras por família ou por prioridade.

## Etapa 5: revisão técnica com memorial

Para os itens priorizados, a revisão segue o roteiro de classificação: entender o produto, ler as Notas de Seção e de Capítulo, aplicar as Regras Gerais de Interpretação e consultar a Nesh. O post sobre [o que é a NCM e como classificar](/ncm-o-que-e-como-classificar/) detalha o método. Para peças e materiais do almoxarifado, as Notas da Seção XVI pesam muito, como explicado em [classificação de peças de reposição](/classificacao-fiscal-materiais-industriais-pecas/).

Cada decisão vai para um memorial: produto, código anterior, código novo, fundamento, responsável e data.

## Etapa 6: controle de mudanças no ERP

Trocar a NCM no cadastro parece simples, mas tem efeitos:

- **Data de vigência.** A correção vale a partir de quando? Notas anteriores com o código antigo continuam no SPED e podem exigir análise do passado.
- **Parametrização tributária.** Mudar a NCM pode mudar IPI, ST e PIS/COFINS. O item precisa ser reparametrizado junto.
- **Integrações.** E-commerce, força de vendas e sistemas de clientes podem ter o código replicado.
- **Permissão de edição.** Quem pode criar e alterar NCM? Sem controle de acesso, o cadastro volta a degradar.

## Etapa 7: o passado

Se a revisão encontra erro que gerou tributo a menor, a empresa decide com o contador como regularizar. Se encontra tributo pago a maior, há um potencial de recuperação dos últimos cinco anos, que depende de retificações e de pedido formal. Os dois lados devem ser quantificados antes de qualquer decisão.

## O cadastro e a Reforma Tributária

A NF-e já tem os campos de Código de Situação Tributária (CST) e de Código de Classificação Tributária (cClassTrib) do IBS e da CBS. O Portal da Conformidade Fácil, mantido pelas administrações tributárias, publica as tabelas e tem um assistente que relaciona NCM e classificação tributária. Para a maioria dos produtos, o código de classificação depende da NCM certa: cesta básica, insumos agropecuários, dispositivos médicos e outros regimes da Lei Complementar nº 214/2025 são definidos por código NCM/SH.

Cadastro saneado em 2026 é o que permite emitir nota certa em 2027, quando a CBS passa a substituir o PIS e a COFINS.

## O que fazer agora

1. Exporte a base de produtos com os campos fiscais e o volume de movimentação.
2. Rode os testes automáticos da tabela acima e conte as inconsistências.
3. Faça uma amostra técnica por família para dimensionar o trabalho.
4. Defina a matriz de prioridade e um cronograma por etapas.
5. Estabeleça regra de permissão e de memorial para toda criação ou alteração de NCM no ERP.
