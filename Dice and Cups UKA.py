'''
Assigment No:0501 -  Dice and Cups 
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/iH1PjmKVJPw
Date: 05/2/2020
I have not given or received any unauthorized assistance on this assignment
'''

import random


class SixSidedDie:
    '''represents a Sixe Sided Die - Base class for Twenty Sided Die and Ten sided Die'''

    def roll(self):
        '''returns random value of six sided die'''
        self.facevalue=random.randint(1, 6) # random values from 1 to 6
        return self.facevalue 

    def getFaceValue(self):
        '''returns current die value'''
        return self.facevalue

    def __repr__(self):
        ''''returns string representation of an SixSidedDie object created'''
        return 'SixSidedDice({})'.format(self.facevalue) 
        
class TenSidedDie(SixSidedDie):
    '''represents a Ten Sided Die'''
        
    def roll(self): # Overriding methods
        '''returns random value of ten sided die'''
        self.facevalue=random.randint(1, 10) # random values from 1 to 10
        return self.facevalue 

    def __repr__(self):# Overriding methods
        ''''returns string representation of an TenSidedDie object created'''
        return 'TenSidedDie({})'.format(self.facevalue) 

class TwentySidedDie (SixSidedDie):
    '''represents a Twenty Sided Die'''
        
    def roll(self): # Overriding methods
        '''returns random value of Twenty sided die'''
        self.facevalue=random.randint(1, 20) # random values from 1 to 20
        return self.facevalue 
    
    def __repr__(self): # Overriding methods
        ''''returns string representation of an TwentySidedDie object created'''
        return 'TwentySidedDie({})'.format(self.facevalue) 

class Cup:
    '''represents a cup object'''

    totalSum = 0 # inital sum zero

    def __init__(self,SixSidedDiceTimes=1,TenSidedDiceTimes = 1,TwentySidedDieTimes = 1): # deafult values for each Dice is 
        self.SixSidedDiceTimes=SixSidedDiceTimes
        self.TenSidedDiceTimes=TenSidedDiceTimes
        self.TwentySidedDieTimes=TwentySidedDieTimes
        self.Dice=[] # intializing list to store all dice objects


    def roll(self):
        '''returns total sum from each roll cup that commutes rolled values from each die'''
        totalSum = 0      
        sumSixSidedDice = self.calculateSumofEachDice(self.SixSidedDiceTimes,1) # calculating sum of each roll
        sumTenSidedDice = self.calculateSumofEachDice(self.TenSidedDiceTimes,2)
        sumTwentySidedDice = self.calculateSumofEachDice(self.TwentySidedDieTimes,3)
        totalSum = sumSixSidedDice + sumTenSidedDice + sumTwentySidedDice # total sum 
        return totalSum

    def calculateSumofEachDice(self,sumRange,diceType):
        '''returns calculated sum of each roll
        Input parameters:

        sumRange = Integer value for the number of times die rolled
        diceType = can be 1,2 or 3 as 1 -> SixSidedDice, 2 -> TenSidedDie , 3 -> TwentySidedDie
        '''
        totalSum = 0 #intialize sum = 0
        for turn in range(sumRange):
            diceObject =self.getDiceObject(diceType)  
            totalSum += diceObject.roll() # roll die - explicitly delegates task to die class - composition
            self.Dice.append(diceObject) # add die object to list
        return totalSum   
    
    def getDiceObject(self,diceType):
        '''returns diceObject for any diceType
         diceType = can be 1,2 or 3 as 1 -> SixSidedDice, 2 -> TenSidedDie , 3 -> TwentySidedDie
        '''
        if diceType == 1:
            diceObject = SixSidedDie() # explicitly creating object of die class - composition
        if diceType == 2:
            diceObject = TenSidedDie()
        if diceType == 3:
            diceObject = TwentySidedDie()
            
        return diceObject
    
    def getSum(self):
        '''returns total sum of each dice item'''
        totalSum = 0
        for diceType in self.Dice:
            totalSum += diceType.getFaceValue()  #calculating sum for each Die face
        return totalSum
    
    def __repr__(self):
        '''returns the count for seach die - string representation of an each die object'''
        output ='Cup('
        lengthOfDice = len(self.Dice)
        count = 0
        for itemValue in self.Dice: 
            output += itemValue.__repr__()
            count += 1
            if (count != lengthOfDice): # if values still in add comma
                output += ', '
        output += ')' # adding comma at end
        return output
    
# for testing outputs - as this class is being used by the other classes - commented out these commands so that they dont show in the other class when I call this file
# d = Cup(1,1,2)
# print(d.roll())
# print(d.getSum())
# print(d)

# d = Cup(1,3,2)
# print(d.roll())
# print(d.getSum())
# print(d)

# d = Cup()
# print(d.roll())
# print(d.getSum())
# print(d)



            


