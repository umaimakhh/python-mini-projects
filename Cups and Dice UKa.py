'''
Assigment No:0502 - Cups and Dice
Name: Umaima Khurshid Ahmad
Youtube Link: https://youtu.be/IyyCK_opYBI 
Date: 05/2/2020
I have not given or received any unauthorized assistance on this assignment
'''
from Assignment0501_UmaimaKh import Cup # file Assignment0501_UmaimaKh should be in the same folder of assignment0502_UmaimaKh
import random

# CUPS AND DICE GAME

class BetAndLuckException(Exception): # custom exception class to handle all errors
    """Raised when any exception occurs"""
    pass    

class ValueIncorrect(BetAndLuckException):
   """Raised when the input value is incorrect"""
   pass

class BalanceExceededFromBet(BetAndLuckException): # used in functions getUserSelectedBetAmount and enterDiceCountAndValidNumber
   """Raised when the the bet amount exceeds current balance"""
   pass
  
class betAndLuckGame(BetAndLuckException): # extends exception class - used in functions getUserSelectedBetAmount
    '''represents a Bet and Luck Game object'''
    
    
    def __init__(self,intialUserGiftBalance,userName,minimunRandomLimit,maximunRandomLimit):
        self.intialUserGiftBalance = intialUserGiftBalance
        self.userName = userName
        self.minimunRandomLimit = minimunRandomLimit
        self.maximunRandomLimit = maximunRandomLimit

        print('\nCongransulations '+userName+'!'+' - You have recieved a balance of $'+str(self.intialUserGiftBalance)+'\n')

    def startGame(self,firstTimeUser,userWalletBalance):
        '''returns user balance deducted from the user bet amount and calls genrates random number'''
        global goalNumber
        goalNumber = self.genrateRandomNumberForGoal() # genrates random number 
        userBetAmount = self.getUserSelectedBetAmount(userWalletBalance,firstTimeUser) # gets user amount that he wishes to bet 
        if firstTimeUser:
            userWalletBalance = self.intialUserGiftBalance - userBetAmount # intialUserGitBalance is 100 for the first time
        else:
            userWalletBalance =  userWalletBalance - userBetAmount    # userWallentBalance is the balance he has when he comes after the first time
        print('\nYour current wallet has $',str(userWalletBalance)) #display balance 
        userWalletBalance = self.getUserInputAndInitalizeCup(userWalletBalance)
        return userWalletBalance

    def getUserInputAndInitalizeCup(self,userWalletBalance):
        ''' gets user Input for all the three dices and initaluze Cups'''
        self.sixSidedDiceCount =  self.enterDiceCountAndValidNumber('Six Sided Die')
        self.tenSidedDiceCount = self.enterDiceCountAndValidNumber('Ten Sided Die')
        self.twentySidedDiceCount =  self.enterDiceCountAndValidNumber('Twenty Sided Die')
        if self.sixSidedDiceCount != -1 and self.tenSidedDiceCount != -1 and self.twentySidedDiceCount != -1: # if values validated proceed further
            return  self.intializeCupAndComputeBet(self.sixSidedDiceCount,self.tenSidedDiceCount,self.twentySidedDiceCount,self.userName,userWalletBalance) #returns user wallet balance
        else:
            raise BetAndLuckException('Incorrect Input')

    def enterDiceCountAndValidNumber(self,diceType):
        '''returns true if entered number is integer and validates if entered value correct'''
        while True:
            try: 
                numberCount =  ((input('\nHow many times would like to roll for '+diceType+' ')))
                if not numberCount.isdigit():
                    raise ValueIncorrect           
            except ValueIncorrect:
                print('\nPlease enter integer value values to contiune')               
            else:
                return int(numberCount)

    def intializeCupAndComputeBet(self,sixSidedDiceCount,tenSidedDiceCount,twentySidedDiceCount,userName,userWalletBalance):
        '''returns current user balance of the base of rolled number'''
        global goalNumber
   
        cup = Cup(sixSidedDiceCount,tenSidedDiceCount,twentySidedDiceCount) # creation of cup with user filled values 
        rolledNumber = cup.roll() # rolled number 

        print('\n ----- The rolled number is '+str(rolledNumber)+'------------')
        if(goalNumber == rolledNumber):
            userWalletBalance = userWalletBalance + (userWalletBalance * 10)
            print(self.userName+'! Wow ! You are lucky enough to win the bet, you get 10 times the amount in your current wallet, now you have earned $' +str(userWalletBalance))
        elif  rolledNumber - 5 <= goalNumber < rolledNumber:
            userWalletBalance = userWalletBalance + (userWalletBalance * 5)
            print(self.userName+'! the rolled number was with 5 of the goal, you get 5 times the amount in your current wallet now you have earned $' +str(userWalletBalance))

        elif rolledNumber - 10 <= goalNumber < rolledNumber:
            userWalletBalance = userWalletBalance + (userWalletBalance * 2)   
            print(self.userName+'! the rolled number was with 10 of the goal, you get 2 times the amount in your current wallet now you have earned $' +str(userWalletBalance))  
        else:
            print('\n'+self.userName+' Sorry, you didnt earn anything - Game Over - your current balance is  $' +str(userWalletBalance)) # game over message        
        return userWalletBalance

    def genrateRandomNumberForGoal(self):
        '''returns a genrated random number'''
        goalNumber = random.randint(self.minimunRandomLimit, self.maximunRandomLimit) # genrating random number from max and min limit 
        print('\n Your goal for this round is '+str(goalNumber) +' - The goal - '+str(goalNumber)) # displaying random number
        return goalNumber
     
    def getUserSelectedBetAmount(self,userWalletBalance,firstTimeUser):
        '''returns bet value entered by the user'''
        while True:
            try: 
                numberCount =  (input('\nHow much do you want to bet om this turn? '))
                if not numberCount.isdigit():
                    raise ValueIncorrect                    
                if (not firstTimeUser and (int(numberCount) > userWalletBalance)) or (firstTimeUser and (int(numberCount) > 100)):
                    raise BalanceExceededFromBet             
            except BalanceExceededFromBet:
                print('Your balance is too low for this bet')
            except ValueIncorrect:
                print('Enter postive Integer value to contiune')
            else:
                return int(numberCount)

class UserLoginState:
    '''represent user log in and logout states'''

    def exitGame(self):
        '''exits the game''' 
        print('It was great playing with you, Please come again!') 
        exit() # game exit

    def greetAndGetUserName(self):
        '''returns user name and display greetings'''
        return (input('\nEnter your name to start the game: ')) # user name enter

    def getUserGameResponse(self):
        ''' returns True if user wants to contiune game''' 
        userWishToContiune =  (input(' Press Y if you wish to contiune and Q to exit '))
        if userWishToContiune == 'Y': # in case user pressed Y to contiune game
            return True
        else:
            return False

def main():
        
        print('\n------------------- Welcome to Bet and Luck Game -------------------\n') # game name
        
        currentUserWallet = 0 # user user wallet
        intialUserGiftBalance = 100 # user intial gift balanace - change from here to change it in whole code
        maxRandomLimit = 100 # max range for genrating random number - - change from here to change it in whole code
        minumRandomLimit = 1 # min range for genrating random number
        contiuneGame = True # maintaining state for user if continue game 
        firstTimeUser = True

        mUserLogState = UserLoginState()
        userName = mUserLogState.greetAndGetUserName() # getting user name from User state class
        mbetAndLuckGame = betAndLuckGame(intialUserGiftBalance,userName,minumRandomLimit,maxRandomLimit)
        contiuneGame = mUserLogState.getUserGameResponse() # check if user wants to contiune game 
       
        while contiuneGame: # primary loop 
            currentUserWallet = mbetAndLuckGame.startGame(firstTimeUser,currentUserWallet) # game started
            firstTimeUser = False # first time user set to False as now commutation will be not done on intialUserGiftBalance
            contiuneGame = mUserLogState.getUserGameResponse()   # check if user wants to contiune game       
        
        mUserLogState.exitGame() # if user doesnt want to contiune exit the game



main()