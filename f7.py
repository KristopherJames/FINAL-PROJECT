#7.TIC TAC TOE GAME

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    win_conditions = [
        # Horizontal wins
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical wins
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal wins
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [player, player, player] in win_conditions

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(player):
    while True:
        try:
            row = int(input(f"{player}, enter the row (1, 2, 3): ")) - 1
            col = int(input(f"{player}, enter the column (1, 2, 3): ")) - 1
            if row in [0, 1, 2] and col in [0, 1, 2]:
                return row, col
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    player1 = input("Enter the name of Player 1 (X): ")
    player2 = input("Enter the name of Player 2 (O): ")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = player1
    current_marker = "X"
    
    while True:
        print_board(board)
        row, col = get_player_move(current_player)
        
        if board[row][col] == " ":
            board[row][col] = current_marker
        else:
            print("The position is already taken. Try again.")
            continue
        
        if check_winner(board, current_marker):
            print_board(board)
            print(f"Congratulations! {current_player} wins!")
            break
        
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = player2 if current_player == player1 else player1
        current_marker = "O" if current_marker == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
