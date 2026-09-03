# Resume

`resume.md` is the source of truth. `render.py` turns it into a PDF via
Chromium's print engine, so layout is plain CSS rather than a Word template.

```bash
pip install markdown pyyaml playwright
python3 render.py resume.md --out ../src/assets/resume.pdf   # public: no phone
python3 render.py resume.md --out resume-with-phone.pdf --phone
```

The front matter holds the contact details; `--phone` decides whether the
number is rendered. The public copy at `src/assets/resume.pdf` is served from
msdhaliwal.com, so it deliberately omits the phone number.
