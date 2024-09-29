'''
O(V+E) time, O(V) space
'''

def dfs(graph, start, visited=None):
    if not visited:
        visited = set()

    print(start)

    visited.add(start)
    parent = graph[start]

    for child in parent:
        if child not in visited:
            dfs(graph, child, visited)

'''
			A
		/	  	\
	   B     	 C
	 / 	 \     /
	D     E - F
'''

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs(graph, 'A')