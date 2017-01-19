import random
def main():
    words = []
    # reading words.txt
    try:
        file = open("word.txt", "rt")
        for lines in file:
            lines = lines.replace("\n", "")
            words.append(lines)
    except IOError:# handling reading error checking if the files is found
        print("There is no such a  file name found")

    secretWord = random.choice(words)#choosing a word from the file
    secretWord = list(secretWord)# converting the chosen word a list
    guessWord = ['', '', '', '', '', '']
    errors = 0
    hangPic = hangermanGraf(errors)#Calling the graphic function
    winPic = WinGUI()# calling the winning gui

    try:

        while errors < 6 and secretWord != guessWord:
            print ("The guess word is:", guessWord)
            print( errors, " errors")
            guess = input("Guess a character: ")#Getting user inputs
            for letters in secretWord:
                if guess == letters:
                    index = 0
                    while index < len (secretWord):
                    # changing the user guess if correct to it appropriate index
                        if secretWord[index] == guess:
                            guessWord[index] = secretWord[index]
                        index += 1
            #Adding 1 to the error when the user guess wrong
            if secretWord.count(guess) == 0:
                errors += 1
                hangPic = hangermanGraf(errors)

    except ValueError:#Invalid input error handling
        print("That was not a valid input, Please try again with string")
    except Exception:#all exception handling
        print("There is something wrong with the code")

    if secretWord == guessWord:
        print("The guess word is", ''.join(guessWord))
        print("This is the correct word.")
        winPic = WinGUI()


        pass
    elif errors ==6:
        print("You have" , errors , "errors")
        print("you did not make it, the correct word is ", ''.join(secretWord))

#Game over GUI
def hangermanGraf(errors):
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

#Winning GUI
def WinGUI():
    print ("              ")
    print ("________      ")
    print ("|             ")
    print ("|             ")
    print ("| \ 0 /       ")
    print ("|  \|/        ")
    print ("|   |         ")
    print ("|  / \        ")
    print (" Your sentence of death has been forgiven by the KING")
    print (" You are a free man now, Enjoy your life")
    print (" You have won")

main()
