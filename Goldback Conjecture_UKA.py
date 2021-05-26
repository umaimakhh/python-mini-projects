import timeit
'''
Assigment No:301 - Goldbach Conjecture
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/8jqoMIraClM
Date: 04/20/2020
I have not given or received any unauthorized assistance on this assignment
'''

def mainGoldBachConjecture():
    '''main function that commutes gold bach Conjecture''' 
    global maxLimit
    maxLimit = 100
    minLimit = 4
    primeNumberList = primeNumbersBySeiveOfEratosthenes(maxLimit)
    evenNumberList = commuteEvenNumbersListFromMax(minLimit,maxLimit)
    goldBachConjectureDict = saveSumOfPrimesInDict(evenNumberList,primeNumberList)
    finalParsedList = parseGolfBachConjectureFormat(goldBachConjectureDict,evenNumberList)
    printFinalParsedList(finalParsedList)  

def primeNumbersBySeiveOfEratosthenes(numberLimit):
    '''returns list of prime numbers by  sieve of Eratosthenes algorithm from the given list
    Input parameters: 
    rangeList : Range List
    References: https://www.youtube.com/watch?v=V08g_lkKj6Q
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    '''
    numberLimit = numberLimit + 1
    isPrime =[True]*(numberLimit) # intialy mark all values as true in an array
    multiplier = 2 # as check multiples starting from 2
    while multiplier <= numberLimit ** 0.5:
        if isPrime[multiplier] == True: # checks on each True Value 
            multiple = (multiplier**2) #1 check for multiples of the multipler, starting would check on 2 
            i = 1
            while multiple <= numberLimit: 
                isPrime[multiple] = False # for all multiples change thier index value to False
                multiple = (multiplier**multiplier) + i*(multiplier)   # commpute next multiple of that multiplier
                i += 1    
        multiplier += 1
    return primeNumbers(isPrime)

def primeNumbers(isPrime):
    '''returns prime list of all the values that are true in the input paratmeter list'''
    primeNumberList = []
    indexVale = 0
    for primeValue in isPrime:
        if primeValue:
            primeNumberList.insert(indexVale,indexVale) # indexValue is a prime number if isprime == true
        indexVale += 1  # incrementing indexValue which is also keeping track of the number    
    return(primeNumberList[2:])

def sumOfPrimes(evenNum,primeNumberList):
    ''' returns a list of tupes that are the sum of two prime numbers from the targeted number'''
    pairList = [] # intialize list to store tuple values as sum of primes
    i = 0
    for primeNumber in primeNumberList:
        for primeNumber2 in primeNumberList:
            if primeNumber+primeNumber2 == evenNum and primeNumber<=primeNumber2: #primeNumber<=primeNumber2 would not give repeated vals for e.g x+y and y+x is the same
                pair = primeNumber,primeNumber2 # add values in tuple
                pairList.insert(i,pair) # insert tuple in list
                i += 1
    return pairList


def commuteEvenNumbersListFromMax(minLimit,maxLimit):
    '''returns a list of even numbers till the max limit provdided
    Input parameter: 
    minLimit : minLimit integer value
    maxLimit : maxium integer value'''
    listofEvenNumbers = []
    i = 0
    for evenNos in range(minLimit,maxLimit+1,2): # generate even numbers still number, number+1 to include number as a evenNumber
        listofEvenNumbers.insert(i,evenNos)
        i +=1
    return listofEvenNumbers

def saveSumOfPrimesInDict(listofEvenNums,primeNumberList):
    '''returns a dictionary storing all the even numbers as a key and all the sum of pairs as thier value
    Input parameters:
    listofEvenNums: list of even numbers
    primeNumberList: list of prime numbers'''
    goldBachConjectureDict = {}
    for evenNumber in listofEvenNums: 
        goldBachConjectureDict.update({evenNumber:sumOfPrimes(evenNumber,primeNumberList)}) # for all numbers in list find sum of primes and store in dictionary
    return goldBachConjectureDict

def parseGolfBachConjectureFormat(goldBachConjectureDic,evenNumberList):
    '''prints the final pair values of prime
    Input parameters:
    goldBachConjectureDic: Dictiory with a format of key-> even number and value as sum of two primes ->(x,y)
    evenNumberList: Even number list that are present in goldBachConjectureDic as the key values'''
    finalParsedList = []
    for evenNumber in sorted(evenNumberList):
        for dicKey, dicValue in goldBachConjectureDic.items():
            i = 0
            finalParsedString = ''
            if dicKey == evenNumber:
                for tupleValues in dicValue:
                    finalParsedString = str(evenNumber) +' = '+ str(tupleValues[0]) + ' + ' +str(tupleValues[1])
                    finalParsedList.insert(i,(finalParsedString))
                    i += 1
    return (finalParsedList)

def createListFromRange(minLimit,maxLimit):
    '''returns a list of all the interger values between the limit provided
    Input parameters:
    minLimit: Integer value to start the list from
    maxLimit: Integer value to end the list'''
    rangeList = []
    i = 0
    for value in range(2,101):
        rangeList.insert(i,value)
        i += 1
    return rangeList

def printFinalParsedList(finalParsedList):
    '''prints the sum of pairs of all even numbers in format 'X+Y = W'''
    print('------ GoldBach Conjecture for first', +maxLimit,'values ------')
    for parsedVal in reversed(finalParsedList):
        print(parsedVal)

def justForTesting():
    ''''this function prints out the time of the two ways to commute prime factors, notice the two time is by using Seive Of Eratosthenes
    alogorthim which is much more faster and optimized'''

    print(timeit.timeit("""rangeList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    for naturalNumber in range(2,len(rangeList)):
        for sVale in rangeList:
            if naturalNumber != sVale and (sVale % naturalNumber) == 0:
                mulitple = rangeList.index(sVale)
                rangeList.pop(mulitple)"""))

    print(timeit.timeit("""import math
    numberLimit = 15
    isPrime =[True]*(numberLimit)
    multiplier = 2 
    while multiplier <= math.sqrt(numberLimit):
        if isPrime[multiplier] == True: 
            multiple = (multiplier**2)
            i = 1
            while multiple <= numberLimit:
                isPrime[multiple] = False
                multiple = (multiplier**multiplier) + i*(multiplier)   
                i += 1    
        multiplier += 1"""))

mainGoldBachConjecture()


    


        
    
    




         
        
