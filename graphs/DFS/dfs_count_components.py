'''
O(V+E) time, O(V) space
'''

def dfs(graph, source):
    visited.add(source)

    for child in graph[source]:
        if child not in visited:
            dfs(graph, child)

def count_components(graph, source, visited):
	num_components = 0
	'''
	We are going to perform DFS on every vertex.
	If there's a dead-end, the function will return.
	Then we increment the number of components by 1.
	For every component, dfs() will return once. This
	is how we can count the number of components.
	'''
	for vertex in graph:
		if vertex not in visited:
			dfs(graph, vertex)
			num_components += 1

	return num_components


'''
			A
		/	  	\
	   B     	 C
	 / 	 \     /
	D     E - F
'''

graph_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

visited = set()
components = count_components(graph_1, 'A', visited)
print(f"{components = }")


'''
         0	    3
        /	 / 	   \
       1    4 	    6
      /	     \     /
     2          5
'''

graph_2 = {
     '0': ['1'],
     '1': ['0', '2'],
     '2': ['1'],
     '3': ['4', '6'],
     '4': ['3', '5'],
     '5': ['4', '6'],
     '6': ['3', '5']
}

visited = set()
components = count_components(graph_2, '0', visited)
print(f"{components = }")


'''
         0	    3		7
        /	 / 	   \
       1    4 	    6
      /	     \     /
     2          5
'''

graph_3 = {
     '0': ['1'],
     '1': ['0', '2'],
     '2': ['1'],
     '3': ['4', '6'],
     '4': ['3', '5'],
     '5': ['4', '6'],
     '6': ['3', '5'],
	 '7': []
}

visited = set()
components = count_components(graph_3, '0', visited)
print(f"{components = }")