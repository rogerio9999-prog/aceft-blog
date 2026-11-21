---
titulo: "O que é a tributação monofásica do PIS e da COFINS e por que ela muda a conta de quem revende"
resumo: No monofásico, o fabricante ou importador recolhe PIS e COFINS por toda a cadeia e a revenda sai com alíquota zero. Entenda a lógica, os setores alcançados e os erros que fazem a empresa pagar duas vezes.
data: 2026-11-20
categoria: PIS e COFINS
tags: [PIS, COFINS, monofásico, tributação concentrada, revenda, alíquota zero]
fontes:
  - Lei nº 10.147/2000 (produtos farmacêuticos, de perfumaria, toucador e higiene pessoal) | https://www.planalto.gov.br/ccivil_03/leis/l10147.htm
  - Lei nº 10.485/2002 (máquinas, veículos, autopeças e pneus) | https://www.planalto.gov.br/ccivil_03/leis/2002/l10485.htm
  - Lei nº 9.718/1998, arts. 4º a 6º (combustíveis) | https://www.planalto.gov.br/ccivil_03/leis/l9718compilada.htm
  - Lei nº 10.637/2002, arts. 2º, § 1º, e 3º, I, b | https://www.planalto.gov.br/ccivil_03/leis/2002/l10637.htm
  - STJ, Tema Repetitivo 1093 (vedação de crédito na aquisição de bens monofásicos) | https://processo.stj.jus.br/repetitivos/temas_repetitivos/pesquisa.jsp?novaConsulta=true&tipo_pesquisa=T&sg_classe=REsp&num_processo_classe=1895255
  - Lei Complementar nº 214/2025, art. 542 (revogações a partir de 2027) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm
checagem:
  - A alíquota concentrada do exemplo é ilustrativa e não corresponde a um produto específico
  - Confirmar em qual dispositivo vigente da Lei nº 10.485/2002 está a alíquota zero para atacadistas e varejistas (o texto não cita o artigo)
  - A lista de setores é exemplificativa; a enumeração completa está no art. 2º, § 1º, da Lei nº 10.637/2002 e nas leis específicas
---

Uma distribuidora de autopeças, uma farmácia ou uma loja de cosméticos vende produtos cujo PIS e COFINS já foram pagos pelo fabricante. Se a empresa não sabe disso, ela recolhe de novo sobre a revenda. O imposto é pago duas vezes sobre a mesma mercadoria, todos os meses, sem que ninguém perceba, porque o valor se mistura ao total do faturamento.

## A ideia da tributação concentrada

No regime comum, PIS e COFINS incidem em cada etapa da cadeia: indústria, atacado e varejo pagam sobre a própria receita. No regime **monofásico**, também chamado de tributação concentrada, a lei transfere a carga para o início da cadeia:

- o **fabricante ou importador** recolhe PIS e COFINS com alíquotas maiores que as normais;
- os **distribuidores e varejistas** que revendem o produto têm alíquota zero sobre essa receita.

O Estado arrecada de poucos contribuintes (fabricantes e importadores), o que facilita o controle. Para quem revende, a consequência é direta: a receita daquele produto não deve sofrer nova incidência de PIS e COFINS.

## Quem está no monofásico

A Lei nº 10.637/2002, no art. 2º, § 1º, lista as leis que fixam alíquotas diferenciadas para produtores e importadores. Os grupos mais comuns são:

| Grupo | Lei de referência |
|---|---|
| Gasolina, diesel, GLP e outros derivados; álcool | Lei nº 9.718/1998 |
| Produtos farmacêuticos, de perfumaria, toucador e higiene pessoal | Lei nº 10.147/2000 |
| Máquinas e veículos, autopeças, pneus e câmaras de ar | Lei nº 10.485/2002 |
| Querosene de aviação | Lei nº 10.560/2002 |
| Bebidas frias (águas, refrigerantes, cervejas), com regras próprias e histórico de alterações | Leis citadas no art. 2º, § 1º, da Lei nº 10.637/2002 |

Cada lei delimita os produtos pelo código da NCM (Nomenclatura Comum do Mercosul), muitas vezes com exceções dentro da mesma posição. Por isso não existe atalho: é preciso conferir produto por produto. O método está no post sobre [como identificar produtos monofásicos pela NCM](/produtos-monofasicos-como-identificar-ncm/).

## O que acontece na revenda

A Lei nº 10.147/2000, por exemplo, reduz a zero as alíquotas sobre a receita de venda desses produtos pelas empresas que não são industriais nem importadoras (art. 2º). A Lei nº 10.485/2002 tem regra equivalente para comerciantes atacadistas e varejistas de veículos e autopeças.

Na prática, o comerciante:

- não recolhe PIS e COFINS sobre a receita de revenda dos itens monofásicos;
- **não toma crédito** sobre a compra desses itens, porque o art. 3º, I, "b", das Leis nº 10.637/2002 e nº 10.833/2003 veda o crédito na aquisição para revenda de produtos monofásicos.

O STJ confirmou essa vedação ao julgar o Tema Repetitivo 1093, em 2022. O tribunal também registrou que a monofasia se prende ao produto, e não à empresa: o mesmo revendedor continua com direito a crédito sobre os outros bens que compra e que seguem a regra geral.

## Exemplo ilustrativo

Um fabricante vende um produto monofásico por R$ 100. Suponha, só para ilustrar, uma alíquota concentrada de 12% de PIS e COFINS somados.

| Etapa | Preço | PIS e COFINS |
|---|---|---|
| Fabricante vende ao varejista | R$ 100,00 | R$ 12,00 (recolhido pelo fabricante) |
| Varejista vende ao consumidor | R$ 150,00 | R$ 0,00 (alíquota zero) |

Se o varejista do Lucro Presumido tratar essa receita como tributada no regime cumulativo (0,65% de PIS e 3% de COFINS), pagará R$ 5,48 a mais sobre cada venda de R$ 150, sem nenhuma obrigação legal de fazê-lo. No Simples Nacional, o efeito é semelhante: o DAS embute PIS e COFINS sobre uma receita que deveria estar segregada.

## Erros que custam caro

- **Cadastro de produto sem NCM confiável.** Se a NCM está errada, o sistema não marca o item como monofásico, ou marca um item que não é.
- **CST de saída genérico.** No Lucro Real e no Presumido, a saída de produto monofásico revendido tem código de situação tributária próprio na nota e na EFD-Contribuições.
- **Crédito indevido na compra.** No Lucro Real, tomar crédito sobre aquisição de produto monofásico para revenda gera glosa.
- **Simples sem segregação.** O optante precisa informar no PGDAS-D a receita com tributação monofásica, para que o sistema desconsidere PIS e COFINS. O passo a passo está em [recuperação do monofásico no Simples](/pis-cofins-monofasico-simples-nacional-recuperacao/).

## E a partir de 2027?

PIS e COFINS deixam de existir a partir de 2027, substituídos pela CBS (Emenda Constitucional nº 132/2023). A Lei Complementar nº 214/2025 revoga, a partir de 1º de janeiro de 2027, várias leis do monofásico, entre elas a Lei nº 10.147/2000. Os regimes da CBS e do IBS para combustíveis e outros setores seguem regras próprias. Para quem revendeu produtos monofásicos e pagou PIS e COFINS indevidamente, a janela de revisão dos últimos cinco anos continua aberta, contada de cada pagamento.

## O que fazer agora

1. Gere a relação dos produtos vendidos nos últimos 12 meses com NCM, CST de PIS e COFINS e valor de receita.
2. Marque os itens cujas NCMs aparecem nas leis do monofásico e confira as exceções de cada posição.
3. Compare com o que foi tributado na apuração: houve PIS e COFINS sobre receita que deveria ter alíquota zero?
4. No Lucro Real, confira se não há crédito tomado sobre compra de monofásico para revenda.
5. Se houver pagamento indevido, organize a recuperação dos últimos cinco anos com base nas notas fiscais.
