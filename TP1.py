class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, start, end):
        """Adds a directed edge from start to end."""
        if start not in self.adjacency_list:
            self.adjacency_list[start] = []
        self.adjacency_list[start].append(end)

    def path_exists(self, start, end):
        """Returns True if a path exists between start and end, else False."""
        if start not in self.adjacency_list:
            return False
        
        visited = set()
        return self.dfs(start, end, visited)

    def dfs(self, current, target, visited):
        """Helper method for depth-first search."""
        if current == target:
            return True
        visited.add(current)
        for neighbor in self.adjacency_list.get(current, []):
            if neighbor not in visited:
                if self.dfs(neighbor, target, visited):
                    return True
        return False


# Create the graph from the provided image
graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(2, 5)
graph.add_edge(5, 6)
graph.add_edge(3, 6)
graph.add_edge(4, 6)
graph.add_edge(6, 7)

start_node = int(input("Enter the start node: "))
end_node = int(input("Enter the end node: "))

if graph.path_exists(start_node, end_node):
    print("True")
else:
    print("False")


#====
# Student name: Le Quang Minh
# Student ID: 22BI13286



