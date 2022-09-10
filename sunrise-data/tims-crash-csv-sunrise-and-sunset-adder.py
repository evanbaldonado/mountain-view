#!/usr/bin/python

# IMPORTS
import sys
from csv import writer
from csv import reader
import datetime
from astral import LocationInfo
from astral.sun import sun

# CONFIG
INPUT_FILE = "../data/tims-crashes.csv" if not len(sys.argv) == 3 else sys.argv[1]
OUTPUT_FILE = "../data/tims-crashes-with-sunrise-sunset-dawn-and-dusk.csv" if not len(sys.argv) == 3 else sys.argv[2]
THRESHOLD_IN_MINUTES = 30 # threshold (inclusive) for how close a crash time must be to a time event (ex: sunrise) to be flagged.

LATITUDE_HEADER, LONGITUDE_HEADER, DATE_HEADER, TIME_HEADER = "LATITUDE", "LONGITUDE", "COLLISION_DATE", "COLLISION_TIME"
TIMEZONE = "America/Los_Angeles"

# Open the input file in read mode and output file in write mode.
with open(INPUT_FILE, 'r') as read_obj, open(OUTPUT_FILE, 'w', newline='') as write_obj:
    csv_reader, csv_writer = reader(read_obj), writer(write_obj)

    # Handle the CSV's header.
    columnNames = []

    for row in csv_reader:
        row += ["SUNRISE_TIME", "SUNRISE_FLAG", "SUNSET_TIME", "SUNSET_FLAG", "DAWN_TIME", "DAWN_FLAG", "DUSK_TIME", "DUSK_FLAG"]
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
        crashTime = datetime.time(crashHour, crashMinute) if (0 <= crashHour and crashHour <= 24 and 0 <= crashMinute and crashMinute <= 60) else "INVALID TIME (" + str(crashHour).zfill(2) + ":" + str(crashMinute).zfill(2) + ")"
        crashTimeString = str(crashHour).zfill(2) + str(crashMinute).zfill(2)
        latitude, longitude = float(row[latitudeIndex]), float(row[longitudeIndex])

        location = LocationInfo(timezone=TIMEZONE, latitude=latitude, longitude=longitude)
        s = sun(location.observer, date=crashDate, tzinfo=location.timezone)

        # Add in sunrise, sunset, dawn, and dusk data for the given row.
        for timeEventString in ("sunrise", "sunset", "dawn", "dusk"):
            timeEvent = s[timeEventString]
            timeEventTimeString = str(timeEvent.hour).zfill(2) + str(timeEvent.minute).zfill(2)

            # Add sunrise/sunset/dawn/dusk time.
            row += [timeEventTimeString]

            # Add sunrise/sunset/dawn/dusk flag.
            if not isinstance(crashTime, str):
                crashDatetime = datetime.datetime(crashYear, crashMonth, crashDay, crashHour, crashMinute, 0)
                timeEventDatetime = datetime.datetime(crashYear, crashMonth, crashDay, timeEvent.hour, timeEvent.minute, 0)
                minutesApart = (crashDatetime - timeEventDatetime).total_seconds() / 60
                if abs(minutesApart) <= THRESHOLD_IN_MINUTES:
                    if minutesApart == 0: row += ["at " + timeEventString]
                    elif minutesApart < 0: row += [str(int(abs(minutesApart))) + " minutes before " + timeEventString]
                    else: row += [str(int(abs(minutesApart))) + " minutes after " + timeEventString]
                else:
                    row += [""]
            else:
                row += [crashTime]

        # Add the updated row to the output file.
        csv_writer.writerow(row)
