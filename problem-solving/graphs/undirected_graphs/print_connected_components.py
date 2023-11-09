def recursive_dfs(graph, current_node, visited, components):
    visited.add(current_node)
    components.append(current_node)
    
    for neighbour in graph[current_node]:
        if neighbour not in visited:
            recursive_dfs(graph, neighbour, visited, components)

def count_connected_components(graph):
    visited = set()
    connected_components = []

    for node in graph:
        if node not in visited:
            # this list remains within the scope of recursion
            components = []
            recursive_dfs(graph, node, visited, components)
            connected_components.append(components)

    return connected_components

# Create a graph represented as an adjacency list
graph = {
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

connected_components = count_connected_components(graph)
print(f"Number of connected components = {len(connected_components)}\n")

# print connected components
for idx, components in enumerate(connected_components):
    print(f"Connected component {idx+1} = {components}")
