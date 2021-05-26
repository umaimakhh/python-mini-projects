'''
Assigment No:0402 - Human Pyramid
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/MdsBH2YPkiU
Date: 04/26/2020
I have not given or received any unauthorized assistance on this assignment
'''

def mainHumanPyramid():
    global weightInPounds
    weightInPounds = 128 
    print('\n \n---- Human Pyramid ----- check humans weight that is on their backs in the pyramid when the each human has a weight in pounds of: ' + str(weightInPounds))
    rowValue = enterRowValueAndValid()
    columnValue = enterColumnValueAndValidNumber()
    if (rowValue is not -1 and columnValue is not -1): # if value validated sucessfully 
        print(humanPyramid(rowValue,columnValue))


def humanPyramid(row, column):
    '''returns the weight in pounds of the specific human
    Input paramter:
    row: integer value
    column: integer value
    Reference: https://web.stanford.edu/class/archive/cs/cs106x/cs106x.1192/assignments/recursion.html'''    
    print(row,column) # for testing
   
    if row == 0:
        return 0.0 # if on top the head - e.g Human A
    elif column == 0:
        return (weightInPounds + humanPyramid(row - 1, column)) / 2 # extreme left human = e.g B or D
    elif column == row:
        return (weightInPounds + humanPyramid(row - 1, column - 1)) / 2 # etreme right humans, only carrring one weight above them for e.g C or F
    else:
        return weightInPounds + (humanPyramid(row - 1, column - 1) / 2) + (humanPyramid(row - 1, column) / 2) # humans carrying weight of 2 for e.g M or I 
        
def enterRowValueAndValid():
    '''returns true if entered number is integer'''
    try: 
        numberRow = abs(int(input('Enter Number for row value: ')))
    except:
        print('Please enter correct row value')
        return -1
    else:
        return numberRow

def enterColumnValueAndValidNumber():
    '''returns true if entered number is integer'''
    try: 
        numberColumn =  abs(int(input('Enter Number for column value: ')))
    except:
        print('Please enter correct column value')
        return -1
    else:
        return numberColumn


mainHumanPyramid()


