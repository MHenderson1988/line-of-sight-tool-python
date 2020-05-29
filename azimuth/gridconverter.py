from OSGridConverter import grid2latlong
import csv
import string
from pyproj import Proj, transform

def convertgridsxy(file):
    mylist=[]
    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            inProj = Proj(init='epsg:27700')
            outProj = Proj(init='epsg:4326')
            x, y = row[0],row[1]
            x, y = transform(inProj,outProj,x,y)
            lat=y
            long=x
            height=row[2]
            name=row[3]
            towrite=lat, long, height, name
            mylist.append(towrite)
            print(towrite)

        with open('../inputdata/windfarms.csv', "w", newline='') as csvfile:
            print("Writing windfarms.csv: 0%")
            writer=csv.writer(csvfile)
            writer.writerows(mylist)
            print("Writing windfarms.csv: 100%")

def convertgrids(file):
    
    mylist=[]
    ALPHA = string.ascii_letters

    with open(file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            if row[0].startswith(tuple(ALPHA)):
                l=grid2latlong(row[0])
                lat=float(l.latitude)
                long=float(l.longitude)
                lat=format(lat, '4f')
                long=format(long, '4f')
                height=row[1]
                name=row[2]
            else:
                lat=float(row[0])
                long=float(row[1])
                lat=format(lat, '4f')
                long=format(long, '4f')
                height=row[2]
                name=row[3]

            towrite=lat, long, height, name
            mylist.append(towrite)
            print(towrite)

    with open('../inputdata/windfarms.csv', "w", newline='') as csvfile:
        print("Writing windfarms.csv: 0%")
        writer=csv.writer(csvfile)
        writer.writerows(mylist)
        print("Writing windfarms.csv: 100%")
        
if __name__ == '__main__':
    convertgridsxy('../inputdata/grid.csv')