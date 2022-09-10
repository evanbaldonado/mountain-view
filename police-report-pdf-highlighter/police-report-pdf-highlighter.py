#!/usr/bin/python

# IMPORTS
import sys
import fitz # Before importing, first, you'll need to install PyMuPDF.

# CONFIG
INPUT_FILE = "../data/example-police-reports.pdf" if not len(sys.argv) == 3 else sys.argv[1]
OUTPUT_FILE = "../data/example-police-reports-highlighted.pdf" if not len(sys.argv) == 3 else sys.argv[2]
HIGHLIGHT_WORDS = sorted(["driveway", "ingress", "egress", "garage", "backing", "reversing", "house", "housing", "duplex", "apartment", "complex", "parking lot", "parking garage", "exit", "exited", "exiting"])

HIGHLIGHT_WORDS_FORMATTED =  " and ".join('"' + highlightWord + '"' for highlightWord in HIGHLIGHT_WORDS) if (len(HIGHLIGHT_WORDS) < 3) else '," '.join([('"' + highlightWord) if (index != len(HIGHLIGHT_WORDS) - 1) else ('and "' + highlightWord) for index, highlightWord in enumerate(HIGHLIGHT_WORDS)]) + '"'

# Check if HIGHLIGHT_WORDS is empty.
if len(HIGHLIGHT_WORDS) < 1:
    print("Error: no search words to highlight specified. Please set HIGHLIGHT_WORDS")
    quit()

# Open the input PDF.
document = fitz.open(INPUT_FILE)
print("\nHighlighting the term" + ("s" if len(HIGHLIGHT_WORDS) > 1 else "") + " " + HIGHLIGHT_WORDS_FORMATTED + " in " + INPUT_FILE + "\n")

# Process each page of the input PDF.
for page in document:
    print("Processing " + str(page) + ".")

    # Highlight all instances of target words.
    for instance in [page.search_for(highlightWord) for highlightWord in HIGHLIGHT_WORDS]:
        page.add_highlight_annot(instance)

# Save the output as a PDF
document.save(OUTPUT_FILE)
print("\nHighlighted document saved to " + OUTPUT_FILE + "\n")
