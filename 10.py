from heapq import heappop, heappush

def a_star(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    open_list = []
    heappush(open_list, (0 + heuristic(start, end), 0, start))
    g_costs = {start: 0}
    parents = {start: None}
    
    while open_list:
        _, cost, current = heappop(open_list)
        
        if current == end:
            return reconstruct_path(parents, current)
        
        for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and grid[neighbor[0]][neighbor[1]] == 0:
                tentative_g_cost = cost + 1
                if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                    g_costs[neighbor] = tentative_g_cost
                    f_cost = tentative_g_cost + heuristic(neighbor, end)
                    heappush(open_list, (f_cost, tentative_g_cost, neighbor))
                    parents[neighbor] = current
    return None

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def reconstruct_path(parents, current):
    path = []
    while current:
        path.append(current)
        current = parents[current]
    return path[::-1]

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)
print(a_star(grid, start, end))
