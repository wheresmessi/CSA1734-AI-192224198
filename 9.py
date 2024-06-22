import itertools

def tsp(graph, start):
    vertices = list(graph.keys())
    vertices.remove(start)
    min_path = float('inf')
    for perm in itertools.permutations(vertices):
        current_path_weight = 0
        k = start
        for j in perm:
            current_path_weight += graph[k][j]
            k = j
        current_path_weight += graph[k][start]
        min_path = min(min_path, current_path_weight)
    return min_path

graph = {
    0: {1: 10, 2: 15, 3: 20},
    1: {0: 10, 2: 35, 3: 25},
    2: {0: 15, 1: 35, 3: 30},
    3: {0: 20, 1: 25, 2: 30}
}
start = 0
print(tsp(graph, start))
