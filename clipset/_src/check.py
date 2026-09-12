#!/usr/bin/env python3
"""Checks every translation against the English source: same shape, same markup, same numbers."""

import json
import pathlib
import re
import sys

SRC = pathlib.Path(__file__).resolve().parent / "content"
LANGS = ["uk", "de", "es", "fr", "it", "pl", "pt-BR", "tr"]
TOP_KEYS = ["lang", "langName", "docTitle", "kicker", "title", "updated", "otherLabel", "footer", "lead", "sections"]
URL = re.compile(r"\[\[[^|\]]+\|([^\]]+)\]\]")
NUM = re.compile(r"\b\d+\b")

failures = []


def shape(doc):
    out = []
    for section in doc["sections"]:
        blocks = []
        for block in section["blocks"]:
            kind = next(iter(block))
            blocks.append((kind, len(block[kind]) if kind == "ul" else 1))
        out.append(tuple(blocks))
    return out


def texts(doc):
    out = []
    for section in doc["sections"]:
        out.append(section["h"])
        for block in section["blocks"]:
            kind = next(iter(block))
            out.extend(block[kind] if kind == "ul" else [block[kind]])
    return out


def report(lang, doc, problem):
    failures.append("%s/%s: %s" % (doc, lang, problem))


for doc in ("privacy", "terms"):
    base = json.loads((SRC / ("%s.en.json" % doc)).read_text(encoding="utf-8"))
    base_shape = shape(base)
    base_text = texts(base)
    base_urls = sorted(URL.findall(" ".join(base_text)))
    base_backticks = " ".join(base_text).count("`")
    base_numbers = sorted(NUM.findall(" ".join(base_text)))

    for lang in LANGS:
        path = SRC / ("%s.%s.json" % (doc, lang))
        if not path.exists():
            report(lang, doc, "file missing")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            report(lang, doc, "invalid JSON: %s" % error)
            continue

        missing = [k for k in TOP_KEYS if k not in data]
        if missing:
            report(lang, doc, "missing keys %s" % missing)
            continue
        if data["lang"] != lang:
            report(lang, doc, "lang field is %r" % data["lang"])
        if "Clipset" not in data["docTitle"]:
            report(lang, doc, "docTitle lacks Clipset: %r" % data["docTitle"])

        if shape(data) != base_shape:
            for index, (want, got) in enumerate(zip(base_shape, shape(data))):
                if want != got:
                    report(lang, doc, "section %d shape %s, expected %s" % (index + 1, got, want))
            if len(shape(data)) != len(base_shape):
                report(lang, doc, "%d sections, expected %d" % (len(shape(data)), len(base_shape)))
            continue

        joined = " ".join(texts(data))
        urls = sorted(URL.findall(joined))
        if urls != base_urls:
            report(lang, doc, "links differ: %s vs %s" % (urls, base_urls))
        if joined.count("**") % 2:
            report(lang, doc, "unbalanced bold markers")
        if joined.count("`") != base_backticks:
            report(lang, doc, "backtick count %d, expected %d" % (joined.count("`"), base_backticks))
        numbers = NUM.findall(joined)
        for number in set(base_numbers):
            if numbers.count(number) < base_numbers.count(number):
                report(lang, doc, "number %s appears %d times, expected %d"
                       % (number, numbers.count(number), base_numbers.count(number)))

if failures:
    print("\n".join(failures))
    sys.exit(1)
print("all translations match the English structure")
