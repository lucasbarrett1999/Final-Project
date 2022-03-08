def displayBoard(incorrectLetters, correctLetters,hiddenWord):
    print("houseDrawingPath"[len(incorrectLetters)])
    print()
    print('Incorrect Letters', end=' ')

    
    for letter in incorrectLetters:
        print(letter, end=' ')
    print()

    blank = '_' * len(hiddenWord)
    # This will load up the guessed letters that are right

    for  i in range(len(hiddenWord)):
        if hiddenWord[i] in correctLetters:
            blank = blank[:i] + hiddenWord + blank[i + 1:]
    #This will show the secret word
    for letter in blank:
        print(letter, end=' ')
    print()