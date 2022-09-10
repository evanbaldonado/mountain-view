# TIMS crash CSV demographics adder

## Overview
[tims-crash-csv-demographics-adder.py](tims-crash-csv-demographics-adder.py) contains code to add demographic information from CSV victim files to CSV crash files, both from Transportation Injury Mapping System ([TIMS](https://tims.berkeley.edu/tools/query/)). The program is written in Python, and it adds a single additional column containing a comma-separated list of victim demographics.

## Configuration
Configure the program by editing the first few lines of [tims-crash-csv-demographics-adder.py](tims-crash-csv-demographics-adder.py).
- INPUT_FILE is the name of the input CSV.
- DEMOGRAPHICS_FILE is the name of the demographics CSV.
- OUTPUT_FILE is the name of the output CSV, which the program will create.

## Setup/usage
1. [Download Python](https://www.python.org/downloads/) if you don't already have it installed.
2. Run the program. From the folder containing the program, run `python3 tims-crash-csv-demographics-adder.py` or `python tims-crash-csv-demographics-adder.py` on the command line.
    - Optionally, you can also use command line arguments to set the input and output file (overrides the configuration). The first argument is the input file, the second argument is the demographics file, and the third argument is the output file. Ex: `python3 tims-crash-csv-demographics-adder.py INPUT_FILE_GOES_HERE DEMOGRAPHICS_FILE_GOES_HERE OUTPUT_FILE_GOES HERE`

## Notes
- If the program enters seemingly nonsensical values such as "998-", the issue may lie in the source data. [data/tims-victims.csv](../data/tims-victims.csv) has some typos.
- The input and output files cannot be the same.
- See [demo.mov](demo.mov) for a demo.
