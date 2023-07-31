import random

rand = random

guess = 0
rounds = 3

while rounds > 0:
    # random number
    randNum = rand.randrange(0,11)
    #text
    print("Guess the number from 1 to 10")
    #input 
    text = input(">> ")
    print("")

    #check if input is number
    if text.isnumeric():
        #adding guess
        guess += int(text)

        #check if the value if the same as random
        if guess == randNum:
            print(f"YOU WON ! THE CORRECT NUMBER IS: {randNum}")
            print("")
            quit()
        #if not the same
        else:
            print(f"Your value isnt correct. Correct number was: {randNum}")
            print("")
            rounds -= 1
    else:
        print("Value is not number. Please try again")
        print("")
        rounds -= 1
else:
    print(f"GAME OVER !!! YOU USED YOUR 3 GUESSES")