def construct_adjacency_matrix(graph, n):
    # Câu a: Xây dựng ma trận kề
    adjacency_matrix = [[0] * n for _ in range(n)]
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            adjacency_matrix[node - 1][neighbor - 1] = 1
    return adjacency_matrix

def inorder_traversal(node, graph, visited):
    # Câu b: Thuật toán duyệt cây theo thứ tự Inorder
    if node not in visited:
        visited.add(node)
        neighbors = graph.get(node, [])
        if neighbors:
            inorder_traversal(neighbors[0], graph, visited)
        print(node, end=" ")
        for i in range(1, len(neighbors)):
            inorder_traversal(neighbors[i], graph, visited)

if __name__ == "__main__":
    graph = {
        1: [2, 3],
        2: [5, 6],
        3: [4],
        4: [8],
        5: [7],
        6: [],
        7: [],
        8: []
    }
    
    n = 8
    # Câu a: Xây dựng ma trận kề và in kết quả
    adjacency_matrix = construct_adjacency_matrix(graph, n)
    for row in adjacency_matrix:
        print(row)
    
    # Câu b: Duyệt cây theo thứ tự Inorder và in kết quả
    visited = set()
    inorder_traversal(1, graph, visited)
