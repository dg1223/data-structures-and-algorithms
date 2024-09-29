from collections import deque

class BFS:
	def __init__(self, value):
		self.value = value
		self.children = []

	def bfs(self, start_node, target):
		print(f"Visiting {start_node.value}")
		'''
        Deque is a doubly-linked list. 
        
        We need to keep track of each path separately. 
        In BFS, we do this using a queue that holds all the 
        paths as separate lists.
        
        On the other hand, the data structure to hold a tree  
        for tree traversal algorithms is different. For 
        traversal, we initialize the tree as a graph using 
        adjacency lists. Since we are only traversing, we 
        don't need to store any path. So, we only need a 
        1-D list/array.		
        '''
		path = [start_node]

		# No need to proceed if we already found a match
		if start_node.value == target:
			return path

		'''
        If we do frontier = deque(start), then deque() unpacks
        the list 'start' and appends its contents from left to
        right inside it. As a result, when we pop from the 
        deque, it returns individual item (node object in our 
        case) which is not iterable when we do current_path[-1]
        Initializing an empty deque first and then appending 
        'start' appends the list [start] to the deque which 
        remains iterable when popped later.
        '''
        #frontier = deque(path)
		frontier = deque()
		frontier.append(path)

		# while a path still exists in the queue
		while frontier:
			current_path = frontier.pop()
			current_node = current_path[-1]
			for child in current_node.children:
				print(f"Visiting {child.value}")
				new_path = current_path.copy()
				new_path.append(child)
				if child.value == target:
					return new_path
				frontier.appendleft(new_path)

		# No necessary but good for readability
		return None

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

start = root
target = 'G'
path = root.bfs(start, target)

if path:
	print(f"Path found from {start.value} to {target}")
	string = " -> ".join(node.value for node in path)
	#string = ""
	#length = len(path)
	#for node in path:		
	#	if length == 1:
	#		string += node.value
	#	else:
	#		string += node.value + " -> "
	#	length -= 1;
	print(string)
else:
	print(f"No path found from {start.value} to {target}")
		