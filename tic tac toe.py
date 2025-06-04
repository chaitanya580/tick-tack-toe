def print_board(board):
    print("\nCurrent Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print()

def check_winner(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("Player X goes first.")
    print_board(board)

    while True:
        move = input(f"Player {current_player}, enter your move (row,col) from 1-3 (e.g., 2,3): ")
        try:
            row, col = map(int, move.strip().split(","))
            row -= 1
            col -= 1
            if row not in range(3) or col not in range(3):
                print("That’s not a valid spot. Please enter numbers between 1 and 3.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken. Try another one.")
                continue
            board[row][col] = current_player
            print_board(board)
            if check_winner(board, current_player):
                print(f"Congratulations! Player {current_player} wins!")
                break
            if board_full(board):
                print("It's a tie! Well played both.")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Oops! Please enter your move as two numbers separated by a comma (like 1,2).")

if __name__ == "__main__":
    tic_tac_toe()
