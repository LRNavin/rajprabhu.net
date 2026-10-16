# rajprabhu.net

Personal research website of Navin Raj Prabhu, served by GitHub Pages from the `main` branch at <https://rajprabhu.net>.

## Layout

- `index.html`, `publications.html`, `cv.html`, `404.html`: generated pages (do not edit by hand)
- `scripts/build.py`: page templates and all content (publications, news, CV)
- `assets/`: stylesheet, script, fonts (self-hosted) and images

## Making a change

```sh
# edit content in scripts/build.py, or styles in assets/style.css
python3 scripts/build.py      # regenerates the HTML pages
python3 -m http.server 8000   # preview at http://localhost:8000
git add -A && git commit -m "Describe the change" && git push
```

Python 3.8+ with the standard library is all the build needs.

See [AGENTS.md](AGENTS.md) for content conventions, design rules and hosting details before making changes.
