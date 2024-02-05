'''
Using adjacency list, queue and while loop
O(V+E) time, O(V) space
'''

from collections import deque

def bfs(graph, start):
	print(start)
	visited = set()
	visited.add(start)

	parent_array = {key: -1 for key in graph}

	queue = deque()
	queue.appendleft(graph[start])

	found_cycle = False

	while queue:
		parent = queue.pop()
		print(visited, parent)
		for child in parent:			
			#breakpoint()
			if child in visited and parent_array[parent[0]] != child:
				found_cycle = True
				break

			if child not in visited:
				print(child)
				visited.add(child)
				parent_array[child] = parent
				queue.appendleft(graph[child])
				

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

#bfs(graph_1, 'A')

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

bfs(graph_2, '0')