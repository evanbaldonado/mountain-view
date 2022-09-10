# Police report PDF highlighter

## Overview
[police-report-pdf-highlighter.py](police-report-pdf-highlighter.py) contains code to parse police crash reports (PDF form) to identify whether driveways or sight triangles/visibility issues may be associated with various crashes. The program is written in Python, and it automatically highlights keywords in the PDF.

## Configuration
Configure the program by editing the first few lines of [police-report-pdf-highlighter.py](police-report-pdf-highlighter.py).
- INPUT_FILE is the name of the input PDF.
- OUTPUT_FILE is the name of the output PDF, which the program will create.
- HIGHLIGHT_WORDS is a list of the words to highlight.

## Setup/usage
1. [Download Python](https://www.python.org/downloads/) if you don't already have it installed.
2. [Install PyMuPDF](https://pymupdf.readthedocs.io/en/latest/installation.html), which helps highlight the PDF.
3. Run the program. From the folder containing the program, run `python3 police-report-pdf-highlighter.py` or `python police-report-pdf-highlighter.py` on the command line.
    - Optionally, you can also use command line arguments to set the input and output file (overrides the configuration). The first argument is the input file, and the second argument is the output file. Ex: `python3 police-report-pdf-highlighter.py INPUT_FILE_GOES_HERE OUTPUT_FILE_GOES HERE`

## Notes
- The full crash report summaries from MVPD are intentionally not included in this repository because we did not obtain permission to publish them at the time of writing. See [data/example-police-reports.pdf](../data/example-police-reports.pdf) for a PDF file to test this script on.
- The input and output files cannot be the same.
- See [demo.mov](demo.mov) for a demo.
