class DFS:
	def __init__(self, value):
		self.value = value
		self.children = []

	def dfs(self, start, target, path=[]):
		print(f"Visiting node: {start.value}")
		'''
		path = path + [start] creates a new list called
		path on each recursive call and stores the path
		from the child node (current start node) to 
		possible target node.
		If we do path.append(start) or path += [start],
		every new path will be added to the previously
		found path. As a result, we won't be able to 
		track distinct paths of each child.
		'''
		path = path + [start]

		if start.value == target:
			return path

		for child in start.children:
			found_path = self.dfs(child, target, path)
			if found_path:
				return found_path

		return None


root = DFS('A')
two = DFS("B")
three = DFS("C")
root.children = [two, three]
four = DFS("D")
five = DFS("E")
six = DFS("F")
seven = DFS("G")
two.children = [five, four]
three.children = [seven, six]

path = root.dfs(root, 'F')
if not path:
	print(f"No path found from {root.value} to F")
else:
	print(f"Path found from {root.value} to F")
	for node in path:
		print(node.value)