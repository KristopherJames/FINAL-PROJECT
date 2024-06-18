#5.ROCK PAPER SCISSORS GAME

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice. Please try again.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    
    return winner

def rock_paper_scissors():
    user_wins = 0
    computer_wins = 0
    
    print("Welcome to Rock-Paper-Scissors! Best of three wins.")
    
    while user_wins < 2 and computer_wins < 2:
        winner = play_round()
        
        if winner == "user":
            user_wins += 1
        elif winner == "computer":
            computer_wins += 1
        
        print(f"Score: You {user_wins} - {computer_wins} Computer\n")
    
    if user_wins == 2:
        print("Congratulations! You are the overall winner!")
    else:
        print("Computer wins the game! Better luck next time!")

if __name__ == "__main__":
    rock_paper_scissors()
