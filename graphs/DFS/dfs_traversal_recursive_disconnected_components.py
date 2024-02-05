'''
O(V+E) time, O(V) space
'''

visited = set()

def dfs(graph, source):

    print(source)

    visited.add(source)

    for child in graph[source]:
        if child not in visited:
            dfs(graph, child)

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

'''
The for loop takes care disconnected components
'''
for vertex in graph_1:
	if vertex not in visited:
		dfs(graph_1, vertex)

print()

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

print()
'''
The for loop takes care disconnected components
'''
for vertex in graph_2:
	if vertex not in visited:
		dfs(graph_2, vertex)

'''
Directed graph

		 0	    3
		/	 / 	   \
	   .	.		.
	   1    4 	    6
	  /	     \     /
	 .		  .   .
	 2          5
'''

graph_3 = {
     '0': ['1'],
     '1': ['2'],
	 '2': [],
     '3': ['4'],
     '4': ['5'],
     '5': ['6'],
     '6': ['3']
}

for vertex in graph_3:
	if vertex not in visited:
		dfs(graph_3, vertex)