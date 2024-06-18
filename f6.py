#6.DICE ROLLING SIMULATOR

import random

def roll_dice():
    return random.randint(1, 6)

def play_round(player):
    roll = roll_dice()
    print(f"{player} rolled a {roll}")
    return roll

def dice_rolling_game():
    player1_wins = 0
    player2_wins = 0

    print("Welcome to the Dice Rolling Game! Best of three wins.\n")

    while player1_wins < 2 and player2_wins < 2:
        print("Rolling dice for Player 1...")
        player1_roll = play_round("Player 1")
        
        print("Rolling dice for Player 2...")
        player2_roll = play_round("Player 2")
        
        if player1_roll > player2_roll:
            player1_wins += 1
            print("Player 1 wins this round!\n")
        elif player2_roll > player1_roll:
            player2_wins += 1
            print("Player 2 wins this round!\n")
        else:
            print("It's a tie! No one wins this round.\n")
        
        print(f"Score: Player 1 - {player1_wins}, Player 2 - {player2_wins}\n")
    
    if player1_wins == 2:
        print("Congratulations! Player 1 is the overall winner!")
    else:
        print("Congratulations! Player 2 is the overall winner!")

if __name__ == "__main__":
    dice_rolling_game()
