from collections import deque

def recursive_bfs(graph, queue, visited):
    if not queue:
        return None

    # either popleft and append or
    # pop and appendleft
    current_vertex = queue.pop()
    print(current_vertex)

    if current_vertex in graph:
        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                queue.appendleft(neighbour)
                visited.add(neighbour)

    recursive_bfs(graph, queue, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    recursive_bfs(graph, queue, visited)

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