#!/usr/bin/env python3
"""
Render resume.md -> PDF (and a standalone HTML) via Chromium print.

    python3 render.py resume.md --out resume.pdf            # public: no phone
    python3 render.py resume.md --out resume-full.pdf --phone

Markdown is the single source of truth. Front matter holds the contact
details; everything below it is ordinary Markdown.
"""
import argparse, asyncio, html, pathlib, re, sys
import markdown, yaml

CSS = """
@page { size: A4; margin: 13mm 14mm 12mm 14mm; }

:root {
  --ink:      #16181c;
  --ink-2:    #3d4148;
  --ink-3:    #6c7179;
  --rule:     #d8d4cc;
  --accent:   #a8481a;
  --serif: "Newsreader", "Iowan Old Style", Palatino, Georgia, serif;
  --sans:  "Inter", -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
}

* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; }
body {
  font-family: var(--sans);
  font-size: 9.4pt;
  line-height: 1.44;
  color: var(--ink-2);
  -webkit-font-smoothing: antialiased;
}

/* ---------- header ---------- */
header { margin-bottom: 13pt; }
h1 {
  font-family: var(--serif);
  font-weight: 500;
  font-size: 25pt;
  line-height: 1;
  letter-spacing: -.015em;
  color: var(--ink);
  margin: 0 0 4pt;
}
.subtitle {
  font-size: 10pt;
  color: var(--accent);
  font-weight: 500;
  letter-spacing: .005em;
  margin: 0 0 7pt;
}
.contact {
  font-size: 8.6pt;
  color: var(--ink-3);
  display: flex;
  flex-wrap: wrap;
  gap: 0 7pt;
  border-top: .6pt solid var(--rule);
  padding-top: 6pt;
}
.contact span::after { content: "·"; margin-left: 7pt; color: var(--rule); }
.contact span:last-child::after { content: ""; }
.contact a { color: var(--ink-3); text-decoration: none; }

/* ---------- sections ---------- */
h2 {
  font-family: var(--sans);
  font-size: 8.2pt;
  font-weight: 600;
  letter-spacing: .11em;
  text-transform: uppercase;
  color: var(--ink);
  margin: 14pt 0 7pt;
  padding-bottom: 3.5pt;
  border-bottom: .6pt solid var(--rule);
  break-after: avoid;
}
h2:first-of-type { margin-top: 4pt; }

h3 {
  font-size: 10.2pt;
  font-weight: 600;
  color: var(--ink);
  margin: 9pt 0 1pt;
  letter-spacing: -.005em;
  break-after: avoid;
}
h3 + p strong { font-weight: 500; }

/* the dates/company line directly under an h3 */
h3 + p {
  font-size: 8.5pt;
  color: var(--ink-3);
  margin: 0 0 4pt;
  break-after: avoid;
}
h3 + p strong { color: var(--ink-3); font-weight: 500; }

p { margin: 0 0 5pt; }
p:last-child { margin-bottom: 0; }

ul { margin: 0 0 3pt; padding-left: 0; list-style: none; }
li {
  position: relative;
  padding-left: 10pt;
  margin-bottom: 2.6pt;
  break-inside: avoid;
}
li::before {
  content: "";
  position: absolute;
  left: 1pt; top: 4.6pt;
  width: 2.6pt; height: 2.6pt;
  border-radius: 50%;
  background: var(--accent);
}
li strong, p strong { color: var(--ink); font-weight: 600; }

/* project tech-stack line: its own paragraph, set apart from the prose */
p.stack {
  margin-top: 2.5pt;
  font-size: 8.3pt;
  color: var(--ink-3);
  letter-spacing: .01em;
}
p.stack em { font-style: normal; }
em { color: var(--ink-3); font-style: normal; }

/* skills block: "Label — items" */
.skills p { margin-bottom: 3.4pt; }
.skills strong { color: var(--ink); }

/* Let long entries flow across a page break rather than leaving a quarter of
   a page blank; h3/h3+p carry break-after:avoid so a heading never lands
   alone at the foot of a page. */
.entry { break-inside: auto; }
a { color: inherit; }
"""

HTML_SHELL = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400;6..72,500&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>
<header>
  <h1>{name}</h1>
  <p class="subtitle">{subtitle}</p>
  <div class="contact">{contact}</div>
</header>
{body}
</body></html>
"""


def split_front_matter(text):
    if text.startswith("---"):
        _, fm, rest = text.split("---", 2)
        return yaml.safe_load(fm), rest.lstrip("\n")
    return {}, text


def build_contact(meta, include_phone):
    items = []
    if include_phone and meta.get("phone"):
        items.append(html.escape(str(meta["phone"])))
    for key, prefix in (("email", "mailto:"), ("website", "https://"),
                        ("linkedin", "https://"), ("github", "https://")):
        v = meta.get(key)
        if v:
            items.append(f'<a href="{prefix}{v}">{html.escape(v)}</a>')
    if meta.get("location"):
        items.insert(0, html.escape(meta["location"]))
    return "".join(f"<span>{i}</span>" for i in items)


def wrap_entries(body_html):
    """Wrap each role/project block so a heading is never orphaned.

    Split on h2 as well as h3, otherwise a section heading ends up inside the
    preceding entry's div and its top margin collapses against the boundary.
    """
    parts = re.split(r"(?=<h2)|(?=<h3)", body_html)
    out = []
    for p in parts:
        if p and p.startswith("<h3"):
            out.append(f'<div class="entry">{p}</div>')
        elif p:
            out.append(p)
    return "".join(out)


async def to_pdf(html_text, out_path):
    from playwright.async_api import async_playwright
    tmp = pathlib.Path(out_path).with_suffix(".html")
    tmp.write_text(html_text, encoding="utf-8")
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        await pg.goto(tmp.resolve().as_uri(), wait_until="networkidle")
        await pg.wait_for_timeout(600)
        await pg.pdf(path=out_path, format="A4", print_background=True,
                     margin={"top": "13mm", "bottom": "12mm",
                             "left": "14mm", "right": "14mm"})
        await b.close()
    return tmp


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--out", required=True)
    ap.add_argument("--phone", action="store_true",
                    help="include the phone number (omit for the public copy)")
    a = ap.parse_args()

    meta, md_body = split_front_matter(pathlib.Path(a.source).read_text(encoding="utf-8"))
    body = markdown.markdown(md_body, extensions=["extra", "sane_lists"])

    # a paragraph that is nothing but italics is a tech-stack line
    body = re.sub(r"<p><em>(.*?)</em></p>", r'<p class="stack"><em>\1</em></p>',
                  body, flags=re.S)

    # tag the skills section so its paragraphs get tighter spacing
    body = re.sub(r"(<h2>Skills</h2>)", r'<div class="skills">\1', body, count=1)
    body = re.sub(r"(<h2>Education</h2>)", r"</div>\1", body, count=1)

    body = wrap_entries(body)

    page = HTML_SHELL.format(
        css=CSS,
        title=f'{meta.get("name","Resume")} — Resume',
        name=html.escape(meta.get("name", "")),
        subtitle=html.escape(meta.get("title", "")),
        contact=build_contact(meta, a.phone),
        body=body,
    )
    tmp = asyncio.run(to_pdf(page, a.out))
    print(f"wrote {a.out}  (html kept at {tmp})")


if __name__ == "__main__":
    main()
