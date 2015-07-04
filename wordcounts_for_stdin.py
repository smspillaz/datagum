import fileinput

import os

from collections import defaultdict

import operator


words = defaultdict(lambda: {
    "count": 0,
    "urls": set()
})

for line in fileinput.input():
    with open(os.path.join("webs", "tmp", line.strip())) as f:
        for l in f.readlines():
            parts = l.split()
            if len(parts) < 2:
                continue

            count, word = tuple(parts)

            try:
                words[word]["count"] += int(count)
            except ValueError:
                continue

            words[word]["urls"].add(line.strip())

stop_list = [
    "javascript",
    "div",
    "var",
    "indexes",
    "h3",
    "p",
    "color1",
    "url",
    "getElementByTagName",
    "xsl",
    "iaudio",
    "rss",
    "toString",
    "class",
    "css",
    "the",
    "au",
    "id",
    "DCTERMS",
    "www",
    "text",
    "span",
    "common",
    "style",
    "button",
    "onclick",
    "media",
    "trackEvent",
    "document",
    "color3",
    "footer",
    "title",
    "src",
    "local",
    "global",
    "gif",
    "UserRequest",
    "function",
    "primaryNavigation",
    "icontext",
    "m21",
    "meta",
    "content",
    "www",
    "href",
    "img",
    "types",
    "audio",
    "png",
    "0",
    "link",
    "addthis",
    "script",
    "name",
    "stylesheet",
    "The",
    "END",
    "true",
    "xmlengine",
    "ABC",
    "abc",
    "http",
    "and",
    "net",
    "alt",
    "li",
    "generic",
    "to",
    "type",
    "js",
    "rel",
    "htm",
    "nav",
    "of",
    "col1",
    "ul",
]

json_object = {
    "words": [],
    "urls": set()
}

for word, info in sorted(words.items(), key=lambda info: info[1]["count"]):
    if word in stop_list:
        continue

    try:
        word_as_int = int(word)
        if word_as_int > 9999:
            continue
    except ValueError:
        pass

    json_object["words"].append({
        "text": word,
        "size": info["count"]
    })

    json_object["urls"] |= info["urls"]


json_object["urls"] = list(json_object["urls"])

import json

print("var frequency_list = {};".format(json.dumps(json_object)))
