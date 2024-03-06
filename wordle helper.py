# pandas is used for working with data sets and shortcutting it to "pd"
import pandas as pd
import random as rd

#Importing data from csv using pandas and assigning it to valid_guess (no output will be displayed)
valid_guesses_csv = pd.read_csv('valid_guesses.csv')
valid_solutions_csv = pd.read_csv('valid_solutions.csv')

#converting both to list nad making a new list with all words 
#ALL LISTS
vg = valid_guesses_csv['word'].tolist()
vs = valid_solutions_csv['word'].tolist()
vt = vg + vs





#you cant iterate over a list so have to use a tuple and so we create a temporare tuple names temp_tuple

def function(guess):
    temp_tuple = tuple(vs)
    for word in temp_tuple:
        for i in range(5):
            if feedback[i] == "w" and guess[i] in word:
                if guess[i] not in right_letters and guess[i] not in misplaced_letters:
                    vs.remove(word)
                    break
                ## else says that if there is a second letter in the word then it will remove it
                # THIS DOESNT WORK
                elif guess[i] in right_letters or guess[i] in misplaced_letters:
                    for j in range(5):
                        if guess[i] == word[j] and i != j :
                            print(word)
                            print(j)
                            vs.remove(word)
                            break
            elif feedback[i] == "r" and guess[i] != word[i]:
                vs.remove(word)
                break
            elif feedback[i] == "m" and guess[i] not in word:
                vs.remove(word)
                break
            elif feedback[i] == "m" and guess[i] == word[i]:
                vs.remove(word)
                break
        
    print(vs)
    print(f"ammount of options left:{len(vs)}")



for turn in range(6):
    guess1 = input(f"Guess {turn+1} : ").lower()
    feedback = ""
    wrong_letters = []
    right_letters = []
    misplaced_letters = []

    for i , letter  in enumerate(guess1):
        print(f"letter: {letter}")
        x = input("Is this letter right , misplaced or wrong (r,m,w): ")
        feedback = feedback + x
        if x == "w":
            wrong_letters.append(letter)
        elif x == "r":
            right_letters.append(letter)
        elif x == "m":
            misplaced_letters.append(letter)
        else:
            print("SOMETHING IS WRONG WITH YOUR CODE")
    

    print(f"Feedback: {feedback}")
    print(f"Wrong letter: {wrong_letters}")
    print(f"Right letters: {right_letters}")
    print(f"misplaced letters: {misplaced_letters}")
    function(guess1)


