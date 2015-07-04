datagum; Revolutionizing Research
=================================

Datagum picks up data like your shoe picks up gum. It scans the entire
content of a research repository up-front to generate an interactive
method for performing searches.

Users click on a word from an available repository of words in a research
body to continually filter down a list of available documents. This solves
the problem of needing to know the exact terminology that a document
uses, since it is already availabel to the user.

datagum uses its own 3sheet.io server by default to scan a list of
documents obtained from Trove and historical ABS Census Data.

Generating a test research repository
=====================================

Assuing that a repository of documents exists in a subdirectory called `webs`,
you can use a bash script to generate a word count for a set of downloaded
documents like so:

    mkdir tmp ; for n in webs/* ; do cat "$n" | tr -sc '[:alnum:]' '\n' | sort | uniq -ic | sort -rn > "./tmp/$n" ; done

Then, you can use `parse_all_documents_for_wordcounts.py` to generate a
list of files containing the superset of the words specified on the commandline.

Pipe the output to `wordcounts_for_stdin.py` to get a global word-count, which
generates a JS variable to be pasted into the `index.html` file.

Downloading a test set of documents
===================================

The included `read_abc_new_json_file.py` reads the `Localphotostories2009-2014-JSON.json`
file obtained from ABC news and downloads every document referred to in it.

Use of open-source technologies
===============================

datagum uses `d3.js` for visualization of counted words and `bootstrap` as
a scaffolding for the web user-interface.