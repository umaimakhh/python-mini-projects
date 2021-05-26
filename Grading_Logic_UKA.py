'''
Assigment No: 1 - Grading Logic Assigment
Author's Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/SY_c813y6H0 
Date: 04/05/2020
'I have not given or received any unauthorized assistance on this assignment'
   
'''
def computeFinalGrade():
    '''returns total score and grade of the student
    it gives the final score of the students assignment
    The function is further divided into further submodules the returns their scores if any:

     1 - Intial Grading Check Questions Score - initalGradingCheck()
     2 - Code Performance Check Questions Score - codeGradingCheck()
     3 - Late Submission Questions Score - checkForLateSubmission(mTotalComputedMarks)
    '''
    initalGradingCheckMarks = initalGradingCheck()
    codeGradingOverAllMarks = 0.0
    if initalGradingCheckMarks > 0: # if the user has already filled then intial questions response move further to check code perfomance questions
        codeGradingOverAllMarks = codeGradingCheck()
    
    if codeGradingOverAllMarks > 0:
        mTotalComputedMarks = initalGradingCheckMarks + codeGradingOverAllMarks
        checkForLateSubmissionMarks = checkForLateSubmission(mTotalComputedMarks)
        if(checkForLateSubmissionMarks == 0): # if its not late submission then commutes just inital Grading Marks addition to the Code perfomance marks
            mTotalComputedMarks = initalGradingCheckMarks + codeGradingOverAllMarks
        else:
            mTotalComputedMarks = checkForLateSubmissionMarks

        mTotalGrade = str(int(mTotalComputedMarks)) + '/70' + ' Grade - ' + gradingLogic(int(mTotalComputedMarks))
        print('\033[1;32;40m The final score of the student is ' + mTotalGrade) # Total marks statement in color green(32 color code) format 1 =style type,
    else:
        print('\033[1;31;40m Failed to update score, please retry with correct values')

def initalGradingCheck():
    '''returns the score of the inital questions by asking the user for 
    which each each questions answer in either true or false -
    adding each answers to a list
    '''

    input('-- Assignment Grading Software - Enter Y or yes for a true response AND N or no for a false response --')

    initalGradingCheckQuestionsIndex = 0 
    eachSubModuleScore = 10
    mIntialGradingCheckList = [] #intailzation of list to store all the true answers of the questions. (to many if else statments would have been expensive)
   
    mFileFormat = booleanHelper((input('Is the assignment submitted as a single uncompressed .py file?' +' ' ))) # question one response
    mIntialGradingCheckList.insert(initalGradingCheckQuestionsIndex,mFileFormat) #inserting boolean response to list

    mStudentNameAndDateVerification = booleanHelper((input(
    '\nDoes the assignment contain author\'s name and date?' +' ' ))) # question two response
    mIntialGradingCheckList.insert(initalGradingCheckQuestionsIndex + 1 ,mStudentNameAndDateVerification)

    IsHonorStatement = booleanHelper((input(
    '\nDoes the assignment contain this statement on the top of the code'
    + ' ' + '"I have not given or received any unauthorized assistance on this assignment"?' 
    + ' '))) # question three response
    mIntialGradingCheckList.insert(initalGradingCheckQuestionsIndex + 1,IsHonorStatement)

    IsYoutubeLink = youtubeLinkCheckSteps() # question four response
    mIntialGradingCheckList.insert(initalGradingCheckQuestionsIndex + 1,IsYoutubeLink)

    studentIntialMarks = 0 # inital students marks

    for trueValues in mIntialGradingCheckList: 
        if trueValues == True:
            studentIntialMarks =  studentIntialMarks + eachSubModuleScore  #adding submodule score for each true answer
    if studentIntialMarks > 0:
        return studentIntialMarks

    return 0

def codeGradingCheck():
    '''returns the total Code perfomance score based on the questions 
    user inputs the float values for each question

    '''
    input('\n\n-- On a scale from 0 - 10, Answer the following questions to evaluate further -- Press Enter to countinue')
    correctnessOfCodeMarks = float(input('\nWhat points would be give for the correctness of the code?'
                             +' '))
    eleganceOfCodeMarks = float(input('\nWhat points would be give for the elegance of the code?'
                             +' '))
    qualityDiscussionOfCodeMarks = float(input('\nWhat points would be give for the '
                                 +'quality of the discussion in the YouTube video?'+' ' ))

    if rangeCheckOfCodePerfomanceMarks(
        correctnessOfCodeMarks,
        eleganceOfCodeMarks,qualityDiscussionOfCodeMarks) == True:
        totalCodeGradingMarks = correctnessOfCodeMarks + eleganceOfCodeMarks + qualityDiscussionOfCodeMarks
        return totalCodeGradingMarks # returns sum of answers of all the questions
    else:
        print('\033[1;31;40m\nThe entereted marks for each answer should be between the range of 0 and 10') # color code for red = 31
    return 0


def rangeCheckOfCodePerfomanceMarks(
    correctnessOfCodeMarks,
    eleganceOfCodeMarks,
    qualityDiscussionOfCodeMarks):
    ''' returns true if all the three parameters are less than 10 and greater than 0 '''
    if 0 <= correctnessOfCodeMarks and eleganceOfCodeMarks and qualityDiscussionOfCodeMarks <= 10: return True
    return False


def booleanHelper(userInputValue):
    '''returns boolean response by to parsing the users response to some questions
    '''
    if userInputValue.lower() ==  'y' or userInputValue == 'yes': # answer True
        return True
    elif userInputValue.lower() ==  'n' or userInputValue == 'no': # answer False
        print('\033[1;31;40m Student has been awarded grade 0')
        exit() 
    else:
        print('\nIncorrect input found, To proceed please try again by entering Y or N only') # In case the user enters invalid response 
        exit() # exit from the code if incorrect value
        return None

def youtubeLinkCheckSteps():
    '''returns boolean value on the bases of 3 subchecks:
    1 - YouTube Link Given?
    2 - Is video unlisted?
    3 - Is Duration 3 mintues?
    '''
    youtubeLinkDurationCheck = False
    youTubeUnlistedVideo = False
    isYouTubeLinkAviablable = booleanHelper((input('\nIs the video youtube link added?'))) # question four- submodule response
    if isYouTubeLinkAviablable:
        youTubeLinkDurationCheck = booleanHelper((input('\nIs the provided YouTube video of 3-minutes?' + ' '))) # question four- submodule response
    
    if youTubeLinkDurationCheck:
        youTubeUnlistedVideo = booleanHelper((input('\nIs the provided YouTube video unlisted'
        +'- an unlisted video will not appear in any of YouTube\'s public spaces?'
        +' '))) # question four - submodule response
    
    if youTubeUnlistedVideo:
        return True

    return False
    
def checkForLateSubmission(totalmarks):
    '''returns integer value of deducted marks (if any) for late assignment
    Input type: totalmarks(The total computed marks)
    The decuted marks are computed of the parameter of total marks:
    totalmarks - totalmarks * (lateSubmissionHourCount * 0.01)
    '''
    isAssignmentSubmittedLate = (input('\nHas the student submitted the assignment late? (Y/N) '
                                 +' ')) # boolean response for late submission
    if isAssignmentSubmittedLate is 'Y':
        lateSubmissionHourCount = int(input('\nHow many hours was the assignment late? '
                                 +' ')) # no of hours of late assignment
        mDeductedMarks = int(totalmarks - totalmarks * (lateSubmissionHourCount*0.01)) # deduction of 1% from the total marks for each hour
        return mDeductedMarks
    else:
        return 0 # returns 0 if not late submission


def gradingLogic(totalscore):
    '''returns the grade of the student depending of the range of the score
    
    Input parameter: Score in number
    '''
    if 60 < totalscore <= 70:
        return 'A'
    elif 50 <  totalscore <= 59:
        return 'B'
    elif 30 < totalscore <= 49:
        return 'C'
    elif totalscore <= 29:
        return 'D'
    return '-'

computeFinalGrade()