from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)


    def dfs(self, vertex, stack, visited):
        visited[vertex] = True
        #print(f"{vertex = }, graph = {self.graph[vertex]}, {visited = }")
        # here, self.graph is the original graph
        for neighbor in self.graph[vertex]:
            #print(f"{neighbor = }")
            if not visited[neighbor]:
                self.dfs(neighbor, stack, visited)
        stack.append(vertex)

    def transpose(self):
        transposed_graph = Graph(self.vertices)
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transposed_graph.add_edge(neighbor, vertex)
        return transposed_graph

    def dfs_on_transposed_graph(self, vertex, scc, visited):
        visited[vertex] = True
        scc.append(vertex)
        # here, self.graph is the transposed graph
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_on_transposed_graph(neighbor, scc, visited)

    def strongly_connected_components(self):
        stack = []
        #vertices = set(self.graph.keys())
        #print(f"{vertices = }")
        visited = {vertex: False for vertex in self.graph.keys()}

        for vertex in self.graph:
            if not visited[vertex]:
                self.dfs(vertex, stack, visited)

        transposed_graph = self.transpose()
        visited = {vertex: False for vertex in transposed_graph.graph.keys()}
        strongly_connected_components = []

        while stack:
            current_vertex = stack.pop()
            if not visited[current_vertex]:
                scc_stack = []
                transposed_graph.dfs_on_transposed_graph(current_vertex, scc_stack, visited)
                strongly_connected_components.append(scc_stack)

        return strongly_connected_components


# Test case
g = Graph(5)
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')
g.add_edge('B', 'D')
g.add_edge('D', 'E')

scc_result = g.strongly_connected_components()
print("Strongly Connected Components:")
for component in scc_result:
    print(component)
