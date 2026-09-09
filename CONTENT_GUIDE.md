# PharmaToxAI content guide

The site is built with Jekyll so routine updates do not require editing page layouts.

## What to edit

| Content | File |
| --- | --- |
| Company name, tagline, contact, LinkedIn, hero text | `_data/company.yml` |
| Main navigation | `_data/navigation.yml` |
| Solutions/services | `_data/services.yml` |
| Team profiles | `_data/team.yml` |
| Publications | `_data/publications.csv` |
| White papers | `_whitepapers/*.md` |
| Main page copy outside structured data | `index.html` |
| Site design | `styles.css` and `jekyll.css` |

## Add a publication

Add one row to `_data/publications.csv`.

```csv
id,title,journal,year,doi,members
p009,"Paper title",Journal Name,2027,https://doi.org/...,casal|digiusto
```

`members` uses the IDs defined in `_data/team.yml` separated by `|`.

The home page automatically shows only the three newest records as a preview. `/publications/` contains the complete curated list used by the site. Publications are not repeated inside the team cards.

## Add or edit a team member

Edit `_data/team.yml`. No HTML changes are required.

```yaml
- id: surname
  initials: AB
  name: Dr. Example Person
  role: Main expertise · secondary expertise
  expertise: Short scientific description.
  linkedin: https://www.linkedin.com/in/...
  conicet: https://bicyt.conicet.gov.ar/...
  email: name@example.org
```

The public team cards show the scientific description plus LinkedIn and CONICET profile links. General inquiries are routed through the PharmaToxAI contact email in `_data/company.yml`.

## Add a service

Edit `_data/services.yml`. A service can optionally include an image and attribution.

```yaml
- number: "05"
  title: New service
  description: Short description.
  features:
    - Feature one
    - Feature two
  image: https://...
  image_alt: Descriptive alt text
  credit_label: Author / Source
  credit_url: https://...
```

## Publish a white paper

Copy `_templates/whitepaper-template.md` into `_whitepapers/`, rename it, replace every placeholder and set `published: true`.

```yaml
---
layout: whitepaper
title: Predictive toxicology in early development
summary: Short summary for the index.
authors:
  - Juan José Casal
date: 2026-09-07
pdf: /assets/whitepapers/predictive-toxicology.pdf
published: true
---
```

Write the body in Markdown. If there is a downloadable PDF, place it under `assets/whitepapers/` and reference it in `pdf`.

The internal template is outside the public collection and is excluded from the Jekyll build. White-paper links are hidden from the public navigation until at least one published white paper exists.

## Deploy

Routine workflow:

1. Edit CSV, YAML or Markdown.
2. Commit and push to `main`.
3. GitHub Pages runs Jekyll and publishes the generated static site.

The custom domain remains `pharmatoxai.ar` through the existing `CNAME` file.

## Local preview

Ruby and Bundler are only needed if you want a local preview.

```bash
bundle install
bundle exec jekyll serve --livereload
```

Then open `http://127.0.0.1:4000`.
