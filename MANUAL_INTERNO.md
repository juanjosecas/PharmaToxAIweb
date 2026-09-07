# Manual interno de mantenimiento — PharmaToxAIweb

> Documento de uso interno para mantener el contenido del sitio. No forma parte de las páginas públicas generadas por Jekyll.

El sitio usa **Jekyll + GitHub Pages**. La arquitectura separa el contenido del diseño para que las actualizaciones habituales no requieran editar HTML complejo ni CSS.

```text
contenido editable
    ↓
_data/*.yml
_data/publications.csv
_whitepapers/*.md
index.html (solo contenido estructural)
    ↓
Jekyll
    ↓
_layouts + _includes + CSS
    ↓
HTML estático
    ↓
https://pharmatoxai.ar
```

La regla general es: **si cambia información, editar `_data/`, `_whitepapers/` o el texto de `index.html`; si cambia la apariencia global, editar layouts/includes/CSS.**

---

## 1. Mapa rápido

| Quiero cambiar | Archivo principal |
| --- | --- |
| Nombre, tagline, descripción, ubicación, email, LinkedIn, hero | `_data/company.yml` |
| Menú superior | `_data/navigation.yml` |
| Servicios / soluciones | `_data/services.yml` |
| Integrantes del equipo | `_data/team.yml` |
| Publicaciones científicas | `_data/publications.csv` |
| White papers | `_whitepapers/*.md` |
| PDFs de white papers | `assets/whitepapers/` |
| Imágenes propias | `assets/images/` |
| Texto estructural de la home | `index.html` |
| Página completa de publicaciones | `publications.html` |
| Índice de white papers | `whitepapers.html` |
| Diseño general | `styles.css` y `jekyll.css` |
| Header/footer/componentes reutilizables | `_includes/` |
| Layouts de páginas | `_layouts/` |
| Dominio, idioma, colecciones | `_config.yml` |
| Dominio personalizado | `CNAME` |
| Navegación móvil/animaciones | `script.js` |

---

## 2. Flujo normal

Para una actualización corriente:

1. Editar el archivo correspondiente.
2. Guardar.
3. Hacer commit.
4. Hacer push a `main`.
5. GitHub Pages ejecuta Jekyll automáticamente.
6. Verificar el workflow `pages build and deployment` en GitHub Actions.

Ejemplo:

```bash
git add _data/publications.csv
git commit -m "Add new publication"
git push origin main
```

No hay un comando de despliegue adicional.

---

## 3. Información general — `_data/company.yml`

Este archivo contiene los datos corporativos reutilizables.

Ejemplo:

```yaml
name: PharmaToxAI
tagline: Modern preclinical. Ethical by design.
short_description: PharmaToxAI integrates computational toxicology...
location: Buenos Aires, Argentina
affiliation: IFIBIO Houssay · UBA–CONICET
founded: 2025
industry: Research Services
email: jcasal@fmed.uba.ar
linkedin: https://ar.linkedin.com/company/pharmatoxai
hero_eyebrow: AI-driven · in silico · in vitro · human-relevant
hero_title: From molecular predictions to biological evidence.
hero_cta_primary: Explore our solutions
hero_cta_secondary: Discuss a compound
```

### Cambiar el título principal

```yaml
hero_title: Nuevo título
```

### Cambiar tagline

```yaml
tagline: Nuevo slogan
```

### Cambiar email general

```yaml
email: contacto@pharmatoxai.ar
```

### Cambiar LinkedIn corporativo

```yaml
linkedin: https://www.linkedin.com/company/...
```

### YAML: regla importante

La indentación se hace con espacios, nunca tabs. Si un texto contiene `:` y puede ser ambiguo, usar comillas:

```yaml
short_description: "PharmaToxAI: predictive toxicology and human models"
```

---

## 4. Servicios — `_data/services.yml`

Cada servicio es un bloque YAML.

```yaml
- number: "03"
  title: Human cellular validation
  description: Experimental evaluation in human cell systems when computational predictions require biological confirmation.
  features:
    - 2D cellular models
    - 3D cellular models
    - Viability and functional endpoints
  image: https://images.pexels.com/...
  image_alt: Cell culture work in a laboratory using multiwell plates and pipetting
  credit_label: CDC / Pexels
  credit_url: https://www.pexels.com/...
```

### Editar un servicio

Cambiar `title`, `description` o elementos de `features`.

### Agregar un servicio

Copiar un bloque completo:

```yaml
- number: "05"
  title: New service
  description: Short description.
  features:
    - Feature one
    - Feature two
    - Feature three
```

El sitio genera la tarjeta automáticamente. Revisar visualmente la grilla si cambia el número total de tarjetas.

### Agregar/cambiar imagen

```yaml
image: /assets/images/cell-culture.jpg
image_alt: Cell culture plate and pipette inside a biosafety cabinet
credit_label: Author / Source
credit_url: https://...
```

`image_alt` describe lo visible; no debe ser texto de marketing.

### Quitar imagen

Eliminar los campos `image`, `image_alt`, `credit_label` y `credit_url` del servicio.

---

## 5. Equipo — `_data/team.yml`

Cada integrante tiene un `id` interno. Ese ID vincula a la persona con las publicaciones.

```yaml
- id: casal
  initials: JC
  name: Dr. Juan J. Casal
  role: Computational modeling · bioinformatics · AI
  expertise: Pharmacist and PhD in Pharmacy...
  linkedin: https://www.linkedin.com/in/juan-jose-casal/
  conicet: https://bicyt.conicet.gov.ar/...
  email: jcasal@fmed.uba.ar
```

### Modificar una persona

Editar `name`, `role`, `expertise`, `linkedin`, `conicet` o `email`.

### Agregar integrante

```yaml
- id: apellido
  initials: AB
  name: Dr. Nombre Apellido
  role: Área 1 · Área 2 · Área 3
  expertise: Descripción breve y relevante para PharmaToxAI.
  linkedin: https://www.linkedin.com/in/...
  conicet: https://bicyt.conicet.gov.ar/...
  email: nombre@dominio.ar
```

### Reglas del `id`

Usar minúsculas, sin espacios ni acentos, preferentemente apellido:

```text
casal
digiusto
rivarola
martinez
```

**No cambiar un ID existente** si ya tiene papers asociados. Si se cambia `casal` por otra cosa, también hay que cambiar todas las referencias en `_data/publications.csv`.

### Sin email

```yaml
email: ""
```

### Cambiar orden visual

Mover el bloque completo dentro de `team.yml`.

---

## 6. Publicaciones — `_data/publications.csv`

Formato:

```csv
id,title,journal,year,doi,members
```

Ejemplo:

```csv
p009,"Título completo del trabajo",Journal Name,2027,https://doi.org/10.xxxx/xxxxx,casal|martinez
```

### Columnas

- `id`: identificador único (`p001`, `p002`, etc.).
- `title`: título completo. Conviene ponerlo siempre entre comillas dobles.
- `journal`: nombre de la revista.
- `year`: año numérico, por ejemplo `2027`.
- `doi`: URL completa `https://doi.org/...`.
- `members`: IDs de integrantes separados por `|`.

### Paper de un solo integrante

```text
casal
```

### Paper compartido

```text
casal|digiusto|rivarola
```

La publicación se ingresa **una sola vez**. El sitio la asocia automáticamente a todos los miembros indicados.

### Comas en títulos

Incorrecto:

```csv
p010,A paper title, with a comma,Journal,2027,...
```

Correcto:

```csv
p010,"A paper title, with a comma",Journal,2027,...
```

### Comillas dentro de títulos

CSV duplica las comillas internas:

```csv
p010,"The role of ""AI"" in toxicology",Journal,2027,...
```

### No modificar el encabezado

Mantener:

```csv
id,title,journal,year,doi,members
```

salvo que también se adapten los templates.

---

## 7. White papers — `_whitepapers/`

La colección Jekyll `_whitepapers` genera páginas individuales y el índice `/whitepapers/`.

Un documento tiene front matter YAML y cuerpo Markdown:

```markdown
---
layout: whitepaper
title: Predictive toxicology in early drug development
summary: Short summary for the resource index.
authors:
  - Juan José Casal
  - Gisela Di Giusto
date: 2026-09-07
pdf: /assets/whitepapers/predictive-toxicology.pdf
published: true
---

## Introduction

Texto...

## Approach

Texto...

## Conclusions

Texto...
```

### Publicar

```yaml
published: true
```

### Mantener como borrador

```yaml
published: false
```

### PDF descargable

Guardar:

```text
assets/whitepapers/predictive-toxicology.pdf
```

Y declarar:

```yaml
pdf: /assets/whitepapers/predictive-toxicology.pdf
```

### Sin PDF

```yaml
pdf: ""
```

### Figura dentro del Markdown

```markdown
![Applicability-domain schematic](/assets/whitepapers/applicability-domain.png)
```

### Links

```markdown
[OECD](https://www.oecd.org/)
```

### Tabla

```markdown
| Endpoint | Method | Evidence |
| --- | --- | --- |
| Toxicity | QSAR | in silico |
| Viability | Cell assay | in vitro |
```

---

## 8. Navegación — `_data/navigation.yml`

Ejemplo:

```yaml
- label: Publications
  url: /publications/

- label: Contact
  url: /#contact
  button: true
```

### Agregar una página

```yaml
- label: Resources
  url: /resources/
```

### Sección de la home

```yaml
- label: Team
  url: /#team
```

El fragmento `#team` debe coincidir con `id="team"` en la home.

### Botón principal

```yaml
button: true
```

Conviene reservarlo para una sola acción relevante.

---

## 9. Cuándo tocar `index.html`

Editar `index.html` para cambios narrativos/estructurales de la home:

- título o texto de una sección no almacenada en `_data`;
- workflow;
- Technology;
- Validation;
- Applications;
- agregar o eliminar una sección completa.

No editarlo para:

- agregar papers;
- modificar personas;
- cambiar LinkedIn;
- cambiar servicios;
- cambiar imágenes de servicios;
- agregar white papers.

---

## 10. Imágenes

### Imágenes externas

```yaml
image: https://example.org/image.jpg
```

Ventaja: repo liviano. Desventaja: dependencia de terceros.

### Imágenes locales

Guardar en:

```text
assets/images/
```

Y usar:

```yaml
image: /assets/images/cell-culture.jpg
```

Preferible para imágenes propias, logo, figuras científicas propias y recursos que deban permanecer estables.

### Nombres recomendados

```text
cell-culture-2d.jpg
pbpk-model.png
qsar-workflow.svg
```

Evitar espacios y nombres como `FINAL_final2.png`.

### Formatos

- fotografías: JPEG/WebP;
- diagramas/logos: SVG cuando sea posible;
- PNG si se necesita transparencia o preservación pixel-perfect.

---

## 11. `_layouts/` y `_includes/`

Son código de presentación, no contenido cotidiano.

### `_layouts/`

Define esqueletos completos de páginas. Por ejemplo `default.html` y `whitepaper.html`.

Cambiar un layout puede afectar muchas páginas.

### `_includes/`

Componentes reutilizables como header, footer, logo y tarjetas. Cambiar `team-card.html` modifica todas las tarjetas del equipo.

---

## 12. CSS — `styles.css` y `jekyll.css`

Editar solo para cambios de diseño:

- colores;
- tipografías;
- tamaños;
- spacing;
- columnas;
- responsive;
- tarjetas;
- hover;
- presentación de publicaciones y white papers.

Después de tocar CSS revisar desktop y móvil.

---

## 13. `_config.yml`

Archivo estructural sensible.

Actualmente incluye:

```yaml
url: https://pharmatoxai.ar
baseurl: ""
lang: en
permalink: pretty
```

Y:

```yaml
collections:
  whitepapers:
    output: true
    permalink: /whitepapers/:name/
```

No modificar salvo que cambie la arquitectura.

### Cambiar idioma

```yaml
lang: es
```

Esto no traduce el sitio; solo cambia metadata HTML.

### Cambiar dominio

Actualizar tanto `_config.yml` como `CNAME`.

---

## 14. `CNAME`

Debe contener solamente:

```text
pharmatoxai.ar
```

No borrar salvo migración deliberada del dominio.

No usar:

```text
https://pharmatoxai.ar
```

---

## 15. Preview local

Opcional para cambios pequeños, recomendable para cambios visuales.

```bash
bundle install
bundle exec jekyll serve --livereload
```

Abrir:

```text
http://127.0.0.1:4000
```

Si se modifica `_config.yml`, reiniciar Jekyll.

---

## 16. Verificar el deploy

Después del push:

1. abrir el repo;
2. ir a `Actions`;
3. abrir `pages build and deployment`;
4. verificar que termine en verde;
5. revisar `https://pharmatoxai.ar`.

Errores comunes de build:

- YAML mal indentado;
- front matter mal cerrado;
- Liquid inválido;
- CSV roto por comas sin comillas;
- archivos con sintaxis incorrecta.

---

## 17. Revertir un cambio

Historial:

```bash
git log --oneline
```

Revertir sin reescribir historial:

```bash
git revert COMMIT_SHA
git push origin main
```

Preferir `git revert` a reescribir `main` con `reset --hard`.

---

## 18. Casos frecuentes

### A. Nuevo paper de Casal y Di Giusto

Editar `_data/publications.csv`:

```csv
p009,"New paper title",Journal Name,2027,https://doi.org/10.xxxx/xxxxx,casal|digiusto
```

Nada más.

### B. Cambiar perfil de Nora

Editar `_data/team.yml`, buscar:

```yaml
- id: martinez
```

Modificar `role` o `expertise`. No cambiar `id`.

### C. Cambiar foto de Human cellular validation

Editar `_data/services.yml`, buscar:

```yaml
- number: "03"
```

Cambiar `image`, `image_alt`, `credit_label`, `credit_url`.

### D. Nuevo servicio

Agregar bloque a `_data/services.yml`. Revisar visualmente la grilla si queda un número impar.

### E. Nuevo white paper

Crear `_whitepapers/nombre.md`, completar front matter y usar `published: true` cuando esté listo.

### F. Nueva página independiente

Crear por ejemplo `technology.md`:

```markdown
---
title: Technology
permalink: /technology/
---

# Technology

Contenido...
```

Luego agregarla a `_data/navigation.yml`.

---

## 19. Qué no hacer

- No duplicar datos en HTML si ya existen en `_data`.
- No escribir papers manualmente dentro de tarjetas de personas.
- No cambiar IDs de miembros sin actualizar `publications.csv`.
- No borrar `CNAME`.
- No volver a crear `.nojekyll`; el sitio necesita procesamiento Jekyll.
- No editar `_site/`; es salida generada.
- No guardar contraseñas, API keys ni secretos en el repo.
- No usar rutas locales (`C:\...`, `/home/...`) como URLs web.

**Importante:** el repositorio es público. Aunque este archivo esté excluido del sitio generado por Jekyll, cualquier persona que visite el repositorio en GitHub puede leerlo. Si alguna documentación debe ser realmente confidencial, no debe almacenarse aquí.

---

## 20. Convenciones

### Commits

Buenos ejemplos:

```text
Add 2027 publication
Update team profiles
Add predictive toxicology white paper
Replace cell culture image
Update hero copy
```

### Archivos

```text
predictive-toxicology.md
cell-culture.jpg
pbpk-workflow.svg
```

### Fechas

Usar ISO:

```text
2026-09-07
```

### URLs internas

```text
/publications/
/whitepapers/
/assets/images/...
```

---

## 21. Archivos que deberían quedar estables

Una vez cerrado el diseño:

```text
_layouts/
_includes/
styles.css
jekyll.css
script.js
```

El trabajo cotidiano debería concentrarse en:

```text
_data/company.yml
_data/navigation.yml
_data/services.yml
_data/team.yml
_data/publications.csv
_whitepapers/
assets/images/
assets/whitepapers/
```

---

## 22. Checklist antes de push

- [ ] YAML indentado con espacios.
- [ ] CSV conserva el encabezado esperado.
- [ ] Títulos con comas están entre comillas.
- [ ] IDs de `members` existen en `team.yml`.
- [ ] DOI en formato `https://doi.org/...`.
- [ ] Imágenes con `alt` descriptivo.
- [ ] Créditos/licencias incluidos cuando corresponda.
- [ ] Front matter Markdown cerrado con `---`.
- [ ] `published` tiene el valor correcto.
- [ ] No hay instrucciones internas o placeholders dentro de páginas públicas.
- [ ] No se agregaron secretos o datos privados al repositorio.
