def recursive_preorder_dfs(graph, stack, visited):
    if not stack:
        return None

    current_vertex = stack.pop()
    print(current_vertex)

    if current_vertex in graph:
        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
                # call DFS to traverse the children before 
                # it reaches the sibling
                recursive_preorder_dfs(graph, stack, visited)

def preorder_dfs(structure, start):
    visited = set()
    stack = [start]
    visited.add(start)
    recursive_preorder_dfs(structure, stack, visited)

## Create a graph represented as an adjacency list
#graph = {
#    'A': ['B', 'C'],
#    'B': ['A', 'D', 'E'],
#    'C': ['A', 'F'],
#    'D': ['B'],
#    'E': ['B', 'F'],
#    'F': ['C', 'E']
#}
#preorder_dfs(graph, 'A')

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Call DFS starting from node 'A'
preorder_dfs(tree, 'A')