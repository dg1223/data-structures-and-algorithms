# pre-order traversal
def dfs(graph, source, destination, visited=None):
    if not visited:
        visited = []

    visited = visited + [source]
    
    if source == destination:
        return visited
    
    for neighbour in graph[source]:
        if neighbour not in visited:
            path = dfs(graph, neighbour, destination, visited)
            if path:
                return path

#graph = {
#  'lava': set(['sharks', 'piranhas']),
#  'sharks': set(['lava', 'bees', 'lasers']),
#  'piranhas': set(['lava', 'crocodiles']),
#  'bees': set(['sharks']),
#  'lasers': set(['sharks', 'crocodiles']),
#  'crocodiles': set(['piranhas', 'lasers'])
#}

#print(dfs(graph, "crocodiles", "bees"))

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs(graph, 'A', 'F'))