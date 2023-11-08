def recursive_postorder_dfs(structure, stack, visited):
    if not stack:
        return None

    current_node = stack.pop()    

    if current_node in structure:
        for neighbour in structure[current_node]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
                # call DFS to traverse the children before 
                # it reaches the sibling
                recursive_postorder_dfs(structure, stack, visited)
    
    print(current_node)

def postorder_dfs(structure, start):
    visited = set()
    stack = [start]
    visited.add(start)
    recursive_postorder_dfs(structure, stack, visited)

## Create a graph represented as an adjacency list
#graph = {
#    'A': ['B', 'C'],
#    'B': ['A', 'D', 'E'],
#    'C': ['A', 'F'],
#    'D': ['B'],
#    'E': ['B', 'F'],
#    'F': ['C', 'E']
#}
#postorder_dfs(graph, 'A')

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

# Call DFS starting from node 'A'
postorder_dfs(tree, 'A')