# pre-order traversal
def dfs(graph, start, destination, visited=None):
    # we can't initialize a set because we need to return
    # the visited vertices as the path
    if not visited:
        visited = []

    visited = visited + [start]
    
    if start == destination:
        return visited
    
    current_root = graph[start]
    
    for neighbour in current_root:
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