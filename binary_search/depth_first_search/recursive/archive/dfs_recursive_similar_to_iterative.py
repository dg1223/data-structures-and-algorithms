class DFS:
	def __init__(self, value):
		self.value = value
		self.children = []

	def dfs(self, start_node, target):
		path = [start_node]
		if start_node.value == target:
			return path

		frontier = [(start_node, path)]
		return self.dfs_recursive(frontier, target)

	def dfs_recursive(self, stack, target):
		current_node, path = stack.pop()
		print(f"Visiting {current_node.value}")
		if current_node.value == target:
			return path
		for child in current_node.children:
			stack.append((child, path + [child]))
			found_path = self.dfs_recursive(stack, target)
			if found_path:
				return found_path
		
		# No necessary but good for readability
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

start = root
target = 'F'
path = root.dfs(start, target)

if path:
	print(f"Path found from {start.value} to {target}")
	string = " -> ".join(node.value for node in path)
	print(string)
else:
	print(f"Path not found from {start.value} to {target}")