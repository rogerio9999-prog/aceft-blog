# Blog AC&FT (blog.aceft.com.br)

Blog da AC&FT Assessoria e Consultoria Fiscal e Tributária (Uberaba/MG, atendimento em todo o Brasil).
Site institucional: https://aceft.com.br (hospedado na Locaweb, fora deste repositório).

**Público:** donos, diretores financeiros, controllers, contadores e equipes fiscais de **indústrias, comércio, mineração e prestadores de serviço**, em geral no Lucro Real ou Presumido (e também empresas do Simples, no tema do crédito monofásico). É um público técnico: pode usar os termos do dia a dia fiscal (CIAP, SPED, EFD ICMS/IPI, EFD-Contribuições, PER/DCOMP), sempre explicando a sigla na primeira vez.

**Serviços da AC&FT que o blog apoia:** laudos técnicos de crédito de ICMS (energia elétrica, combustíveis, gás combustível, telecomunicações), laudos de perda (desossa, evaporação na panificação), recuperação de PIS e COFINS (insumos, últimos 5 anos), crédito monofásico no Simples Nacional, revisão fiscal dos últimos 5 anos, ativo imobilizado (inventário físico com TAGs, avaliação, vida útil, depreciação, CIAP), classificação fiscal (NCM) e adequação à Reforma Tributária (classificação para IBS e CBS).

## Estrutura

- `posts/*.md`: um arquivo por artigo. **É aqui que o conteúdo diário entra.**
- `build.py`: gera o site em `_site/` (página inicial, temas, **tags** `/tag/slug/`, artigos, página **/sobre/**, página de **busca** `/buscar/` com `search-index.json`, RSS, sitemap, robots.txt). Inclui dados estruturados (Organization/AccountingService, WebSite, BlogPosting, BreadcrumbList e FAQPage) e a verificação do Bing Webmaster Tools (`msvalidate.01`). O Google é verificado pela propriedade de domínio `aceft.com.br` (não precisa de tag).
- `style.css`, `assets/`: visual e imagens (mesma identidade do aceft.com.br).
- `CNAME`: domínio do GitHub Pages (blog.aceft.com.br).
- `.github/workflows/deploy.yml`: publica no GitHub Pages a cada push na `main` e todo dia às 06:00.
- `.github/workflows/validar-posts.yml`: confere o build em todo Pull Request.
- `.github/workflows/auto-publicar.yml`: publica sozinho os PRs `posts/...` às 11:47 (segunda tentativa às 12:53).

Comandos: `python build.py` (gera), `python build.py --serve` (gera e serve em localhost:8000), `python build.py --rascunhos` (inclui rascunhos e datas futuras).
O build **falha** se um post tiver campo obrigatório faltando, categoria inválida, slug repetido ou travessão. Rode-o sempre antes de abrir o PR.

## Formato de um post

Nome do arquivo: `posts/AAAA-MM-DD-slug-curto.md` (o slug vira a URL `https://blog.aceft.com.br/slug-curto/`).

```markdown
---
titulo: "Título claro, com o benefício ou a dúvida do leitor"
resumo: Uma ou duas frases (até ~200 caracteres). Vira a meta description e o texto do card.
data: 2026-11-21
categoria: Créditos de ICMS
tags: [tag 1, tag 2, tag 3]
fontes:
  - Nome da norma, decisão ou página oficial | https://url-oficial
checagem:
  - Ponto que o revisor humano precisa conferir
---

Texto em Markdown, começando direto pelo problema do leitor (sem repetir o título).
```

- Use aspas no título quando ele tiver dois-pontos ou caracteres especiais.
- Categorias válidas (exatamente assim): `Laudos Técnicos`, `Créditos de ICMS`, `PIS e COFINS`, `Recuperação de Créditos`, `Ativo Imobilizado`, `Classificação Fiscal`, `CBS / IBS`.
- Campos opcionais: `atualizado: AAAA-MM-DD`, `autor`, `slug`, `faq`.
- `checagem` **não aparece no site**: serve só para a revisão.
- Post com `data` futura só aparece no site a partir daquele dia.
- **`faq` (opcional, recomendado):** lista de 2 a 4 pares `Pergunta? | Resposta.` (um por linha, com `  - `). Vira uma seção "Perguntas frequentes" no fim do post e gera o dado estruturado `FAQPage` (pode render resultado rico no Google). A resposta é texto puro, curta e sem travessão. Exemplo:
  ```yaml
  faq:
    - O crédito de ICMS da energia vale para o comércio? | Em regra não: a regra geral adiou esse crédito. Há exceções para atividades de transformação, que dependem da legislação do estado.
    - Posso recuperar energia dos anos anteriores? | Sim, em regra os últimos cinco anos, conforme o art. 23 da LC 87/1996 e o procedimento do estado.
  ```
- **Tags:** reaproveite tags já usadas (veja outros posts) em vez de criar sinônimos. Uma tag só vira página própria (`/tag/slug/`) quando aparece em 2 ou mais posts, então tags consistentes constroem páginas de cauda longa.

## Rotina diária: 3 posts

Todo dia, produzir **3 posts**, um de cada linha editorial abaixo, em **um único Pull Request** (branch `posts/AAAA-MM-DD`). **Nunca fazer push direto na `main`.**

1. **ICMS e laudos técnicos.** Crédito de ICMS sobre energia elétrica, combustíveis, gás, telecomunicações, insumos, material intermediário, uso e consumo, CIAP; como um laudo técnico sustenta o crédito (medição, rateio, registro fotográfico); laudos de perda (desossa, evaporação); decisões do STJ e do STF; regras estaduais (diga sempre de qual estado é a regra; use Minas Gerais como exemplo quando fizer sentido).
2. **PIS, COFINS e recuperação de créditos.** Conceito de insumo, exclusões da base, crédito monofásico no Simples Nacional, revisão fiscal dos últimos 5 anos, prescrição, PER/DCOMP, retificação de SPED e de declarações, cuidados com a compensação, jurisprudência.
3. **Ativo imobilizado, classificação fiscal e Reforma Tributária** (alternar entre os três). Inventário e conciliação do imobilizado, vida útil, depreciação fiscal e contábil, teste de recuperabilidade, CIAP, baixa de bens; NCM e seus reflexos em IPI, ICMS e PIS/COFINS; Reforma: crédito de IBS e CBS sobre bens de capital e insumos, classificação de produtos (cClassTrib), transição dos créditos de ICMS e PIS/COFINS.

Antes de escrever, **liste os arquivos em `posts/`** e não repita temas já cobertos nos últimos 90 dias. Se um tema antigo mudou, prefira atualizar o post existente (campo `atualizado`).

### Regras de conteúdo (obrigatórias)

- **Precisão acima de tudo.** Não inventar números, alíquotas, prazos, números de lei, de decreto, de convênio, de tema repetitivo ou de processo. Se não tiver certeza, pesquise na fonte oficial; se ainda assim não tiver, escreva de forma que não dependa do número e registre o ponto em `checagem`.
- **Fontes oficiais** em `fontes`, com link: Planalto, Receita Federal, CONFAZ, Secretarias de Fazenda estaduais (SEF-MG etc.), STJ, STF, CARF, CPC, CFC, DOU. Nada de blogs de terceiros como fonte.
- **ICMS é estadual.** Toda regra de ICMS deve dizer de qual estado é, ou explicar que varia por estado.
- **Sem promessas** de valores ou percentuais de recuperação ("recupere milhões", "crédito garantido"). Explicar o direito, os requisitos e os riscos.
- **Sem conselho individual definitivo:** o direito ao crédito depende de análise do caso concreto; o texto mostra a regra e o raciocínio.
- **Não citar clientes** (nem os que aparecem no site), nem valores ou situações reais de clientes. Exemplos numéricos são sempre ilustrativos e assim identificados.

### Estilo

- Português do Brasil, tom de consultor tributário experiente falando com quem cuida do fiscal e do financeiro: técnico, claro, direto, sem juridiquês.
- **Nunca use travessão (— ou –)**, em nenhuma parte do post. Use vírgula, dois-pontos, parênteses ou ponto final. O `build.py` recusa posts com travessão. O hífen comum (-) continua permitido.
- Evite vícios de texto gerado por IA: frases de efeito vazias ("Não é só X, é Y"), listas de três adjetivos, "Em resumo", "Vale ressaltar", "É importante destacar". Frases curtas e concretas.
- 800 a 1.500 palavras.
- Abrir com o problema do leitor (um crédito que a empresa deixa de aproveitar, um risco na fiscalização), não com definição.
- Subtítulos `##`, listas curtas, **um exemplo numérico ilustrativo** sempre que houver cálculo (refaça as contas com Python) e tabelas quando houver comparação.
- Linkar 1 ou 2 posts relacionados do próprio blog (`/slug/`) quando existirem.
- Preencher o campo `faq` com 2 a 4 perguntas que o leitor realmente faria (bom para SEO e para o dado estruturado `FAQPage`).
- Terminar com um "o que fazer agora" prático (documentos a separar, o que conferir no SPED etc.). O convite para falar com a AC&FT já é inserido automaticamente: não repita.

### Revisão final (obrigatória, antes de abrir o PR)

Os posts são **publicados automaticamente às 11:47** se ninguém intervier. Depois de escrever, releia cada post como revisor:

1. Para **cada** número, alíquota, prazo, número de norma, de tema ou de processo citado, confirme na fonte oficial (WebFetch). Se não confirmar, corrija ou reescreva sem depender do número.
2. Refaça as contas dos exemplos com Python.
3. Confira que cada link em `fontes` abre e trata do assunto.
4. O que sobrar de dúvida vai para `checagem`. **Não use `rascunho: true`:** todos os posts do dia vão ao ar no horário. Se restar dúvida relevante, reescreva o trecho de forma geral (sem a informação não confirmada), retire o trecho ou troque o tema por outro da mesma linha editorial.

### Pull Request

Título: `Posts de DD/MM/AAAA`. No corpo, para cada post: título, linha editorial, resumo em uma frase, trechos reescritos de forma geral por falta de confirmação (se houver) e a lista `checagem` copiada do arquivo.

### Publicação automática

`.github/workflows/auto-publicar.yml` faz o merge dos PRs `posts/...` às 11:47 de Brasília (segunda tentativa às 12:53), exceto os marcados com a etiqueta `segurar`, os fechados e os que falharam na validação.
