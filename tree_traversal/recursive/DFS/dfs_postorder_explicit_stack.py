def recursive_postorder_dfs(graph, stack, visited):
    # base case
    if not stack:
        return None

    current_vertex = stack.pop()    

    if current_vertex in graph:
        for neighbour in graph[current_vertex]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)
                # call DFS to traverse the children before 
                # it reaches the sibling
                recursive_postorder_dfs(graph, stack, visited)
    
    print(current_vertex)

def postorder_dfs(graph, start):
    # Edge case: empty graph as input
    if start not in graph:
        print("Graph is empty")
        return None

    visited = set()
    stack = [start]
    visited.add(start)
    recursive_postorder_dfs(graph, stack, visited)

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

#tree = {}

# Call DFS starting from node 'A'
postorder_dfs(tree, 'A')