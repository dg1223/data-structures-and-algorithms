def recursive_dfs_with_cycle_detection(graph, current_node, parent, visited):
    visited.add(current_node)

    for neighbour in graph[current_node]:
        if neighbour not in visited:
            if recursive_dfs_with_cycle_detection(graph, neighbour, current_node, visited):
                return True
        # e.g. A -> B -> C -> A
        elif parent != neighbour:
            return True

    return False

def has_cycle(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            if recursive_dfs_with_cycle_detection(graph, node, None, visited):
                return True
    
    return False


# Create a graph represented as an adjacency list
#graph = {
#    'A': ['B', 'C'],
#    'B': ['A', 'D', 'E'],
#    'C': ['A', 'F'],
#    'D': ['B'],
#    'E': ['B', 'F'],
#    'F': ['C', 'E']
#}

graph = {
    'A': ['C'],
    'B': ['A', 'D'],
    'C': ['F'],
    'D': [],
    'E': ['B'],
    'F': ['E']
}

if has_cycle(graph):
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")