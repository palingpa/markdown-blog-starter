#!/usr/bin/env python3
"""Generate a very small static index from posts/*.md."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POSTS = ROOT / "posts"
OUT = ROOT / "public"


def md_to_html_lite(text: str) -> str:
    lines = text.strip().splitlines()
    html = []
    for line in lines:
        if line.startswith("# "):
            html.append(f"<h1>{line[2:].strip()}</h1>")
        elif line.startswith("## "):
            html.append(f"<h2>{line[3:].strip()}</h2>")
        elif not line.strip():
            html.append("")
        else:
            html.append(f"<p>{line}</p>")
    return "\n".join(html)


def main():
    OUT.mkdir(exist_ok=True)
    cards = []
    for path in sorted(POSTS.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        title = path.stem.replace("-", " ").title()
        for line in raw.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
        slug = path.stem
        body = md_to_html_lite(raw)
        page = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="style.css"></head>
<body>
<article>
{body}
<p><a href="index.html">← Back</a></p>
</article>
</body></html>
"""
        (OUT / f"{slug}.html").write_text(page, encoding="utf-8")
        cards.append(f'<li><a href="{slug}.html">{title}</a></li>')

    index = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>Notes</title>
<link rel="stylesheet" href="style.css"></head>
<body>
<h1>Notes</h1>
<ul>
{chr(10).join(cards)}
</ul>
</body></html>
"""
    (OUT / "index.html").write_text(index, encoding="utf-8")
    (OUT / "style.css").write_text(
        "body{font-family:system-ui,sans-serif;max-width:680px;margin:2rem auto;padding:0 1rem;line-height:1.65;color:#111}"
        "a{color:#2563eb}",
        encoding="utf-8",
    )
    print(f"built {len(cards)} posts -> {OUT}")


if __name__ == "__main__":
    main()
