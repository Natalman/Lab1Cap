import random

guessNum = 0

number = random.randint(1,20)

while guessNum < 6:
    print('take a guess')
    userGuess = input()
    userGuess = int(userGuess)

    guessNum = guessNum + 1

    if userGuess < number:
        print('Your guess is too low')

    if userGuess > number:
        print ('your guess is too high')

    if userGuess == number:
        break

if userGuess == number:
    guessNum = str(guessNum)
    print ('You have guessed my number that is: ' + number + ' in ' +  userGuess + ' guesses ')

if userGuess != number:
    guessNum = str(guessNum)
    print ('You have reached the guessing allowed: ' + guessNum + ' times')
