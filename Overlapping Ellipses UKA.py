'''
Assigment No:0702 -  Overlapping ellipses 
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/j3B1uY4G5jo
Date: 05/22/2020
I have not given or received any unauthorized assistance on this assignment
'''
import math
import random
import turtle
import os

class WarAndPeacePseudoRandomNumberGenerator():
    '''represents an object of pngr'''

    def __init__(self, seed=0):
        '''init method'''
        self.pairValueWithProb = []
        self.seed = seed
        self.perviousCharacterPosition = 0

    def readSeedCharacter(self):
        '''returns a list of tuples with piars of characters
        tuple format : ('c','a')'''    
        global file
        global nextPosition
        global fileSize
        global seedIncrement
        listPairs = []
        step = 100 # step for the next position to pick character from

        while nextPosition < fileSize:
            y = 1
            while y <33: # get only 32 bits 
                    x = 1
                    perviousCharacter ='' # keeping track of pervious and curent character 
                    currentCharacter =''

                    while x<3: # get only 2 characters per iteration
                        pairValues = ()
                        if nextPosition != 0 and nextPosition < fileSize:
                            file.seek(nextPosition)
                        elif nextPosition == 0:
                            file.seek(self.seed+seedIncrement)
                        char = file.read(1) # read single character only
                        if x == 1:
                            perviousCharacter = char #add as a first element of the list 
                        else:
                            currentCharacter = char #add as a second element of the list 
                        if x == 2:
                            if perviousCharacter is not currentCharacter: #if both not same only then add the values to tuple
                                pairValues = perviousCharacter,currentCharacter    
                                listPairs.append(pairValues)
                        x =x+1
                        xs = file.tell()+step # keep track of next poistion as file.tell() keeps on moving
                        nextPosition = nextPosition + xs
                    y = y+1
                    final32BitList = listPairs
                    
        if(nextPosition > fileSize): #start if number genration is larger and reaches find end
                file.seek(self.seed+seedIncrement) #to avoid same number genration everytime the time reaches end add seedIncrement
                seedIncrement +=1
                nextPosition = 0
                xs = 0
        return final32BitList

    def setBits(self,listPairs):
        '''returns genrated bits to 1 for each tuple value if greater ASCI
        tuple format : ('c','a',1) or tuple format : ('c','a',0)
        Input Parameter:
        listpair: all pair of tuples in a list'''
        pairValuesWithBits = []
        for pairValue in (listPairs): 
            if pairValue[0] > pairValue[1]:
                pairValue = pairValue[0],pairValue[1],1  #if first character is greater than 2nd character add bit to 1
            else: 
                pairValue = pairValue[0],pairValue[1],0 #if first alpha is less than 2nd character add bit to 0
            pairValuesWithBits.append(pairValue)   # add updated tuples in a list 
        return (pairValuesWithBits)

    def genrateProbOfEachBit(self,parValueswithBits):
        '''returns list of tuples with all the probility included
        tuple format : ('c','a',1,1/x)
        Input Parameter:
        parValueswithBits: list with pair of tuples with bits - ('c','a',1) '''
        x = 2
        pairValueWithProb = []
        for pairValue in (parValueswithBits):
            prob = 1/x
            pairValue = pairValue[0],pairValue[1],pairValue[2],prob #adding prob to tuple
            x = x*2
            pairValueWithProb.append(pairValue)   # add updated tuples in a list 
        return (pairValueWithProb)

    def random(self):
        '''returns random number genrated from text file parsed from tuple list'''
        tupleofCharacterWithBits = self.setBits(self.readSeedCharacter()) #get character pairs and set bits accordinly

        pairValueWithProb = self.genrateProbOfEachBit(tupleofCharacterWithBits)
        numberEquation = 0.0 #intialize number
        for pairValue in (pairValueWithProb):
            if pairValue[2] == 1: # get all the open bits
                numberEquation = numberEquation + pairValue[3] # adding to genrate random number
        return (numberEquation)  

def getSelectedNumber():
    '''returns integer that user entered'''
    return abs(int(input('Enter Number for seed - if want to use the deaulft seed enter 0: '))) # returns user input returns only positive values

def initalizeFile():
    global file
    global fileSize
    global nextPosition
    global seedIncrement
    global final32BitList
    
    fileName = 'war-and-peace.txt'
    filePath = 'E:\DPU\Spring 2020 courses\Python Programming\week7\\' +fileName
    nextPosition = 0
    seedIncrement = 0

    file = open(filePath, 'r')
    file.seek(0, os.SEEK_END)
    fileSize = file.tell()

class Point():
    '''represents an object of point'''
    def __init__(self, xCordinate,yCordinate):
        '''init method'''
        self.xCordinate = xCordinate
        self.yCordinate = yCordinate

    def getXFocalPoint(self):
        '''returns X focal Point'''
        return self.xCordinate
    
    def getYFocalPoint(self):
        '''returns Y Focal Point'''
        return self.yCordinate

    def distance(self, otherPoint):
        'calculates the distance between 2 points'
        dist = math.sqrt((otherPoint.getXFocalPoint() - self.getXFocalPoint())**2 + (otherPoint.getYFocalPoint() - self.getYFocalPoint())**2)  
        return dist
    
    def __repr__(self):
        '''string representation Point(x, y)'''
        return 'Point({}, {})'.format(self.xCordinate, self.yCordinate)
        
class Ellipse():
    '''represents an object of Ellipse'''

    def __init__(self, p1,p2,width):
        '''init method'''
        self.p1 = p1
        self.p2 = p2
        self.width = width
    
    def getFocalPoint1(self):
        '''returns first pocal point of ellipise'''
        return self.p1
    
    def getFocalPoint2(self):
        '''returns 2nd pocal point of ellipise'''
        return self.p2

    def getWForPoints(self):
        '''returns the sum of the focal points'''
        return self.p1 + self.p2 

    def getWidith(self):
        '''returns the sum of the focal points'''
        return self.width    

    def isFocalPointsInEllipse(self,pointXCoordinate,pointYCoordinare):
        '''returns the true if focal points in the ellpise'''
        randomFocalPoint = Point(pointXCoordinate,pointYCoordinare)
        if self.p1.distance(randomFocalPoint) + self.p2.distance(randomFocalPoint) < self.width: # point withing the eclipes
            return True
        else:
            return False
    
def main():
    '''gets user details and intializes file'''
    global numberRange
    numberRange = 10000 # number of random genrated numbers to be executed

    initalizeFile() # intalize file

    #uncomment singal block one of the single block only

    focalPoint1X,focalPoint1Y,focalPoint2X,focalPoint2Y,focalPoint1Xe2,focalPoint1Ye2,focalPoint2Xe2,focalPoint2Ye2,widthfE1,widthfE2 = inputUser() # user input
    p1 = Point(focalPoint1X,focalPoint1Y)
    p2 = Point(focalPoint2X,focalPoint2Y)
    p3 = Point(focalPoint1Xe2,focalPoint1Ye2)
    p4 = Point(focalPoint2Xe2,focalPoint2Ye2)
    widthOfE1 =widthfE1
    widthOfE2 =widthfE1

    # for testing - 
    # p1 = Point(float(0),float(0))
    # p2 = Point(float(0),float(0))
    # p3 = Point(float(0),float(0))
    # p4 = Point(float(0),float(0))
    # widthOfE1 =float(2)
    # widthOfE2 =float(2)

    # p1 = Point(float(0),float(0))
    # p2 = Point(float(0),float(0))
    # p3 = Point(float(0),float(1))
    # p4 = Point(float(0),float(1))
    # widthOfE1 =float(2)
    # widthOfE2 =float(1)

    e1 = Ellipse(p1,p2,widthOfE1)
    e2 = Ellipse(p3,p4,widthOfE2)
    computeOverlapOfEllipses(e1,e2)

def inputUser():
    focalPoint1X,focalPoint1Y = getInputFromUser("Enter the position of 1st Focal Point(format:x y):",True)
    focalPoint1X=float(focalPoint1X)
    focalPoint1Y=float(focalPoint1Y)

    focalPoint2X,focalPoint2Y = getInputFromUser("Enter the position of 2nd Focal Point(format:x y):",True)
    focalPoint2X=float(focalPoint2X)
    focalPoint2Y=float(focalPoint2Y)

    focalPoint1Xe2,focalPoint1Ye2 = getInputFromUser("Enter the position of 1st Focal Point(format:x y): - E2 ",True)
    focalPoint1Xe2=float(focalPoint1Xe2)
    focalPoint1Ye2=float(focalPoint1Ye2)

    focalPoint2Xe2,focalPoint2Ye2 = getInputFromUser("Enter the position of 2nd Focal Point(format:x y): - E2 ",True)
    focalPoint2Xe2=float(focalPoint2Xe2)
    focalPoint2Ye2=float(focalPoint2Ye2)

    widthOfE1 = float(getInputFromUser("Enter width of the ellpise 1 ",False))
    widthOfE2 = float(getInputFromUser("Enter width of the ellpise 2 ",False))
    return focalPoint1X,focalPoint1Y,focalPoint2X,focalPoint2Y,focalPoint1Xe2,focalPoint1Ye2,focalPoint2Xe2,focalPoint2Ye2,widthOfE1,widthOfE2

def getInputFromUser(question,isSplit):
    '''returns value from user'''
    if isSplit:
       return input(question).split()
    else:
        return input(question)

def genrateAreaOfReactangle(leftRightX,leftRightY,
    topRightX,topRightY,leftBottomX,LeftBottomY,leftTopX,leftTopY):
    '''returns area of rectangle'''
    #genreating coordinates for rectangle 
    LR = Point(leftRightX, leftRightY)
    TR = Point(topRightX, topRightY)
    LL = Point(leftBottomX, LeftBottomY)
    TL = Point(leftTopX, leftTopY)
 
    #commuting length for area
    lengthOfRectange = LR.distance(TR)
    breathOfReactange = LR.distance(LL)

    return lengthOfRectange*breathOfReactange # area of Rectangle

def computeOverlapOfEllipses(e1,e2):
    #puting btoh elipse around box(l,r,t,b)

    leftRightX,leftRightY,topRightX,topRightY,leftBottomX,LeftBottomY,leftTopX,leftTopY = genrateRectangleCoordinates(e1,e2)

    areaOfRectangle = genrateAreaOfReactangle(leftRightX,leftRightY,
    topRightX,topRightY,leftBottomX,LeftBottomY,leftTopX,leftTopY)

    #scaling and shifting the number as for now its (0.0,1]
    minimunXValue = min(leftRightX,topRightX,leftBottomX,leftTopX)
    maxiumXValue = max(leftRightX,topRightX,leftBottomX,leftTopX)

    maxYValue = max(leftRightY,topRightY,LeftBottomY,leftTopY)
    miniumYValue = min(leftRightY,topRightY,LeftBottomY,leftTopY)

    #getting range of scaling factor
    rangeOfX = maxiumXValue - minimunXValue
    rangeOfY = maxYValue - miniumYValue

    # only one to be commented out
    count, number = getAreaOfOverLappiningRegion(rangeOfX,rangeOfY,minimunXValue,miniumYValue,maxiumXValue,maxYValue,e1,e2) #for getting without visual representation
    #count, number = getAreaOfOverLappiningRegionWithTurtleIllusration(rangeOfX,rangeOfY,minimunXValue,miniumYValue,maxiumXValue,maxYValue,e1,e2) # for getting visual representation
    percentage = count/number
    area= percentage*areaOfRectangle
    print('\n\nArea of the overlapping region is: {} for {} times genration of random points'.format(area,number))

def getAreaOfOverLappiningRegionWithTurtleIllusration(rangeOfX,rangeOfY,minimunXValue,miniumYValue,maxX,maxY,e1,e2):
    '''returns count number and draws Turtle Illustration with communting the counts of comman range by reach point'''
    global numberRange
        #creating object for pseudo random from previous assignment - composition
    pngr = WarAndPeacePseudoRandomNumberGenerator()
    numbRange = 0
    count = 0
    # draw illustration
    pngr = WarAndPeacePseudoRandomNumberGenerator()
    drawingT = turtle.Turtle()
    wn = turtle.Screen()
    wn.setworldcoordinates(-2,2,3,-2)
    drawingT = turtle.Turtle()
    drawingT.up()
    drawingT.goto(-1,0)
    drawingT.down()
    drawingT.goto(1,0)

    drawingT.up()
    drawingT.goto(0,1)
    drawingT.down()
    drawingT.goto(0,-1)
    drawingT.up()
    for randomPoints in range(numberRange):
        x = (pngr.random()* rangeOfX)+minimunXValue
        y = (pngr.random()* rangeOfY)+miniumYValue
        drawingT.goto(x,y)
        point = Point(x,y) # genrating random point
        if checkPointsInOverLappingRegion(e1,e2,point): #checking how often is point side the ellipsies.
            count += 1
            drawingT.color("blue")
        elif checkPointsInE1(e1,point):
            drawingT.color("red")
        elif checkPointsInE2(e2,point):
            drawingT.color("green")
        else:
            drawingT.color('#a0c8f0')
        drawingT.dot()
    wn.exitonclick()
    return count,numberRange
    
def checkPointsInE1(e1,point):
    '''returns true if point inside e1 of the'''
    if e1.isFocalPointsInEllipse(point.getXFocalPoint(),point.getYFocalPoint()):
        return True

def checkPointsInE2(e2,point):
    '''returns true if point inside e2 of the'''
    if e2.isFocalPointsInEllipse(point.getXFocalPoint(),point.getYFocalPoint()):
        return True

def getAreaOfOverLappiningRegion(rangeOfX,rangeOfY,minimunXValue,miniumYValue,maxX,maxY,e1,e2):
    '''communting the counts of comman range by reach point'''
    global numberRange
    #creating object for pseudo random from previous assignment - composition
    pngr = WarAndPeacePseudoRandomNumberGenerator()
    count = 0 # keeping count of the number of times point inside ellipse
    for randomPoints in range(0, numberRange):
        x = (pngr.random()* rangeOfX)+minimunXValue
        y = (pngr.random()* rangeOfY)+miniumYValue
        point = Point(x,y) # genrating random point
        if checkPointsInOverLappingRegion(e1,e2,point): #checking how often is point side the ellipsies.
            count += 1
    return count,numberRange
    
def checkPointsInOverLappingRegion(e1,e2,point):
    '''returns true if point inside even one of the ellipse'''
    if e1.isFocalPointsInEllipse(point.getXFocalPoint(),point.getYFocalPoint()) and e2.isFocalPointsInEllipse(point.getXFocalPoint(),point.getYFocalPoint()):
        return True  

def genrateRectangleCoordinates(e1,e2):
    '''getting all X and Y cordinataes of ellipies commutes max width box and return reactangle coordinates'''
    
    getAllXFocalPointsOfEllipse = []
    getAllYFocalPointsOfEllipse = []

     #getting all minimun X focal point 
    xe1pointFocal1 = e1.getFocalPoint1().getXFocalPoint()
    getAllXFocalPointsOfEllipse.append(xe1pointFocal1)
    
    xe1pointFocal2 = e1.getFocalPoint2().getXFocalPoint()
    getAllXFocalPointsOfEllipse.append(xe1pointFocal2)


    xe2pointFocal1 = e2.getFocalPoint1().getXFocalPoint()
    getAllXFocalPointsOfEllipse.append(xe2pointFocal1)

    xe2pointFocal2 = e2.getFocalPoint2().getXFocalPoint()
    getAllXFocalPointsOfEllipse.append(xe2pointFocal2)

    minimunFocalPointX = min(getAllXFocalPointsOfEllipse) #minimun Focal Point X cordinate From All both Ellipses
    maxFocalPointX = max(getAllXFocalPointsOfEllipse) #minimun Focal Point X cordinate From All both Ellipses

     #getting all minimun Y focal point 
    ye1pointFocal1 = e1.getFocalPoint1().getYFocalPoint()
    getAllYFocalPointsOfEllipse.append(ye1pointFocal1)
    
    ye1pointFocal2 = e1.getFocalPoint2().getYFocalPoint()
    getAllYFocalPointsOfEllipse.append(ye1pointFocal2)


    ye2pointFocal1 = e2.getFocalPoint1().getYFocalPoint()
    getAllYFocalPointsOfEllipse.append(ye2pointFocal1)

    ye2pointFocal2 = e2.getFocalPoint2().getYFocalPoint()
    getAllYFocalPointsOfEllipse.append(ye2pointFocal2)
   
    minimunFocalPointY = min(getAllYFocalPointsOfEllipse) #minimun Focal Point Y cordinate From All both Ellipses
    maxiumFocalPointY = max(getAllYFocalPointsOfEllipse) #max Focal Point Y cordinate From All both Ellipses

    #getting maxium width from both Epilices
    if e1.getWidith() > e2.getWidith():
        maximumWidth = e1.getWidith()
    else:
        maximumWidth = e2.getWidith()

    #genreating coordinates    

    LeftRightXCoordinate = maxFocalPointX + maximumWidth
    LeftRightYCoordinate = minimunFocalPointY - maximumWidth

    TopRightXCoordinate = maxFocalPointX + maximumWidth
    TopRightYCoordinate = maxiumFocalPointY + maximumWidth

    LeftBottomXCoordinate = minimunFocalPointX - maximumWidth
    LeftBottomYCoordinate = minimunFocalPointY - maximumWidth

    LeftTopXCoordinate = minimunFocalPointX - maximumWidth
    LeftTopYCoordinate = maxiumFocalPointY + maximumWidth

    return LeftRightXCoordinate,LeftRightYCoordinate,TopRightXCoordinate,TopRightYCoordinate,LeftBottomXCoordinate,LeftBottomYCoordinate,LeftTopXCoordinate,LeftTopYCoordinate


main()