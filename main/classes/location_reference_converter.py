# The location_reference_converter.py class allows for the translation of cartesian references into
# latitude and longitude.

import csv


# This method reads the .csv file column headings and outputs the correct conversion
def identify_columns(file):
    with open(file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        header = reader.fieldnames
        for words in header:
            if words == 'Easting':
                print("Easting/Northings detected... Converting...")
                return 'osbg'
            if words == 'Latitude':
                print("Decimal latitude/Longitude detected...")
                return 'latlong'
            else:
                return Exception("Did not detect latitude/longitude, eastings/northings or British National Grid "
                                 "Reference.  Check you have labelled your columns correctly!")
