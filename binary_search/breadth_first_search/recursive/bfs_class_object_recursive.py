from collections import deque

class BFS:
	def __init__(self, value):
		self.value = value
		self.children = []

	def bfs(self, start_node, target):
		'''
		The deque structure is basically a (doubly-linked)
		list. We need to keep track of each path separately. 
		For BFS, a (frontier) queue does the job. So, we 
		need each queue to be a list so that we can access
		individial nodes from any list. As a result, the 
		frontier queue becomes a 2-D list or array.
		On the contrary, the data structure to hold the tree  
		is different for tree traversal algos where we 
		initialize the tree as a graph using adjacency lists. 
		We also don't need to store any path for traversal 
		algos. So, we only need a 1-D list/array as we don't 
		need to hold additional lists.		
		'''
		path = [start_node]
		if start_node.value == target:
			print(f"Visiting {start_node.value}")
			return path
		frontier = deque()
		frontier.append(path)

		return self.bfs_recursive(frontier, target)

	def bfs_recursive(self, queue, target):		
		if not queue:
			return None

		path = queue.pop()
		current_node = path[-1]
		print(f"Visiting {current_node.value}")
		if current_node.value == target:
			return path
		for child in current_node.children:
			new_path = path + [child]
			queue.appendleft(new_path)

		return self.bfs_recursive(queue, target)


root = BFS('A')
two = BFS("B")
three = BFS("C")
root.children = [two, three]
four = BFS("D")
five = BFS("E")
six = BFS("F")
seven = BFS("G")
two.children = [five, four]
three.children = [seven, six]

path = root.bfs(root, 'F')
if not path:
	print(f"No path found from {root.value} to F")
else:
	print(f"Path found from {root.value} to F")
	for node in path:
		print(node.value)