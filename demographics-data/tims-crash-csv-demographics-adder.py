#!/usr/bin/python

# IMPORTS
import sys
from csv import writer
from csv import reader

# CONFIG
INPUT_FILE = "../data/tims-crashes.csv" if not len(sys.argv) == 4 else sys.argv[1]
DEMOGRAPHICS_FILE = "../data/tims-victims.csv" if not len(sys.argv) == 4 else sys.argv[2]
OUTPUT_FILE = "../data/tims-crashes-with-demographics.csv" if not len(sys.argv) == 4 else sys.argv[3]

CASE_ID_HEADER, VICTIM_SEX_HEADER, VICTIM_AGE_HEADER = "CASE_ID", "VICTIM_SEX", "VICTIM_AGE";

# Fetch the demographics data and store it by CASE_ID.
demographics = {}
with open(DEMOGRAPHICS_FILE, 'r') as read_obj:
    csv_reader = reader(read_obj)

    # Handle the CSV's header.
    columnNames = []

    for row in csv_reader:
        columnNames = list(row)
        break

    caseIdIndex, victimSexIndex, victimAgeIndex = columnNames.index(CASE_ID_HEADER), columnNames.index(VICTIM_SEX_HEADER), columnNames.index(VICTIM_AGE_HEADER)

    # Loop through each row of the CSV.
    for row in csv_reader:
        caseId, victimSex, victimAge = row[caseIdIndex], row[victimSexIndex], row[victimAgeIndex]
        victimDemographic = str(victimAge) + str(victimSex)
        if caseId not in demographics:
            demographics[caseId] = str(victimDemographic)
        else:
            demographics[caseId] += (", " + victimDemographic)

# Open the input file in read mode and output file in write mode.
with open(INPUT_FILE, 'r') as read_obj, open(OUTPUT_FILE, 'w', newline='') as write_obj:
    csv_reader, csv_writer = reader(read_obj), writer(write_obj)

    # Handle the CSV's header.
    columnNames = []

    for row in csv_reader:
        row += ["VICTIM_DEMOGRAPHICS"]
        columnNames = list(row)
        csv_writer.writerow(row)
        break

    caseIdIndex = columnNames.index(CASE_ID_HEADER)

    # Loop through each row of the CSV.
    for row in csv_reader:
        caseId = row[caseIdIndex]
        if caseId in demographics:
            row += [demographics[caseId]]
        else:
            row += ["N/A"]

        # Add the updated row to the output file.
        csv_writer.writerow(row)
