import heapq

# Initial and goal states
start_board = [
    [0, 1, 3],
    [4, 2, 5],
    [7, 8, 6]
]
goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Moves: (dx, dy)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Manhattan distance heuristic
def manhattan(board):
    return sum(abs(i - (val-1)//3) + abs(j - (val-1)%3) for i, row in enumerate(board) for j, val in enumerate(row) if val)

# BFS using priority queue for A* search
open_set = [(manhattan(start_board), start_board)]
closed_set = set()
parent = {tuple(map(tuple, start_board)): None}

while open_set:
    _, board = heapq.heappop(open_set)
    if board == goal_board:
        path = []
        while board:
            path.append(board)
            board = parent[tuple(map(tuple, board))]
        for state in path[::-1]:
            for row in state:
                print(row)
            print()
        break
    closed_set.add(tuple(map(tuple, board)))
    x, y = next((i, j) for i, row in enumerate(board) for j, val in enumerate(row) if val == 0)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = [row[:] for row in board]
            new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
            new_tup = tuple(map(tuple, new_board))
            if new_tup not in closed_set:
                heapq.heappush(open_set, (manhattan(new_board), new_board))
                parent[new_tup] = board
