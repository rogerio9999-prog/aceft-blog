---
titulo: "cClassTrib e CST do IBS e da CBS na NF-e: o que são e como escolher o código certo"
resumo: Cada item da NF-e passa a ter um CST e um código de classificação tributária (cClassTrib) para o IBS e a CBS. Veja como as tabelas oficiais são organizadas, onde consultá-las e os cuidados no cadastro.
data: 2026-11-20
categoria: Reforma Tributária
tags: [cClassTrib, CST, NF-e, IBS, CBS]
fontes:
  - Portal da Conformidade Fácil (tabelas de CST, cClassTrib, crédito presumido e assistente de classificação) | https://dfe-portal.svrs.rs.gov.br/CFF
  - Tabela de Classificação Tributária do IBS e da CBS (consulta on-line) | https://dfe-portal.svrs.rs.gov.br/CFF/ClassificacaoTributaria
  - Lei Complementar nº 214/2025 (hipóteses de redução, isenção, diferimento e suspensão) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm
checagem:
  - A versão das tabelas muda com frequência (o portal indicava o Informe Técnico 2025.002 v1.71, de 30/10/2026); conferir a versão vigente na data da leitura
  - O portal publicou aviso, em 12/11/2026, sobre alteração de datas de implantação de Notas Técnicas; confirmar as datas atuais de obrigatoriedade das regras de validação dos grupos de IBS e CBS
  - Os códigos citados como exemplo foram copiados da tabela on-line em novembro de 2026 e podem ser alterados
---

Os sistemas emissores já receberam os campos novos da NF-e para o IBS e a CBS, e o fiscal recebeu, junto, uma pergunta para cada produto: qual CST e qual cClassTrib usar? Para muitos itens a resposta é a tributação integral. Para outros, a escolha depende de a operação estar numa das dezenas de hipóteses de redução, isenção, diferimento ou suspensão da Lei Complementar nº 214/2025. Código errado significa débito errado para o vendedor e crédito errado para o comprador.

## Dois códigos, uma lógica

| Campo | Tamanho | O que informa |
|---|---|---|
| CST do IBS e da CBS | 3 dígitos | A situação tributária geral da operação (tributação integral, alíquota reduzida, isenção, diferimento etc.) |
| cClassTrib | 6 dígitos | A hipótese legal específica dentro daquela situação; os três primeiros dígitos repetem o CST |

O cClassTrib detalha o CST. Se o CST diz "alíquota reduzida", o cClassTrib diz qual redução, com base em qual dispositivo ou anexo da lei.

## Os grupos de CST

Na tabela publicada no Portal da Conformidade Fácil, os CSTs aparecem agrupados assim:

| CST | Situação |
|---|---|
| 000 | Tributação integral |
| 010 e 011 | Tributação com alíquotas uniformes (regimes específicos, como serviços financeiros e planos de saúde) |
| 200 | Alíquota reduzida |
| 220 e 221 | Alíquota fixa e alíquota fixa proporcional |
| 222 | Redução de base de cálculo |
| 400 | Isenção |
| 410 | Imunidade e não incidência |
| 510 e 515 | Diferimento e diferimento com redução de alíquota |
| 550 | Suspensão |
| 620 | Tributação monofásica |
| 800 | Transferência de crédito |
| 810 e 811 | Ajustes (incluindo ajuste de IBS na Zona Franca de Manaus) |
| 820 | Tributação em documento específico |
| 830 | Exclusão da base de cálculo |

## Exemplos de cClassTrib

Alguns códigos da tabela, para mostrar a lógica:

- **000001**: situações tributadas integralmente pelo IBS e pela CBS;
- **200003**: vendas de produtos destinados à alimentação humana do Anexo I da LC 214/2025;
- **200034**: fornecimento dos alimentos destinados ao consumo humano do Anexo VII;
- **200038**: fornecimento dos insumos agropecuários e aquícolas do Anexo IX;
- **200030**: venda dos dispositivos médicos do Anexo IV.

Repare que muitos códigos citam um anexo da lei. E os anexos são listas de códigos NCM/SH ou NBS. Na prática, o cClassTrib de um produto depende de a NCM estar certa e de o produto corresponder à descrição do anexo.

## Indicadores que travam a nota

Cada CST e cClassTrib vem com indicadores na tabela oficial: se exige tributação, se há redução de base ou de alíquota, transferência de crédito, diferimento, tributação monofásica, crédito presumido, entre outros. As regras de validação dos documentos fiscais usam esses indicadores para obrigar ou proibir o preenchimento de grupos do XML. Escolher um cClassTrib incompatível com os demais campos pode gerar rejeição da nota quando as validações estiverem ativas.

Há também uma tabela separada de **crédito presumido**, com códigos próprios, usada nas hipóteses em que a lei concede crédito presumido ao adquirente.

## Onde consultar

O Portal da Conformidade Fácil, mantido pelas administrações tributárias, reúne:

- a tabela de classificação tributária, consultável por CST ou por cClassTrib;
- a tabela de crédito presumido;
- os Informes Técnicos com as versões das tabelas em planilha;
- um **assistente para classificação tributária**, que permite pesquisar por NCM ou descrição e pelo tipo de documento (NF-e ou NFC-e).

As tabelas são revisadas com frequência. A versão usada no ERP precisa ser atualizada a cada novo Informe Técnico, com registro da data em que a mudança entrou em produção.

## Erros previsíveis

- **Marcar tudo como 000001** por precaução. Para quem vende itens com redução (alimentos, insumos agropecuários, dispositivos médicos), isso significa destacar imposto a mais e perder competitividade.
- **Aplicar redução pela "família" do produto**, sem conferir a NCM e a descrição do anexo.
- **Parametrizar por cliente e não por operação.** Algumas hipóteses dependem do destinatário (órgão público, produtor rural não contribuinte), outras do produto. O cadastro precisa combinar as duas coisas.
- **Esquecer devoluções, remessas e bonificações**, que têm tratamento próprio.

## O papel da NCM e da NBS

A classificação tributária do IBS e da CBS é construída em cima da classificação fiscal. Um cadastro de NCM errado contamina o cClassTrib. Por isso a ordem de trabalho é: primeiro sanear NCM e NBS, depois parametrizar os novos códigos. Os posts sobre [saneamento do cadastro de produtos](/saneamento-cadastro-produtos-erp-ncm/) e o [checklist de classificação para IBS e CBS](/classificacao-produtos-reforma-tributaria-checklist/) organizam esse trabalho.

## O que fazer agora

1. Verifique qual versão das tabelas de CST e cClassTrib está carregada no ERP e compare com a publicada no Portal da Conformidade Fácil.
2. Liste os produtos e serviços que podem ter tratamento diferente da tributação integral, pelos anexos da LC 214/2025.
3. Para cada um, defina CST e cClassTrib com o fundamento legal e registre a decisão.
4. Teste a emissão em homologação com os principais cenários: venda normal, venda com redução, devolução, remessa e bonificação.
5. Crie uma rotina de atualização das tabelas a cada novo Informe Técnico.
