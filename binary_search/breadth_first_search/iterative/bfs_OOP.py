from collections import deque

class BFS:
    def __init__(self, value):
        self.value = value
        self.children = []

    def bfs(self, root, target):
        frontier = deque()
        start = [root]
        frontier.appendleft(start)

        while frontier:
            current_path = frontier.pop()
            current_node = current_path[-1]
            if current_node.value == target:
                return current_path
            for child in current_node.children:
                new_path = current_path.copy()
                new_path.append(child)
                frontier.appendleft(new_path)
        return None

sample_root_node = BFS("Home")
docs = BFS("Documents")
photos = BFS("Photos")

sample_root_node.children = [docs, photos]

my_wish = BFS("WishList.txt")
my_todo = BFS("TodoList.txt")
my_cat = BFS("Fluffy.jpg")
my_dog = BFS("Spot.jpg")

docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]

path_to_target = sample_root_node.bfs(sample_root_node, "Fluffy.jpg")
if not path_to_target:
    print("No path found")
else:
    print("Path found!")
    for node in path_to_target:
        print(node.value)