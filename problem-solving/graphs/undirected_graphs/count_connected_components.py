def recursive_dfs(graph, current_node, visited):
    visited.add(current_node)
    
    for neighbour in graph[current_node]:
        if neighbour not in visited:
            recursive_dfs(graph, neighbour, visited)

def count_connected_components(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited:
            recursive_dfs(graph, node, visited)
            count += 1

    return count

# Create graphs represented as adjacency lists
graph_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
    'G': ['H'],
    'H': ['G'],
    'I': ['J'],
    'J': ['I'],
}

graph_2 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B'],
    'E': ['F'],
    'F': ['E']
}

graph_3 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

connected_components_graph_1 = count_connected_components(graph_1)
connected_components_graph_2 = count_connected_components(graph_2)
connected_components_graph_3 = count_connected_components(graph_3)
print(f"{connected_components_graph_1 = }")
print(f"{connected_components_graph_2 = }")
print(f"{connected_components_graph_3 = }")
