# Confialy website — handoff notes

Static site: plain HTML/CSS/JS, no build step needed to view or host it.
Open `index.html` directly, or upload the whole folder to any static host
(Netlify, Vercel, Cloudflare Pages, S3+CloudFront, your own server, etc.).

## 1. Contact form → contact@confialy.com (action required)

The form on `contact.html` is fully built (fields, validation, spam
honeypot, success/error states) but it currently points at a **placeholder**
endpoint, because I can't create a mailbox-connected backend or send
mail on your behalf without your own credentials.

To make submissions actually arrive in contact@confialy.com, the fastest
option for a static site is a form-to-email service:

1. Create a free account at **formspree.io** (or Getform, Web3Forms — any
   similar service works the same way).
2. Create a new form and set its destination to `contact@confialy.com`.
3. Copy the form endpoint it gives you, e.g. `https://formspree.io/f/abcd1234`.
4. Open `contact.html`, find this line near the top of the `<form>` tag:
   `data-endpoint="https://formspree.io/f/YOUR_FORM_ID"`
   and replace `YOUR_FORM_ID` with your real ID (or the full URL your
   provider gives you).
5. Also update `FORM_ENDPOINT` at the top of `build.py` if you regenerate
   the site later, so it stays in sync.

Until this is set, submitting the form shows a message explaining it isn't
connected yet, instead of failing silently.

**Alternative:** if you'd rather receive mail via your own mail server or a
serverless function (e.g. a small AWS Lambda / Cloudflare Worker that calls
an email API), point `data-endpoint` at that URL instead — the form already
POSTs standard `FormData`, so most backends can accept it with minimal changes.

## 2. Regenerating the site

All product copy lives in `build_data.py` (one dict per product line — H1,
personas, coverage, FAQs, etc.). `build.py` renders every page from it.

```
python3 build.py
```

Edit `build_data.py`, re-run the script, and every page rebuilds
consistently — you never have to hand-edit repeated HTML across 15 pages.

## 3. Decisions I made by default (flag/confirm with the product lead)

- **Content language:** English, using the approved v2 master copy from
  `Confialy_Product_Page_Content_EN_v2.md`. The project docs list the
  master content language as an open question — I didn't want to risk
  mistranslating the persuasion-tuned copy, so I built the English version
  first. A Spanish version (and a language switcher) can be generated the
  same way once ES copy is approved by a human reviewer, especially given
  the older-demographic audience.
- **Seguro de Transporte** page is flagged on the page itself (an amber
  banner) as scope-unconfirmed, per the project docs.
- **Payment/issuance copy:** kept neutral everywhere ("pay securely",
  "we'll confirm as soon as it's ready") — no named payment provider, no
  promised instant issuance, per the open technical questions.
- **No named insurers, no VISA/NIE claim** anywhere on the site.
- **Testimonials:** every product page has a clearly marked, empty
  placeholder slot — no fabricated quotes.
- Trust-bar wording and any stats are the same placeholder wording from
  the content manual — confirm final numbers with the product lead before
  launch, per the manual's own checklist.

## 4. SEO / GEO basics included

- Per-page `<title>`, meta description, canonical URL, Open Graph tags.
- `FAQPage` JSON-LD schema on every product page (from the same FAQ
  content shown on-page — nothing invisible or hidden text).
- `sitemap.xml` and `robots.txt` at the site root.
- Semantic HTML: one `<h1>` per page, real `<section>`/`<nav>`/`<footer>`
  landmarks, `<details>` for FAQs (readable without JS).
- Everything server-rendered as plain HTML — no client-side rendering
  required for content to be crawlable.

## 5. Structure

```
index.html            homepage
products.html         all 15 lines, grouped by category
products/<slug>.html  one page per line (15 total)
about.html
how-it-works.html
contact.html          the lead form
css/style.css         design system (tokens, components)
js/main.js            nav toggle + form submit handling
assets/               your logo files
sitemap.xml, robots.txt
build_data.py, build.py   the generator — edit data, re-run to rebuild
```
