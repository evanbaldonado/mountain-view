# Police report PDF highlighter

## Overview
[sample-addresses.py](sample-addresses.py) contains code to select a random sample (with replacement) of property addresses in Mountain View, from a geojson list from [OpenAddresses](https://batch.openaddresses.io/location/188). The program's output is written directly to the command line.

## Configuration
Configure the program by editing the first few lines of [sample-addresses.py](sample-addresses.py).

- INPUT_FILE is the name of the input geojson. It is expected to have one address per line, in the format from [OpenAddresses](https://batch.openaddresses.io/location/188).
- SAMPLE_SIZE is the size of the sample (how many addresses) to take.

## Setup/usage
1. [Download Python](https://www.python.org/downloads/) if you don't already have it installed.
2. Run the program. From the folder containing the program, run `python3 sample-addresses.py` or `python sample-addresses.py` on the command line.
    - Optionally, you can also use command line arguments to set the input file (overrides the configuration). The first argument is the input file, and the second argument is the sample size. Ex: `python3 sample-addresses.py INPUT_FILE_GOES_HERE SAMPLE_SIZE_GOES_HERE`

## Notes
- A sample size of 30 addresses should be sufficient, as per the [Central Limit Theorem (CLT)](https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_probability/BS704_Probability12.html). The CLT also states that sampling should be done with replacement (allow for the possibility of the same address being picked multiple times).
- The geojson input file contains separate entries for each address, including units at a single property address. So as not to double-count or unfairly weight any given property address, [sample-addresses.py](sample-addresses.py) counts each property address only once, regardless of how many units it may contain.
- See [demo.mov](demo.mov) for a demo.
