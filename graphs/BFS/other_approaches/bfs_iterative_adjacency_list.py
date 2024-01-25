def bfs(graph, start_vertex, target_vertex):
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    visited = set()
    bfs_queue = [vertex_and_path]

    while bfs_queue:
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex)
        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                current_path = path + [neighbour]
                if neighbour == target_vertex:
                    return current_path
                bfs_queue.append([neighbour, current_path])

the_most_dangerous_graph = {
    'lava': set(['sharks', 'piranhas']),
    'sharks': set(['lava', 'bees', 'lasers']),
    'piranhas': set(['lava', 'crocodiles']),
    'bees': set(['sharks']),
    'lasers': set(['sharks', 'crocodiles']),
    'crocodiles': set(['piranhas', 'lasers'])
  }

print(bfs(the_most_dangerous_graph, "crocodiles", "bees"))