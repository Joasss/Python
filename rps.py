import random

user_wins = 0
comp_wins = 0

choices = ['rock', 'paper', 'scissors']

while True:
    rndInt = random.randint(0,2)
    choise_computer = choices[rndInt]

    choice_user = input("Rock, Paper or Scissors? ").lower()

    while choice_user not in choices:
        choice_user = input("Please enter Rock, Paper or Scissors: ").lower()
    
    print()
    print("Your choice: " + choice_user)
    print("My choice: " + choise_computer)
    print()
    if choise_computer == "rock":
        if choice_user == "rock":
            print("It's a tie!")
        elif choice_user == "paper":
            print("You won!")
            user_wins +=1
        elif choice_user == "scissors":
            print("You lost!")
            comp_wins +=1
    if choise_computer == "paper":
        if choice_user == "rock":
            print("You lost!")
            comp_wins +=1
        elif choice_user == "paper":
            print("It's a tie!")
        elif choice_user == "scissors":
            print("You won!")
            user_wins +=1
    if choise_computer == "scissors":
        if choice_user == "rock":
            print("You won!")
            user_wins +=1
        elif choice_user == "paper":
            print("You lost!")
            comp_wins +=1
        elif choice_user == "scissors":
            print("It's a tie!")
    print()
    print("Your Score: " + str(user_wins))
    print("My Score: " + str(comp_wins))
    print()
    
    again = input("Do you want to play again? (Y/N) ").lower()
    validagain = ['y', 'yes', 'n', 'no']
    while again not in validagain:
        again = input("Do you want to play again? Respond with (Y/N) ").lower()
    if again == "n" or again == "no":
        break