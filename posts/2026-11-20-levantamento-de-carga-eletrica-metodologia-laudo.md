---
titulo: "Levantamento de carga elétrica: como o laudo calcula o índice de aproveitamento do crédito de ICMS"
resumo: Potência, horas de uso e fator de utilização. Veja passo a passo como um levantamento de carga chega ao percentual de energia consumida na produção, com tabela de cálculo e conferência contra a conta.
data: 2026-11-20
categoria: Laudos Técnicos
tags: [levantamento de carga, energia elétrica, índice de aproveitamento, laudo técnico, ICMS]
fontes:
  - Lei Complementar nº 87/1996 (Lei Kandir), art. 33, II | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp87.htm
  - RICMS/MG 2023 (Decreto nº 48.589/2023), Parte Geral, art. 31, § 11 | https://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/ricms_2023_seco/regulamento2023_1.html
checagem:
  - Todos os equipamentos, potências, fatores, horas e valores do exemplo são ilustrativos
  - A classificação da oficina de manutenção como não produtiva no exemplo é um critério conservador; o tratamento pode variar por estado e por processo
---

Quando a fábrica não tem medidores separados por setor, a pergunta "quanto da energia vai para a produção?" só tem uma resposta defensável: um levantamento de carga bem documentado. É ele que dá origem ao índice de aproveitamento usado no crédito de ICMS da energia elétrica. Se o método for fraco, o índice cai na primeira conferência do fiscal.

Este texto mostra a metodologia por dentro. Para a visão geral do direito ao crédito, veja [crédito de ICMS sobre energia elétrica na indústria](/credito-icms-energia-eletrica-industria-laudo/).

## O ponto de partida legal

A Lei Complementar nº 87/1996, art. 33, II, b, permite o crédito do ICMS da energia elétrica **consumida no processo de industrialização**. A energia usada em outras finalidades do mesmo estabelecimento só dará crédito a partir de 1º de janeiro de 2033 (alínea d), ressalvada a proporção das exportações (alínea c). Em Minas Gerais, o RICMS/2023 reproduz essa regra no art. 31, § 11. Outros estados seguem a mesma lei complementar, mas a leitura de casos limite pode variar.

O levantamento de carga serve para separar essas duas parcelas dentro de uma única conta.

## As três variáveis de cada equipamento

Para cada consumidor de energia, o levantamento registra:

1. **Potência (kW).** Lida na plaqueta do equipamento ou no catálogo do fabricante, e conferida com medição quando possível. Motores, resistências, compressores, iluminação, ar-condicionado.
2. **Horas de funcionamento no mês.** Depende de turnos, dias trabalhados e regime de cada máquina. Uma extrusora de três turnos e um ar-condicionado de horário comercial têm horas muito diferentes.
3. **Fator de utilização.** Um motor de 75 kW raramente trabalha a 100% da potência o tempo todo. O fator expressa a carga média real em relação à nominal. Ele pode vir de medição com analisador de energia, de dados do fabricante ou de referências técnicas, sempre com o critério explicado.

O consumo estimado de cada equipamento é:

**consumo (kWh) = potência (kW) × fator de utilização × horas no mês**

## A classificação: produtivo ou não produtivo

Depois de estimar o consumo, cada item recebe uma classificação. As áreas que normalmente geram discussão:

| Área | Tendência de classificação | Ponto de atenção |
|---|---|---|
| Máquinas da linha de produção | Produtiva | Conferir se estão ativas |
| Iluminação do galpão produtivo | Produtiva | Separar da iluminação externa |
| Compressores e utilidades da linha | Produtiva, se atendem a produção | Verificar se também atendem outras áreas |
| Oficina de manutenção | Discutível | Depende do estado e da ligação com o processo |
| Laboratório de controle de qualidade | Discutível | Avaliar se o ensaio integra o processo |
| Escritório, TI, refeitório, vestiários | Não produtiva | Crédito adiado até 2033 |
| Iluminação externa e portaria | Não produtiva | Crédito adiado até 2033 |

O laudo deve justificar cada escolha. Quando um equipamento atende a produção e outra área (um compressor que também alimenta a oficina, por exemplo), o mais seguro é ratear e explicar o rateio.

## Exemplo ilustrativo completo

Uma indústria de plásticos em Minas Gerais trabalha em três turnos na produção (600 horas no mês) e em horário comercial no escritório (220 horas). Todos os números abaixo são ilustrativos.

| Equipamento | Potência (kW) | Fator | Horas/mês | Consumo (kWh) | Classe |
|---|---|---|---|---|---|
| Moinho | 75 | 0,80 | 600 | 36.000 | Produtiva |
| Compressor de ar da linha | 37 | 0,75 | 600 | 16.650 | Produtiva |
| Extrusora | 55 | 0,85 | 600 | 28.050 | Produtiva |
| Iluminação do galpão | 6 | 1,00 | 600 | 3.600 | Produtiva |
| Oficina de manutenção | 20 | 0,40 | 220 | 1.760 | Não produtiva |
| Ar-condicionado do escritório | 30 | 0,60 | 220 | 3.960 | Não produtiva |
| Iluminação do escritório e TI | 10 | 1,00 | 220 | 2.200 | Não produtiva |
| Iluminação externa | 8 | 1,00 | 360 | 2.880 | Não produtiva |
| Refeitório | 15 | 0,50 | 150 | 1.125 | Não produtiva |
| **Total** | | | | **96.225** | |

Consumo produtivo: 36.000 + 16.650 + 28.050 + 3.600 = **84.300 kWh**.

Índice de aproveitamento: 84.300 ÷ 96.225 = **87,61%**.

Se a conta do mês trouxe R$ 16.560 de ICMS destacado, o crédito sustentado pelo levantamento seria de 87,61% desse valor, ou cerca de R$ 14.507,75.

Note que a oficina foi classificada como não produtiva por critério conservador. Se a análise jurídica do estado permitir outra leitura, o índice muda, e o laudo deve mostrar os dois cenários.

## A conferência com a conta: o teste que o fiscal faz

O levantamento estima 96.225 kWh no mês. A conta da distribuidora mostrou 92.000 kWh. A estimativa ficou 4,59% acima do consumo real.

Uma diferença dessa ordem é esperada, porque fatores de utilização e horas são médias. O que o laudo faz:

- registra a diferença e explica a origem provável (fatores conservadores, paradas não previstas);
- aplica o **índice** (a proporção) sobre o ICMS real da conta, e não o consumo estimado em kWh;
- confere a estimativa contra vários meses, inclusive meses atípicos.

Se a estimativa ficar muito longe da conta, algo está errado: equipamento esquecido, horas superestimadas, máquina desativada ainda listada. Um levantamento que estima o dobro do que a conta mostra não convence ninguém.

## Medição direta: quando vale a pena

O levantamento por potência e horas é o método mais comum, mas não o único. Em plantas com grande consumo, a instalação de medidores por quadro de distribuição ou o uso de analisadores de energia por alguns dias dá números mais robustos. Muitas vezes o melhor laudo combina os dois: medição nos grandes consumidores e estimativa nos pequenos.

Quanto mais a empresa depender do crédito, maior o investimento em medição que se justifica.

## Erros comuns de metodologia

- **Usar a potência total instalada como consumo.** Ignora fator de utilização e horas e distorce o índice.
- **Esquecer cargas pequenas e permanentes.** Iluminação externa, servidores e câmeras funcionam 24 horas e somam.
- **Copiar o fator de um equipamento para todos.** Cada tipo de carga tem comportamento próprio.
- **Não registrar a data e o regime de turnos.** Se a fábrica muda de dois para três turnos, o índice muda junto.
- **Não guardar evidências.** Sem foto da plaqueta e sem planilha de cálculo, o número perde força. Veja [registro fotográfico e plaquetas como prova](/registro-fotografico-laudo-tecnico-prova/).

## O que fazer agora

1. Peça à manutenção a relação de equipamentos elétricos por setor, com potência nominal.
2. Levante o regime de turnos de cada área nos últimos 12 meses.
3. Separe as contas de energia do mesmo período, com consumo em kWh e ICMS destacado.
4. Faça um teste simples: some a potência dos grandes motores, aplique horas e fatores aproximados e compare com a conta. Se não fechar nem de longe, o índice atual provavelmente não tem base.
5. Confira se o percentual creditado no SPED Fiscal é o mesmo em todos os meses, mesmo quando a produção variou.
