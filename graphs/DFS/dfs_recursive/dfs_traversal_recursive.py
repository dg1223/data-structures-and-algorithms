def dfs(graph, source, visited=None):
    if not visited:
        visited = set()

    print(source)

    visited.add(source)

    for child in graph[source]:
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

print(dfs(graph, 'A'))