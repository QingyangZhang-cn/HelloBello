#! /usr/bin/env python3
# coding:utf-8
import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secertNum):
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi') #You got a right num on rigt position
        elif guess[i] in secretNum:
            clues.append('Pico')  #You got a right num but wrong position
    if len(clues) == 0:
        return 'Bagels'
    clues.sort()
    return ' '.join(clues)

def isOnlyDigits(num):
    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False 
    return True


if __name__ == '__main__':
    print('I am thinking of %s-digit number. Try to guess it.' %(NUM_DIGITS))
    print('The clues I give are...')
    print('Bagels, none of the digits is correct.')
    print('Pico, you got a correct number in the wrong position.')
    print('Fermi, you got a correct number in the correct position.')
    while True:
        secretNum = getSecretNum()
        print('I have thought up a number. You have %s chances to use.' %(MAX_GUESS))
        guessesTaken = 1
        while guessesTaken <= MAX_GUESS:
            guess = ''
            while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
                print('Guess #%s: ' %(guessesTaken))
                guess = input()
            print(getClues(guess, secretNum))
            guessesTaken += 1
            if guess == secretNum:
               break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' %(secretNum))
        print('Do you want to play again?(Y or N)')
        if not input().lower().startswith('y'):
            break
