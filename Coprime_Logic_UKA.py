'''
Assigment No: 1 - Grading Logic Assigment
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/hz-m7Imsf9c
Date: 04/05/2020
I have not given or received any unauthorized assistance on this assignment
'''
import timeit


def coprime_test_loop():
    '''Prompts the user if their entered numbers are coprime or not.
    These questions are asked until the user press Q button to exit 
    '''
    userLogOut = False #  maintaing user state for exit : inital state first time false
    while(userLogOut == False):
        
        print('Press Q if you want to exit') # only Character 'Q' used to detect user log out
        mFirstNumber = input('Enter the first number: ')
        if mFirstNumber == 'Q':
            userLogOut == True # if user presses Q, user log out state changed
            break
        mSecondNumber = input('Enter second number: ')
        if mSecondNumber == 'Q':
            userLogOut == True # if user presses Q, user log out state changed
            break
      

        if mFirstNumber.isnumeric() and mSecondNumber.isnumeric():
            isPairCoprime = coprime(int(mFirstNumber), int(mSecondNumber)) # boolean value true if coprime
          
            if isPairCoprime:
                decision = 'are'
            else:
                decision = 'are not'
            print('The numbers '+mFirstNumber 
            +' and ' + mSecondNumber + ' ' + decision + ' coprime numbers')
        else:
            print('----------- Invalid Input -----------') # error print incase entered input is not in numbers

       

def coprime(firstNumber,secondNumber):
    '''returns true or false if the two numbers are coprime or not.
    **coprime numbers: Numbers with 1 as the only positive integer factor. 
    Input Type:
    parameter 1: Any Number
    parameter 2: Any Number
    '''
    mGreatestCommonFactor = commuteGreatestCommonFactor(firstNumber,secondNumber) # value of greatest common factor
    if mGreatestCommonFactor == 1: # number combination is coprime if mGreatestCommonFactor = 1
        return True
    return False

def commuteGreatestCommonFactor(numberOne,numberTwo):
    '''returns largest positive integer that divides both numberOne and numberTwo 
    using Euclidean algorithm.
    Reference taken: https://en.wikipedia.org/wiki/Euclidean_algorithm

    commuteGreatestCommonFactor(numberOne,numOne%numberTwo)
    numOne % numberTwo (remainder) becomes our numberTwo and repeated until the remainder becomes 0
    when the remainder numOne % numberTwo is 0 then numberTwo is our Greatest Common Factor
    
    Input Type:
    parameter 1: Any Number
    parameter 2: Any Number
    '''
    if numberOne == 0 or numberTwo == 0:
        return 0

    while numberOne % numberTwo > 0: # will countinue until remainder is 0
        remainder = numberOne % numberTwo # remainder computed to be assignment to numberTwo
        numberOne = numberTwo
        numberTwo = remainder # assigning value of the remainder to numberTwo for the next computation of numberOne % numberTwo
    return numberTwo



# efficiency check excuation time for testing purpose    
# print(timeit.timeit("""for i in range(1,45): 
#         if 45%i == 0 and 77%i == 0:
#             hcf = True
#         else:
#             hcf = False"""))
       
# print(timeit.timeit(
# """numberOne = 45 
# numberTwo = 77
# while numberOne % numberTwo > 0:
#     remainder = numberOne % numberTwo
#     numberOne = numberTwo
#     numberTwo = remainder"""))
   
coprime_test_loop()


