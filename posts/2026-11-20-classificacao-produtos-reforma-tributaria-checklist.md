---
titulo: "Checklist: como classificar produtos e insumos para o IBS e a CBS"
resumo: Um roteiro em 10 passos para revisar o cadastro de produtos vendidos e de insumos comprados antes de operar com IBS e CBS, da NCM ao cClassTrib, passando por anexos de redução, Imposto Seletivo e uso pessoal.
data: 2026-11-20
categoria: Reforma Tributária
tags: [checklist, classificação tributária, IBS, CBS, cadastro de produtos]
fontes:
  - Lei Complementar nº 214/2025 (regimes diferenciados, anexos por NCM/SH e NBS, créditos e uso ou consumo pessoal) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm
  - Portal da Conformidade Fácil (tabelas de CST, cClassTrib, crédito presumido e assistente de classificação) | https://dfe-portal.svrs.rs.gov.br/CFF
  - Receita Federal, Classificação Fiscal de Mercadorias | https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/classificacao-fiscal-de-mercadorias
  - Decreto nº 7.708/2012 (NBS) | https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/decreto/d7708.htm
checagem:
  - Os anexos da LC 214/2025 foram alterados pela LC 227/2026; conferir a redação vigente de cada anexo usado na classificação
  - Confirmar a versão vigente das tabelas de CST e cClassTrib no Portal da Conformidade Fácil
---

A Reforma Tributária trouxe muita regra nova, mas o trabalho que mais pesa no dia a dia é antigo: saber exatamente o que a empresa vende e o que ela compra. Para o IBS e a CBS, cada produto precisa de uma NCM correta, de uma verificação contra os anexos da Lei Complementar nº 214/2025 e de um código de classificação tributária na nota. Cada insumo precisa ser avaliado quanto ao crédito. O checklist abaixo organiza esse trabalho em uma ordem que evita retrabalho.

## Parte 1: produtos vendidos

### 1. NCM conferida e documentada

Tudo começa aqui. Os anexos da LC 214/2025 que concedem redução ou alíquota zero, e o Anexo XVII do Imposto Seletivo, são listas de códigos NCM/SH. Com NCM errada, todo o resto erra junto. Use o roteiro do post sobre [o que é a NCM e como classificar](/ncm-o-que-e-como-classificar/) e registre o memorial de classificação dos itens relevantes.

### 2. NBS para os serviços

Assistência técnica, manutenção, industrialização por encomenda, locação de equipamentos: tudo o que a empresa presta como serviço precisa de código na NBS (Decreto nº 7.708/2012), porque a lei também define reduções por NBS.

### 3. Confronto com os anexos de redução e de alíquota zero

Verifique se cada produto aparece em algum regime diferenciado da LC 214/2025. Alguns exemplos de anexos, todos definidos por código e descrição:

| Regime | Onde está na LC 214/2025 |
|---|---|
| Cesta básica nacional de alimentos | Anexo I |
| Dispositivos médicos | Anexos IV e XII |
| Dispositivos de acessibilidade | Anexos V e XIII |
| Medicamentos | Anexo VI e regras próprias |
| Alimentos destinados ao consumo humano | Anexo VII |
| Produtos de higiene pessoal e limpeza | Anexo VIII |
| Insumos agropecuários e aquícolas | Anexo IX |
| Produtos hortícolas, frutas e ovos | Anexo XV |

O enquadramento exige que o produto corresponda **ao código e à descrição** do anexo. Família de produto parecida não basta.

### 4. Imposto Seletivo

Confira se algum produto está no Anexo XVII (veículos, embarcações e aeronaves, produtos fumígenos, bebidas alcoólicas e açucaradas, bens minerais). O IS começa em 2027 e é cobrado uma única vez, sem crédito.

### 5. Regimes que dependem do destinatário ou da operação

Algumas reduções e suspensões não dependem só do produto: vendas a produtor rural não contribuinte, operações com destino à Zona Franca de Manaus e Áreas de Livre Comércio, vendas a órgãos públicos, exportações, operações com empresa comercial exportadora. O cadastro precisa permitir que a regra do produto se combine com a regra do cliente e da operação.

### 6. CST e cClassTrib definidos por item e por cenário

Com os passos anteriores feitos, defina o Código de Situação Tributária (CST) e o Código de Classificação Tributária (cClassTrib) para cada combinação relevante de produto e operação, usando as tabelas oficiais do Portal da Conformidade Fácil. O assistente do portal permite pesquisar por NCM. O post sobre [cClassTrib na NF-e](/cclasstrib-classificacao-tributaria-nfe/) explica os códigos.

## Parte 2: insumos e itens comprados

### 7. Crédito como regra, exceções mapeadas

No IBS e na CBS, o crédito sobre aquisições é a regra (art. 47). Mapeie as exceções:

- itens de **uso ou consumo pessoal** do art. 57 (joias, bebidas alcoólicas, bens recreativos, bens fornecidos a sócios e empregados sem custo, veículos e imóveis residenciais nessas condições);
- as ressalvas que **mantêm o crédito**, como uniformes, EPI e alimentação fornecida no estabelecimento durante a jornada;
- compras sem débito (imunes, isentas, alíquota zero, diferimento, suspensão), que não geram crédito ao comprador (art. 49), salvo crédito presumido expresso.

### 8. NCM das compras relevantes

A NCM do insumo define se o fornecedor deve aplicar redução, alíquota zero ou tributação integral. Isso muda o valor do crédito. Confira a NCM e o cClassTrib das notas dos principais fornecedores e trate divergências antes que virem glosa ou crédito perdido.

### 9. Bens de capital identificados

Compras para o ativo imobilizado têm crédito integral e imediato (art. 108) e prazos menores de ressarcimento (art. 40). O cadastro e o fluxo de entrada precisam identificar o bem como ativo desde a nota fiscal.

## Parte 3: governança

### 10. Memorial, versão e responsável

Cada decisão de classificação precisa de:

- fundamento (NCM, Notas, anexo e artigo da lei, tabela e versão do cClassTrib);
- data de vigência no ERP;
- responsável pela decisão e pela revisão periódica.

As tabelas oficiais e os anexos mudam. Sem controle de versão, a empresa não consegue provar, daqui a cinco anos, por que emitiu a nota daquele jeito.

## Checklist resumido

| Nº | Item | Feito? |
|---|---|---|
| 1 | NCM dos produtos vendidos conferida e documentada | |
| 2 | NBS dos serviços prestados definida | |
| 3 | Produtos confrontados com os anexos de redução e alíquota zero | |
| 4 | Produtos confrontados com o Anexo XVII (Imposto Seletivo) | |
| 5 | Regras por destinatário e por operação mapeadas | |
| 6 | CST e cClassTrib parametrizados por cenário | |
| 7 | Exceções de crédito (uso pessoal, operações sem débito) mapeadas | |
| 8 | NCM e cClassTrib das compras relevantes conferidos | |
| 9 | Bens de capital identificados no fluxo de entrada | |
| 10 | Memorial, versão das tabelas e responsáveis definidos | |

## O que fazer agora

1. Extraia do ERP os produtos vendidos e os insumos comprados com NCM, NBS, volume e fornecedor.
2. Comece pelos passos 1 e 2: sem classificação fiscal correta, os demais passos não se sustentam.
3. Priorize os itens de maior faturamento e os que podem ter regime diferenciado.
4. Teste em ambiente de homologação a emissão das notas com os novos campos, nos cenários principais.
5. Defina uma revisão periódica do cadastro a cada atualização das tabelas oficiais ou da lei.
