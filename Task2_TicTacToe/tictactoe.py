# Task 2 - Tic Tac Toe Game
# Author: Your Name (CODSOFT Internship)

def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

def check_winner(board, player):
    # All possible winning combinations
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    for turn in range(9):
        while True:
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
                if board[move] == " ":
                    board[move] = current_player
                    break
                else:
                    print("That spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter a number between 1 and 9.")

        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins! 🎉")
            return

        current_player = "O" if current_player == "X" else "X"

    print("It's a draw! 🤝")

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
