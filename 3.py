from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    # Create a queue for BFS and add the initial state (0, 0)
    queue = deque([(0, 0)])
    # Set to keep track of visited states
    visited = set((0, 0))
    
    while queue:
        jug1, jug2 = queue.popleft()
        print(jug1,jug2)
        if jug1 == target or jug2 == target:
            return True
        
        # List all possible states from the current state
        possible_states = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  # Pour jug1 to jug2
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   # Pour jug2 to jug1
        ]
        
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    
    return False

# Example usage
jug1_capacity = 4
jug2_capacity = 3
target = 2

if water_jug_bfs(jug1_capacity, jug2_capacity, target):
    print("Solution exists")
else:
    print("No solution exists")
