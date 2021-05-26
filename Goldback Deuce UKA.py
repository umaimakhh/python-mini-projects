'''
Assigment No:0401 - Goldbach deuce
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/iW8wIDD1mB8
Date: 04/25/2020
I have not given or received any unauthorized assistance on this assignment
'''

import random
def mainGoldBachDeuce():
    '''main function that commutes gold bach Ducue'''
    global randomStartRange, randomEndRange # global varibles for the range of numbers in a list
    randomStartRange = 100
    randomEndRange = 0
    numberRange = enterAndValidNumberRange() # gets user input  and validates for number of elements in list
    number = enterAndValidNumber() # gets user input  and validates on which sum of pairs exists in list
    if((numberRange is not 0) and (number is not 0)): # if validation successfully then move further
        genrateRandomList = sorted(genrateRandomListFromN(numberRange)) # random list
        searchCombinations(number,genrateRandomList)
        print(genrateRandomList)
   


def enterAndValidNumber():
    '''returns true if entered number is integer'''
    try: 
        number = (getSelectedNumber())
    except:
        print('Please enter integers value to process further')
        return 0
    else:
        return number

def enterAndValidNumberRange():
    '''returns true if entered number is integer'''
    try: 
        number = (getSelectedNumberForRange())
    except:
        print('Please enter integers value to process further')
        return 0
    else:
        return number
    
def getSelectedNumber():
    '''returns integer that user entered'''
    return abs(int(input('Enter Number to check sum: '))) # returns user input returns only positive values

def getSelectedNumberForRange():
    '''returns integer that user entered'''
    return abs(int(input('Enter Number of elements you want to check from random range 0 - 100: '))) # returns user input returns only positive values


def genrateRandomListFromN(num): 
    '''returns a random list of N numbers with the max and minium range provided
    Input parameter:
    num = No. of elements for the list'''
    randomRangeList = [] 
    for indexValue in range(num): 
        randomRangeList.append(random.randint(randomEndRange,randomStartRange)) # creating random values in range
    return randomRangeList 

def searchCombinations(number,numberRangeList):
    '''returns the combinations of sum of pairs if it exists in the random list
    Input parameter:
    number = the number for which pairs are to be found
    numberRangeList = list of random numbers'''
    sumOfPairs = ()
    for indexValue in numberRangeList:
        pairIndex = communteSumOfPairsBinarySearch(number - indexValue,numberRangeList,0,len(numberRangeList) - 1) #initial low and high values
        if pairIndex > 1 and indexValue > pairIndex: # pairIndex value if greater than 1 - means sum exists
            sumOfPairs = pairIndex,indexValue # add pair in tuple
            print(sumOfPairs)
    if len(sumOfPairs) == 0:
        print('No sums of pairs found in list')
    


def communteSumOfPairsBinarySearch(number,numberRangeList,mLowValue,mHighValue):
    '''returns number from through binary search if found else it would return -1 
    Input parameter:
    number: Integer value that needs to check on the list 
    numberRangeList: random list of integers
    mLowValue: start index for the search
    mHighValue: end index till the search will be perfomed'''
    if mLowValue > mHighValue: # we searched everywhere now mLowValue has exceeded mHighValue index still number not found
        return -1
    middleValue = int((mLowValue + mHighValue)/2) # finding middle index
    value = numberRangeList[middleValue] # value at the middle index
    if value == number: # item found
        return value
    elif number < value: # item still not found
        return communteSumOfPairsBinarySearch(number,numberRangeList,mLowValue,middleValue - 1)  # change mHighValue index as next left to pervious middle index value - left hand side list
    else: # item still not found
        return communteSumOfPairsBinarySearch(number,numberRangeList,middleValue + 1,mHighValue) # change mLowValue index as next right index to pervious middle index - right hand side list


mainGoldBachDeuce()
