from collections import deque

def bfs(root, target):
    frontier = deque()
    paths = [root]
    frontier.appendleft(paths)

    while frontier:
        current_path = frontier.pop()
        current_node = current_path[-1]

        if current_node.value == target:
            return current_path
    
        # explore children nodes
        for child in current_node.children:
            new_path = current_path.copy()
            new_path.append(child)
            frontier.appendleft(new_path)
    return None
        