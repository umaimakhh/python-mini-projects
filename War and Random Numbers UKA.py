
'''
Assigment No:0702 -  War and Peace 
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/8VcDzZfGPYI
Date: 05/22/2020
I have not given or received any unauthorized assistance on this assignment
'''
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
        parValueswithBits: list with pair of tuples with bits - ('c','a',1)'''
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
         
def main():
    global file
    global fileSize
    global nextPosition
    global seedIncrement
    global final32BitList

    seedValue = getSelectedNumber()
    fileName = 'war-and-peace.txt'
    filePath = 'E:\DPU\Spring 2020 courses\Python Programming\week7\\' +fileName
    nextPosition = 0
    seedIncrement = 0

    file = open(filePath, 'r')
    file.seek(0, os.SEEK_END)# getting file size to track end of file to start genreating numbers again. 
    fileSize = file.tell()
    if(seedValue != 0):
            pngr = WarAndPeacePseudoRandomNumberGenerator(seedValue) # object of WarAndPeacePseudoRandomNumberGenerator
    else:
            pngr = WarAndPeacePseudoRandomNumberGenerator() # object of WarAndPeacePseudoRandomNumberGenerator


    pngr = WarAndPeacePseudoRandomNumberGenerator(seedValue) # object of WarAndPeacePseudoRandomNumberGenerator
    randomNumberRange = []
    for i in range(10000):
        randomNumberRange.append(pngr.random())
    print("Minimun",min(randomNumberRange))
    print("Maximum",max(randomNumberRange))
    print('Mean',str(sum(randomNumberRange)/len(randomNumberRange)))


main()