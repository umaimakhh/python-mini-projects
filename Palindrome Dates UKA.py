'''
Assigment No:0601 - Palindorime Dates
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/0d0Jz-bMtpM
Date: 05/12/2020
I have not given or received any unauthorized assistance on this assignment
'''


def checkPalindorime():
    '''main funcation that stores stores all the palindrome dates in text file'''
    global filePath
    fileName = 'palindromeFile.txt'
    filePath = 'E:\DPU\Spring 2020 courses\Python Programming\week 6\\' + fileName # file path 
    genratePalindromeTextFile() # generate text file for the first time
    date = '01/01/2001' #first date of 21st Centuary
    while date[-4:] != '2101': # dates till year 2100
        isPalindrosme = isPalindorime(date)
        if isPalindrosme:
            storeDateInFile(date) # store that in file 
            date = getStartOfNextMonthDate(date) # no need to check all dates for that month cause one no palindrome date if once occurs in a month
        else:
            date = incrementNextDay(date) # check next day
    print('\n\nPalindrome Dates stored successfully in '+filePath+'\n\n')

def genratePalindromeTextFile():
    ''''creates file in path to store all palindrome dates'''
    global filePath
    try:
        palindromeFileText = open(filePath, 'x') # x for file creation
    except FileExistsError: # excepion handled when file already created, mostly this would occur while testing the same code.
        pass
    else:
        palindromeFileText = open(filePath, 'a') # x for file creation
        title = '21st century Palindrome Dates using the DD/MM/YYYY format\n'
        palindromeFileText.write(title+'\n') # next time start with new line
        palindromeFileText.close() # close file if created

def storeDateInFile(palindromedate):
    global filePath
    outfile = open(filePath, 'a') # a for append on file
    outfile.write(palindromedate+'\n') # next time start with new line
    outfile.close()

def isPalindorime(date):
    '''returns true if date is Palindorime using slicing''' 
    if (date[0] == date[-1]) and (date[1] == date[-2]) and (date[3] == date[-3]) and (date[4] == date[-4]):
        return True

def incrementDate(currentDate):
    '''returns next day DD
    input parameter:
    currentDate : current Date in format DD'''
    date = int(currentDate)
    date += 1
    return '{0:02d}'.format(date)

def incrementNextDay(date):
    '''returns next day of current input date
    Input paramenter:
    date : data in format DD/MM/YYYY'''
    # using slicing technique
    currentDate = getParseDateFromDateFormat(date) # next date
    newDate = incrementDate(currentDate) # increment to next date 
    if newDate == '32': # invalid date in month
        return getStartOfNextMonthDate(date)
    else:
        date = date[1:]
        date = replaceString(date,newDate,0) # replace current date with next date
    return date


def getParseDateFromDateFormat(date):
    '''returns date format DD from DD/MM/YYYY
    Input parameter:
    date : data in format DD/MM/YYYY'''
    date = (date[0:2])
    if len(date) < 2:
        date ='{0:02d}'.format(date)
    return (date)

def getParseMonthFromDateFormat(date):
    '''returns date format DD from DD/MM/YYYY
    Input parameter:
    date : data in format DD/MM/YYYY'''
    date = (date[3:5])
    if len(date) < 2:
        date ='{0:02d}'.format(date)
    return (date)


def getParseYearFromDateFormat(date):
    '''returns date format DD from DD/MM/YYYY
    Input parameter:
    date : data in format DD/MM/YYYY'''
    return int(date[-4:])

def getStartOfNextMonthDate(date):
    '''returns start of next month date format DD from DD/MM/YYYY
    Input parameter:
    date : data in format DD/MM/YYYY'''
    currentMonth = int(getParseMonthFromDateFormat(date))
    currentMonth += 1
    if len(str(currentMonth)) < 2:
        (currentMonth) ='{0:02d}'.format((currentMonth))
    if currentMonth != 13:
        datefirst = '01'
        month = str(currentMonth)
        year = date[-4:]
        date = '{}/{}/{}'.format(datefirst,month,year)
    else: # invalid month so the next year has started 
        date = getFirstDateOfNextYearDate(date)
    return date
        
def getFirstDateOfNextYearDate(date):
    '''returns start of next year date format DD from DD/MM/YYYY
    Input parameter:
    date : data in format DD/MM/YYYY'''
    currentYear = getParseYearFromDateFormat(date) # get current year from date
    currentYear += 1
    datefirst = '01'  # first day of year
    month = '01' # first day of year
    year = str(currentYear)
    date = '{}/{}/{}'.format(datefirst,month,year)
    return date   

def replaceString(s, newstring, index):
    '''insert the new string between "slices" of the original'''
    return s[:index] + newstring + s[index + 1:]  

checkPalindorime()

