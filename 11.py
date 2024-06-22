def is_safe(graph, color, node, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def map_coloring(graph, color, node, colors):
    if node == len(graph):
        return True
    for c in colors:
        if is_safe(graph, color, node, c):
            color[node] = c
            if map_coloring(graph, color, node + 1, colors):
                return True
            color[node] = None
    return False

def solve_map_coloring(graph, colors):
    color = [None] * len(graph)
    if not map_coloring(graph, color, 0, colors):
        return None
    return color

graph = [
    [1, 2, 3],
    [0, 2],
    [0, 1, 3],
    [0, 2]
]
colors = ['Red', 'Green', 'Blue']
print(solve_map_coloring(graph, colors))
