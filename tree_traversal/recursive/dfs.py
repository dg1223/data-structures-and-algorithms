from collections import deque

def recursive_dfs(structure, queue, visited):
    if not queue:
        return None

    current_node = queue.pop()
    print(current_node)

    if current_node in structure:
        for neighbour in structure[current_node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                # call DFS to traverse the children before 
                # it reaches the sibling
                recursive_dfs(structure, queue, visited)

def dfs(structure, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    recursive_dfs(structure, queue, visited)

# Create a graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
dfs(graph, 'A')

#tree = {
#    'A': ['B', 'C'],
#    'B': ['D', 'E'],
#    'C': ['F', 'G']
#}
#
## Call BFS starting from node 'A'
#dfs(tree, 'A')