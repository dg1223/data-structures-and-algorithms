def recursive_dfs_with_cycle_detection(graph, current_node, parent, visited, cycle):
    visited.add(current_node)
    cycle.append(current_node)

    for neighbour in graph[current_node]:
        if neighbour not in visited:
            if recursive_dfs_with_cycle_detection(graph, neighbour, current_node, visited, cycle):
                return True
        elif parent != neighbour and neighbour in cycle:
            print("Cycle:", cycle[cycle.index(neighbour):] + [neighbour])
            return True

    cycle.pop()
    return False

def has_cycle(graph):
    visited = set()

    for node in graph:
        if node not in visited:
            cycle = []
            if recursive_dfs_with_cycle_detection(graph, node, None, visited, cycle):
                return True
    
    return False

# Create a graph represented as an adjacency list
undirected_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

directed_graph = {
    'A': ['C'],
    'B': ['A', 'D'],
    'C': ['F'],
    'D': [],
    'E': ['B'],
    'F': ['E']
}

if has_cycle(undirected_graph):
    print("The undirected graph contains a cycle.")
else:
    print("The undirected graph does not contain a cycle.")

if has_cycle(directed_graph):
    print("The directed graph contains a cycle.")
else:
    print("The directed graph does not contain a cycle.")
