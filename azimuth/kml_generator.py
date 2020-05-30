import csv

import simplekml


def generate_kml(folderoutput):
    kml = simplekml.Kml(open=1)  # initialise kml object

    # Create folder for radar and turbines

    radar_folder = kml.newfolder(name="Radars")
    turbine_folder = kml.newfolder(name="Turbines")
    line_of_sight_folder = kml.newfolder(name="Lines of sight")

    # Extract data from radar and turbine csv files
    with open('../inputdata/radars.csv') as radarfile:  # get radar data
        reader = csv.reader(radarfile, delimiter=',')
        for row in reader:
            radar_long = (float(row[0]))  # convert to correct data types
            radar_lat = (float(row[1]))
            radar_height = (float(row[2]))
            radar_name = (row[3])

            # Create a point for the radar
            pnt = radar_folder.newpoint(name=radar_name, coords=[(radar_lat, radar_long, radar_height)])
            pnt.altitudemode = simplekml.AltitudeMode.relativetoground
            pnt.extrude = 1
            print('Creating a new point for: ' + radar_name + ' at: ' + str(radar_long) + ',' + str(radar_lat))

            # Open windfarm csv and store variables
            with open('../inputdata/wind_farms.csv') as windfarmfile:  # get wind farm data
                reader = csv.reader(windfarmfile, delimiter=',')
                for row in reader:
                    wind_farm_long = (float(row[0]))  # Convert to correct data types
                    wind_farm_lat = (float(row[1]))
                    wind_farm_height = (float(row[2]))
                    wind_farm_name = (row[3])

                    # Create a line from the radar to the wind farm
                    linestring = line_of_sight_folder.newlinestring(name=(wind_farm_name + radar_name))
                    linestring.coords = [(radar_lat, radar_long, radar_height),
                                         (wind_farm_lat, wind_farm_long, wind_farm_height)]
                    linestring.altitudemode = simplekml.AltitudeMode.relativetoground
                    print('Creating a line of sight between: ' + radar_name + ' and ' + wind_farm_name)

        # Create new points for the turbines stored in list
        with open('../inputdata/wind_farms.csv') as turbinefile:
            reader = csv.reader(turbinefile, delimiter=',')
            for row in reader:
                wind_farm_long = (float(row[0]))  # Convert to correct data types
                wind_farm_lat = (float(row[1]))
                wind_farm_height = (float(row[2]))
                wind_farm_name = (row[3])
                pnt = turbine_folder.newpoint(name=wind_farm_name)
                pnt.coords = [(wind_farm_lat, wind_farm_long, wind_farm_height)]
                pnt.altitudemode = simplekml.AltitudeMode.relativetoground
                pnt.extrude = 1

    # Save the file
    kml.save(folderoutput + "/kml_assessment.kml")
    print("Operation complete")
