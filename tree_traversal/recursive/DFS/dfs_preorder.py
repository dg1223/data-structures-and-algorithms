def recursive_dfs(structure, stack, visited):
    if not stack:
        return None

    current_node = stack.pop()
    print(current_node)

    if current_node in structure:
        for neighbour in structure[current_node]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
                # call DFS to traverse the children before 
                # it reaches the sibling
                recursive_dfs(structure, stack, visited)

def dfs(structure, start):
    visited = set()
    stack = [start]
    visited.add(start)
    recursive_dfs(structure, stack, visited)

## Create a graph represented as an adjacency list
#graph = {
#    'A': ['B', 'C'],
#    'B': ['A', 'D', 'E'],
#    'C': ['A', 'F'],
#    'D': ['B'],
#    'E': ['B', 'F'],
#    'F': ['C', 'E']
#}
#dfs(graph, 'A')

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Call DFS starting from node 'A'
dfs(tree, 'A')