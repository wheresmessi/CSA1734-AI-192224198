from collections import deque

def is_valid(state):
    m_left, c_left, boat, m_right, c_right = state
    
    # Check if missionaries outnumbered by cannibals
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    
    return True

def bfs():
    initial_state = (3, 3, 1, 0, 0)  # (m_left, c_left, boat, m_right, c_right)
    goal_state = (0, 0, 0, 3, 3)
    
    queue = deque([(initial_state, [])])  # (state, path)
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        m_left, c_left, boat, m_right, c_right = current_state
        
        if current_state == goal_state:
            return path + [current_state]
        
        for move in [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]:
            if boat == 1:
                new_state = (m_left - move[0], c_left - move[1], 0, m_right + move[0], c_right + move[1])
            else:
                new_state = (m_left + move[0], c_left + move[1], 1, m_right - move[0], c_right - move[1])
            
            if is_valid(new_state) and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [current_state]))
    
    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        print("Missionaries and Cannibals Solution:")
        for state in solution:
            print(f"Left: {state[0]}M-{state[1]}C Boat: {'>' if state[2] == 1 else '<'} Right: {state[3]}M-{state[4]}C")
        print(f"Solution found in {len(solution) - 1} steps.")

# Solve the problem using BFS
solution = bfs()
print_solution(solution)
