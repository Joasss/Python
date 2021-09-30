import random

while True:
    print("____________________________________")
    print()
    raw_lowestnumber = input(
        "Please enter the lowest number that you want to me to guess a number between: ")
    raw_highestnumber = input(
        "Please enter the highest number that you want to me to guess a number between: ")
    raw_guesses = input("Please enter the amount of guesses you want to do: ")

    lowestnumber = int(raw_lowestnumber)
    highestnumber = int(raw_highestnumber)
    guesses = int(raw_guesses)
    made_guesses = int(0)

    if isinstance(lowestnumber, int) and isinstance(highestnumber, int):
        if lowestnumber > highestnumber:
            print("You entered invalid numbers!")
            break
        total = lowestnumber + highestnumber
        if total < 2:
            print("You entered invalid numbers!")
            break
        if lowestnumber < 1:
            print("You entered invalid numbers!")
            break
        if guesses < 0:
            print("You entered an invalid amount of guesses!")
            break
        print()
        print("I am going to guess a number between " +
              str(lowestnumber) + " and " + str(highestnumber) + "!")
        print()

        lowestnumber -= 1
        highestnumber -= 1
        rndIntRaw = random.randint(lowestnumber, highestnumber)
        rndIntInt = int(rndIntRaw)
        rndInt = rndIntInt - 1

        if guesses > total:
            guesses = total-1

        while made_guesses < guesses:
            made_guesses + 1
            guess_raw = input("Guess the number between " +
                              str(lowestnumber + 1) + " and " + str(highestnumber + 1) + ": ")
            while guess_raw is None:
                guess_raw = input("Guess the number between " +
                                  str(lowestnumber + 1) + " and " + str(highestnumber + 1) + ": ")
            guess = int(guess_raw)
            if isinstance(guess, int):
                if guess == rndInt:
                    print("Correct! The number was: " + str(rndInt) + "!")
                    break
                if guess > rndInt:
                    print("The number is lower!")
                if guess < rndInt:
                    print("The number is higher!")

    else:
        print("You entered invalid numbers!")

    again = input("Do you want to play again? (Y/N) ").lower()
    validagain = ['y', 'yes', 'n', 'no']
    while again not in validagain:
        again = input("Do you want to play again? Respond with (Y/N) ").lower()
    if again == "n" or again == "no":
        break
