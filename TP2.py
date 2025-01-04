from collections import defaultdict, deque

# Graph input: adjacency list
edges = [
    (1, 2), (1, 4), (2, 3), (3, 7), (7, 6), (6, 2), 
    (7, 5), (4, 5), (5, 5), (8, 3), (8, 9)
]

# Step 1: Create Adjacency Matrix
def create_adjacency_matrix(edges, n):
    matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        matrix[u-1][v-1] = 1
    return matrix

# Step 2: Find SCC using Kosaraju's Algorithm
def kosaraju_scc(n, edges):
    def dfs(v, graph, visited, stack):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor, graph, visited, stack)
        stack.append(v)

    def dfs_reverse(v, graph, visited, component):
        visited[v] = True
        component.append(v)
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs_reverse(neighbor, graph, visited, component)

  
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    for u, v in edges:
        graph[u-1].append(v-1)
        reverse_graph[v-1].append(u-1)

   
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(i, graph, visited, stack)

    
    visited = [False] * n
    scc = []
    while stack:
        v = stack.pop()
