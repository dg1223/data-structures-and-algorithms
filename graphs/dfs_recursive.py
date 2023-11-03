# pre-order traversal
def dfs(graph, start_vertex, target_vertex, visited=None):
    if not visited:
        visited = []

    visited = visited + [start_vertex]
    
    if start_vertex == target_vertex:
        return visited
    
    for neighbour in graph[start_vertex]:
        if neighbour not in visited:
            path = dfs(graph, neighbour, target_vertex, visited)
            if path:
                return path

the_most_dangerous_graph = {
  'lava': set(['sharks', 'piranhas']),
  'sharks': set(['lava', 'bees', 'lasers']),
  'piranhas': set(['lava', 'crocodiles']),
  'bees': set(['sharks']),
  'lasers': set(['sharks', 'crocodiles']),
  'crocodiles': set(['piranhas', 'lasers'])
  }

print(dfs(the_most_dangerous_graph, "crocodiles", "bees"))