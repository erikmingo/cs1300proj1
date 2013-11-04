#!/usr/bin/python

import random

class numbergame:
    def __init__(self, lower, upper):
        self.lowerbound  = lower
        self.upperbound =  upper
#    def number(self, number):
#        self.number = number

class numbergameuser:
    def __init__(self, name):
        self.name = name
    def numguesses(self, numguesses):
        self.totguesses = numguesses

    def number(self, number):
        self.num = number

    def score(self, score):
        self.totscore = score


# game init chooses range
def gameinit():
    lowerbound = int(input("What do you want the lower bound of the range to be (must be bigger than 0) ? Enter here: "))
    upperbound = int(input("What do you want the upper bound of the range to be ? Enter here: "))
    while lowerbound >= upperbound or lowerbound <= 0:
        print("Invalid range try again... ")
        lowerbound = int(input("What do you want the lower bound of the range to be ? Enter here: "))
        upperbound = int(input("What do you want the upper bound of the range to be ? Enter here: "))
#    game = numbergame(lowerbound, upperbound)
    return lowerbound, upperbound

#creates a user object

def userinit():
    name = str(input("What is your username for today? Enter here: "))
    return name

def usernum():
    print("Pick a number between %s - %s" % (game.lowerbound, game.upperbound))
    usernum = int(input("Enter your number here: "))
    while usernum > game.upperbound or usernum < game.lowerbound:
        print("The number you picked is not in the range, please pick a number between %s - %s" % (game.lowerbound, game.upperbound))
        usernum = int(input("Enter your number here: "))
    return usernum

# works, user picks a number relative to the range the user picked, variable is global
def computernumberpick():
    print("The computer will pick a number in the range %s to %s" % (game.lowerbound, game.upperbound))
    compnum = random.randint(game.lowerbound, game.upperbound)
    return compnum


def computerguess(usernum):
# equals 5k first run
    maxguess = game.upperbound
    minguess = game.lowerbound
    compguess = maxguess / 2
    rangeguess = maxguess - minguess
    maxguess = int(maxguess)
    minguess = int(minguess)
    compguess = int(compguess)
    rangeguess = int(rangeguess)
    numguesses = 1
    print("Computer guesses: ", compguess)

    while compguess != usernum:
        if compguess > usernum:
            maxguess = int(compguess)
            compguess = int(maxguess / 2)
            numguesses = int(numguesses + 1)
            print("Computer gueeses: ", compguess)
        elif compguess < usernum:
            minguess = int(compguess)
            compguess = int((maxguess + minguess) / 2)
            numguesses = int(numguesses + 1)
            print("Computer guesses: ", compguess)

    print("The computer guesses your number in: ", numguesses, "guesses")
    return numguesses

def userguess(compnum):
    userguess = int(input("What's your guess? from %s - %s please: " % (game.lowerbound, game.upperbound)))
    numguesses = 1

    if userguess < game.lowerbound or userguess > game.upperbound:
        print("The number you entered is too big or too small, please stay in the range from %s to %s" % (game.lowerbound, game.upperbound))
    while userguess != compnum:
        if userguess > compnum:
            print("Your guess was too big, try again")
            userguess = int(input("Enter your next guess: "))
            numguesses = numguesses + 1
        elif userguess < compnum:
            print("Your guess was too low, try again")
            userguess = int(input("Enter your next guess: "))
            numguesses = numguesses + 1
    print("You guesses the computer's number in", numguesses, "guesses")
    return numguesses

def whowins(userscore, computerscore):
    if userscore < computerscore:
        print("%s wins!" % user.name)
        print("You guessed the computers number in %s trys!" % user.totguesses)
        print("The computer guessed your number in %s trys!" % computer.totguesses)
        user.totscore = user.totscore + 1

    elif userscore > computerscore:
        print("%s wins!" % computer.name)
        print("You guessed the computers number in %s trys!" % user.totguesses)
        print("The computer guessed your number in %s trys!" % computer.totguesses)
        computer.totscore = computer.totscore + 1
    else:
        print("You tied... ")



# Initializes the game, creates the lower and upper bounds

#creates a user! Gives object name + number
name = userinit()
user = numbergameuser(name)


#create a computer object, with a score associated
computer = numbergameuser("Dat Computer")
#computer.numguesses(computerguess(user.number))
#print("okay! your turn to guess the computer's number! to win you must guess it's number in ", computer.numguesses, " guesses")
#computer.number(computernumberpick())
#user.numguesses(userguess(computer.number))

user.score(0)
computer.score(0)


playcounter = 1
while playcounter == 1:
    #pick lower and upper

    lower, upper = gameinit()
    game = numbergame(lower, upper)


    user.number(usernum())

    computer.numguesses(computerguess(user.num))
    print("okay! your turn to guess the computer's number! to win you must guess it's number in ", computer.totguesses, " guesses")
    computer.number(computernumberpick())
    user.numguesses(userguess(computer.num))

    whowins(user.totguesses, computer.totguesses)

    print("The score is")
    print("---------------")

    print("%s -- %s" % (user.name, user.totscore))
    print("%s -- %s" % (computer.name, computer.totscore))

    decider = str(input("Want to play again? (yes/no): "))
    if decider == "yes" or decider == "Yes" or decider == "YES":
        playcounter = 1
    elif decider == "No" or decider == "no" or decider == "NO":
        print("Come playa again soon")
        playcounter = 0

