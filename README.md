# PharmaToxAI web

Corporate website for PharmaToxAI, built with Jekyll and published with GitHub Pages.

The site is intentionally data-driven so routine scientific and corporate updates do not require editing the layout.

## Main content sources

- `_data/company.yml` — company metadata, hero copy, contact and corporate LinkedIn
- `_data/navigation.yml` — navigation
- `_data/services.yml` — solutions and service cards
- `_data/team.yml` — team profiles
- `_data/publications.csv` — publication database
- `_whitepapers/` — Markdown white papers
- `index.html` — home-page structure and longer fixed copy

See [`CONTENT_GUIDE.md`](CONTENT_GUIDE.md) for the editing workflow.

## Jekyll structure

- `_layouts/default.html` — global HTML shell
- `_layouts/whitepaper.html` — white paper page layout
- `_includes/` — reusable header, footer, logo and team cards
- `publications.html` — automatically generated publication index
- `whitepapers.html` — automatically generated white-paper index
- `styles.css` — original visual system
- `jekyll.css` — Jekyll/content-page extensions
- `script.js` — navigation and reveal interactions

## Local preview

```bash
bundle install
bundle exec jekyll serve --livereload
```

Open `http://127.0.0.1:4000`.

## Deployment

GitHub Pages builds the Jekyll site from `main`. The custom domain is preserved by `CNAME` as `pharmatoxai.ar`.
