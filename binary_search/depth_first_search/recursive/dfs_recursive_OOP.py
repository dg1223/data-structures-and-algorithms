class DFS:
	def __init__(self, value):
		self.value = value
		self.children = []

	def dfs(self, start, target, path=[]):
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