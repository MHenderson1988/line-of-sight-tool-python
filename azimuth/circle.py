import numpy as np

class Circle:

    def __init__(self,radiusOfCircle,lengthOfArc):
        self.radius = radiusOfCircle
        self.circumference = 2 * np.pi * self.radius
        self.diameter = self.radius * 2
        self.arcLength = lengthOfArc
        self.degrees = self.calcDegrees()
        self.radians = self.calcRadians()
        self.chordLength = self.calcChordLength()
        self.sagitta = self.calcSagitta()
        self.arcHeight = self.calcArcHeight()
        self.segmentArea = self.calcSegmentArea()
        self.centreToChord = self.calcCentreToChord()
        self.xc = self.calcCircularCentreX()
        self.yc = self.calcCircularCentreY()
        
    #Setters and getters for the Circle class (TODO: setters)
    def getRadius(self):
        return self.radius

    def getCircumference(self):
        return self.circumference

    def getDiameter(self):
        return self.diameter

    def getArcLength(self):
        return self.arcLength

    def getRadians(self):
        return self.radians

    def getDegrees(self):
        return self.degrees

    def getChordLength(self):
        return self.chordLength

    def getSagitta(self):
        return self.sagitta
    
    def getArcHeight(self):
        return self.arcHeight

    def getSegmentArea(self):
        return self.segmentArea

    def getCentreToChord(self):
        return self.centreToChord
    
    def getXc(self):
        return self.xc
    
    def getYc(self):
        return self.yc

    #Define Circle class methods

    #Calculate the central angle, in degrees, by using the arcLength
    def calcDegrees(self):
        self.degrees = (self.arcLength / (np.pi * self.diameter)) * 360 #Gives angle in degrees at centre of the circle between the two points (beginning and end points of arcLength)
        return self.degrees

    #Calculate the central angle in radians, between two points on the circle
    def calcRadians(self):#Where theta is the angle between both points at the centre of the circle
        self.radians = np.radians(self.degrees) # Convert degrees to radians to work with ChordLength formula
        return self.radians

    #Returns the chord lengths of the arc, taking theta (angle in radians) as it's argument
    #The chord is the horizontal line which separates the arc segment from the rest of the circle
    def calcChordLength(self):
        self.chordLength = 2*self.radius*np.sin(self.radians/2) #formula works for theta (radians) only, not degrees #confirmed using http://www.ambrsoft.com/TrigoCalc/Sphere/Arc_.htm
        return self.chordLength

    #Calculates the length of arc, taking theta (angle in radians) as its argument.
    def calcArcLength(self):
        self.arcLength = (self.degrees/360)*self.diameter*np.pi #confirmed using http://www.ambrsoft.com/TrigoCalc/Sphere/Arc_.htm
        return self.arcLength

    #Calculates the sagitta of the arc segment.  The sagitta is the horizontal line which extends from the bottom
    #of the circle to the chord of the segment
    def calcSagitta(self):
        self.sagitta = self.radius - (np.sqrt((self.radius**2)-((self.chordLength/2)**2))) #Confirmed correct against online calculator https://www.liutaiomottola.com/formulae/sag.htm
        return self.sagitta
    
    #Calculate the height of the arc
    #Radius - sagitta of the segment
    def calcArcHeight(self):
        self.arcHeight = self.radius - self.sagitta
        return self.arcHeight

    #Calculates the area of the circular segment/arc).
    def calcSegmentArea(self):
        self.segmentArea = (self.radians - np.sin(self.radians) / 2) * self.radius**2
        return self.segmentArea

    #Calculate the height of the arc showing distance FROM the centre of the circle
    #Radius - sagitta of the segment
    def calcCentreToChord(self):
        self.centreToChord = self.radius - self.sagitta
        return self.centreToChord

    #Calculate centre point of circle
    #x 
    def calcCircularCentreX(self):
        self.xc = self.getChordLength()/2
        return self.xc
    
    def calcCircularCentreY(self):
        self.yc = self.getSagitta() - self.getRadius()
        return self.yc
        