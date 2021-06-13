## Overview

This application allows the user to batch process multiple line of sight queries and output them in graphical form,
using data from the Google Elevation API. A .kml file is also produced for viewing in Google Earth.

### History

I wrote this application after being frustrated at the lack of simple, free tools for processing large batches of line
of sight calculations. I watched a co-worker spend an entire shift re-entering the same data again and again over 100
hundred times and save the output as a screenshot which then had to be cropped in MS paint.

Originally it was used to compare airport radars to proposed wind turbine developments however I have modified the
original to be used for any generic location or object you desire. I hope this helps someone out.

## Installation

### Cloning

```git clone https://github.com/MHenderson1988/line-of-sight-analysis.git```

Run gui.py and follow the on-screen instructions.

### Before you start

To run the application, in it's current form, you will require -

* A valid 'Google Elevation API' key
* 2x Valid .csv files

### Valid CRS (Coordinate reference systems)

Currently the application can convert between the following -

* Decimal latitude/longitude\
* Eastings and Northings\

### Example .csv file

Update - May 2021 All csv processing is now automated for Eastings and Northings and decimal degrees. OS Grid no longer
supported due to inaccuracy.  
Accepted csv headings - 'Latitude, Longitude, Height, Name' or 'Easting, Northing, Height, Name' (in any order).
![An example of a valid .csv file using decimal latitude/longitude](img/csv_example.png)

The above example uses decimal latitude/longitude.

Row 1 - Latitude (Float)\
Row 2 - Longitude (Float)\
Row 3 - Height, in metres (int/float)\
Row 4 - Unique name (String)

### Example output

Graphical output will look like this -

![An example of the matplotlib output](img/example_output.png)

The green line shows the path taken between the top point of the first and second locations. Below is the imposed
elevation data which has been manipulated to the simulated curvature of the earth (shown by the orange arc).

The plotted line which illustrates the line of sight will be coloured green if line of sight exists. If a disruption to
the view is detected then the line will be coloured red.

## Current limitations

Currently the application has the following limitations -

* Earth curvature is calculated, assuming that the Earth is a perfect sphere
* Only Google Elevation API is currently supported
* Only natural terrain is accounted for. This application does not take foliage or man-made objects/buildings into
  account
