# TIMS crash CSV sunrise and sunset adder

## Overview
[tims-crash-csv-sunrise-and-sunset-adder.py](tims-crash-csv-sunrise-and-sunset-adder.py) contains code to add information about sunrise, sunset, dawn, and dusk times to CSV crash files from Transportation Injury Mapping System ([TIMS](https://tims.berkeley.edu/tools/query/)). The program is written in Python, and it adds additional columns for sunrise, sunset, dawn, and dusk times to the CSV. It also flags crashes that are within a certain amount of time from sunrise/sunset/dawn/dusk.

## Configuration
Configure the program by editing the first few lines of [tims-crash-csv-sunrise-and-sunset-adder.py](tims-crash-csv-sunrise-and-sunset-adder.py).
- INPUT_FILE is the name of the input CSV.
- OUTPUT_FILE is the name of the output CSV, which the program will create.
- THRESHOLD_IN_MINUTES is the threshold (inclusive) for how close a crash time must be to a time event (ex: sunrise) to be flagged.

## Setup/usage
1. [Download Python](https://www.python.org/downloads/) if you don't already have it installed.
2. [Install Astral](https://astral.readthedocs.io/en/latest/), which helps calculate the sunrise, sunset, dawn, and dusk times at a given location on a given day.
3. Run the program. From the folder containing the program, run `python3 tims-crash-csv-sunrise-and-sunset-adder.py` or `python tims-crash-csv-sunrise-and-sunset-adder.py` on the command line.
    - Optionally, you can also use command line arguments to set the input and output file (overrides the configuration). The first argument is the input file, and the second argument is the output file. Ex: `python3 tims-crash-csv-sunrise-and-sunset-adder.py INPUT_FILE_GOES_HERE OUTPUT_FILE_GOES HERE`

## Notes
- The input and output files cannot be the same.
- See [demo.mov](demo.mov) for a demo.
