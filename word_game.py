import os
import random

words = ["PATHWAY", "WAY", "RECOGNIZE" ,"REVIEW", "SAILBOAT", "WHEEL"]

word = random.choice(words)

correct_letters = ""
total_letters = ""
guesses = 0

while True:
    os.system("cls")
    #Header
    print('')
    print("Welcome to the word guessing game! ")
    print('')
    print("What is your guess? Please, choose a letter \U0001F914")
    print('')

    result = ""
    for letter in word:
        if letter in correct_letters:
            result += letter
        else:
            result += "_"
    print("                  {}".format(result))
    print('')
    print('')

    if result == word:
        print('')
        print("Congratulations! You guessed it! \U0001F44F ")
        print(f'It took you {guesses} guesses.') #Total of guesses tried
        print('')
        break

        #User choosing letters
    while True:
        letter_user_without_format = input("Give me a letter: ")
        letter_user = letter_user_without_format.upper()
        if len(letter_user) < 1 or len(letter_user) > 1 :
            print("Please choose a letter")
        elif letter_user in total_letters:
            print('You choose this letter before. Do you remember? ')
        elif not letter_user.isalpha():
            print("Please choose a letter")
        else:
            total_letters += letter_user
            break
    
    #Letters putting for the user

    if letter_user not in word:
        guesses +=1
    else:
        correct_letters += letter_user
