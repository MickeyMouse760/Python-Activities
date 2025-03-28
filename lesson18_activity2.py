import random
contin = True
while contin==True:
    user = input("Which do you want, rock, paper, or scissors?")
    choices = ["rock", "paper", "scissors"]
    comp = random.choice(choices)
    if user==comp:
        print("It's a tie!")
    else:
        if user == "rock":
            if comp=="scissors":
                print("You win!")
            else:
                print("You lose!")
                if user == "scissors":
                    if comp == "rock":
                        print("You lose!")
                    else:
                        print("You win!")
                        if user == "paper":
                            if comp == "rock":
                                print("You win!")
                            else:
                                print("You lose!")
    ans = input("Do you want to play again?(y or n)")
    if ans != "y":
        break
        