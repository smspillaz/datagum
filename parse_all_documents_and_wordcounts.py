import os
from collections import defaultdict

import sys

wordlists = defaultdict(lambda: {"files": [], "count": 0})


def process_wordlist_filenames_for(filenames, word):
    return_filenames = set()

    for filename in filenames:
        with open(os.path.join("webs", "tmp", filename)) as f:
            for line in f.readlines():
                try:
                    parts = line.split()
                    if len(parts) < 2:
                        continue

                    if word in line:
                        return_filenames.add(filename)
                    # wordlists[line.split()[1]]["files"].append(filename)
                    # wordlists[line.split()[1]]["count"] += int(line.split()[0])
                except ValueError:
                    continue

    return return_filenames

last_filenames = set(os.listdir(os.path.join("webs", "tmp")))
for arg in sys.argv[1:]:
    last_filenames = process_wordlist_filenames_for(last_filenames, arg)

print("\n".join(last_filenames))
