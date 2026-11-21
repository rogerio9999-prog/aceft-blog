---
titulo: "Registro fotográfico e plaquetas de potência: como transformar o laudo técnico em prova"
resumo: Foto de plaqueta, foto de ambiente e diagrama elétrico são o que liga o número do laudo à fábrica real. Veja o que fotografar, como organizar e um exemplo de erro de potência que muda o índice.
data: 2026-11-20
categoria: Laudos Técnicos
tags: [registro fotográfico, plaqueta, laudo técnico, prova, crédito de ICMS]
fontes:
  - Lei Complementar nº 87/1996 (Lei Kandir), arts. 23 e 33 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp87.htm
  - Código Tributário Nacional, art. 195 | https://www.planalto.gov.br/ccivil_03/leis/l5172compilado.htm
  - Guia Prático da EFD ICMS/IPI, registro 0305 (função e centro de custo do bem) | https://www.gov.br/sped/pt-br/assuntos/escrituracoes-digitais/efd-icms-ipi/manuais-e-documentos-tecnicos
checagem:
  - Potências, consumos e índices do exemplo são ilustrativos
  - As recomendações de organização das fotos são boas práticas, não exigência legal
---

Um laudo de crédito de ICMS pode ter uma planilha impecável e ainda assim cair numa fiscalização. Basta o fiscal perguntar: "como eu sei que esse motor de 75 kW existe e está na linha de produção?". Se a resposta for "está na planilha", a prova é fraca. Se a resposta for uma foto datada do motor instalado, outra da plaqueta com a potência legível e a indicação no layout da fábrica, a conversa muda.

## Por que a foto importa tanto

O laudo afirma três coisas sobre cada equipamento: que ele existe, que tem certa potência e que trabalha em certa área. A planilha registra essas afirmações. A foto prova.

A Lei Complementar nº 87/1996 condiciona o crédito à idoneidade da documentação (art. 23). O Código Tributário Nacional, art. 195, garante ao fisco o exame de documentos e mercadorias e exige a guarda dos comprovantes até a prescrição. O registro fotográfico é parte desses comprovantes: ele documenta a situação da fábrica numa data que, anos depois, ninguém mais consegue reconstituir de memória.

## O que fotografar

### A plaqueta de identificação

Todo motor, compressor, transformador ou equipamento industrial tem uma plaqueta com fabricante, modelo, número de série e dados elétricos (potência, tensão, corrente). A foto precisa:

- mostrar a plaqueta inteira e legível;
- ser tirada com o equipamento instalado, não no almoxarifado;
- permitir ler a potência sem ampliar demais.

Plaqueta ilegível por desgaste é comum. Nesse caso, o laudo registra a dificuldade e busca a potência no catálogo do fabricante pelo modelo, ou mede a carga com instrumento.

### O equipamento no ambiente

Uma segunda foto, mais aberta, mostra o equipamento no local de trabalho. Ela responde à pergunta "onde ele está?" e ajuda a classificar a área como produtiva ou não.

### O ambiente como um todo

Fotos dos setores (linha de produção, utilidades, escritório, refeitório, área externa) mostram a distribuição das cargas e servem de referência quando a fábrica mudar.

### Os quadros elétricos e os medidores

Quando o laudo usa submedição ou quando um equipamento atende só uma área por circuito dedicado, a foto do quadro e do diagrama unifilar sustenta a afirmação.

## Como organizar

| Elemento | Boa prática |
|---|---|
| Identificação | Cada foto com código do equipamento igual ao da planilha |
| Data | Data visível nos metadados ou no relatório |
| Localização | Referência ao setor e ao layout da fábrica |
| Ligação com o patrimônio | Quando for bem do imobilizado, o mesmo código da plaqueta patrimonial (TAG) |
| Arquivo | Pasta única, com cópia fora do servidor da empresa |

A ligação com o controle patrimonial é um ganho extra. O inventário do imobilizado com TAGs, tratado em [inventário do ativo imobilizado](/inventario-ativo-imobilizado-conciliacao-ciap/), e o laudo de energia descrevem as mesmas máquinas. Quando os códigos conversam, um documento confirma o outro. A própria EFD ICMS/IPI pede, no registro 0305, a função e o centro de custo dos bens do CIAP, e a coerência entre essas informações e o laudo reforça os dois.

## Exemplo ilustrativo: a plaqueta que mudou o índice

Uma indústria usava um laudo com índice de 87,61%, calculado sobre 96.225 kWh por mês, dos quais 84.300 kWh na produção. No cadastro, o moinho aparecia com motor de 75 kW, trabalhando com fator 0,80 por 600 horas mensais.

Na atualização, a foto da plaqueta mostrou que o motor original tinha sido trocado anos antes por um de 55 kW. A diferença de consumo estimado:

- (75 − 55) × 0,80 × 600 = **9.600 kWh por mês** a menos na produção.

| Item | Laudo antigo | Laudo corrigido |
|---|---|---|
| Consumo produtivo (kWh) | 84.300 | 74.700 |
| Consumo total (kWh) | 96.225 | 86.625 |
| Índice de aproveitamento | 87,61% | 86,23% |

A diferença no índice é pequena, mas era um erro que favorecia a empresa e que o fiscal encontraria com uma visita e uma foto. A correção veio antes, documentada, junto com a explicação da troca do motor. Erros na direção contrária, como máquinas grandes que nunca entraram no levantamento, também aparecem nessas revisões.

## O que a foto não resolve

- **Não prova horas de funcionamento.** Para isso servem registros de produção, escalas de turno e, quando possível, medição.
- **Não prova classificação jurídica.** A foto mostra onde o equipamento está; se aquela área dá direito a crédito no seu estado é uma questão de legislação.
- **Não substitui assinatura técnica.** O registro é anexo do laudo, que precisa de responsável habilitado (veja [quem pode assinar um laudo técnico](/laudo-tecnico-quem-pode-assinar-responsabilidade/)).

## Fotos para o passado

Na revisão de créditos dos últimos cinco anos, o desafio é provar como a fábrica era. Fotos antigas de manutenção, de auditorias, de seguradoras, de projetos de ampliação e até de material institucional ajudam a reconstituir o cenário. Notas fiscais de compra e de venda de máquinas marcam quando cada uma entrou e saiu. Quanto mais cedo a empresa passa a registrar a fábrica, menos ela depende dessa reconstituição.

## O que fazer agora

1. Abra o laudo atual e confira se cada equipamento relevante tem foto da plaqueta e foto no ambiente.
2. Escolha os dez maiores consumidores e confirme, no local, se a potência da plaqueta é a mesma da planilha.
3. Verifique se os códigos dos equipamentos no laudo conversam com as TAGs do imobilizado.
4. Separe fotos antigas da fábrica que possam ajudar a reconstituir períodos anteriores.
5. Guarde tudo em pasta única, com data, fora do computador de uma só pessoa.
