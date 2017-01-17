secretWord = ['m', 'a', 's', 't', 'e', 'r']
guessWord = ['', '', '', '', '', '']
errors = 0

while errors < 7 and secretWord != guessWord:
    print ("The guess word is:", guessWord)
    print( errors, " errors")
    guess = input("Guess a character: ")

    if errors== 0:
    	print ("________      ")
    	print ("|      |      ")
    	print ("|             ")
    	print ("|             ")
    	print ("|             ")
    	print ("|             ")
    elif errors == 1:
    	print ("________      ")
    	print ("|      |      ")
    	print ("|      0      ")
    	print ("|             ")
    	print ("|             ")
    	print ("|             ")
    elif errors == 2:
    	print ("________      ")
    	print ("|      |      ")
    	print ("|      0      ")
    	print ("|     /       ")
    	print ("|             ")
    	print ("|             ")
    elif errors == 3:
    	print ("________      ")
    	print ("|      |      ")
    	print ("|      0      ")
    	print ("|     /|      ")
    	print ("|             ")
    	print ("|             ")
    elif errors == 4:
    	print ("________      ")
    	print ("|      |      ")
    	print ("|      0      ")
    	print ("|     /|\     ")
    	print ("|             ")
    	print ("|             ")
    elif errors == 5:
    	print ("________      ")
    	print ("|      |      ")
    	print ("|      0      ")
    	print ("|     /|\     ")
    	print ("|     /       ")
    	print ("|             ")
    else:
    	print ("________      ")
    	print ("|      |      ")
    	print ("|      0      ")
    	print ("|     /|\     ")
    	print ("|     / \     ")
    	print ("|             ")
    	print ("GAME OVER!")


    for letters in secretWord:
        if guess == letters:
            index = 0
            while index < len (secretWord):
                if secretWord[index] == guess:
                    guessWord[index] = secretWord[index]
                index += 1

    if secretWord.count(guess) == 0:
        errors += 1

if secretWord == guessWord:
    print("The guess word is", guessWord)
    print("This is the correct word.")

elif errors ==7:
    print("You have" , errors , "errors")
    print("you did not make it, the correct word is ", secretWord)
