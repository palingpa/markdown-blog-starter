# markdown-blog-starter

A few Markdown posts plus a Python script that builds a simple `public/` site.

## Build

```bash
python build.py
python -m http.server -d public 8080
```

Posts live in `posts/*.md`. The builder is intentionally naive (headings + paragraphs).

