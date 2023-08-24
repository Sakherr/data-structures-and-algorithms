class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value):
        self.nodes.append(Node(value))

    def add_edge(self, node1, node2):
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

    def depth_first(self, start_node):
        visited = set()
        traversal_order = []

        def dfs(node):
            visited.add(node)
            traversal_order.append(node.value)
            
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_node)
        return traversal_order