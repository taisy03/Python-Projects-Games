import random

def guess(x):
    random_number = random.randint(1,x)
    
    while guess != random_number :
        mg = input(f"Guess a number between 1 and {x}: ")
        myguess = int(mg)
        if myguess < 1 or myguess > x:
            print("You guessed outside the range! Try again.")

        elif myguess < random_number:
            print("You guessed too low! Try again.")
        
        elif myguess > random_number:
            print("You gueesed too high! Try again. ")

        else:
            print("Yay! You guessed correctly")
            break

guess(int(input("choose a range between 1 and x , where x= ")))
#we can put any number into line 20 to choose the range
#guess(12)