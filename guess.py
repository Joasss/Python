########################################
# Naam: Joas Bruil
# Doel: nummer randen van de computer
# Klas: h4e
# Docent: JBU
# Project: Number Guessing Game
# Modules: random
########################################

import random

# Om te kunnen restarten nadat de game is afgelopen.
while True:
    print("____________________________________");
    print();

    # Krijg de input van de user en verander het naar integers
    rawLowestNumber = input("Please enter the lowest number that you want to me to guess a number between: ");
    rawHighestNumber = input("Please enter the highest number that you want to me to guess a number between: ");
    rawGuesses = input("Please enter the amount of guesses you want to do: ");

    lowestNumber = int(rawLowestNumber);
    highestNumber = int(rawHighestNumber);
    guesses = int(rawGuesses);
    madeGuesses = int(0);


    # Check of het geldige getallen zijn
    if isinstance(lowestNumber, int) and isinstance(highestNumber, int):

        # Failsaves (crashes voorkomen en eisen)
        if lowestNumber > highestNumber:
            print("The lowest number cannot be higher than the highest number.");
            break;
        total = lowestNumber + highestNumber;

        if total < 2:
            print("Your numbers need to be higher in order to play.");
            break;

        if lowestNumber < 1:
            print("The lowest number cannot be below 1.");
            break;

        if guesses < 0:
            print("The amount of guesses cannot be below 0.");
            break;

        if guesses > 8:
            print("The amount of guesses cannot be higher than 8.");
            break;

        # Start het spel (berichten en random getallen genereren)
        print();
        print("I am going to guess a number between " + str(lowestNumber) + " and " + str(highestNumber) + "!");
        print();

        lowestNumber -= 1;
        highestNumber -= 1;

        rndIntRaw = random.randint(lowestNumber, highestNumber);
        rndIntInt = int(rndIntRaw);
        rndInt = rndIntInt;


        if guesses > total: guesses = total-1;

        # Zolang het nummer niet geraden is, laat de gebruiker raden.
        while madeGuesses < guesses:
            madeGuesses + 1;
            guessRaw = input("Guess the number between " + str(lowestNumber + 1) + " and " + str(highestNumber + 1) + ": ");

            while guessRaw is None:
                guessRaw = input("Guess the number between " + str(lowestNumber + 1) + " and " + str(highestNumber + 1) + ": ");

            guess = int(guessRaw);

            # Handle the input van de user
            if isinstance(guess, int):
                if guess == rndInt:
                    print("Correct! The number was: " + str(rndInt) + "! You guessed it in " + str(madeGuesses) + "guesses.");
                    break;

                if guess > rndInt:
                    print("The number is lower! You have made " + str(madeGuesses) + "guesses.");

                if guess < rndInt:
                    print("The number is higher! You have made " + str(madeGuesses) + "guesses.");

    else:
        print("You entered invalid numbers!");

    # Laat het spel weer opnieuw beginnen
    again = input("Do you want to play again? (Y/N) ").lower();

    validAgain = ['y', 'yes', 'n', 'no'];

    while again not in validAgain:
        again = input("Do you want to play again? Respond with (Y/N) ").lower();

    if again == "n" or again == "no":
        break;
