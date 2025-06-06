def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell in ['X', 'O'] for row in board for cell in row])

def tic_tac_toe():
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        move = input(f"Player {current_player}, enter your move (1-9): ")
        if not move.isdigit() or not 1 <= int(move) <= 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        move = int(move) - 1
        row, col = divmod(move, 3)
        if board[row][col] in ['X', 'O']:
            print("Cell already taken. Try a different move.")
            continue

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
