'''
Using adjacency list, queue and while loop
'''

from collections import deque

def bfs(graph, start):
	print(start)
	visited = set()
	queue = deque()
	queue.appendleft(graph[start])
	visited.add(start)

	while queue:
		parent = queue.pop()
		for child in parent:
			if child not in visited:
				print(child)
				queue.appendleft(graph[child])
				visited.add(child)

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

bfs(graph, 'A')