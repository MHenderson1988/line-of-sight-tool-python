import simplekml
import csv

def generatekml(folderoutput):
    kml = simplekml.Kml(open=1) #initialise kml object
    ##Create folder for radar and turbines
    radarfolder=kml.newfolder(name="Radars")
    turbinefolder=kml.newfolder(name="Turbines")
    lineofsightfolder=kml.newfolder(name="Lines of sight")

    ##Extract data from radar and turbine csv files##
    with open('../inputdata/radars.csv') as radarfile: #get radar data
        reader = csv.reader(radarfile, delimiter=',')
        for row in reader:
            radarlong=(float(row[0])) #convert to correct data types
            radarlat=(float(row[1]))
            radarheight=(float(row[2]))
            radarname=(row[3])
            
            ##create a point for the radar
            pnt = radarfolder.newpoint(name=(radarname), coords=[(radarlat, radarlong, radarheight)])
            pnt.altitudemode = simplekml.AltitudeMode.relativetoground
            pnt.extrude=1
            print('Creating a new point for: ' +radarname +' at: ' +str(radarlong) +','+str(radarlat))
            
            ##Open windfarm csv and store variables
            with open('../inputdata/windfarms.csv') as windfarmfile: #get windfarm data
                reader = csv.reader(windfarmfile, delimiter=',')
                for row in reader:
                    windfarmlong = (float(row[0])) #convert to correct data types
                    windfarmlat = (float(row[1]))
                    windfarmheight = (float(row[2]))
                    windfarmname = (row[3])
                    
                    ##Create a line from the radar to the windfarm
                    linestring = lineofsightfolder.newlinestring(name=((windfarmname) + (radarname)))
                    linestring.coords = [(radarlat, radarlong, radarheight), (windfarmlat, windfarmlong, windfarmheight)]
                    linestring.altitudemode = simplekml.AltitudeMode.relativetoground
                    print('Creating a line of sight between: ' +radarname +' and ' +windfarmname)

    ##Create new points for the turbines stored in list
        with open ('../inputdata/windfarms.csv') as turbinefile:
            reader = csv.reader(turbinefile, delimiter=',')
            for row in reader:
                windfarmlong = (float(row[0])) #convert to correct data types
                windfarmlat = (float(row[1]))
                windfarmheight = (float(row[2]))
                windfarmname = (row[3])
                pnt = turbinefolder.newpoint(name=(windfarmname))
                pnt.coords = [(windfarmlat,windfarmlong,windfarmheight)]
                pnt.altitudemode = simplekml.AltitudeMode.relativetoground
                pnt.extrude=1
                
    ##save the file
    kml.save(folderoutput + "/EGPK Windfarm Assessment.kml")
    print("Operation complete")        
