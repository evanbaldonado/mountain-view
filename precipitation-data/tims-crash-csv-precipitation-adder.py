#!/usr/bin/python

# IMPORTS
import sys
from csv import writer
from csv import reader
import datetime
import math
from meteostat import Hourly, Point

# CONFIG
INPUT_FILE = "../data/tims-crashes.csv" if not len(sys.argv) == 3 else sys.argv[1]
OUTPUT_FILE = "../data/tims-crashes-with-precipitation.csv" if not len(sys.argv) == 3 else sys.argv[2]

LATITUDE_HEADER, LONGITUDE_HEADER, DATE_HEADER, TIME_HEADER = "LATITUDE", "LONGITUDE", "COLLISION_DATE", "COLLISION_TIME"
TIMEZONE = "America/Los_Angeles"

# Open the input file in read mode and output file in write mode.
with open(INPUT_FILE, 'r') as read_obj, open(OUTPUT_FILE, 'w', newline='') as write_obj:
    csv_reader, csv_writer = reader(read_obj), writer(write_obj)

    # Handle the CSV's header.
    columnNames = []

    for row in csv_reader:
        row += ["PRECIPITATION"]
        columnNames = list(row)
        csv_writer.writerow(row)
        break

    latitudeIndex, longitudeIndex = columnNames.index(LATITUDE_HEADER), columnNames.index(LONGITUDE_HEADER)
    crashDateIndex, crashTimeIndex = columnNames.index(DATE_HEADER), columnNames.index(TIME_HEADER)

    # Loop through each row of the CSV.
    for row in csv_reader:

        crashDateString, crashTimeString = row[crashDateIndex], row[crashTimeIndex].zfill(4)
        crashYear, crashMonth, crashDay, crashHour, crashMinute = int(crashDateString[:4]), int(crashDateString[5:7]), int(crashDateString[-2:]), int(crashTimeString[:2]), int(crashTimeString[2:4])

        crashDate = datetime.date(crashYear, crashMonth, crashDay)
        crashDateStartTime = datetime.datetime(crashYear, crashMonth, crashDay)
        crashDateEndTime = datetime.datetime(crashYear, crashMonth, crashDay, 23, 59)
        crashTime = datetime.time(crashHour, crashMinute) if (0 <= crashHour and crashHour <= 24 and 0 <= crashMinute and crashMinute <= 60) else "INVALID TIME (" + str(crashHour).zfill(2) + ":" + str(crashMinute).zfill(2) + ")"
        crashTimeString = str(crashHour).zfill(2) + str(crashMinute).zfill(2)
        latitude, longitude = float(row[latitudeIndex]), float(row[longitudeIndex])

        # Check that the crash time is valid
        if isinstance(crashTime, str):
            row += [crashTime]
        else:
            meteostatPoint = Point(latitude, longitude)
            meteostatHourly = Hourly(meteostatPoint, crashDateStartTime, crashDateEndTime)
            meteostatHourlyData = meteostatHourly.fetch()

            precipitation = meteostatHourlyData.iloc[crashHour]['prcp'] # Note: 'coco' stores a weather code, but this is not always populated so we use precipitation instead.
            row += ["Y (" + str(precipitation) + "mm)"] if (precipitation != 0.0 and not math.isnan(precipitation)) else [""]

        # Add the updated row to the output file.
        csv_writer.writerow(row)
