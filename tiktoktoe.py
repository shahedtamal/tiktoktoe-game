def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row.count(row[0]) == 3 and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        try:
            row = int(input(f"Player {current_player}, enter your row (0-2): "))
            col = int(input(f"Player {current_player}, enter your column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
        
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid position. Please enter numbers between 0 and 2.")
            continue
        
        if board[row][col] != ' ':
            print("Cell is already occupied. Try again.")
            continue
        
        board[row][col] = current_player
        
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()