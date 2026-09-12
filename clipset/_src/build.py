#!/usr/bin/env python3
"""Builds the Clipset legal pages: every language is inlined into one static file.

Run:  python3 clipset/_src/build.py
Writes clipset/index.html and clipset/terms/index.html.
"""

import html
import json
import pathlib
import re

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
LANGS = ["en", "uk", "de", "es", "fr", "it", "pl", "pt-BR", "tr"]

CSS = """
:root {
  --bg: #F4F5F5;
  --card: #FFFFFF;
  --ink: #181B19;
  --ink-soft: #3E423F;
  --muted: #7C837E;
  --line: #E5E6E5;
  --chip: #F4F5F5;
  --accent: #479C14;
  --shadow: 0 12px 32px rgba(24, 27, 25, .07);
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0A0B0A;
    --card: #181B19;
    --ink: #F9FAFA;
    --ink-soft: #E5E6E5;
    --muted: #A0A6A2;
    --line: #3E423F;
    --chip: #252825;
    --accent: #6FD926;
    --shadow: none;
  }
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  font-size: 17px;
  line-height: 1.62;
  -webkit-font-smoothing: antialiased;
}
.bar {
  position: sticky; top: 0; z-index: 10;
  display: flex; align-items: center; gap: 10px;
  padding: 12px 20px;
  background: var(--bg);
  border-bottom: 1px solid var(--line);
}
.mark {
  font-weight: 700; letter-spacing: -.02em; font-size: 17px;
  margin-right: auto; color: var(--ink); text-decoration: none;
}
.mark span { color: var(--accent); }
.bar a.switch {
  font-size: 14px; font-weight: 600; color: var(--ink-soft);
  text-decoration: none; padding: 8px 14px;
  border-radius: 999px; background: var(--chip); white-space: nowrap;
}
.bar a.switch:hover { color: var(--ink); }
select {
  font: inherit; font-size: 14px; font-weight: 600;
  color: var(--ink-soft); background: var(--chip);
  border: 0; border-radius: 999px; padding: 8px 12px;
  appearance: none; -webkit-appearance: none; cursor: pointer;
}
main { max-width: 760px; margin: 0 auto; padding: 28px 20px 72px; }
.card {
  background: var(--card); border-radius: 28px;
  box-shadow: var(--shadow); padding: 36px 32px 40px;
}
@media (max-width: 560px) {
  .card { border-radius: 22px; padding: 26px 20px 30px; }
  body { font-size: 16px; }
  main { padding: 18px 14px 56px; }
}
.kicker {
  display: inline-block; font-size: 12px; font-weight: 700;
  letter-spacing: .08em; text-transform: uppercase; color: var(--muted);
  background: var(--chip); border-radius: 999px; padding: 6px 12px; margin-bottom: 18px;
}
h1 { font-size: 34px; line-height: 1.15; letter-spacing: -.03em; margin: 0 0 10px; }
@media (max-width: 560px) { h1 { font-size: 27px; } }
.updated { color: var(--muted); font-size: 14px; margin: 0 0 24px; }
.lead {
  font-size: 17px; color: var(--ink-soft); margin: 0;
  padding: 18px 20px; background: var(--chip); border-radius: 18px;
}
article { counter-reset: sec; }
section { counter-increment: sec; counter-reset: clause; margin-top: 32px; }
section > h2 {
  font-size: 20px; letter-spacing: -.02em; margin: 0 0 12px;
  padding-top: 26px; border-top: 1px solid var(--line);
}
section > h2::before { content: counter(sec) ". "; color: var(--muted); font-weight: 600; }
p { margin: 0 0 14px; color: var(--ink-soft); }
p.clause { padding-left: 3.2em; text-indent: -3.2em; margin-bottom: 12px; }
p.clause::before {
  counter-increment: clause;
  content: counter(sec) "." counter(clause);
  display: inline-block; width: 3.2em; text-indent: 0;
  color: var(--muted); font-weight: 600; font-variant-numeric: tabular-nums;
}
@media (max-width: 560px) {
  p.clause { padding-left: 2.9em; text-indent: -2.9em; }
  p.clause::before { width: 2.9em; }
}
ul { margin: 0 0 16px; padding-left: 20px; color: var(--ink-soft); }
li { margin-bottom: 8px; }
li::marker { color: var(--muted); }
b, strong { color: var(--ink); font-weight: 650; }
code {
  font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
  font-size: .92em; background: var(--chip); color: var(--ink);
  padding: 1px 6px; border-radius: 6px;
}
a { color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: 2px; }
.note {
  margin: 0 0 16px; padding: 16px 18px; border-radius: 16px;
  background: var(--chip); font-size: 15px;
}
.foot {
  margin-top: 38px; padding-top: 22px; border-top: 1px solid var(--line);
  color: var(--muted); font-size: 14px;
  display: flex; flex-wrap: wrap; gap: 8px 16px; align-items: baseline;
}
.foot a { font-weight: 600; }
[hidden] { display: none !important; }
@media print {
  .bar { display: none; }
  .card { box-shadow: none; padding: 0; }
  body { background: #fff; }
  main { padding: 0; }
}
"""

JS = """
(function () {
  var LANGS = %(langs)s;
  var select = document.getElementById('lang');
  function pick() {
    var q = new URLSearchParams(location.search).get('lang');
    var stored = null;
    try { stored = localStorage.getItem('clipset.legal.lang'); } catch (e) {}
    var wanted = [q, stored].concat(navigator.languages || [navigator.language || 'en']);
    for (var i = 0; i < wanted.length; i++) {
      var w = wanted[i];
      if (!w) continue;
      for (var j = 0; j < LANGS.length; j++) {
        if (LANGS[j].toLowerCase() === w.toLowerCase()) return LANGS[j];
      }
      var base = w.split('-')[0].toLowerCase();
      for (var k = 0; k < LANGS.length; k++) {
        if (LANGS[k].split('-')[0].toLowerCase() === base) return LANGS[k];
      }
    }
    return 'en';
  }
  function apply(code, remember) {
    var found = false;
    LANGS.forEach(function (l) {
      var node = document.getElementById('doc-' + l);
      if (!node) return;
      var on = l === code;
      node.hidden = !on;
      if (on) {
        found = true;
        document.documentElement.lang = l;
        document.title = node.getAttribute('data-title');
        var switcher = document.querySelector('.bar a.switch');
        if (switcher) switcher.textContent = node.getAttribute('data-other');
      }
    });
    if (!found) { apply('en', false); return; }
    if (select) select.value = code;
    var links = document.querySelectorAll('a[data-keep-lang]');
    for (var i = 0; i < links.length; i++) {
      links[i].href = links[i].getAttribute('data-href') + '?lang=' + encodeURIComponent(code);
    }
    if (remember) { try { localStorage.setItem('clipset.legal.lang', code); } catch (e) {} }
  }
  apply(pick(), false);
  if (select) {
    select.addEventListener('change', function () { apply(select.value, true); window.scrollTo(0, 0); });
  }
})();
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%(title)s</title>
<meta name="description" content="%(description)s">
<meta name="color-scheme" content="light dark">
<meta name="robots" content="index, follow">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(description)s">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%%3E%%3Crect width='32' height='32' rx='8' fill='%%23181B19'/%%3E%%3Cpath d='M13 10l10 6-10 6z' fill='%%236FD926'/%%3E%%3C/svg%%3E">
<style>%(css)s</style>
</head>
<body>
<nav class="bar">
  <a class="mark" href="%(home)s" data-keep-lang data-href="%(home)s">Clip<span>set</span></a>
  <a class="switch" href="%(other)s" data-keep-lang data-href="%(other)s">%(other_label)s</a>
  <select id="lang" aria-label="Language">%(options)s</select>
</nav>
<main>
%(docs)s
</main>
<script>%(js)s</script>
</body>
</html>
"""

LINK = re.compile(r"\[\[([^|\]]+)\|([^\]]+)\]\]")
BOLD = re.compile(r"\*\*(.+?)\*\*")
CODE = re.compile(r"`([^`]+)`")


def esc(text):
    out = html.escape(text, quote=False)
    out = BOLD.sub(lambda m: "<b>" + m.group(1) + "</b>", out)
    out = CODE.sub(lambda m: "<code>" + m.group(1) + "</code>", out)
    out = LINK.sub(lambda m: '<a href="' + m.group(2) + '" target="_blank" rel="noopener">' + m.group(1) + "</a>", out)
    return out


def render_blocks(blocks):
    chunks = []
    for block in blocks:
        if "p" in block:
            chunks.append("      <p>%s</p>" % esc(block["p"]))
        elif "c" in block:
            chunks.append('      <p class="clause">%s</p>' % esc(block["c"]))
        elif "note" in block:
            chunks.append('      <p class="note">%s</p>' % esc(block["note"]))
        elif "ul" in block:
            items = "".join("<li>%s</li>" % esc(i) for i in block["ul"])
            chunks.append("      <ul>%s</ul>" % items)
    return "\n".join(chunks)


def render_doc(data, other_href, other_label):
    sections = []
    for section in data["sections"]:
        sections.append(
            '    <section>\n      <h2>%s</h2>\n%s\n    </section>'
            % (esc(section["h"]), render_blocks(section["blocks"]))
        )
    return """  <article id="doc-%(lang)s" data-title="%(title)s" data-other="%(other_attr)s" hidden>
    <div class="card">
      <span class="kicker">%(kicker)s</span>
      <h1>%(heading)s</h1>
      <p class="updated">%(updated)s</p>
      <p class="lead">%(lead)s</p>
%(sections)s
      <div class="foot">
        <span>%(footer)s</span>
        <a href="%(other_href)s" data-keep-lang data-href="%(other_href)s">%(other_label)s</a>
      </div>
    </div>
  </article>""" % {
        "lang": data["lang"],
        "title": html.escape(data["docTitle"], quote=True),
        "other_attr": html.escape(other_label, quote=True),
        "kicker": esc(data["kicker"]),
        "heading": esc(data["title"]),
        "updated": esc(data["updated"]),
        "lead": esc(data["lead"]),
        "sections": "\n".join(sections),
        "footer": esc(data["footer"]),
        "other_href": other_href,
        "other_label": esc(other_label),
    }


def build(doc, other_doc, out_path, home, other_href):
    langs, docs, options, english, english_other = [], [], [], None, ""
    for code in LANGS:
        path = SRC / "content" / ("%s.%s.json" % (doc, code))
        if not path.exists():
            print("  missing: %s" % path.name)
            continue
        data = json.loads(path.read_text(encoding="utf-8"))
        sibling = SRC / "content" / ("%s.%s.json" % (other_doc, code))
        label = json.loads(sibling.read_text(encoding="utf-8"))["title"] if sibling.exists() else data["otherLabel"]
        langs.append(code)
        docs.append(render_doc(data, other_href, label))
        options.append('<option value="%s">%s</option>' % (code, html.escape(data["langName"], quote=True)))
        if code == "en":
            english = data
            english_other = label
    page = PAGE % {
        "title": html.escape(english["docTitle"], quote=True),
        "description": html.escape(BOLD.sub(r"\1", english["lead"])[:180], quote=True),
        "css": CSS,
        "js": JS % {"langs": json.dumps(langs)},
        "docs": "\n".join(docs),
        "options": "".join(options),
        "home": home,
        "other": other_href,
        "other_label": html.escape(english_other, quote=True),
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(page, encoding="utf-8")
    print("wrote %s  (%d languages, %.0f KB)" % (out_path.relative_to(ROOT.parent), len(langs), out_path.stat().st_size / 1024))


if __name__ == "__main__":
    build("privacy", "terms", ROOT / "index.html", "./", "./terms/")
    build("terms", "privacy", ROOT / "terms" / "index.html", "../", "../")
