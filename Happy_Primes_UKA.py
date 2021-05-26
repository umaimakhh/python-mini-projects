'''Assigment No:302 - Happy Numbers
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/KvkPKblvAHM
Date: 04/21/2020
I have not given or received any unauthorized assistance on this assignment

Reference: https://www.youtube.com/watch?v=Mr215Wb9ks8

19 is a happy prime
83 101 is a sad prime
4 is a sad non prime
94 is a happy non prime
'''

def mainHappyNumber():
    '''main function that checks if the number entered is happy or sad number'''
    if enterAndValidNumber():
        isHappyNumber = commuteHappyNumber() # checks if number is happy or not
        printFinalDecision(isHappyNumber)   
        
def enterAndValidNumber():
    '''returns true if entered number is integer'''
    global number
    try: 
        number = (getSelectedNumber())
    except:
        print('Please enter integers value to process further')
        return False
    else:
        return True
    
def getSelectedNumber():
    '''returns integer that user entered'''
    return abs(int(input('Enter Number to check: '))) # returns user input returns only positive values

def splitNumber(numberToSplit):
    '''returns the split numbers in tuples -> if number is 45 returns (4,5)'''
    numberToSplitTuple = () # initailize tuple
    for digitSplit in repr(numberToSplit):
        numberToSplitTuple += (digitSplit,) # add digits to tuple 
    return numberToSplitTuple

def commuteHappyNumber():
    '''returns true if enetered number is happy number and false if sad number
    sad number is when the sum of square of digits end in 4'''
    value =  splitNumber(number) # intialy spit the entered number
    squaredSum = addSquareOfEachSplit(value) # intialy sum the entered number splits
    while checkHappyNumber(squaredSum): # repeat until either sum of squared number is 1 or not equal to 4 
        value = splitNumber(squaredSum)
        squaredSum = addSquareOfEachSplit(value)
    if squaredSum == 4: # number is sad number
        return False
    elif squaredSum == 1: # number is happy number
        return True

def checkHappyNumber(squaredSum):
    '''returns true if commuted sum has reached to 1 or is not 4'''
    return squaredSum is not 1 and squaredSum != 4

def addSquareOfEachSplit(numberToSplitTuple):
    '''returns the sum of square values in tuple
    Input Parameter: 
    numberToSplitTuple : tuple with orginal number split'''
    value = 0
    indexValue = 0
    while checkIfLimit(indexValue,numberToSplitTuple): # check to only iterate until on tuple size 
       value += int(numberToSplitTuple[indexValue])**2 # square index value and add to pervious squared value
       indexValue += 1
    return value
              
def checkIfLimit(indexValue,numberToSplitTuple):
    ''' returns if values have reached all the total tuples
    Input parameter: 
    indexValue: integer value of index
    numberToSplitTuple: tuple with digits'''
    return indexValue < len(numberToSplitTuple) # true if index value less than the length of tuple

def printFinalDecision(isHappyNumber):
    '''prints the final decision of happy number on the basis of the input parameter isHappyNumber
    Input Parameter:
    isHappyNumber: boolean value'''
    isPrimeNumber = checkPrime() # true if number is prime
    if isPrimeNumber and isHappyNumber:
        print(str(number) + ' is a Happy Prime')
    elif isPrimeNumber and not isHappyNumber:
        print(str(number) + ' is a Sad Prime')
    elif not isPrimeNumber and isHappyNumber:
        print(str(number) + ' is a Happy non Prime')
    elif not isPrimeNumber and not isHappyNumber:
        print(str(number) + ' is a sad non Prime')

def checkPrime():
    '''returns true if enetered number by the user is a prime number'''
    for value in range(2,number):
        return number % value != 0

mainHappyNumber()
        


        