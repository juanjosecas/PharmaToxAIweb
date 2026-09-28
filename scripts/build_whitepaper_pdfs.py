"""Render published Jekyll white papers to PDFs inside the Pages artifact."""

from html import escape
from pathlib import Path

from bs4 import BeautifulSoup
from weasyprint import CSS, HTML


SITE = Path("_site")
CSS_FILE = Path(__file__).with_name("whitepaper-print.css")


def main():
    pages = sorted((SITE / "whitepapers").glob("*/index.html"))
    if not pages:
        raise RuntimeError("No published white paper pages found in _site/whitepapers")

    for page in pages:
        soup = BeautifulSoup(page.read_text(encoding="utf-8"), "html.parser")
        title = soup.select_one(".content-hero h1")
        summary = soup.select_one(".content-hero .content-lead")
        metadata = soup.select_one(".content-hero .content-meta")
        article = soup.select_one("article.prose")
        if title is None or article is None:
            raise RuntimeError(f"Missing white paper title or content: {page}")

        url = f"https://pharmatoxai.ar/whitepapers/{page.parent.name}/"
        summary_html = f"<p class='summary'>{summary.decode_contents()}</p>" if summary else ""
        metadata_html = f"<p class='metadata'>{metadata.get_text(' · ', strip=True)}</p>" if metadata else ""
        document = f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>{escape(title.get_text(" ", strip=True))}</title></head>
<body>
  <header><span>PharmaToxAI</span><span>White paper</span></header>
  <h1>{escape(title.get_text(" ", strip=True))}</h1>
  {summary_html}
  {metadata_html}
  {article}
  <footer>Online edition: <a href="{url}">{url}</a></footer>
</body>
</html>"""
        output = page.with_name("paper.pdf")
        HTML(string=document, base_url=url).write_pdf(
            output, stylesheets=[CSS(filename=CSS_FILE)]
        )
        if output.stat().st_size < 4096 or output.read_bytes()[:4] != b"%PDF":
            raise RuntimeError(f"Invalid generated PDF: {output}")
        print(f"{output}: {output.stat().st_size} bytes")


if __name__ == "__main__":
    main()
