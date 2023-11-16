from collections import deque

def recursive_bfs(graph, queue, visited):
    if not queue:
        return None

    # either popleft and append or
    # pop and appendleft
    current_node = queue.pop()
    print(current_node)

    if current_node in graph:
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                queue.appendleft(neighbour)
                visited.add(neighbour)

    recursive_bfs(graph, queue, visited)

def bfs(structure, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    recursive_bfs(structure, queue, visited)

# Create a graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')

#tree = {
#    'A': ['B', 'C'],
#    'B': ['D', 'E'],
#    'C': ['F', 'G']
#}
#
## Call BFS starting from node 'A'
#bfs(tree, 'A')