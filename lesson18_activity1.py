import random
num = str(random.randint(0, 9))
correct = True
while correct==True:
    print("You have to guess the number from 0 to 9\n")
    guess=input("Give your best guess: \n")
    if guess == num:
        print("Correct! Good Job")
        correct = False
        break
    else:
        print("Incorrect! Try Again\n")