import multiprocessing

import sys

import json

from urllib2 import urlopen

import os

with open("Localphotostories2009-2014-JSON.json", "r") as photo_stories:
    structure = json.loads(photo_stories.read().decode("utf-8", errors="ignore"))

print(sys.argv[0])

for story in structure:
    print("URL " + story["URL"] + " " + story["Title"])
    if story["URL"]:
        if os.path.exists(os.path.basename(story["URL"])):
            story["URL"] = os.path.basename(story["URL"])
            continue

        try:
            url_f = urlopen(story["URL"])
            with open(os.path.basename(story["URL"]), "w") as l_f:
                l_f.write(url_f.read())
            story["URL"] = os.path.basename(story["URL"])
            url_f.close()
        except Exception:
            print("Error getting " + story["URL"])
            story["URL"] = ""


open("json", "w").write(json.dumps(structure))
