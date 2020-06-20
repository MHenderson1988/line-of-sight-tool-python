# This class reads both sets of location data from the .csv files and transforms the comparisons into .kml
# files.  Kml files are for use with Google Earth and will allow you to see 3D representations of the line of
# sight analysis.  For best results please ensure 3D terrain is enable in Google Earth.

import simplekml


# This method returns a new kml object and creates the required folders for the program - one for each set of locations
# and one for the line of sight lines.  Takes two lists of location objects (The ones to be compared) and the names of
# folders to store them in, as its arguments.

def create_kml_file(first_location_list, second_location_list, first_folder_name, second_folder_name, output_folder):
    kml_object, kml_folder_list_one, kml_folder_list_two, kml_folder_linestring = initialise_folders(first_folder_name,
                                                                                                     second_folder_name)
    first_location_points = create_points(first_location_list, kml_folder_list_one)
    second_location_points = create_points(second_location_list, kml_folder_list_two)
    linestrings = create_linestrings(first_location_list, second_location_list, kml_folder_linestring)
    save_string = output_folder + "/line_of_sight_analysis.kml"
    kml_object.save(save_string)
    return print(".kml file saved to - " + save_string)


# Returns a simpleKML object, a KML folder for the first AND second locations, and a folder for the line of sight
# objects.  Takes the names of the two folders to create, as its arguments.

def initialise_folders(first_folder_name, second_folder_name):
    kml = simplekml.Kml(open=1)
    folder_one = kml.newfolder(name=first_folder_name)
    folder_two = kml.newfolder(name=second_folder_name)
    line_of_sight_folder = kml.newfolder(name="Lines of sight")
    return kml, folder_one, folder_two, line_of_sight_folder


# Returns a list of points for the given list of locations.  Takes a list of location objects and the folder in which
# to store the points, as it's arguments.

def create_points(location_list, which_folder):
    points_list = []
    for i in range(len(location_list)):
        loc_one_lat, loc_one_long = location_list[i].latitude, location_list[i].longitude
        loc_one_height, loc_one_name = location_list[i].height, location_list[i].name
        point = which_folder.newpoint(name=loc_one_name, coords=[(loc_one_long, loc_one_lat, loc_one_height)])
        point.altitudemode = simplekml.AltitudeMode.relativetoground
        point.extrude = 1
        points_list.append(point)
    return points_list


# Returns a list of linestrings (used to indicate line of sight between the two matched locations).  Takes two lists
# of location objects and the folder to store the line strings in as its arguments.

def create_linestrings(location_list_one, location_list_two, linestring_folder):
    linestring_list = []
    for x in range(len(location_list_one)):
        for i in range(len(location_list_two)):
            first_coordinates = location_list_one[x].coordinates_yx
            second_coordinates = location_list_two[i].coordinates_yx
            linestring = linestring_folder.newlinestring(
                name=(location_list_one[x].name + ', ' + location_list_two[i].name))
            linestring.coords = [first_coordinates, second_coordinates]
            linestring.altitudemode = simplekml.AltitudeMode.relativetoground
            linestring_list.append(linestring)
    return linestring_list
