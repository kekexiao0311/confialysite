# -*- coding: utf-8 -*-
import os
from build_data import (
    ICONS, CHECK_SVG, ARROW_SVG, CATEGORIES, PRODUCTS,
    STANDARD_DISCLAIMER, HOW_IT_WORKS, TRUST_BAR,
    POSITIONING_PILLARS, STATS, TIER1, UI, MESSAGES, LANGS,
)

ROOT = os.path.dirname(os.path.abspath(__file__))
FORM_ENDPOINT = "https://formspree.io/f/YOUR_FORM_ID"  # placeholder — see README
DOMAIN = "https://www.confialy.com"

# ---------------------------------------------------------------- helpers --

def other_lang(lang):
    return "es" if lang == "en" else "en"

def lang_prefix(lang):
    return "" if lang == "en" else "es/"

def out_path(lang, page_key):
    return lang_prefix(lang) + page_key

def depth_for(lang, page_key):
    d = page_key.count("/")
    if lang == "es":
        d += 1
    return d

def rel(depth):
    return "../" * depth

def T(lang, key):
    return UI[lang][key]

def icon(name):
    return ICONS.get(name, "")

def hero_scene_svg(icon_key):
    icon_svg = icon(icon_key)
    nested = icon_svg.replace(
        '<svg ', '<svg x="70" y="66" width="100" height="100" style="color:var(--forest)" ', 1
    )
    return f"""<svg viewBox="0 0 240 232" xmlns="http://www.w3.org/2000/svg">
  <circle cx="120" cy="116" r="108" fill="var(--sage-tint)"/>
  <circle cx="164" cy="76" r="46" fill="var(--amber-tint)"/>
  <circle cx="52" cy="176" r="10" fill="var(--amber)"/>
  <circle cx="204" cy="168" r="7" fill="var(--sage)"/>
  <circle cx="40" cy="70" r="6" fill="var(--forest)" opacity="0.35"/>
  {nested}
</svg>"""

# Real photography on every product page instead of the line-icon scene.
# Slug -> (filename in assets/photos/, {"en": alt text, "es": alt text})
PRODUCT_PHOTOS = {
    "salud": ("salud-hero.jpg", {"en": "Father laughing with his baby daughter outdoors", "es": "Padre riendo con su hija bebé al aire libre"}),
    "dental": ("dental-hero.jpg", {"en": "Close-up of a healthy, confident smile", "es": "Primer plano de una sonrisa sana y segura"}),
    "hogar": ("hogar-hero.jpg", {"en": "Couple carrying boxes and a plant into their new home", "es": "Pareja entrando a su nueva casa con cajas y una planta"}),
    "coche": ("coche-hero.jpg", {"en": "Woman smiling inside her car", "es": "Mujer sonriendo dentro de su coche"}),
    "motor": ("motor-hero.jpg", {"en": "Two women riding a scooter through a city street", "es": "Dos mujeres montando en scooter por una calle de la ciudad"}),
    "negocio": ("negocio-hero.jpg", {"en": "Confident small business owner standing in her shop", "es": "Dueña de un pequeño negocio, segura de sí misma en su local"}),
    "vida": ("vida-hero.jpg", {"en": "A multi-generational family walking together in a park", "es": "Una familia multigeneracional paseando junta por un parque"}),
    "accidente": ("accidente-hero.jpg", {"en": "Man smiling outdoors while hiking in the mountains", "es": "Hombre sonriendo al aire libre mientras hace senderismo en la montaña"}),
    "mascota": ("mascota-hero.jpg", {"en": "Woman hugging her golden retriever outdoors", "es": "Mujer abrazando a su golden retriever al aire libre"}),
    "responsabilidad-civil": ("responsabilidad-civil-hero.jpg", {"en": "Friends laughing together over dinner at home", "es": "Amigos riendo juntos durante una cena en casa"}),
    "responsabilidad-profesional": ("responsabilidad-profesional-hero.jpg", {"en": "Two professionals shaking hands over a business agreement", "es": "Dos profesionales dándose la mano tras un acuerdo"}),
    "seguro-de-comunidad": ("seguro-de-comunidad-hero.jpg", {"en": "A modern residential apartment building with balconies", "es": "Un edificio residencial moderno con balcones"}),
    "defensa-juridica": ("defensa-juridica-hero.jpg", {"en": "Two people reviewing documents together, smiling", "es": "Dos personas revisando documentos juntas, sonriendo"}),
    "ciberriesgos": ("ciberriesgos-hero.jpg", {"en": "Woman working on her laptop at an outdoor cafe", "es": "Mujer trabajando con su portátil en una cafetería al aire libre"}),
    "seguro-de-transporte": ("seguro-de-transporte-hero.jpg", {"en": "Smiling delivery driver standing by his van full of packages", "es": "Repartidor sonriente junto a su furgoneta llena de paquetes"}),
}

def hero_scene(lang, slug, r):
    photo = PRODUCT_PHOTOS.get(slug)
    if photo:
        filename, alts = photo
        return f"""<div class="hero-scene hero-scene--photo">
      <div class="hero-scene__blob"></div>
      <div class="hero__photo-frame"><img src="{r}assets/photos/{filename}" alt="{alts[lang]}" loading="eager"></div>
    </div>"""
    return f'<div class="hero-scene">{hero_scene_svg(PRODUCTS[slug]["icon"])}</div>'

def swoosh(center=False):
    cls = "swoosh swoosh--center" if center else "swoosh"
    return f'<svg class="{cls}" viewBox="0 0 84 18" xmlns="http://www.w3.org/2000/svg"><path d="M2 14c10-14 20-14 26-6s16 8 26 0 20-8 28 2"/></svg>'

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)

# --------------------------------------------------------------- head/nav --

def head(lang, page_key, title, desc):
    depth = depth_for(lang, page_key)
    r = rel(depth)
    canonical = f"{DOMAIN}/{out_path(lang, page_key)}"
    alt_en = f"{DOMAIN}/{out_path('en', page_key)}"
    alt_es = f"{DOMAIN}/{out_path('es', page_key)}"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{alt_en}">
<link rel="alternate" hreflang="es" href="{alt_es}">
<link rel="alternate" hreflang="x-default" href="{alt_en}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:locale" content="{'es_ES' if lang=='es' else 'en_US'}">
<meta property="og:site_name" content="Confialy">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/confialy-mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400..700&family=Figtree:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}css/style.css">
</head>
<body>
"""

def header(lang, page_key, active=""):
    depth = depth_for(lang, page_key)
    r = rel(depth)
    def cur(name):
        return ' aria-current="page"' if active == name else ""
    tier1_links = "".join(
        f'<a href="{r}{out_path(lang, "products/"+slug+".html")}"{cur(slug)}>{PRODUCTS[slug][lang]["name"]}</a>\n      '
        for slug in TIER1
    )
    other = other_lang(lang)
    lang_href = r + out_path(other, page_key)
    return f"""<header class="site-header">
  <nav class="nav">
    <a class="nav__brand" href="{r}{out_path(lang, 'index.html')}">
      <img src="{r}assets/confialy-mark.png" alt="Confialy">
      <span>Confialy</span>
    </a>
    <div class="nav__links">
      <a href="{r}{out_path(lang, 'index.html')}"{cur('home')}>{T(lang,'nav_home')}</a>
      {tier1_links}<a href="{r}{out_path(lang, 'products.html')}"{cur('more')}>{T(lang,'nav_more')}</a>
      <a href="{r}{out_path(lang, 'contact.html')}"{cur('contact')}>{T(lang,'nav_contact')}</a>
    </div>
    <div class="nav__actions">
      <div class="lang-switch">
        <a href="{r}{out_path('en', page_key)}"{' aria-current="true"' if lang=='en' else ''}>EN</a>
        <span class="lang-switch__sep">|</span>
        <a href="{r}{out_path('es', page_key)}"{' aria-current="true"' if lang=='es' else ''}>ES</a>
      </div>
      <a class="btn btn--primary btn--sm" href="{r}{out_path(lang, 'contact.html')}">{T(lang,'nav_cta')}</a>
      <button class="nav__toggle" aria-label="Menu" aria-expanded="false">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </nav>
</header>
"""

def footer(lang, page_key):
    depth = depth_for(lang, page_key)
    r = rel(depth)
    cat_links = ""
    for cat in CATEGORIES:
        items = "".join(
            f'<li><a href="{r}{out_path(lang, "products/"+slug+".html")}">{PRODUCTS[slug][lang]["name"]}</a></li>'
            for slug in cat["slugs"][:4]
        )
        cat_links += f'<div><h5>{cat[lang]["name"]}</h5><ul>{items}</ul></div>'
    company_links = f"""<div><h5>{T(lang,'footer_company')}</h5><ul>
      <li><a href="{r}{out_path(lang, 'about.html')}">{T(lang,'footer_about')}</a></li>
      <li><a href="{r}{out_path(lang, 'how-it-works.html')}">{T(lang,'footer_how')}</a></li>
      <li><a href="{r}{out_path(lang, 'contact.html')}">{T(lang,'footer_contact')}</a></li>
    </ul></div>"""
    return f"""<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      <div class="footer-brand"><img src="{r}assets/confialy-mark-light.png" alt=""><span>Confialy</span></div>
      <p>{T(lang,'footer_tagline')}</p>
    </div>
    {company_links}
    {cat_links}
  </div>
  <div class="container footer-bottom">
    <span>{T(lang,'footer_rights')}</span>
    <span>{T(lang,'footer_disclaimer')}</span>
  </div>
</footer>
<script src="{r}js/main.js"></script>
</body>
</html>"""

def trust_bar_html(lang):
    items = "".join(
        f'<div class="trust-item">{icon(k)}<div><strong>{t}</strong><span>{d}</span></div></div>'
        for k, t, d in TRUST_BAR[lang]
    )
    return f'<div class="trust-bar">{items}</div>'

def steps_html(lang):
    items = "".join(
        f'<div class="step"><div class="step__num">{icon(k)}</div><h4>{t}</h4><p>{d}</p></div>'
        for k, t, d in HOW_IT_WORKS[lang]
    )
    return f'<div class="steps">{items}</div>'

def positioning_pillars_html(lang):
    items = "".join(
        f'<div class="pillar"><div class="pillar__icon">{icon(k)}</div><h4>{t}</h4><p>{d}</p></div>'
        for k, t, d in POSITIONING_PILLARS[lang]
    )
    return f'<div class="pillars">{items}</div>'

def stat_strip_html(lang):
    items = "".join(
        f'<div class="stat-strip__item"><span class="stat-num">{n}</span><span class="stat-label">{lb}</span></div>'
        for n, lb in STATS[lang]
    )
    return f'<div class="stat-strip">{items}</div>'

def product_card(lang, slug):
    p = PRODUCTS[slug][lang]
    is_flagged = bool(p.get("scope_flag"))
    flag = f'<span class="product-card__flag">{T(lang, "scope_flag_label").rstrip(":")}</span>' if is_flagged else ""
    return f"""
        <a class="product-card{' product-card--flagged' if is_flagged else ''}" href="products/{slug}.html">
          {flag}
          <div class="product-card__icon">{icon(PRODUCTS[slug]['icon'])}</div>
          <h4>{p['display']}</h4>
          <p>{p['card_teaser']}</p>
          <span class="product-card__cta">{p['cta']} {ARROW_SVG}</span>
        </a>"""

# ------------------------------------------------------------- home page --

def build_home(lang):
    page_key = "index.html"
    r = rel(depth_for(lang, page_key))
    blocks = ""
    for cat in CATEGORIES:
        cards = "".join(product_card(lang, slug) for slug in cat["slugs"])
        blocks += f"""
      <div class="category-block">
        <div class="category-block__head"><h3>{cat[lang]['name']}</h3><span>&mdash; {cat[lang]['note']}</span></div>
        <div class="product-grid">{cards}
        </div>
      </div>"""

    meta_title = "Confialy — Compara Seguros en España de Forma Independiente" if lang == "es" else "Confialy — Independent Insurance Comparison in Spain"
    meta_desc = (
        "Confialy compara presupuestos reales de seguros de las principales aseguradoras de España en 15 líneas de producto. Independiente, transparente, sin presión."
        if lang == "es" else
        "Confialy compares real insurance quotes from Spain's leading insurers across 15 product lines. Independent, transparent, no pressure."
    )
    products_h2 = (
        "Sea lo que sea lo que necesites asegurar, te lo comparamos" if lang == "es"
        else "Whatever you need to insure, we'll compare it for you"
    )
    products_eyebrow = "Los 15 seguros" if lang == "es" else "All 15 product lines"

    html = head(lang, page_key, meta_title, meta_desc)
    html += header(lang, page_key, "home")
    html += f"""
<main>
  <section class="hero">
    <div class="container hero__grid">
      <div>
        <span class="eyebrow">{"Comparación de seguros, honesta" if lang=="es" else "Insurance comparison, made honest"}</span>
        <h1>{T(lang,'home_h1')}</h1>
        {swoosh()}
        <p class="hero__lede">{T(lang,'home_subline')}</p>
        <div class="hero__actions">
          <a class="btn btn--primary" href="products.html">{"Ver nuestros seguros" if lang=="es" else "See our products"}</a>
          <a class="btn btn--outline" href="contact.html">{"Habla con una persona real" if lang=="es" else "Talk to a real person"}</a>
        </div>
      </div>
      <div class="hero__art">
        <div class="hero__photo-frame">
          <img src="{r}assets/photos/home-hero.jpg" alt="{"Familia sonriendo junta en casa" if lang=="es" else "Family smiling together at home"}" loading="eager">
        </div>
      </div>
    </div>
    <div class="hero__divider">
      <svg viewBox="0 0 1440 80" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg"><path d="M0 40 C 240 90, 480 0, 720 40 C 960 80, 1200 10, 1440 40 L1440 80 L0 80 Z" fill="#FBF6EC"/></svg>
    </div>
  </section>

  <section class="section--white section--tight">
    <div class="container">{stat_strip_html(lang)}</div>
  </section>

  <section class="section--sand section--tight">
    <div class="container">{trust_bar_html(lang)}</div>
  </section>

  <section class="section section--forest">
    <div class="container positioning">
      <span class="eyebrow">{T(lang,'eyebrow_why')}</span>
      <h2>{"Un bróker que de verdad está de tu lado" if lang=="es" else "A broker that's actually on your side"}</h2>
      {swoosh(True)}
      <p>{"La mayoría de webs de seguros te venden el plan de una sola aseguradora. Confialy no." if lang=="es" else "Most insurance sites sell you one insurer's own plan. Confialy doesn't."}</p>
      {positioning_pillars_html(lang)}
    </div>
  </section>

  <section class="section section--white">
    <div class="container">
      <span class="eyebrow">{products_eyebrow}</span>
      <h2>{products_h2}</h2>
      {swoosh()}
      {blocks}
    </div>
  </section>

  <section class="section section--sand">
    <div class="container">
      <span class="eyebrow">{T(lang,'eyebrow_how')}</span>
      <h2>{T(lang,'h2_how_home')}</h2>
      {swoosh()}
      {steps_html(lang)}
    </div>
  </section>

  <section class="section section--white">
    <div class="container">
      <div class="cta-band">
        <span class="eyebrow" style="background:rgba(255,255,255,0.12);color:#D9E9DF;">{"Sin obligación de compra" if lang=="es" else "No obligation to buy"}</span>
        <h3>{"Pide presupuestos reales, entiende exactamente qué significan, decide a tu ritmo" if lang=="es" else "Get real quotes, understand exactly what they mean, decide on your own terms"}</h3>
        <p>{T(lang,'cta_row_note')}</p>
        <div class="btn-row">
          <a class="btn btn--on-dark" href="products.html">{"Ver todos los seguros" if lang=="es" else "Browse all products"}</a>
          <a class="btn btn--ghost-on-dark" href="contact.html">{T(lang,'nav_contact')}</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += footer(lang, page_key)
    write(out_path(lang, page_key), html)

# --------------------------------------------------------- products page --

def build_products_index(lang):
    page_key = "products.html"
    blocks = ""
    for cat in CATEGORIES:
        cards = "".join(product_card(lang, slug) for slug in cat["slugs"])
        blocks += f"""
      <div class="category-block">
        <div class="category-block__head"><h3>{cat[lang]['name']}</h3><span>&mdash; {cat[lang]['note']}</span></div>
        <div class="product-grid">{cards}
        </div>
      </div>"""
    meta_title = (
        "Todos los Seguros en España | Confialy — Comparación Independiente"
        if lang == "es" else
        "All Insurance Products in Spain | Confialy — Independent Comparison"
    )
    meta_desc = (
        "Descubre los 15 tipos de seguro que compara Confialy en España: salud, dental, hogar, coche, moto, negocio, mascota, vida, y más."
        if lang == "es" else
        "Browse all 15 insurance lines Confialy compares in Spain: health, dental, home, car, motorcycle, business, pet, life, and more."
    )
    html = head(lang, page_key, meta_title, meta_desc)
    html += header(lang, page_key, "more")
    html += f"""
<main>
  <section class="section section--white" style="padding-bottom:0;">
    <div class="container">
      <span class="eyebrow">{T(lang,'products_index_eyebrow')}</span>
      <h1>{T(lang,'products_index_h1')}</h1>
      {swoosh()}
      <p style="max-width:62ch;color:var(--text-soft)">{T(lang,'products_index_lede')}</p>
    </div>
  </section>
  <section class="section section--white">
    <div class="container">{blocks}</div>
  </section>
</main>
"""
    html += footer(lang, page_key)
    write(out_path(lang, page_key), html)

# ---------------------------------------------------------- product page --

def build_product(lang, slug):
    prod = PRODUCTS[slug]
    p = prod[lang]
    page_key = f"products/{slug}.html"
    r = rel(depth_for(lang, page_key))

    faqs_html = ""
    faq_entries = []
    for q, a in p["faqs"]:
        faqs_html += f'\n        <details class="faq-item"><summary>{q}</summary><p>{a}</p></details>'
        qq, aa = q.replace('"', '\\"'), a.replace('"', '\\"')
        faq_entries.append('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (qq, aa))
    faq_schema = '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ",".join(faq_entries) + "]}"

    coverage_list = "".join(
        f'<li>{CHECK_SVG}<span><strong>{item}.</strong> {desc}</span></li>'
        for item, desc in p["coverage"]
    )
    personas_html = "".join(
        f'<div class="persona-card"><div class="persona-card__icon">{icon(prod["icon"])}</div><p>{persona}</p></div>'
        for persona in p["personas"]
    )
    why_bullets_html = "".join(
        f'<div class="feature-col"><span class="feature-col__num">{i:02d}</span><div><p>{b}</p></div></div>'
        for i, b in enumerate(p["why_bullets"], 1)
    )

    scope_flag_html = ""
    if p.get("scope_flag"):
        scope_flag_html = f"""
      <div class="badge-flag">{icon('badge-check')}<span><strong>{T(lang,'scope_flag_label')}</strong> {p['scope_flag']}</span></div>"""

    active = slug if slug in TIER1 else "more"
    html = head(lang, page_key, p["meta_title"], p["meta_desc"])
    html += header(lang, page_key, active)
    html += f"""
<main>
  <section class="section section--white" style="padding-bottom:0;">
    <div class="container">
      <p class="breadcrumb"><a href="../index.html">{T(lang,'breadcrumb_home')}</a> / <a href="../products.html">{T(lang,'breadcrumb_products')}</a> / {p['display']}</p>
      {scope_flag_html}
      <div class="hero__grid" style="align-items:flex-start;">
        <div>
          <span class="eyebrow">{p['eyebrow']}</span>
          <h1>{p['h1']}</h1>
          {swoosh()}
          <p class="hero__lede">{p['sub']}</p>
          <div class="hero__actions">
            <a class="btn btn--primary" href="../contact.html">{p['cta']}</a>
          </div>
          <p class="hero__note">{T(lang,'cta_row_note')}</p>
        </div>
        {hero_scene(lang, slug, r)}
      </div>
    </div>
  </section>

  <section class="section section--sand">
    <div class="container">
      <span class="eyebrow">{T(lang,'eyebrow_why')}</span>
      <h2>{T(lang,'h2_why_tpl').format(display=p['display'])}</h2>
      {swoosh()}
      <p style="max-width:64ch;color:var(--text-soft)">{p['best_fit']}</p>
      <div class="feature-cols">{why_bullets_html}</div>
    </div>
  </section>

  <section class="section section--white">
    <div class="container">
      <span class="eyebrow">{T(lang,'eyebrow_who')}</span>
      <h2>{T(lang,'h2_who_tpl').format(display=p['display'])}</h2>
      {swoosh()}
      <div class="personas">{personas_html}</div>
    </div>
  </section>

  <section class="section section--sand">
    <div class="container">
      <span class="eyebrow">{T(lang,'eyebrow_coverage')}</span>
      <h2>{T(lang,'h2_coverage_tpl').format(display=p['display'])}</h2>
      {swoosh()}
      <div class="coverage-grid">
        <ul class="coverage-list">{coverage_list}</ul>
        <div class="check-callout">
          <h4>{icon('badge-check')} {T(lang,'watch_out_label')}</h4>
          <p>{p['watch_out']}</p>
        </div>
      </div>
      <p class="disclaimer">{STANDARD_DISCLAIMER[lang]}</p>
    </div>
  </section>

  <section class="section section--white">
    <div class="container">
      <span class="eyebrow">{T(lang,'eyebrow_how')}</span>
      <h2>{T(lang,'h2_how_product_tpl').format(display=p['display'])}</h2>
      {swoosh()}
      {steps_html(lang)}
    </div>
  </section>

  <section class="section section--sand">
    <div class="container">
      <div class="testimonial-slot">
        <div class="testimonial-slot__icon">{icon('message')}</div>
        <strong>{T(lang,'testimonial_title')}</strong>
        <span>{T(lang,'testimonial_body_prefix')} {p['display'].lower()} {T(lang,'testimonial_body_suffix')}</span>
      </div>
    </div>
  </section>

  <section class="section section--white">
    <div class="container">
      <span class="eyebrow">{T(lang,'eyebrow_faq')}</span>
      <h2>{T(lang,'h2_faq_tpl').format(display=p['display'])}</h2>
      {swoosh()}
      <div class="faq-list">{faqs_html}
      </div>
    </div>
  </section>

  <section class="section section--sand">
    <div class="container">
      <div class="cta-band">
        <h3>{p['final_cta']}</h3>
        <div class="btn-row">
          <a class="btn btn--on-dark" href="../contact.html">{p['cta']}</a>
        </div>
      </div>
    </div>
  </section>
</main>
<script type="application/ld+json">{faq_schema}</script>
"""
    html += footer(lang, page_key)
    write(out_path(lang, page_key), html)

# ------------------------------------------------------------ about page --

def build_about(lang):
    page_key = "about.html"
    if lang == "es":
        title = "Sobre Confialy | Comparación Independiente de Seguros en España"
        desc = "Confialy es un bróker y comparador de seguros independiente en España. Descubre a quién comparamos, cómo nos pagan, y por qué no publicamos reseñas falsas."
        body = """
      <h1>No somos la aseguradora. Estamos de tu lado.</h1>
      {swoosh}
      <p class="hero__lede">Confialy es una plataforma independiente de comparación y contratación de seguros para personas que viven en España — españoles y residentes extranjeros por igual. Comparamos presupuestos reales en 15 líneas de producto, desde salud y hogar hasta defensa jurídica y ciberriesgos, rápido y sin complicaciones, para que decidas con tranquilidad.</p>

      <h2 style="margin-top:48px;">Por qué existimos</h2>
      <p>Comparar seguros en España suele significar cinco llamadas, cinco explicaciones distintas, y una póliza llena de jerga que se supone que debes confiar sin más. Creamos Confialy para que sea un formulario, presupuestos reales uno junto a otro, y respuestas en lenguaje claro sobre lo que realmente estás comprando — incluyendo lo que un plan NO cubre, no solo lo que sí.</p>

      <h2 style="margin-top:36px;">En qué nos diferenciamos de la web de una aseguradora</h2>
      <p>La web de una aseguradora está hecha para venderte el plan de esa aseguradora. Confialy es un bróker: te mostramos ofertas de varias aseguradoras y te dejamos compararlas con honestidad. Nos mantenemos neutrales en cada página, salvo que exista un acuerdo firmado y confirmado con una aseguradora para esa línea concreta.</p>

      <h2 style="margin-top:36px;">Nuestra política de testimonios</h2>
      <p>Verás espacios reservados donde eventualmente irán las opiniones de clientes. Es intencionado — no publicamos citas inventadas. Una marca construida sobre «estamos de tu lado» no puede arriesgarse a que la pillen con una reseña falsa, así que esos espacios quedan vacíos hasta que se llenen con opiniones reales.</p>

      <h2 style="margin-top:36px;">A quién ayudamos</h2>
      <ul style="list-style:disc;padding-left:22px;">
        <li style="margin-bottom:8px;">Españoles que comparan precios de renovación, incluidas personas que prefieren una conversación telefónica a un proceso totalmente digital.</li>
        <li style="margin-bottom:8px;">Residentes extranjeros que ya viven en España, buscando explicaciones claras y bilingües de productos que no conocen.</li>
      </ul>

      <div class="cta-band" style="margin-top:48px;">
        <h3>¿Dudas antes de comparar?</h3>
        <p>Habla con una persona real en español o inglés — sin presión, sin obligación de compra.</p>
        <div class="btn-row"><a class="btn btn--on-dark" href="contact.html">Contáctanos</a></div>
      </div>
"""
    else:
        title = "About Confialy | Independent Insurance Comparison in Spain"
        desc = "Confialy is an independent insurance broker and comparison platform for Spain. Learn who we compare for, how we're paid, and why we don't publish fake reviews."
        body = """
      <h1>We're not the insurance company. We're on your side.</h1>
      {swoosh}
      <p class="hero__lede">Confialy is an independent insurance comparison and purchase platform for people living in Spain — Spanish locals and foreign residents alike. We compare real quotes across 15 product lines, from health and home to legal defense and cyber risk, fast and without the runaround, so you can decide with peace of mind.</p>

      <h2 style="margin-top:48px;">Why we exist</h2>
      <p>Comparing insurance in Spain usually means five phone calls, five different explanations, and a policy full of jargon you're expected to just trust. We built Confialy so it's one form, real quotes side by side, and plain-language answers about what you're actually buying — including what a plan doesn't cover, not just what it does.</p>

      <h2 style="margin-top:36px;">How we're different from an insurer's own site</h2>
      <p>An insurer's website is built to sell you that insurer's plan. Confialy is a broker: we show offers from multiple insurers and let you compare them honestly. We stay carrier-neutral on every page unless a specific partnership is signed and confirmed for that product line.</p>

      <h2 style="margin-top:36px;">Our testimonial policy</h2>
      <p>You'll notice placeholders where customer reviews will eventually go. That's intentional — we don't publish invented quotes. A brand built on “we're on your side” can't risk being caught with a fake review, so those slots stay empty until they're filled with real feedback.</p>

      <h2 style="margin-top:36px;">Who we help</h2>
      <ul style="list-style:disc;padding-left:22px;">
        <li style="margin-bottom:8px;">Spanish locals comparing renewal prices, including people who prefer a phone conversation to a fully digital process.</li>
        <li style="margin-bottom:8px;">Foreign residents already living in Spain, looking for clear, bilingual explanations of unfamiliar products.</li>
      </ul>

      <div class="cta-band" style="margin-top:48px;">
        <h3>Questions before you compare?</h3>
        <p>Reach a real person in Spanish or English — no pressure, no obligation to buy.</p>
        <div class="btn-row"><a class="btn btn--on-dark" href="contact.html">Contact us</a></div>
      </div>
"""
    html = head(lang, page_key, title, desc)
    html += header(lang, page_key, "")
    html += f"""
<main>
  <section class="section section--white">
    <div class="container" style="max-width:820px;">
      {body.format(swoosh=swoosh())}
    </div>
  </section>
</main>
"""
    html += footer(lang, page_key)
    write(out_path(lang, page_key), html)

# ------------------------------------------------------- how-it-works pg --

def build_how_it_works(lang):
    page_key = "how-it-works.html"
    if lang == "es":
        title = "Cómo Funciona Confialy | Compara y Contrata Seguros en España"
        desc = "Descubre cómo funciona el proceso de presupuesto, comparación y contratación de Confialy, desde tu primer formulario hasta una póliza activa en tu panel."
        h1 = "De un Presupuesto a una Póliza Activa, en Seis Pasos Claros"
        lede = "El mismo proceso aplica a las 15 líneas de producto. Nada aquí promete emisión instantánea ni nombra un proveedor de pago — esos detalles dependen de la aseguradora y el plan que elijas, y se muestran antes de comprar."
        nodes = [
            ("1. Formulario de presupuesto", "Preguntas claras, una por pantalla. El progreso se guarda automáticamente como borrador para retomarlo después."),
            ("2. Comparación de presupuestos", "Ofertas reales de varias aseguradoras — precio, puntos clave de cobertura, nombre de la aseguradora — una junto a otra."),
            ("3. Elige tu plan", "Se repasan los puntos clave de cobertura y el aviso legal estándar antes de pasar al pago."),
            ("4. Paga de forma segura", "Introduce tus datos de pago para completar la compra."),
            ("5. Confirmación de la póliza", "Confirmamos en cuanto esté lista y te avisamos por email — consulta el estado en tu panel cuando quieras."),
            ("6. Tu panel", "Borradores que puedes retomar, y pólizas activas con sus documentos, en un solo lugar."),
        ]
    else:
        title = "How Confialy Works | Get an Independent Insurance Quote in Spain"
        desc = "See how Confialy's quote, comparison and purchase flow works, from your first form to an active policy in your dashboard."
        h1 = "From a Quote to an Active Policy, in Six Clear Steps"
        lede = "The same flow applies to all 15 product lines. Nothing here promises instant issuance or names a payment provider — those details depend on the insurer and plan you choose, and are shown before you buy."
        nodes = [
            ("1. Quote form", "Plain questions, one per screen. Progress saves automatically as a draft you can resume later."),
            ("2. Compare quotes", "Real offers from multiple insurers — price, coverage highlights, insurer name — side by side."),
            ("3. Choose your plan", "Coverage highlights and the standard disclaimer are restated before you move to payment."),
            ("4. Pay securely", "Enter your payment details to complete your purchase."),
            ("5. Policy confirmation", "We confirm as soon as it's ready and email you — check status anytime in your dashboard."),
            ("6. Your dashboard", "Drafts you can resume, and active policies with documents, in one place."),
        ]
    nodes_html = "".join(
        f'<div class="flow-node"><span>{"Paso" if lang=="es" else "Step"}</span><h4 style="font-size:1rem;margin:0 0 6px;">{t}</h4><p>{d}</p></div>'
        for t, d in nodes
    )
    html = head(lang, page_key, title, desc)
    html += header(lang, page_key, "")
    html += f"""
<main>
  <section class="section section--white" style="padding-bottom:0;">
    <div class="container">
      <span class="eyebrow">{"El proceso de compra" if lang=="es" else "The purchase flow"}</span>
      <h1>{h1}</h1>
      {swoosh()}
      <p style="max-width:62ch;color:var(--text-soft)">{lede}</p>
    </div>
  </section>
  <section class="section section--white">
    <div class="container"><div class="flow-strip">{nodes_html}</div></div>
  </section>
  <section class="section section--sand">
    <div class="container">
      <span class="eyebrow">{T(lang,'eyebrow_how')}</span>
      <h2>{"La versión corta" if lang=="es" else "The short version"}</h2>
      {swoosh()}
      {steps_html(lang)}
    </div>
  </section>
  <section class="section section--white">
    <div class="container">
      <div class="cta-band">
        <h3>{"¿Listo para ver presupuestos reales?" if lang=="es" else "Ready to see real quotes?"}</h3>
        <div class="btn-row">
          <a class="btn btn--on-dark" href="products.html">{"Ver seguros" if lang=="es" else "Browse products"}</a>
          <a class="btn btn--ghost-on-dark" href="contact.html">{"Habla con nosotros" if lang=="es" else "Talk to us"}</a>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += footer(lang, page_key)
    write(out_path(lang, page_key), html)

# ----------------------------------------------------------- contact page --

def build_contact(lang):
    page_key = "contact.html"
    options = "".join(f'<option value="{PRODUCTS[s][lang]["display"]}">{PRODUCTS[s][lang]["display"]}</option>' for s in PRODUCTS)
    m = MESSAGES[lang]
    if lang == "es":
        title = "Contacta con Confialy | Habla con una Persona Real sobre tu Seguro"
        desc = "¿Tienes una pregunta antes de comparar o comprar? Contacta con Confialy en español o inglés — sin presión, sin obligación de compra."
        h1 = "Habla con una Persona Real, no con un Guión de Chatbot"
        lede = "¿Pregunta sobre un presupuesto, un producto que no entiendes del todo, o algo completamente distinto? Escríbenos — no hay obligación de comprar nada."
    else:
        title = "Contact Confialy | Talk to a Real Person About Your Insurance"
        desc = "Have a question before you compare or buy? Contact Confialy in Spanish or English — no pressure, no obligation to buy."
        h1 = "Talk to a Real Person, Not a Chatbot Script"
        lede = "Question about a quote, a product you don't fully understand, or something else entirely? Send us a message — there's no obligation to buy anything."

    html = head(lang, page_key, title, desc)
    html += header(lang, page_key, "contact")
    html += f"""
<main>
  <section class="section section--white">
    <div class="container">
      <span class="eyebrow">{T(lang,'nav_contact')}</span>
      <h1>{h1}</h1>
      {swoosh()}
      <p style="max-width:62ch;color:var(--text-soft)">{lede}</p>

      <div class="contact-layout" style="margin-top:36px;">
        <div class="contact-info">
          <h3>{"Habla con nosotros" if lang=="es" else "Get in touch"}</h3>
          <p>{"Respondemos en español o inglés, normalmente en un día laborable." if lang=="es" else "We reply in Spanish or English, usually within one business day."}</p>
          <div class="contact-info__item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 6h18v12H3z"/><path d="m3 7 9 6 9-6"/></svg>
            <div><strong>{"Correo" if lang=="es" else "Email"}</strong><br><a href="mailto:contact@confialy.com">contact@confialy.com</a></div>
          </div>
          <div class="contact-info__item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>
            <div><strong>{"Tiempo de respuesta" if lang=="es" else "Response time"}</strong><br>{"En 1 día laborable, normalmente antes." if lang=="es" else "Within 1 business day, usually sooner."}</div>
          </div>
          <div class="contact-info__item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M12 21s-7-4.6-7-10a7 7 0 0 1 14 0c0 5.4-7 10-7 10Z"/><circle cx="12" cy="11" r="2.4"/></svg>
            <div><strong>{"Ubicación" if lang=="es" else "Based in"}</strong><br>{"España — atendemos a residentes en todo el país." if lang=="es" else "Spain — serving residents nationwide."}</div>
          </div>
        </div>

        <div class="form-card">
          <div id="form-msg" class="form-msg" role="status"></div>
          <form id="contact-form" data-endpoint="{FORM_ENDPOINT}"
                data-msg-ok="{m['ok']}" data-msg-not-connected="{m['not_connected']}"
                data-msg-server-err="{m['server_err']}" data-msg-sending="{m['sending']}" data-msg-submit="{m['submit']}">
            <input class="honeypot" type="text" name="company_website" tabindex="-1" autocomplete="off">
            <div class="form-row">
              <div class="field">
                <label for="first_name">{"Nombre" if lang=="es" else "First name"}</label>
                <input id="first_name" name="first_name" type="text" required autocomplete="given-name">
              </div>
              <div class="field">
                <label for="last_name">{"Apellidos" if lang=="es" else "Last name"}</label>
                <input id="last_name" name="last_name" type="text" required autocomplete="family-name">
              </div>
            </div>
            <div class="form-row">
              <div class="field">
                <label for="email">{"Correo electrónico" if lang=="es" else "Email"}</label>
                <input id="email" name="email" type="email" required autocomplete="email">
              </div>
              <div class="field">
                <label for="phone">{"Teléfono" if lang=="es" else "Phone"} <span class="hint">({"opcional" if lang=="es" else "optional"})</span></label>
                <input id="phone" name="phone" type="tel" autocomplete="tel">
              </div>
            </div>
            <div class="field">
              <label for="product">{"¿Sobre qué seguro es tu consulta?" if lang=="es" else "Which product is this about?"}</label>
              <select id="product" name="product">
                <option value="">{"No estoy seguro / pregunta general" if lang=="es" else "Not sure / general question"}</option>
                {options}
              </select>
            </div>
            <div class="field">
              <label for="message">{"Tu mensaje" if lang=="es" else "Your message"}</label>
              <textarea id="message" name="message" required placeholder="{"Cuéntanos qué necesitas..." if lang=="es" else "Tell us a bit about what you need..."}"></textarea>
            </div>
            <label class="consent">
              <input type="checkbox" required>
              <span>{"Acepto que Confialy me contacte sobre mi consulta por correo o teléfono. Sin obligación de compra." if lang=="es" else "I agree that Confialy can contact me about my enquiry by email or phone. No obligation to buy."}</span>
            </label>
            <button class="btn btn--primary btn--full" type="submit">{m['submit']}</button>
          </form>
        </div>
      </div>
    </div>
  </section>
</main>
"""
    html += footer(lang, page_key)
    write(out_path(lang, page_key), html)

# --------------------------------------------------------------- sitemap --

def build_sitemap():
    urls = []
    for lang in LANGS:
        for key in ["index.html", "products.html", "about.html", "how-it-works.html", "contact.html"]:
            urls.append(out_path(lang, key))
        for slug in PRODUCTS:
            urls.append(out_path(lang, f"products/{slug}.html"))
    entries = "\n".join(f"  <url><loc>{DOMAIN}/{u}</loc></url>" for u in urls)
    xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{entries}\n</urlset>\n'
    write("sitemap.xml", xml)

# ---------------------------------------------------------------- runner --

def build_all():
    for lang in LANGS:
        build_home(lang)
        build_products_index(lang)
        for slug in PRODUCTS:
            build_product(lang, slug)
        build_about(lang)
        build_how_it_works(lang)
        build_contact(lang)
    build_sitemap()

if __name__ == "__main__":
    build_all()
