#!/usr/bin/python

# IMPORTS
import sys # For accepting user input
import json # For converting strings into dictionaries
import random # For picking random addresses

# CONFIG
INPUT_FILE = "../data/mountain-view-addresses.geojson" if not len(sys.argv) == 3 else sys.argv[1]
SAMPLE_SIZE = 30 if not len(sys.argv) == 3 else int(sys.argv[2]) # Size of the sample to be collected. 30 should be sufficient, as per the Central Limit Theorem: https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_probability/BS704_Probability12.html

# Read the input file into a list of dictionaries.
addressList = []
with open(INPUT_FILE, 'r') as read_obj:
    addressList = [json.loads(address) for address in read_obj.readlines()]

# Obtain a set of unique property addresses (multiple units in one property are considered duplicates).
addressSet = set([address['properties']['number'] + " " + address['properties']['street'] for address in addressList])

# Obtain a sample list of random addresses (with replacement).
addressSample = random.choices(list(addressSet), k = SAMPLE_SIZE)

# Print output.
print("\nOut of " + str(len(addressList)) + " total addresses in Mountain View, there are " + str(len(addressSet)) + " unique property addresses. Here is a random sample (with replacement) of " + str(SAMPLE_SIZE) + " of these unique property addresses:\n")
print("\n".join(addressSample))
