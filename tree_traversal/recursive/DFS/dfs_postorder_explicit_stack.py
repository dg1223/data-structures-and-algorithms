def recursive_postorder_dfs(tree, stack, visited):
    # base case
    if not stack:
        return None

    current_vertex = stack.pop()    

    if current_vertex in tree:
        for neighbour in tree[current_vertex]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
                # call DFS to traverse the children before 
                # it reaches the sibling
                recursive_postorder_dfs(tree, stack, visited)
    
    print(current_vertex)

def postorder_dfs(tree, start):
    # Edge case: empty graph as input
    if start not in tree:
        print("Graph is empty")
        return None

    visited = set()
    stack = [start]
    visited.add(start)
    recursive_postorder_dfs(tree, stack, visited)


tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G']
}

#tree = {}

# Call DFS starting from node 'A'
postorder_dfs(tree, 'A')