from circle import Circle
import numpy as np
import matplotlib.pyplot as plt

def calcStartAngle(startY,centreY,startX,centreX):
    startAngle = np.arctan2(startY-centreY, startX-centreX)
    return startAngle

def calcEndAngle(endY,centreY,endX,centreX):
    endAngle = np.arctan2(endY-centreY, endX-centreX)
    return endAngle

def main():
    distance = 35
    radius = 3440.065
    
    #create circle object
    c1 = Circle(radius,distance)
    angle = c1.getDegrees()
    xc = c1.getXc()
    yc = c1.getYc()
    
    #set start and end points
    x1,y1 = 0,0
    x2,y2 = distance,0
    
    #get start and end angles
    startAngle = calcStartAngle(y1,yc,x1,xc)
    endAngle = calcEndAngle(y2,yc,x2,xc)
    angleList = np.linspace(startAngle,endAngle,distance)
    x_values = np.linspace(x1,x2,distance)
    y_valuesList = []
    
    for i in range(len(x_values)):
        y = radius*np.sin(angleList[i]) - c1.getArcHeight()
        y_valuesList.append(y)
    
    #Create numpy array to hold y values
    y_values = np.array(y_valuesList)
    
    plt.ylim(0,1)
    plt.plot(x_values,y_values)
    plt.show()

if __name__ == "__main__":
    main()