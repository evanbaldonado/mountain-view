# TIMS crash CSV precipitation adder

## Overview
[tims-crash-csv-precipitation-adder.py](tims-crash-csv-precipitation-adder.py) contains code to add information about precipitation conditions to CSV crash files from Transportation Injury Mapping System ([TIMS](https://tims.berkeley.edu/tools/query/)). The program is written in Python, and it adds additional an column for precipitation.

## Configuration
Configure the program by editing the first few lines of [tims-crash-csv-precipitation-adder.py](tims-crash-csv-precipitation-adder.py).
- INPUT_FILE is the name of the input CSV.
- OUTPUT_FILE is the name of the output CSV, which the program will create.

## Setup/usage
1. [Download Python](https://www.python.org/downloads/) if you don't already have it installed.
2. [Install Meteostat](https://dev.meteostat.net/python/), which determines the precipitation for a given location at a given time.
3. Run the program. From the folder containing the program, run `python3 tims-crash-csv-precipitation-adder.py` or `python tims-crash-csv-precipitation-adder.py` on the command line.
    - Optionally, you can also use command line arguments to set the input and output file (overrides the configuration). The first argument is the input file, and the second argument is the output file. Ex: `python3 tims-crash-csv-precipitation-adder.py INPUT_FILE_GOES_HERE OUTPUT_FILE_GOES HERE`

## Notes
- The input and output files cannot be the same.
- Meteostat has a weather code, but this is not always populated for our times/location so we use precipitation instead.
- Meteostat groups data by the hour. We assumed that an hour's data refers to precipitation for the hour after it. Ex: 1 p.m. data would be for 1 p.m. (inclusive) to 2 p.m. (exclusive).
- To determine which hourly bucket to associate with a crash time, we truncate the crash time. Ex: a 1:37 p.m. crash would have precipitation data from the 1 p.m. bucket. Note that the data is only precise to the hourly level, but this is the best approximation of precipitation we were able to find. It could have rained sometime during the hour but not during the exact time of the crash.
- See [demo.mov](demo.mov) for a demo.
