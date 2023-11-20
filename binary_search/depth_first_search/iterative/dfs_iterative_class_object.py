class DFS:
    def __init__(self, value):
        self.value = value
        self.children = []

    def dfs(self, start, target):
        frontier = []
        start = [start]
        frontier.append(start)

        while frontier:
            current_path = frontier.pop()
            current_node = current_path[-1]
            print(f"current_node = {current_node.value}")
            if current_node.value == target:
                return current_path
            for child in current_node.children:
                print(f"child = {child.value}")
                new_path = current_path.copy()
                new_path.append(child)
                frontier.append(new_path)

        return None


root = DFS('A')
two = DFS("B")
three = DFS("C")
root.children = [three, two]
four = DFS("D")
five = DFS("E")
six = DFS("F")
seven = DFS("G")
two.children = [five, four]
three.children = [seven, six]

frontier = root.dfs(root, 'F')
if not frontier:
    print(f"No path found from {root.value} to F")
else:
    print(f"Path found from {root.value} to F")
    for node in frontier:
        print(node.value)