#!/usr/bin/env python3
"""
Gerador do blog da AC&FT Assessoria e Consultoria Fiscal e Tributária (blog.aceft.com.br).

Uso:
    python build.py              gera o site em _site/
    python build.py --serve      gera e abre um servidor local em http://localhost:8000
    python build.py --rascunhos  inclui posts marcados como rascunho e com data futura

Os posts ficam em posts/*.md. Veja CLAUDE.md para o formato e o guia editorial.
"""
from __future__ import annotations

import html
import json
import os
import re
import shutil
import sys
import unicodedata
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.exit("Falta a biblioteca 'markdown'. Rode: python -m pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent
POSTS_DIR = ROOT / "posts"
OUT = ROOT / "_site"

SITE_URL = "https://blog.aceft.com.br"
MAIN_SITE = "https://aceft.com.br"
SITE_NAME = "AC&FT Assessoria e Consultoria Fiscal e Tributária"
BLOG_NAME = "Blog AC&FT"
AUTOR_PADRAO = "Equipe AC&FT"
WHATSAPP = "https://wa.me/5534991516719"
EMAIL = "rogerio@aceft.com.br"
TELEFONE = "+55 34 99151-6719"
CIDADE = "Uberaba"
UF = "MG"
AUTOR_RESPONSAVEL = "Rogério Lima Teixeira"
REGISTRO_PROFISSIONAL = "MG-092937/O"
# Verificação do Bing Webmaster Tools (Google é por propriedade de domínio, não precisa de tag).
BING_SITE_VERIFICATION = "D41AB44FBD3B96958E593913C785F8E3"
# Tags com ao menos este número de posts ganham página própria (/tag/slug/).
TAG_MIN_POSTS = 2
POSTS_PER_PAGE = 12
BRT = timezone(timedelta(hours=-3))

OG_IMAGE = SITE_URL + "/assets/og-image.png"

# Dados estruturados do site inteiro (Organização + WebSite com caixa de busca).
ORG_LD = {
    "@context": "https://schema.org",
    "@type": ["Organization", "AccountingService"],
    "@id": MAIN_SITE + "/#organizacao",
    "name": SITE_NAME,
    "alternateName": "AC&FT",
    "url": MAIN_SITE,
    "logo": SITE_URL + "/assets/icon-512.png",
    "image": OG_IMAGE,
    "email": EMAIL,
    "telephone": TELEFONE,
    "areaServed": {"@type": "Country", "name": "Brasil"},
    "address": {"@type": "PostalAddress", "addressLocality": CIDADE,
                "addressRegion": UF, "addressCountry": "BR"},
    "founder": {"@type": "Person", "name": AUTOR_RESPONSAVEL},
    "knowsAbout": ["Crédito de ICMS", "PIS e COFINS", "Laudos técnicos tributários",
                   "Ativo imobilizado", "Classificação fiscal (NCM)", "Reforma Tributária"],
    "sameAs": [MAIN_SITE],
}
WEBSITE_LD = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": SITE_URL + "/#website",
    "url": SITE_URL + "/",
    "name": BLOG_NAME,
    "inLanguage": "pt-BR",
    "publisher": {"@id": MAIN_SITE + "/#organizacao"},
    "potentialAction": {
        "@type": "SearchAction",
        "target": {"@type": "EntryPoint", "urlTemplate": SITE_URL + "/buscar/?q={search_term_string}"},
        "query-input": "required name=search_term_string",
    },
}
SITE_LD = json.dumps([ORG_LD, WEBSITE_LD], ensure_ascii=False)

HEAD_EXTRA = f"""<meta property="og:image" content="{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Blog AC&amp;FT: laudos técnicos, ICMS, ativo imobilizado e recuperação de créditos">
<meta name="twitter:card" content="summary_large_image">
<meta name="msvalidate.01" content="{BING_SITE_VERIFICATION}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/assets/icon-512.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<script type="application/ld+json">{SITE_LD}</script>"""

CATEGORIES = {
    "Laudos Técnicos": "laudos-tecnicos",
    "Créditos de ICMS": "icms",
    "PIS e COFINS": "pis-cofins",
    "Recuperação de Créditos": "recuperacao-de-creditos",
    "Ativo Imobilizado": "ativo-imobilizado",
    "Classificação Fiscal": "classificacao-fiscal",
    "Reforma Tributária": "reforma-tributaria",
}
REQUIRED = ["titulo", "resumo", "data", "categoria", "fontes"]
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
         "agosto", "setembro", "outubro", "novembro", "dezembro"]


# --------------------------------------------------------------------------- #
# Modelo e leitura dos posts
# --------------------------------------------------------------------------- #
@dataclass
class Post:
    slug: str
    titulo: str
    resumo: str
    data: date
    categoria: str
    fontes: list[str]
    html: str
    palavras: int
    atualizado: date | None = None
    tags: list[str] = field(default_factory=list)
    autor: str = "Equipe AC&FT"
    rascunho: bool = False
    faq: list[str] = field(default_factory=list)
    headings: list[tuple[str, str]] = field(default_factory=list)

    @property
    def url(self) -> str:
        return f"/{self.slug}/"

    @property
    def cat_slug(self) -> str:
        return CATEGORIES[self.categoria]

    @property
    def leitura(self) -> int:
        return max(1, round(self.palavras / 200))


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def parse_front_matter(raw: str, path: Path) -> tuple[dict, str]:
    """Front matter simples: 'chave: valor' e listas com '  - item'."""
    if not raw.startswith("---"):
        raise ValueError(f"{path.name}: o arquivo precisa começar com '---'")
    _, fm, body = raw.split("---", 2)
    meta: dict = {}
    key = None
    for line in fm.strip().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^\s+-\s+(.*)$", line)
        if m and key:
            meta.setdefault(key, [])
            if not isinstance(meta[key], list):
                raise ValueError(f"{path.name}: '{key}' mistura valor e lista")
            meta[key].append(unquote(m.group(1)))
            continue
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if not m:
            raise ValueError(f"{path.name}: linha inválida no cabeçalho: {line!r}")
        key, value = m.group(1), m.group(2).strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key] = [unquote(v) for v in value[1:-1].split(",") if v.strip()]
        elif value:
            meta[key] = unquote(value)
    return meta, body


def unquote(v: str) -> str:
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


def parse_date(v: str, path: Path, campo: str) -> date:
    try:
        return date.fromisoformat(v)
    except ValueError:
        raise ValueError(f"{path.name}: '{campo}' deve estar no formato AAAA-MM-DD (recebi {v!r})")


def render_markdown(body: str) -> tuple[str, list[tuple[str, str]]]:
    md = markdown.Markdown(
        extensions=["extra", "sane_lists", "toc"],
        extension_configs={"toc": {"slugify": lambda v, sep: slugify(v), "permalink": False}},
    )
    out = md.convert(body)
    # links externos abrem em nova aba
    out = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', out)
    # tabelas roláveis no celular
    out = out.replace("<table>", '<div class="table-wrap"><table>').replace("</table>", "</table></div>")
    # subtítulos de nível 2, para montar o sumário (índice) do artigo
    headings = [(t.get("id", ""), t.get("name", "")) for t in getattr(md, "toc_tokens", []) if t.get("level") == 2]
    return out, headings


def load_posts(incluir_rascunhos: bool) -> list[Post]:
    hoje = datetime.now(BRT).date()
    posts, slugs, erros = [], set(), []
    for path in sorted(POSTS_DIR.glob("*.md")):
        try:
            raw = path.read_text(encoding="utf-8")
            linhas = [str(i) for i, l in enumerate(raw.splitlines(), 1) if "—" in l or "–" in l]
            if linhas:
                raise ValueError(f"{path.name}: travessão (— ou –) nas linhas {', '.join(linhas)}. "
                                 "Reescreva com vírgula, dois-pontos, parênteses ou ponto final.")
            meta, body = parse_front_matter(raw, path)
            faltando = [k for k in REQUIRED if not meta.get(k)]
            if faltando:
                raise ValueError(f"{path.name}: faltam os campos {', '.join(faltando)}")
            if meta["categoria"] not in CATEGORIES:
                raise ValueError(f"{path.name}: categoria '{meta['categoria']}' não existe. "
                                 f"Use uma de: {', '.join(CATEGORIES)}")
            if not isinstance(meta["fontes"], list):
                meta["fontes"] = [meta["fontes"]]
            slug = meta.get("slug") or re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
            slug = slugify(slug)
            if slug in slugs:
                raise ValueError(f"{path.name}: slug '{slug}' repetido")
            slugs.add(slug)
            faq = meta.get("faq", []) if isinstance(meta.get("faq", []), list) else [meta["faq"]]
            faq = [f for f in faq if "|" in f]  # cada item: "Pergunta? | Resposta."
            corpo_html, headings = render_markdown(body)
            post = Post(
                slug=slug,
                titulo=meta["titulo"],
                resumo=meta["resumo"],
                data=parse_date(meta["data"], path, "data"),
                atualizado=parse_date(meta["atualizado"], path, "atualizado") if meta.get("atualizado") else None,
                categoria=meta["categoria"],
                fontes=meta["fontes"],
                tags=meta.get("tags", []) if isinstance(meta.get("tags", []), list) else [meta["tags"]],
                autor=meta.get("autor", AUTOR_PADRAO),
                rascunho=str(meta.get("rascunho", "false")).lower() in ("true", "sim", "1"),
                html=corpo_html,
                palavras=len(re.findall(r"\w+", body)),
                faq=faq,
                headings=headings,
            )
        except ValueError as e:
            erros.append(str(e))
            continue
        if not incluir_rascunhos and (post.rascunho or post.data > hoje):
            continue
        posts.append(post)
    if erros:
        sys.exit("Erros nos posts:\n  - " + "\n  - ".join(erros))
    posts.sort(key=lambda p: (p.data, p.slug), reverse=True)
    return posts




# --------------------------------------------------------------------------- #
# Templates
# --------------------------------------------------------------------------- #
e = html.escape

# Preenchido em build(): nome da tag -> slug, só para tags com página própria (/tag/slug/).
TAG_SLUGS: dict[str, str] = {}


def data_br(d: date) -> str:
    return f"{d.day} de {MESES[d.month - 1]} de {d.year}"


def data_curta(d: date) -> str:
    return f"{d.day:02d} {MESES[d.month - 1][:3]} {d.year}"


def header() -> str:
    return f"""<header class="site-header">
  <div class="wrap nav">
    <a class="brand" href="/" aria-label="{e(BLOG_NAME)}"><img src="/assets/logo.png" alt="AC&amp;FT" width="126" height="50"><span class="brand-blog">Blog</span></a>
    <button class="nav-toggle" id="navToggle" aria-label="Abrir menu" aria-expanded="false">☰</button>
    <ul class="nav-links" id="navLinks">
      <li><a href="/" class="is-active">Artigos</a></li>
      <li><a href="/buscar/">Buscar</a></li>
      <li><a href="{MAIN_SITE}/#servicos">Serviços</a></li>
      <li><a href="{MAIN_SITE}/#empresa">A Empresa</a></li>
      <li><a href="/sobre/">Sobre</a></li>
      <li><a class="btn btn--accent" href="{WHATSAPP}" target="_blank" rel="noopener">Fale com um especialista</a></li>
    </ul>
  </div>
</header>"""


def footer() -> str:
    cats = "\n".join(f'          <li><a href="/categoria/{s}/">{e(c)}</a></li>' for c, s in CATEGORIES.items())
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="brand" href="/" aria-label="{e(BLOG_NAME)}"><img src="/assets/logo.png" alt="AC&amp;FT" width="126" height="50"></a>
        <p class="footer-about">Assessoria e consultoria fiscal e tributária para indústria, comércio e serviços em todo o Brasil: laudos técnicos, recuperação de créditos de ICMS e PIS/COFINS, ativo imobilizado e classificação fiscal.</p>
        <p class="footer-small"><a href="/feed.xml">Assine o feed RSS do blog</a></p>
      </div>
      <div>
        <h4>Temas</h4>
        <ul>
{cats}
        </ul>
      </div>
      <div>
        <h4>Contato</h4>
        <ul>
          <li><a href="/sobre/">Sobre o autor</a></li>
          <li><a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp (34) 99151-6719</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Uberaba/MG, atendimento em todo o Brasil</li>
          <li><a href="{MAIN_SITE}/">aceft.com.br</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© {datetime.now(BRT).year} AC&amp;FT Assessoria e Consultoria Fiscal e Tributária. Registro MG-092937/O, Rogério Lima Teixeira, Técnico em Contabilidade.</span>
    </div>
  </div>
</footer>

<a class="wa" href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="Fale no WhatsApp">✆ <span>Fale no WhatsApp</span></a>

<script>
  var t = document.getElementById('navToggle'), n = document.getElementById('navLinks');
  t.addEventListener('click', function () {{
    var open = n.classList.toggle('is-open');
    t.setAttribute('aria-expanded', open);
  }});
</script>"""


def page(*, title: str, description: str, path: str, body: str, og_type: str = "website",
         extra_head: str = "", noindex: bool = False) -> str:
    url = SITE_URL + path
    robots = '<meta name="robots" content="noindex,follow">\n' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<meta name="theme-color" content="#001e2e">
{robots}<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="{e(BLOG_NAME)}">
{HEAD_EXTRA}
<link rel="alternate" type="application/rss+xml" title="{e(BLOG_NAME)}" href="/feed.xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
{extra_head}
</head>
<body>

{header()}

{body}

{footer()}
</body>
</html>
"""


def post_card(p: Post) -> str:
    return f"""<article class="post-card">
  <a href="{p.url}">
    <span class="post-cat">{e(p.categoria)}</span>
    <h3>{e(p.titulo)}</h3>
    <p>{e(p.resumo)}</p>
    <span class="post-meta">{data_curta(p.data)} · {p.leitura} min de leitura</span>
  </a>
</article>"""


def chips(ativa: str | None, contagem: dict[str, int]) -> str:
    items = [f'<a class="chip{" is-active" if ativa is None else ""}" href="/">Todos</a>']
    for c, s in CATEGORIES.items():
        if contagem.get(c):
            cls = " is-active" if ativa == c else ""
            items.append(f'<a class="chip{cls}" href="/categoria/{s}/">{e(c)} <small>{contagem[c]}</small></a>')
    return '<nav class="chips" aria-label="Temas">' + "".join(items) + "</nav>"


def pagination(base: str, atual: int, total: int) -> str:
    if total <= 1:
        return ""
    def href(n: int) -> str:
        return base if n == 1 else f"{base}pagina/{n}/"
    partes = []
    if atual > 1:
        partes.append(f'<a href="{href(atual - 1)}">← Anteriores</a>')
    partes.append(f"<span>Página {atual} de {total}</span>")
    if atual < total:
        partes.append(f'<a href="{href(atual + 1)}">Mais antigos →</a>')
    return '<nav class="pagination">' + "".join(partes) + "</nav>"


def listing_pages(posts: list[Post], base: str, titulo: str, subtitulo: str,
                  ativa: str | None, contagem: dict[str, int], titulo_pagina: str,
                  extra_head: str = "") -> dict[str, str]:
    pages = {}
    total = max(1, -(-len(posts) // POSTS_PER_PAGE))
    for n in range(1, total + 1):
        lote = posts[(n - 1) * POSTS_PER_PAGE: n * POSTS_PER_PAGE]
        destaque = ""
        if n == 1 and lote and ativa is None:
            d, lote = lote[0], lote[1:]
            destaque = f"""<a class="post-featured" href="{d.url}">
      <span class="post-cat">{e(d.categoria)} · mais recente</span>
      <h2>{e(d.titulo)}</h2>
      <p>{e(d.resumo)}</p>
      <span class="post-meta">{data_curta(d.data)} · {d.leitura} min de leitura</span>
    </a>"""
        cards = "\n".join(post_card(p) for p in lote)
        vazio = '<p class="lead">Nenhum artigo publicado ainda.</p>' if not posts else ""
        path = base if n == 1 else f"{base}pagina/{n}/"
        sufixo = "" if n == 1 else f" (página {n})"
        body = f"""<section class="hero">
  <div class="wrap">
    <span class="eyebrow">{e(BLOG_NAME)}</span>
    <h1>{titulo}</h1>
    <p class="lead">{subtitulo}</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {chips(ativa, contagem)}
    {destaque}
    <div class="post-grid">
{cards}
    </div>
    {vazio}
    {pagination(base, n, total)}
  </div>
</section>"""
        pages[path] = page(title=f"{titulo_pagina}{sufixo}", description=re.sub(r"<[^>]+>", "", subtitulo),
                           path=path, body=body, extra_head=extra_head if n == 1 else "")
    return pages


def breadcrumb_ld(trilha: list[tuple[str, str]]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": nome, "item": SITE_URL + href}
            for i, (nome, href) in enumerate(trilha)
        ],
    }


def toc_html(headings: list[tuple[str, str]]) -> str:
    """Sumário do artigo, só quando há 3 ou mais subtítulos."""
    itens = [(hid, nome) for hid, nome in headings if hid]
    if len(itens) < 3:
        return ""
    lis = "".join(f'<li><a href="#{e(hid)}">{e(nome)}</a></li>' for hid, nome in itens)
    return (f'<nav class="toc" aria-label="Neste artigo"><p class="toc-title">Neste artigo</p>'
            f'<ol>{lis}</ol></nav>')


def split_faq(item: str) -> tuple[str, str]:
    pergunta, resposta = (x.strip() for x in item.split("|", 1))
    return pergunta, resposta


def faq_html(faq: list[str]) -> str:
    if not faq:
        return ""
    blocos = "".join(
        f'<details class="faq-item"><summary>{e(p)}</summary><p>{e(r)}</p></details>'
        for p, r in (split_faq(i) for i in faq)
    )
    return f'<section class="post-faq"><h2>Perguntas frequentes</h2>{blocos}</section>'


def faq_ld(faq: list[str]) -> dict:
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": p,
             "acceptedAnswer": {"@type": "Answer", "text": r}}
            for p, r in (split_faq(i) for i in faq)
        ],
    }


def tags_html(tags: list[str]) -> str:
    if not tags:
        return ""
    itens = []
    for t in tags:
        s = TAG_SLUGS.get(t)
        itens.append(f'<li><a href="/tag/{s}/">{e(t)}</a></li>' if s else f"<li>{e(t)}</li>")
    return '<ul class="post-tags">' + "".join(itens) + "</ul>"


def post_page(p: Post, relacionados: list[Post]) -> str:
    fontes = "\n".join(f"<li>{fonte_html(f)}</li>" for f in p.fontes)
    rel = ""
    if relacionados:
        rel = f"""<section class="section section--soft">
  <div class="wrap">
    <h2 class="related-title">Leia também</h2>
    <div class="post-grid">
{chr(10).join(post_card(r) for r in relacionados)}
    </div>
  </div>
</section>"""
    atualizado = (f' · atualizado em <time datetime="{p.atualizado.isoformat()}">{data_br(p.atualizado)}</time>'
                  if p.atualizado else "")
    tags = tags_html(p.tags)
    ld = {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": p.titulo,
        "description": p.resumo,
        "datePublished": p.data.isoformat(),
        "dateModified": (p.atualizado or p.data).isoformat(),
        "inLanguage": "pt-BR",
        "mainEntityOfPage": SITE_URL + p.url,
        "articleSection": p.categoria,
        "keywords": ", ".join(p.tags),
        "author": {"@type": "Person", "name": AUTOR_RESPONSAVEL,
                   "jobTitle": "Técnico em Contabilidade", "url": SITE_URL + "/sobre/",
                   "worksFor": {"@id": MAIN_SITE + "/#organizacao"}},
        "publisher": {"@id": MAIN_SITE + "/#organizacao", "@type": "Organization", "name": SITE_NAME,
                      "url": MAIN_SITE,
                      "logo": {"@type": "ImageObject", "url": SITE_URL + "/assets/icon-512.png"}},
        "image": OG_IMAGE,
    }
    grafo = [ld, breadcrumb_ld([("Blog", "/"), (p.categoria, f"/categoria/{p.cat_slug}/"), (p.titulo, p.url)])]
    if p.faq:
        grafo.append(faq_ld(p.faq))
    extra = (f'<meta property="article:published_time" content="{p.data.isoformat()}">\n'
             + "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>'
                         for x in grafo))
    wa = WHATSAPP + "?text=" + quote_wa("Olá! Li o artigo “" + p.titulo + "” no blog da AC&FT e gostaria de uma avaliação.")
    body = f"""<section class="hero hero--post">
  <div class="wrap wrap--post">
    <nav class="breadcrumb" aria-label="Você está em"><a href="/">Blog</a> / <a href="/categoria/{p.cat_slug}/">{e(p.categoria)}</a></nav>
    <h1>{e(p.titulo)}</h1>
    <p class="lead">{e(p.resumo)}</p>
    <p class="post-byline"><a href="/sobre/">{e(p.autor)}</a> · <time datetime="{p.data.isoformat()}">{data_br(p.data)}</time>{atualizado} · {p.leitura} min de leitura</p>
  </div>
</section>

<article class="section section--post">
  <div class="wrap wrap--post">
    {toc_html(p.headings)}
    <div class="prose">
{p.html}
    </div>
    {faq_html(p.faq)}
    {tags}

    <aside class="post-sources">
      <h2>Fontes e legislação</h2>
      <ul>
{fontes}
      </ul>
      <p class="post-revisor">Responsável técnico: <a href="/sobre/">{e(AUTOR_RESPONSAVEL)}</a>, Técnico em Contabilidade (registro {e(REGISTRO_PROFISSIONAL)}).</p>
      <p class="post-disclaimer">Conteúdo informativo, atualizado na data de publicação. A legislação tributária muda com frequência e cada empresa tem particularidades: o direito ao crédito depende de análise do caso concreto.</p>
    </aside>

    <div class="post-cta">
      <h2>Sua empresa pode ter créditos a recuperar?</h2>
      <p>Fale com a AC&amp;FT para uma avaliação do potencial tributário da sua empresa.</p>
      <a class="btn btn--accent" href="{e(wa)}" target="_blank" rel="noopener">Falar no WhatsApp</a>
    </div>
  </div>
</article>

{rel}"""
    return page(title=f"{p.titulo} | {BLOG_NAME}", description=p.resumo, path=p.url,
                body=body, og_type="article", extra_head=extra)


def quote_wa(text: str) -> str:
    from urllib.parse import quote
    return quote(text)


def fonte_html(f: str) -> str:
    """'Descrição | https://url' vira link; sem URL vira texto."""
    if "|" in f:
        desc, url = (x.strip() for x in f.rsplit("|", 1))
        if url.startswith("http"):
            return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(desc)}</a>'
    return e(f)


def sobre_page() -> str:
    pessoa = {
        "@context": "https://schema.org",
        "@type": "Person",
        "@id": SITE_URL + "/sobre/#responsavel",
        "name": AUTOR_RESPONSAVEL,
        "jobTitle": "Técnico em Contabilidade",
        "worksFor": {"@id": MAIN_SITE + "/#organizacao"},
        "url": SITE_URL + "/sobre/",
        "email": EMAIL,
        "knowsAbout": ORG_LD["knowsAbout"],
        "sameAs": [MAIN_SITE],
    }
    extra = ('<script type="application/ld+json">'
             + json.dumps([pessoa, breadcrumb_ld([("Blog", "/"), ("Sobre", "/sobre/")])], ensure_ascii=False)
             + "</script>")
    body = f"""<section class="hero hero--post">
  <div class="wrap wrap--post">
    <nav class="breadcrumb" aria-label="Você está em"><a href="/">Blog</a> / Sobre</nav>
    <h1>Sobre o blog e o responsável técnico</h1>
    <p class="lead">Quem escreve e revisa o conteúdo da AC&amp;FT sobre créditos tributários, laudos técnicos e ativo imobilizado.</p>
  </div>
</section>

<article class="section section--post">
  <div class="wrap wrap--post">
    <div class="prose">
<h2>Responsável técnico</h2>
<p><strong>{e(AUTOR_RESPONSAVEL)}</strong> é Técnico em Contabilidade (registro {e(REGISTRO_PROFISSIONAL)}) e responsável técnico da {e(SITE_NAME)}, em {e(CIDADE)} ({UF}), com atendimento em todo o Brasil.</p>
<p>A atuação concentra-se em recuperação de créditos tributários de ICMS, PIS e COFINS; laudos técnicos de crédito de ICMS sobre energia elétrica, combustíveis, gás combustível e telecomunicações; laudos de perda; gestão de ativo imobilizado (inventário físico com TAGs, vida útil, depreciação e CIAP); classificação fiscal (NCM); e adequação à Reforma Tributária (classificação para IBS e CBS).</p>
<h2>Como o conteúdo é produzido</h2>
<p>Os artigos são produzidos pela equipe da AC&amp;FT e passam por revisão técnica antes da publicação. Cada texto cita as fontes oficiais em que se baseia, como Planalto, Receita Federal, CONFAZ, Secretarias de Estado de Fazenda, STJ, STF, CARF, CPC e CFC.</p>
<p>O conteúdo é informativo e não substitui a análise do caso concreto. A legislação tributária muda com frequência e cada empresa tem particularidades: o direito ao crédito depende de avaliação específica.</p>
<h2>Contato</h2>
<p>WhatsApp <a href="{WHATSAPP}" target="_blank" rel="noopener">(34) 99151-6719</a>, e-mail <a href="mailto:{EMAIL}">{EMAIL}</a>, site <a href="{MAIN_SITE}/" target="_blank" rel="noopener">aceft.com.br</a>.</p>
    </div>

    <div class="post-cta">
      <h2>Sua empresa pode ter créditos a recuperar?</h2>
      <p>Fale com a AC&amp;FT para uma avaliação do potencial tributário da sua empresa.</p>
      <a class="btn btn--accent" href="{WHATSAPP}" target="_blank" rel="noopener">Falar no WhatsApp</a>
    </div>
  </div>
</article>"""
    return page(title=f"Sobre o blog e o responsável técnico | {BLOG_NAME}",
                description=f"{AUTOR_RESPONSAVEL}, Técnico em Contabilidade (registro {REGISTRO_PROFISSIONAL}), "
                            "responsável técnico da AC&FT: créditos tributários, laudos técnicos e ativo imobilizado.",
                path="/sobre/", body=body, extra_head=extra)


def search_index(posts: list[Post]) -> str:
    dados = [{"t": p.titulo, "r": p.resumo, "u": p.url, "c": p.categoria,
              "g": " ".join(p.tags), "d": data_curta(p.data)} for p in posts]
    return json.dumps(dados, ensure_ascii=False, separators=(",", ":"))


def buscar_page() -> str:
    body = """<section class="hero hero--post">
  <div class="wrap wrap--post">
    <nav class="breadcrumb" aria-label="Você está em"><a href="/">Blog</a> / Buscar</nav>
    <h1>Buscar no blog</h1>
    <p class="lead">Procure por tema, tributo ou termo fiscal (ICMS, CIAP, PER/DCOMP, NCM, energia elétrica).</p>
    <form class="search-form" role="search" onsubmit="return false;">
      <input type="search" id="q" name="q" placeholder="Digite um termo e veja os artigos" autocomplete="off" aria-label="Buscar no blog">
    </form>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="search-status" id="status" aria-live="polite"></p>
    <div class="post-grid" id="resultados"></div>
  </div>
</section>

<script>
(function () {
  var norm = function (s) { return (s || "").toLowerCase().normalize("NFD").replace(/[\\u0300-\\u036f]/g, ""); };
  var input = document.getElementById("q");
  var status = document.getElementById("status");
  var out = document.getElementById("resultados");
  var dados = [];
  var esc = function (s) { var d = document.createElement("div"); d.textContent = s; return d.innerHTML; };

  function card(p) {
    return '<article class="post-card"><a href="' + p.u + '">' +
      '<span class="post-cat">' + esc(p.c) + '</span>' +
      '<h3>' + esc(p.t) + '</h3><p>' + esc(p.r) + '</p>' +
      '<span class="post-meta">' + esc(p.d) + '</span></a></article>';
  }
  function render(q) {
    var termos = norm(q).split(/\\s+/).filter(Boolean);
    if (!termos.length) { out.innerHTML = ""; status.textContent = "Digite um termo para buscar entre " + dados.length + " artigos."; return; }
    var r = dados.filter(function (p) {
      var alvo = norm(p.t + " " + p.r + " " + p.c + " " + p.g);
      return termos.every(function (t) { return alvo.indexOf(t) !== -1; });
    });
    status.textContent = r.length ? (r.length + " artigo(s) para \\u201c" + q + "\\u201d") : ("Nenhum artigo para \\u201c" + q + "\\u201d.");
    out.innerHTML = r.slice(0, 60).map(card).join("");
  }
  function start() {
    var q = new URLSearchParams(location.search).get("q") || "";
    input.value = q;
    render(q);
    input.addEventListener("input", function () {
      render(input.value);
      var u = input.value ? ("?q=" + encodeURIComponent(input.value)) : location.pathname;
      history.replaceState(null, "", u);
    });
    input.focus();
  }
  fetch("/search-index.json").then(function (r) { return r.json(); })
    .then(function (j) { dados = j; start(); })
    .catch(function () { status.textContent = "Não foi possível carregar o índice de busca."; });
})();
</script>"""
    return page(title=f"Buscar no blog | {BLOG_NAME}",
                description="Busque artigos do blog da AC&FT por tema, tributo ou termo fiscal.",
                path="/buscar/", body=body, noindex=True)


# --------------------------------------------------------------------------- #
# Arquivos auxiliares
# --------------------------------------------------------------------------- #
def feed(posts: list[Post]) -> str:
    def rfc822(d: date) -> str:
        return datetime(d.year, d.month, d.day, 6, 0, tzinfo=BRT).strftime("%a, %d %b %Y %H:%M:%S -0300")
    items = "\n".join(f"""  <item>
    <title>{e(p.titulo)}</title>
    <link>{SITE_URL}{p.url}</link>
    <guid>{SITE_URL}{p.url}</guid>
    <pubDate>{rfc822(p.data)}</pubDate>
    <category>{e(p.categoria)}</category>
    <description>{e(p.resumo)}</description>
  </item>""" for p in posts[:30])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
<channel>
  <title>{e(BLOG_NAME)}</title>
  <link>{SITE_URL}/</link>
  <description>Laudos técnicos, créditos de ICMS e PIS/COFINS, ativo imobilizado e recuperação de créditos tributários.</description>
  <language>pt-BR</language>
{items}
</channel>
</rss>
"""


def sitemap(posts: list[Post], paths: list[str]) -> str:
    urls = [f"  <url><loc>{SITE_URL}{p}</loc></url>" for p in paths]
    urls += [f"  <url><loc>{SITE_URL}{p.url}</loc><lastmod>{(p.atualizado or p.data).isoformat()}</lastmod></url>"
             for p in posts]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")


def write(path: str, content: str) -> None:
    target = OUT / path.lstrip("/")
    if path.endswith("/"):
        target = target / "index.html"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


# --------------------------------------------------------------------------- #
def build(incluir_rascunhos: bool = False) -> list[Post]:
    posts = load_posts(incluir_rascunhos)
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    shutil.copy2(ROOT / "style.css", OUT / "style.css")
    shutil.copytree(ROOT / "assets", OUT / "assets")
    shutil.copy2(ROOT / "assets" / "favicon.ico", OUT / "favicon.ico")
    # Domínio próprio do GitHub Pages e arquivos de verificação (Google, Bing), copiados sem alteração
    for src in [ROOT / "CNAME", *ROOT.glob("google*.html"), *ROOT.glob("BingSiteAuth.xml")]:
        if src.exists():
            shutil.copy2(src, OUT / src.name)

    contagem = {c: sum(1 for p in posts if p.categoria == c) for c in CATEGORIES}
    listados = ["/", "/sobre/"]

    # Índice de tags por slug. Só ganham página própria as tags com ao menos TAG_MIN_POSTS posts.
    tag_posts: dict[str, list[Post]] = {}
    tag_nome: dict[str, str] = {}
    for p in posts:
        vistos = set()
        for t in p.tags:
            s = slugify(t)
            if not s or s in vistos:
                continue
            vistos.add(s)
            tag_posts.setdefault(s, []).append(p)
            tag_nome.setdefault(s, t)
    TAG_SLUGS.clear()
    for t in {tag for p in posts for tag in p.tags}:
        s = slugify(t)
        if s and len(tag_posts.get(s, [])) >= TAG_MIN_POSTS:
            TAG_SLUGS[t] = s

    for path, content in listing_pages(
            posts, "/", "Créditos tributários <em>na prática</em>",
            "Laudos técnicos, ICMS, PIS e COFINS, ativo imobilizado e recuperação de créditos, "
            "explicados para quem cuida do fiscal e do financeiro da empresa.",
            None, contagem, f"{BLOG_NAME}: laudos técnicos, ICMS e recuperação de créditos").items():
        write(path, content)

    for cat, s in CATEGORIES.items():
        doc = [p for p in posts if p.categoria == cat]
        if not doc:
            continue
        base = f"/categoria/{s}/"
        listados.append(base)
        bc = ('<script type="application/ld+json">'
              + json.dumps(breadcrumb_ld([("Blog", "/"), (cat, base)]), ensure_ascii=False) + "</script>")
        for path, content in listing_pages(doc, base, e(cat), f"Todos os artigos sobre {cat}.",
                                           cat, contagem, f"{cat} | {BLOG_NAME}", extra_head=bc).items():
            write(path, content)

    for p in posts:
        mesma = [r for r in posts if r is not p and r.categoria == p.categoria]
        outras = [r for r in posts if r is not p and r.categoria != p.categoria]
        write(p.url, post_page(p, (mesma + outras)[:3]))

    # Páginas de tag (cauda longa), ordenadas pelo slug
    for s in sorted(tag_posts):
        lst = tag_posts[s]
        if len(lst) < TAG_MIN_POSTS:
            continue
        nome = tag_nome[s]
        base = f"/tag/{s}/"
        listados.append(base)
        bc = ('<script type="application/ld+json">'
              + json.dumps(breadcrumb_ld([("Blog", "/"), (nome, base)]), ensure_ascii=False) + "</script>")
        for path, content in listing_pages(lst, base, e(nome), f"Artigos com a tag {e(nome)}.",
                                           None, contagem, f"{nome} | {BLOG_NAME}", extra_head=bc).items():
            write(path, content)

    write("/sobre/", sobre_page())
    write("/buscar/", buscar_page())
    write("/search-index.json", search_index(posts))

    write("/feed.xml", feed(posts))
    write("/sitemap.xml", sitemap(posts, listados))
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")
    write("/404.html", page(title=f"Página não encontrada | {BLOG_NAME}", description="Página não encontrada.",
                            path="/404.html", body='<section class="hero"><div class="wrap"><h1>Página não encontrada</h1>'
                            '<p class="lead">O endereço pode ter mudado. <a href="/">Veja todos os artigos</a>.</p></div></section>'))
    (OUT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"OK: {len(posts)} posts publicados em {OUT.relative_to(ROOT)}/")
    return posts


if __name__ == "__main__":
    build(incluir_rascunhos="--rascunhos" in sys.argv)
    if "--serve" in sys.argv:
        import functools
        import http.server
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
        print("Servindo em http://localhost:8000 (Ctrl+C para parar)")
        http.server.ThreadingHTTPServer(("127.0.0.1", 8000), handler).serve_forever()
