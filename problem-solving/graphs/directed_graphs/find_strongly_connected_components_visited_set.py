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
        visited.add(vertex)
        #print(f"{vertex = }, graph = {self.graph[vertex]}, {visited = }")
        # here, self.graph is the original graph
        for neighbor in self.graph[vertex]:
            #print(f"{neighbor = }")
            if neighbor not in visited:
                self.dfs(neighbor, stack, visited)
        stack.append(vertex)

    def transpose(self):
        transposed_graph = Graph(self.vertices)
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                transposed_graph.add_edge(neighbor, vertex)
        return transposed_graph

    def dfs_on_transposed_graph(self, vertex, individual_scc_list, visited):
        visited.add(vertex)
        individual_scc_list.append(vertex)
        # here, self.graph is the transposed graph
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_on_transposed_graph(neighbor, individual_scc_list, visited)

    def strongly_connected_components(self):
        stack = []
        visited = set()
        #vertices = set(self.graph.keys())
        #print(f"{vertices = }")

        for vertex in self.graph:
            if vertex not in visited:
                self.dfs(vertex, stack, visited)

        transposed_graph = self.transpose()
        visited = set()
        strongly_connected_components = []

        while stack:
            current_vertex = stack.pop()
            '''
            I tend to forget checking the visited set here.
            '''
            if current_vertex not in visited:
                # we need this list to print the components
                individual_scc_list = []
                transposed_graph.dfs_on_transposed_graph(current_vertex, individual_scc_list, visited)
                strongly_connected_components.append(individual_scc_list)

        return strongly_connected_components


# Test case
g = Graph(5)
g.add_edge('A', 'B')
g.add_edge('B', 'C')
g.add_edge('C', 'A')
g.add_edge('B', 'D')
g.add_edge('D', 'E')

scc_list = g.strongly_connected_components()
print("Strongly Connected Components:")
for idx, component in enumerate(scc_list):
		print(f"SCC #{idx} = {component}")
