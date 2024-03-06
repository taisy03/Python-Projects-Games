
import random 

def play():
    computer_score = 0
    player_score = 0
    play_again = "y"
    while  play_again != "n" :
        player = input("Choose rock (R), paper (P) or Scissors (S): ").lower()
        if player != 'r' and player != 's' and player != 'p' :
            print("That\'s not a choice!")
            player = input("Choose rock (R), paper (P) or Scissors (S): ").lower()
        comp= random.choice(['r','p','s'])
        if comp == 'r':
            comp_c = "rock"
        elif comp == 's':
            comp_c = "scissors"
        elif comp == 'p':
            comp_c = "paper"

        print(f'Computer chose {comp_c}')
        if player == comp :
            print("It\'s a draw! Play again!")
        elif (player == 'p' and comp == 'r') or (player == 's' and comp =='p') or (player == 'r' and comp == 's') :
            print("Player Wins!")
            play_again =input("Do you want to play again? Yes (Y) or No (N) : ").lower()
            player_score += 1
        elif (player == 'r' and comp == 'p') or (player == 'p' and comp == 's') or (player == 's' and comp == 'r') :
            print("Computer Wins!")
            play_again =input("Do you want to play again? Yes (Y) or No (N) : ").lower()
            computer_score += 1

    print("The final score is: ")
    print(f"Computer = {computer_score}")
    print(f"Player = {player_score}")
    if computer_score == player_score :
        print("It\'s a draw!")
    elif computer_score > player_score :
        print("Computer Wins!")
    elif computer_score < player_score :
        print("Player wins!")
    
play()
