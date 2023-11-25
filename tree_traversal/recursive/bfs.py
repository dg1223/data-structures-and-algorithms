from collections import deque

def bfs(graph, start):
    visited = set()
    '''
    For tree traversal algos, we initialize the tree as 
    a graph using adjacency lists. We also don't need to 
    keep track of any path since we are merely traversing  
    one vertex after another. So, we only need a 1-D list
    /array as we don't need to hold additional lists.
    On the contrary, for binary search, we need to keep 
    track of each path separately. Each path also contains 
    one or more vertices. So, we need a 2-D list that 
    can hold multiple lists as paths.	
    '''
    queue = deque()
    queue.append(start)
    visited.add(start)
    recursive_bfs(graph, queue, visited)

def recursive_bfs(graph, queue, visited):
    if not queue:
        return None

    current_vertex = queue.pop()
    print(current_vertex)

    '''
    Leaf nodes may or may not be intialized as keys in the
    adjacency list dictionary. If they are not keys, then
    we don't need to search for their neighbours.
    '''
    if current_vertex in graph:
        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                queue.appendleft(neighbour)
                visited.add(neighbour)

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