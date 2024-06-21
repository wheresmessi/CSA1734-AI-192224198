def print_board(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
        if col - i - 1 >= 0 and board[row - i - 1][col - i - 1] == 1:
            return False
        if col + i + 1 < len(board) and board[row - i - 1][col + i + 1] == 1:
            return False
    return True

def solve_nqueens(board, row):
    if row == len(board):
        print_board(board)
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            if solve_nqueens(board, row + 1):
                return True
            board[row][col] = 0

    return False

def solve_8queens():
    board = [[0] * 8 for _ in range(8)]
    if not solve_nqueens(board, 0):
        print("No solution exists")

solve_8queens()
