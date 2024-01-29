'''
Using adjacency list, queue and while loop
'''

from collections import deque

def bfs(graph, start):
	visited = set()
	queue = deque()
	queue.appendleft(start)
	visited.add(start)

	while queue:
		parent = queue.pop()
		print(parent)

		for child in parent: