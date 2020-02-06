"""
Program: problem7.py
Author: Vivek Kiran
Assignment #: Lab Exercise 8
Last Modified Date: 02/06/2020
Program Description:
Game of guess the correct number game
"""
import random

secretNumber = random.randint(1,10)

maximumTries = 10
attemptCounter = 0
triesLeftCounter = 10

print("~~~Welcome to the Game of guess the correct number~~~")
print("Rules of the Game")
print('The computer has generated a secret number between 1 and 10!')
print('You are allowed a maximum of 10 attempts.\n')
print("Generated Number", secretNumber) #Not To be displayed in final code, just for trial"

userGuessNumber = int(input('Guess a secret number generated between 1 and 10? '))

while attemptCounter < maximumTries:
    if userGuessNumber == secretNumber:
        print("You guessed it right! Congratulations!")
        break
    elif userGuessNumber < secretNumber:
        triesLeftCounter -= 1
        attemptCounter += 1
        print("You guessed it wrong, your guess is too less!")
        print('Incorrect Attempts: ', attemptCounter)
        print('Number of Tries Left: ', triesLeftCounter)
        userGuessNumber = int(input('Guess a secret number generated between 1 and 10? '))

    elif userGuessNumber > secretNumber:
        triesLeftCounter -= 1
        attemptCounter += 1
        print("You guessed it wrong, your guess is too high!")
        print('Incorrect Attempts: ', attemptCounter)
        print('Number of Tries Left: ', triesLeftCounter)
        userGuessNumber = int(input('Guess a secret number generated between 1 and 10? '))
    else:
        triesLeftCounter -= 1
        attemptCounter += 1
        print("Invalid Input")
        print('Incorrect Attempts: ', attemptCounter)
        print('Number of Tries Left: ', triesLeftCounter)
        userGuessNumber = int(input('Guess a secret number generated between 1 and 10? '))



