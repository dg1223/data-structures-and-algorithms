from collections import deque

class BFS:
    def __init__(self, value):
        self.value = value
        self.children = []

    def bfs(self, root, target):
        frontier = deque()
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
        start = [root]
        frontier.appendleft(start)

        while frontier:
            current_path = frontier.pop()
            current_node = current_path[-1]
            print(f"current node = {current_node.value}")
            if current_node.value == target:
                return current_path
            for child in current_node.children:
                print(f"child = {child.value}")
                new_path = current_path.copy()
                new_path.append(child)
                frontier.appendleft(new_path)
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