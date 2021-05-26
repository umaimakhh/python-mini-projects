
'''
Assignment No: 0202 - Stem and Leaf plot
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/-gUXrM5HVrE
Date: 04/14/2020
I have not given or received any unauthorized assistance on this assignment
'''

def computeStemLeafMain():
    '''main function that shows users greetings passing entered file name for futher computing the stem and leaf plot'''

    userLogOut = False #  maintaing user state for exit : inital state first time false
    while(userLogOut == False):
        showUserGreetings()
        selectedFileName = getSelectedInputFile() # file name that the user entered
        if(selectedFileName == 'Q'): # if user pressed Q then exit loop
            userLogOut == True
            break
        else:
            dataListFromFile = parseDataFromFileName(selectedFileName) # file name passed to get the data from the file stored in list 
            displayStemAndLeaf(dataListFromFile) # main stem and leaf comuptation
    
def showUserGreetings():
    ''' displays user greetings with names of files that should entered for computing the stem and leaf plot'''
    
    print('\n------------ Welcome to the Stem And Plot diagram -----------')
    print('------------ Enter 1 , 2 or 3 to select the file to view its stem and leave plot -----------')
    print('------------ Name of First File:  1 -----------') # file name 1
    print('------------ Name of Second File: 2 -----------') # file name 2
    print('------------ Name of Third File:  3 -----------') # file name 3

def getSelectedInputFile():
    '''returns file name that user entered'''
    return input('Enter file name to check for the stem and leaf plot or Q to exit ') # returns user input
     
def getSelectedFilePath(selectedFileName):
    '''returns file path across the selected file name - directory would change once code transfered
    Current Directory: E:\DPU\Spring 2020 courses\Python Programming
    '''
    filePath = 'E:\DPU\Spring 2020 courses\Python Programming\\' # file stored in this directory, make the same directory or change directory path to run
    
    if selectedFileName == '1':
       return filePath + 'StemAndLeaf1.txt' # file name in directory folder
    elif selectedFileName == '2':
        return filePath +'StemAndLeaf2.txt'
    elif selectedFileName == '3':
        return filePath +'StemAndLeaf3.txt'
    else:
        return '0'
    
def getDataFromSelectedFile(parseFileNameFromInput):
    '''returns data from reading the selected file'''
    dataList = [] # intialize list
    i = 0
    infile = open(parseFileNameFromInput, "r") # opens file form the path provided - r specifies read file only
    lineList = infile.readlines() # returns list containing each line in the file as a list item
    infile.close()
    for i in range ( 0, len(lineList) ):
        x = int(lineList[i].strip()) # strip removes additional space if any 
        dataList.insert(i,x)
        i = i + 1
    return dataList

def parseDataFromFileName(selectedFileName):
    '''returns data from selected file'''
    if isCorrectInputFileName(selectedFileName): # if file name 1, 2 or 3 then proceed further
        parseFileNameFromInput = getSelectedFilePath(selectedFileName)
        dataReadFromFile = getDataFromSelectedFile(parseFileNameFromInput)
    else:
        print('Incorrect file name, please choose from the given infromation') # show error if incorrect file name entered
        quit()
    return dataReadFromFile

def isCorrectInputFileName(selectedFileName):
    ''' returns true or false if file name correct'''
    return selectedFileName == '3' or selectedFileName == '2' or selectedFileName == '1'

def displayStemAndLeaf(dataListFromFile):
    '''display the final stem and leaf plot'''
    allStemDataList = parseStemValuesFromDataList(dataListFromFile) # list giving all stem values from the input data list
    computeFinalStemLeaf(allStemDataList, dataListFromFile) # final function to compute and print plot      
            

def computeFinalStemLeaf(stemDataList,dataListFromFile):
    '''prints the final stem and leaf plot
    Input parameters: 
        1) List with stem values extracted from the orginal data list - stemDataList
        2) Orginal data list - dataListFromFile
    '''
    print('\n------------ STEM AND LEAF PLOT ------------\n')
    print('\nKey: X | Y coresponds to XY\n')
    for stemDataListValue in stemDataList: 
        x = ''
        for mainlist in sorted(dataListFromFile): 
            firstIndexValue = int((str(mainlist)[:-1])) # removes the last index value (leaf) from the element 
            while equalStemAndIndex(firstIndexValue,stemDataListValue): # if true then leaf value would be of the current stem value
                x += ' '+ (str(mainlist)[-1:]) # append leaf values to the x as leaves could be more than one
                break
        print(str(stemDataListValue) + ' |' + (x) ) # print once the whole iteration of single stemDataListValue done
    
def equalStemAndIndex(firstIndexValue,stemDataListValue):
    '''returns if the iterated stem value list is equal to the first value of the data list'''
    return firstIndexValue == stemDataListValue
    
def parseStemValuesFromDataList(dataListFromFile):
    '''returns all the stem values
    Input Parameter: Orginal data list - dataListFromFile
    '''
    stemList = []
    i = 0
    for data in sorted((dataListFromFile)):
        if isNoUnrepeatedValue(data,stemList): # check for unrepeated values
            stemList.insert(i,int(str(data)[:-1]))
        i += 1 
    allStemDataList = parseStemValuesWithZeroLeaf(min(stemList),max(stemList)) 
    return sorted(allStemDataList)

def isNoUnrepeatedValue(dataItem, stemList):
    return int(str(dataItem)[:-1]) not in stemList

def parseStemValuesWithZeroLeaf(minimumStemListValue, maxiumStemListValue):
    '''returns the all stem values between the range of stem values that do not have data values across them
    Input parameters:
    minimumStemListValue - The minium value of the stem list
    maxiumStemListValue  -  The maximum value of the stem list
    '''
    allStemUnits = []
    for allStemUnit in range(minimumStemListValue,maxiumStemListValue + 1,1): #start, end, step - maxiumStemListValue + 1 is done to incldue maxiumStemListValue in list
        indexValue = 0
        allStemUnits.insert(indexValue,allStemUnit) # insert values in list
        indexValue += 1
    return allStemUnits # stem list with zero leaves as well

computeStemLeafMain() # main function call 

