def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    for _ in range(9):
        print_board(board)
        row, col = map(int, input(f'Player {current_player}, enter your move (row col): ').split())
        if board[row][col] == ' ':
            board[row][col] = current_player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f'Player {winner} wins!')
                return
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Invalid move, try again.')
    print_board(board)
    print('It\'s a draw!')

tic_tac_toe()
