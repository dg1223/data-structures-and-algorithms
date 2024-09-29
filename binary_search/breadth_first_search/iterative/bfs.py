from collections import deque

class BFS:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def bfs(self, root, target):
        paths = [root]
        
        frontier = deque()
        frontier.appendleft(paths)
        
        while frontier:
            current_path = frontier.pop()
            current_node = current_path[-1]
            
            print("Traversing path:", [node.value for node in current_path])
            
            if current_node.value == target:
                return current_path
            
            for child in current_node.children:
                new_path = current_path.copy()
                new_path.append(child)
                # for each child, we have a new path to traverse   
                frontier.appendleft(new_path)
                
        return None
        
# Test
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
    print("\nNo path found")
else:
    print("\nPath found!\n")
    for node in path_to_target:
        print(node.value)