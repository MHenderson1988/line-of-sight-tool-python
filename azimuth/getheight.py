import csv
import math
import urllib.request
import json
import matplotlib.pyplot as plt
import time
import numpy as np
from circle import Circle

def calcStartAngle(startY,centreY,startX,centreX):
    startAngle = np.arctan2(startY-centreY, startX-centreX)
    return startAngle

def calcEndAngle(endY,centreY,endX,centreX):
    endAngle = np.arctan2(endY-centreY, endX-centreX)
    return endAngle

##Extract data from radar and turbine csv files##
def generate_elevation(folderoutput):
    with open('../inputdata/radars.csv') as csvfile: #get radar data
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            #START-END POINT
            P1=[]
            P2=[]
            
            radarlong=(float(row[0])) #convert to correct data types
            radarlat=(float(row[1]))
            radarheight=(float(row[2]))
            radarname=(row[3])
            
            radarlong=(radarlong)
            radarlat=(radarlat)
            
            P1.append(radarlong)
            P1.append(radarlat)

        ##Open windfarm csv and store variables
        
            with open('../inputdata/windfarms.csv') as csvfile: #get windfarm data
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    windfarmlong = (float(row[0])) #convert to correct data types
                    windfarmlat = (float(row[1]))
                    windfarmheight = (float(row[2]))
                    windfarmname = (row[3])
                           
                    P2=[windfarmlong, windfarmlat]
                    
                    print(P1, P2)
                    
                    #NUMBER OF POINTS
                    s=200
                    interval_lat=(P2[0]-P1[0])/s #interval for latitude
                    interval_lon=(P2[1]-P1[1])/s #interval for longitude

                    #SET A NEW VARIABLE FOR START POINT
                    lat0=P1[0]
                    lon0=P1[1]

                    #LATITUDE AND LONGITUDE LIST
                    lat_list=[lat0]
                    lon_list=[lon0]
                    
                    print("Generating path")
                    #GENERATING POINTS
                    for i in range(s):
                        lat_step=lat0+interval_lat
                        lon_step=lon0+interval_lon
                        lon0=lon_step
                        lat0=lat_step
                        lat_list.append(lat_step)
                        lon_list.append(lon_step)
                        
                    print("Path Generated")
                    
                    #HAVERSINE FUNCTION
                    def haversine(lat1,lon1,lat2,lon2):
                        lat1_rad=math.radians(lat1)
                        lat2_rad=math.radians(lat2)
                        lon1_rad=math.radians(lon1)
                        lon2_rad=math.radians(lon2)
                        delta_lat=lat2_rad-lat1_rad
                        delta_lon=lon2_rad-lon1_rad
                        a=math.sqrt((math.sin(delta_lat/2))**2+math.cos(lat1_rad)*math.cos(lat2_rad)*(math.sin(delta_lon/2))**2)
                        d=2*6371000*math.asin(a)
                        return d
                    
                    print("Calculating distance")
                    
                    #DISTANCE CALCULATION
                    d_list=[]
                    for j in range(len(lat_list)):
                        lat_p=lat_list[j]
                        lon_p=lon_list[j]
                        dp=haversine(lat0,lon0,lat_p,lon_p)/1000 #km
                        dp=dp*0.539957 #convert km to nm
                        d_list.append(dp)
                    d_list_rev=d_list[::-1] #reverse list

                    print("Distance calculated")

                    try:
                        print("Sending request")
                        #SEND REQUEST
                        api_key= ""##Your google elevation api key here
                        samples='&samples=' + str(s)
                        radarPos=str(radarlong) + ',' + str(radarlat)
                        turbinePos=str(windfarmlong) + ',' + str(windfarmlat)
                        url='https://maps.googleapis.com/maps/api/elevation/json?path=' + radarPos + '|' + turbinePos + samples + api_key
                        print(url)
                        response = urllib.request.Request(url,headers={'Content-Type': 'application/json'})
                        fp=urllib.request.urlopen(response)
                        
                        #RESPONSE PROCESSING
                        res_byte=fp.read()
                        res_str=res_byte.decode("utf8")
                        js_str=json.loads(res_str)
                        #print (js_mystr)
                        fp.close()
                        print("Processing response")
                        
                        #Create circle and generate earth curvature
                        radius = 3440.065 #in nm

                        #create circle object
                        c1 = Circle(radius,d_list_rev[-1])
                        angle = c1.getDegrees()
                        xc = c1.getXc()
                        yc = c1.getYc()
                        
                        #set start and end points
                        x1,y1 = 0,0
                        x2,y2 = d_list_rev[-1],0
                        
                        #get start and end angles
                        startAngle = calcStartAngle(y1,yc,x1,xc)
                        endAngle = calcEndAngle(y2,yc,x2,xc)
                        angleList = np.linspace(startAngle,endAngle,s)
                        x_values = np.linspace(x1,x2,s)
                        y_valuesList = []
                        
                        for i in range(len(x_values)):
                            y = radius*np.sin(angleList[i]) - c1.getArcHeight()
                            y = y * 1852 #convert nautical miles to meters
                            y_valuesList.append(y)
                        
                        #Create numpy array to hold y values of earth curve
                        y_values = np.array(y_valuesList)

                        #GETTING ELEVATION
                        response_len=len(js_str['results'])
                        elev_list=[]
                        for j in range(response_len):
                            elev_list.append(js_str['results'][j]['elevation'] + y_values[j])
                        #Add or reduce height to simulate curve of earth at 7.98 inch per mile
                        startLOS = elev_list[0] + radarheight
                        endLOS = elev_list[-1] + windfarmheight

                        #BASIC STAT INFORMATION
                        mean_elev=round((sum(elev_list)/len(elev_list)),3)
                        min_elev=min(elev_list)
                        max_elev=max(elev_list)
                        distance=d_list_rev[-1]
                        
                        del d_list_rev[-1]
                        print(len(d_list_rev))
                        print(len(elev_list))

                        print("Plotting line of sight profile")
                        
                        #PLOT ELEVATION PROFILE
                        base_reg=0
                        plt.figure(figsize=(10,4))
                        plt.plot(d_list_rev,elev_list)
                        plt.plot(x_values,y_values)
                        plt.plot([0,distance],[min_elev,min_elev],'--g',label='min: '+str(min_elev)+' m')
                        plt.plot([0,distance],[max_elev,max_elev],'--r',label='max: '+str(max_elev)+' m')
                        plt.plot([0,distance],[mean_elev,mean_elev],'--y',label='ave: '+str(mean_elev)+' m')
                        plt.plot([0,distance],[startLOS, endLOS])##line of sight line
                        plt.fill_between(d_list_rev,elev_list,base_reg,alpha=0.1)
                        plt.text(d_list_rev[0],elev_list[0],radarname)
                        plt.text(d_list_rev[-1],elev_list[-1],windfarmname)
                        plt.xlabel("Distance(Nm)")
                        plt.ylabel("Elevation(m)")
                        plt.grid()
                        plt.legend(fontsize='small')
                                            
                        print('Saving...')
                        
                        filename= radarname + windfarmname
                        
                        ##Save the graph
                        plt.savefig(folderoutput + '/' +  ' ' + filename)
                        plt.close()
                        
                        print(filename + ' ' + 'saved...')
                        time.sleep(3)
                    except Exception as e:
                        print(str(e))

if __name__ == "__main__":
    generate_elevation('../lineofsight_graphs')
