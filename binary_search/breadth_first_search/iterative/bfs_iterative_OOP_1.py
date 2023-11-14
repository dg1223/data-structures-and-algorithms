from collections import deque

class BFS:
    def __init__(self, value):
        self.value = value
        self.children = []

    def bfs(self, root, target):
        frontier_queue = deque()
        start = [root]
        frontier_queue.appendleft(start)

        while frontier_queue:
            current_path = frontier_queue.pop()
            current_node = current_path[-1]
            print(f"current node = {current_node.value}")
            if current_node.value == target:
                return current_path
            for child in current_node.children:
                print(f"child = {child.value}")
                new_path = current_path.copy()
                new_path.append(child)
                frontier_queue.appendleft(new_path)
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

path = root.bfs(root, 'F')
if not path:
    print(f"No path found from {root.value} to F")
else:
    print(f"Path found from {root.value} to F")
    for node in path:
        print(node.value)